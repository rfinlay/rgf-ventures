# Exa PACS/RIS Integration Research — for the Dr. Luis Ramos radiology workflow-automation suite

**Author:** Sherlock (research persona) → Gio
**Date:** 2026-07-31
**Status:** Research/report only. Read-only. No actions taken, no environment touched. No PHI involved.
**Subject instance:** Exa accessed at `exa.swrxsyonline.com` (Dr. Luis Ramos reads here).

> **Method + honesty note.** Konica Minolta publishes marketing material for Exa but **no public developer portal, API reference, or partner/SDK documentation**. I confirmed product architecture and reporting features from primary vendor pages. During this session two search backends degraded (DuckDuckGo served CAPTCHA challenges; Bing returned name-collision/irrelevant results — "Exa" also names a popular AI **search** company `exa.ai`, which pollutes queries). Where I could not fetch a live source, I say so and rate confidence accordingly, and I clearly separate **Verified / Inferred / Unknown**. The most important integration facts will have to be confirmed during your hands-on recon of *his specific* hosted instance — that is called out explicitly at the end.

---

## Q1 — What is Exa?

**Verified (High):**
- **Exa is the "Exa Platform" (a.k.a. Exa PACS|RIS) by Konica Minolta Healthcare Americas** — an integrated **PACS + RIS + Billing** platform for medical imaging. Source: https://healthcare.konicaminolta.us/healthcare-it/exa-pacs and https://healthcare.konicaminolta.us/exa-pacsris
- **Architecture is browser-based, "Zero Footprint" (ZFP) with Server-Side Rendering (SSR).** The server renders images; DICOM data is *not* transmitted to or stored on the workstation. "No downloads, plug-ins or installations… from any computer, tablet or smartphone, any OS, any browser." SSR removes prefetching, so priors load immediately. This also means **less PHI on the endpoint** ("no data transferred to or stored on workstations"). Sources: KM Exa PACS page (above); KM RIS page (above); mirror confirmations at https://radiologyimagingsolutions.com/konica-minolta-exa-pacs/ and https://healthcare.toolsinfo.com/tool/konica-minolta-exa-pacs
- **Single integrated database across modules** — one unified patient chart; a change propagates platform-wide. Source: KM RIS page.
- Modules/features named by KM: diagnostic ZFP viewer, specialty viewers (PET, DBT/mammo, surgical video, cardiology, ortho), **smart worklist** (highly configurable columns/filters/tabs), **Performance Dashboard** (exam volume, radiologist performance, referrer profitability), TAT/STAT meters, **Exa Chat**, **Exa Peer Review**, web-based **report management** (dictation/transcription, approvals, online publication, auto-faxing), and **custom workflow design engine** (drag-and-drop status pipeline). Sources: KM Exa PACS page; radiologyimagingsolutions.com.
- KM markets Exa on **AWS** ("Partnership with AWS provides the platform of the future"). Source: KM Exa PACS page.

**Inferred (Medium–High):** `exa.swrxsyonline.com` is almost certainly a **hosted / reseller / imaging-center deployment** of the Exa Platform — i.e., Exa delivered as a web tenant on an operator's domain (`swrxsyonline.com`) rather than a Konica-Minolta-branded URL. This pattern is consistent with KM's model of selling Exa through imaging-solution resellers (multiple resellers surfaced: Radiology Imaging Solutions, RSI Imaging, Associated X-Ray, Browns Medical, Alpha Medical). It is likely a multi-tenant or single-tenant hosted instance operated by an imaging center or teleradiology group Dr. Ramos reads for. **Unknown:** who operates `swrxsyonline.com`, whether it's KM-hosted-on-AWS vs. reseller-hosted, and the exact version. → **Confirm hands-on.**

---

## Q2 — Integration surface (the core question)

**This is where public documentation runs out.** KM does not publish an Exa API reference, developer program, or SDK that I could locate across multiple engines. Absence of a public developer portal is itself a finding: **you should not architect against a documented Exa REST API — assume there isn't one until proven otherwise on his instance.**

### What is Verified
- **HL7 v2 interfacing is a first-class, supported integration path.** KM's own "Exa Platform Implementation Overview" lists **"3rd Party HL7 Interface Resources… HL7 integration will require completion of the interface to the third party EMR vendor."** This confirms Exa exposes/consumes HL7 v2 interfaces (the standard ORM orders / ORU results / ADT flows) as part of a normal implementation, but they are **provisioned by KM professional services per site**, not self-serve. Source (snippet from KM PDF): https://healthcare.konicaminolta.us/sites/default/files/2023-03/Exa%20Platform%20Implementation%20Overview%20V3.pdf  *(Confidence: High that HL7 exists; Medium on exact message types available on his instance.)*
- **DICOM is inherent.** Exa is a full PACS; it necessarily supports DICOM C-STORE (receive), Query/Retrieve (C-FIND/C-MOVE), and Modality Worklist. SSR means rendered pixels are served from the server, but the underlying archive is DICOM. *(Confidence: High as a category; the specific AE-title/port availability to a third party is site-config. → confirm hands-on.)*
- **Billing/EMR integrations exist in practice** — KM references partners like **Imagine Software** (RCM/billing) and **DataFirst** on the platform, i.e., third parties do integrate, via HL7/interfaces arranged through KM. Source: KM RIS page (partner mentions).

### What is Inferred / Unknown (must confirm hands-on)
| Interface | Status | Notes |
|---|---|---|
| **HL7 v2 (ORM/ORU/ADT)** | **Verified exists**, per-site provisioned | Realistic rail to (a) receive orders/worklist and (c-ish) emit/receive **final report text** as ORU. |
| **DICOM C-STORE / Q-R / MWL** | Inferred High (it's a PACS) | Rail to read studies/worklist and route images to an on-prem AI. |
| **DICOMweb (QIDO-RS / WADO-RS / STOW-RS)** | **Unknown** | Not documented publicly. Many modern web PACS expose it internally; his ZFP viewer likely talks a web API to the server, but whether a *documented, third-party-usable* DICOMweb endpoint is exposed is unconfirmed. **High-value thing to probe on his instance.** |
| **FHIR** | **Unknown / unlikely-documented** | No evidence KM exposes a FHIR API for Exa. Assume no. |
| **REST/developer API + webhooks** | **Unknown; assume none public** | No developer portal found. The ZFP client obviously calls a private backend API, but it is undocumented/unsupported for third parties and may change without notice. |
| **Interface engine** | Inferred | HL7 work implies KM uses/accepts an interface engine (Mirth/Rhapsody-class) on their side; you'd interface *to* it, not *into* Exa internals. |
| **Partner/SDK program** | **None found** | No public Exa developer/partner SDK. |

**Realistic path for an external app:**
- **(a) Read studies / worklist:** most viable via **DICOM Query/Retrieve or Modality Worklist**, or **DICOMweb if exposed**. Reading the *live UI worklist* is also possible via browser-DOM (see Q4). *(Inferred, Medium.)*
- **(b) Read / receive report text:** most viable via **HL7 ORU** outbound (final signed reports) arranged through KM — this is the cleanest, supported rail for downstream consumption (reconciliation, QA, analytics). *(Verified rail exists; site provisioning Unknown.)*
- **(c) Write / pre-fill report content:** **No supported programmatic write path is documented.** Realistic options are all *client-side*: a **browser extension** that inserts text into the Exa report editor, or clipboard-assist. Server-side report injection would require an undocumented private API or a KM-built custom interface (unlikely to be offered). *(Inferred, Medium-Low feasibility server-side; Medium feasibility client-side.)*

---

## Q3 — Report creation / structured reporting

**Verified (High):**
- Exa has an **integrated dictation, transcription and reports module** in a single UI. **Templates** are provided to customize reports (logos, tables, study/patient info fields). Report lifecycle includes dictation → transcription → **approvals → online publication → auto-fax**. Source: KM Exa PACS page.
- **Voice recognition is native via "Exa Voice," powered by nVoq** — a **cloud-based** speech-recognition engine fully integrated into Exa, no local install/training, "up and running in seconds." Source: KM Exa PACS page. *(This means voice/report text transits nVoq's cloud already — relevant to your PHI-boundary design.)*
- **Mobile dictation sync:** open a study on the workstation and the Exa mobile app auto-attaches the phone dictation to that study. Source: radiologyimagingsolutions.com.

**Inferred / Unknown:**
- **Third-party voice (Nuance PowerScribe / Fluency Direct):** KM's *native* voice is nVoq, not PowerScribe. Radiology groups frequently still bolt PowerScribe/Fluency onto a PACS via the vendor's "PowerScribe API / bridge" or a focus-follows-cursor overlay. Whether *his* instance uses Exa Voice (nVoq) or an external PowerScribe/Fluency is **Unknown → confirm hands-on** (it materially changes the companion-tool design: PowerScribe has its own automation surface; Exa Voice does not, publicly). *(Confidence: Medium that it's Exa Voice by default.)*
- **Programmatic pre-fill of report content:** No documented API. Template/macro pre-population *inside* Exa is a user-facing feature (templates, and likely macros/auto-text in the editor), but populating it from an external agent means **client-side insertion** (extension/clipboard) unless KM builds a custom HL7/interface. *(Inferred, Medium-Low.)*

---

## Q4 — Companion-tool feasibility (zero-footprint web app)

Because Exa is a **pure web app with server-side rendering**, the companion design space is shaped by "the browser tab is the integration point."

| Approach | How it works | Pros | Cons / Risk |
|---|---|---|---|
| **Browser extension (DOM read/write)** — *most promising for write-assist* | Extension runs in his Exa tab; reads worklist/report-editor DOM, injects generated text into the report field, surfaces an assistant sidebar. | Works with the app as-is; no KM cooperation; can both **read context** and **write/pre-fill** report text; PHI can stay in-browser/local. | **Brittle** — SSR/DOM can change on KM updates; must be maintained. ToS/security review needed. Can't see pixels (server-rendered) without the image API. Per-user deployment. |
| **Local agent + DICOM/DICOMweb** | On-prem service receives DICOM (C-STORE route or Q-R/DICOMweb pull), runs image AI locally, returns findings. | Standard, stable, vendor-agnostic; keeps images **on-prem**; good for image-based AI (detection/measurement). | Needs a DICOM/DICOMweb endpoint on his instance (confirm). Doesn't by itself write into Exa's report — pair with extension or HL7. |
| **HL7 ORU intercept (downstream)** | Receive final report feed for reconciliation/QA/analytics. | Supported rail; clean, signed data; great for the **RVU/payment reconciliation** feature. | Read-only, post-signature. Provisioned by KM per site. |
| **Clipboard / "assist" overlay** | Local app generates text; radiologist pastes; or an accessibility overlay. | Zero coupling; trivially robust. | Manual step; least "automated"; no structured capture. |

**Recommendation (feasibility):** a **hybrid** — (1) **browser extension** as the read/write bridge into the live Exa session for report pre-fill and worklist context, plus (2) an optional **local DICOM/DICOMweb agent** if image-side AI is in scope, plus (3) **HL7 ORU** (if KM enables it) feeding the **reconciliation dashboard**. Keep all PHI-bearing inference local (Q5). *(Confidence: Medium — contingent on DOM stability and which interfaces his instance actually exposes.)*

---

## Q5 — Privacy-preserving on-prem radiology-AI patterns (HIPAA-aligned)

> Search backends were degraded this session; the canonical references below are **domain-established standards I'm confident exist**, but I flag that I did **not** re-fetch each URL live this session. Confidence ratings reflect that.

**Established patterns (Confidence: High as practices; Medium on exact URLs un-re-verified this session):**
- **Keep PHI local; de-identify before any cloud LLM call.** Two clean architectures: (a) **local inference only** — run the model on-prem (e.g., a local LLM such as Llama-class via Ollama/vLLM for report text; local CV models for images) so **no PHI leaves the premises**; or (b) **de-identify → cloud** — strip PHI, send only de-identified content to a cloud LLM under a **Business Associate Agreement (BAA)**, re-identify locally. Minimum-necessary + purpose limitation throughout (HIPAA Privacy Rule).
- **DICOM de-identification standard: DICOM PS3.15 Annex E — "Attribute Confidentiality Profiles."** Defines exactly which DICOM tags carry PHI and the profiles/options to remove them. Canonical: https://dicom.nema.org/medical/dicom/current/output/html/part15.html
- **RSNA "CTP" (Clinical Trial Processor / MIRC)** — mature open-source DICOM anonymization pipeline (rule-based tag scrubbing, pixel-region blanking). Reference: https://mircwiki.rsna.org (MIRC/CTP). Widely used to de-identify before research/AI.
- **HHS de-identification guidance — Safe Harbor (18 identifiers) vs. Expert Determination.** The two lawful de-id methods under HIPAA. https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html
- **Pixel-level PHI matters, not just tags.** Burned-in annotations (common in **ultrasound**, secondary captures, screenshots) require OCR + redaction, not just header scrubbing. This is a frequent leak point — design for it.
- **On-prem / edge deployment stacks people actually use:** **Orthanc** (open-source, lightweight DICOM server with **DICOMweb** + built-in anonymization — excellent as the local ingest/de-id hub), **OHIF** (open-source web viewer), **NVIDIA MONAI / MONAI Deploy** (on-prem medical-imaging inference framework). Commercial radiology-AI vendors that deploy via an **on-prem/edge appliance receiving DICOM** (PHI stays local, results returned to PACS/worklist): **Aidoc, Gleamer, Annalise.ai, Rad AI, Nuance/Microsoft Precision Imaging Network.** *(Vendor names: Confidence High that these operate edge/on-prem models; specific contract terms out of scope.)*

**What this implies for you:** put an **Orthanc-class local hub** (or your own service) as the PHI boundary; run report-text generation on a **local LLM** so dictation/impression content never leaves; if you ever want a frontier cloud model, gate it behind **de-identification + a BAA**. Note that **Exa Voice already sends voice to nVoq's cloud** (Q3) — so the org has likely already executed a BAA covering that; worth confirming, and it sets precedent for your architecture.

---

## Q6 — Known third-party integrations with Exa (reference points)

**Verified (High):**
- **nVoq** — powers **Exa Voice** (cloud speech recognition). Source: KM Exa PACS page.
- **Imagine Software** — billing/RCM partner referenced on KM's platform. Source: KM RIS page.
- **DataFirst** — partner referenced on KM's platform. Source: KM RIS page.
- **AWS** — cloud hosting/infrastructure partner for the Exa Platform. Source: KM Exa PACS page.
- **EMR/EHR via HL7** — KM's implementation docs treat third-party EMR HL7 interfacing as a standard deliverable. Source: KM Implementation Overview PDF (Q2).

**Unknown (could not confirm this session):** specific named **AI/reporting/dashboard/voice** third parties certified against Exa (e.g., whether any imaging-AI vendor advertises an "Exa" connector). Search degradation + the `exa.ai` name collision blocked clean confirmation. **Treat "which AI vendors have a turnkey Exa integration" as an open question** — most likely answer, given no public partner program, is: integrations are **bespoke, HL7/DICOM-mediated, arranged through KM**, not a marketplace. *(Inferred, Medium.)*

---

## Q7 — Independent (1099) radiologist productivity / RVU / payment reconciliation

> Domain synthesis; specific product URLs not re-verifiable this session. Confidence noted.

**Established (High confidence as domain facts):**
- **wRVU (work RVU)** is the unit of physician work per CPT code, published in the **CMS Physician Fee Schedule RVU files** (CMS.gov, updated annually). A 1099 radiologist is typically paid **per-study, per-wRVU, or per-shift**; per-RVU and per-study are the ones that need reconciliation.
- **Reconciliation = "reads I performed" vs. "reads I was paid for."** Sources of truth: the **PACS/RIS worklist / activity log** (studies signed, with timestamps, modality, CPT/exam description) on one side, and the **payer/group remittance or 1099 pay statement** on the other. Exa's own **Performance Dashboard** already tracks **daily exam volume and per-radiologist performance** — a ready internal data source for the "work performed" side (Source: KM Exa PACS page, Q1).
- **Common revenue-leakage modes to catch:** studies read but never billed; **addenda / second reads** not counted; wrong CPT or missing modifier (e.g., professional-component -26); denied/underpaid claims; **contracted rate vs. actual paid** mismatch; studies reassigned/rerouted and dropped; time-zone/date-boundary miscounts on overnight shifts.
- **Reference tooling landscape:** there is **no dominant off-the-shelf "1099 radiologist reconciliation dashboard."** Adjacent commercial tools are **RCM/billing + radiology analytics** platforms — e.g., **Imagine Software** (KM's billing partner), **Zotec Partners**, **RamSoft**, and group-internal BI. In practice independent rads reconcile with **spreadsheets** against their group's productivity report. *(Confidence: Medium — landscape is fragmented; exact feature sets un-re-verified this session.)* **This gap is precisely the build opportunity:** a reconciliation dashboard that ingests Exa's worklist/volume data (or HL7 ORU feed) and cross-checks it against pay statements is a genuine, under-served need.

---

## What this means for our build

**Recommended integration path (in priority order):**
1. **Report pre-fill / live assist → browser extension** operating inside his Exa ZFP session. This is the only realistic **write** path given no public API and a zero-footprint web app. It also reads worklist/report context. Build it to tolerate KM UI updates (defensive selectors, feature flags).
2. **Reconciliation dashboard → HL7 ORU feed (if KM will enable it) or Exa Performance-Dashboard/worklist export.** Cleanest supported data for "work performed vs. paid." Start read-only; this is the highest-value, lowest-integration-risk feature.
3. **Image-side AI (if in scope) → local DICOM/DICOMweb agent** (Orthanc-class hub) that receives/pulls studies, infers **on-prem**, returns results. Confirm a DICOM Q-R / DICOMweb endpoint exists on his instance.
4. **PHI boundary → local-first.** Local LLM for report text; de-identify + BAA only if a cloud model is ever needed. (Org likely already has an nVoq BAA — leverage that precedent.)

**Assume NOT available (until proven):** a public Exa REST API, FHIR, webhooks, or a partner SDK. Design so the product still works without them.

**Open questions to resolve during hands-on recon (Tailscale into his environment):**
1. **Who operates `exa.swrxsyonline.com`** (reseller vs KM-on-AWS), and the Exa **version**.
2. **DICOMweb?** Does the ZFP client hit a QIDO/WADO/STOW endpoint reachable to a third party? (Watch network calls in the browser dev tools.) Is DICOM C-FIND/C-MOVE/MWL available to a new AE?
3. **HL7 feeds:** Is there an outbound **ORU** (final reports) and inbound **ORM** available, and who controls that interface (his group's IT, the reseller, or KM)?
4. **Voice engine in use:** **Exa Voice (nVoq)** vs external **PowerScribe/Fluency**? (Changes the report-automation surface materially.)
5. **Report editor DOM structure** — is the impression/findings field a plain contenteditable/textarea (easy to inject) or a complex widget?
6. **Worklist/report export** — any CSV/report export or DB read access for the reconciliation feature?
7. **Payment-data source** — where do his pay statements come from (group remittance format), so the dashboard can join "reads" ↔ "payments"?
8. **BAA/compliance posture** — existing agreements (nVoq/AWS) and whether the operator permits a browser extension + local agent on the reading workstation.

---

### Source list
- Konica Minolta — Exa PACS: https://healthcare.konicaminolta.us/healthcare-it/exa-pacs *(High)*
- Konica Minolta — Exa PACS|RIS / Platform: https://healthcare.konicaminolta.us/exa-pacsris *(High)*
- Konica Minolta — Exa Platform Implementation Overview (PDF, HL7 3rd-party interface): https://healthcare.konicaminolta.us/sites/default/files/2023-03/Exa%20Platform%20Implementation%20Overview%20V3.pdf *(High for HL7 existence; PDF body not machine-parseable via this fetch, relied on indexed snippet)*
- Radiology Imaging Solutions — Exa PACS (reseller detail incl. mobile dictation, SSR): https://radiologyimagingsolutions.com/konica-minolta-exa-pacs/ *(Medium-High, reseller mirror of KM copy)*
- ToolsInfo — Exa PACS overview (integrations RIS/EMR/HIS, HIPAA/SSO): https://healthcare.toolsinfo.com/tool/konica-minolta-exa-pacs *(Medium, third-party directory)*
- DICOM PS3.15 Annex E (de-identification): https://dicom.nema.org/medical/dicom/current/output/html/part15.html *(High as standard; not re-fetched this session)*
- RSNA MIRC/CTP anonymizer: https://mircwiki.rsna.org *(High as tool; not re-fetched this session)*
- HHS HIPAA de-identification guidance: https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html *(High; not re-fetched this session)*

**Search-tooling caveat:** DuckDuckGo returned bot/CAPTCHA challenges and Bing returned name-collision/irrelevant results (the AI-search company "Exa"/exa.ai) throughout this session, limiting confirmation of Q5/Q6/Q7 specifics. Findings above are conservatively rated; the integration-critical items are flagged for hands-on verification, which is the correct place to resolve them regardless.
