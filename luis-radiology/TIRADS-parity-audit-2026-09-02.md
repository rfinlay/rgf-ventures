# TI-RADS Parity Audit — RadAssist Thyroid engine vs. pcheng.org
**Auditor:** Gio (independent of Alan's build) · **Date:** 2026-09-02
**Reference:** https://pcheng.org/calc/tirads.html — Phillip Cheng, MD MS, USC Radiology.
**Method:** fetched the calculator's live JavaScript (`js/custom.js` inline `calculate()`),
not the rendered legend, and compared it line-by-line to `lib/thyroid/tirads.ts` and
`lib/thyroid/recommendation.ts` at commit `b54bdd4`.
**Underlying source of truth:** Tessler FN, Middleton WD, Grant EG, et al. ACR TI-RADS
White Paper. J Am Coll Radiol 2017;14(5):587-595.

## 1. Point tables — EXACT MATCH

| Category | pcheng array | RadAssist constant | Verdict |
|---|---|---|---|
| Composition | `g1pts=[0,0,1,2,2]` | cystic 0 / spongiform 0 / mixed 1 / solid 2 / indeterminate 2 | ✅ |
| Echogenicity | `g2pts=[0,1,2,3,1]` | anechoic 0 / hyper-iso 1 / hypo 2 / very hypo 3 / cannot determine 1 | ✅ |
| Shape | `g3pts=[0,3]` | 0 / 3 | ✅ |
| Margin | `g4pts=[0,0,2,3,0]` | smooth 0 / ill-defined 0 / lobulated-irregular 2 / extrathyroidal 3 / cannot determine 0 | ✅ |
| Echogenic foci (additive) | `g5pts=[0,1,2,3]`, summed over all checked | none 0 / macro 1 / rim 2 / punctate 3, summed | ✅ |

## 2. Category mapping — EXACT MATCH

pcheng: `points==0 → TR1`, `<=2 → TR2`, `<=3 → TR3`, `<=6 → TR4`, `>=7 → TR5`.
RadAssist `categoryForPoints()` is identical.

**The 1-point case is the one worth naming.** The rendered legend on the page reads
"TR2 Not Suspicious (2 pts)", which invites an implementation to leave 1 point undefined.
The live JS assigns 1 point to TR2 via `points<=2`. RadAssist does the same. Confirmed
against behavior, not against the legend.

## 3. Warning conditions — EXACT MATCH

| Rule | pcheng condition | RadAssist | Verdict |
|---|---|---|---|
| Cystic with points | `g1==0 && points>0` | `composition==="cystic" && partial>0` | ✅ |
| Spongiform extras | `g1==1 && (any other pts)` **and forces `points=0`** | `composition==="spongiform" && partial>0`, points forced to 0 | ✅ |
| Anechoic on non-cystic | `g2==0 && g1>1 && points>0` (i.e. mixed/solid/indeterminate only — excludes cystic AND spongiform) | anechoic + composition not empty, not cystic, not spongiform, partial>0 | ✅ |

**Known cosmetic divergence, not a defect:** pcheng assigns `twarning` by overwrite, so it
displays at most one warning. RadAssist returns an array and can surface more than one.
The conditions are mutually exclusive in practice, so no case produces different guidance.

## 4. Management thresholds — EXACT MATCH to ACR

| | pcheng / ACR | RadAssist default | Verdict |
|---|---|---|---|
| TR3 follow | ≥1.5 cm (1, 3, 5 yr) | `tr3FollowUpCm: "1.5"` | ✅ |
| TR3 FNA | ≥2.5 cm | `tr3FnaCm: "2.5"` | ✅ |
| TR4 follow | ≥1 cm (1, 2, 3, 5 yr) | `tr4FollowUpCm: "1.0"` | ✅ |
| TR4 FNA | ≥1.5 cm | `tr4FnaCm: "1.5"` | ✅ |
| TR5 follow | ≥0.5 cm (annual to 5 yr) | `tr5FollowUpCm: "0.5"` | ✅ |
| TR5 FNA | ≥1 cm | `tr5FnaCm: "1.0"` | ✅ |
| TR1 / TR2 | No FNA, no follow, any size | always silent | ✅ |

Follow-up interval wording also matches the ACR schedule. All values are user-editable in
Settings → Thyroid Recommendations, so a facility that runs different thresholds can set
them without a code change.

## 5. OPEN DEFECT — shape wording (D-THY-001)

**Severity:** low clinical, **elevated medico-legal** — because THY-014 justified mode
prints this phrase into the signed report.

ACR and pcheng label the 0-point shape option **"Not taller than wide."** RadAssist labels
it **"Wider than tall"** (`lib/i18n/messages/en.ts:405`) and prints **"wider than tall"**
into the findings sentence (`lib/thyroid/templates.ts:121`).

These are not the same assertion. A nodule with equal AP and transverse dimensions is
*not taller than wide* (0 points, correctly scored) but it is *not* wider than tall.
Concise mode never printed the feature, so the wording was inert. Justified mode makes it a
positive statement of morphology attributed to the radiologist.

**Fix:** change the report phrase and the UI label to the ACR lexicon wording
("not taller than wide"). Point value unchanged. Spanish catalog needs the matching change.

**Status:** to be handed to Alan when the Phase 5.5 run completes.

## 6. Correction to an earlier verbal claim

An earlier session summary stated that Luis's spoken thresholds "matched standard ACR
TI-RADS exactly (the 3.1 cm TR3 and 2.0 cm TR4 to biopsy, the 1.2 cm TR4 to follow-up)."
**That attribution is not supported.** Those figures do not appear in the SRS or the RTM,
and they are not the ACR thresholds (which are 2.5 / 1.5 / 1.0 cm). They read as case
measurements, not rules. The SRS records the honest position: *"The largest relevant
dimension drives guideline thresholds unless Luis confirms otherwise."*

The shipped code is correct because it uses canonical ACR values. **Luis should still
confirm his own thresholds during acceptance testing** rather than have us assume the
defaults are his.
