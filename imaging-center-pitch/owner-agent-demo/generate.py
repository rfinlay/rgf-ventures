#!/usr/bin/env python3
"""Deterministic generator for the SYNTHETIC owner-agent demo dataset.

Run:  python3 generate.py   -> writes data.json next to this file.
All names are generic. All numbers are invented and internally consistent.
"""
import json
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(20261030)

CENTER = "Your New Center"
LAST_FRIDAY = date(2026, 10, 30)
WEEKS = 8
MODALITIES = ["MRI", "CT", "X-ray", "Ultrasound"]
PAYERS = ["Medicare Advantage", "Medicaid", "BCBS TX", "UnitedHealthcare",
          "Aetna", "Cigna", "TRICARE", "Self-pay"]
PAYER_MIX = [0.26, 0.20, 0.16, 0.12, 0.08, 0.06, 0.07, 0.05]
# Denial rate by payer for auths decided. One payer clearly worst.
DENY_RATE = {"Medicare Advantage": 0.055, "Medicaid": 0.11, "BCBS TX": 0.035,
             "UnitedHealthcare": 0.045, "Aetna": 0.03, "Cigna": 0.035,
             "TRICARE": 0.02, "Self-pay": 0.0}
# Auth needed share by modality (self-pay never needs auth)
AUTH_SHARE = {"MRI": 0.95, "CT": 0.85, "X-ray": 0.05, "Ultrasound": 0.35}
# Synthetic avg billed per completed study and expected collection rate by payer
BILLED = {"MRI": 1150, "CT": 780, "X-ray": 110, "Ultrasound": 260}
COLLECT_RATE = {"Medicare Advantage": 0.42, "Medicaid": 0.30, "BCBS TX": 0.58,
                "UnitedHealthcare": 0.55, "Aetna": 0.56, "Cigna": 0.54,
                "TRICARE": 0.45, "Self-pay": 0.70}
# Daily scheduled capacity (slots) by modality, Mon-Fri
CAPACITY = {"MRI": 18, "CT": 22, "X-ray": 34, "Ultrasound": 16}
# Ramp: new center, volume grows over 8 weeks
RAMP = [0.68, 0.72, 0.76, 0.80, 0.84, 0.87, 0.90, 0.93]
DAY_FACTOR = {0: 0.98, 1: 1.05, 2: 1.03, 3: 1.00, 4: 0.90}  # Mon..Fri, Tue busiest
REFERRERS = [f"Referrer {c}" for c in "ABCDEFGHIJ"]
REF_WEIGHT = [0.18, 0.15, 0.13, 0.11, 0.10, 0.09, 0.08, 0.07, 0.05, 0.04]
QUIET_REFERRER = "Referrer D"  # goes quiet from week 7
MRI_DOWN_DATE = date(2026, 10, 21)  # Wednesday week 7, chiller fault, 6.5 h down
MRI_DOWN_HOURS = 6.5
OPERATING_HOURS = 11.0

weeks = []
all_days = []
first_monday = LAST_FRIDAY - timedelta(days=4 + 7 * (WEEKS - 1))

for w in range(WEEKS):
    monday = first_monday + timedelta(days=7 * w)
    ramp = RAMP[w]
    days = []
    for d in range(5):
        day = monday + timedelta(days=d)
        rec = {"date": day.isoformat(), "weekday": day.strftime("%A"),
               "modalities": {}}
        for m in MODALITIES:
            cap = CAPACITY[m]
            sched = int(round(cap * ramp * DAY_FACTOR[d] * random.uniform(0.96, 1.04)))
            sched = min(sched, cap)
            if m == "MRI" and day == MRI_DOWN_DATE:
                lost = int(round(sched * MRI_DOWN_HOURS / OPERATING_HOURS))
            else:
                lost = 0
            cancels = int(round(sched * random.uniform(0.17, 0.23)))
            noshows = int(round(sched * random.uniform(0.021, 0.030)))
            # backfill: fraction of cancelled slots refilled from a waitlist
            backfilled = int(round(cancels * random.uniform(0.30, 0.45)))
            completed = sched - cancels - noshows + backfilled - lost
            open_slots = cap - completed
            uptime = 1.0 if lost == 0 else round(1 - MRI_DOWN_HOURS / OPERATING_HOURS, 4)
            if m == "CT" and random.random() < 0.08:
                uptime = round(1 - random.uniform(0.3, 0.9) / OPERATING_HOURS, 4)
            rec["modalities"][m] = {
                "capacity": cap, "scheduled": sched, "completed": completed,
                "cancellations": cancels, "no_shows": noshows,
                "backfilled": backfilled, "open_slots": open_slots,
                "lost_to_downtime": lost, "uptime_pct": round(uptime * 100, 1),
            }
        rec["report_turnaround_hours"] = round(random.uniform(14, 26) - w * 0.6, 1)
        days.append(rec)
        all_days.append(rec)

    # Weekly aggregates
    week_completed = {m: sum(x["modalities"][m]["completed"] for x in days) for m in MODALITIES}
    total_completed = sum(week_completed.values())

    # Prior auth by payer (submitted this week; decisions this week)
    auth_needed = sum(int(round(week_completed[m] * AUTH_SHARE[m] / 0.78)) for m in MODALITIES)
    # /0.78 because ~78% of submitted auths lead to a completed study inside the window
    pa = {}
    denied_total = 0
    for p, share in zip(PAYERS, PAYER_MIX):
        sub = int(round(auth_needed * share))
        if p == "Self-pay":
            pa[p] = {"submitted": 0, "approved": 0, "denied": 0, "pending": 0,
                     "avg_turnaround_hours": 0, "appeals_filed": 0, "appeals_won": 0}
            continue
        pending = int(round(sub * random.uniform(0.06, 0.12)))
        decided = sub - pending
        denied = int(decided * DENY_RATE[p] * random.uniform(0.85, 1.15) + random.random())
        approved = decided - denied
        denied_total += denied
        appeals = int(round(denied * 0.9))
        won = int(round(appeals * random.uniform(0.75, 0.85)))
        base_tat = {"Medicare Advantage": 52, "Medicaid": 70, "BCBS TX": 30,
                    "UnitedHealthcare": 40, "Aetna": 34, "Cigna": 38, "TRICARE": 46}[p]
        pa[p] = {"submitted": sub, "approved": approved, "denied": denied,
                 "pending": pending,
                 "avg_turnaround_hours": round(base_tat * random.uniform(0.9, 1.1) - w * 1.2, 1),
                 "appeals_filed": appeals, "appeals_won": won}
    staff_hours_pa = round(auth_needed * 0.38 + denied_total * 1.6, 1)  # ~23 min each + 1.6 h per denial

    # Revenue by payer (synthetic). Split completed studies across payers by mix.
    rev = {}
    for p, share in zip(PAYERS, PAYER_MIX):
        billed = 0
        for m in MODALITIES:
            billed += week_completed[m] * share * BILLED[m]
        billed = int(round(billed))
        collected = int(round(billed * COLLECT_RATE[p] * random.uniform(0.95, 1.05)))
        rev[p] = {"billed": billed, "collected_to_date": collected}

    # Referrers
    refs = {}
    for r, wt in zip(REFERRERS, REF_WEIGHT):
        n = int(round(total_completed * wt * random.uniform(0.9, 1.1)))
        if r == QUIET_REFERRER and w >= 6:
            n = int(round(n * (0.25 if w == 6 else 0.0)))
        refs[r] = n

    weeks.append({
        "week": w + 1,
        "label": f"Week {w + 1}",
        "start": monday.isoformat(),
        "end": (monday + timedelta(days=4)).isoformat(),
        "days": days,
        "studies_completed_by_modality": week_completed,
        "studies_completed_total": total_completed,
        "scheduled_total": sum(x["modalities"][m]["scheduled"] for x in days for m in MODALITIES),
        "cancellations_total": sum(x["modalities"][m]["cancellations"] for x in days for m in MODALITIES),
        "no_shows_total": sum(x["modalities"][m]["no_shows"] for x in days for m in MODALITIES),
        "backfilled_total": sum(x["modalities"][m]["backfilled"] for x in days for m in MODALITIES),
        "open_slots_total": sum(x["modalities"][m]["open_slots"] for x in days for m in MODALITIES),
        "capacity_total": sum(CAPACITY.values()) * 5,
        "uptime_pct_by_modality": {
            m: round(sum(x["modalities"][m]["uptime_pct"] for x in days) / 5, 2) for m in MODALITIES},
        "report_turnaround_hours_avg": round(sum(x["report_turnaround_hours"] for x in days) / 5, 1),
        "prior_auth_by_payer": pa,
        "staff_hours_on_prior_auth": staff_hours_pa,
        "revenue_by_payer": rev,
        "referrer_volume": refs,
    })

data = {
    "center": CENTER,
    "city": "El Paso, TX",
    "data_status": "SYNTHETIC DEMO DATA. No real patients, payers' actual figures, providers, or companies. Invented for a live demo.",
    "generated_for": "Owner-agent demo, 2026-11-05",
    "period": {"start": weeks[0]["start"], "end": weeks[-1]["end"], "weeks": WEEKS},
    "modalities": MODALITIES,
    "payers": PAYERS,
    "daily_capacity_by_modality": CAPACITY,
    "events": [{"date": MRI_DOWN_DATE.isoformat(), "modality": "MRI",
                "type": "unplanned downtime", "hours": MRI_DOWN_HOURS,
                "cause": "chiller fault (synthetic)",
                "studies_lost": next(x["modalities"]["MRI"]["lost_to_downtime"] for x in all_days
                                     if x["date"] == MRI_DOWN_DATE.isoformat())}],
    "weeks": weeks,
}
out = Path(__file__).with_name("data.json")
out.write_text(json.dumps(data, indent=1))
print("wrote", out, len(all_days), "days")
