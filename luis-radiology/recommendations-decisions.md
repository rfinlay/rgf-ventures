# RadAssist Recommendations — Luis's answers + final logic (2026-08-03)

## FINAL — confirmed + simplified by Luis (2026-08-04)
**Key workflow clarification from Luis:** the clinic usually does NOT share whether the patient has pre-existing CV risk factors or is symptomatic — he doesn't know at read time. **Therefore a calcium score of ZERO must output BOTH recommendation 1 (no risk factors) AND recommendation 2 (with risk factors) in the report**, and the downstream clinician applies whichever fits.
- **⇒ NO risk-factor toggle. NO symptomatic toggle.** (My earlier Q1/Q2 are moot — better than answered, eliminated.)
- **⇒ NO new UI inputs needed at all.** The engine runs purely on **score + MESA percentile**, which the app already has. Fully automatic.
- **Symptomatic note** (conditional "symptomatic patients may have non-calcified plaque…") **always shows for score 0** — it's part of both rec 1 and rec 2.
- **Precedence (unchanged):** borderline → the Ca score number dictates. Anchors: 50 @ 92nd → Very high; 50 @ 80th → Moderately high (75-90th pct does NOT escalate a <100 score; only >90th does).
- **LDL optional:** show both (primary + optional). **Editable text in Settings:** yes.

## Final decision tree (BUILD TO THIS)
Inputs: total Ca score + MESA percentile only. No toggles.
- **Score 0 → output BOTH:**
  - *(If no risk factors)* **Low.** 0.1% annualized MI/cardiac-death risk. LDL <160. Retest 5 yr.
  - *(If pre-existing risk factors)* **Moderate.** <1% risk. RF modification. LDL <130. Retest 5 yr.
  - + symptomatic→non-calcified-plaque note. (Both shown because risk-factor/symptomatic status is unknown at read time.)
- **Score 1-99 AND ≤90th pct →** Moderately high. 1-2% risk. RF modification. LDL <130 (<100 optional). Retest 3-5 yr.
- **Score 1-99 AND >90th pct →** Very high. RF modification. LDL <70.
- **Score 100-399 →** High / CHD risk equivalent. >2% risk. RF modification. LDL <100 (<70 optional). Retest 3-5 yr.
- **Score ≥400 →** Very high. RF modification. LDL <70.

## One minor UX default (not blocking, no need to ask Luis)
- **Placement:** default to **auto-append** the recommendation into the copied report (kills the manual paste). Text is editable/movable in Settings if he ever wants it separate.

## NEW — bug Luis reported
"The app does not populate the individual coronary Ca score values, just the Total aggregate score." → The report supports a `{{vessel_breakdown}}` token (lib/calcium/templates.ts) that should list per-vessel values; it's falling back to the "breakdown not provided" line. Alan to reproduce (enter per-vessel → confirm breakdown populates) and fix so the individual vessel scores render. Bundle with the recommendations build.

## Next — SPEC LOCKED (2026-08-04), no more Luis input needed
Luis confirmed + simplified the logic. **Clear to build.** → Alan builds recommendations engine (`buildCalciumRecommendation(score, percentile)` → recommendation block, score-0 emits both rec 1 & 2) + the **vessel-breakdown fix** (per-vessel values render, not just Total) → Neo review → Gio verify → deploy to radassist.app. No new UI inputs, no PHI, no BAA. Recommendation text editable in Settings; auto-appends to the copied report by default.
