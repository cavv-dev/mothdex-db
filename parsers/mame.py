import os
import xml.etree.ElementTree as ET
from models import Entry
from common import DATA_DIR

database = None


def load_database():
    """Load MAME software names and descriptions."""
    global database
    database = {}

    for filename in sorted(os.listdir(os.path.join(DATA_DIR, 'mame', 'hash'))):
        if not filename.endswith('.xml'):
            continue

        root = ET.parse(os.path.join(
            DATA_DIR, 'mame', 'hash', filename)).getroot()
        for software in root.findall('software'):
            name = software.get('name')
            description = software.findtext('description')
            if name and description:
                database.setdefault(name, description)


class MAMEParser:
    def __init__(self, fallback=()):
        """Create a MAME parser with fallback fields."""
        self.fallback = fallback

    def parse(self, source):
        """Replace MAME short names with database descriptions."""
        if database is None:
            load_database()

        for entry in source.entries:
            description = database.get(entry.title)
            if not description:
                continue

            new_entry = Entry(title=description, serial=entry.title)
            entry.merge(new_entry, fallback=self.fallback)
