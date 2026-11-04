import os

DATA_DIR = 'data'
TEMP_DIR = 'temp'
TEMP_PROXY_DIR = os.path.join(TEMP_DIR, 'proxy')
TEMP_TORRENTS_DIR = os.path.join(TEMP_PROXY_DIR, 'torrents')
TORRENT_MAP_FILENAME = 'torrent_map.json'
TEMP_TORRENTS_MAP_PATH = os.path.join(TEMP_PROXY_DIR, TORRENT_MAP_FILENAME)
TEMP_STATIC_FILES_DIR = os.path.join(TEMP_DIR, 'static')
