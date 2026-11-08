import re
from models import Entry

TITLE_PATTERN = re.compile(r'^\[TH([0-9]+(?:\.[0-9]+)?(?:-[0-9]+)?)\]\s*(.+)$')


class TouhouProjectCollectionParser:
    def __init__(self, fallback=()):
        """Create a Touhou Project Collection parser with fallback fields."""
        self.fallback = fallback

    def parse(self, source):
        """Normalize Touhou Project Collection titles."""
        for entry in source.entries:
            match = TITLE_PATTERN.match(entry._title or '')
            if not match:
                continue

            number, title = match.groups()
            separator = ' ' if '-' in number else ' - '
            title = title.replace(' ~ ', ': ')
            entry.merge(
                Entry(title=f'Touhou {number}{separator}{title}'), fallback=self.fallback)
