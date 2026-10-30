# election-2026

Working files for covering the Texas 2026 elections.

## Layout

| Folder | What's in it |
|---|---|
| [`general-2026/early-vote/`](general-2026/early-vote/) | November 3 general election: early-vote analysis, decision benchmarks, and source data |
| [`primaries-2026/`](primaries-2026/) | March 3 primaries and May runoffs: turnout, primary-voter pools, down-ballot results, SD-9 special ([`primaries-notes.md`](primaries-2026/primaries-notes.md)) |

### `general-2026/early-vote/`

- [`analysis.md`](general-2026/early-vote/analysis.md): findings, calls, Tarrant County, district maps, and corrections, through Oct. 28 (Day 10), plus the Friday trend check on Oct. 29 (Day 11) data
- [`benchmarks.md`](general-2026/early-vote/benchmarks.md): Friday, Saturday and Sunday thresholds, set in advance, for turning the final early-vote data into calls
- `sources/`
  - `reports/`: Ryan Data & Research Day 8 report; Ryan's 2018 day 8 report (15 largest counties only); county Day 8 table; Transparency USA statewide, Tarrant and snapshot PDFs (snapshots through Oct. 28, and two through Oct. 29 at 95 and 244 counties)
  - `maps/`: Transparency USA district-map screenshots (Congress, state Senate, state House, plus metro zooms)
  - `data/`: TexPolls county early-voting CSVs (through Oct. 26 and Oct. 28), which include 2022 same-day turnout
  - `text/`: plain-text extractions of the PDFs, for searching
  - `MANIFEST.jsonl`: one row per source file (origin, timestamp, SHA-256, size)

## Conventions

- Source files are named `YYYY-MM-DD_source_description.ext`, where the date is the data's "through" date.
- Publish only aggregate counts, never individual voter records.
