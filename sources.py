from models import Source, Index, Entry, Filter, Link
from parsers.torrent import TorrentParser
from parsers.internet_archive import InternetArchiveParser
from parsers.mariocube import MarioCubeParser
from parsers.nopaystation import NoPaystationParser
from parsers.libretro import LibretroParser
from parsers.no_intro import NoIntroParser
from parsers.gametdb import GameTDBParser
from parsers.mame import MAMEParser
from parsers.wii_rom_set_by_ghostware import WiiRomSetByGhostwareParser
from parsers.wiiu_archiver_2020 import WiiUArchiver2020Parser
from parsers.igdb import IGDBParser
from parsers.touhou_project_collection import TouhouProjectCollectionParser

SOURCES = (
    Source(
        Entry(platform='nes'),
        Link(
            type='Game',
            format='nes',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headered%29.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headered%29/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headerless%29.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headerless%29/',
                type='Game (Headerless)'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='fds'),
        Link(
            type='Game',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Family%20Computer%20Disk%20System%20%28FDS%29.torrent',
            link=Link(
                format='fds',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Family%20Computer%20Disk%20System%20%28FDS%29/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Family%20Computer%20Disk%20System%20%28QD%29.torrent',
            link=Link(
                format='qd',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Family%20Computer%20Disk%20System%20%28QD%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='snes'),
        Link(
            type='Game',
            format='sfc',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Super%20Nintendo%20Entertainment%20System.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Super Nintendo Entertainment System',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Super%20Nintendo%20Entertainment%20System/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='gb'),
        Link(
            type='Game',
            format='gb',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Game%20Boy.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Game Boy',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Game%20Boy/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='gbc'),
        Link(
            type='Game',
            format='gbc',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Game%20Boy%20Color.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Game Boy Color',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Game%20Boy%20Color/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='gba'),
        Link(
            type='Game',
            format='gba',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Game%20Boy%20Advance.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Game Boy Advance',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Game%20Boy%20Advance/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Game%20Boy%20Advance%20%28Multiboot%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Game Boy Advance (Multiboot)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Game%20Boy%20Advance%20%28Multiboot%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Game%20Boy%20Advance%20%28Video%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Game Boy Advance (Video)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Game%20Boy%20Advance%20%28Video%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Game%20Boy%20Advance%20(e-Reader).torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Game Boy Advance (e-Reader)',
            link=Link(
                format='raw',
                type='Card data',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Game%20Boy%20Advance%20(e-Reader)/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='pmin'),
        Link(
            type='Game',
            format='pmin',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Pokemon%20Mini.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Pokemon Mini',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Pokemon%20Mini/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='vb'),
        Link(
            type='Game',
            format='vb',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Virtual%20Boy.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Virtual Boy',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Virtual%20Boy/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='n64'),
        Link(
            type='Game',
            format='z64',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%2064%20%28BigEndian%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo 64 (BigEndian)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%2064%20%28BigEndian%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%2064%20%28ByteSwapped%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo 64 (ByteSwapped)',
            link=Link(
                format='v64',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%2064%20%28ByteSwapped%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='64dd'),
        Link(
            type='Game',
            format='ndd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%2064DD.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo 64DD',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%2064DD/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='gc'),
        Link(
            type='Game',
            format='rvz',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Nintendo%20-%20GameCube%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D.torrent',
            base_path='Minerva_Myrient/Redump/Nintendo - GameCube - NKit RVZ [zstd-19-128k]',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Nintendo%20-%20GameCube%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20Unknown.torrent',
            base_path='Minerva_Myrient/Internet Archive/Unknown/RedumpNintendoGameCubeAmerica',
            link=Link(
                format='iso',
                source_url='https://minerva-archive.org/browse/Internet%20Archive/Unknown/RedumpNintendoGameCubeAmerica/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20kodi_amp_spmc_canada.torrent',
            base_path='Minerva_Myrient/Internet Archive/Unknown/RedumpNintendoGameCubeAmericaPart2',
            link=Link(
                format='iso',
                source_url='https://minerva-archive.org/browse/Internet%20Archive/Unknown/RedumpNintendoGameCubeAmericaPart2/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='gc'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20kodi_amp_spmc_canada.torrent',
            base_path='Minerva_Myrient/Internet Archive/kodi_amp_spmc_canada/EuropeanGamecubeCollectionByGhostware',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/kodi_amp_spmc_canada/EuropeanGamecubeCollectionByGhostware/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20kodi_amp_spmc_canada.torrent',
            base_path='Minerva_Myrient/Internet Archive/kodi_amp_spmc_canada/AsiaGamecubeCollectionByGhostware',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/kodi_amp_spmc_canada/AsiaGamecubeCollectionByGhostware/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(parse_title_regions=False,
                      clean_title_contents=False, move_title_article=True),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.iso')),

    Source(
        Entry(platform='gc'),
        Link(
            type='Game',
            format='iso'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/AsiaGamecubeCollectionByGhostware')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(parse_title_regions=False,
                      clean_title_contents=False, move_title_article=True),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.iso')),

    Source(
        Entry(platform='gc'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20pixelspoil.torrent',
            base_path='Minerva_Myrient/Internet Archive/pixelspoil/NCubeJ',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/pixelspoil/NCubeJ/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='gc'),
        Link(
            type='Game',
            format='iso'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/NCubeJ')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='nds'),
        Link(
            type='Game',
            format='nds',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DS%20%28Decrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DS (Decrypted)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DS%20%28Decrypted%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DS%20%28Download%20Play%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DS (Download Play)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DS%20%28Download%20Play%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DS%20%28Encrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DS (Encrypted)',
            link=Link(
                type='Game (Encrypted)',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DS%20(Encrypted)/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='dsi'),
        Link(
            type='Game',
            format='dsi',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DSi%20%28Decrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DSi (Decrypted)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DSi%20%28Decrypted%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DSi%20%28Encrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DSi (Encrypted)',
            link=Link(
                type='Game (Encrypted)',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DSi%20%28Encrypted%29/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DSi%20%28Digital%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DSi (Digital)',
            link=Link(
                format='nds',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DSi%20%28Digital%29/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DSi%20%28Digital%29%20%28CDN%29%20%28Decrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DSi (Digital) (CDN) (Decrypted)',
            link=Link(
                format='CDN',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DSi%20%28Digital%29%20%28CDN%29%20%28Decrypted%29/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%20DSi%20%28Digital%29%20%28CDN%29%20%28Encrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo DSi (Digital) (CDN) (Encrypted)',
            link=Link(
                format='CDN',
                type='Game (Encrypted)',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%20DSi%20%28Digital%29%20%28CDN%29%20%28Encrypted%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='dsi'),
        Link(
            type='Game',
            format='nds'
        )
    ).add_indexes(
        Index(url='https://repo.mariocube.com/DSiWare/NDS/%23/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/A/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/B/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/C/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/D/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/E/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/F/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/G/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/H/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/I/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/J/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/K/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/L/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/M/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/N/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/O/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/P/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/Q/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/R/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/S/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/T/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/U/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/V/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/W/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/X/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/Y/'),
        Index(url='https://repo.mariocube.com/DSiWare/NDS/Z/')
    ).add_parsers(
        MarioCubeParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.nds')),

    Source(
        Entry(platform='wii'),
        Link(
            type='Game',
            format='rvz',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Nintendo%20-%20Wii%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D.torrent',
            base_path='Minerva_Myrient/Redump/Nintendo - Wii - NKit RVZ [zstd-19-128k]',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Nintendo%20-%20Wii%20-%20NKit%20RVZ%20%5Bzstd-19-128k%5D/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Non-Redump%20-%20Nintendo%20-%20Wii.torrent',
            base_path='Minerva_Myrient/No-Intro/Non-Redump - Nintendo - Wii',
            link=Link(
                format='iso',
                source_url='https://minerva-archive.org/browse/No-Intro/Non-Redump%20-%20Nintendo%20-%20Wii/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Wii%20%28Digital%29%20%28CDN%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Wii (Digital) (CDN)',
            link=Link(
                format='CDN',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Wii%20%28Digital%29%20%28CDN%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='wii'),
        Link(
            type='Game',
            format='rvz'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/Wii-Redump-2024-Individual-Games-Part1'),
        Index(url='https://archive.org/download/Wii-Redump-2024-Individual-Games-Part2'),
        Index(url='https://archive.org/download/Wii-Redump-2024-Individual-Games-Part3'),
        Index(url='https://archive.org/download/Wii-Redump-2024-Individual-Games-Part4'),
        Index(url='https://archive.org/download/Wii-Redump-2024-Individual-Games-Part5'),
        Index(url='https://archive.org/download/Wii-Redump-2024-Individual-Games-Part6')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='wii'),
        Link(
            type='Game',
            format='wbfs',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20kodi_amp_spmc_canada.torrent',
            base_path='Minerva_Myrient/Internet Archive/kodi_amp_spmc_canada/WiiRomSetByGhostware',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/kodi_amp_spmc_canada/WiiRomSetByGhostware/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        WiiRomSetByGhostwareParser(),
        GameTDBParser(fallback=()),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.wbfs')),

    Source(
        Entry(platform='wii'),
        Link(
            type='Game',
            format='wad'
        )
    ).add_indexes(
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/0-9/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/A/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/B/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/C/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/D/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/E/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/F/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/G/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/H/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/I/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/J/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/K/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/L/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/M/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/N/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/O/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/P/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/Q/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/R/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/S/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/T/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/U/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/V/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/W/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/X/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/Y/'),
        Index(url='https://repo.mariocube.com/WADs/_WiiWare,%20VC,%20DLC,%20Channels%20&%20IOS/Z/')
    ).add_parsers(
        MarioCubeParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.wad')),

    Source(
        Entry(platform='3ds'),
        Link(
            type='Game',
            format='3ds',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%203DS%20%28Decrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo 3DS (Decrypted)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%203DS%20%28Decrypted%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%203DS%20%28Encrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo 3DS (Encrypted)',
            link=Link(
                type='Game (Encrypted)',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%203DS%20%28Encrypted%29/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Nintendo%203DS%20%28Digital%29%20%28CDN%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Nintendo 3DS (Digital) (CDN)',
            link=Link(
                format='CDN',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Nintendo%203DS%20%28Digital%29%20%28CDN%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='3ds'),
        Link(
            type='Game (Encrypted)',
            format='3ds'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/3DS-Redump-2024-Individual-Games-Part1'),
        Index(url='https://archive.org/download/3DS-Redump-2024-Individual-Games-Part2')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='n3ds'),
        Link(
            type='Game',
            format='3ds',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20New%20Nintendo%203DS%20%28Decrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - New Nintendo 3DS (Decrypted)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20New%20Nintendo%203DS%20%28Decrypted%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20New%20Nintendo%203DS%20%28Encrypted%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - New Nintendo 3DS (Encrypted)',
            link=Link(
                type='Game (Encrypted)',
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20New%20Nintendo%203DS%20%28Encrypted%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='n3ds'),
        Link(
            type='Game',
            format='3ds'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/xenoblade-chronicles-3-d-europe-en-fr-de-es-it')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='wiiu'),
        Link(
            type='Game',
            format='CDN',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Nintendo%20-%20Wii%20U%20%28Digital%29%20%28CDN%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Nintendo - Wii U (Digital) (CDN)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Nintendo%20-%20Wii%20U%20%28Digital%29%20%28CDN%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Nintendo%20-%20Wii%20U%20-%20WUX.torrent',
            base_path='Minerva_Myrient/Redump/Nintendo - Wii U - WUX',
            link=Link(
                format='wux',
                source_url='https://minerva-archive.org/browse/Redump/Nintendo%20-%20Wii%20U%20-%20WUX/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Non-Redump%20-%20Nintendo%20-%20Wii%20U.torrent',
            base_path='Minerva_Myrient/No-Intro/Non-Redump - Nintendo - Wii U',
            link=Link(
                format='wud',
                source_url='https://minerva-archive.org/browse/No-Intro/Non-Redump%20-%20Nintendo%20-%20Wii%20U/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='wiiu'),
        Link(
            type='Disc Key',
            format='key',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Nintendo%20-%20Wii%20U%20-%20Disc%20Keys.torrent',
            base_path='Minerva_Myrient/Redump/Nintendo - Wii U - Disc Keys',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Nintendo%20-%20Wii%20U%20-%20Disc%20Keys/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='wiiu'),
        Link(
            type='Game',
            format='wua',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20teamgt19.torrent',
            base_path='Minerva_Myrient/Internet Archive/teamgt19/nintendo-wii-u-usa-full-set-wua-format-embedded-dlc-updates',
            link=Link(source_url='https://minerva-archive.org/browse/Internet%20Archive/teamgt19/nintendo-wii-u-usa-full-set-wua-format-embedded-dlc-updates/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20teamgt19.torrent',
            base_path='Minerva_Myrient/Internet Archive/teamgt19/nintendo-wii-u-eshop-usa-full-set-wua-format-embedded-dlc-updates',
            link=Link(source_url='https://minerva-archive.org/browse/Internet%20Archive/teamgt19/nintendo-wii-u-eshop-usa-full-set-wua-format-embedded-dlc-updates/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.wua')),

    Source(
        Entry(platform='wiiu'),
        Link(
            type='Game',
            format='NUS',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-retail-nus-usa',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-retail-nus-usa/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-download-nus-usa',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-download-nus-usa/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-turbografx16-nus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-turbografx16-nus/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-wii-nus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-wii-nus/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-nintendo-64-nus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-nintendo-64-nus/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-nes-fc-nus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-nes-fc-nus/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-super-nintendo-snes-nus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-super-nintendo-snes-nus/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-nintendo-ds-nds-nus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-nintendo-ds-nds-nus/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-gameboy-advance-nus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-gameboy-advance-nus/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20archiver_2020.torrent',
            base_path='Minerva_Myrient/Internet Archive/archiver_2020/wii-u-retail-game-disc-nus-usa',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/archiver_2020/wii-u-retail-game-disc-nus-usa/')
        )
    ).add_parsers(
        TorrentParser(),
        WiiUArchiver2020Parser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='ps1'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sony%20-%20PlayStation.torrent',
            base_path='Minerva_Myrient/Redump/Sony - PlayStation',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Sony%20-%20PlayStation/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Non-Redump%20-%20Sony%20-%20PlayStation.torrent',
            base_path='Minerva_Myrient/No-Intro/Non-Redump - Sony - PlayStation',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Non-Redump%20-%20Sony%20-%20PlayStation/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ps1'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_psx/CHD-PSX-USA',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_psx/CHD-PSX-USA/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_psx_eur/CHD-PSX-EUR',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_psx_eur/CHD-PSX-EUR/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_psx_jap/CHD-PSX-JAP',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_psx_jap/CHD-PSX-JAP/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_psx_misc/CHD-PSX-Misc',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_psx_misc/CHD-PSX-Misc/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='ps2'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sony%20-%20PlayStation%202.torrent',
            base_path='Minerva_Myrient/Redump/Sony - PlayStation 2',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Sony%20-%20PlayStation%202/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Non-Redump%20-%20Sony%20-%20PlayStation%202.torrent',
            base_path='Minerva_Myrient/No-Intro/Non-Redump - Sony - PlayStation 2',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Non-Redump%20-%20Sony%20-%20PlayStation%202/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ps2'),
        Link(
            type='Game',
            format='iso'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part1'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part2'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part3'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part4'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part5'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part6'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part7'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part8'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part9'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part10'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part11'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part12'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part13'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part14'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part15'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part16'),
        Index(url='https://archive.org/download/PS2-Redump-2024-Individual-Games-Part17')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='psp'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sony%20-%20PlayStation%20Portable.torrent',
            base_path='Minerva_Myrient/Redump/Sony - PlayStation Portable',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Sony%20-%20PlayStation%20Portable/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Non-Redump%20-%20Sony%20-%20PlayStation%20Portable.torrent',
            base_path='Minerva_Myrient/No-Intro/Non-Redump - Sony - PlayStation Portable',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Non-Redump%20-%20Sony%20-%20PlayStation%20Portable/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='psp'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/psp-chd-zstd-redump-part1/psp-chd-zstd',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/psp-chd-zstd-redump-part1/psp-chd-zstd/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='psp'),
        Link(
            type='Game',
            format='chd'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/psp-chd-zstd-redump-part1/psp-chd-zstd/'),
        Index(url='https://archive.org/download/psp-chd-zstd-redump-part2/psp-chd-zstd/')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='psp'),
        Link(
            type='Game',
            format='iso'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/PSNCollectionByGhostware')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.iso')),

    Source(
        Entry(platform='ps3'),
        Link(
            type='Game',
            format='pkg'
        )
    ).add_indexes(
        Index(url='https://nopaystation.com/tsv/PS3_GAMES.tsv'),
        Index(url='https://nopaystation.com/tsv/PS3_DEMOS.tsv'),
        Index(
            url='https://nopaystation.com/tsv/PS3_DLCS.tsv',
            link=Link(type='DLC')
        )
    ).add_parsers(
        NoPaystationParser(),
        GameTDBParser(),
        IGDBParser()
    ),

    Source(
        Entry(platform='ps3'),
        Link(
            type='Game',
            format='pkg+rap',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sony%20-%20PlayStation%203%20%28PSN%29%20%28Content%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Sony - PlayStation 3 (PSN) (Content)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sony%20-%20PlayStation%203%20%28PSN%29%20%28Content%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sony%20-%20PlayStation%203.torrent',
            base_path='Minerva_Myrient/Redump/Sony - PlayStation 3',
            link=Link(
                format='iso',
                source_url='https://minerva-archive.org/browse/Redump/Sony%20-%20PlayStation%203/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ps3'),
        Link(
            type='Update',
            format='pkg',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sony%20-%20PlayStation%203%20(PSN)%20(Updates).torrent',
            base_path='Minerva_Myrient/No-Intro/Sony - PlayStation 3 (PSN) (Updates)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sony%20-%20PlayStation%203%20(PSN)%20(Updates)/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser()
    ).add_filters(Filter('title', r'^(.+?\s*\([^)]+?\)).*\.zip')),

    Source(
        Entry(platform='ps3'),
        Link(
            type='Game',
            format='iso'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part1'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part2'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part3'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part4'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part5'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part6'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part7'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part8'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part9'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part10'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part11'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part12'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part13'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part14'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part15'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part16'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part17'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part18'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part19'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part20'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part21'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part22'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part23'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part24'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part25'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part26'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part27'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part28'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part29'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part30'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part31'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part32'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part33'),
        Index(url='https://archive.org/download/PS3-Redump-2024-Individual-Games-Part34')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        GameTDBParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ps3'),
        Link(
            type='Disc Key',
            format='key',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sony%20-%20PlayStation%203%20-%20Disc%20Keys.torrent',
            base_path='Minerva_Myrient/Redump/Sony - PlayStation 3 - Disc Keys',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Sony%20-%20PlayStation%203%20-%20Disc%20Keys/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sony%20-%20PlayStation%203%20-%20Disc%20Keys%20TXT.torrent',
            base_path='Minerva_Myrient/Redump/Sony - PlayStation 3 - Disc Keys TXT',
            link=Link(
                format='dkey',
                type='Disc Key TXT',
                source_url='https://minerva-archive.org/browse/Redump/Sony%20-%20PlayStation%203%20-%20Disc%20Keys%20TXT/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='psv'),
        Link(
            type='Game',
            format='pkg'
        )
    ).add_indexes(
        Index(url='https://nopaystation.com/tsv/PSV_GAMES.tsv'),
        Index(url='https://nopaystation.com/tsv/PSV_DEMOS.tsv'),
        Index(
            url='https://nopaystation.com/tsv/PSV_DLCS.tsv',
            link=Link(type='DLC')
        )
    ).add_parsers(
        NoPaystationParser(),
        IGDBParser()
    ),

    Source(
        Entry(platform='psv'),
        Link(
            type='Game',
            format='pkg',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sony%20-%20PlayStation%20Vita%20%28PSN%29%20%28Content%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Sony - PlayStation Vita (PSN) (Content)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sony%20-%20PlayStation%20Vita%20%28PSN%29%20%28Content%29/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='psv'),
        Link(
            type='Update',
            format='pkg',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sony%20-%20PlayStation%20Vita%20%28PSN%29%20%28Updates%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Sony - PlayStation Vita (PSN) (Updates)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sony%20-%20PlayStation%20Vita%20%28PSN%29%20%28Updates%29/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser()
    ).add_filters(Filter('title', r'^(.+?\s*\([^)]+?\)).*\.zip')),

    Source(
        Entry(platform='xbox'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Microsoft%20-%20Xbox.torrent',
            base_path='Minerva_Myrient/Redump/Microsoft - Xbox',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Microsoft%20-%20Xbox/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='x360'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Microsoft%20-%20Xbox%20360.torrent',
            base_path='Minerva_Myrient/Redump/Microsoft - Xbox 360',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Microsoft%20-%20Xbox%20360/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Microsoft%20-%20Xbox%20360%20%28Digital%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Microsoft - Xbox 360 (Digital)',
            link=Link(
                format='DIGITAL',
                source_url='https://minerva-archive.org/browse/No-Intro/Microsoft%20-%20Xbox%20360%20%28Digital%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='sms'),
        Link(
            type='Game',
            format='sms',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sega%20-%20Master%20System%20-%20Mark%20III.torrent',
            base_path='Minerva_Myrient/No-Intro/Sega - Master System - Mark III',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sega%20-%20Master%20System%20-%20Mark%20III/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='sms'),
        Link(
            type='Game',
            format='sms'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.ms-mkiii')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='gg'),
        Link(
            type='Game',
            format='gg',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sega%20-%20Game%20Gear.torrent',
            base_path='Minerva_Myrient/No-Intro/Sega - Game Gear',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sega%20-%20Game%20Gear/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='gg'),
        Link(
            type='Game',
            format='gg'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.gg')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='md'),
        Link(
            type='Game',
            format='md',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sega%20-%20Mega%20Drive%20-%20Genesis.torrent',
            base_path='Minerva_Myrient/No-Intro/Sega - Mega Drive - Genesis',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sega%20-%20Mega%20Drive%20-%20Genesis/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='md'),
        Link(
            type='Game',
            format='md'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.md')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='scd'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sega%20-%20Mega%20CD%20&%20Sega%20CD.torrent',
            base_path='Minerva_Myrient/Redump/Sega - Mega CD & Sega CD',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Sega%20-%20Mega%20CD%20%26%20Sega%20CD/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='scd'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_segacd/CHD-SegaCD-NTSC',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_segacd/CHD-SegaCD-NTSC/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_segacd/CHD-MegaCD-PAL',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_segacd/CHD-MegaCD-PAL/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_segacd/CHD-MegaCD-NTSCJ',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_segacd/CHD-MegaCD-NTSCJ/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_segacd/CHD-SegaCD-Bonus',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_segacd/CHD-SegaCD-Bonus/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='32x'),
        Link(
            type='Game',
            format='32x',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Sega%20-%2032X.torrent',
            base_path='Minerva_Myrient/No-Intro/Sega - 32X',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Sega%20-%2032X/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='32x'),
        Link(
            type='Game',
            format='32x'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.32x')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='sat'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sega%20-%20Saturn.torrent',
            base_path='Minerva_Myrient/Redump/Sega - Saturn',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Sega%20-%20Saturn/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='sat'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/sega_saturn')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='sat'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_saturn/CHD-Saturn/USA',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/USA/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_saturn/CHD-Saturn/Europe',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/Europe/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_saturn/CHD-Saturn/Japan',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/Japan/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/chd_saturn/CHD-Saturn/Other-Regions',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/chd_saturn/CHD-Saturn/Other-Regions/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='dc'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Sega%20-%20Dreamcast.torrent',
            base_path='Minerva_Myrient/Redump/Sega - Dreamcast',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Sega%20-%20Dreamcast/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='dc'),
        Link(
            type='Game',
            format='bin+gdi'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/almstcmpltdrmcst')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='dc'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/dc-chd-zstd-redump/dc-chd-zstd',
            link=Link(source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/dc-chd-zstd-redump/dc-chd-zstd/'))
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='mame'),
        Link(
            type='Game',
            format='rom',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20MAME%20-%20ROMs%20(non-merged).torrent',
            base_path='Minerva_Myrient/MAME/ROMs (non-merged)',
            link=Link(source_url='https://minerva-archive.org/browse/MAME/ROMs%20(non-merged)/'))
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        MAMEParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='mame'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20MAME%20-%20CHDs%20(merged).torrent',
            base_path='Minerva_Myrient/MAME/CHDs (merged)',
            link=Link(
                source_url='https://minerva-archive.org/browse/MAME/CHDs%20(merged)/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        MAMEParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='fbn'),
        Link(
            type='Game',
            format='rom',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/fbnarcade-fullnonmerged/arcade',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/fbnarcade-fullnonmerged/arcade/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='hbmame'),
        Link(
            type='Game',
            format='rom',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20HBMAME.torrent',
            base_path='Minerva_Myrient/HBMAME/ROMs (merged)',
            link=Link(
                source_url='https://minerva-archive.org/browse/HBMAME/ROMs%20(merged)/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='hbmame'),
        Link(
            type='Game',
            format='rom'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/hbmame_0244_roms')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='fbeat'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Konami%20-%20FireBeat.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Konami - FireBeat',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Konami%20-%20FireBeat/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='fbeat'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/konami_firebeat')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='m2'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Konami%20-%20M2.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Konami - M2',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Konami%20-%20M2/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='m2'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/konami_m2')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='s573'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Konami%20-%20System%20573.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Konami - System 573',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Konami%20-%20System%20573/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='s573'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/konami_system_573')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='sgv'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Konami%20-%20System%20GV.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Konami - System GV',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Konami%20-%20System%20GV/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='sgv'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/konami_system_gv')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='eamu'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Konami%20-%20e-Amusement.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Konami - e-Amusement',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Konami%20-%20e-Amusement/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='eamu'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/konami_e-amusement')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='tri'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Namco%20-%20Sega%20-%20Nintendo%20-%20Triforce.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Namco - Sega - Nintendo - Triforce',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Namco%20-%20Sega%20-%20Nintendo%20-%20Triforce/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='s246'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Namco%20-%20System%20246.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Namco - System 246',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Namco%20-%20System%20246/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='chih'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Sega%20-%20Chihiro.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Sega - Chihiro',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Sega%20-%20Chihiro/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='chih'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/sega_chihiro')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='lind'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Sega%20-%20Lindbergh.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Sega - Lindbergh',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Sega%20-%20Lindbergh/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='lind'),
        Link(
            type='Game',
            format='iso'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/sega_lindbergh')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='naomi'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Sega%20-%20Naomi.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Sega - Naomi',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Sega%20-%20Naomi/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='naomi'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/sega_naomi')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='naomi2'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Sega%20-%20Naomi%202.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Sega - Naomi 2',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Sega%20-%20Naomi%202/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='naomi2'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/sega_naomi_2')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ring'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Sega%20-%20RingEdge.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Sega - RingEdge',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Sega%20-%20RingEdge/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ring2'),
        Link(
            type='Game',
            format='iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Arcade%20-%20Sega%20-%20RingEdge%202.torrent',
            base_path='Minerva_Myrient/Redump/Arcade - Sega - RingEdge 2',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Arcade%20-%20Sega%20-%20RingEdge%202/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='dos'),
        Link(
            type='Game',
            format='exe',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Total%20DOS%20Collection.torrent',
            base_path='Minerva_Myrient/Total DOS Collection/Games/Files',
            link=Link(
                source_url='https://minerva-archive.org/browse/Total%20DOS%20Collection/Games/Files/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(
        Filter('title', r'(.*)\.zip'),
        Filter(
            'title', r'^(?:(.+?)(?:\s+v\d+(?:\.\d+)+[a-zA-Z]*)(?:.*?)|(.+?)(?:\s+\([^)]*\))*)(?:\s*\[[^]]*\])*(\s+\(\d{3}[\dxX]\)).*$')
    ),

    Source(
        Entry(platform='dos'),
        Link(
            type='Game',
            format='exe'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/Total_DOS_Collection_Release_16_March_2019/Games/Files/')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(
        Filter('title', r'(.*)\.zip'),
        Filter(
            'title', r'^(?:(.+?)(?:\s+v\d+(?:\.\d+)+[a-zA-Z]*)(?:.*?)|(.+?)(?:\s+\([^)]*\))*)(?:\s*\[[^]]*\])*(\s+\(\d{3}[\dxX]\)).*$')
    ),

    Source(
        Entry(platform='pc'),
        Link(
            type='Game',
            format='bin+cue/iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20_.torrent',
            base_path='Minerva_Myrient/Redump/IBM - PC compatible',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/_/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%200-9.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/0-9/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20A.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/A/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20B.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/B/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20C.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/C/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20D.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/D/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20E.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/E/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20F.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/F/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20G.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/G/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20H.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/H/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20I.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/I/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20J.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/J/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20K.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/K/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20L.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/L/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20M.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/M/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20N.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/N/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20O.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/O/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20P.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/P/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20Q.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/Q/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20R.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/R/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20S.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/S/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20T.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/T/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20U.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/U/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20V.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/V/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20W.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/W/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20X.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/X/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20Y.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/Y/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20IBM%20-%20PC%20compatible%20-%20Z.torrent',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/IBM%20-%20PC%20compatible/Z/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='pc'),
        Link(
            type='Game',
            format='wad',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/2020_03_22_DOOM/DOOM WADs',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/2020_03_22_DOOM/DOOM%20WADs/')
        )
    ).add_parsers(
        TorrentParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'^(.*?)(?:\s*\(v[^)]+\)(\s*.*?))?\.zip')),

    Source(
        Entry(platform='pc'),
        Link(
            type='Game',
            format='exe',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Touhou%20Project%20Collection.torrent',
            base_path='Minerva_Myrient/Touhou Project Collection/Official Content/Games',
            link=Link(
                source_url='https://minerva-archive.org/browse/Touhou%20Project%20Collection/Official%20Content/Games/')
        )
    ).add_parsers(
        TorrentParser(),
        TouhouProjectCollectionParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='mac'),
        Link(
            type='Game',
            format='bin+cue/iso',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Apple%20-%20Macintosh.torrent',
            base_path='Minerva_Myrient/Redump/Apple - Macintosh',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Apple%20-%20Macintosh/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='a26'),
        Link(
            type='Game',
            format='a26',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%202600.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari 2600',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%202600/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='a26'),
        Link(
            type='Game',
            format='a26'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.atari-2600')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='a52'),
        Link(
            type='Game',
            format='a52',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%205200.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari 5200',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%205200/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='a52'),
        Link(
            type='Game',
            format='a52'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.atari-5200')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='a78'),
        Link(
            type='Game',
            format='bin',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%207800%20%28BIN%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari 7800 (BIN)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%207800%20%28BIN%29/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='a78'),
        Link(
            type='Game',
            format='a78'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.atari-7800')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='lynx'),
        Link(
            type='Game',
            format='lnx',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%20Lynx%20%28LNX%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari Lynx (LNX)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%20Lynx%20%28LNX%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%20Lynx%20%28LYX%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari Lynx (LYX)',
            link=Link(
                format='lyx',
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%20Lynx%20%28LYX%29/'
            )
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%20Lynx%20%28BLL%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari Lynx (BLL)',
            link=Link(
                format='bll',
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%20Lynx%20%28BLL%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='lynx'),
        Link(
            type='Game',
            format='lnx'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/AtariLynxRomCollectionByGhostware')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.lnx')),

    Source(
        Entry(platform='jag'),
        Link(
            type='Game',
            format='j64',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%20Jaguar%20%28J64%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari Jaguar (J64)',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%20Jaguar%20%28J64%29/')
        ),
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Atari%20-%20Atari%20Jaguar%20%28JAG%29.torrent',
            base_path='Minerva_Myrient/No-Intro/Atari - Atari Jaguar (JAG)',
            link=Link(
                format='jag',
                source_url='https://minerva-archive.org/browse/No-Intro/Atari%20-%20Atari%20Jaguar%20%28JAG%29/'
            )
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='jag'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/jagcd-chd-zstd/jagcd-chd-zstd',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/jagcd-chd-zstd/jagcd-chd-zstd/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='jag'),
        Link(
            type='Game',
            format='chd'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/jagcd-chd-zstd/jagcd-chd-zstd/')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='jcd'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Atari%20-%20Jaguar%20CD%20Interactive%20Multimedia%20System.torrent',
            base_path='Minerva_Myrient/Redump/Atari - Jaguar CD Interactive Multimedia System',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Atari%20-%20Jaguar%20CD%20Interactive%20Multimedia%20System/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='tg16'),
        Link(
            type='Game',
            format='pce',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20NEC%20-%20PC%20Engine%20-%20TurboGrafx-16.torrent',
            base_path='Minerva_Myrient/No-Intro/NEC - PC Engine - TurboGrafx-16',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/NEC%20-%20PC%20Engine%20-%20TurboGrafx-16/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='tg16'),
        Link(
            type='Game',
            format='pce'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nointro.tg-16')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.7z')),

    Source(
        Entry(platform='tgcd'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20NEC%20-%20PC%20Engine%20CD%20&%20TurboGrafx%20CD.torrent',
            base_path='Minerva_Myrient/Redump/NEC - PC Engine CD & TurboGrafx CD',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/NEC%20-%20PC%20Engine%20CD%20%26%20TurboGrafx%20CD/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='tgcd'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/pcecd-chd-zstd-redump/pcecd-chd-zstd',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/pcecd-chd-zstd-redump/pcecd-chd-zstd/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='tgcd'),
        Link(
            type='Game',
            format='chd'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/pcecd-chd-zstd-redump/pcecd-chd-zstd/')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='pcfx'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20NEC%20-%20PC-FX%20%26%20PC-FXGA.torrent',
            base_path='Minerva_Myrient/Redump/NEC - PC-FX & PC-FXGA',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/NEC%20-%20PC-FX%20%26%20PC-FXGA/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='pcfx'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nec_pc-fxpc_fxga')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='pc98'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20NEC%20-%20PC-98%20series.torrent',
            base_path='Minerva_Myrient/Redump/NEC - PC-98 series',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/NEC%20-%20PC-98%20series/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='pc98'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/nec_pc-98_series')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='intv'),
        Link(
            type='Game',
            format='int',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Mattel%20-%20Intellivision.torrent',
            base_path='Minerva_Myrient/No-Intro/Mattel - Intellivision',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Mattel%20-%20Intellivision/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='cv'),
        Link(
            type='Game',
            format='col',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20No-Intro%20-%20Coleco%20-%20ColecoVision.torrent',
            base_path='Minerva_Myrient/No-Intro/Coleco - ColecoVision',
            link=Link(
                source_url='https://minerva-archive.org/browse/No-Intro/Coleco%20-%20ColecoVision/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='3do'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Panasonic%20-%203DO%20Interactive%20Multiplayer.torrent',
            base_path='Minerva_Myrient/Redump/Panasonic - 3DO Interactive Multiplayer',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Panasonic%20-%203DO%20Interactive%20Multiplayer/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='3do'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/panasonic_3do_interactive_multiplayer')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='3do'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/3do-chd-zstd-redump/3do-chd-zstd',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/3do-chd-zstd-redump/3do-chd-zstd/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='cdi'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Philips%20-%20CD-i.torrent',
            base_path='Minerva_Myrient/Redump/Philips - CD-i',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Philips%20-%20CD-i/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='fmt'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Fujitsu%20-%20FM-Towns.torrent',
            base_path='Minerva_Myrient/Redump/Fujitsu - FM-Towns',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Fujitsu%20-%20FM-Towns/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ngcd'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20SNK%20-%20Neo%20Geo%20CD.torrent',
            base_path='Minerva_Myrient/Redump/SNK - Neo Geo CD',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/SNK%20-%20Neo%20Geo%20CD/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ngcd'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/snk_neo_geo')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='ngcd'),
        Link(
            type='Game',
            format='chd',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Internet%20Archive%20-%20chadmaster.torrent',
            base_path='Minerva_Myrient/Internet Archive/chadmaster/ngcd-chd-zstd-redump/ngcd-chd-zstd',
            link=Link(
                source_url='https://minerva-archive.org/browse/Internet%20Archive/chadmaster/ngcd-chd-zstd-redump/ngcd-chd-zstd/')
        )
    ).add_parsers(
        TorrentParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='ngcd'),
        Link(
            type='Game',
            format='chd'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/ngcd-chd-zstd-redump/ngcd-chd-zstd/')
    ).add_parsers(
        InternetArchiveParser(),
        LibretroParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.chd')),

    Source(
        Entry(platform='pip'),
        Link(
            type='Game',
            format='bin+cue',
            source_name='MiNERVA Archive'
        )
    ).add_indexes(
        Index(
            url='https://minerva-archive.org/assets/Minerva_Myrient_v0.3/Minerva_Myrient%20-%20Redump%20-%20Bandai%20-%20Pippin.torrent',
            base_path='Minerva_Myrient/Redump/Bandai - Pippin',
            link=Link(
                source_url='https://minerva-archive.org/browse/Redump/Bandai%20-%20Pippin/')
        )
    ).add_parsers(
        TorrentParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip')),

    Source(
        Entry(platform='pip'),
        Link(
            type='Game',
            format='bin+cue'
        )
    ).add_indexes(
        Index(url='https://archive.org/download/bandai_pippin')
    ).add_parsers(
        InternetArchiveParser(),
        NoIntroParser(),
        IGDBParser()
    ).add_filters(Filter('title', r'(.*)\.zip'))
)
