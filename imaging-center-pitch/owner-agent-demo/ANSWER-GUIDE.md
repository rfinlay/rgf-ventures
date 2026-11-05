# Owner-Agent Demo: Answer Guide (SYNTHETIC)

Center: "Your New Center", El Paso. MRI + CT + X-ray + ultrasound.
Data window: 8 weeks, Mon 2026-09-07 through Fri 2026-10-30. "Last week" = Week 8 (Oct 26 to 30).
Every number below comes from `data.json`. Verify live with `python3 query.py week 8`, `payers`, `revenue`, `referrers`, `uptime`, `compare`, `days 8`.
All dollar figures are invented. No real patients, providers, or companies.

## 1. "How did last week go?"
Good week, best volume yet. 350 studies completed (71 MRI, 87 CT, 128 X-ray, 64 ultrasound), up from 339 the week before.
412 were scheduled; 82 cancelled (20%) and 9 no-showed (2%). We refilled 29 of those slots from the waitlist.
Every scanner ran at 100% uptime. 9 prior auths were denied and we already appealed all 9, winning 8.
Recommendation: push the waitlist harder on Fridays, that is where most of the 100 empty slots sit.
(synthetic demo data)

## 2. "Which payer denies us the most, and what is it costing?"
Medicaid. 11.2% of its decided auths were denied over 8 weeks (31 of 278), about double anyone else. Medicare Advantage is next at 6.3%.
Each denial burns roughly 1.6 staff hours on rework plus a delayed or lost study. 31 denials is about 50 staff hours and up to $25k of billed MRI and CT held up.
Medicaid also takes longest to answer: 67 hours average versus 25 for BCBS TX.
Recommendation: build a Medicaid-specific checklist (clinical notes attached up front) and submit those auths first thing Monday.
(synthetic demo data)

## 3. "How many appeals did we win?"
61 of 75 appeals won over 8 weeks, an 81% win rate. Last week we filed 9 and won 8.
That means most denials are paperwork, not medical necessity. The first submission is what needs fixing.
Medicaid (23 of 31) and Medicare Advantage (17 of 23) account for nearly all appeals.
Recommendation: move the appeal evidence into the initial request so we stop paying for the same study twice in staff time.
(synthetic demo data)

## 4. "How many empty slots did we have, and how many did we fill?"
Last week: 450 slots of capacity, 350 completed, 100 open. We backfilled 29 cancelled slots from the waitlist.
Friday is the softest day (27 open) and Tuesday the tightest (15 open).
Open slots are down 31% from the first month (654 in weeks 1 to 4, 449 in weeks 5 to 8) as referrals ramp.
Recommendation: a same-day text to the waitlist when a cancellation lands would turn more of the 82 weekly cancellations into completed studies.
(synthetic demo data)

## 5. "How is MRI uptime?"
100% last week. One event in the window: Wednesday Oct 21, chiller fault, MRI down 6.5 hours, 10 studies lost or rescheduled.
That pulled Week 7 MRI uptime to 88% and the 8-week average to 98.5%. CT, X-ray, and ultrasound are at or near 100%.
MRI volume recovered the next week (60 then 71).
Recommendation: confirm the chiller service contract response time is under 4 hours; it is the only single point of failure on the floor.
(synthetic demo data)

## 6. "Which referrer went quiet?"
Referrer D. They sent 30 to 39 studies a week for six weeks, then 8 in Week 7 and zero last week.
Nothing changed on our side that week except the MRI outage on Oct 21, so the timing is worth a direct call.
Everyone else grew. Referrer A is your top source at 69 last week, up from 46 in Week 1.
Recommendation: call Referrer D this week; that is roughly 35 studies a week, about 10% of volume.
(synthetic demo data)

## 7. "How many staff hours are going to prior auth?"
97 hours last week, up from 79 in Week 1. That is about 2.5 full-time people just on authorizations.
It tracks volume: 207 auths submitted last week at roughly 23 minutes each, plus about 1.6 hours of rework per denial.
Total over 8 weeks: 705 hours.
Recommendation: this is the first job to automate; a front-end check that catches missing notes before submission cuts both the base time and the denial rework.
(synthetic demo data)

## 8. "What was the busiest day?"
Tuesday Oct 27 with 75 completed studies (15 MRI, 19 CT, 28 X-ray, 13 ultrasound) against 87 scheduled.
Tuesday is consistently the peak; Friday is consistently the lightest (63 completed, 27 open slots).
Recommendation: shift one tech's Friday hours to Tuesday morning and open the Friday slots to walk-in X-ray.
(synthetic demo data)

## 9. "What are our turnaround times?"
Report turnaround averaged 18.5 hours last week; the 8-week trend is from about 19 hours down to 18.
Prior auth turnaround averaged 37 hours across payers last week. BCBS TX is fastest at 25 hours; Medicaid slowest at 67.
Both are inside a normal range for a new center but not yet where referrers notice.
Recommendation: set a public target of same-business-day reads for X-ray and 24 hours for MRI and CT, and track it weekly.
(synthetic demo data)

## 10. "How does this month compare to last month?"
Weeks 5 to 8 versus weeks 1 to 4: completed studies up 18% (1,146 to 1,351), billed up 17% ($586k to $686k).
Open slots down 31%. Denial rate improved from 6.2% to 5.2%. Report turnaround improved by about an hour.
The one number that went the wrong way is staff hours on prior auth, up 44 hours, because volume grew.
Recommendation: the ramp is healthy; the constraint moving forward is auth staffing, not demand.
(synthetic demo data)

## 11. "What should we fix first?"
Medicaid prior auths. It is the worst denier (11%), the slowest responder (67 hours), and 20% of your volume.
Fixing the first submission would cut roughly half the appeal work and free about 25 staff hours a month.
Second: call Referrer D. Third: Friday backfill.
Recommendation: one week of Medicaid auth cleanup before anything else; it is the cheapest fix with the clearest payback.
(synthetic demo data)

## 12. "How do collections compare to what we billed?"
8 weeks: $1.27M billed, $601k collected so far, 47%. Last week alone: $180k billed, $84k collected to date.
Collection rate by payer: self-pay 71%, BCBS TX 59%, Aetna 56%, UnitedHealthcare 55%, Cigna 54%, TRICARE 46%, Medicare Advantage 42%, Medicaid 30%.
Early weeks are still paying in, so the 47% will rise; it is not a collections problem yet.
Recommendation: watch Medicaid and Medicare Advantage aging at 60 days; together they are 46% of billed and the slowest to pay.
(synthetic demo data)

## Quick reference (Week 8)
| Metric | Value |
|---|---|
| Scheduled / completed | 412 / 350 |
| Cancellations / no-shows | 82 (19.9%) / 9 (2.2%) |
| Capacity / open / backfilled | 450 / 100 / 29 |
| Auths submitted / approved / denied / pending | 207 / 181 / 9 / 17 |
| Appeals filed / won | 9 / 8 |
| Staff hours on prior auth | 97.2 |
| Report turnaround | 18.5 h |
| Billed / collected | $180,231 / $84,368 |
| Busiest day | Tue Oct 27, 75 studies |
| Quiet referrer | Referrer D (0, was ~35/wk) |
