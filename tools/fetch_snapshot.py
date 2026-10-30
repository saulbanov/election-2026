#!/usr/bin/env python3
"""Acquire one Transparency USA statewide snapshot and file it. Acquisition only.

Downloads https://turnout.transparencyusa.org/2026-general/reports/<date>.pdf,
reads its county count and timestamp, and, if these exact bytes are not already
in sources/MANIFEST.jsonl, files the PDF and its text extraction under sources/
with one manifest row. It decides nothing about whether the data is usable;
build_views.py does that.

    python3 tools/fetch_snapshot.py --date 2026-10-30

Prints one JSON line: {"new": bool, "counties": int, "as_of": str, "path": str, "sha": str}.
Exit status 0 on success (new or already filed), 2 if the report isn't posted yet.
"""
import argparse, datetime as dt, hashlib, json, re, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

EV = SRC = None  # set from --repo
URL = 'https://turnout.transparencyusa.org/2026-general/reports/{date}.pdf'
PDFTOTEXT = '/opt/homebrew/bin/pdftotext'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', required=True, help='the "through" date of the snapshot, YYYY-MM-DD')
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent), help='the election-2026 checkout to file into')
    a = ap.parse_args()
    global EV, SRC
    EV = Path(a.repo) / 'general-2026' / 'early-vote'; SRC = EV / 'sources'
    url = URL.format(date=a.date)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'election-2026 snapshot fetch'}), timeout=60) as r:
            body = r.read()
    except urllib.error.HTTPError as e:
        print(json.dumps({'new': False, 'error': f'HTTP {e.code}', 'url': url}))
        return 2
    if not body.startswith(b'%PDF'):
        print(json.dumps({'new': False, 'error': 'not a PDF', 'url': url}))
        return 2
    sha = hashlib.sha256(body).hexdigest()
    manifest = SRC / 'MANIFEST.jsonl'
    rows = [json.loads(l) for l in manifest.read_text().splitlines() if l.strip()]
    known = {r['body_sha256']: r['path'] for r in rows}

    text = subprocess.run([PDFTOTEXT, '-layout', '-', '-'], input=body, capture_output=True, check=True).stdout.decode('utf-8')
    m = re.search(r'As of ([^·\n]+?)\s*·\s*(\d+) of 254 counties reporting', text)
    if not m:
        print(json.dumps({'new': False, 'error': 'no county count in the PDF text', 'url': url}))
        return 2
    as_of, counties = m.group(1).strip(), int(m.group(2))
    if sha in known:
        print(json.dumps({'new': False, 'counties': counties, 'as_of': as_of, 'path': known[sha], 'sha': sha}))
        return 0

    stem = f'{a.date}_transparency-usa_statewide-snapshot_{counties}-counties'
    pdf, txt = SRC / 'reports' / f'{stem}.pdf', SRC / 'text' / f'{stem}.txt'
    if pdf.exists():  # same county count posted twice with different bytes: keep both
        stem += '_' + sha[:8]
        pdf, txt = SRC / 'reports' / f'{stem}.pdf', SRC / 'text' / f'{stem}.txt'
    pdf.write_bytes(body)
    txt.write_text(text, encoding='utf-8')
    row = {'ts': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'tool': 'fetch_snapshot.py', 'request': url + f' (as of {as_of}; {counties} of 254 counties)',
           'body_sha256': sha, 'body_bytes': len(body), 'session': 'scheduled', 'origin': 'election-2026/tools/fetch_snapshot.py',
           'path': str(pdf.relative_to(SRC))}
    with manifest.open('a') as f:
        f.write(json.dumps(row) + '\n')
    print(json.dumps({'new': True, 'counties': counties, 'as_of': as_of, 'path': row['path'], 'sha': sha}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
