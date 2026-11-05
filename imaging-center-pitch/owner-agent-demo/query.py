#!/usr/bin/env python3
"""Tiny query helper for the SYNTHETIC owner-agent demo dataset.

Usage:
  python3 query.py                 # full summary of every metric
  python3 query.py week 8          # one week's rollup
  python3 query.py payers          # prior auth by payer over 8 weeks
  python3 query.py revenue         # billed vs collected by payer
  python3 query.py referrers       # referrer volume by week
  python3 query.py uptime          # scanner uptime by modality
  python3 query.py days 8          # daily rollup for week N
  python3 query.py compare         # weeks 1-4 vs 5-8 (month-over-month)
"""
import json
import sys
from pathlib import Path

D = json.loads(Path(__file__).with_name("data.json").read_text())
W = D["weeks"]
MODS = D["modalities"]
PAYERS = D["payers"]


def pct(a, b):
    return 0.0 if b == 0 else round(100.0 * a / b, 1)


def week_summary(w):
    print(f"\n== {w['label']} ({w['start']} to {w['end']}) ==")
    print(f"scheduled {w['scheduled_total']}  completed {w['studies_completed_total']}  "
          f"cancellations {w['cancellations_total']} ({pct(w['cancellations_total'], w['scheduled_total'])}%)  "
          f"no-shows {w['no_shows_total']} ({pct(w['no_shows_total'], w['scheduled_total'])}%)")
    print(f"capacity {w['capacity_total']}  open slots {w['open_slots_total']}  backfilled {w['backfilled_total']}  "
          f"utilization {pct(w['studies_completed_total'], w['capacity_total'])}%")
    print("completed by modality:", w["studies_completed_by_modality"])
    print("uptime % by modality:", w["uptime_pct_by_modality"])
    print(f"report turnaround avg {w['report_turnaround_hours_avg']} h   staff hours on prior auth {w['staff_hours_on_prior_auth']}")
    pa = w["prior_auth_by_payer"]
    sub = sum(v["submitted"] for v in pa.values())
    den = sum(v["denied"] for v in pa.values())
    app = sum(v["approved"] for v in pa.values())
    pen = sum(v["pending"] for v in pa.values())
    af = sum(v["appeals_filed"] for v in pa.values())
    aw = sum(v["appeals_won"] for v in pa.values())
    tat = [v["avg_turnaround_hours"] for p, v in pa.items() if v["submitted"]]
    print(f"prior auth: submitted {sub} approved {app} denied {den} ({pct(den, app + den)}% of decided) pending {pen}  "
          f"appeals filed {af} won {aw} ({pct(aw, af)}%)  avg auth turnaround {round(sum(tat)/len(tat),1)} h")
    worst = max((p for p in pa if pa[p]["submitted"]), key=lambda p: pct(pa[p]["denied"], pa[p]["approved"] + pa[p]["denied"]))
    print(f"worst denying payer: {worst} {pct(pa[worst]['denied'], pa[worst]['approved'] + pa[worst]['denied'])}%")
    bil = sum(v["billed"] for v in w["revenue_by_payer"].values())
    col = sum(v["collected_to_date"] for v in w["revenue_by_payer"].values())
    print(f"revenue billed ${bil:,}  collected to date ${col:,} ({pct(col, bil)}%)")
    busiest = max(w["days"], key=lambda d: sum(d["modalities"][m]["completed"] for m in MODS))
    print(f"busiest day: {busiest['weekday']} {busiest['date']} "
          f"({sum(busiest['modalities'][m]['completed'] for m in MODS)} studies)")
    print("referrers:", w["referrer_volume"])


def payers(weeks=W):
    print(f"\n== Prior auth by payer, weeks {weeks[0]['week']}-{weeks[-1]['week']} ==")
    print(f"{'payer':22}{'subm':>6}{'appr':>6}{'den':>5}{'den%':>7}{'pend':>6}{'appF':>6}{'appW':>6}{'win%':>7}{'TAT h':>7}")
    tot = dict(submitted=0, approved=0, denied=0, pending=0, appeals_filed=0, appeals_won=0)
    for p in PAYERS:
        s = {k: sum(w["prior_auth_by_payer"][p][k] for w in weeks) for k in tot}
        for k in tot:
            tot[k] += s[k]
        tats = [w["prior_auth_by_payer"][p]["avg_turnaround_hours"] for w in weeks if w["prior_auth_by_payer"][p]["submitted"]]
        tat = round(sum(tats) / len(tats), 1) if tats else 0
        print(f"{p:22}{s['submitted']:>6}{s['approved']:>6}{s['denied']:>5}{pct(s['denied'], s['approved']+s['denied']):>7}"
              f"{s['pending']:>6}{s['appeals_filed']:>6}{s['appeals_won']:>6}{pct(s['appeals_won'], s['appeals_filed']):>7}{tat:>7}")
    print(f"{'TOTAL':22}{tot['submitted']:>6}{tot['approved']:>6}{tot['denied']:>5}{pct(tot['denied'], tot['approved']+tot['denied']):>7}"
          f"{tot['pending']:>6}{tot['appeals_filed']:>6}{tot['appeals_won']:>6}{pct(tot['appeals_won'], tot['appeals_filed']):>7}")
    print("staff hours on prior auth by week:", [w["staff_hours_on_prior_auth"] for w in weeks],
          "total", round(sum(w["staff_hours_on_prior_auth"] for w in weeks), 1))


def revenue(weeks=W):
    print(f"\n== Revenue (SYNTHETIC) weeks {weeks[0]['week']}-{weeks[-1]['week']} ==")
    tb = tc = 0
    for p in PAYERS:
        b = sum(w["revenue_by_payer"][p]["billed"] for w in weeks)
        c = sum(w["revenue_by_payer"][p]["collected_to_date"] for w in weeks)
        tb += b
        tc += c
        print(f"{p:22} billed ${b:>9,}  collected ${c:>9,}  ({pct(c, b)}%)")
    print(f"{'TOTAL':22} billed ${tb:>9,}  collected ${tc:>9,}  ({pct(tc, tb)}%)")


def referrers():
    print("\n== Referrer volume by week ==")
    names = list(W[0]["referrer_volume"])
    print(f"{'referrer':12}" + "".join(f"{'W'+str(w['week']):>5}" for w in W) + "  total")
    for r in names:
        vals = [w["referrer_volume"][r] for w in W]
        print(f"{r:12}" + "".join(f"{v:>5}" for v in vals) + f"{sum(vals):>7}")


def uptime():
    print("\n== Uptime % by modality by week ==")
    for m in MODS:
        vals = [w["uptime_pct_by_modality"][m] for w in W]
        print(f"{m:11}", vals, "8-wk avg", round(sum(vals) / 8, 2))
    print("events:", D["events"])


def days(n):
    w = W[n - 1]
    print(f"\n== Daily, {w['label']} ==")
    for d in w["days"]:
        tot = {k: sum(d["modalities"][m][k] for m in MODS) for k in ("scheduled", "completed", "cancellations", "no_shows", "open_slots", "backfilled")}
        print(d["weekday"][:3], d["date"], tot, "by mod:", {m: d["modalities"][m]["completed"] for m in MODS},
              "report TAT", d["report_turnaround_hours"])


def compare():
    a, b = W[:4], W[4:]
    def agg(ws):
        comp = sum(w["studies_completed_total"] for w in ws)
        bil = sum(v["billed"] for w in ws for v in w["revenue_by_payer"].values())
        den = sum(v["denied"] for w in ws for v in w["prior_auth_by_payer"].values())
        dec = den + sum(v["approved"] for w in ws for v in w["prior_auth_by_payer"].values())
        opn = sum(w["open_slots_total"] for w in ws)
        tat = round(sum(w["report_turnaround_hours_avg"] for w in ws) / len(ws), 1)
        sh = round(sum(w["staff_hours_on_prior_auth"] for w in ws), 1)
        return dict(completed=comp, billed=bil, denial_pct=pct(den, dec), open_slots=opn, report_tat=tat, staff_hours_pa=sh)
    print("\n== Weeks 1-4 vs weeks 5-8 ==")
    A, B = agg(a), agg(b)
    for k in A:
        print(f"{k:14} {A[k]:>10} -> {B[k]:>10}   change {pct(B[k] - A[k], A[k]) if isinstance(A[k], int) else round(B[k]-A[k],1)}{'%' if isinstance(A[k], int) else ''}")


if __name__ == "__main__":
    args = sys.argv[1:]
    print(D["data_status"])
    if not args:
        for w in W:
            week_summary(w)
        payers(); revenue(); referrers(); uptime(); compare()
    elif args[0] == "week":
        week_summary(W[int(args[1]) - 1])
    elif args[0] == "days":
        days(int(args[1]))
    elif args[0] == "payers":
        payers()
    elif args[0] == "revenue":
        revenue()
    elif args[0] == "referrers":
        referrers()
    elif args[0] == "uptime":
        uptime()
    elif args[0] == "compare":
        compare()
    else:
        print(__doc__)
