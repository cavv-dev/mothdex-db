from pathlib import Path
import atexit
import filecmp
import re
from unidecode import unidecode
import urllib
import requests
import base64
import os
import shutil
import json
import time


def create_db_search_key(name):
    """Create the normalized search key used by the database."""
    name = replace_invalid_chars(name)
    name = unidecode(name).lower()
    spaced = normalize_repeated_chars(
        re.sub(r'[^a-z0-9\s]', ' ', name), ' ').strip()
    solid = re.sub(r'[^a-z0-9]', '', name)

    if spaced != solid:
        return f'{spaced} {solid}'
    return spaced


def replace_invalid_chars(title):
    """Replace special title characters with searchable words."""
    for invalid, valid in {
        '+': 'plus',
        '&': 'and',
        '™': '',
        '©': '',
        '®': ''
    }.items():
        title = title.replace(invalid, f' {valid} ')
    return title


def normalize_repeated_chars(text, char):
    """Replace repeated copies of a character with one copy."""
    escaped_char = re.escape(char)
    return re.sub(rf'{escaped_char}+', char, text).strip()


def create_slug(entry):
    """Create a URL-safe slug from an entry."""
    title = entry.title

    title = replace_invalid_chars(title)
    title = unidecode(title)
    platform = entry.platform
    regions = '-'.join(entry.regions)
    slug = f'{title}-{platform}-{regions}'

    slug = re.sub(r'[^a-zA-Z0-9-]', '-', slug).lower()
    slug = normalize_repeated_chars(slug, '-').strip('-')

    return slug


def remove_ext(filename):
    """Remove a filename extension while keeping the base name."""
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)

    if ext == '':
        return filename
    return name


def size_bytes_to_str(size):
    """Format a byte count with a readable unit."""
    suffixes = ['B', 'K', 'M', 'G', 'T', 'P']
    i = 0
    while size >= 1024 and i < len(suffixes) - 1:
        size /= 1024.0
        i += 1

    f = ('%.2f' % size).rstrip('0').rstrip('.')
    return '%s%s' % (f, suffixes[i])


def size_str_to_bytes(size_str):
    """Convert a readable size string into bytes."""
    for character in size_str:
        if not character.isalpha():
            continue
        unit = character
        break

    size = float(re.sub(r'[^\d\.]', '', size_str))
    if unit == 'B':
        size = size
    elif unit == 'K':
        size = size * 1024
    elif unit == 'M':
        size = size * 1024 * 1024
    elif unit == 'G':
        size = size * 1024 * 1024 * 1024

    return int(size)


def join_urls(url, *links):
    """Join a base URL with one or more link parts."""
    for link in links:
        url = urllib.parse.urljoin(url.rstrip('/') + '/', link.lstrip('/'))
    return url


def to_posix_path(path_str):
    """Convert a path to POSIX separators."""
    if not path_str:
        return ''

    return Path(path_str.replace('\\', '/')).as_posix()


def sync_and_move_dirs(source_dir, destination_dir):
    """Synchronize destination contents, then move new source files into it."""
    if not os.path.exists(source_dir):
        return

    if os.path.abspath(os.path.normpath(source_dir)) == os.path.abspath(os.path.normpath(destination_dir)):
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for root, dirs, files in os.walk(destination_dir, topdown=False):
        rel_path = os.path.relpath(root, destination_dir)
        src_root = source_dir if rel_path == '.' else os.path.join(
            source_dir, rel_path)

        for file in files:
            dest_file = os.path.join(root, file)
            src_file = os.path.join(src_root, file)
            if not os.path.exists(src_file):
                os.remove(dest_file)

        for dir_name in dirs:
            dest_subdir = os.path.join(root, dir_name)
            rel_subpath = os.path.relpath(dest_subdir, destination_dir)
            src_subdir = os.path.join(source_dir, rel_subpath)
            if not os.path.exists(src_subdir):
                shutil.rmtree(dest_subdir)

    for root, dirs, files in os.walk(source_dir, topdown=False):
        rel_path = os.path.relpath(root, source_dir)
        dest_root = destination_dir if rel_path == '.' else os.path.join(
            destination_dir, rel_path)

        if not os.path.exists(dest_root):
            os.makedirs(dest_root)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)

            if os.path.isfile(dest_file) and filecmp.cmp(src_file, dest_file, shallow=False):
                os.remove(src_file)
                continue

            if os.path.isdir(dest_file):
                shutil.rmtree(dest_file)
            elif os.path.exists(dest_file):
                os.remove(dest_file)

            shutil.move(src_file, dest_file)


CACHE_DIR = 'cache'


class Cacher:
    def __init__(self, name):
        """Create a JSON-backed cache with the given name."""
        self.name = name
        self.cache_path = os.path.join(CACHE_DIR, f'{self.name}.json')
        self.cache_data = {}
        self.dirty = False

        os.makedirs(CACHE_DIR, exist_ok=True)

        if os.path.exists(self.cache_path):
            with open(self.cache_path, 'r') as f:
                self.cache_data = json.load(f)
        atexit.register(self.flush)

    def cache(self, key, content):
        """Store encoded content under a cache key."""
        encoded_content = base64.b64encode(content).decode('ascii')
        if self.cache_data.get(key) == encoded_content:
            return

        self.cache_data[key] = encoded_content
        self.dirty = True

    def flush(self):
        """Write changed cache data to disk."""
        if not self.dirty:
            return

        with open(self.cache_path, 'w') as f:
            json.dump(self.cache_data, f)
        self.dirty = False

    def get(self, key):
        """Return cached content for a key, or None if absent."""
        if not key in self.cache_data:
            return None
        return base64.b64decode(self.cache_data[key])

    def release(self):
        """Flush pending changes and release cached values from memory."""
        self.flush()
        self.cache_data.clear()


class HTTPFetcher:
    timeout = 30
    session = requests.Session()

    def fetch(url):
        """Fetch URL content and retry temporary request failures."""
        for attempt in range(3):
            try:
                r = HTTPFetcher.session.get(url, timeout=HTTPFetcher.timeout)
                r.raise_for_status()
                return r.content
            except requests.RequestException:
                if attempt == 2:
                    raise
                time.sleep(attempt + 1)
