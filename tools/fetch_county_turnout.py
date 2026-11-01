#!/usr/bin/env python3
"""Acquire county Election Day turnout pages. Acquisition only.

Some large counties post running Election Day check-in counts on their own sites during the day. This
script fetches each page listed in COUNTIES and saves it exactly as served, only when its bytes change,
so the folder records every version a county posted and when this script first saw it:

    turnout/county/<county>/<label>/<fetched UTC>.<ext>
    turnout/county/MANIFEST.jsonl

A page fetched with "curl" is a plain request. A page with "browseros" is read through the local BrowserOS
browser, same-origin, as tools/fetch_sos_turnout.py does, for sites that render with JavaScript or check
scripted requests; if a check appears, that county is skipped and named. Nothing here parses or judges
the counts; that is a separate step.

    python3 tools/fetch_county_turnout.py            # every county
    python3 tools/fetch_county_turnout.py --county Harris

Prints one JSON line per page: {"county", "label", "new", "status", "path"}. Exit 0 when every page was
tried (a failed page is reported on its line), 3 if a BrowserOS page was needed and BrowserOS is not running.
"""
from __future__ import annotations

import argparse
import base64
import re
import datetime as dt
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

# (county, label, url, method, extension), from the Nov. 1, 2026 survey of county sites (README.md,
# "County Election Day turnout"). Only Travis has proof of counts posted while polls were open (March 3,
# 2026: hourly check-ins "as of 12:32 PM"). Dallas posted vote-center PDFs about hourly from 3 p.m. in
# March; its site challenges scripts, so it is read through BrowserOS, and the files it links under the
# Nov. 3 page are saved as they appear. Tarrant's per-location PDF is a placeholder until the county fills it.
TRAVIS = 'https://updates.electionlink.net/widgets/travistx/2026-11-03/'
COUNTIES: list[tuple[str, str, str, str, str]] = [
    ('Travis', 'checkins-per-hour', TRAVIS + 'CheckinsPerHourTable.csv', 'curl', 'csv'),
    ('Travis', 'by-precinct', TRAVIS + 'TurnoutByPrecinctTable.csv', 'curl', 'csv'),
    ('Travis', 'summary', TRAVIS + 'BallotTypeTurnout.html', 'curl', 'html'),
    ('Tarrant', 'ed-by-location', 'https://www.tarrantcountytx.gov/content/dam/main/elections/2026/1126/reports/Election_Day_Voting_Totals.pdf', 'curl', 'pdf'),
    ('Dallas', 'election-page-links', 'https://www.dallascountyvotes.org/election-results/historical/november-3-2026-general-and-joint-election/', 'browseros-links', 'tsv'),
]
# Dallas: save a linked file when its address looks like Election Day turnout, rosters or reports
LINK_PATTERN = r'/wp-content/uploads/2026/11/|turnout|election[-_ ]?day'

# A plain, honest user-agent. Sites that challenge scripts are read through BrowserOS, never by posing as a browser.
UA = 'election-2026 turnout fetcher (Future Heist; https://saulbanov.github.io/texas-election-page/)'


def get_curl(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b''


def get_browseros(b, url: str) -> tuple[int, bytes]:
    from fetch_sos_results import evaluate  # noqa: E402
    opened = b.tool('tabs', action='new', url=url)
    page = int(opened.split('opened page ')[1].split()[0])
    try:
        html = evaluate(b, page, "return JSON.stringify(document.documentElement.outerHTML);")
        return 200, html.encode('utf-8')
    finally:
        b.tool('tabs', action='close', page=page)


def browseros_links(b, url: str) -> list[tuple[str, int, bytes]]:
    """The page itself, then every same-site file it links whose address matches LINK_PATTERN, read in the page."""
    from fetch_sos_results import evaluate, CHUNK  # noqa: E402
    opened = b.tool('tabs', action='new', url=url)
    page = int(opened.split('opened page ')[1].split()[0])
    try:
        # the page's HTML changes on every load, so what is kept is its sorted list of links (text and address),
        # which changes only when the county posts or removes something
        links = evaluate(b, page, "return JSON.stringify([...new Set([...document.querySelectorAll('a[href]')].map(a => a.textContent.trim().replace(/\\s+/g, ' ') + '\\t' + a.href))].sort());")
        links = json.loads(links) if isinstance(links, str) else links
        out = [('page', 200, ('\n'.join(links) + '\n').encode('utf-8'))]
        hrefs = [l.split('\t', 1)[1] for l in links if '\t' in l]
        hrefs = [h for h in hrefs if h.startswith('https://www.dallascountyvotes.org/') and re.search(LINK_PATTERN, h, re.I) and re.search(r'\.(pdf|xlsx?|csv|zip)$', h, re.I)]
        for h in hrefs:
            got = evaluate(b, page, f"const r = await fetch({json.dumps(h)}, {{cache: 'no-store'}}); if (!r.ok) return {{status: r.status, n: 0}}; const u = new Uint8Array(await r.arrayBuffer()); let s = ''; for (let i = 0; i < u.length; i += 32768) s += String.fromCharCode.apply(null, u.subarray(i, i + 32768)); window.__f = btoa(s); return {{status: r.status, n: window.__f.length}};")
            if not got['n']:
                out.append((h, got['status'], b'')); continue
            b64 = ''.join(evaluate(b, page, f"return JSON.stringify(window.__f.slice({i}, {i + CHUNK}));") for i in range(0, got['n'], CHUNK))
            out.append((h, got['status'], base64.b64decode(b64)))
        return out
    finally:
        b.tool('tabs', action='close', page=page)


def save(out_dir: Path, manifest: Path, known: set, county: str, label: str, url: str, method: str, ext: str, body: bytes) -> dict:
    sha = hashlib.sha256(body).hexdigest()
    if sha in known:
        return {'county': county, 'label': label, 'new': False}
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    path = out_dir / county.lower().replace(' ', '-') / label / f'{stamp}.{ext}'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    row = {'ts': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'tool': f'fetch_county_turnout.py ({method})',
           'request': url, 'body_sha256': sha, 'body_bytes': len(body), 'session': 'election-2026',
           'origin': 'election-2026/tools/fetch_county_turnout.py', 'path': str(path.relative_to(out_dir)), 'county': county}
    with manifest.open('a') as f:
        f.write(json.dumps(row) + '\n')
    known.add(sha)
    return {'county': county, 'label': label, 'new': True, 'path': row['path']}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument('--county', action='append')
    a = ap.parse_args()
    out_dir = Path(a.repo) / 'turnout' / 'county'
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / 'MANIFEST.jsonl'
    known = {json.loads(l)['body_sha256'] for l in manifest.read_text().splitlines() if l.strip()} if manifest.exists() else set()
    todo = [c for c in COUNTIES if not a.county or c[0] in a.county]
    b = None
    if any(c[3].startswith('browseros') for c in todo):
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from fetch_sos_results import BrowserOS, MCP
        b = BrowserOS()
        try:
            b.start()
        except OSError as e:
            print(json.dumps({'error': f'BrowserOS is not reachable at {MCP}: {e}'})); return 3
    for county, label, url, method, ext in todo:
        try:
            if method == 'browseros-links':
                for href, status, body in browseros_links(b, url):
                    if href == 'page':
                        print(json.dumps({**save(out_dir, manifest, known, county, label, url, method, ext, body), 'status': status}))
                    elif status != 200 or not body:
                        print(json.dumps({'county': county, 'label': href.rsplit('/', 1)[-1], 'new': False, 'status': status}))
                    else:
                        name = re.sub(r'[^A-Za-z0-9._-]', '_', href.rsplit('/', 1)[-1])
                        stem, _, fext = name.rpartition('.')
                        print(json.dumps({**save(out_dir, manifest, known, county, 'files/' + stem, href, method, fext.lower(), body), 'status': status}))
                continue
            status, body = get_browseros(b, url) if method == 'browseros' else get_curl(url)
        except Exception as e:  # one county's failure must not stop the rest
            print(json.dumps({'county': county, 'label': label, 'new': False, 'error': repr(e)[:200]})); continue
        if status != 200 or not body:
            print(json.dumps({'county': county, 'label': label, 'new': False, 'status': status})); continue
        print(json.dumps({**save(out_dir, manifest, known, county, label, url, method, ext, body), 'status': status}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
