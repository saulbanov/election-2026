#!/usr/bin/env python3
"""Parse every filed Transparency USA statewide snapshot into machine-readable views.

Reads sources/text/*_transparency-usa_statewide-snapshot*.txt (filed by
fetch_snapshot.py or by hand), parses each into counts, and writes:

    views/series.json   every snapshot, oldest first, each flagged complete or not
    views/latest.json   the newest complete snapshot (>= COMPLETE counties), the one
                        before it, and the newest partial post if it is newer

Every entry names its source file and SHA-256, so a consumer can trace each number.
Pure parsing and arithmetic; it fetches nothing.

    python3 tools/build_views.py
"""
import datetime as dt, json, re, sys
from pathlib import Path

EV = SRC = VIEWS = None  # set from --repo
COMPLETE = 240  # counties; below this a post overstates the big Democratic counties
BY = 'election-2026/tools/build_views.py'

N = r'([\d,]+)'
num = lambda s: int(s.replace(',', ''))


def parse(text: str) -> dict:
    out = {}
    m = re.search(r'Snapshot through \w+, (\w+ \d+, \d{4})', text)
    out['through'] = dt.datetime.strptime(m.group(1), '%B %d, %Y').date().isoformat()
    m = re.search(r'As of ([^·\n]+?)\s*·\s*(\d+) of 254 counties reporting', text)
    out['as_of'], out['counties'] = m.group(1).strip(), int(m.group(2))
    m = re.search(r'REGISTERED\s+VOTES CAST\s+TURNOUT\s*\n\s*' + N + r'\s+' + N + r'\s+([\d.]+)%', text)
    out['registered'], out['votes'], out['turnout_pct'] = num(m.group(1)), num(m.group(2)), float(m.group(3))
    m = re.search(r'ABSENTEE / MAIL\s+EARLY IN-PERSON\s+ELECTION DAY\s*\n\s*' + N + r'\s+' + N + r'\s+' + N, text)
    out['mail'], out['early_in_person'], out['election_day'] = num(m.group(1)), num(m.group(2)), num(m.group(3))

    # Each bar: a label line, then "Voted X · Not voted Y · Z active". Labels repeat across
    # sections ("1 of 4"), so track the section heading too.
    section, label, groups = 'history', None, {}
    heads = {'General history': 'general', 'Democratic primaries': 'dem', 'Republican primaries': 'gop', 'Gender': 'gender', 'Age bands': 'age'}
    for line in text.splitlines():
        t = line.strip()
        if t in heads:
            section = heads[t]; continue
        lm = re.match(r'(DEM Only|DEM Mixed|GOP Only|GOP Mixed|General Only|No History|[1-4] of 4|Female|Male|18-24|25-34|35-44|45-54|55-64|65\+)\b', t)
        if lm:
            label = lm.group(1); continue
        vm = re.match(r'Voted ' + N + r' · Not voted ' + N + r' · ' + N + r' active', t)
        if vm and label:
            groups[f'{section}:{label}'] = {'voted': num(vm.group(1)), 'not_voted': num(vm.group(2)), 'active': num(vm.group(3))}
            label = None
    g = lambda k: groups[k]['voted']
    nv = lambda k: groups[k]['not_voted']
    out['groups'] = groups
    out['dem_primary'] = g('history:DEM Only') + g('history:DEM Mixed')
    out['gop_primary'] = g('history:GOP Only') + g('history:GOP Mixed')
    out['general_only'] = g('history:General Only')
    out['no_history'] = g('history:No History')
    out['no_primary'] = out['general_only'] + out['no_history']
    out['primary_margin'] = out['dem_primary'] - out['gop_primary']
    out['reliable_gop_not_voted'] = nv('gop:3 of 4') + nv('gop:4 of 4')
    out['reliable_dem_not_voted'] = nv('dem:3 of 4') + nv('dem:4 of 4')
    out['reliable_gap'] = out['reliable_gop_not_voted'] - out['reliable_dem_not_voted']
    out['young_voted'] = g('age:18-24') + g('age:25-34')
    out['young_share'] = round(100 * out['young_voted'] / out['votes'], 2)
    out['women_lead'] = g('gender:Female') - g('gender:Male')
    out['daily'] = [{'day': d, 'voters': num(v)} for d, v, _running in re.findall(r'^\s*(\w+day, \w+ \d+)\s+' + N + r'\s+' + N, text, re.M)]
    return out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent), help='the election-2026 checkout to read and write')
    global EV, SRC, VIEWS
    EV = Path(ap.parse_args().repo) / 'general-2026' / 'early-vote'; SRC, VIEWS = EV / 'sources', EV / 'views'
    manifest = {}
    for l in (SRC / 'MANIFEST.jsonl').read_text().splitlines():
        if l.strip():
            r = json.loads(l); manifest[r['path']] = r['body_sha256']
    snaps = []
    for txt in sorted((SRC / 'text').glob('*_transparency-usa_statewide-snapshot*.txt')):
        pdf = 'reports/' + txt.name[:-4] + '.pdf'
        if pdf not in manifest:
            print(f'SKIPPED: {txt.name} has no manifest row for {pdf}', file=sys.stderr); continue
        try:
            s = parse(txt.read_text(encoding='utf-8'))
        except (AttributeError, KeyError) as e:
            print(f'SKIPPED: could not parse {txt.name}: {e!r}', file=sys.stderr); continue
        s['complete'] = s['counties'] >= COMPLETE
        s['source'] = {'path': 'general-2026/early-vote/sources/' + pdf, 'sha256': manifest[pdf], 'text': 'general-2026/early-vote/sources/text/' + txt.name}
        snaps.append(s)
    # oldest first: by through date, then by when it was posted (county count rises through the day)
    snaps.sort(key=lambda s: (s['through'], s['counties']))
    complete = [s for s in snaps if s['complete']]
    latest = complete[-1] if complete else None
    # 'previous' is the last complete post from an earlier day, so changes read day over day
    earlier = [s for s in complete if latest and s['through'] < latest['through']]
    partial = snaps[-1] if snaps and not snaps[-1]['complete'] and (not latest or snaps[-1]['through'] > latest['through']) else None
    VIEWS.mkdir(exist_ok=True)
    stamp = {'by': BY, 'built': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'complete_threshold': COMPLETE}
    def write(name, body):
        # rewrite only when the content changes, so an unchanged run leaves git clean
        f = VIEWS / name
        if f.exists():
            old = json.loads(f.read_text()); old.pop('built', None)
            if old == {k: v for k, v in body.items() if k != 'built'}:
                return
        f.write_text(json.dumps(body, indent=1) + '\n')
    write('series.json', {**stamp, 'snapshots': snaps})
    write('latest.json', {**stamp, 'latest': latest, 'previous': earlier[-1] if earlier else None, 'partial': partial})
    print(f'{len(snaps)} snapshots, {len(complete)} complete; latest complete through {latest["through"] if latest else None} '
          f'({latest["counties"] if latest else 0} counties); partial newer: {bool(partial)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
