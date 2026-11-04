import re
from models import Entry

TITLE_ID_PATTERN = re.compile(r'[_\[\(\{ ]{1,2}([A-Z0-9]{6})(?:\]|\)|\}).*')


class WiiRomSetByGhostwareParser:
    def __init__(self, fallback=()):
        """Create a WiiRomSetByGhostware parser with fallback fields."""
        self.fallback = fallback

    def parse(self, source):
        """Extract Wii title IDs and clean entry titles."""
        for entry in source.entries:
            match = TITLE_ID_PATTERN.search(entry.title)
            serial = match.group(1) if match else None
            title = TITLE_ID_PATTERN.sub('', entry.title).strip()

            new_entry = Entry(title=title, serial=serial)
            entry.merge(new_entry, fallback=self.fallback)
