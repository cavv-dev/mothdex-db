import csv
import io
import os
import xml.etree.ElementTree as ET
from models import Entry, Index, Link
from utils import join_urls, size_bytes_to_str
from common import TEMP_STATIC_FILES_DIR

REGIONS = {
    'US': 'us',
    'EU': 'eu',
    'JP': 'jp'
}
STATIC_URL = 'https://mothdex.net/static/content'


class NoPaystationParser:
    def make_link(self, source, index, **link_data):
        """Build a NoPayStation link from source metadata."""
        link = Link()
        link.merge(
            source.link,
            index.link,
            Link(source_name='NoPayStation', source_url=index.url),
            Link(**link_data)
        )
        return link

    def parse(self, source):
        """Parse NoPayStation package data into entries."""
        entries = []

        for index in source.indexes:
            rows = csv.DictReader(
                io.StringIO(index.text), delimiter='\t')
            for row in rows:
                package_url = row['PKG direct link']
                if not package_url.startswith('http'):
                    continue

                try:
                    size = round(float(row['File Size']))
                except (TypeError, ValueError):
                    size = 0
                if size < 1:
                    continue
                size_str = size_bytes_to_str(size)

                links = []
                if package_url.endswith('.xml'):
                    package_index = Index(url=package_url)
                    package_index.fetch()
                    root = ET.fromstring(package_index.content)
                    for number, piece in enumerate(root.findall('pieces')):
                        url = piece.attrib['url']
                        links.append(self.make_link(
                            source,
                            index,
                            type=f'{index.link.type or source.link.type} #{number}',
                            filename=url.rstrip('/').split('/')[-1],
                            url=url,
                            size=size,
                            size_str=size_str
                        ))
                else:
                    links.append(self.make_link(
                        source,
                        index,
                        filename=package_url.rstrip('/').split('/')[-1],
                        url=package_url,
                        size=size,
                        size_str=size_str
                    ))

                platform = source.entry.platform
                content_id = row.get('Content ID', '')
                if platform == 'ps3':
                    rap = row.get('RAP', '')
                    if content_id and len(rap) == 32:
                        filename = f'{content_id}.rap'
                        path = os.path.join(
                            TEMP_STATIC_FILES_DIR, 'ps3', 'raps', filename)
                        os.makedirs(os.path.dirname(path), exist_ok=True)
                        with open(path, 'wb') as fb:
                            fb.write(bytes.fromhex(rap))
                        links.append(self.make_link(
                            source,
                            index,
                            type='RAP file',
                            format='rap',
                            filename=filename,
                            url=join_urls(STATIC_URL, 'ps3', 'raps', filename),
                            size=16,
                            size_str=size_bytes_to_str(16)
                        ))
                elif platform == 'psv':
                    zrif = row.get('zRIF', '')
                    if content_id and zrif:
                        path = os.path.join(
                            TEMP_STATIC_FILES_DIR, 'psv', 'zrifs', content_id)
                        os.makedirs(os.path.dirname(path), exist_ok=True)
                        with open(path, 'w') as f:
                            f.write(zrif)
                        links.append(self.make_link(
                            source,
                            index,
                            type='ZRIF string',
                            format='string',
                            filename=content_id,
                            url=join_urls(STATIC_URL, 'psv',
                                          'zrifs', content_id),
                            size=len(zrif),
                            size_str=size_bytes_to_str(len(zrif))
                        ))

                entry = Entry(
                    title=row['Name'],
                    platform=platform,
                    regions={REGIONS.get(row['Region'], 'other')},
                    serial=row['Title ID'],
                    links=links
                )
                entry.merge(source.entry, index.entry)

                if not entry:
                    continue

                entries.append(entry)

        source.entries.extend(entries)
