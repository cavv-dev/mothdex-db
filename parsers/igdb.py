import json
import re
import os
from models import Entry
from utils import Cacher
from common import DATA_DIR

databases = None
platform_ids = None
matches_cacher = Cacher('igdb_matches')


def create_search_key(title):
    """Normalize a game title for IGDB matching."""
    title = re.sub(r'\(.*', '', title)
    return re.sub(r'[^a-z0-9]', '', title.lower())


def load_databases():
    """Load IGDB data and prepare its search indexes."""
    global databases, platform_ids

    if databases is not None:
        return

    with open(os.path.join(DATA_DIR, 'igdb', 'dbs.json'), encoding='utf-8') as f:
        saved_databases = json.load(f)

    if 'platforms' in saved_databases and 'data' in saved_databases:
        platform_ids = saved_databases['platforms']
        databases = saved_databases['data']
    else:
        platform_ids = {platform: platform for platform in saved_databases}
        databases = saved_databases

    for database in databases.values():
        for game in database['games']:
            game['search_key'] = create_search_key(game['name'])
        database['games'].sort(key=lambda game: len(game['search_key']))
        # Join search keys into a single string for fast substring search
        database['search_string'] = '\x00'.join(
            game['search_key'] for game in database['games'])


def find_best_match(platform_id, title):
    """Find the first matching IGDB game for a platform and title."""
    cache_key = f'{platform_id}:{title}'
    cached = matches_cacher.get(cache_key)
    if cached is not None:
        return json.loads(cached)

    title_values = [create_search_key(title)]
    title_without_prefix = title.split('-', 1)[0].strip()
    if title_without_prefix and title_without_prefix != title.strip():
        title_values.append(create_search_key(title_without_prefix))

    database = databases[str(platform_id)]
    search_string = database['search_string']

    for title_value in title_values:
        if not title_value:
            continue
        idx = search_string.find(title_value)
        if idx != -1:
            game_idx = search_string.count('\x00', 0, idx)
            game = database['games'][game_idx]
            match = {
                'title': game['name'],
                'cover': game['cover']
            }
            matches_cacher.cache(
                cache_key, json.dumps(match, separators=(',', ':')).encode('utf-8'))
            return match

    return {}


class IGDBParser:
    def __init__(self, fallback=('title', 'cover_url')):
        """Create an IGDB parser with fallback fields."""
        self.fallback = fallback

    def parse(self, source):
        """Enrich source entries with IGDB titles and cover art."""
        load_databases()

        for entry in source.entries:
            platform_id = platform_ids[entry.platform or source.entry.platform]
            match = find_best_match(platform_id, entry.title)
            if not match:
                continue

            title = match['title']
            cover_url = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{match['cover']}.jpg"

            new_entry = Entry(
                title=title,
                cover_url=cover_url
            )
            entry.merge(new_entry, fallback=self.fallback)
