# RadAssist / Ramos Project — Overall Plan & Architecture (2026-08-03)

## Vision (one sentence)
RadAssist becomes Dr. Ramos's radiology-workflow assistant: **today a thin cloud UI he clicks himself, tomorrow the same capabilities operated by a local AI agent on an on-prem appliance**, with PHI staying in his office under a signed BAA. The UI never goes away; it's the window. The agent is the operator.

## The core architecture decision: NOT microservices. Modular monolith of agent-callable capabilities, split only at the compliance boundary.
- **One product for Luis (RadAssist), not a fleet of apps.** His experience stays unified: one login, one place. This is what Rick wants and it's correct for a single-clinician pilot.
- **Internally, every feature is a clean, agent-callable capability** (defined input → defined output): calcium scoring, recommendations engine, report templating, later documentation-prefill, later reconciliation, later PACS integration. Both the UI *and* the future local agent call the SAME capabilities. This is the [[build-agent-native-tools]] principle: the agent is the operator, the UI is one thin window, designed in from the start.
- **Why not classic microservices:** for a solo founder + one-client pilot, microservices = operational sprawl (separate deploys, networking, monitoring) with no payoff. Steven's rule was "no sprawl." A modular monolith gives us the same clean seams without the tax. We split into a separate deployment ONLY where a real boundary forces it.
- **The one real boundary = compliance (PHI).** This is a HYBRID deployment, and it mirrors the exact hybrid-cloud lesson Rick just wrote for CLCS: sensitive data stays local, elastic/UI lives in the cloud.
  - **Non-PHI capabilities** (calcium math, recommendations logic, templating) → run in the **cloud UI now** (Vercel + Neon), no BAA needed, fast feedback from Luis.
  - **PHI-touching capabilities** (anything reading patient data or PACS: reconciliation, HL7/DICOM, the agent operating on real records) → run **on the local Mac mini appliance** in his office, behind the signed BAA, surfaced through the same RadAssist UI.
- **Result:** one app to Luis, modular inside, and when we add the appliance we plug the local capabilities in behind the same window instead of rebuilding.

## Phased plan (5-phase, refined 2026-08-04)
- **Phase 1 (NOW) — Calcium wedge + recommendations.** Secured calcium tool (done, live, Luis loves it). Add the **auto-recommendations engine** (his ask — spec below) + **vessel-display bug fix** + **PHI-free in-app telemetry/feedback**. PHI-light (no patient identifiers, manual entry) → stays **cloud, no BAA**. Goal: prove value, deepen trust, gather feedback.
- **Phase 2 — Documentation / boilerplate prefill.** The original known requirement: auto-fill standard/repeated report text. Extends the report engine. Still PHI-light where entry is manual → cloud, likely no BAA.
- **Phase 3 — Reconciliation dashboard + workflow tools.** The dashboards discussed. First piece that touches real workflow/patient data → moves to the **local appliance path** (BAA required).
- **Phase 4 — PACS integration (Luis-driven).** The **Mac mini appliance is delivered** to his office. RadAssist runs **on-prem** and integrates with **Exa PACS** (HL7/DICOM): scores flow in, report writes back — **no more manual entry/paste**. **Luis still drives it (clicks).** While he works, the appliance **observes and learns** his patterns/preferences (all local) — this is the training groundwork for Phase 5. Requires **BAA + local box**. PHI never leaves the appliance.
- **Phase 5 — Autonomous local agent.** The agent **takes over the clicking**, operating RadAssist's tools for Luis on that same appliance, using what it learned in Phase 4. Local, BAA-gated, PHI stays on-prem.

**Key clarifications (settled 2026-08-04):**
- **PACS integration = local, by necessity.** The moment RadAssist reads from / writes to Exa, it touches PHI, and PHI must stay on-prem — so a cloud RadAssist can't integrate with the PACS. The "appliance" isn't a step *after* integration; it's *where* the integration runs. Integration and going-local happen together (Phase 4).
- **Two separate machines:** (1) Luis's **existing PACS workstation** gets Tailscale + OpenSSH for **read-only RECON only** (temporary, so Gio can learn the Exa integration surface); (2) the **Phase 4 appliance = a separate Mac mini** Rick delivers onto Luis's LAN (runs RadAssist + integration + agent locally, talks to Exa over the LAN). Don't run the stack on his clinical workstation.
- **Ownership gate CLEARED (2026-08-04):** it's Luis's own machine and he has admin — no hospital/practice IT policy in the way.
- **Rollout logic:** UI tools he clicks himself (Phases 1-4) build trust → agent takes the wheel (Phase 5).

## UI/UX Enhancements Backlog (added 2026-08-05, Rick's request)
Cross-cutting polish, not phase-blocking. Fire when RadAssist resumes (currently ON HOLD pending Luis's feedback). Both route Alan → Neo → Gio → deploy on Rick's "ship it."
- **Spanish language support (EN/ES).** El Paso is a bilingual border region. Add a language toggle covering the UI, the guides, and the generated report boilerplate + recommendation text. **Clinical caveat:** the recommendation and report medical wording must be translated accurately and **reviewed/approved by Luis before use — he is a native Spanish speaker from Mexico, so target Mexican Spanish medical phrasing and treat him as the authority on the clinical wording.** Never ship machine-translated clinical text unreviewed. Approach: extract UI/report strings to a locale layer (EN default, ES Luis-reviewed); keep the AJ-130/MESA terms and vessel names as clinicians expect them.
- **Light / Dark mode.** Port the **Command Center G3** pattern (proven): cookie-driven SSR palette (no FOUC), brand-derived dark tokens, WCAG AA contrast, keep the strict nonce CSP + PWA/offline shell intact; header toggle + `prefers-color-scheme` default. Genuinely useful here — radiologists read in dim reading rooms. **CRITICAL caveat: the copied/exported report must NEVER carry the theme.** "Copy report" (and any export) must always output STANDARD formatting — plain text / normal dark-on-light — regardless of the app's theme. Dark mode is a display-only concern; if dark styling (white-on-dark) bled into the copied content it would paste unreadable into his PACS/ExaTrans dictation. Test explicitly: toggle dark mode → Copy report → confirm the pasted text is standard, not themed.

## Next RadAssist refinement backlog (added 2026-09-01 from Luis's live-use feedback)
**Priority rule:** Luis's Thyroid Report Project is the active discovery priority. These Calcium Score refinements run as a separate follow-on track. Do not deploy before Rick reviews the demo and explicitly says ship it.

- **Full-image usability:** reduce or eliminate the need for Luis to manually crop large screenshots before AI pre-fill.
- **Automatic region detection:** identify the likely measurement/result block in a full screenshot and analyze that region rather than unrelated page content.
- **Crop preview and adjustment:** show the detected region before extraction and let Luis quickly resize or reposition it when needed.
- **Confidence-based fallback:** when the selected region is too broad, noisy, or ambiguous, explain why and request a tighter crop instead of guessing.
- **Large-image preprocessing:** test scaling, contrast, thresholding, and multi-region OCR against representative screenshots from Luis's actual monitors and scanner output.
- **No-regression requirement:** cropped screenshots that already work well must remain accurate and fast.
- **Value measurement:** capture privacy-safe operational metrics or a short weekly worksheet covering studies processed, average time per study, crop retries, corrected fields, and estimated time saved. No patient identifiers or clinical values in telemetry.
- **Baseline still owed by Luis:** confirm pre-RadAssist versus current weekly study volume, average minutes per study, and correction/rework rate. The last known baseline is approximately 15 studies at 20 minutes each.
- **Meeting validation:** observe the complete Calcium Score workflow onsite and identify whether cropping is the true bottleneck or a symptom of source-format variation.

**Delivery sequence:** scope during the thyroid discovery visit → Alan builds on a non-production branch → Neo reviews → Gio verifies with full-size and cropped samples → Rick demos to Luis → deploy only on Rick's explicit approval.

## Phase 1 feature spec — Calcium Recommendations Engine (v0.1, pending Luis confirmation)
**What:** given the score + MESA percentile + a couple of clinical flags, output the matching guideline recommendation block (risk level, annualized MI/cardiac-death risk %, LDL target, retest interval, notes), appended to the report so Luis stops pasting it by hand.

**Inputs:** calcium score, MESA percentile (already computed), **new: "cardiovascular risk factors present? (y/n)"**, **new: "symptomatic? (y/n)"** (pending Q1/Q2).

**Decision table (from Luis's guidelines, needs precedence confirmation — Q3/Q4):**
- Score 0, no CV risk factors → **Low.** ~0.1% annualized MI/cardiac-death risk. LDL <160. Retest 5 yr. (+ symptomatic→non-calcified-plaque note)
- Score 0, with CV risk factors → **Moderate.** <1% risk. Risk-factor modification. LDL <130. Retest 5 yr. (+ symptomatic note)
- Score 1-99 AND <75th pct → **Moderately high.** 1-2% risk. RF modification. LDL <130 (<100 optional). Retest 3-5 yr.
- Score 100-399 OR >75th pct → **High (CHD risk equivalent).** >2% risk. RF modification. LDL <100 (<70 optional). Retest 3-5 yr.
- Score <100 AND >90th pct → **Very high.** RF modification. LDL <70.
- Score >400 → **Very high.** RF modification. LDL <70.
- **Precedence rule (to confirm): higher risk category always wins when bands overlap.**

**Output:** recommendation block appended to the copyable report; **editable in Settings like the template** (pending Q5).

**Build path:** agent-callable module `buildCalciumRecommendation({score, percentile, riskFactors, symptomatic, template})` → same module the future agent calls. Route: Alan builds → Neo reviews → Gio verifies → deploy to radassist.app. No BAA (no PHI).

**Clinical safety framing:** the app surfaces **Luis's own guidelines**; he remains the physician who reviews and signs. We encode his authority, we don't invent medicine.

## Open questions for Luis (Rick sends; Gio never contacts client)
See chat / below. Once answered → finalize spec → Alan builds.
