#!/usr/bin/env python3
"""Election-night results view: what the state's returns say so far, read against the early-vote mix.

    build_results_view.py [--repo .] [--election ID]     # newest saved version of the 2026 general
    build_results_view.py --county-json PATH --composition D,R,NP [--race "U. S. SENATOR"]   # replay / tests

Analysis only. It reads results files that tools/fetch_sos_results.py saved (results/sources/<id>/v<n>/),
the early-vote mix from general-2026/early-vote/views/latest.json, and each county's early-vote total from
the newest Secretary of State turnout file (turnout/sources/), and writes results/views/live.json when its
content changes. It fetches nothing.

What it reports, for the headline race and every statewide race it finds:
  - the early and mail vote (the state's EV field), which counties release first after polls close;
  - all votes counted so far, and Election Day as the difference;
  - precincts reporting;
  - a projection of the full early vote while counties are still reporting. Big counties report first and
    lean Democratic, so a partial early margin misleads (in the 2024 replay Allred led by 7.8 with three-
    quarters of the early vote in; Cruz led the full early vote by 9.3). Each county not yet in counts at its
    early margin in the last general (the baseline) plus the swing so far in the counties that are in,
    weighted by its expected early votes;
  - the implied lean of voters with no primary history, from the projected early margin:
    lean = (early margin - 0.9 x (D primary share - R primary share)) / no-primary share, all in points of
    the early vote. 0.9 assumes 95% of primary voters back their party (the model's "loyal"). It is marked
    final once every county's early vote is in.
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import sys
import base64
from pathlib import Path

LOYAL = 95
COVERAGE_FOR_LEAN = 0.25  # project the early vote once counties holding a quarter of it have reported
COMPLETE = 0.995
BASELINE_ID = '49664'  # 2024 general
OFFICES = [  # (label, test on the state's office name)
    ('U.S. Senate', lambda n: n.replace(' ', '').startswith('U.S.SENATOR')),
    ('Governor', lambda n: n.strip() == 'GOVERNOR'),
    ('Lt. Governor', lambda n: n.strip() == 'LIEUTENANT GOVERNOR'),
    ('Attorney General', lambda n: n.strip() == 'ATTORNEY GENERAL'),
    ('Agriculture', lambda n: n.strip() == 'COMMISSIONER OF AGRICULTURE'),
    ('Railroad Commission', lambda n: n.strip().startswith('RAILROAD COMMISSIONER')),
]


def tally(county: dict, label_test, expected: dict | None) -> dict | None:
    """Sum one office across counties: Democratic and Republican votes, early (EV) and all (V)."""
    t = {'d': 0, 'r': 0, 'all': 0, 'ev_d': 0, 'ev_r': 0, 'ev_all': 0, 'pr': 0, 'tpr': 0, 'd_name': None, 'r_name': None,
         'counties_ev': 0, 'cov_num': 0, 'cov_den': 0, 'by_county': {}}
    seen = False
    for fips, c in county.items():
        race = next((r for r in c.get('Races', {}).values() if label_test(r.get('ON', ''))), None)
        exp = (expected or {}).get(c.get('N', '').upper())
        if race is None:
            continue
        seen = True
        ev_here = 0
        for cand in race['C'].values():
            v, ev = cand.get('V', 0) or 0, cand.get('EV', 0) or 0
            t['all'] += v; t['ev_all'] += ev; ev_here += ev
            if cand.get('P') == 'DEM':
                t['d'] += v; t['ev_d'] += ev; t['d_name'] = t['d_name'] or cand['N']
            elif cand.get('P') == 'REP':
                t['r'] += v; t['ev_r'] += ev; t['r_name'] = t['r_name'] or cand['N']
        t['pr'] += race.get('PR', 0) or 0; t['tpr'] += race.get('TPR', 0) or 0
        d_ev = sum((x.get('EV', 0) or 0) for x in race['C'].values() if x.get('P') == 'DEM')
        r_ev = sum((x.get('EV', 0) or 0) for x in race['C'].values() if x.get('P') == 'REP')
        t['by_county'][c.get('N', '').upper()] = (ev_here, pct(d_ev, r_ev, ev_here))
        if ev_here:
            t['counties_ev'] += 1
        if exp:
            t['cov_den'] += exp
            if ev_here:
                t['cov_num'] += exp
    return t if seen else None


def pct(a: int, b: int, n: int):
    return round(100 * (a - b) / n, 2) if n else None


def project(t: dict, expected: dict | None, baseline: dict | None):
    """Projected early margin for the whole state: reported counties as counted, the rest at their baseline
    early margin plus the weighted swing in reported counties. None without both expected and baseline."""
    if not expected or not baseline:
        return None
    sw_num = sw_den = 0.0
    for name, (n, m) in t['by_county'].items():
        if n and m is not None and name in baseline:
            sw_num += n * (m - baseline[name]); sw_den += n
    if not sw_den:
        return None
    swing = sw_num / sw_den
    num = den = 0.0
    for name, w in expected.items():
        n, m = t['by_county'].get(name, (0, None))
        if n and m is not None:
            num += n * m; den += n
        elif name in baseline:
            num += w * (baseline[name] + swing); den += w
    return (round(num / den, 2), round(swing, 2)) if den else None


def read(county: dict, composition: dict, expected: dict | None = None, baseline: dict | None = None, headline: str = 'U.S. Senate') -> dict:
    """The view's body from one County.json, an early-vote mix {d, r, np} (shares, any scale), each county's
    expected early votes by county name, and each county's baseline early margin in the headline race."""
    s = composition['d'] + composition['r'] + composition['np']
    d_sh, r_sh, np_sh = (100 * composition[k] / s for k in ('d', 'r', 'np'))
    k = 2 * LOYAL / 100 - 1
    races = []
    for label, test in OFFICES:
        t = tally(county, test, expected)
        if not t:
            continue
        coverage = (t['cov_num'] / t['cov_den']) if t['cov_den'] else (t['counties_ev'] / len(county))
        early_m = pct(t['ev_d'], t['ev_r'], t['ev_all'])
        proj = project(t, expected, baseline) if label == headline else None
        row = {
            'race': label, 'd_name': t['d_name'], 'r_name': t['r_name'],
            'early': {'d': t['ev_d'], 'r': t['ev_r'], 'total': t['ev_all'], 'margin': early_m},
            'all': {'d': t['d'], 'r': t['r'], 'total': t['all'], 'margin': pct(t['d'], t['r'], t['all'])},
            'election_day': {'d': t['d'] - t['ev_d'], 'r': t['r'] - t['ev_r'], 'total': t['all'] - t['ev_all'],
                             'margin': pct(t['d'] - t['ev_d'], t['r'] - t['ev_r'], t['all'] - t['ev_all'])},
            'precincts': {'reporting': t['pr'], 'total': t['tpr']},
            'early_counties': t['counties_ev'], 'early_coverage': round(coverage, 4),
        }
        complete = coverage >= COMPLETE
        use_m = early_m if complete else (proj[0] if proj and coverage >= COVERAGE_FOR_LEAN else None)
        if proj:
            row['early']['projected_margin'], row['early']['swing'] = proj
        row['early']['complete'] = complete
        if use_m is not None:
            row['implied_lean'] = round((use_m - k * (d_sh - r_sh)) / np_sh * 100, 1)
            row['implied_lean_final'] = complete
        races.append(row)
    return {'composition': {'d': round(d_sh, 2), 'r': round(r_sh, 2), 'np': round(np_sh, 2)}, 'loyal': LOYAL,
            'coverage_for_lean': COVERAGE_FOR_LEAN, 'races': races}


def read_html(text: str) -> dict:
    """The view's body from the state's 2026 results page (statewide totals only: no county or early split)."""
    import re, html as H
    races = []
    blocks = re.findall(r'<div class="election">(.*?)</div><div class="polling">Polling Locations Reporting:\s*([\d.]+)%</div><div><table class="election">(.*?)</table>', text, re.S)
    for name, polling, table in blocks:
        name = H.unescape(name)
        label = next((l for l, test in OFFICES if test(name)), None)
        if not label or any(r['race'] == label for r in races):
            continue
        d = r = total = 0; d_name = r_name = None
        for party, cand, votes in re.findall(r'<td class="party">(.*?)</td><td class="candidate">(.*?)</td><td class="ballot"(?:\s*/>|>(.*?)</td>)', table, re.S):
            v = int(re.sub(r'[^\d]', '', votes) or 0)
            total += v
            if party.strip() == 'DEMOCRATIC': d += v; d_name = d_name or H.unescape(cand).strip()
            elif party.strip() == 'REPUBLICAN': r += v; r_name = r_name or H.unescape(cand).strip()
        races.append({'race': label, 'd_name': d_name, 'r_name': r_name, 'early': None, 'election_day': None,
                      'all': {'d': d, 'r': r, 'total': total, 'margin': pct(d, r, total)},
                      'polling_reporting_pct': float(polling)})
    return {'races': races}


def newest_turnout(repo: Path) -> tuple[dict | None, str | None]:
    """Each county's early votes (in person plus mail) from the newest saved 10/30 state turnout file."""
    files = sorted(glob.glob(str(repo / 'turnout' / 'sources' / '*' / 'early' / '2026-10-30' / '*.json')))
    if not files:
        return None, None
    j = json.loads(base64.b64decode(json.loads(Path(files[-1]).read_text())['upload']))
    return ({c['name'].upper(): c['total_in_person_votes_for_election'] + c['total_mail_votes_for_election'] for c in j['turnout_by_county']},
            str(Path(files[-1]).relative_to(repo)))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument('--election', help='state election id (default: the newest folder saved for a 2026 general)')
    ap.add_argument('--county-json', help='read this County.json instead (replay or test); prints the view, writes nothing')
    ap.add_argument('--composition', help='D,R,NP early-vote counts or shares (with --county-json)')
    a = ap.parse_args()
    repo = Path(a.repo)
    if a.county_json:
        d, r, n = (float(x) for x in a.composition.split(','))
        print(json.dumps(read(json.loads(Path(a.county_json).read_text()), {'d': d, 'r': r, 'np': n}), indent=1))
        return 0

    src = repo / 'results' / 'sources'
    consts = json.loads((src / 'ElectionConstants.json').read_text()) if (src / 'ElectionConstants.json').exists() else {}
    listed = {eid: {**info, 'Y': y, 'T': t} for y, types in consts.get('electionInfo', {}).items() for t, els in types.items() for eid, info in els.items()}
    eid = a.election or next((e for e, i in listed.items() if i['Y'] == '2026' and i['T'] == 'G'), None)
    # the state's server often cuts the page off partway, dropping every race after the cut; read only whole pages
    pages = sorted(p for p in glob.glob(str(src / '*' / 'html' / '*.html')) if Path(p).read_text().rstrip().endswith('</html>'))
    if (not eid or not (src / eid).is_dir()) and pages:
        # 2026: the state's returns are one statewide page (tools/fetch_sos_html_results.py), not County.json
        hp = Path(pages[-1]); text = hp.read_text()
        import re
        upd = re.search(r'\(Updated ([^)]+?)\s*\)', text)
        latest = json.loads((repo / 'general-2026' / 'early-vote' / 'views' / 'latest.json').read_text())['latest']
        s = latest['dem_primary'] + latest['gop_primary'] + latest['no_primary']
        out = {'by': 'election-2026/tools/build_results_view.py',
               'election': {'id': hp.parent.parent.name, 'name': '2026 NOVEMBER GENERAL ELECTION', 'updated': upd and upd.group(1)},
               'sources': [{'file': str(hp.relative_to(repo)), 'sha256': hashlib.sha256(hp.read_bytes()).hexdigest(),
                            'note': 'electionresults.sos.state.tx.us/results.html as served: statewide totals, no county or early split'}],
               'composition': {'d': round(100 * latest['dem_primary'] / s, 2), 'r': round(100 * latest['gop_primary'] / s, 2), 'np': round(100 * latest['no_primary'] / s, 2)},
               'loyal': LOYAL, **read_html(text)}
        dst = repo / 'results' / 'views' / 'live.json'
        dst.parent.mkdir(parents=True, exist_ok=True)
        old = json.loads(dst.read_text()) if dst.exists() else None
        if old and {k: v for k, v in old.items() if k != 'built'} == out:
            print('no change'); return 0
        out['built'] = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        dst.write_text(json.dumps(out, indent=1) + '\n')
        print(f"wrote {dst.relative_to(repo)} (statewide page, updated {out['election']['updated']})")
        return 0
    if not eid or not (src / eid).is_dir():
        print(json.dumps({'note': 'no 2026 general results saved yet'})); return 0
    ver_dir = max((p for p in (src / eid).iterdir() if p.name.startswith('v')), key=lambda p: int(p.name[1:]))
    cj = ver_dir / 'County.json'
    latest = json.loads((repo / 'general-2026' / 'early-vote' / 'views' / 'latest.json').read_text())['latest']
    expected, exp_src = newest_turnout(repo)
    # baseline for the projection: each county's early margin in the 2024 U.S. Senate race (election 49664)
    bdir = max((src / BASELINE_ID).iterdir(), key=lambda p: int(p.name[1:]))
    bt = tally(json.loads((bdir / 'County.json').read_text()), dict(OFFICES)['U.S. Senate'], None)
    baseline = {name: m for name, (n, m) in bt['by_county'].items() if m is not None}
    body = read(json.loads(cj.read_text()), {'d': latest['dem_primary'], 'r': latest['gop_primary'], 'np': latest['no_primary']}, expected, baseline)
    out = {
        'by': 'election-2026/tools/build_results_view.py',
        'election': {'id': eid, 'name': listed.get(eid, {}).get('N'), 'version': int(ver_dir.name[1:])},
        'sources': [{'file': str(cj.relative_to(repo)), 'sha256': hashlib.sha256(cj.read_bytes()).hexdigest()},
                    {'file': 'general-2026/early-vote/views/latest.json', 'note': f"early-vote mix through {latest['through']}, {latest['counties']} counties"}]
                   + ([{'file': exp_src, 'note': "each county's early votes: how much of the early vote is in, and the weights for the projection"}] if exp_src else [])
                   + [{'file': str((bdir / 'County.json').relative_to(repo)), 'note': 'baseline: each county\'s early margin in the 2024 U.S. Senate race'}],
        **body,
    }
    dst = repo / 'results' / 'views' / 'live.json'
    dst.parent.mkdir(parents=True, exist_ok=True)
    old = json.loads(dst.read_text()) if dst.exists() else None
    if old and {k: v for k, v in old.items() if k != 'built'} == out:
        print('no change'); return 0
    out['built'] = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    dst.write_text(json.dumps(out, indent=1) + '\n')
    print(f"wrote {dst.relative_to(repo)} (election {eid} v{out['election']['version']})")
    return 0


if __name__ == '__main__':
    sys.exit(main())
