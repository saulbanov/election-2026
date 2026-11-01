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

### `results/`

Election-night results files from the Texas Secretary of State's results site (results.texas-election.com), saved exactly as the site's app serves them:

- `results/sources/<electionId>/v<version>/OfficeSummary.json`: statewide totals for every candidate in every race
- `results/sources/<electionId>/v<version>/County.json`: every county and race, with each candidate's total votes (`V`) and early votes (`EV`; Election Day is the difference), and precincts reporting
- `results/sources/<electionId>/v<version>/Race.json`, `results/sources/ElectionConstants.json` (the site's election list), `results/sources/MANIFEST.jsonl`

On file: the 2020, 2022 and 2024 general elections (ids 44144, 47009, 49664), the only generals the site lists. The site challenges scripted requests, so `tools/fetch_sos_results.py` reads these files through the local BrowserOS browser, same-origin, and stops if a check appears.


### `results/views/live.json` (election night)

`tools/build_results_view.py` reads the newest saved 2026 returns and writes the view the page mirrors: for the Senate and each statewide race, the early and all-vote margins, Election Day as the difference, and precincts reporting. While counties are still reporting it projects the full early vote (each county out at its 2024 Senate early margin plus the swing in counties that are in) and the no-primary lean that implies: (early margin − 0.9 × (D primary share − R primary share)) ÷ no-primary share, using Transparency USA's final early mix. The lean is marked final once every county's early vote is in. On Nov. 3 the Mac job fetches returns and rebuilds the view every 3 minutes from 6:50 p.m.

`tools/replay_results.py 2024` (or `2022`) replays a past night in stages from its final results, big counties' early votes first. In the 2024 replay, with 28% of the early vote in, the projection gave Cruz +9.3 for the full early vote (actual: Cruz +9.31). A partial early margin alone misleads: with three-quarters in, Allred led it by 7.8. With Ryan's day-12 mixes (Nov. 1), the replays' implied leans are D +0.2 for the 2024 Senate race and D +2.3 for the 2022 governor's race, both among early voters; the day-8 mixes used before gave D +5.3 and D +12. The 2022 projection missed the full early margin by up to 2.6 points, because its baseline was a presidential year.

### `turnout/`

The Secretary of State's turnout app at goelect.txelections.civixapps.com/ivis-evr-ui/evr (a Civix app) serves county turnout as base64-encoded JSON from `/api-ivis-system/api/v1/getFile`. Read through BrowserOS on 2026-10-31, same-origin, it showed no check.

- `?type=EVR_ELECTION`: the election list. The 2026 November general is election 53815, with early-voting dates 10/14 through 10/30.
- `?type=EVR_EARLYVOTING&electionId=53815&electionDate=MM/DD/YYYY`: for each of the 254 counties, registered voters, in-person votes that day, and in-person and mail totals for the election so far. On Oct. 31 the 10/30 file was still partial (18,053 votes from 83 counties, `date_updated` 2026-10-30).
- `?type=EVR_ELECTIONDAYTURNOUT&electionId=…&electionDate=…`: Election Day in-person votes by county, in the same shape. The March 3, 2026 primary's file is final (`date_updated` 2026-06-10). Whether this file updates during Election Day is unconfirmed until Nov. 3.
- `?type=EVR_STATEWIDE_ELECTIONDAY`: a zipped CSV of the statewide report.

These are turnout counts only, with no primary history; the breakdown by primary history still comes from Transparency USA.

`tools/fetch_sos_turnout.py` saves the Friday early-vote file and the Election Day file exactly as served, only when their bytes change, to `turnout/sources/53815/<early|election-day>/<date>/<fetched UTC>.json`, with a row in `turnout/sources/MANIFEST.jsonl`. The scheduled Mac job runs it at most every 15 minutes, Oct. 31 to Nov. 4, so the folder shows each version the state posted and when it first appeared. On Oct. 31 the Election Day file already held 1,535 votes in 55 counties, with the same internal day id as Friday's early file; what that means is unexplained.

### `turnout/county/` (Election Day check-ins)

A survey of 14 county election sites on Nov. 1, 2026 looked for Election Day turnout posted while polls are open:

- **Travis:** yes. Its ElectionLink tracker (updates.electionlink.net/widgets/travistx/2026-11-03/) posts hourly countywide check-ins and a per-precinct table with an Election Day column, regenerated every few minutes. A Wayback capture shows the March 3, 2026 file "AS OF TUE MAR 3 12:32 PM" with 37,795 check-ins. Plain requests work.
- **Dallas:** likely. On March 3, 2026 it posted per-vote-center check-in PDFs about hourly from 3 p.m. Its site answers scripts with an AWS WAF challenge, so it is read only through BrowserOS; the files it links on the Nov. 3 results page are saved as they appear.
- **Tarrant:** possible. A per-location check-in PDF sits at a fixed address (a placeholder now); no evidence it updates during the day.
- **Harris, Bexar, Collin:** daytime figures only in press conferences and news blogs.
- **Denton, Fort Bend, Williamson, El Paso, Hidalgo, Montgomery, Comal, Midland:** none on their sites. Williamson tweeted running totals in 2016 and 2018; El Paso says it posts updates on Facebook and X. Neither is read here. The Republican marker counties in the page's tells (Montgomery, Comal, Midland) publish nothing during the day.

`tools/fetch_county_turnout.py` saves those pages as served, only when they change, with a row in `turnout/county/MANIFEST.jsonl`. The Mac job runs it every 3 minutes from 6 a.m. Nov. 3 to noon Nov. 4. Nothing reads the counts yet.
