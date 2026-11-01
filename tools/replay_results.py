#!/usr/bin/env python3
"""Replay a past election night through build_results_view.read(), so Tuesday is not its first run.

    replay_results.py 2024      # U.S. Senate 2024 (Cruz v. Allred), election 49664
    replay_results.py 2022      # Governor 2022 (Abbott v. O'Rourke), election 47009

Only the final results of past years are on file, not each version the state posted that night, so the
stages are built from the final County.json in the order returns arrive: counties release their early
and mail votes first, largest first (25%, 50%, 75%, 90%, then all of the early vote), then Election Day
votes come in, smallest counties first (25%, 50%, 75%, 100%). Each stage is a County.json of the same
shape, read by the same function the live view uses. Writes nothing.

The early-vote mix is Ryan Data & Research's day-8 mix for that year (general-2026/early-vote/sources/
text/2026-10-26_ryan-data-research_day8-report.txt, "2026 vs. 2024 / 2022 Comparison"), standing in for
the final early mix, as in the page's 2024 estimate.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_results_view import OFFICES, read, tally  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CASES = {
    '2024': {'id': '49664', 'race': 'U.S. Senate', 'mix': {'d': 1379607 + 62482, 'r': 2113864 + 122547, 'np': 1974710 + 565782}, 'known': 'about D +5.4 (page estimate)',
             'baseline': ('47009', 'Governor')},
    '2022': {'id': '47009', 'race': 'Governor', 'mix': {'d': 972814 + 89786, 'r': 1422494 + 76634, 'np': 711477 + 143200}, 'known': 'about R +4 (page assumption)',
             'baseline': ('44144', 'U.S. Senate')},
}


def stage(final: dict, early_set: set, ed_set: set) -> dict:
    """A County.json in which only early_set counties have released early votes and only ed_set counties
    have added Election Day votes."""
    out = copy.deepcopy(final)
    for fips, c in out.items():
        for race in c.get('Races', {}).values():
            for cand in race['C'].values():
                ev, v = cand.get('EV', 0) or 0, cand.get('V', 0) or 0
                cand['EV'] = ev if fips in early_set else 0
                cand['V'] = (ev if fips in early_set else 0) + ((v - ev) if fips in ed_set else 0)
            race['PR'] = race.get('TPR', 0) if fips in ed_set else 0
    return out


def main() -> int:
    case = CASES[sys.argv[1] if len(sys.argv) > 1 else '2024']
    vdir = max((ROOT / 'results' / 'sources' / case['id']).iterdir(), key=lambda p: int(p.name[1:]))
    final = json.loads((vdir / 'County.json').read_text())
    test = dict(OFFICES)[case['race']]  # each county's early votes in the headline race
    size = {f: sum(cand.get('EV', 0) or 0 for r in c['Races'].values() if test(r.get('ON', '')) for cand in r['C'].values()) for f, c in final.items()}
    big_first = sorted(final, key=lambda f: -size[f])
    total = sum(size.values())
    expected = {final[f]['N'].upper(): size[f] for f in final}
    bid, brace = case['baseline']  # the previous general's early margins, by county, for the projection
    bdir = max((ROOT / 'results' / 'sources' / bid).iterdir(), key=lambda p: int(p.name[1:]))
    btally = tally(json.loads((bdir / 'County.json').read_text()), dict(OFFICES)[brace], None)
    baseline = {name: m for name, (n, m) in btally['by_county'].items() if m is not None}

    def first(share):  # the largest counties that together hold this share of the early vote
        acc, out = 0, set()
        for f in big_first:
            if acc >= share * total:
                break
            out.add(f); acc += size[f]
        return out

    plan = [('7:00, nothing in', set(), set())]
    plan += [(f'early votes, {int(s * 100)}% in', first(s), set()) for s in (0.25, 0.5, 0.75, 0.9)]
    allc = set(final)
    plan += [('all early votes in', allc, set())]
    small_first = big_first[::-1]
    for s in (0.25, 0.5, 0.75, 1.0):
        n = round(s * len(small_first))
        plan.append((f'Election Day, {int(s * 100)}% of counties', allc, set(small_first[:n])))

    print(f"{sys.argv[1] if len(sys.argv) > 1 else '2024'} {case['race']}: known no-primary lean {case['known']}")
    print(f"baseline for the projection: {bid} {brace}")
    print(f"{'stage':32} {'early so far':>12} {'projected':>10} {'all votes':>10} {'coverage':>9} {'implied lean':>13} {'precincts':>10}")
    for label, es, ds in plan:
        v = read(stage(final, es, ds), case['mix'], expected, baseline, case['race'])
        r = next(x for x in v['races'] if x['race'] == case['race'])
        pr = f"{r['precincts']['reporting']}/{r['precincts']['total']}"
        print(f"{label:32} {str(r['early']['margin']):>12} {str(r['early'].get('projected_margin', '-')):>10} {str(r['all']['margin']):>10} {r['early_coverage']:>9.0%} {str(r.get('implied_lean', '-')):>13} {pr:>10}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
