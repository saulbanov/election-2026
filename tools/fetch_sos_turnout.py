#!/usr/bin/env python3
"""Acquire Texas Secretary of State county turnout files through BrowserOS. Acquisition only.

The Secretary of State's turnout app (goelect.txelections.civixapps.com/ivis-evr-ui/evr, a Civix app)
serves county turnout as JSON wrapped in base64 from /api-ivis-system/api/v1/getFile. Like
fetch_sos_results.py, this script asks the local BrowserOS browser to open the app and read those files
same-origin, the way the page does. If a check appears it stops and says so; it never passes one itself.

Each file is saved exactly as served, and only when its bytes change, so the folder records every
version the state posted and when this script first saw it:

    turnout/sources/<electionId>/<kind>/<YYYY-MM-DD>/<fetched UTC>.json
    turnout/sources/MANIFEST.jsonl

kind is "early" (EVR_EARLYVOTING: each county's in-person votes that day plus running in-person and mail
totals) or "election-day" (EVR_ELECTIONDAYTURNOUT: Election Day in-person votes by county).

    python3 tools/fetch_sos_turnout.py                              # Friday's early vote and Election Day, 2026 general
    python3 tools/fetch_sos_turnout.py --early 10/29/2026 --election-day ''

Prints one JSON line per file: {"kind", "date", "new", "date_updated", "path"}. Exit 0 on success,
3 if BrowserOS is not running, 4 if the app shows a check or an error.
"""
import argparse, base64, datetime as dt, hashlib, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_sos_results import BrowserOS, MCP, CHUNK, evaluate  # noqa: E402

APP = 'https://goelect.txelections.civixapps.com/ivis-evr-ui/evr'
API = '/api-ivis-system/api/v1/getFile'
GENERAL_2026 = '53815'
TYPES = {'early': 'EVR_EARLYVOTING', 'election-day': 'EVR_ELECTIONDAYTURNOUT'}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument('--election', default=GENERAL_2026)
    ap.add_argument('--early', action='append', help='an early-voting date, MM/DD/YYYY; repeatable (default 10/30/2026)')
    ap.add_argument('--election-day', default='11/03/2026', help="MM/DD/YYYY, or '' to skip")
    a = ap.parse_args()
    wanted = [('early', d) for d in (a.early or ['10/30/2026'])] + ([('election-day', a.election_day)] if a.election_day else [])
    out_dir = Path(a.repo) / 'turnout' / 'sources'
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / 'MANIFEST.jsonl'
    known = {json.loads(l)['body_sha256'] for l in manifest.read_text().splitlines() if l.strip()} if manifest.exists() else set()

    b = BrowserOS()
    try:
        b.start()
    except OSError as e:
        print(json.dumps({'error': f'BrowserOS is not reachable at {MCP}: {e}'})); return 3
    opened = b.tool('tabs', action='new', url=APP)
    page = int(opened.split('opened page ')[1].split()[0])
    try:
        # a challenge page has no app data; the election list is the test
        probe = evaluate(b, page, f"const r = await fetch('{API}?type=EVR_ELECTION', {{cache:'no-store'}}); const t = await r.text(); return {{status: r.status, upload: t.startsWith('{{\"upload\"')}};")
        if not probe['upload']:
            print(json.dumps({'error': 'the turnout app is showing a check or an error in BrowserOS; clear it in the browser, then rerun', 'probe': probe})); return 4
        for kind, date in wanted:
            url = f"{API}?type={TYPES[kind]}&electionId={a.election}&electionDate={date.replace('/', '%2F')}"
            got = evaluate(b, page, f"const r = await fetch('{url}', {{cache:'no-store'}}); window.__to = r.ok ? await r.text() : ''; return {{status: r.status, n: window.__to.length}};")
            if not got['n']:
                print(json.dumps({'kind': kind, 'date': date, 'new': False, 'status': got['status'], 'note': 'nothing served'})); continue
            text = ''.join(evaluate(b, page, f"return JSON.stringify(window.__to.slice({i}, {i + CHUNK}));") for i in range(0, got['n'], CHUNK))
            if len(text) != got['n']:
                raise RuntimeError(f"{kind} {date}: got {len(text)} of {got['n']} characters")
            try:  # read the file's own timestamp for the manifest; the saved bytes stay as served
                updated = json.loads(base64.b64decode(json.loads(text)['upload']))['date_updated']
            except Exception:
                updated = None
            iso = dt.datetime.strptime(date, '%m/%d/%Y').date().isoformat()
            stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
            path = out_dir / a.election / kind / iso / f'{stamp}.json'
            new = save(path, text, 'https://goelect.txelections.civixapps.com' + url, updated, manifest, known)
            print(json.dumps({'kind': kind, 'date': date, 'new': new, 'date_updated': updated, 'path': str(path.relative_to(out_dir)) if new else None}))
    finally:
        b.tool('tabs', action='close', page=page)
    return 0


def save(path: Path, text: str, url: str, updated, manifest: Path, known: set) -> bool:
    body = text.encode('utf-8')
    sha = hashlib.sha256(body).hexdigest()
    if sha in known:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    row = {'ts': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'tool': 'fetch_sos_turnout.py (BrowserOS, same-origin)',
           'request': url, 'body_sha256': sha, 'body_bytes': len(body), 'session': 'election-2026', 'origin': 'election-2026/tools/fetch_sos_turnout.py',
           'path': str(path.relative_to(manifest.parent)), 'date_updated': updated}
    with manifest.open('a') as f:
        f.write(json.dumps(row) + '\n')
    known.add(sha)
    return True


if __name__ == '__main__':
    sys.exit(main())
