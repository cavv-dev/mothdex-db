import re
from models import Entry
from utils import normalize_repeated_chars

REGIONS_MAP = {
    'World': '',
    'USA': 'us',
    'Canada': 'us',
    'Mexico': 'us',
    'Europe': 'eu',
    'Australia': 'eu',
    'Italy': 'eu',
    'Germany': 'eu',
    'France': 'eu',
    'Spain': 'eu',
    'United Kingdom': 'eu',
    'UK': 'eu',
    'Netherlands': 'eu',
    'Austria': 'eu',
    'Belgium': 'eu',
    'Croatia': 'eu',
    'Denmark': 'eu',
    'Finland': 'eu',
    'Greece': 'eu',
    'Ireland': 'eu',
    'Poland': 'eu',
    'Portugal': 'eu',
    'Sweden': 'eu',
    'Turkey': 'eu',
    'Japan': 'jp',
    'Argentina': 'other',
    'Brazil': 'other',
    'China': 'other',
    'Hong Kong': 'other',
    'India': 'other',
    'Israel': 'other',
    'Korea': 'other',
    'Latin America': 'other',
    'New Zealand': 'other',
    'Norway': 'other',
    'Russia': 'other',
    'Scandinavia': 'other',
    'South Africa': 'other',
    'Switzerland': 'other',
    'Taiwan': 'other',
    'United Arab Emirates': 'other',
    'Asia': 'other',
    'Unknown': 'other'
}

LANGUAGES = (
    'En', 'Ja', 'Fr', 'De', 'Es', 'It', 'Nl', 'Pt', 'Sv', 'No', 'Da', 'Fi',
    'Zh', 'Ko', 'Pl', 'Ru', 'Cs', 'Hu', 'Zh-Hant', 'Zh-Hans', 'El', 'Es-XL',
    'Pt-BR', 'Tr', 'En-GB', 'Ar', 'En+En', 'It+En', 'Ro', 'Af', 'Hr', 'Sk',
    'Sl', 'Th', 'Mk', 'Id', 'Lt', 'Sr', 'Et', 'Lv', 'Sq', 'Bg', 'Pt-PT',
    'Fr-CA', 'Fr+En', 'Uk', 'Gd', 'He', 'Hi', 'Hy', 'La', 'Vi', 'Ca', 'Kw'
)

TITLE_REMOVE_LIST = (
    'Europe', 'USA', 'Japan', 'World'
) + LANGUAGES

WORD_ARTICLES = (
    # English
    'the', 'a', 'an',
    # German
    'der', 'die', 'das', 'ein', 'eine',
    # French
    'le', 'la', 'les', 'l\'', 'un', 'une', 'des',
    # Italian
    'il', 'lo', 'i', 'gli', 'uno', 'una', 'un\'',
    # Spanish
    'el', 'los', 'las', 'unos', 'unas',
    # Portuguese
    'o', 'os', 'as', 'um', 'uma',
    # Dutch
    'de', 'het', 'een',
    # Scandinavian
    'en', 'et', 'den', 'det',
    # Greek
    'to', 'ta'
)


def parse_regions(title):
    """Extract known regions from a title."""
    # Extract all groups of parentheses from the title
    matches = re.findall(r"\((.*?)\)", title)

    # Split the contents of each parentheses group into subgroups
    groups = [group.split(',') for group in matches]

    regions = []
    for group in groups:
        for content in group:
            content = content.strip()
            region = REGIONS_MAP.get(content)
            if region and region not in regions:
                regions.append(region)
        # Stop processing further groups if regions are found
        if regions:
            break

    return regions


def remove_groups_with_contents(title, contents_to_remove):
    """Remove parenthesized groups containing selected text."""
    # Construct a regex pattern to match parentheses groups containing any of the specified contents
    contents_pattern = '|'.join(contents_to_remove)
    pattern = rf"\((?:{contents_pattern})(?:,(?:{contents_pattern}))*\)"

    return re.sub(pattern, '', title)


def move_article(title):
    """Move a trailing title article to the beginning."""
    # Match the title structure: main name, article, and optional extra info
    match = re.match(r'^(.*?),\s*(\S+)(?:\s+(.*))?$', title)

    if match:
        name = match.group(1)
        # Avoid changes if the main name contains parentheses (to prevent false positives)
        if '(' in name:
            return title

        article = match.group(2)
        if article.lower() not in WORD_ARTICLES:
            return title

        other = match.group(3)
        # Construct the final title
        if other:
            if article.endswith("'"):
                return f'{article}{name} {other}'
            return f'{article} {name} {other}'
        else:
            if article.endswith("'"):
                return f'{article}{name}'
            return f'{article} {name}'

    return title


def get_clean_title(title):
    """Remove unwanted groups and return a clean title with extras."""
    clean_title = title
    extras = []

    # Extract all groups of parentheses from the title
    matches = re.findall(r'\((.*?)\)', title)

    # Split the contents of each parentheses group into subgroups
    groups = [group.split(',') for group in matches]

    # Remove parentheses groups if they match specific criteria
    for group in groups:
        remove_group = True
        for content in group:
            content = content.strip()
            if content not in REGIONS_MAP and content not in LANGUAGES and content not in TITLE_REMOVE_LIST:
                remove_group = False
                break
            if content in REGIONS_MAP and content not in TITLE_REMOVE_LIST:
                remove_group = False
                break
        if remove_group:
            for content in group:
                content = content.strip()
                if content not in REGIONS_MAP:
                    extras.append(content)
            clean_title = remove_groups_with_contents(clean_title, group)

    # Normalize repeated spaces and move articles
    clean_title = normalize_repeated_chars(clean_title, ' ')

    return clean_title, extras


class NoIntroParser:
    def __init__(self, parse_title_regions=True, clean_title_contents=True, move_title_article=True, fallback=()):
        """Create a No-Intro parser with title cleanup options and fallback fields."""
        self.parse_title_regions = parse_title_regions
        self.clean_title_contents = clean_title_contents
        self.move_title_article = move_title_article
        self.fallback = fallback

    def parse(self, source):
        """Clean source titles and add parsed regions and extras."""
        for entry in source.entries:
            title = entry.title
            regions = entry.regions
            extras = []

            if self.parse_title_regions:
                regions = parse_regions(title)
            if self.clean_title_contents:
                title, extras = get_clean_title(title)
            if self.move_title_article:
                title = move_article(title)

            new_entry = Entry(
                title=title,
                regions=regions
            )
            entry.merge(new_entry, fallback=self.fallback)

            for link in entry.links:
                link.extras.extend(extras)
