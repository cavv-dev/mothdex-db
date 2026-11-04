# Mothdex database
Collections of scripts and modules to build the final `roms.db` SQLite database used by [Mothdex](https://mothdex.net).

## Setup
Set values inside of `config.json`.

Install requirements:
```bash
python -m pip install -r requirements.txt
```

## Build
Run the builder:

```bash
python build.py
```

Optional flags: `--use-cached`, `--download-data`.

`--use-cached` reuses cached indexes while scraping sources. `--download-data` downloads the auxiliary source data before scraping. The flags can be combined.

```bash
python build.py --use-cached
python build.py --download-data
python build.py --download-data --use-cached
```

The builder downloads and processes the configured sources, creates `roms.db`, and updates the proxy and static file folders. Temporary files are stored in `temp/`.

## Contributing

Read [CONTRIBUTING.md](https://github.com/cavv-dev/mothdex-db/blob/main/CONTRIBUTING.md) to learn how to add/edit sources or parsing logic.
