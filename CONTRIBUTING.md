# Contributing to the database

Read this information carefully. Pull requests that do not meet the requirements will be rejected.

## Directory structure
- `build.py` creates the SQLite database.
- `sources.py` describes where data comes from and how it should be handled.
- `models.py` contains the objects passed through the build pipeline.
- `parsers/` contains code that reads source data to add/transform database entries.
- `scripts/` contains one-off or download scripts to prepare for building.
- `data/` contains downloaded data and metadata used by parsers.
- `cache/` contains cached requests and build data.
- `temp/` contains files created during a build.

Before writing or editing code, look at the existing implementations, especially
the sources, parsers, and related helpers. This document describes the general
workflow, but it may not cover every source-specific behavior or edge case.

## Sources
A source connects a platform to one or more indexes and describes the default data for its entries.

A source can contain:
- `entry`: default entry to use as a base for all new entries.
- `link`: default link to use as a base for all new links.
- `indexes`: URLs or files to read. An index can also set a base path, enable/disable recursion in scan, default entry data or link data (that will be merged with the defaults of `source`).
- `parsers`: parsers that will process the indexes one by one.
- `filters`: Regex patterns that remove or clean values.

Use the existing platform values inside of `platforms.py`. Add new platforms when needed.

## Parsers
A parser is a class with a `parse(source)` method.

The parser should:
- Read `source.indexes`.
- Convert source data into `Entry` and `Link` objects.
- Merge the base entries/links with the new entry/link.
- Add completed entries to `source.entries`.
- Skip invalid or incomplete entries when appropriate.

Parsers should not write directly to the final database. The builder owns database creation and entry merging.

Use helpers from `utils.py` for shared operations. Use `Cacher` when repeated downloads are expensive and safe to cache.

### Parser fallback fields

`fallback` lists fields that should only be filled when empty. Other non-empty fields are replaced; empty values are ignored. For example, `IGDBParser(fallback=('title', 'cover_url'))` keeps an existing title or cover. Use `fallback=()` to replace values normally.

## Data model
- `Entry` represents a ROM or other database item.
- `Link` represents a downloadable file or related resource.
- `Index` represents input data to fetch and parse.
- `Source` groups the defaults, indexes, parsers, and filters for one source.
- `Filter` controls which values are accepted or cleaned.

Values from different parsers are merged by slug during the build. Parsers should provide only the data they know and avoid replacing useful values with empty ones.

## Adding/editing a source
Sources are stored as a tuple (`SOURCES`) inside `sources.py`.

Add/edit one according to [Sources](#sources).

## Adding a parser
Create a file in `parsers/` and keep the parser focused on one input format or source type.

Then:
- Import the parser in `sources.py`.
- Add it to the relevant source with `add_parsers(...)`.
- Confirm that the parser handles missing, empty, and unexpected input.
- Run a build using cached data when possible.
- Check titles, platforms, regions, links, filenames, and URLs in the result.

## Style and changes
Prefer small changes that match the existing code. Do not duplicate parsing logic between sources. Do not commit credentials or generated files.

## Use of LLMs/AI
LLM-assisted contributions are welcome, but submitters must understand the code they submit, verify that it works, and be able to explain their changes during review.
