#!/usr/bin/env python
import json
import os
import requests
from common import DATA_DIR

PLATFORM_ID_MAP = {
    'nes': 18,
    'fds': 51,
    'snes': 19,
    'gb': 33,
    'gbc': 22,
    'gba': 24,
    'pmin': 166,
    'vb': 87,
    'n64': 4,
    '64dd': 416,
    'gc': 21,
    'nds': 20,
    'dsi': 159,
    'wii': 5,
    '3ds': 37,
    'n3ds': 137,
    'wiiu': 41,
    'ps1': 7,
    'ps2': 8,
    'psp': 38,
    'ps3': 9,
    'psv': 46,
    'xbox': 11,
    'x360': 12,
    'sms': 64,
    'gg': 35,
    'md': 29,
    'scd': 78,
    '32x': 30,
    'sat': 32,
    'dc': 23,
    'mame': 52,
    'fbn': 52,
    'hbmame': 52,
    'fbeat': 52,
    'm2': 52,
    's573': 52,
    'sgv': 52,
    'eamu': 52,
    'tri': 52,
    's246': 52,
    'chih': 52,
    'lind': 52,
    'naomi': 52,
    'naomi2': 52,
    'ring': 52,
    'ring2': 52,
    'dos': 13,
    'pc': 6,
    'mac': 14,
    'a26': 59,
    'a52': 66,
    'a78': 60,
    'lynx': 61,
    'jag': 62,
    'jcd': 410,
    'tg16': 86,
    'tgcd': 150,
    'pcfx': 274,
    'pc98': 149,
    'intv': 67,
    'cv': 68,
    '3do': 50,
    'cdi': 117,
    'fmt': 118,
    'ngcd': 136,
    'pip': 476
}


def load_games(path):
    """Load and merge saved IGDB game data."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            saved_games = json.load(f)
    except FileNotFoundError:
        saved_games = {}

    if 'platforms' in saved_games and 'data' in saved_games:
        saved_games['platforms'] = PLATFORM_ID_MAP
        return saved_games

    data = {}
    for platform, platform_data in saved_games.items():
        platform_id = PLATFORM_ID_MAP.get(platform)
        if platform_id is None:
            continue

        platform_key = str(platform_id)
        canonical_data = data.setdefault(
            platform_key, {'games': [], 'next_id': 0})
        existing_games = {
            (game.get('name'), game.get('cover'))
            for game in canonical_data['games']
        }
        for game in platform_data.get('games', []):
            game_key = (game.get('name'), game.get('cover'))
            if game_key not in existing_games:
                canonical_data['games'].append(game)
                existing_games.add(game_key)
        canonical_data['next_id'] = max(
            canonical_data['next_id'], platform_data.get('next_id', 0))

    return {'platforms': PLATFORM_ID_MAP, 'data': data}


def download_igdb(client_id, client_secret):
    """Download IGDB game data and save it locally."""
    print('Downloading IGDB game data...')
    s = requests.Session()

    r = s.post('https://id.twitch.tv/oauth2/token', params={
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    })

    r.raise_for_status()
    access_token = r.json()['access_token']
    path = os.path.join(DATA_DIR, 'igdb', 'dbs.json')
    os.makedirs(os.path.dirname(path), exist_ok=True)

    games = load_games(path)

    platforms_by_id = {}
    for platform, platform_id in PLATFORM_ID_MAP.items():
        platforms_by_id.setdefault(platform_id, []).append(platform)

    # Several local platforms can share one IGDB platform ID, so fetch each ID once
    for platform_id, platforms in platforms_by_id.items():
        platform = ', '.join(platforms)
        platform_data = games['data'].setdefault(
            str(platform_id), {'games': [], 'next_id': 0})

        print(f'{platform}: downloading...')
        while True:
            # Resume from the last ID saved locally to keep pagination restartable
            next_id = platform_data.get('next_id', 0)
            r = s.post(
                'https://api.igdb.com/v4/games',
                headers={
                    'Client-ID': client_id,
                    'Authorization': f'Bearer {access_token}'
                },
                data=(
                    'fields name, cover.image_id, alternative_names.name; '
                    f'where platforms = ({platform_id}) & cover != null & id >= {next_id}; '
                    'sort id asc; limit 500;'
                )
            )
            r.raise_for_status()
            response = r.json()

            for game in response:
                if 'name' not in game or 'cover' not in game or 'image_id' not in game['cover']:
                    continue
                platform_data['games'].append({
                    'name': game['name'],
                    'cover': game['cover']['image_id']
                })
                for alternative in game.get('alternative_names', []):
                    platform_data['games'].append({
                        'name': alternative['name'],
                        'cover': game['cover']['image_id']
                    })

            if len(response) < 500:
                platform_data['next_id'] = response[-1]['id'] + \
                    1 if response else next_id
            else:
                platform_data['next_id'] = response[-1]['id'] + 1

            with open(path, 'w', encoding='utf-8') as f:
                json.dump(games, f, ensure_ascii=False, indent=2)
            print(
                f'{platform}: saved {len(response)} API results ({len(platform_data["games"])} names).')

            if len(response) < 500:
                break

    print(f'Successfully downloaded IGDB data to {path}')
