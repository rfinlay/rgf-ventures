# Imaging-Specific Gaps: Where Is the Real Value? (Sherlock, 2026-11-03)

Input: SHERLOCK-SYSTEMS-GAP-AUDIT-2026-11-03.md, imaging-specific MISSING/PARTIAL items only.
Method: the general web search provider failed every query this session (stated plainly). All evidence below is from PubMed via NCBI E-utilities, abstracts read directly. No vendor pricing could be fetched, so every dollar figure for a product is marked as an estimate or "get quotes."

## Summary

1. **Top pick: follow-up recommendation tracking, built on top of critical results closed loop.** This is the only imaging gap with sourced evidence for *both* value levers: patient safety and malpractice exposure, plus completed follow-up exams that the center would otherwise never see. In published programs, tracking raised completion of recommended follow-up imaging from 52% to 78% (RR 1.49), from 26.5% to 59.7%, and from 41.4% to 61.1% across seven ACR sites. It is a natural **Rick build** because RadAssist already reads the report and #12 already delivers it. **Recommend: Build (extension of #12 and RadAssist), rides on whatever critical-results module the RIS provides.**
2. **Second: run peer review as peer learning, not score-based peer review.** It is required for ACR accreditation either way, so the *base* value is compliance. The upside is small but sourced: about 0.95 hours a month saved per radiologist (roughly $1,650 a year in salary time per radiologist at an academic center) and a far higher yield of useful feedback (11.2% addendum rate vs 0.27%). **Recommend: Buy (PACS peer module or ACR RADPEER); no Rick build.** Mostly compliance; be honest about that.
3. **Third: pre-visit contrast screening plus point-of-care creatinine.** The value is fewer day-of-scan delays and reschedules for outpatients who arrive without a recent eGFR. A UK economic evaluation found point-of-care testing cost-effective, driven by reduced delays; a 300-patient outpatient study found it practical, with 4.7% of patients below eGFR 45, all caught by screening. US savings are **not quantified**. **Recommend: Buy the device (CLIA waiver); small Integrate step to put the screening questions in the pre-visit intake that #5 / scheduling already sends.**
4. **Compliance-only (required, little business value beyond being allowed to bill):** CT dose monitoring/ACR DIR, MRI safety screening and zones, contrast and injector logs. Buy inside the RIS/PACS or a dose tool. Do not pitch these as ROI.
5. **Real money, but contract levers, not systems:** teleradiology/after-hours reading (per-study rate, SLA), and modality uptime/service (uptime guarantee and response terms). No published figures I would quote; get three quotes each in Phase 2.
6. Already covered in the prior audit's Tier 2 ideas (not repeated here): structured referrer e-orders, and CD import plus link-based image share.

## Top 3 in detail

### 1. Follow-up recommendation tracking on a closed-loop results workflow

**What it is.** Two layers. (a) Critical results: an urgent finding triggers a logged notice to the referrer with acknowledgment and escalation (required by the ACR communication practice parameter; the plan only says "critical results called"). (b) Non-urgent actionable findings: when a report recommends follow-up imaging ("repeat CT chest in 6 months"), the system records it, notifies referrer and patient, and checks at the due date whether the exam happened; if not, staff make one outreach call.

**Evidence (sourced).**
- How often reports recommend more imaging: unadjusted rate rose from about 6% to 12% of exams over 13 years, 5.9 million exams at one academic system (Sistrom et al., Radiology 2009, PMID 19710005). Academic hospital mix; an outpatient center's rate may differ.
- How often recommendations are followed without tracking: 39.1% overall; 66.7% for outpatients with a same-institution PCP (JACR 2021, PMID 32857982).
- What tracking does: Nodule Net nurse-navigator program, follow-up completed 78% when tracked vs 52% when not (RR 1.49, 95% CI 1.24 to 1.79); outreach was needed to prompt 28% of completions; 4 malignancies found among those (Respir Med 2022, PMID 35051877). A private 33-radiologist group's custom application raised lung nodule follow-up from 26.5% to 59.7%, with 17.2% of followed patients showing new or worsening findings (BMJ Open Qual 2019, PMID 31206047). ACR Learning Network, seven sites: follow-up imaging completion 41.4% to 61.1%; the best sites combined a tracking system with a dedicated coordinator (JACR 2025, PMID 40436300).
- Critical results alert system: policy adherence 91.3% to 95.0% at Brigham, with 41% of alerts sent non-interruptively (AJR 2014, PMID 25341129).
- Malpractice: communication failures are described as a common cause of harm and claims against radiologists (Waite et al., Clin Imaging 2018, PMID 29906784, a review). **I found no sourced claim-rate or dollar figure; do not quote one.**

**Illustrative math (ESTIMATE, not sourced; replace with the center's own numbers).** If the center does 15,000 exams a year, 5% carry a follow-up imaging recommendation (half the academic rate, conservative), and tracking lifts completion by 20 points, that is about 150 additional completed follow-up exams a year. Not all of them will return to this center; how many do is a #4 metric, not a promise.

**Buy vs build vs integrate.** Critical results logging: Buy (RIS, PACS or dictation module; require audit log). Follow-up tracking: commercial tools exist but are priced for health systems (get quotes); for one site, **Build** as an extension of #12 report delivery: RadAssist or structured report fields flag the recommendation, a due-date queue feeds the same outreach and scheduling rails #5 uses.

**Rough cost vs value.** Build: **estimate 3 to 5 weeks of Rick time**, plus a few staff hours a week for outreach (the published programs that worked had a person, not just software). Value: safety and malpractice defense (a documented loop is the defense), referrer trust, and returning exams. Value is real but not yet sized; measure it in #4.

**Risk.** Medium. The center does not order exams; the referrer does. Outreach must say "your doctor recommended" and route the order through the referrer, never solicit the scan directly (avoid any appearance of self-generated demand). Tracking creates a duty: once you track, a dropped item is worse than not tracking, so the queue needs an owner. Must not become clinical decision advice (FDA boundary, plan #13).

**Feeds.** #12 report delivery, RadAssist (recommendation extraction), #5 scheduling/outreach, #4 owner reporting (open recommendations, completion rate), #1 prior auth (follow-up exam orders).

**Pitch line.** "When your radiologist says 'repeat in six months,' we make sure it happens and the referrer knows, which protects the patient, protects the radiologist, and brings the follow-up back to your building."

### 2. Peer learning program for radiologist QA

**What it is.** ACR accreditation requires a physician peer review program. The choice is score-based review (random double reads scored 1 to 4) or peer learning (radiologists flag cases worth learning from, non-punitive, with feedback loop). Either satisfies the requirement when documented; confirm the current ACR wording in Phase 1.

**Evidence (sourced).**
- Time: peer learning took 0.76 h/month vs 1.71 h/month for score-based review per radiologist; estimated saving $1,653.68 per radiologist per year in direct salary time, $3,469.39 in productivity time; 70.4% preferred peer learning (Kwak et al., Clin Imaging 2024, PMID 38113549; academic salaries).
- Yield: addendum rate 11.2% with a peer learning tool vs 0.27% with score-based review, a 41-fold difference (AJR 2019, PMID 30403533).

**Buy vs build vs integrate.** Buy: PACS peer module or ACR RADPEER. No Rick build. RadAssist could later surface cases where a later exam disagreed with a prior read, but that is a nice-to-have.

**Rough cost vs value.** Cost: subscription or bundled module (get quotes). Value: with 1 to 3 radiologists, the sourced saving is roughly $1,700 to $5,000 a year in salary time. **Mostly compliance.** The honest pitch is "the required program, done the way radiologists prefer and that actually changes reports."

**Risk.** Low. With 1 to 3 local radiologists, peer review is hard to keep anonymous; using the teleradiology partner as an external reviewer helps.

**Feeds.** ACR accreditation binder; #4 (QA volume as a metric); RadAssist later.

**Pitch line.** "Accreditation requires peer review anyway; we set it up as peer learning, which takes radiologists less than half the time and produces about forty times more useful feedback."

### 3. Pre-visit contrast screening and point-of-care creatinine

**What it is.** The contrast risk questions (kidney disease, diabetes, prior reaction, metformin) go into the pre-visit intake sent at scheduling. Patients who screen positive and lack a recent eGFR get a fingerstick creatinine on arrival instead of being sent for a lab and rescheduled. Agent, lot, dose and any reaction are logged in the RIS (the compliance half).

**Evidence (sourced).**
- UK outpatient CT, 300 patients: 4.7% had scan-day eGFR below 45, all identified by screening; i-STAT agreed closely with the lab; 6 device failures (Radiography 2019, PMID 30777224).
- Economic evaluation: screening plus point-of-care testing for screen-positives plus lab confirmation was the cost-effective strategy (79.3% probability), driven by reduced delays in the CT pathway (PMID 34339953; UK NHS costs, QALY framework). **The US dollar value per avoided reschedule is not sourced.**

**Buy vs build vs integrate.** Buy the device and get a CLIA certificate of waiver (already on the opening checklist). Integrate: screening questions in the intake form and a "needs eGFR" flag on the schedule. Contrast and injector logging: Buy (RIS fields). Little Rick time (**estimate: days**).

**Rough cost vs value.** Device plus cartridges (get quotes). Value: fewer day-of reschedules and idle CT slots, which is a scanner-utilization benefit; size it from the center's own reschedule log in #4. Partly compliance (contrast records), partly operational.

**Risk.** Low to medium. A point-of-care test is lab testing under CLIA; staff training and QC records are required. Screening cutoffs are a radiologist policy decision, not software logic.

**Feeds.** #5 scheduling/intake, #2 eligibility (same pre-visit contact), #4 (reschedules avoided).

**Pitch line.** "A patient who shows up for a contrast CT without a recent kidney test should get a two-minute fingerstick, not a second appointment."

## The rest, ranked by honest value

| Item | Value type | Recommendation |
|---|---|---|
| Teleradiology / after-hours | Real money (read cost, coverage) | Contract lever: per-study rate, TAT SLA, reads in our PACS, credentialing. Get three quotes. No sourced price. |
| Modality uptime / service | Real money (scanner downtime = lost slots) | Contract lever: uptime guarantee, response time, remote monitoring, helium alerts, negotiated with the purchase. No sourced downtime figure. |
| Referrer e-orders | Prior auth and staff time | Already Idea 1 in the prior audit. |
| CD import / image share | Quality, referrer trust, radiologist time | Already Idea 3 in the prior audit. Avoided repeats are lost revenue for a fee-for-service center, not savings. |
| CT dose monitoring / ACR DIR | Compliance only | Buy (PACS module or dose tool). Required for accreditation; no ROI claim. |
| MRI safety screening and zones | Compliance and patient harm | Buy (e-form inside intake, implant reference subscription, badge access). No sourced efficiency figure found. |
| Protocoling | Small radiologist time | Inside RIS/PACS; standard protocol book. Not worth a build. |

## Source list
- Sistrom CL, et al. Recommendations for additional imaging in radiology reports: multifactorial analysis of 5.9 million examinations. Radiology 2009. PMID 19710005.
- Factors affecting adherence to recommendations for additional imaging of incidental findings in radiology reports. J Am Coll Radiol 2021;18(2):233-239. PMID 32857982.
- Singh H, et al. Nodule Net: a centralized prospective lung nodule tracking and safety-net program. Respir Med 2022;192:106737. PMID 35051877.
- Lim PS, et al. Process improvement for follow-up radiology report recommendations of lung nodules. BMJ Open Qual 2019;8(2):e000370. PMID 31206047.
- Wandtke B, et al. The ACR Learning Network Recommendations Follow-Up Improvement Collaborative. J Am Coll Radiol 2025;22(9):1071-1081. PMID 40436300.
- Lacson R, et al. Four-year impact of an alert notification system on closed-loop communication of critical test results. AJR 2014;203(5):933-8. PMID 25341129.
- Waite S, et al. Communication errors in radiology: pitfalls and how to avoid them. Clin Imaging 2018;51:266-272. PMID 29906784.
- Kwak DH, et al. Peer learning is both preferable and less expensive than score-based peer review. Clin Imaging 2024;106:110065. PMID 38113549.
- Improving radiology peer learning: comparing a novel electronic peer learning tool and a traditional score-based peer review system. AJR 2019. PMID 30403533.
- Point of care creatinine testing in diagnostic imaging: a feasibility study within the outpatient CT setting. Radiography 2019. PMID 30777224.
- Cost-effectiveness of point-of-care creatinine testing to assess kidney function prior to contrast-enhanced CT imaging. PMID 34339953.

Confidence: HIGH on the quoted study numbers (read from abstracts). MEDIUM on transfer to a single El Paso outpatient center (most studies are academic or hospital). LOW/none on any dollar value not explicitly sourced above.
