import html
import re
from models import Index, Entry, Link
from utils import size_str_to_bytes, join_urls

ROW_PATTERN = re.compile(
    r'<tr.*?>.*?<td><a href="(.*?)">(.*?)</a>.*?</td>.*?<td>.*?</td>.*?<td>(.*?)</td>.*?</tr>',
    re.DOTALL
)


class InternetArchiveParser:
    def parse(self, source):
        """Parse Internet Archive directory listings into entries."""
        entries = []
        indexes = source.indexes

        while indexes:
            index = indexes.pop()
            matches = ROW_PATTERN.findall(index.text)

            for url, title, size_str in matches:
                if url == '../' or 'Go to parent directory' in title:
                    continue

                url = join_urls(index.url, url)

                if index.recursive and url.endswith('/'):
                    new_index = Index(url=url)
                    new_index.fetch()
                    indexes.append(new_index)
                    continue

                title = html.unescape(title)
                filename = title
                size = size_str_to_bytes(size_str)
                if size < 1:
                    continue

                link = Link()
                link.merge(
                    Link(
                        source_name='Internet Archive',
                        source_url=index.url
                    ),
                    source.link,
                    index.link,
                    Link(
                        filename=filename,
                        url=url,
                        size=size,
                        size_str=size_str
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
