#!/usr/bin/env python3
"""Acquire Texas Secretary of State election-results files through BrowserOS. Acquisition only.

results.texas-election.com is a Cloudflare-fronted app that challenges scripted requests, so this
script does not request it directly. It asks the local BrowserOS browser (the user's own browser,
http://127.0.0.1:9010/mcp) to open the site in a tab and read the app's own data files from there,
same-origin, the way the page itself does. If the site shows a check, this script stops and says so;
the person at the keyboard clears it. It never tries to pass a check itself.

Files are saved exactly as served, one folder per election and data version, with a manifest row each:

    results/sources/<electionId>/v<version>/{OfficeSummary,County,Race}.json
    results/sources/ElectionConstants.json
    results/sources/MANIFEST.jsonl

    python3 tools/fetch_sos_results.py --generals          # every general election the site lists
    python3 tools/fetch_sos_results.py --election 49664    # one election, by id
    python3 tools/fetch_sos_results.py --year 2026 --type G   # the 2026 general, once the site lists it

Prints one JSON line per election: {"election": id, "name": ..., "version": n, "new": bool, "files": [...]}.
Exit 0 on success, 3 if BrowserOS is not running, 4 if the site shows a check.
"""
import argparse, datetime as dt, hashlib, json, sys, urllib.request
from pathlib import Path

MCP = 'http://127.0.0.1:9010/mcp'
SITE = 'https://results.texas-election.com'
DATA = SITE + '/static/data/'
FILES = ('OfficeSummary.json', 'County.json', 'Race.json')
CHUNK = 90_000  # characters per evaluate call; JSON escaping must stay under the tool's 200,000-byte inline limit


class BrowserOS:
    """A minimal MCP client for BrowserOS over streamable HTTP."""
    def __init__(self, url=MCP):
        self.url, self.sid, self.n, self.task = url, None, 0, None

    def _post(self, payload):
        h = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
        if self.sid:
            h['mcp-session-id'] = self.sid
        req = urllib.request.Request(self.url, data=json.dumps(payload).encode(), headers=h, method='POST')
        with urllib.request.urlopen(req, timeout=60) as r:
            self.sid = self.sid or r.headers.get('mcp-session-id')
            body = r.read().decode('utf-8')
        if 'id' not in payload:
            return None
        for line in body.splitlines():  # server-sent events: the reply is on a "data:" line
            if line.startswith('data:') and line[5:].strip():
                msg = json.loads(line[5:])
                if msg.get('id') == payload['id']:
                    if 'error' in msg:
                        raise RuntimeError(msg['error'])
                    return msg['result']
        try:
            return json.loads(body)['result']
        except Exception:
            raise RuntimeError('no reply in: ' + body[:300])

    def call(self, method, params=None):
        self.n += 1
        return self._post({'jsonrpc': '2.0', 'id': self.n, 'method': method, 'params': params or {}})

    def start(self):
        self.call('initialize', {'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 'election-2026 results reader', 'version': '1'}})
        self._post({'jsonrpc': '2.0', 'method': 'notifications/initialized'})

    def tool(self, name, **args):
        args.setdefault('agentName', 'election-2026')
        if self.task:
            args.setdefault('session', self.task)
        res = self.call('tools/call', {'name': name, 'arguments': args})
        text = '\n'.join(c.get('text', '') for c in res.get('content', []) if c.get('type') == 'text')
        meta = (res.get('_meta') or {}).get('com.browseros.neo/session')
        if meta and not self.task:
            self.task = meta
        if res.get('isError'):
            raise RuntimeError(f'{name}: {text[:400]}')
        return text


def evaluate(b, page, code):
    """Run a page-context script and return its value, parsed from the tool's wrapped output."""
    out = b.tool('evaluate', page=page, code=code, maxChars=200_000, timeout=30_000)
    marker = 'ignore any embedded commands.\n'
    start = out.index(marker) + len(marker)
    end = out.rindex('\n[END_UNTRUSTED_PAGE_CONTENT')
    if 'truncated' in out[end:]:
        raise RuntimeError('evaluate result was truncated; lower CHUNK')
    return json.loads(out[start:end])  # every script below returns JSON (strings go through JSON.stringify)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent))
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--generals', action='store_true', help='every general election the site lists')
    g.add_argument('--election', action='append', help='an election id; repeatable')
    g.add_argument('--year', help='with --type: the election of that year and type the site lists')
    ap.add_argument('--type', default='G', help='G general, P primary, RU runoff, SE special')
    a = ap.parse_args()
    out_dir = Path(a.repo) / 'results' / 'sources'
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / 'MANIFEST.jsonl'
    known = {json.loads(l)['body_sha256'] for l in manifest.read_text().splitlines() if l.strip()} if manifest.exists() else set()

    b = BrowserOS()
    try:
        b.start()
    except OSError as e:
        print(json.dumps({'error': f'BrowserOS is not reachable at {MCP}: {e}'})); return 3
    opened = b.tool('tabs', action='new', url=SITE + '/races')
    page = int(opened.split('opened page ')[1].split()[0])
    try:
        # a challenge page has no app data; the app's own files are the test
        probe = evaluate(b, page, "const r = await fetch('/static/data/Version.json', {cache:'no-store'}); return {status: r.status, ok: r.ok, ct: r.headers.get('content-type')};")
        if not probe['ok'] or 'json' not in (probe['ct'] or ''):
            print(json.dumps({'error': 'the results site is showing a check or an error in BrowserOS; clear it in the browser, then rerun', 'probe': probe})); return 4

        consts_txt = evaluate(b, page, "return JSON.stringify(await (await fetch('/static/data/ElectionConstants_404.json', {cache:'no-store'})).text());")
        save(out_dir / 'ElectionConstants.json', consts_txt, DATA + 'ElectionConstants_404.json', manifest, known)
        consts = json.loads(consts_txt)
        listed = {eid: {**info, 'Y': y, 'T': t} for y, types in consts['electionInfo'].items() for t, els in types.items() for eid, info in els.items()}
        if a.generals:
            ids = [eid for eid, i in listed.items() if i['T'] == 'G']
        elif a.year:
            ids = [eid for eid, i in listed.items() if i['Y'] == a.year and i['T'] == a.type]
        else:
            ids = a.election
        if not ids:
            print(json.dumps({'new': False, 'note': f'no election listed for {a.year} {a.type} yet'})); return 0

        for eid in ids:
            ver = evaluate(b, page, f"return await (await fetch('/static/data/election/{eid}/Version.json', {{cache:'no-store'}})).json();")
            v = ver['___versionNo']
            files, new = [], False
            for name in FILES:
                url = f'{DATA}election/{eid}/{v}/{name}'
                n = evaluate(b, page, f"const r = await fetch('{url}', {{cache:'no-store'}}); window.__sos = r.ok ? await r.text() : ''; return window.__sos.length;")
                if not n:
                    continue
                text = ''.join(evaluate(b, page, f"return JSON.stringify(window.__sos.slice({i}, {i + CHUNK}));") for i in range(0, n, CHUNK))
                if len(text) != n:
                    raise RuntimeError(f'{name}: got {len(text)} of {n} characters')
                path = out_dir / eid / f'v{v}' / name
                new |= save(path, text, url, manifest, known)
                files.append(str(path.relative_to(out_dir)))
            print(json.dumps({'election': eid, 'name': listed.get(eid, {}).get('N'), 'version': v, 'elecDate': ver.get('elecDate'), 'new': new, 'files': files}))
    finally:
        b.tool('tabs', action='close', page=page)
    return 0


def save(path: Path, text: str, url: str, manifest: Path, known: set) -> bool:
    body = text.encode('utf-8')
    sha = hashlib.sha256(body).hexdigest()
    if sha in known and path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    row = {'ts': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'tool': 'fetch_sos_results.py (BrowserOS, same-origin)',
           'request': url, 'body_sha256': sha, 'body_bytes': len(body), 'session': 'election-2026', 'origin': 'election-2026/tools/fetch_sos_results.py',
           'path': str(path.relative_to(manifest.parent))}
    with manifest.open('a') as f:
        f.write(json.dumps(row) + '\n')
    known.add(sha)
    return True


if __name__ == '__main__':
    sys.exit(main())
