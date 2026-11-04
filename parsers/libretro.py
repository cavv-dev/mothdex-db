import re
import os
import requests
from urllib.parse import quote, unquote
from models import Entry
from utils import remove_ext
from common import DATA_DIR

PLATFORMS = {
    'nes': {
        'system': 'Nintendo - Nintendo Entertainment System',
        'dats': [
            'metadat/no-intro/Nintendo - Nintendo Entertainment System.dat',
            'dat/Nintendo - Nintendo Entertainment System.dat'
        ]
    },
    'fds': {
        'system': 'Nintendo - Family Computer Disk System',
        'dats': [
            'metadat/no-intro/Nintendo - Family Computer Disk System.dat'
        ]
    },
    'snes': {
        'system': 'Nintendo - Super Nintendo Entertainment System',
        'dats': [
            'metadat/no-intro/Nintendo - Super Nintendo Entertainment System.dat',
            'dat/Nintendo - Super Nintendo Entertainment System.dat'
        ]
    },
    'gb': {
        'system': 'Nintendo - Game Boy',
        'dats': [
            'metadat/no-intro/Nintendo - Game Boy.dat'
        ]
    },
    'gbc': {
        'system': 'Nintendo - Game Boy Color',
        'dats': [
            'metadat/no-intro/Nintendo - Game Boy Color.dat'
        ]
    },
    'gba': {
        'system': 'Nintendo - Game Boy Advance',
        'dats': [
            'metadat/no-intro/Nintendo - Game Boy Advance.dat'
        ]
    },
    'pmin': {
        'system': 'Nintendo - Pokemon Mini',
        'dats': [
            'metadat/no-intro/Nintendo - Pokemon Mini.dat'
        ]
    },
    'vb': {
        'system': 'Nintendo - Virtual Boy',
        'dats': [
            'metadat/no-intro/Nintendo - Virtual Boy.dat'
        ]
    },
    'n64': {
        'system': 'Nintendo - Nintendo 64',
        'dats': [
            'metadat/no-intro/Nintendo - Nintendo 64.dat'
        ]
    },
    '64dd': {
        'system': 'Nintendo - Nintendo 64DD',
        'dats': [
            'metadat/no-intro/Nintendo - Nintendo 64DD.dat'
        ]
    },
    'gc': {
        'system': 'Nintendo - GameCube',
        'dats': [
            'metadat/redump/Nintendo - GameCube.dat',
            'dat/Nintendo - GameCube.dat'
        ]
    },
    'nds': {
        'system': 'Nintendo - Nintendo DS',
        'dats': [
            'metadat/no-intro/Nintendo - Nintendo DS.dat',
            'metadat/no-intro/Nintendo - Nintendo DS (Download Play).dat'
        ]
    },
    'dsi': {
        'system': 'Nintendo - Nintendo DSi',
        'dats': [
            'metadat/no-intro/Nintendo - Nintendo DSi.dat'
        ]
    },
    'wii': {
        'system': 'Nintendo - Wii',
        'dats': [
            'metadat/redump/Nintendo - Wii.dat',
            'dat/Nintendo - Wii.dat',
        ]
    },
    '3ds': {
        'system': 'Nintendo - Nintendo 3DS',
        'dats': [
            'metadat/no-intro/Nintendo - Nintendo 3DS.dat',
            'metadat/no-intro/Nintendo - Nintendo 3DS (Digital).dat'
        ]
    },
    'n3ds': {
        'system': 'Nintendo - Nintendo 3DS',
        'dats': [
            'metadat/no-intro/Nintendo - New Nintendo 3DS.dat',
            'metadat/no-intro/Nintendo - New Nintendo 3DS (Digital).dat'
        ]
    },
    'wiiu': {
        'system': 'Nintendo - Wii U',
        'dats': [
            'dat/Nintendo - Wii U.dat'
        ]
    },
    'ps1': {
        'system': 'Sony - PlayStation',
        'dats': [
            'metadat/redump/Sony - PlayStation.dat'
        ]
    },
    'ps2': {
        'system': 'Sony - PlayStation 2',
        'dats': [
            'metadat/redump/Sony - PlayStation 2.dat'
        ]
    },
    'psp': {
        'system': 'Sony - PlayStation Portable',
        'dats': [
            'metadat/redump/Sony - PlayStation Portable.dat',
            'metadat/no-intro/Sony - PlayStation Portable.dat',
            'metadat/no-intro/Sony - PlayStation Portable (PSN).dat',
            'metadat/no-intro/Sony - PlayStation Portable (PSX2PSP).dat',
            'metadat/no-intro/Sony - PlayStation Portable (UMD Music).dat',
            'metadat/no-intro/Sony - PlayStation Portable (UMD Video).dat',
            'dat/Sony - PlayStation Minis.dat'
        ]
    },
    'ps3': {
        'system': 'Sony - PlayStation 3',
        'dats': [
            'metadat/no-intro/Sony - PlayStation 3 (PSN).dat',
            'dat/Sony - PlayStation 3.dat'
        ]
    },
    'psv': {
        'system': 'Sony - PlayStation Vita',
        'dats': [
            'metadat/no-intro/Sony - PlayStation Vita.dat',
            'metadat/no-intro/Sony - PlayStation Vita (PSN).dat'
        ]
    },
    'xbox': {
        'system': 'Microsoft - Xbox',
        'dats': [
            'metadat/redump/Microsoft - Xbox.dat'
        ]
    },
    'x360': {
        'system': 'Microsoft - Xbox 360',
        'dats': [
            'metadat/redump/Microsoft - Xbox 360.dat',
            'metadat/no-intro/Microsoft - Xbox 360.dat',
            'metadat/no-intro/Microsoft - Xbox 360 (Digital).dat'
        ]
    },
    'sms': {
        'system': 'Sega - Master System - Mark III',
        'dats': [
            'metadat/no-intro/Sega - Master System - Mark III.dat'
        ]
    },
    'gg': {
        'system': 'Sega - Game Gear',
        'dats': [
            'metadat/no-intro/Sega - Game Gear.dat'
        ]
    },
    'md': {
        'system': 'Sega - Mega Drive - Genesis',
        'dats': [
            'metadat/no-intro/Sega - Mega Drive - Genesis.dat'
        ]
    },
    'scd': {
        'system': 'Sega - Mega-CD - Sega CD',
        'dats': [
            'metadat/redump/Sega - Mega-CD - Sega CD.dat'
        ]
    },
    '32x': {
        'system': 'Sega - 32X',
        'dats': [
            'metadat/no-intro/Sega - 32X.dat'
        ]
    },
    'sat': {
        'system': 'Sega - Saturn',
        'dats': [
            'metadat/redump/Sega - Saturn.dat',
            'dat/Sega - Saturn.dat'
        ]
    },
    'dc': {
        'system': 'Sega - Dreamcast',
        'dats': [
            'metadat/redump/Sega - Dreamcast.dat'
        ]
    },
    'mame': {
        'system': 'MAME',
        'dats': [
            'metadat/mame/MAME.dat'
        ]
    },
    'fbn': {
        'system': 'FBNeo - Arcade Games',
        'dats': [
            'metadat/fbneo-member/FBNeo - Arcade Games.dat'
        ]
    },
    'hbmame': {
        'system': 'HBMAME',
        'dats': [
            'dat/HBMAME.dat'
        ]
    },
    'dos': {
        'system': 'DOS',
        'dats': [
            'dat/DOS.dat'
        ]
    },
    'a26': {
        'system': 'Atari - 2600',
        'dats': [
            'metadat/no-intro/Atari - 2600.dat'
        ]
    },
    'a52': {
        'system': 'Atari - 5200',
        'dats': [
            'metadat/no-intro/Atari - 5200.dat'
        ]
    },
    'a78': {
        'system': 'Atari - 7800',
        'dats': [
            'metadat/no-intro/Atari - 7800.dat'
        ]
    },
    'lynx': {
        'system': 'Atari - Lynx',
        'dats': [
            'metadat/no-intro/Atari - Lynx.dat'
        ]
    },
    'jag': {
        'system': 'Atari - Jaguar',
        'dats': [
            'metadat/no-intro/Atari - Jaguar.dat'
        ]
    },
    'jcd': {
        'system': 'Atari - Jaguar CD',
        'dats': [
            'metadat/redump/Atari - Jaguar CD.dat'
        ]
    },
    'tg16': {
        'system': 'NEC - PC Engine - TurboGrafx 16',
        'dats': [
            'metadat/no-intro/NEC - PC Engine - TurboGrafx 16.dat'
        ]
    },
    'tgcd': {
        'system': 'NEC - PC Engine CD - TurboGrafx-CD',
        'dats': [
            'metadat/redump/NEC - PC Engine CD - TurboGrafx-CD.dat'
        ]
    },
    'pcfx': {
        'system': 'NEC - PC-FX',
        'dats': [
            'metadat/redump/NEC - PC-FX.dat'
        ]
    },
    'pc98': {
        'system': 'NEC - PC-98',
        'dats': [
            'metadat/redump/NEC - PC-98.dat',
            'dat/NEC - PC-98.dat'
        ]
    },
    'intv': {
        'system': 'Mattel - Intellivision',
        'dats': [
            'metadat/no-intro/Mattel - Intellivision.dat'
        ]
    },
    'cv': {
        'system': 'Coleco - ColecoVision',
        'dats': [
            'metadat/no-intro/Coleco - ColecoVision.dat'
        ]
    },
    '3do': {
        'system': 'The 3DO Company - 3DO',
        'dats': [
            'metadat/redump/The 3DO Company - 3DO.dat'
        ]
    },
    'cdi': {
        'system': 'Philips - CD-i',
        'dats': [
            'metadat/redump/Philips - CD-i.dat'
        ]
    },
    'ngcd': {
        'system': 'SNK - Neo Geo CD',
        'dats': [
            'metadat/redump/SNK - Neo Geo CD.dat'
        ]
    }
}

databases = {}
session = requests.Session()


def normalize_serial(platform, serial):
    """Transform a serial number for a platform into a more generic format (compatible with GameTDB)."""
    if not serial:
        return serial

    if platform == 'ps3':
        return re.sub(r'^([A-Z]{4})-(\d{5})$', r'\1\2', serial)

    if platform == 'wii':
        serial = re.sub(r'^RVL-', '', serial)
        return re.sub(r'^([A-Z0-9]{4})(?:-[^-]+(?:-.*)?|[A-Z0-9]{2})?$', r'\1', serial)

    if platform in ('nds', 'dsi'):
        return re.sub(r'^(?:NTR|TWL)-', '', serial)

    if platform in ('3ds', 'n3ds'):
        return re.sub(r'^[^-]+-[^-]+-([A-Z0-9]{4})$', r'\1', serial)

    if platform == 'gc':
        return re.sub(r'^[^-]+-[^-]+-([^-]+)-.*$', r'\1', serial)

    return serial


def load_databases():
    """Load Libretro DAT files and build lookup maps."""
    for platform, data in PLATFORMS.items():
        databases[platform] = {}

        db = []
        for dat_filename in data['dats']:
            with open(os.path.join(DATA_DIR, 'libretro', dat_filename), encoding='utf-8') as f:
                text = f.read()

            for block in re.findall(r'^game \(\n(.*?)^\)', text, re.S | re.M):
                name = re.search(r'^\s*name\s+"(.*?)"', block, re.M)
                serial = re.search(r'^\s*serial\s+"(.*?)"', block, re.M)
                rom = re.search(r'rom \(\s*name\s+(?:"(.*?)"|(\S+))', block)
                db.append({
                    'name': name.group(1) if name else None,
                    'serial': normalize_serial(platform, serial.group(1)) if serial else None,
                    'rom_name': remove_ext((rom.group(1) or rom.group(2))) if rom else None,
                })

        by_name = {}
        by_serial = {}
        by_rom_name = {}

        for db_entry in db:
            by_name.setdefault(db_entry['name'], db_entry)
            by_rom_name.setdefault(db_entry['rom_name'], db_entry)
            if db_entry['serial']:
                by_serial.setdefault(db_entry['serial'], db_entry)

        databases[platform]['by_name'] = by_name
        databases[platform]['by_serial'] = by_serial
        databases[platform]['by_rom_name'] = by_rom_name


class LibretroParser:
    def __init__(self, fallback=()):
        """Create a Libretro parser with fallback fields."""
        self.fallback = fallback

    def parse(self, source):
        """Enrich source entries with Libretro metadata and artwork."""
        if not databases:
            load_databases()

        for entry in source.entries:
            db = databases[entry.platform]
            lookup_serial = normalize_serial(entry.platform, entry.serial)

            db_entry = (db['by_name'].get(entry.title) or db['by_rom_name'].get(
                entry.title) or db['by_serial'].get(lookup_serial))

            if not db_entry:
                continue

            title = None
            serial = None
            cover_url = None

            db_entry_name = db_entry.get('name')
            db_entry_serial = db_entry.get('serial')
            db_entry_rom_name = db_entry.get('rom_name')

            serial = db_entry_serial

            if entry.platform in ('mame', 'fbn', 'hbmame'):
                if not db_entry_serial and entry.title == db_entry_rom_name:
                    serial = db_entry_rom_name
                title = db_entry_name

            index_url = f"https://thumbnails.libretro.com/{quote(PLATFORMS[entry.platform]['system'])}/Named_Boxarts/"

            if not 'available_boxarts' in PLATFORMS[entry.platform]:
                PLATFORMS[entry.platform]['available_boxarts'] = []
                r = session.get(index_url)
                if not r.ok:
                    continue
                r.raise_for_status()

                results = re.findall(
                    r'<tr>.*alt="\[IMG\]".*?href="(.*?)".*?>.*?</tr>', r.text)
                for result in results:
                    PLATFORMS[entry.platform]['available_boxarts'].append(
                        remove_ext(unquote(result)))

            if db_entry_name in PLATFORMS[entry.platform]['available_boxarts']:
                cover_url = f'{index_url}{quote(db_entry_name)}.png'

            new_entry = Entry(
                title=title,
                serial=serial,
                cover_url=cover_url,
            )
            entry.merge(new_entry, fallback=self.fallback)
