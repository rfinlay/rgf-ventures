# Software Requirements Specification — RadAssist (working name)
### Privacy-Preserving Radiology Workflow Automation Assistant

**Prepared by:** Rick Finlay / RGF Global Ventures
**Date:** 2026-07-30
**Sources:** Customer consultation + live workflow shadow, radiologist "Luis" (25+ yrs, 1099 independent contractor), 80-minute Plaud-recorded session 2026-07-30. Structured requirements extracted via RGF Plaud elicitation template.
**Status:** Draft v0.1 (pre-technical-discovery)

---

## 1. Purpose & Scope

### 1.1 Purpose
Define the requirements for **RadAssist**, a local, privacy-preserving AI assistant that automates the **pre-cognitive, repetitive tasks** in a radiologist's reading workflow — screen setup, prior-study retrieval, structured-data entry, calculator lookups, report pre-fill, and business/productivity tracking — **without touching the cognitive act of image interpretation**.

The guiding insight from Luis, verbatim in effect: *his pay is capped not by how fast he reads images, but by the menial clicking, typing, and organizing around each read.* Every minute of "pre-cognitive" overhead removed converts directly into throughput and income. That is the entire value thesis.

### 1.2 Scope (Pilot vs. Product)
- **In scope — Pilot:** Report pre-fill + end-of-report guideline generation + a calculator-automation demo (calcium score), running locally, alongside his existing PACS ("Exa") and dictation, non-intrusively.
- **In scope — Product roadmap:** Layout/preset persistence ("hanging protocols"), automated prior-study retrieval and side-by-side display, real-time productivity/revenue dashboard with monthly reconciliation, voice-recognition safeguards.
- **Explicitly out of scope:** Any AI that reads, interprets, or diagnoses images. RadAssist accelerates workflow; the radiologist remains the sole diagnostic authority. This is a legal, ethical, and trust boundary, not a phase-one limitation.

### 1.3 The wedge (what to build first)
Luis already believes in this — he *used to pay his son* to pre-fill Calcium Score reports (pull structured data from one system → enter into the MESA Calcium Score Calculator → get a percentile → transcribe back into the report). Rebuilding that one loop as software is the ideal pilot: high felt-pain, self-contained, no deep PACS integration required to prove, and it lands the "aha."

---

## 2. Stakeholders & Actors

| Actor | Role / Interest |
|---|---|
| **Radiologist (Luis)** — primary user | 25+ yrs, 1099 independent contractor, productivity-based pay. Reads X-ray, ultrasound, CT, MRI, cardiovascular. Wants throughput + autonomy + privacy. Has admin rights on local machines. |
| **RGF Global Ventures (Rick)** — developer/consultant | Builds and owns the software; local-agent architecture on Mac Mini + tokenized private API calls. |
| **Customer IT specialists** | Available to support Exa PACS integration; gatekeepers for back-end/workstation access. |
| **Contracting radiology groups** | Rad Partners (~4,200 radiologists) and two others Luis can introduce — the downstream market for a productized version. |
| **Corporate/PACS vendors** | Own "Exa" PACS + push standardized formats and surveillance tooling ("Mosaic"). Source of workflow friction and a constraint, not a customer. |
| **Patients** | Not users, but their PHI flows through the environment — the compliance stakeholder. |

---

## 3. Functional Requirements

| ID | The system shall… | Priority | Source | Acceptance criteria |
|----|----|----|----|----|
| **REQ-001** | Auto-extract structured fields (age, sex, ethnicity, vessel/calcium scores) from the current report/study context. | Must | Calcium-score pain point | Given a report open in Exa, ≥95% of the defined fields are parsed correctly on a 20-case test set; unparsed fields are flagged, never silently blank. |
| **REQ-002** | Auto-populate the MESA Calcium Score Calculator with extracted fields and capture the returned percentile. | Must | "Son pre-filled calcium scores" story | For a test case set, the tool returns the same percentile a manual run produces, with zero transcription steps by the radiologist. |
| **REQ-003** | Insert the calculated result + the matching guideline statement (e.g., AHA-aligned) back into the report at the correct location. | Must | Report pre-fill / guideline gen | Result + guideline text lands in the template field; radiologist reviews and accepts with one action; edit is always possible before sign. |
| **REQ-004** | Pre-fill report templates with boilerplate/standard language keyed to modality + exam type. | Must | Boilerplate pre-fill (Luis's core ask) | For the 3 highest-volume exam types, opening a case pre-loads the correct template + boilerplate; radiologist confirms/edits, never re-types from scratch. |
| **REQ-005** | Generate an end-of-report guideline/impression block appropriate to findings, for radiologist review. | Must | Pilot deliverable | Draft guideline block is produced and clearly marked "draft — review required"; nothing is finalized without explicit radiologist sign-off. |
| **REQ-006** | Persist and auto-apply screen layout, pane arrangement, and modality presets ("hanging protocols") per exam type, across workstations. | Should | Manual setup pain point | On opening an exam type, saved layout/presets apply automatically; preferences follow the user to a second workstation. |
| **REQ-007** | Detect relevant prior studies/reports on case open and display them side-by-side with the current exam. | Should | Prior-study retrieval pain point | For follow-up cases (e.g., pituitary microadenoma), the most relevant prior is surfaced automatically with configurable matching rules. |
| **REQ-008** | Provide a real-time dashboard of study queue, completed counts, and daily/monthly revenue. | Should | Productivity-visibility pain point | Dashboard reflects live queue + completed counts; revenue computes from per-study values; updates within seconds of a sign-off. |
| **REQ-009** | Produce an automated monthly reconciliation report validating study counts/payments against contracting-company statements. | Should | 1099 reconciliation need | Month-end report lists counts + expected pay; flags variances against the company's reported numbers. |
| **REQ-010** | Provide voice-recognition safeguards: clear mic-state indicator, guard against accidental/ambient dictation, reliable template-command invocation. | Could | Dictation-corruption pain point | Mic state is always unambiguous; ambient noise cannot inject text into a report during a defined lock state. |
| **REQ-011** | Assist the critical-findings communication protocol (e.g., pull contact, pre-stage the required documentation) on a flagged urgent finding. | Could | Pulmonary-embolism scenario | On a radiologist-flagged critical finding, the protocol checklist + contact path is pre-staged; radiologist remains the actor. Liability-sensitive — assist only, never auto-notify. |
| **REQ-012** | Operate as a non-intrusive companion (separate window or browser extension) alongside Exa + dictation without disrupting them. | Must | Compatibility expectation | Installing/running RadAssist causes no change to existing PACS/dictation behavior; it can be dismissed instantly. |
| **REQ-013** | Learn user-specific preferences (layouts, presets, common steps) over time and apply them automatically. | Should | Privacy-first assistant expectation | After N cases of an exam type, the tool proposes the user's established setup without manual configuration. |

---

## 4. Non-Functional Requirements

- **NFR-1 — Privacy / PHI (HIGHEST):** All patient data processing stays **local by default**. Any AI model call must go through **tokenized, private API sessions** with PHI minimized/de-identified before transmission; work product and data remain owned and stored on the radiologist's machine. No PHI to third-party cloud storage. This is the architectural backbone, driven both by HIPAA and by Luis's explicit data-ownership concern.
- **NFR-2 — Compliance:** Design toward HIPAA safeguards (access control, audit logging of what the assistant touched, encryption at rest + in transit). Maintain a defensible boundary: the tool does not make diagnostic decisions.
- **NFR-3 — Non-intrusiveness:** Zero forced change to existing PACS/dictation workflow; runs alongside, dismissible instantly. Adoption depends on this.
- **NFR-4 — Performance:** Pre-fill/extraction actions complete in seconds so the tool saves time rather than adding a wait.
- **NFR-5 — Autonomy preservation:** The radiologist reviews and can override every automated insertion before sign-off. The tool proposes; the human disposes.
- **NFR-6 — Reliability:** No action may corrupt or finalize a report without explicit confirmation (directly answers the voice-recognition corruption fear).
- **NFR-7 — Portability:** Preferences and behavior follow the user across workstations.
- **NFR-8 — Compatibility:** Windows workstation + Chrome + Exa PACS environment; the agent host is a local Mac Mini.
- **NFR-9 — Scalability (product):** Architecture should generalize from one radiologist to a per-seat/per-service model for larger groups.

---

## 5. User Stories

- As a radiologist, I want the report template pre-filled with the right boilerplate the moment I open a case, so that I start reading instead of typing. (REQ-004)
- As a radiologist, I want calcium-score data extracted, calculated, and written back automatically, so that I stop doing my son's old data-entry job. (REQ-001, REQ-002, REQ-003)
- As a radiologist, I want a guideline-aligned impression drafted for my review, so that I finalize faster without losing my interpretive voice. (REQ-005)
- As a radiologist, I want my screen layout and presets to appear automatically per exam type, so that I skip the manual setup clicks every case. (REQ-006)
- As a radiologist, I want relevant prior studies surfaced side-by-side automatically, so that I don't hunt for them and don't miss interval change. (REQ-007)
- As an independent contractor, I want a live view of my queue, output, and revenue plus a month-end reconciliation, so that I can optimize my day and verify I'm paid correctly. (REQ-008, REQ-009)
- As a radiologist, I want unambiguous mic state and dictation guards, so that ambient noise never corrupts a report. (REQ-010)
- As a privacy-conscious clinician, I want everything to run locally and keep my data mine, so that I adopt this without compliance fear. (NFR-1, REQ-013)

---

## 6. Business Rules & Constraints

- **BR-1:** The assistant never performs diagnostic interpretation; it handles pre-cognitive tasks only.
- **BR-2:** No report content is finalized/signed without explicit radiologist confirmation.
- **BR-3:** PHI never leaves the local environment un-minimized; cloud AI receives only what is necessary and de-identified where possible.
- **BR-4:** The tool must coexist with, not replace, Exa PACS and the existing dictation system.
- **BR-5 (constraint):** Corporate/vendor push toward standardized formats and surveillance tooling ("Mosaic," eye/muscle tracking) conflicts with the radiologist's autonomy — RadAssist must side with clinician control, not corporate surveillance.
- **BR-6 (constraint):** Compensation is productivity-based; every feature is judged by time saved per case.

---

## 7. Data & Integrations

- **PACS:** "Exa" suite, Windows workstations, accessed via Chrome. Integration points TBD at technical-discovery call (REQ to schedule). Admin rights available on local machines; customer IT can support.
- **Calculator:** MESA Calcium Score Calculator (web-based) — obtain exact input schema + URL for integration (action item).
- **Report templates:** Radiologist uses custom templates + voice-recognition macros today.
- **AI models:** Claude / ChatGPT via tokenized private API sessions from a local agent (Mac Mini).
- **Dictation/voice system:** Third-party; RadAssist interoperates but does not own it.
- **Contracting-company statements:** Monthly study/payment data for reconciliation (format TBD).

---

## 8. Assumptions
- Luis's environment (Windows + Chrome + Exa) is stable and representative of the target market.
- Customer IT will grant inspection/back-end access without disrupting live reading.
- A local-agent + tokenized-API architecture satisfies both HIPAA posture and Luis's ownership requirement.
- The MESA calculator and report templates are automatable via parsing + form-fill (to be validated in discovery).

## 9. Dependencies
- Technical-discovery session with customer IT to map Exa integration surface.
- Back-end/workstation access for inspection.
- MESA calculator input schema.
- Sample de-identified reports for parser training/testing.

## 10. Risks
- **R-1 (High):** PHI handling/HIPAA exposure if de-identification or local-boundary is imperfect. Mitigation: local-first, minimize-before-send, audit logging, legal review before any real-PHI pilot.
- **R-2 (High):** PACS integration surface may be closed/limited (vendor lock). Mitigation: browser-extension/overlay approach that doesn't require deep PACS APIs for phase one; validate in discovery.
- **R-3 (Med):** Liability on the critical-findings feature if the tool is perceived to own notification. Mitigation: assist-only, human remains the actor.
- **R-4 (Med):** Voice-recognition improvements may depend on a third-party system RGF doesn't control. Mitigation: scope to safeguards/guards around it, not replacement.
- **R-5 (Med):** Scope creep from "automate everything" — Luis listed many asks. Mitigation: pilot the wedge, prove value, expand.
- **R-6 (Low/strategic):** Single-customer dependency. Mitigation: design for the broader 1099-contractor market Luis can introduce.

## 11. Open Questions (blockers to a trustworthy spec)
- What exactly does Exa expose (API, HL7/FHIR, DICOM, or screen-only)? Determines integration approach.
- MESA calculator: exact input fields + whether an API exists vs. screen-scrape/form-fill.
- Which 3 exam types are highest-volume for the pilot pre-fill?
- What is the acceptable PHI boundary for the cloud-model calls — fully local model, or de-identified cloud calls?
- Per-study revenue values + contracting-company statement format for the dashboard/reconciliation.
- Regulatory posture: does any pilot feature approach "clinical decision support" that would trigger FDA/coverage considerations? (Interpretation is out of scope specifically to avoid this — confirm the guideline-generation feature stays on the safe side.)

## 12. Action Items (from the session)
- [ ] Technical discovery call with customer IT on Exa integration points — within 7 days.
- [ ] Obtain back-end/workstation access for inspection (no workflow disruption) — next working day.
- [ ] Build + deliver initial pilot (report pre-fill + end-of-report guideline generation) — "next few days."
- [ ] Add real-time productivity/revenue dashboard + monthly reconciliation to pilot scope.
- [ ] Obtain MESA Calcium Score Calculator details for integration — within 3 business days.
- [ ] Draft + send proposal (workflow automation tool + requirements summary) — within 10 days.
- [ ] Prepare POC demo (browser extension) for layout/preset persistence — within 21 days.
- [ ] Document voice-recognition improvement requirements + prior-study detection data model — within 14 days.
- [ ] Prepare commercialization plan (pricing + support models) for broader rollout — post-pilot.
- [ ] Schedule follow-up to demo prototype + gather feedback — within 3 weeks.
