import re
from unidecode import unidecode
from utils import Cacher, HTTPFetcher, remove_ext


class Link:
    next_id = 1

    def __init__(self, type=None, extras=None, format=None, filename=None, url=None, size=None, size_str=None, source_name=None, source_url=None):
        """Create a download link."""
        self.id = self.next_id
        self.type = type
        self.extras = [] if not extras else extras
        self.format = format
        self.filename = filename
        self.url = url
        self.size = size
        self.size_str = size_str
        self.source_name = source_name
        self.source_url = source_url

        Link.next_id += 1

    def merge(self, *new_links):
        """Copy available values from other links into this link."""
        for new_link in new_links:
            for field, value in vars(new_link).items():
                if value:
                    setattr(self, field, value)


class Filter:
    def __init__(self, field, pattern):
        """Create a field filter using a regular expression."""
        self.field = field
        self.pattern = pattern


class Entry:
    def __init__(self, title=None, platform=None, regions=None, serial=None, cover_url=None, links=None, source=None):
        """Create a ROM entry."""
        self._title = title
        self._platform = platform
        self.regions = set() if not regions else regions
        self._serial = serial
        self._cover_url = cover_url
        self.links = [] if not links else links
        self.source = source

    def __bool__(self):
        """Return whether the entry passes its source filters."""
        if not self.source:
            return True
        for f in self.source.filters:
            filtered_field = f'_{f.field}'
            value = getattr(self, filtered_field)
            if not value:
                return False
            match = re.match(f.pattern, value)
            if not match:
                return False
        return True

    @property
    def title(self):
        """Return the filtered title."""
        return self.get_filtered('title')

    @property
    def platform(self):
        """Return the filtered platform."""
        return self.get_filtered('platform')

    @property
    def serial(self):
        """Return the filtered serial."""
        return self.get_filtered('serial')

    @property
    def cover_url(self):
        """Return the filtered cover URL."""
        return self.get_filtered('cover_url')

    def get_filtered(self, field):
        """Return a field after applying its source filter."""
        value = getattr(self, f'_{field}')
        if not self.source:
            return value
        for f in self.source.filters:
            filtered_field = f'_{f.field}'
            if f'_{field}' != filtered_field:
                continue

            value = getattr(self, filtered_field)
            if not value:
                continue

            match = re.match(f.pattern, value)
            if not match:
                continue

            groups = match.groups()
            value = ''.join(filter(None, groups))
        return value

    def update(self, field, value):
        """Update one entry field or extend its collections."""
        if field in ('_title', '_platform', '_serial', '_cover_url', 'source'):
            setattr(self, field, value)
        elif field == 'regions':
            self.regions.update(value)
        elif field == 'links':
            self.links.extend(value)

    def merge(self, *new_entries, fallback=()):
        """Merge values from other entries, using fallbacks when requested."""
        fallback = {f'_{field}' if field in (
            'title', 'platform', 'serial', 'cover_url') else field for field in fallback}
        for new_entry in new_entries:
            for field, value in vars(new_entry).items():
                if value and ((field in fallback and not getattr(self, field)) or field not in fallback):
                    self.update(field, value)

    def generate_links_extras(self):
        """Populate `extras` field in each link by comparing filenames. Should be done once, when the entry is ready."""
        tokenized_filenames = []
        pattern = r'\(([^)]+)\)|\[([^\]]+)\]|\{([^}]+)\}|([^\s\(\)\[\]{}]+)'

        for link in self.links:
            tokens = []
            filename = unidecode(remove_ext(link.filename or ''))
            for match in re.finditer(pattern, filename):
                group_index = match.lastindex
                token = match.group(group_index)
                if group_index == 4 and re.fullmatch(r'[^a-zA-Z0-9]+', token):
                    continue
                tokens.append(token)
            tokenized_filenames.append(tokens)

        common_tokens = set(
            token.casefold() for token in tokenized_filenames[0]) if tokenized_filenames else set()
        for tokens in tokenized_filenames[1:]:
            common_tokens.intersection_update(
                token.casefold() for token in tokens)

        for link, tokens in zip(self.links, tokenized_filenames):
            link.extras = [
                token for token in tokens if token.casefold() not in common_tokens]


class Index:
    cacher = Cacher('indexes')
    use_cached = False

    def __init__(self, url=None, base_path=None, recursive=True, entry=None, link=None):
        """Create a source index."""
        self.url = url
        self.base_path = base_path
        self.recursive = recursive
        self.entry = Entry() if not entry else entry
        self.link = Link() if not link else link
        self.content = None

    @property
    def text(self):
        """Return downloaded index content as text."""
        return self.content.decode('utf-8', errors='ignore')

    def fetch(self):
        """Load index content from cache or its URL."""
        if self.use_cached:
            self.content = self.cacher.get(self.url)
        if not self.content:
            self.content = HTTPFetcher.fetch(self.url)
            self.cacher.cache(self.url, self.content)


class Source:
    def __init__(self, entry=None, link=None):
        """Create a source with a base entry, base link, parsers, and indexes."""
        self.entry = Entry() if not entry else entry
        self.entry.source = self
        self.link = Link() if not link else link
        self.indexes = []
        self.parsers = []
        self.filters = []
        self.entries = []

    def add_indexes(self, *index):
        """Add indexes to the source and return the source."""
        self.indexes.extend(index)
        return self

    def add_parsers(self, *parsers):
        """Add parsers to the source and return the source."""
        self.parsers.extend(parsers)
        return self

    def add_filters(self, *filters):
        """Add filters to the source and return the source."""
        self.filters.extend(filters)
        return self

    def scrape(self, use_cached=False):
        """Fetch source indexes and parse their entries."""
        for index in self.indexes:
            if use_cached:
                index.use_cached = use_cached
            index.fetch()
        for parser in self.parsers:
            parser.parse(self)
        for index in self.indexes:
            index.content = None
