#!/usr/bin/env python3
"""Acquire the Secretary of State's 2026 election-night results page. Acquisition only.

For 2026 the state posts returns at electionresults.sos.state.tx.us/results.html, one static page with
statewide totals per race and the share of polling locations reporting. The older results.texas-election.com
app still lists nothing after 2024. A plain request works (no check), so this script makes one, with a
User-Agent that says what it is, and saves the page exactly as served when its results change (the races, totals and Updated stamp):

    results/sources/<electionId>/html/<UTC time>.html     (election id read from the page, e.g. 53815)
    results/sources/MANIFEST.jsonl                         (one row per saved file)

Prints one JSON line: {"new": bool, "path": ..., "updated": "<the page's Updated stamp>"}. Exit 0, or 1 on a
failed request.
"""
import argparse, datetime as dt, hashlib, json, re, sys, urllib.request
from pathlib import Path

URL = 'https://electionresults.sos.state.tx.us/results.html'
UA = 'election-2026 results reader (github.com/saulbanov/election-2026)'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent))
    a = ap.parse_args()
    src = Path(a.repo) / 'results' / 'sources'
    manifest = src / 'MANIFEST.jsonl'
    try:
        with urllib.request.urlopen(urllib.request.Request(URL, headers={'User-Agent': UA}), timeout=60) as r:
            body = r.read()
    except Exception as e:
        print(json.dumps({'error': f'{URL}: {e}'})); return 1
    text = body.decode('utf-8', 'replace')
    if not text.rstrip().endswith('</html>'):
        # the server often cuts the page off partway (a 9 KB page held only the Senate race); wait for a whole one
        print(json.dumps({'new': False, 'truncated': len(body)})); return 0
    m = re.search(r'data-target="#collapse(\d+)"', text)
    if not m:
        print(json.dumps({'error': 'no election id on the page; its layout may have changed'})); return 1
    upd = re.search(r'\(Updated ([^)]+?)\s*\)', text)
    sha = hashlib.sha256(body).hexdigest()
    # Cloudflare stamps each response with fresh script tokens, so compare only the results: from the first race to the last table
    region = text[text.find('data-target="#collapse'):text.rfind('</table>')]
    content = hashlib.sha256(region.encode()).hexdigest()
    rows = [json.loads(l) for l in manifest.read_text().splitlines() if l.strip()] if manifest.exists() else []
    if any(r.get('content_sha256') == content for r in rows):
        print(json.dumps({'new': False, 'updated': upd and upd.group(1)})); return 0
    now = dt.datetime.now(dt.timezone.utc)
    path = src / m.group(1) / 'html' / (now.strftime('%Y-%m-%dT%H%M%SZ') + '.html')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    row = {'ts': now.strftime('%Y-%m-%dT%H:%M:%SZ'), 'tool': 'fetch_sos_html_results.py (plain request)', 'request': URL,
           'body_sha256': sha, 'content_sha256': content, 'body_bytes': len(body), 'session': 'election-2026', 'origin': 'election-2026/tools/fetch_sos_html_results.py',
           'path': str(path.relative_to(src))}
    with manifest.open('a') as f:
        f.write(json.dumps(row) + '\n')
    print(json.dumps({'new': True, 'path': str(path.relative_to(src)), 'updated': upd and upd.group(1)}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
