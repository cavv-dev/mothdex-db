import html
import re
from models import Entry, Link
from utils import join_urls, size_bytes_to_str

ROW_PATTERN = re.compile(
    r'<tr><td>-</td><td><a href="(.*?)">(.*?)</a></td><td>(\d+)</td><td></td><td>.*?</td><td>.*?</td>',
    re.DOTALL
)


class MarioCubeParser:
    def parse(self, source):
        """Parse MarioCube directory listings into entries."""
        entries = []

        for index in source.indexes:
            for url, title, size in ROW_PATTERN.findall(index.text):
                size = int(size)
                if size < 1:
                    continue
                title = html.unescape(title)
                filename = title
                url = join_urls(index.url, url)

                link = Link()
                link.merge(
                    Link(
                        source_name='MarioCube',
                        source_url=index.url
                    ),
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
                    Entry(title=title, links=[link])
                )

                if not entry:
                    continue

                entries.append(entry)

        source.entries.extend(entries)
