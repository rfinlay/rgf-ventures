# Prioritized Automation List — RadAssist
### Path forward for an app Luis would love
**RGF Global Ventures — 2026-07-30**

Ranking logic: **value = time saved per case × cases per day** (his pay is productivity-based, so this is literally his income), scored against **build effort** and **integration risk** (how much it depends on cracking the Exa PACS or third-party systems). The winners are high-value items we can ship **without** first solving deep PACS integration.

---

## Tier 1 — The Pilot (build now, "next few days")

**1. Report Pre-Fill + Calcium-Score Automation (the wedge)**
- **Why first:** This is the exact task Luis *paid his son to do*. He already believes in it, the pain is visceral, and it's self-contained. Nail this and you've sold him the whole vision.
- **What it does:** Extract structured fields → auto-run the MESA Calcium Score Calculator → write the percentile + guideline statement back into the report. Plus pre-fill modality/exam-type boilerplate on case open.
- **Value:** High. **Effort:** Medium. **Integration risk:** Low (parse + form-fill + template insert; no deep PACS API needed).
- Requirements: REQ-001, REQ-002, REQ-003, REQ-004, REQ-005.

**2. End-of-Report Guideline/Impression Draft**
- Pairs with #1 — drafts a guideline-aligned impression block for his review. Same pilot, same demo.
- **Value:** High. **Effort:** Low-Med. **Risk:** Low (draft-only, human signs off).
- Requirement: REQ-005.

> **Pilot success = Luis watches the calcium-score loop run itself once.** That's the moment.

---

## Tier 2 — Fast Follow (weeks after pilot proves out)

**3. Real-Time Productivity & Revenue Dashboard + Monthly Reconciliation**
- **Why high on the list:** It's **standalone** (doesn't need PACS integration to be useful — it can start from study logs/counts), it hits his 1099 "am I being paid correctly?" pain, and **we already own this pattern.** This is the Command Center / BudgetIQ engine re-skinned for radiology throughput. Strong ROI for low net-new effort.
- **Value:** Med-High. **Effort:** Low-Med (reuse existing dashboard engine). **Risk:** Low.
- Requirements: REQ-008, REQ-009.

**4. Layout / Preset Persistence ("Hanging Protocols") via Browser Extension**
- Auto-applies his screen splits, pane arrangement, and presets per exam type, across workstations. Kills the per-case setup clicking.
- **Value:** High. **Effort:** Med-High (Chrome extension against Exa's web UI). **Risk:** Med (depends on Exa's DOM/behavior — validate in discovery).
- Requirements: REQ-006, REQ-013.

---

## Tier 3 — Deeper Integration (requires the technical-discovery outcome)

**5. Automated Prior-Study Retrieval + Side-by-Side Display**
- Surfaces the relevant prior automatically on case open (e.g., pituitary microadenoma follow-up).
- **Value:** High. **Effort:** High. **Risk:** High — needs real PACS query access. Gated on what Exa exposes.
- Requirement: REQ-007.

**6. Voice-Recognition Safeguards**
- Mic-state clarity + ambient-noise dictation guards to stop report corruption.
- **Value:** Med. **Effort:** High/uncertain. **Risk:** Med (third-party dictation system he doesn't own). Scope to guards around it, not replacement.
- Requirement: REQ-010.

---

## Tier 4 — Careful / Later (value real, but liability-sensitive)

**7. Critical-Findings Communication Assist**
- Pre-stage the protocol checklist + contact path on a flagged urgent finding (e.g., PE). **Assist only — the radiologist stays the actor; the tool never auto-notifies.** Liability boundary must be explicit.
- **Value:** Med. **Effort:** Med. **Risk:** Med-High (liability). 
- Requirement: REQ-011.

---

## Cross-cutting foundation (not a feature — the backbone of all tiers)
**Privacy-preserving local-agent architecture (NFR-1/2).** Local-first processing, PHI minimized before any tokenized cloud-model call, data + work product owned on his machine, audit logging. This is both the HIPAA answer and Luis's stated dealbreaker. Every tier rides on it.

---

## The strategic read (my recommendation to you, papi)

1. **Ship Tier 1 as the pilot, fast.** It's the promise he already made to himself. Small, safe, high-drama payoff. Don't let scope creep push it past "next few days."
2. **Lead Tier 2 with the dashboard** because it's a **near-free win for us** — it's the Command Center/BudgetIQ engine you already built and hardened. That's a real strategic edge: you're not starting from zero on the business-ops half of this product.
3. **Gate Tiers 3-6 on the technical-discovery call.** Don't promise prior-study retrieval or voice fixes until you know what Exa actually exposes. The browser-extension/overlay path is your hedge if the PACS is closed.
4. **Keep the diagnostic boundary sacred.** "We accelerate your workflow; we never read your images" is the line that keeps this out of FDA/clinical-decision-support territory and keeps clinician trust. It's a feature, not a limitation — say it out loud in the proposal.
5. **The market is the quiet headline.** Luis can introduce you to 3 groups incl. Rad Partners (~4,200 radiologists), and the field is shifting to 1099 contractors who each individually feel this pain. Build for Luis, architect for the seat-based product. This is a genuine RGF Ventures product line, not a favor for a neighbor.
