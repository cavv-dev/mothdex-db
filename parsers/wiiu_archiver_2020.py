import re
from models import Entry


REGIONS = {
    'EUR': 'eu',
    'USA': 'us',
    'JPN': 'jp'
}

REGION_PATTERN = re.compile(r'\[([^]]*)\]')


class WiiUArchiver2020Parser:
    def __init__(self, fallback=()):
        """Create a parser for archiver_2020's Wii U entries with fallback fields."""
        self.fallback = fallback

    def parse(self, source):
        """Extract Wii U regions and link types from entry titles."""
        for entry in source.entries:
            groups = REGION_PATTERN.findall(entry.title)
            region = None

            for group in reversed(groups):
                region = REGIONS.get(group.strip().upper())
                if region:
                    break

            title = REGION_PATTERN.sub('', entry.title)
            title = re.sub(r'\s+', ' ', title).strip()

            regions = [region] if region else None
            entry.merge(Entry(title=title, regions=regions),
                        fallback=self.fallback)

            if len(groups) > 1 and groups[-1].strip().upper() not in REGIONS:
                for link in entry.links:
                    link.type = groups[-1]
