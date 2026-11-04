import json
import re
import os
import xml.etree.ElementTree as ET
import requests
from models import Entry
from utils import Cacher
from common import DATA_DIR


XML_FILENAMES = ('dstdb.xml', 'wiitdb.xml', '3dstdb.xml',
                 'wiiutdb.xml', 'ps3tdb.xml')

PLATFORM_XML = {
    'nds': 'dstdb.xml', 'dsi': 'dstdb.xml',
    'wii': 'wiitdb.xml', 'gc': 'wiitdb.xml',
    '3ds': '3dstdb.xml', 'n3ds': '3dstdb.xml',
    'wiiu': 'wiiutdb.xml', 'ps3': 'ps3tdb.xml'
}

TYPE_PLATFORM = {
    'dstdb.xml': {
        'DS': 'nds',
        'DSi': 'dsi',
        'DSiWare': 'dsi',
        'CUSTOM': 'nds'
    },
    'wiitdb.xml': {
        'GameCube': 'gc',
        'CUSTOM': 'wii',
        'Homebrew': 'wii',
        'WiiWare': 'wii',
        'Channel': 'wii'
    },
    '3dstdb.xml': {
        '3DS': '3ds',
        'None': '3ds',
        '3DSWare': '3ds',
        'New3DS': 'n3ds',
        'New3DSWare': 'n3ds',
        'Homebrew': '3ds',
        'CUSTOM': '3ds'
    },
    'wiiutdb.xml': {
        'WiiU': 'wiiu',
        'eShop': 'wiiu',
        'Channel': 'wiiu',
        'CUSTOM': 'wiiu'
    },
    'ps3tdb.xml': {
        'PS3': 'ps3',
        'CUSTOM': 'ps3',
        'SEN': 'ps3',
        'Homebrew': 'ps3'
    }
}

REGION_MAP = {
    'NTSC-U': 'us',
    'NTSC-J': 'jp',
    'PAL': 'eu',
    'NTSC-K': 'other',
    'NTSC-T': 'other',
    'PAL-R': 'other',
    'NTSC-A': 'other'
}

REGION_CODE_PATTERNS = {
    'dstdb.xml': r'.{3}(.)',
    'wiitdb.xml': r'.{3}(.)',
    '3dstdb.xml': r'.{3}(.)',
    'wiiutdb.xml': r'.{3}(.)',
    'ps3tdb.xml': r'([A-Z]{4})'
}

SERIAL_PATTERNS = {
    'nds': r'(\w{4})',
    'dsi': r'(\w{4})',
    'wii': r'(\w{4})',
    'gc': r'(\w{4})',
    '3ds': r'(\w{4})',
    'n3ds': r'(\w{4})',
    'wiiu': r'(\w{6}|\w{4})',
    'ps3': r'(\w{4}).*(\w{5})'
}

ARTWORK_PATHS = {
    'nds': 'ds/coverS',
    'dsi': 'ds/coverS',
    'wii': 'wii/cover',
    'gc': 'wii/cover',
    '3ds': '3ds/coverM',
    'n3ds': '3ds/coverM',
    'wiiu': 'wiiu/coverM',
    'ps3': 'ps3/cover'
}

REGION_COUNTRIES = {
    'dstdb.xml': {
        'E': 'US',
        'J': 'JA',
        'K': 'KO',
        'D': 'DE',
        'F': 'FR',
        'H': 'NL',
        'I': 'IT',
        'S': 'ES',
        'Z': 'SE',
        'N': 'NO',
        'Q': 'DK',
        'M': 'SE',
        'G': 'GR',
        'T': 'US',
        '': 'EN'
    },
    'wiitdb.xml': {
        'E': 'US',
        'J': 'JA',
        'D': 'DE',
        'F': 'FR',
        'S': 'ES',
        'M': 'SE',
        'Y': 'DE',
        'K': 'KO',
        'H': 'NL',
        'I': 'IT',
        'Z': 'ES',
        '': 'EN'
    },
    '3dstdb.xml': {
        'J': 'JA',
        'E': 'US',
        'K': 'KO',
        'D': 'DE',
        'W': 'ZH',
        'I': 'IT',
        'H': 'NL',
        'V': 'IT',
        '': 'EN'
    },
    'wiiutdb.xml': {
        'E': 'US',
        'J': 'JA',
        'R': 'RU',
        'A': 'JA',
        '': 'EN'
    },
    'ps3tdb.xml': {
        'BCAS': 'ZH',
        'BCAX': 'JA',
        'BCJB': 'JA',
        'BCJN': 'JA',
        'BCJS': 'JA',
        'BCJX': 'JA',
        'BCKS': 'KO',
        'BCUS': 'US',
        'BLAS': 'ZH',
        'BLJB': 'JA',
        'BLJM': 'JA',
        'BLJS': 'JA',
        'BLKS': 'KO',
        'BLMJ': 'JA',
        'BLUS': 'US',
        'CPCS': 'JA',
        'HOP3': 'JA',
        'KTGS': 'JA',
        'XCUS': 'US',
        '..J.': 'JA',
        '..U.': 'US',
        '..H.': 'US',
        '': 'EN'
    }
}

COUNTRIES = ('US', 'EN', 'JA', 'FR', 'DE', 'ES', 'IT', 'NL', 'PT',
             'NO', 'FI', 'SE', 'ZH', 'KO', 'RU', 'AU', 'DK', 'other')
ARTWORK_BASE_URL = 'https://art.gametdb.com'

artwork_cacher = Cacher('gametdb_artwork')
matches_cacher = Cacher('gametdb_matches')
databases = None
session = requests.Session()


def create_search_key(name):
    """Normalize a GameTDB name for matching."""
    name = re.sub(r'\(.*', '', name or '')
    return re.sub(r'[^a-z0-9]', '', name.lower())


def load_databases():
    """Load GameTDB XML data into memory."""
    global databases
    if databases is not None:
        return

    databases = {}
    for filename in XML_FILENAMES:
        games = []
        by_id = {}
        root = ET.parse(os.path.join(DATA_DIR, 'gametdb', filename)).getroot()
        for game in root.findall('game'):
            game_id = game.findtext('id')
            name = game.get('name') or ''
            title = game.findtext(
                'locale/title') or name.split('(', 1)[0].strip()
            item = {
                'id': game_id,
                'title': title,
                'type': game.findtext('type'),
                'region': game.findtext('region'),
                'search_key': create_search_key(name),
            }
            games.append(item)
            by_id[game_id] = item
        databases[filename] = {'games': games, 'by_id': by_id}


def find_best_match(platform, title, regions):
    """Find the closest GameTDB record for a title and region."""
    wanted = create_search_key(title)
    region_key = ','.join(sorted(regions or ()))
    cache_key = f'{platform}:{wanted}:{region_key}'
    cached = matches_cacher.get(cache_key)
    if cached is not None:
        return json.loads(cached)

    filename = PLATFORM_XML[platform]
    best = None
    for game in databases[filename]['games']:
        if platform != TYPE_PLATFORM[filename].get(game['type'], platform):
            continue
        if regions and REGION_MAP.get(game['region']) not in regions:
            continue
        if wanted not in game['search_key']:
            continue
        if not best or len(game['search_key']) < len(best['search_key']):
            best = game

    if not best:
        return {}

    match = {
        'id': best['id'],
        'title': best['title'],
        'region': best['region'],
    }
    matches_cacher.cache(
        cache_key, json.dumps(match, separators=(',', ':')).encode('utf-8'))
    return match


def find_full_id(game_id, platform):
    """Expand a partial GameTDB ID to its full ID."""
    database = databases[PLATFORM_XML[platform]]
    if game_id in database['by_id']:
        return game_id
    for game in database['games']:
        if game['id'].startswith(game_id):
            return game['id']
    return None


def get_artwork_url(game_id, platform):
    """Find and cache artwork for a GameTDB ID."""
    match = re.search(SERIAL_PATTERNS[platform], game_id or '')
    if not match:
        return None
    full_id = find_full_id(''.join(match.groups()), platform)
    if not full_id:
        return None

    filename = PLATFORM_XML[platform]
    region_match = re.match(REGION_CODE_PATTERNS[filename], full_id)
    if not region_match:
        return None
    country = next((country for pattern, country in REGION_COUNTRIES[filename].items(
    ) if re.match(pattern, region_match.group(1))), 'EN')
    cache_key = f'{platform}:{full_id}'
    cached = artwork_cacher.get(cache_key)
    if cached is not None:
        return cached.decode('utf-8') or None

    extension = 'jpg' if platform in ('3ds', 'n3ds', 'wiiu', 'ps3') else 'png'
    countries = (country,) + \
        tuple(item for item in COUNTRIES if item != country)
    for candidate in countries:
        url = f'{ARTWORK_BASE_URL}/{ARTWORK_PATHS[platform]}/{candidate}/{full_id}.{extension}'
        try:
            r = session.head(url, allow_redirects=True, timeout=5)
            r.raise_for_status()
            if r.status_code == 200:
                artwork_cacher.cache(cache_key, url.encode('utf-8'))
                return url
        except requests.RequestException:
            pass

    artwork_cacher.cache(cache_key, b'')
    return None


class GameTDBParser:
    def __init__(self, fallback=('title', 'regions')):
        """Create a GameTDB parser with fallback fields."""
        self.fallback = fallback

    def parse(self, source):
        """Enrich source entries with GameTDB titles and artwork."""
        load_databases()
        for entry in source.entries:
            platform = entry.platform or source.entry.platform
            if platform not in PLATFORM_XML:
                continue

            game = None
            if entry.serial:
                full_id = find_full_id(entry.serial, platform)
                if full_id:
                    game = databases[PLATFORM_XML[platform]
                                     ]['by_id'].get(full_id)
                    cover_url = get_artwork_url(entry.serial, platform)
                else:
                    cover_url = None
            else:
                game = find_best_match(platform, entry.title, entry.regions)
                cover_url = get_artwork_url(
                    game['id'], platform) if game else None

            if not game:
                continue

            new_entry = Entry(
                title=game['title'],
                regions=([REGION_MAP.get(game['region'])]
                         if game['region'] else None),
                serial=game['id'],
                cover_url=cover_url
            )
            entry.merge(new_entry, fallback=self.fallback)
