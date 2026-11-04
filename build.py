import json
import sqlite3
import os
import sys
import shutil
from utils import create_slug, create_db_search_key, sync_and_move_dirs
from sources import SOURCES
from platforms import PLATFORMS
from models import Index
from parsers.torrent import TorrentParser
from common import TEMP_DIR, TEMP_PROXY_DIR, TEMP_TORRENTS_DIR, TEMP_TORRENTS_MAP_PATH, TEMP_STATIC_FILES_DIR
from scripts.download_gametdb_xmls import download_gametdb_xmls
from scripts.download_igdb import download_igdb
from scripts.download_libretro_dats import download_libretro_dats
from scripts.download_mame_hashes import download_mame_hashes

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_NAME = os.path.join(BASE_DIR, 'roms.db')
DB_TEMP_NAME = os.path.join(BASE_DIR, 'roms_temp.db')
DB_OLD_NAME = os.path.join(BASE_DIR, 'roms_old.db')

REGIONS = {
    'eu': 'Europe',
    'us': 'USA',
    'jp': 'Japan',
    'other': 'Other'
}

entries_map = {}


def init_db():
    """Create the database and its initial reference data."""
    if os.path.exists(DB_TEMP_NAME):
        os.remove(DB_TEMP_NAME)

    with sqlite3.connect(DB_TEMP_NAME) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute('PRAGMA foreign_keys = ON;')

            cursor.execute('''
                CREATE TABLE platforms (
                    id TEXT PRIMARY KEY,
                    class TEXT,
                    brand TEXT,
                    name TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE entries (
                    slug TEXT PRIMARY KEY,
                    search_key TEXT,
                    title TEXT,
                    platform TEXT,
                    serial TEXT,
                    cover_url TEXT,
                    FOREIGN KEY (platform) REFERENCES platforms (id)
                )
            ''')

            cursor.execute('''
                CREATE VIRTUAL TABLE entries_fts USING fts5(
                    search_key,
                    content='entries',
                    content_rowid='rowid'
                )
            ''')

            cursor.execute('''
                CREATE TABLE regions (
                    id TEXT PRIMARY KEY,
                    name TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE regions_entries (
                    entry TEXT,
                    region TEXT,
                    FOREIGN KEY (entry) REFERENCES entries (slug),
                    FOREIGN KEY (region) REFERENCES regions (id)
                )
            ''')

            cursor.execute('''
                CREATE TABLE links (
                    id INTEGER PRIMARY KEY,
                    entry TEXT,
                    type TEXT,
                    format TEXT,
                    filename TEXT,
                    url TEXT,
                    size INTEGER,
                    size_str TEXT,
                    source_name TEXT,
                    source_url TEXT,
                    FOREIGN KEY (entry) REFERENCES entries (slug)
                )
            ''')

            cursor.execute('''
                CREATE TABLE extras_links (
                    link INTEGER,
                    extra TEXT,
                    FOREIGN KEY (link) REFERENCES links (id)
                )
            ''')

            cursor.execute(
                'CREATE INDEX idx_entries_platform ON entries (platform);')
            cursor.execute(
                'CREATE INDEX idx_regions_entries_entry ON regions_entries (entry);')
            cursor.execute(
                'CREATE INDEX idx_regions_entries_region ON regions_entries (region);')
            cursor.execute('CREATE INDEX idx_links_entry ON links (entry);')
            cursor.execute(
                'CREATE INDEX idx_extras_links_link ON extras_links (link);')

            for id, info in PLATFORMS.items():
                cursor.execute('INSERT INTO platforms (id, class, brand, name) VALUES (?, ?, ?, ?)', (
                    id, info['class'], info['brand'], info['name']))

            for id, name in REGIONS.items():
                cursor.execute(
                    'INSERT INTO regions (id, name) VALUES (?, ?)', (id, name))
    conn.close()


def add_entries():
    """Add collected entries to the database."""
    with sqlite3.connect(DB_TEMP_NAME) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute('PRAGMA foreign_keys = ON;')

            def entry_rows():
                for slug, entry in entries_map.items():
                    search_key = create_db_search_key(entry.title)
                    yield (slug, search_key, entry.title, entry.platform, entry.serial, entry.cover_url)

            def region_rows():
                for slug, entry in entries_map.items():
                    for region in entry.regions:
                        yield (slug, region)

            def link_rows():
                for slug, entry in entries_map.items():
                    for link in entry.links:
                        yield (link.id, slug, link.type, link.format, link.filename, link.url, link.size, link.size_str, link.source_name, link.source_url)

            def extra_rows():
                for entry in entries_map.values():
                    for link in entry.links:
                        for extra in link.extras:
                            yield (link.id, extra)

            cursor.executemany('''
                INSERT INTO entries (slug, search_key, title, platform, serial, cover_url)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', entry_rows())
            cursor.execute('''
                INSERT INTO entries_fts (rowid, search_key)
                SELECT rowid, search_key
                FROM entries
            ''')
            cursor.executemany('''
                INSERT INTO regions_entries (entry, region)
                VALUES (?, ?)
            ''', region_rows())
            cursor.executemany('''
                INSERT INTO links (id, entry, type, format, filename, url, size, size_str, source_name, source_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', link_rows())
            cursor.executemany('''
                INSERT INTO extras_links (link, extra)
                VALUES (?, ?)
            ''', extra_rows())
    conn.close()


if __name__ == '__main__':
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    download_data = '--download-data' in args
    use_cached = '--use-cached' in args

    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    for dir in (TEMP_DIR, TEMP_PROXY_DIR, TEMP_TORRENTS_DIR, TEMP_STATIC_FILES_DIR):
        os.makedirs(dir, exist_ok=True)

    TorrentParser.set_torrent_key_secret(config['torrent_map_secret_key'])

    if download_data:
        print("Downloading data.")
        download_igdb(config['igdb_client_id'], config['igdb_client_secret'])
        download_libretro_dats()
        download_gametdb_xmls()
        download_mame_hashes()

    if use_cached:
        print("Using cached indexes.")

    print("Scraping sources.")
    for i, source in enumerate(SOURCES, start=1):
        print(f"{str(i)}) [{source.entry.platform}]")
        source.scrape(use_cached)

    print("Preparing entries.")
    for source in SOURCES:
        for entry in source.entries:
            slug = create_slug(entry)
            if slug in entries_map:
                entries_map[slug].merge(entry)
            else:
                entries_map[slug] = entry
        source.entries.clear()

    Index.cacher.release()

    print("Making database.")
    init_db()
    add_entries()

    if os.path.exists(DB_NAME):
        shutil.copy2(DB_NAME, DB_OLD_NAME)
    os.replace(DB_TEMP_NAME, DB_NAME)

    print("Saving torrent map.")
    with open(TEMP_TORRENTS_MAP_PATH, 'w') as f:
        json.dump(TorrentParser.torrent_map, f)

    print("Moving proxy data and static files.")
    sync_and_move_dirs(TEMP_PROXY_DIR, config['proxy_dir'])
    sync_and_move_dirs(TEMP_STATIC_FILES_DIR, config['static_files_dir'])

    print("Done.")
