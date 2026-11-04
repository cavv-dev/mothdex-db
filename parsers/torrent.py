import libtorrent as lt
import base64
import hashlib
import hmac
import os
from models import Entry, Link
from utils import to_posix_path, size_bytes_to_str
from common import TEMP_TORRENTS_DIR


class TorrentParser:
    torrent_key_secret = None
    torrent_map = {}
    saved_torrents = set()

    def set_torrent_key_secret(key):
        """Set the secret used to sign torrent links."""
        TorrentParser.torrent_key_secret = key.encode('utf-8')

    def parse(self, source):
        """Parse torrent files into downloadable entries."""
        entries = []

        for index in source.indexes:
            decoded_data = lt.bdecode(index.content)
            info = lt.torrent_info(decoded_data)
            info_hash = str(info.info_hash())
            file_storage = info.layout()

            for i in range(file_storage.num_files()):
                file_path = to_posix_path(file_storage.file_path(i))

                index_base_path = index.base_path.rstrip(
                    '/') if index.base_path else ''
                if index_base_path:
                    if not file_path.startswith(index_base_path + '/'):
                        continue
                    relative_path = file_path[len(index_base_path) + 1:]
                else:
                    relative_path = file_path

                if not index.recursive and '/' in relative_path:
                    continue

                title = os.path.basename(file_path)
                filename = title

                size = file_storage.file_size(i)
                if size < 1:
                    continue

                identity = f'{info_hash}:{i}'.encode()
                digest = hmac.new(
                    TorrentParser.torrent_key_secret,
                    identity,
                    hashlib.sha256
                ).digest()
                key = base64.urlsafe_b64encode(digest).decode()[:10]
                url = f'https://proxy.mothdex.net/file/{key}'

                link = Link()
                link.merge(
                    source.link,
                    index.link,
                    Link(
                        filename=filename,
                        url=url,
                        size=size,
                        size_str=size_bytes_to_str(size)
                    )
                )
                entry = Entry()
                entry.merge(
                    source.entry,
                    index.entry,
                    Entry(
                        title=title,
                        links=[link]
                    )
                )

                if not entry:
                    continue

                TorrentParser.torrent_map[key] = (info_hash, i)
                entries.append(entry)

            if not info_hash in TorrentParser.saved_torrents:
                with open(os.path.join(TEMP_TORRENTS_DIR, f'{info_hash}.torrent'), 'wb') as fb:
                    fb.write(index.content)
                TorrentParser.saved_torrents.add(info_hash)

        source.entries.extend(entries)
