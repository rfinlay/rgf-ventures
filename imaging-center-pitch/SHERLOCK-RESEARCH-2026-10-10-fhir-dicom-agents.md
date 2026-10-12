# Sherlock Research Brief: Payer FHIR, DICOM Operational Data, and Agentic Admin Automation

**Prepared:** 2026-10-10, for the dinner with Dr. Luis Ramos and Fernando Escarzaga (~2026-10-20)
**Scope:** the three areas the 2026-10-01 research under-covered. Prior-authorization economics are NOT re-researched; this brief builds on `AUTOMATION-CANDIDATES.md` and corrects it where the evidence demands.
**Method:** primary sources preferred and read directly wherever reachable. The CMS-0057-F final rule (89 FR 8758, 234,472 words), the 2026 NPRM (91 FR 19890), Texas HB 3459, Texas HB 3812, Texas HB 149 (TRAIGA), the ACR Practice Parameter, and the Joint Commission 2026 goal sets were all downloaded and searched or text-extracted locally rather than read through secondary summaries.

**Confidence scale:** High = primary source read directly, or multiple independent sources agree. Medium = single credible secondary source, or primary source seen only through an intermediary. Low = vendor self-report, single trade mention, or inference.
**Labels used throughout:** **VENDOR CLAIM** = marketing or vendor-published, evidence of a claim only. **MEASURED** = independently or peer-reviewed measured. **PROJECTED** = forward-looking. **UNVERIFIED** = could not confirm.

> **A standing caution that applies to this entire brief.** There is **no independently audited or peer-reviewed outcome study for agentic administrative automation** anywhere in this space as of October 2026. Every vendor percentage in §Q3 is vendor-published, with the measurement, the baseline, and the choice of reported cohort all controlled by the seller. Any ROI model built on those numbers is built on marketing. The defensible move — which is also what the ACR's new AI practice parameter calls for — is to cite them as vendor-claimed and propose a measured pilot with a pre-registered baseline.

---

## 1. Bottom line

1. **Rick's recollection of the CMS-0057-F dates is correct and now verifiable from the rule text.** Decision timeframes + denial reasons + public metrics bind in **2026**; the four APIs bind in **2027**. But the dates are *staggered by payer type*, not flat calendar dates. (Primary source, 89 FR 8758. **High**)
2. **The Da Vinci CRD/DTR/PAS stack is RECOMMENDED, NOT REQUIRED, by the rule in force.** The *required* standards are only the base layer (FHIR R4.0.1, US Core, SMART App Launch) at 45 CFR 170.215. A payer can be fully compliant on 2027-01-01 with a FHIR PA API that is not PAS-conformant — CMS concedes this in the 2026 NPRM. **Design for per-payer variation; this raises the effort estimate for candidate #1.** (Primary source. **High**)
3. **A 2026 proposed rule exists that prior work does not account for: CMS-0062-P (91 FR 19890, 2026-04-14, still NOT final).** It would make CRD/DTR/PAS mandatory, extend PA to drugs by 2027-10-01, and add QHP issuers to the decision-timeframe rule. It does **not** move the 2027 non-drug dates. (Primary source. **High**)
4. **For advanced imaging, the payer is often not the decision-maker — a radiology benefit manager is.** Whether the imaging decision is reachable through the payer's FHIR PA API is **UNVERIFIED and is the most important open technical question in the build.** (**Medium-High** on RBM dominance; **UNVERIFIED** on FHIR reachability)
5. **The FHIR mandate levels the interface, not the integration cost — and not at all for a greenfield center on day one.** The Prior Authorization API is open to "a provider" with no in-network condition; the Provider Access API requires a contractual relationship the center won't yet have. **Do not pitch FHIR as the moat. Pitch appeal follow-through as the moat.** (**High** on the asymmetry; **Medium** on the conclusion)
6. **Payer-specific prior-auth approval, denial, appeal-overturn and turnaround data is ALREADY PUBLIC** on each impacted payer's website since 2026-03-31, refreshed every March 31, including each payer's **list of all items and services requiring prior authorization**. Free, named-payer, pitch-ready, and nobody has pulled it for El Paso. Caveat: "aggregated for all items and services," so not imaging-specific. (Primary source. **High**)
7. **Scanner utilization and exam-duration analytics from DICOM timestamps is peer-reviewed and deployed, not speculative** — and in the one published head-to-head it beat the institution's clinical data warehouse. This upgrades candidate #4 from "Evidence: Low" to **High**. Two caveats: validate scanner clocks first, and build on Tier-1 machine-written tags only. (Peer-reviewed, Emory, 715 scanners. **High**)
8. **Three things an owner would expect from a DICOM feed are NOT reliably available:** repeat/reject rate (vendor-proprietary, non-comparable — AAPM TG305 exists because of this), per-technologist attribution (Operators' Name is optional and often blank or a shared login), and protocol/body-part normalization (a 2025 study collapsed 116 header values into 36 codes). **Do not promise these without a site audit.** (Peer-reviewed. **High**)
9. **🔴 THE REFERRER-VOLUME PREMISE FAILS. There is no published evidence that turnaround time or referrer communication causes measurable referral-volume gain.** Four targeted PubMed queries returned zero. Worse, the methodologically strongest study in the field (JACR 2025 conjoint, n=393 patients + 168 physicians) finds **cost/copay dominates** site selection and does not even test TAT. **A whole pitch section must be rewritten to the satisfaction/retention level.** Fernando founded and sold an imaging company; he will likely know this. (**High** on the negative finding)
10. **🔴 The Joint Commission requirement usually cited does not apply to an outpatient imaging center.** The 2026 Ambulatory Health Care goal set contains **no critical-results goal at all**; NPSG.02.03.01 is the *Laboratory* identifier; hospitals moved to NPG.01.02.01. The real compliance hook is the **ACR Practice Parameter (Revised 2025)**. (Official PDFs read directly. **High**)
11. **The ACR parameter (Revised 2025) does contain the single best buildable requirement in the brief:** electronic non-routine communication is permitted "as long as they provide documentation of receipt to demonstrate that the communication has been delivered and acknowledged." Conversely it sets **no numeric TAT standard** and assigns the referrer a **reciprocal duty** — which both limits liability scoping and undercuts any "ACR requires fast TAT" claim. (Primary source. **High**)
12. **Texas gold-carding is a real, strengthened, imaging-relevant lever that belongs to the ORDERING PHYSICIAN, not the facility** — and HB 3812 (effective 2025-09-01) made it materially better: evaluation period six months → **one year**, a new **five-service minimum**, **affiliate aggregation across all the payer's plans**, and rescission narrowed to January only. The center can never earn one, but it holds the per-referrer data to help referrers earn one. **This is the most differentiated referrer-acquisition idea in the brief.** (Enrolled statutes read directly. **High**)
13. **Payers are being sold AI to deny routine imaging claims POST-SERVICE and PRE-PAYMENT** — X-ray, ultrasound, non-cardiac nuclear medicine, explicitly avoiding prior authorization. The scan is delivered and the cost sunk before review. **This reframes the pitch from efficiency to parity against an automated counterparty.** (Vendor primary page verified; see the important correction in §2.10. **Medium-High**)
14. **Texas is the densest AI-compliance state in the country for this build, and TRAIGA binds the PROVIDER, not the payer.** Patient disclosure is required no later than the date service is first provided when AI is used in relation to a health care service. (Enrolled bill read directly. **High** on the text; see §2.11 for a genuine construction ambiguity)
15. **Imaging-specific administrative labor benchmarks essentially do not exist publicly.** The one radiology FTE figure found is from **11 practices**. CAQH has no radiology breakout. HFMA MAP Keys has no imaging keys. The credible radiology A/R figure (~31 days median) is behind an RBMA paywall. **Do not approximate these; ask Fernando.** (**High** on the gap)

---

## 2. CORRECTIONS to prior work

**This is the section to revise the existing documents against.** Items 2.9–2.12 are the ones that change what Rick *says at the table*.

### 2.1 CORRECTION — compliance dates are staggered by payer type

`AUTOMATION-CANDIDATES.md` line 49 says the timeframes "bind impacted payers from 2026-01-01"; GIO-STRATEGIC-ANSWERS line 184 says "decision timeframes and public reporting from 2026-01-01, the APIs by 2027-01-01." Right for two payer types, wrong for the other two. The rule's actual construction, verbatim:

> "by January 1, 2026, for MA organizations and state Medicaid and CHIP FFS programs; by the rating period beginning on or after January 1, 2026, for Medicaid managed care plans and CHIP managed care entities; and for plan years beginning on or after January 1, 2026, for QHP issuers on the FFEs"

The same three-part construction governs the 2027 API dates. CMS then says: "Throughout this rule, we generally refer to these compliance dates as ``in 2027'' for the various payers."

**Why it matters:** a Medicaid managed-care plan whose rating period starts 2027-07-01 is not obligated until then — and that is exactly the payer class that dominates El Paso's Medicaid-heavy market. Say **"in 2027, phasing in by payer across the year."** (**High**)

### 2.2 CORRECTION — Da Vinci CRD/DTR/PAS are NOT required

Neither prior document states this, and the omission reads as an assumption that the Da Vinci stack *is* the mandate.

- Required standards at 45 CFR 170.215: **FHIR R4.0.1** (a)(1); **US Core IG STU 3.1.1** (b)(1)(i); **SMART App Launch IG 1.0.0** (c)(1); plus OpenID Connect. (89 FR 8758. **High**)
- On Da Vinci the rule says: "We are also **strongly recommending** that payers use specific IGs to supplement the required standards at 45 CFR 170.215." (**High**)
- CMS confirms the consequence in the 2026 NPRM: "we are proposing to require certain ... implementation guides (IGs) that are **currently recommended**," and "**Some impacted payers may have opted not to use the currently recommended IGs**, which we now propose to require." (91 FR 19890. **High**)

**Design consequence:** the prior-auth agent cannot be written against PAS alone. It needs a per-payer adapter layer. This **increases** the effort for candidate #1 and should be said plainly rather than discovered in month three.

### 2.3 NEW — a 2026 proposed rule prior work does not mention

**CMS-0062-P, 91 FR 19890, published 2026-04-14, comments closed 2026-06-15. Still a PROPOSED rule as of 2026-10-10 — must not be presented as binding.** (**High**)

If finalized it would: make **CRD 2.0.1, DTR 2.0.1, PAS 2.0.1** mandatory (note: PAS **2.0.1**, while the published guide is **STU 2.1.0** of 2024-12-20 — a version-pinning trap); extend PA to **drugs** at **2027-10-01**; **add QHP issuers on the FFEs to the shortened decision timeframes**; let **all** state Medicaid/CHIP FFS programs request compliance-date extensions (so Texas Medicaid FFS could be later than 2027); and set **2028-01-01** expirations for current standard versions plus FF-SHOP Patient Access API.

**Pitch consequence:** this strengthens the case for designing against FHIR, while confirming the IG versions are still moving — which is an argument for the adapter layer and for Rick's "tool-first, agent-second" standard.

### 2.4 REFINEMENT — the decision timeframes: four qualifications

1. They apply to covered items and services **excluding drugs**.
2. "**7 calendar days** for standard requests **with the possibility of an extension to up to 14 days** in certain circumstances." An agent treating 7 days as hard will raise false alarms; model the extension (payers must publicly report how often they use it).
3. Expedited is 72 hours "**unless a shorter minimum timeframe is established under applicable state law**." The Texas figure is **UNVERIFIED**.
4. **QHP issuers on the FFEs were EXCLUDED from the shortened timeframes** in the 2024 rule (they are in scope for the APIs). Also excluded entirely: **stand-alone dental plan** issuers and **FF-SHOP**-only issuers. (**High**)

### 2.5 NEW — Texas gold-carding, verified against the enrolled statutes

Neither prior document mentions it. Both statutes were read directly, which upgrades this to **High** and corrects the secondary sources.

**Texas Insurance Code ch. 4201, Subchapter N, created by HB 3459 (effective 2021-09-01), amended by HB 3812 (effective 2025-09-01).**

Mechanism (§4201.653, as amended): a health maintenance organization or insurer "may not require a physician or provider to obtain preauthorization for a particular health care service if, in the most recent **one-year** evaluation period ... the health maintenance organization or insurer, **including any affiliate**, has approved or would have approved **not less than 90 percent** of the preauthorization requests submitted by the physician or provider for the particular health care service; **and** the physician or provider has provided the particular health care service **at least five times** during the evaluation period."

**What HB 3812 changed — all in the provider's favour:**
- Evaluation period **six months → one year**
- **New minimum: five services** provided during the period
- **New §4201.653(a-1): affiliate aggregation** — the payer must count *all* preauthorization requests across all its policies and plans, "regardless of whether the preauthorization request was made in connection with a health insurance policy or health benefit plan that is subject to this subchapter"
- Rescission window narrowed from "January **or June**" to **January only**, and no earlier than the first anniversary of the last evaluation period
- Utilization review must be directed by a Texas-licensed physician who may **not** hold an administrative-medicine license

**Four details that matter and that secondary sources get wrong:**
- **The exemption is automatic.** §4201.653(d): "A physician or provider **is not required to request an exemption** ... to qualify for the exemption."
- **Scope (§4201.652):** HMO plans under ch. 843 and **preferred provider / exclusive provider** plans under ch. 1301, plus any person contracting to issue preauthorization determinations.
- **🔴 Texas Medicaid is EXPRESSLY EXCLUDED**, "including the Medicaid managed care program," as are CHIP and the ch. 63 children's plan. Secondary sources claiming Medicaid managed care is covered are **wrong**.
- **Medicare Advantage is outside it** — the word "Medicare" appears **zero times** in HB 3459; MA is federally governed.
- Rescission requires a retrospective review of a random sample of **not fewer than five and no more than 20 claims**, 25 days' notice, and is appealable to an independent review organization that must decide within 30 days; the payer is bound by a non-affirming IRO determination and may not rescind retroactively.

**Why this is a genuinely new pitch angle.** The center cannot earn a gold card — the exemption attaches to the physician or provider submitting the requests, and for imaging that is the referrer. But the center sits on the data: every order, every authorization, every outcome, per referrer, per CPT. An agent that tells a referring physician *"you are at 94% approval on lumbar MRI across 31 requests this year with this carrier and its affiliates; you qualify automatically"* hands that referrer a **permanent reduction in their own administrative burden**, on a one-year clock, with affiliate aggregation working for them. That is a referrer-acquisition instrument no RIS ships and no consolidator offers, built from data the center already has — and it converts candidate #12 from "Buy, no evidence found" into something defensible.

**It is also the one referrer-channel idea that survives the collapse of the TAT premise in §2.9**, because its value to the referrer is administrative relief, not a service-quality feeling.

### 2.6 NEW — payer prior-auth performance data is already public, by named payer

Under the rule, every impacted payer must post on its **own public website**, annually, beginning **2026-03-31** (CY2025 data), verbatim:

> "(1) A list of all items and services that require prior authorization. (2) The percentage of standard prior authorization requests that were approved... (3) ...denied... (4) ...approved after appeal... (5) The percentage of prior authorization requests for which the timeframe for review was extended, and the request was approved... (6) The percentage of expedited prior authorization requests that were approved... (7) ...denied... (8) The average and median time that elapsed between the submission of a request and a determination..."

**Two consequences.** The **"list of all items and services that require prior authorization"** is a published, per-payer input to the "is auth required?" determination — the front half of candidates #1 and #2 — available **now, without any API**. And approval/denial/appeal-overturn/TAT by **named payer** is pullable for whichever plans dominate El Paso, turning the KFF national aggregate into payer-specific evidence.

**Hard caveat that must travel with it:** the metrics are "**aggregated for all items and services**" — not imaging-specific, exactly like the KFF figures already in the deck. (**High**)

### 2.7 REFINEMENT — a fresher citation for the AMA figures

`AUTOMATION-CANDIDATES.md` line 41 cites "AMA 2025." The same figures appear in an **AMA press release dated 2026-05-13** (n=1,000 practicing physicians, fielded 2025), which adds material the deck lacks:

- **Only 33%** believe the insurers' voluntary pledge will make a meaningful difference
- **95%** say PA delays necessary care; **79%** report patients abandoning treatment; **92%** say it negatively affects outcomes; **26%** report a serious adverse event
- **32%** report requests often/always denied; **74%** report denials increased over five years
- **Just 24%** report medical-necessity denials are consistently reviewed by appropriately qualified clinicians; only **16%** say peer-to-peer reviewers often/always have appropriate qualifications
- Reports **no decrease** in burden

**Why the refresh matters:** it is 2026 rather than 2025 evidence, and the 24%/16% figures are the strongest published support for the *appeal* thesis specifically — they say denials are frequently not competently reviewed, which is why four in five appeals win. (**High** as survey data)

### 2.8 NEW — the payer-pledge counter-narrative, and why it does not undercut the pitch

Fernando may have read that insurers are fixing this themselves. Pre-empt it.

- June/July 2025: AHIP and BCBSA announced voluntary commitments covering plans for ~257 million Americans, including standardizing electronic PA on **FHIR APIs** and real-time decisions on **80% of electronic PA requests with complete documentation**, targeted at **2027**. (**Medium-High**)
- One year in, AHIP/BCBSA reported an **11% reduction** in services requiring PA (~6.5 million fewer requests), **>15% in Medicare Advantage**. (**Medium** — trade-association self-report about its own members, no independent audit; Becker's coverage returned HTTP 403.)
- Against it: the AMA's 2026 survey finds only 33% of physicians expect it to matter and reports no measured decrease.

**Honest framing, which is also stronger:** the pledge is *good news for the design* and *no news for the economics*. It extends FHIR PA toward commercial plans the federal rule does not reach — partially closing the gap at `AUTOMATION-CANDIDATES.md` line 58 — but it is voluntary, self-reported, unaudited, and coexists with **PA expansion** for advanced imaging (see §2.10). Volume reduction also does not touch the appeal gap, which is where the abandoned revenue is.

### 2.9 🔴 CORRECTION, THE BIGGEST ONE — the referrer-volume premise is not supported

**This invalidates a pitch claim as written, and it must be fixed before the dinner.**

The question was whether report turnaround time or referrer communication quality **drives referral volume**. The answer separates cleanly:

**(a) Referrers SAY reporting matters — well supported.** UCSF surveyed 2,720 clinicians across 11 domains of the radiology process map, 729 responded (27%). Multivariate logistic regression on overall satisfaction: **results/reporting overall OR 4.71 (95% CI 2.15–10.23)**, the strongest of all 11 domains; attending radiologist interactions OR 3.71; **timeliness of inpatient results OR 2.91 (CI 1.01–8.09)**; urgent outpatient appointment availability OR 2.01. Conclusion: referrers "value most the accuracy of the radiology report and their interactions with attending radiologists." (*Clin Imaging* 2023;97:72-77, PMID 36907042. **High**) **Three limits:** the outcome is **satisfaction, not volume**; it is a single academic department, not a freestanding center; and **timeliness ranked below accuracy and relationships**, with the only significant timeliness variable being *inpatient*.

**(b) It changes referral VOLUME — NO EVIDENCE FOUND.** Targeted PubMed queries returned: `radiology turnaround time referral retention` → **0**; `radiology report turnaround time market share` → **0**; `referring physician satisfaction radiology referral volume` → 3, all irrelevant; `referring physician loyalty imaging center` → 3, all irrelevant. Independent replication in my own search found the same: `radiology report turnaround time referring physician loyalty referral` → **0**, and `referring provider satisfaction radiology drivers loyalty` → **0**. Web searching for volume change after a TAT improvement returned nothing. (**High** on the negative finding)

**🔴 The study that actively undercuts the premise.** Yuan C, Huang H, Dirschl D, Chintagunta P, Paushter D. "Characterization and Targeting of the Main Drivers of Elective Imaging Utilization: A Cross-Sectional Study Applying Conjoint Analysis." *JACR* 2025 May;22(5):521-529, PMID 39828000. **393 patients + 168 physicians**, conjoint choice screens with latent-class segmentation — this measures *revealed trade-off weights*, not stated preference, so it is much harder to dismiss than a satisfaction survey. Findings: "**Both patients and referring physicians placed most value on copay and cost**, with both groups containing a large segment that places almost all value on low costs." Physicians also valued **image quality and a trusted radiologist** (one segment weighting these above cost). **TAT and communication responsiveness were not among the dominant attributes — TAT was not even a tested attribute.** (**High**)

Corroborating: an analysis of **50,484 lower-limb MRI scans** found "the key determinant of where a patient received MRI was referring physician recommendation," with patients bypassing on average six lower-priced facilities. (**Medium-High**) And Advisory Board's top five reasons referrals go out of network — patient preference 23.0%, provider directed 22.7%, no in-network specialist 15.4%, availability 12.5%, continuity 11.7% — contain **neither TAT nor report communication**. (**Medium-High**, proprietary 2019 dataset)

**What IS strongly evidenced — a different and usable argument.** TAT is deteriorating nationally: **+113% 2014–2023** (CT +318%, MR +256%, US +140%, XR +63%) across 2.6M outpatient studies (*JACR* 2026;23(7):1244-1252, PMID 41914942); updated to **+27% in one year and +177% over 2014–2024** across 2.9M studies (*JACR* 2026 Aug 4, PMID 42550124; Neiman HPI 2026-08-04). Longer TAT was found in more disadvantaged communities. TAT is also manipulable — pay-for-performance moved completion-to-finalization 42.7 → 31.6 → 16.3 hours. (**High** on the trend; **Medium** on the P4P study — and note it measures TAT, not resulting volume.)

**DEFENSIBLE language:**
> "Referring clinicians rate results and reporting as the single strongest driver of their overall satisfaction with a radiology service (OR 4.71, UCSF, n=729, *Clin Imaging* 2023), and national interpretation turnaround time has worsened 177% since 2014 (*JACR* 2026, 2.9M Medicare studies). Referrers control site-of-service routing. **Satisfaction and routing control are documented; a causal link from turnaround time to referral volume is not published, and we treat volume gain as a hypothesis to be measured, not an established benchmark.**"

**NOT defensible — do not write or say:** "faster turnaround drives referral volume" · "better referrer communication increases referrals by X%" · "imaging centers lose N% of referrals to slow reporting" · "56% of referrals are faxed."

**And confront the cost finding head-on.** The strongest study says **cost/copay dominates**. A pitch built on communication quality while ignoring price positioning is vulnerable to one question from a man who founded and sold an imaging company. Concede it: communication and operational excellence is a **retention and efficiency** play and a **tie-breaker among price-comparable sites** — physicians valuing image quality and a trusted radiologist is a real measured segment — **not a volume-acquisition engine.**

### 2.10 🔴 NEW — payers are being sold AI to deny routine imaging post-service, and the brief's framing needs one correction

This is strategically the most important new fact, and it needs to be stated precisely because the trade-press framing overstates it.

**What is verified (primary vendor page, avalonhcs.com, retrieved 2026-10-10. High on the offering's existence and design):** Avalon Health Solutions markets a **Routine Radiology Benefit Management** product to health plans that applies "evidence-based clinical policies to routine imaging claims in the outpatient setting prior to payment," operating **post-service and pre-payment**, **without requiring prior authorization**, so it does not delay care. Scope: **X-ray, ultrasound, non-cardiac nuclear medicine, outpatient only**. Explicitly **excluded**: CT, MRI, PET, cardiac nuclear medicine, and inpatient/ED/observation. Claims "$1 per member per month savings potential" and targets "approximately 30% of imaging considered low-value or unnecessary" — both **VENDOR CLAIM**. **No named health-plan customers on the page.**

**The correction:** trade coverage framed this as a deployed "new payer tactic." The verifiable reality is that it is **a benefit-manager's offering being marketed to payers**, with consultants recommending the model — not a documented deployed practice with named plans. The Radiology Business article describing it returned **HTTP 403** on direct fetch (Cloudflare), twice, so its characterization — including that denials are coded as **provider liability** — rests on search extracts and is **UNVERIFIED against the original**. The Avalon page itself **does not state who bears the cost of a denied claim.**

**Why it still matters enormously, and arguably more than the overstated version:** the *design intent* is confirmed from the vendor's own page. For the routine modalities that make up a community imaging center's bread-and-butter volume, a payer can review and decline **after the scan is delivered and the cost is sunk**, with **no prior authorization step at which the center could have protected itself**. That is a categorically different risk from the pre-service auth problem the deck is built around, and the center's only defences are documentation quality at the time of service and the capacity to contest post-payment determinations — which is an *appeals* capability.

**Alongside it, PA for advanced imaging is still expanding:** effective **2026-10-01**, **Surest (a UnitedHealthcare company) requires prior authorization for certain outpatient radiology** — CT, MRI/MRA, nuclear cardiology, PET. (uhcprovider.com, primary payer source. **High**) So the voluntary-pledge "relief" narrative and a concrete PA expansion coexist in the same year. **Do not present the pledge as relief.**

**Pitch consequence:** this reframes the engagement from *efficiency* to **parity against an automated counterparty**, which is a stronger and more durable argument. It also means the appeal engine — already the lead product — has a second and growing job: post-service, pre-payment determinations on routine studies, not just pre-service denials on advanced ones.

### 2.11 🔴 NEW — Texas is the densest AI-compliance state for this build, and TRAIGA binds the PROVIDER

`AUTOMATION-CANDIDATES.md` line 210 flags TRAIGA as "scope not fully verified." I read the enrolled bill. It is **more** relevant than the deck assumes, with one genuine ambiguity.

**Texas HB 149 (TRAIGA), effective 2026-01-01, creating Business & Commerce Code ch. 552.** §552.051 "DISCLOSURE TO CONSUMERS," verbatim:

- §552.051(a) defines "**health care services**" as "services related to human health or to the diagnosis, prevention, or treatment of a human disease or impairment provided by an individual licensed, registered, or certified under applicable state or federal law to provide those services."
- §552.051(f): "**If an artificial intelligence system is used in relation to health care service or treatment, the provider of the service or treatment shall provide the disclosure under Subsection (b) to the recipient of the service or treatment or the recipient's personal representative not later than the date the service or treatment is first provided**, except in the case of emergency, in which case the provider shall provide the required disclosure as soon as reasonably possible."
- Disclosure quality (§552.051(d)): must be "**clear and conspicuous**," "written in **plain language**," and "**may not use a dark pattern**." It may be provided via hyperlink to a separate web page (§552.051(e)).
- §552.052 prohibits deploying AI intended to incite self-harm or harm to others. §552.003 **preempts local AI regulation**. §552.002(2) reserves insurance regulation to the Department of Insurance.

**🔴 The genuine ambiguity, which should be flagged not smoothed over:** §552.051(**b**) — the subsection that actually creates the disclosure duty — is written as applying to "**a governmental agency** that makes available an artificial intelligence system intended to interact with consumers." Subsection (f) then directs a health-care provider to "provide the disclosure **under Subsection (b)**." Read literally, (f) cross-references a duty that (b) imposes only on governmental agencies. Whether (f) independently imposes the duty on private providers is a **statutory-construction question I cannot resolve from the text**, and the law-firm commentary that reads it as binding private providers does not address the cross-reference. **Recommendation: comply as though it binds — the disclosure is cheap and the downside is asymmetric — but do not state the obligation as settled law at the dinner, and get a Texas health-lawyer read before it goes in a specification.** (**High** on the statutory text; **Medium** on the obligation's application to a private imaging center)

**Correction to the subagent research that informed this:** "first date of service" does **not** appear in the enrolled bill; the operative phrase is "not later than the date the service or treatment is first provided." Same effect, but quote the statute.

**The rest of the Texas stack, for completeness:** **SB 815** (effective 2025-09-01) prohibits utilization review agents from using an automated decision system to make an adverse determination — payer-side, and helpful to the center. **SB 1188** (2026-01-01) requires US physical storage of Texas patient EHR data and is reported to require review of AI-created records (**scope UNVERIFIED**, consistent with prior work). Plus gold-carding above. **Texas is also one of the six WISeR states** — see §Q3b.

**Design consequence:** any patient-facing agent (scheduling, reminders, voice) needs a disclosure path at or before first service, in **plain language, no dark patterns, and in Spanish** given the 26.5% ACS figure already in the deck. Tier A (owner-facing, read-only) is unaffected. This is a specification item, not a dinner topic.

### 2.12 CORRECTION — do not cite the Joint Commission for critical results

A natural instinct is to cite TJC as the compliance driver for a critical-results product. **That would be wrong for an outpatient imaging center**, verified by reading the official 2026 program PDFs:

- **Ambulatory Health Care (the program covering outpatient radiology and diagnostic settings): the complete 2026 goal set contains NO critical-results goal.** It is only NPSG.01.01.01 (patient ID), 03.04.01/03.05.01/03.06.01 (medication safety), 07.01.01 (hand hygiene), 16.01.01 (health outcomes), and UP.01.01.01/01.02.01/01.03.01 (Universal Protocol). **There is no Goal 2.** (**High**)
- **Hospitals:** effective 2026-01-01 NPSGs were reorganized into "**National Performance Goals**"; the critical-results requirement is now **NPG.01.02.01** — "The hospital reports critical results of tests and diagnostic procedures on a timely basis," with EP 1 requiring written procedures defining critical results, by whom and to whom reported, and acceptable reporting time (documentation required), and EP 2 requiring timeliness evaluation. (**High**)
- **NPSG.02.03.01 still exists verbatim — for the Laboratory program.** So the identifier is not fictional, it is the wrong program. (**High**)

**The real drivers for an outpatient imaging center** are the **ACR Practice Parameter**, state law, payer and accreditation contracts, and malpractice exposure. (See §Q3c.)

### 2.13 CORRECTION — two technical errors to fix before the deck is built

1. **CTDIvol is (0018,9345), not (0018,1152).** (0018,1152) is **Exposure** (mAs, radiography/fluoroscopy). Verified programmatically against the DICOM PS3.6 Chapter 6 data dictionary. My own earlier draft of this brief conflated these; using the wrong tag in front of a 40-year RDMS/RPA would be costly. (**High**)
2. **IHE Mammography Acquisition Workflow (MAWF) was RETIRED 2024-06-25.** Do not name it in a 2026 contract — it signals requirements copied from a stale template. For dose, name **REM (Radiation Exposure Monitoring**, Final Text), which prior work omitted. (**High**)

Also: **DICOM PS3.20 is "Imaging Reports using HL7 CDA," not the FHIR mapping.** The authoritative DICOM↔FHIR mapping lives in the **FHIR ImagingStudy resource**, which is **Maturity 3 / Trial Use — not normative.** Don't let a vendor claim "FHIR-normative imaging" as settled. (**High**)

### 2.14 REFINEMENT — "no vendor fits a single site" needs a payer-funded carve-out

GIO-STRATEGIC-ANSWERS already converted this from a site-count to an economics claim. One more refinement: a large part of the prior-auth vendor category is **payer-funded**, so the center may meet it as the *payer's* tool rather than a purchase. **Cohere Health** (Humana-funded, expanded to diagnostic imaging), **Anterior**, **Availity** (free provider tier, payer transaction economics), and **Rhyme** (migrating to payer-footed) are all in this class.

**The sharp point to make:** free or low-cost to the provider **does not mean aligned with the provider.** Cohere's claimed "90% PA automation" and Anterior's UM acceleration both include automating **adverse** determinations. A single-site center should treat these as **counterparty infrastructure** and should not assume a payer-supplied auth tool will advocate for its claim. **Where a plan in the payer mix runs one, the center's agent should route into it rather than compete with it** — the build case rests on the long tail of plans and on the appeal gap, not on every plan being manual. (**High** on the structure; **Low-Medium** on vendor performance figures, which are partner self-report.)

### 2.15 REFINEMENT — drop the "data hostage" dollar figure

`AUTOMATION-CANDIDATES.md` #3 is correct that vendor access terms are the precondition for everything. But there is **no documented evidence** of imaging centers charged for API access or data egress: **no litigation found** (the PACS lawsuits in the record are **data-breach** cases — e.g. the Northeast Radiology class action, **dismissed** — and must not be miscited), and **no published per-study or per-GB PACS API fee schedule exists**. The best hard migration figures are **2007 and hospital-scale** ($400k+, "about 2 years and several hundred thousand dollars"), inapplicable to a single El Paso site.

**Recommendation: drop any data-hostage dollar figure and reframe as the contractual-unknown argument.** It is better sourced, and it avoids a hostage-negotiation narrative sitting badly next to Fernando's active Akumin litigation. The defensible line:

> "We cannot show you a published price list for data egress, because vendors do not publish one. That is precisely the problem: the cost is unknown at signing and discovered at exit. So we fix it at signing."

The one defensible cost range is **$15,000–$80,000/year for interface engines** (Mirth/Cloverleaf/Rhapsody, by message volume and deployment) — which is a different thing from API access. (**Medium** on the range; **High** on the absence of API-fee evidence.)

---

## 3. Findings by research question

### Q1 — Payer-side FHIR: regulatory timeline and real-world readiness

#### Q1a. Exact compliance dates — CONFIRMED

**Rule identity:** CMS-0057-F, **89 FR 8758**, published **2024-02-08**, **effective 2024-04-08**, FR doc 2024-00895, amending 42 CFR parts 422, 431, 435, 438, 440, 457 and 45 CFR part 156. (**High**)

| Requirement | Compliance | Construction |
|---|---|---|
| PA decision timeframes (72h expedited / 7 cal. days standard, extendable to 14; **excludes drugs**) | **2026** | Jan 1 2026 MA + Medicaid/CHIP FFS; rating period on/after Jan 1 2026 managed care. **QHPs on FFEs EXCLUDED** |
| Specific denial reason to the provider | **2026** | Same three-part construction |
| Public reporting of PA metrics on payer website | **first report 2026-03-31** (CY2025), annually | Same |
| Annual PA metrics reported to CMS | **2026-03-31** (CY2025), annually by Mar 31 | Same |
| Patient Access API usage metrics to CMS | **2026** | Same |
| **Prior Authorization API** | **2027** | Jan 1 2027 MA + Medicaid/CHIP FFS; rating period on/after Jan 1 2027 managed care; plan years on/after Jan 1 2027 QHPs on FFEs |
| **Provider Access API** | **2027** | Same |
| **Payer-to-Payer API** | **2027** | Same |
| **Patient Access API** — add PA information | **2027** | Same |

**IMPACTED:** MA organizations; state Medicaid FFS; state CHIP FFS; Medicaid managed care plans; CHIP managed care entities; QHP issuers on the Federally-Facilitated Exchanges.

**NOT impacted — the commercially important half:** commercial/fully-insured plans off the FFEs; **self-funded ERISA employer plans** (likely a large share of a greenfield center's commercial book); traditional Medicare FFS; **SADP-only** QHP issuers; **FF-SHOP-only** QHP issuers; State-based Exchange QHP issuers as distinct from *Federally-Facilitated* Exchange issuers (**Texas uses the FFE, so Texas QHPs are in scope** — inferred from the rule's definition, not from a CMS determination; **Medium**).

**Delegated entities:** payers are responsible for delegated and downstream entity compliance; for QHP issuers this is explicit at 45 CFR 156.340, with the terms defined at 45 CFR 156.20. This is the hook that nominally pulls RBMs in. (**High**)

**Patient Access API timing detail:** PA information must appear "no later than 1 business day after the payer receives the prior authorization request or there is another status change." (**High**)

#### Q1b. The implementation-guide stack

**REQUIRED** (45 CFR 170.215, as reorganized by HTI-1, 89 FR 1192): FHIR **R4.0.1** (a)(1); **US Core IG STU 3.1.1** (b)(1)(i), noted as expiring 2026-01-01; **SMART App Launch IG 1.0.0** (c)(1), same expiry; **OpenID Connect Core 1.0**. CMS finalized "more specificity as to which of the required standards ... are applicable to each API," and payers "will only be required to use the specifications that CMS has identified as necessary" per API. Payers may voluntarily adopt newer versions early. (**High**)

**RECOMMENDED, NOT REQUIRED:** Da Vinci **CRD**, **DTR**, **PAS**; plus CARIN IG for Blue Button STU 2.0.0, Da Vinci PDex STU 2.0.0, PDex US Drug Formulary STU 2.0.1, PDex Plan Net. (**High**)

**What the Prior Authorization API must functionally do** — the requirement, independent of IG. Payers must implement an API allowing a provider to: (1) **determine whether prior authorization is required**; (2) **identify documentation requirements**; (3) **receive approval/denial status**, with the **specific reason** on denial. (**High**)

**PAS's provider-side posture:** PAS **STU 2.1.0** (2024-12-20) contemplates an **intermediary** that "can convert the FHIR requests to the corresponding X12 instances." Under the enforcement discretion, trading partners "SHALL disregard any requirements in this Implementation Guide to translate the PAS FHIR Bundle into or out of the X12 278." **No certification or registration requirement for provider systems.** (**High**)

#### Q1c. Real-world readiness as of late 2026

**Enforcement discretion — the one firm, favourable fact.** HHS issued a "Statement of Enforcement Discretion for Referral Certification and Authorization Transaction" on **2024-06-13**: HIPAA Administrative Simplification enforcement will not be taken against covered entities choosing **not** to use X12 278 and instead using an **all-FHIR Prior Authorization API**. No terminal date, but HHS "presently anticipate[s] that it will be bounded by a future rulemaking." (**High**)

**No delay to the 2027 dates has been announced.** CMS-0062-P does not propose to move the non-drug 2027 dates — it states it is "not proposing to change" the existing 72-hour expedited timeframe, and its new dates are additive. (**Medium-High**; proving a negative by search is inherently weaker than a primary source.)

**The best-documented implementation, and its limits.** Humana + athenahealth + Availity, using the Da Vinci CRD/DTR/PAS guides: ~**17,585** orders/month avoided needing auth verification, ≈**4,396 staff hours/month** saved; **70%** monthly average auto-approval; ~**54%** of requests needed no authorization; **26 hours** average time to approval or denial, **Oct–Dec 2023**; **no** authorizations denied for insufficient documentation. (Availity case study. **VENDOR/PARTNER SELF-REPORT. Low-Medium** on the figures.) **Limits:** the window is **Q4 2023**, nearly three years stale; pilot-vs-production is not stated; and the participants are a national payer, a national EHR vendor and a national clearinghouse — the opposite of a one-site center with no EHR.

**Figures that are NOT usable.** "58% reduction in PA decision cycle time at a regional Medicaid MCO" and "auto-approval rates above 80% at large commercial payers" appear only in vendor blogs with no named payer, methodology, or date. **Do not use.** (**Low — unusable**)

**On CAQH.** Rebranded to the **DataSpring Index**; caqh.org/insights/index-report now 301-redirects. The **2025 Index is the 13th edition** (2024 activity, released ~2026-02-19), now **registration-gated with Index Pro at $899/user**, and its per-transaction table is rendered as charts rather than extractable text. Verified from the official CAQH deck: medical PA **electronic adoption 40%** (up from 31% in 2023); **15 minutes** saved per PA using X12 278 vs fax/email/mail; **$21B** total industry savings opportunity; **$258B** administrative cost avoided in 2024. (**High/Medium**)

**🔴 A conflict in circulating figures, resolved.** Read directly from the official 80-page 2024 CAQH Index PDF — **provider** cost per prior authorization: **manual $12.88**, partial (portal/IVR) **$8.93**, electronic (X12 278) **$5.38**. Also eligibility/benefit verification $8.57/$4.46/$2.00 and claim status inquiry $13.80/$5.24/$3.64; provider time **24 minutes** by phone/fax/email, **16 minutes** via portal. **Secondary sources variously quote "$11.44/$3.82," "$11.17/$1.89," and "$8.03/$2.65" — none matches the official table.** Use the figures above with the edition named, or do not use them. **All CAQH data is industry self-report, not audited accounting.** (**High**)

#### Q1d. What it takes for a small center to CONSUME a payer PA FHIR API

**The rule imposes no registration, certification, or attestation burden on the provider, and PAS imposes none either.** That is real. (**High** on the absence of a *regulatory* burden.)

**But the rule does not deliver a connection, and four barriers remain:**

1. **Per-payer onboarding is a commercial and technical reality.** Payers run developer portals with their own registration and app approval. Authentication for bulk provider-facing access is expected to use **SMART Backend Services (asymmetric JWT)**, with OAuth 2.0 client-credentials as a simpler alternative; the current Provider Access recommendation is an **attestation workflow** (v2) rather than attribution lists. (Secondary technical sources; Aetna's developer portal returned only a JS shell. **Medium**) **Net: per-payer onboarding effort is real, unquantified, and the single biggest cost driver in candidate #1.**
2. **The Provider Access API requires an in-network relationship — a genuine greenfield problem.** CMS requires sharing with providers who have "a contractual relationship with the payer and a treatment relationship with the patient," and **encouraged but did not require** sharing with out-of-network or unenrolled providers. (**High**) A center opening April 2027 will be mid-credentialing; until contracted, the richest data API is unavailable. **The Prior Authorization API carries no such condition** — the rule says it "allows a provider to query a payer's system" — so the auth workflow is available earlier than data retrieval.
3. **Patient opt-out applies** to Provider Access, so coverage is less than 100% by design. (**High**)
4. **Agents acting for the practice are contemplated.** CMS stated providers should be able "to delegate administrative tasks to their staff," that payers "should set reasonable requirements that allow staff to provide information or perform tasks on a provider's behalf," and that "the attribution process should not impede this benefit." (**High**) Favourable footing — though CMS is describing *staff*, and reading it as blessing autonomous software is an extension, flagged as such.

**Do clearinghouses intermediate it, and does that negate the advantage?** Partly, and it does not negate it. PAS explicitly contemplates an intermediary; **Availity** markets a "CMS-0057-F Interoperability Suite" with a connectivity hub claiming **>3.4 million providers**, and **Waystar** an Authorization Suite it says "supports CRD, PAS, and DTR integrations while routing requests based on payer, plan, and service requirements." (**VENDOR CLAIMS. Low** on specifics, **Medium** on existence.) **Assessment:** a clearinghouse is the pragmatic path to breadth, and the differentiator in candidate #1 was never transport — it is orchestration: detecting auth-required orders, assembling the packet, tracking clocks, and **drafting and filing appeals**. Clearinghouses move transactions; they do not file the appeal nobody has time to file. The honest statement is that the center will probably pay a clearinghouse for connectivity **and still have the appeal gap.** (**Medium**, reasoned assessment)

#### Q1e. Is the FHIR mandate a leveling event?

**Assessment: partially, and less than the category's rhetoric suggests.**

**Levels:** the API must be offered to any querying provider with no volume floor, no certification, and **no in-network condition on the PA API** (**High**); provider-side conformance is unregulated (**High**); enforcement discretion removes X12 278 expertise as a barrier (**High**); public metrics and published auth-required lists are free inputs available equally, and small operators are better placed to act on them (**High**).

**Favours incumbents:** per-payer onboarding cost is roughly fixed, so cost per study falls with volume (**Medium**); the Provider Access in-network condition penalizes the newly opened specifically (**High**); because the IGs are only recommended, absorbing N payer variants is itself an economy of scale, and CMS's own NPRM confirms the variation is expected (**High** on variation, **Medium** on the conclusion); payer-funded tools arrive free and payer-first (§2.14).

**And the imaging-specific one that matters most:** advanced imaging authorization is largely **delegated to RBMs** — **eviCore** (Cigna, Aetna commercial, Humana, UHC Oxford), **Carelon** (Elevance/Anthem and many BCBS plans), **Evolent/RadMD** (regional BCBS and Medicaid MCOs). One secondary aggregation of public payer documents counts **eviCore named by 70 payers, Carelon 51, Evolent 32, Optum 28, Prime Therapeutics 27** (**Low-Medium**; underlying filings not verified). CMS holds payers responsible for delegated entities, but **whether the imaging decision is reachable through the payer's FHIR PA API is UNVERIFIED and is the most important open technical question in this build.** (**Medium-High** on RBM dominance)

**Bottom line for the pitch:** the mandate levels the **interface**, not the **integration cost**, and does not level the RBM layer where imaging authorization lives. The durable small-provider advantage is **follow-through on appeals** — a workflow and capacity asset, not a technology one — which the AMA's 2026 data continues to support (59% don't expect to win, 52% lack time, only 24% say denials are competently reviewed). **Do not pitch FHIR as the moat.** (**Medium**, explicitly a judgment)

### Q2 — DICOM / imaging data access

#### Q2a. DICOMweb support among small-center PACS/RIS vendors

**The single most important contract distinction: "has an API" is not "has DICOMweb."** A proprietary API means every integration is a sunk cost if the vendor changes; a DICOMweb API means the integration survives the vendor.

| Vendor / product | DICOMweb documented? | Evidence class | Confidence |
|---|---|---|---|
| **Sectra** PACS/VNA | **Yes** — QIDO-RS provider + client | Published DICOM conformance statement | High |
| **Fujifilm Synapse** | **Yes** — WADO-URI, WADO-RS, QIDO-RS, STOW-RS | Published conformance statement | High |
| **Visage 7** | **Yes** — QIDO-RS, WADO-RS/URI, STOW-RS | Conformance statement + product page | Medium-High |
| **RamSoft** PowerServer / OmegaAI | **Partial/likely** — OmegaAI marketed on DICOMweb + FHIR R4; conformance index lists DICOM and FHIR statements but **no DICOMweb-specific doc** | VENDOR CLAIM + conformance index | Medium |
| **Ambra Health / Intelerad InteleShare** | **Proprietary REST, NOT DICOMweb** | Public API reference, directly inspected | High |
| **Intelerad** IntelePACS | Claimed via search snippet only; no public developer portal found | Search index | Low-Medium |
| **eRAD** (RadNet) | **Proprietary HTTP API**; DMWL for worklist; no DICOMweb claim found | Vendor pages | Medium |
| **Merative / Merge** | Conformance covers DIMSE, media storage, MWL; DICOMweb **not** evidenced | Conformance index | Low-Medium |
| **Konica Minolta Exa** | "A new API" per trade press; no DICOMweb doc found | Trade press + VENDOR CLAIM | Low |
| **Novarad / PaxeraHealth / Hyland Acuo** | "DICOM-compliant"/"DICOMweb integrations" asserted; no conformance doc located | VENDOR CLAIM | Low |
| **Change Healthcare / Optum** | **UNVERIFIED** — no accessible conformance or developer doc found | — | — |

Key specifics worth putting in a contract: **Fujifilm Synapse added STOW-RS and extended WADO-RS at version 5.3.000** — a usable version floor. **Sectra** runs a QIDO Provider *and* a QIDO client that can fan a query across multiple providers.

**The Ambra finding, stated plainly.** Ambra/InteleShare publishes a complete public API reference (1.65 MB, directly fetched and grepped): **zero** occurrences of DICOMweb, WADO, QIDO, or STOW. It is an excellent *proprietary* JSON/HTTPS API — including per-study audit trail and webhooks, both genuinely useful for operational analytics — with essentially no DICOMweb surface. **This is the cleanest illustration of real lock-in: not "no API" but "an API you cannot port."** (**High**)

**Extra-cost gating: UNVERIFIED for every vendor.** No PACS vendor publishes an API price list. Treat "is DICOMweb included in the base license, at no incremental cost, for the life of the agreement?" as an **open contract question, not a known fact.** (**High** that it is absent from the public record)

**Shortlist implication:** on documented DICOMweb alone, **Sectra, Fujifilm Synapse and Visage** are evidenced; **RamSoft OmegaAI** is plausible and worth a direct conformance request given its small-center fit.

#### Q2b. The "data hostage" problem

See §2.15. Headline: **the strong version of this claim is not supported by the public record** — no litigation, no published API-access fee schedule. The documented problem is *migration*, and the mechanism is that **pixels port but context does not**: "each vendor's database structure remains proprietary," textual patient/exam information and pointers "are imported incorrectly," and "there is little incentive for the legacy vendor to make a deal." Annotations and key-image flags are often proprietary. But the dollar figures ($400k+, "several hundred thousand") are **2007 and hospital-scale** and must not be presented as numbers Luis and Fernando would face. (**High** for the quotes, **Low** for present-day applicability.)

One caution: the AuntMinnie article titled "9 ways to reduce your legal exposure to PACS problems" (2018) **does not discuss egress, extraction, API fees, or data ownership at all** — the title is misleading and it would be easy to miscite. (**High**)

#### Q2c. Operationally valuable DICOM metadata — reliable vs theoretical

**This has the best evidence in the brief. The organizing insight: reliability depends on WHO WRITES THE VALUE.** Machine-written, standard-required values are dependable. Free-text and human-entered values are not.

**TIER 1 — reliably populated. Build the product on these.** Study Date/Time (0008,0020 / 0008,0030), Series Date/Time (0008,0021 / 0008,0031), Acquisition Date/Time (0008,0022 / 0008,0032), Content Time (0008,0033), Modality (0008,0060, enumerated and required), **Station Name (0008,1010)** for per-scanner/per-room attribution, Series Number (0020,0011). All **High**.

From Tier 1 alone, with no vendor cooperation and no extra module: exam duration (last − first timestamp in study), **inter-exam gap and scanner idle time** (grouped by Station Name), room operational day length, exams per operational hour, series counts per exam. All **High** feasibility.

**The peer-reviewed proof.** **Niffler** (Kathiravelu et al., *J Digit Imaging* 2021;34(4):1005-1013, PMID **34405297**, PMC8455728, open access) is an open-source DICOM framework deployed at **Emory Healthcare across 715 scanners spanning 12 sites**, retrieving up to **350 GB/day** as a real-time stream over two years. Its Metadata Extractor was used specifically "to understand the **operational efficiency of individual MRI systems**," benchmarked against the institution's Clinical Data Warehouse:

> "Niffler accurately identified the scanners' examination timeframes and idling times, whereas CDW falsely depicted several exam overlaps due to human errors."

**Three conclusions, and they upgrade candidate #4 from "Evidence: Low (no external evidence)" to High.** (1) Scanner utilization and idle-time analytics from DICOM metadata is peer-reviewed, deployed and open-source. (2) DICOM metadata was **more accurate than the enterprise data warehouse**, because the warehouse carried human data-entry error — the analogous comparison at an imaging center is DICOM versus RIS-entered times, which argues the DICOM-derived numbers are the trustworthy ones. (3) **The critical caveat:** the same paper "identified scanners with **misconfigured time** and reconfigured five scanners." **Scanner clock validation is a prerequisite, not an afterthought** — it belongs in the specification, with ongoing NTP monitoring.

**The best commercial precedent, and the best pitch citation.** "Use of Image-Based Analytics for Ultrasound Practice Management and Efficiency Improvement," *J Digit Imaging* 2019, PMID **30623273**. Collects from "tens of thousands of DICOM images" using "structured reporting, public and private DICOM headers, and text within the images via optical character recognition." Computes "median exam length (time from the first image to last), transducer models used in an exam, and exams performed in a particular room, practice location, or by a given sonographer," plus "the length of a scan room's operational day, the number and type of exams performed, the time between exams, and summary data such as exams per operational hour and time-based room utilization." **Documented financial outcome: "two defective probes were not replaced (a savings of over $10,000) when utilization data showed..."** (abstract truncates). (**High**)

Three things to note: it validates the exact metric set, in an **outpatient-relevant modality**, peer-reviewed; the documented saving is **equipment capital avoidance driven by utilization data** — a concrete, defensible benefit type; and **they needed OCR and private tags**, which honestly signals standard public tags alone were insufficient for their full metric set.

**TIER 2 — available but frequently unreliable. Verify before promising.**
- **Operators' Name (0008,1070) — LOW-MEDIUM.** Type 3 (**optional**). Depends on the technologist logging in; commonly blank, shared logins, initials, or free text. **Do not promise per-technologist analytics without a site-specific audit.**
- **Performing Physician's Name (0008,1050)** — same class of problem.
- **Protocol Name (0018,1030) — LOW-MEDIUM.** Free text, locally invented, drifts.
- **Body Part Examined (0018,0015) — LOW-MEDIUM.** Documented as too generic: a pancreatitis study and a renal-stone study both carry "abdomen," so one paper derives body part from the free-text **Study Description** instead, reaching 99.94% accuracy (*Stud Health Technol Inform* 2013, PMID 23920517). **This inverts the naive assumption: (0008,1030) Study Description is often more informative than (0018,0015).** And a 2025 study on 20,000 routine PACS X-rays **collapsed 116 distinct header body-part entries into 36 SNOMED CT codes** (*BMC Med Imaging* 2025, PMID 41390620) — direct quantitative evidence of real-world tag chaos. (**High**)
- **CTDIvol (0018,9345)** — CT only, and RDSR is the better path. **Exposure (0018,1152)** = mAs. **KVP (0018,0060)**.
- **Burned In Annotation (0028,0301)** — flags pixel-burned PHI, which defeats header-level de-identification. Security-relevant for any outbound flow, AI vendor, or research sharing.

**TIER 3 — MPPS: highest operational value, lowest availability.** Performed Procedure Step Start/End Date and Time (0040,0244 / 0040,0245 / 0040,0250 / 0040,0251), PPS ID (0040,0253), PPS Description (0040,0254). MPPS start/end are the **only** attributes directly expressing true procedure duration rather than inferring it from image timestamps (Noumeir, *J Digit Imaging* 2005;18(4), PMID 15988627. **High**). **Critical caveat: that paper's stated purpose is to "bridge the gap between MPPS implementation and deployment" — i.e. MPPS was specified and under-deployed, and the paper exists because of that gap.** In small outpatient centers with mixed or older fleets, **assume MPPS is absent until proven present, per scanner.**

**Design consequence, and it is the opposite of what the standard would suggest:** compute duration from series/acquisition timestamps as the **primary** method, and treat MPPS as a precision upgrade where available. That is the correct engineering call.

**NOT RELIABLY EXTRACTABLE — repeat/reject rate.** **AAPM Task Group Report 305** (Little et al., *J Appl Clin Med Phys* 2023;24(5):e13938, PMID 36995917) exists because of this: "**Due to the lack of standardization, reject data often cannot be easily compared between radiography systems from different vendors.**" TG305 *proposes* standardized data elements and a reject-reason schema — the standard does not yet exist in practice, and the authorship spans Agfa, GE, Canon, Fujifilm and major academic centers, so the fragmentation is industry-wide. Reject data lives in **vendor-proprietary software embedded in the X-ray unit**, not in standard DICOM tags reaching PACS. **Name TG305 in the contract if reject analysis matters.** (**High**)

For scale only: a single busy ED digital X-ray room audit of **11,596 images** found a **10.3%** overall reject rate, 1.3% multiple-reject, worst projections horizontal-beam hip 33.5% and knee 30.5%, top reasons positioning **67.1%** and anatomy cut-off 8.4% — data from reject software **embedded in the X-ray unit** (*J Med Radiat Sci* 2021, PMID 33826800). ⚠️ **Australian ED, not US outpatient — order-of-magnitude only.** Note positioning dominance makes reject rate primarily a **training** signal.

**PROVEN AND COMPLIANCE-BACKED — dose via RDSR.** The ACR **Dose Index Registry** startup guide is unambiguous: "**RDSRs are the sole means of data tranferrence and scanners should be configured to send RDSRs or they will not be included in the registry.**" Secondary capture is no longer accepted. Submission requires **ACR Connect** on a physical or virtual server at the facility, with the **DIR Link** application, which "enables the collection, de-identification, and transmission of data securely from CT scanners, fluoroscopes and x-ray devices." Modalities: CT (since 2011), fluoroscopy, digital radiography; nuclear medicine "soon." **DIR participation meets the Joint Commission dose benchmark requirement** and can support MIPS via the ACR's QCDR. Annual fee scales with physician count and number of sites. (**High**)

**Two consequences:** **RDSR routing must be a scanner-configuration and PACS-routing requirement at commissioning** — if scanners are not configured to emit RDSR, the dose data does not exist retroactively; and the center likely needs DIR anyway for Joint Commission purposes, so dose analytics is a compliance obligation it can extract operational value from rather than a new cost.

Supporting dose evidence: a PRISMA systematic review (1,293 screened → **49 included**, *Physica Medica* 2025, PMID 40694887) finds dose-monitoring software enables benchmarking against diagnostic reference levels and scanner comparisons, but concludes "**effective implementation requires skilled users, standardised protocol naming, and regular data verification**" — the empirical backbone of the Tier-2 warning, and the reason protocol-level analytics must be scoped and priced **with a normalization step**. (**High**) Deployment footprint: Radimetrics in 20 studies, DoseWatch 12, Qaelum DOSE 4, Imalogix in North America (**Low-Medium**, paywalled market report). DoseWatch ingests from **RDSR, image headers, MPPS, and OCR** — the multi-source fallback chain is itself evidence that no single source is complete.

Open-source dose precedent with a quantified win: **OpenREM + openSkin** across three PDSA cycles "eliminated the possibility of a high skin dose procedure failing to trigger an investigation" and **reduced staff time on skin-dose investigations by an estimated 94%** (*BMJ Open Qual* 2020, PMID 31986118. **High**). A free tool with a measured automation benefit — directly relevant to an automation pitch.

#### Q2d. A "DICOM + FHIR unified operational data layer"

**Verdict: the cloud DICOMweb layer is production-real and GA; the DICOM→FHIR mapping is real but Trial Use; FHIRcast is emerging; operational analytics on DICOM metadata is production-real. But there is NO published case study of a unified DICOM+FHIR operational layer at a small outpatient center.**

**Open-source — production-real, zero license cost.** **Orthanc** DICOMweb plugin provides "a basic, reference implementation of WADO-URI, WADO-RS, QIDO-RS and STOW-RS, following DICOM PS3.18," **both server and client** — the client role matters, because it is exactly the "sidecar analytics without touching the PACS" pattern. **dcm4chee-arc-light 5** provides QIDO-RS/WADO-RS/STOW-RS (tri-licensed MPL/GPL/LGPL). **OHIF Viewer** configures qidoRoot/wadoRoot/stowRoot independently, documented-compatible with dcm4chee 5.x, Orthanc, DICOMcloud, OsiriX, Horos; requires archive exposure plus CORS. All **High**.

**Cloud services — all three GA, all three support DICOMweb. Published pricing, scraped 2026-10-10:**

*Google Cloud Healthcare API DICOM store* — bills **two** storage components: Structured (metadata index) ≈**$0.24/GiB-month** (1–1,024 GiB tier) dropping to ≈$0.19 above, and Blob (pixels) ≈**$0.02/GiB-month**, with 0–1 GiB free on each. Colder classes down to Archive $0.00000411/GiB-hr; retrieval Standard $0, Nearline $0.01/GiB, Coldline $0.02/GiB (90-day minimum with early-deletion fee), Archive $0.05/GiB. Requests: first 25,000 free, then $0.39–$0.99 per 100k by class. **Egress-shaped operations: Export batch $0.19/GiB (0–1) → $0.14 → $0.09; Export streaming $0.34 → $0.29 → $0.24; Transcode $0.003–0.004/GiB.** (**High**)

*AWS HealthImaging* — GA, HIPAA-eligible. **Frequent Access $0.105/GB-month; Archive Instant Access $0.006/GB-month; data import FREE; API calls $0.005/1,000; minimum billable image set 5 MB; 10 GB structured storage pre-provisioned per data store; auto-tiering after 30 days inactivity; outbound transfer charged, in-region to AWS services free.** ⚠️ **Architectural caveats:** it does **not** store plain DICOM P10 as-is — it reorganizes into **image sets** mapped to series, **normalizes** patient/study/series metadata, exposes metadata by **human-readable keywords rather than hex tags**, and returns pixels as **HTJ2K**. It offers "DICOMweb conformant APIs" plus **cloud-native APIs for actions DICOMweb does not support, like metadata update.** The normalization is genuinely useful for analytics, but **it is a transformation, not a faithful archive, and the non-DICOMweb surface is itself a portability consideration.** Native C-STORE/DIMSE support **UNVERIFIED** — appears S3/API-import oriented, likely needing a DICOM router in front of modalities. (**High** on pricing; **Low** on DIMSE)

*Azure Health Data Services DICOM service* — GA, PHI-designed, LRS replication, RBAC, data isolation per API instance. Supports **Studies Service** (PS3.18 ch.10) with a nonstandard delete, and **Worklist Service (UPS-RS)** Push and Pull SOPs. Pricing from the official Azure Retail Prices API (the web page renders `$-` via JS): **Structured Storage $0.39/GB-mo; Blob Storage $0.023/GB-mo; API Requests $0.54/100k; Transcode $0.004/GB; Export Batch $0.19 → $0.139992/GB; Export Streaming $0.34 → $0.289986/GB; Notifications $0.59/1M; Structured De-Identification and Transformations $1.14/GB.** Billing mechanics: initial-mode import not charged; responses ≥500 or 429 not charged; **multi-part DICOMweb requests are charged PER DICOM INSTANCE** — a real cost trap for high-slice CT/MR. (**High**)

**Three Azure features are directly on-thesis:** **Change Feed** — "ordered, guaranteed, immutable, read-only logs of all changes," readable independently and in parallel at the client's own pace (a proper event stream for analytics without polling); **DICOMcast** — open-source, self-hosted in Azure, which "inject[s] DICOM metadata into a FHIR service or FHIR server as an imaging study resource," i.e. **a shipping implementation of the DICOM→FHIR ImagingStudy pattern from a hyperscaler**; and **Extended query tags** — index on standard *or private* DICOM tags beyond the conformance defaults, which matters given the ultrasound-analytics paper needed private tags. (**High**)

**Cost sanity check:** at single-center scale, cloud DICOM storage is **not** a barrier — roughly $100/month order-of-magnitude for a year's hot data at AWS frequent-access rates, far less archived. But **per-GB rates alone will mislead**: Azure charges per instance on multi-part requests, architectures differ (normalization, HTJ2K, free import), and real cost depends on volume, instance counts, retention and tiering. **Model it against Luis's projected volumes.** (Arithmetic from published rates; volume assumption illustrative only.)

**DICOM→FHIR at scale — production-real for research.** A German Medical Informatics Initiative pipeline extracts, converts and pseudonymizes DICOM metadata into **ImagingStudy** FHIR resources, deployed at the Data Integration Center of University Hospital Erlangen, evaluated at large scale across two departments (*Methods Inf Med* 2024, PMID 40233823, PMC12133321. **High**). **Classification: production-real for research data integration at a large academic hospital — NOT a small-outpatient operational deployment.** The *pattern* is proven; the *context* is not analogous.

**FHIRcast — emerging, do not depend on it.** Publish/subscribe context sync (radiologist opens a study; viewer and dictation follow), current version **STU2**, radiology as canonical use case. Adoption is limited with an acknowledged chicken-and-egg dynamic. The RSNA *Imaging AI in Practice* demonstration has run since 2020 with **>20 vendor partners** and "improved support for FHIRcast in 2024" (*Radiology* 2026, PMID 42301015. **High**) — but **that is an annual conference demonstration: strong evidence of vendor engagement, weak evidence of production deployment.** The official FHIRcast site, as retrieved, named **no vendor implementations and no deployments**. A Firely survey reporting FHIRcast at "40% extent of use" is self-selected, vendor-published, with an undefined metric — **do not quote it as 40% adoption.** The relevant IHE profile framing it is **Integrated Reporting Applications (IRA)**. **Verdict: name it as a desired roadmap capability, not a 2026 requirement.** (**Medium**)

#### Q2e. IHE profiles as contract leverage — with a material limitation

| Profile | Status | Leverage |
|---|---|---|
| **Scheduled Workflow.b (SWF.b)** | **Final Text** (Rev 19.0, 2020-09-18) | **The anchor profile** — order→schedule→acquire→store consistency; **includes MWL and MPPS transactions** |
| **Portable Data for Imaging (PDI)** | Final Text | Patient/outside-provider media — relevant to a new center building referral relationships |
| **Imaging Object Change Management (IOCM)** | Final Text (Rev 14.0, 2014-07-30) | Correction/deletion propagation — **data-integrity leverage** |
| **Cross-enterprise Document Sharing for Imaging (XDS-I.b)** | Final Text (2012-07-24) | Cross-enterprise sharing; **Imaging Document Source must be grouped with ATNA Secure Node** (auditing and node authentication come bundled — a benefit to claim) |
| **Radiation Exposure Monitoring (REM)** | Final Text (Rev 12.0, 2012-07-24) | **The dose profile to name** — RDSR conveyance. Prior work omitted it |
| **Mammography Acquisition Workflow (MAWF)** | ⚠️ **RETIRED 2024-06-25** | **Do NOT name in a 2026 contract** |
| **Integrated Reporting Applications (IRA)** | Framework for FHIRcast context sync | Forward-looking only (**Medium**) |

**Also: MPPS is a transaction set inside SWF.b, not a standalone profile.** Ask for "**SWF.b conformance including the MPPS actors and transactions**" — more precise and harder to wriggle out of.

**🔴 The limitation that must travel with any IHE contract language.** An **IHE Integration Statement is prepared and published by the VENDOR, not by IHE.** From IHE's own General Introduction Appendix F, verbatim: "**Vendors are solely responsible for the accuracy and validity of their IHE Integration Statements**," and "**IHE and its sponsoring organizations have not evaluated or approved any IHE Integration Statement.**" IHE further states "IHE Integration Profiles are not statements of conformance to standards, and **IHE is not a certifying body**," that "vendors publishing IHE Integration Statements accept full responsibility for their content," and that Product Registry data is "exclusively entered by vendors." On Connectathon testing generally: "The IHE testing process is **not intended to independently evaluate, or ensure, product compliance**, but to offer a practical and effective assessment of interoperability." (**High**)

**So naming a profile is necessary but not sufficient leverage.** An Integration Statement is contractually useful as a **representation you can bind the vendor to** — not third-party proof.

**Two published verification sources, one much stronger than the other:**
- **IHE Product Registry** (`product-registry.ihe.net`, HTTP 200 verified; Gazelle-hosted UI, user manual published) — **vendor self-declared.** Browse systems by IHE Actor and Profile. IHE's own guidance: the database is easier to search, but **the vendor-published Integration Statement document is the primary source.**
- **🟢 IHE Connectathon Results** (`connectathon-results.ihe.net`, HTTP 200, verified) — **independently TESTED, and the stronger check.** Covers **89 editions, 899 companies, 207 unique profiles tested**, "thousands of vendor-to-vendor connections," with per-company pages carrying test results and any **IHE Connectathon SEAL** earned. Two search modes: Company Search (filter by year/actor/profile) and a Custom Search Matrix (company + profile + actor simultaneously).

**The verification procedure to run on the shortlist — and the contract language:**
1. **Get the artifact.** Require the vendor's own **IHE Integration Statement PDF for the exact product AND version** being sold. Version matters: RamSoft publishes *three separate* PowerServer v6.0 statements by component, and Fujifilm's STOW-RS support begins at **5.3.000**.
2. **Cross-check the self-declaration** in the Product Registry — confirm claimed Actors/Profiles match the PDF.
3. **🟢 Cross-check independent testing** on connectathon-results.ihe.net, filtered to the profile and actor, confirming a **recent year**. **A gap between what the Integration Statement claims and what was actually tested at a Connectathon is the highest-value question you can ask in a vendor meeting.**
4. **Require the DICOM Conformance Statement separately** — IHE conformance ≠ DICOMweb. Demand the PS3.18 section naming **QIDO-RS, WADO-RS, STOW-RS** explicitly, and whether **UPS-RS Worklist** is included.
5. **Bind it:** product + version; **SWF.b including MPPS actors/transactions**; **REM**; **IOCM**; **PDI**; **XDS-I.b** if cross-enterprise sharing is in scope; **DICOMweb QIDO-RS/WADO-RS/STOW-RS per PS3.18 at no incremental license cost for the life of the agreement**; **AAPM TG305** data elements if reject analysis matters; and **documented, fee-transparent export and migration terms**. **Do not name MAWF.**

**This generalizes to a principle worth saying at the table: demonstration beats declaration for every interoperability claim** — which is the same move GIO-STRATEGIC-ANSWERS line 189 already recommends for claimed FHIR capability.

### Q3 — Agent apps, human-in-the-loop, and the referring-physician channel

#### Q3a. Agentic administrative automation: what exists, and who can actually buy it

**The buyability question has a cleaner answer than the feature question, and tier matters more than features.**

| Tier | Who | Single-site can buy? |
|---|---|---|
| **Payer-funded / payer-contracted** | Cohere Health, Anterior, Availity (base tier), Rhyme (increasingly) | **No — cannot buy. Arrives via the payer.** Free to provider, serves payer's interest |
| **Enterprise provider-side** | Notable, Hyro, Abridge, Ambience, SmarterDx, Latent, Waystar, R1/Humata, Parlance, Syllable, Infinitus | **No / impractical.** Health-system sales motion, 5–6 figure floors, no self-serve |
| **Plausibly reachable** | Candid Health (% of collections), Honey Health (per-PA), **Alpha Nodus via RamSoft**, Luma Health, Artera, Tennr, Assort (at its $75K floor), Staffingly (human BPO) | **Yes, with caveats** |

**Several vendors are mislabelled as agentic.** Genuinely agentic: **Anterior** (genAI clinical reasoning with vendor-staffed clinician review), **Latent**, **Waystar AltitudeAI** (autonomous claim resubmission), **Artera** (multi-turn SMS + voice that actually writes the reschedule), **Adonis** (agentic orchestration over RPA actuation). Not agentic despite the branding: **Rhyme** is network/EDI plumbing; **Availity** self-describes as "a transparent AI **recommendation** engine, **not a decisioning engine**" — the most honest positioning found; **Cohere** is clinician-built guideline logic with an LLM as a *future* build; **Abridge/Ambience** are generative ambient capture, not agentic; **Parlance** is conversational IVR.

**The best fit for this engagement, and it is radiology-native: Alpha Nodus "Gravity AI" inside RamSoft PowerServer RIS/PACS.** AI-driven front-office automation — **prior authorizations, scheduling, document tasks** — delivered as a module **inside the radiology system of record**, with real-time payer-requirement verification. Claimed "up to **25% reduction of claim denial rates**" and PAs "fully automated or reduced to just minutes." I had the Diagnostic Imaging article (2025-03-26) fetched and verified: **this is a VENDOR CLAIM presented as a stated benefit with no independent validation, no measurement data, and no pilot study cited**; the "minutes" quote is from the Alpha Nodus CEO, and target practice size is not specified. **But RamSoft PowerServer is sold heavily to independent and small imaging operations, so this is the highest-fit, lowest-friction option identified** — it arrives in a system the center would already own. (**High** on the fit; **High** that the outcome figure is a vendor claim)

**Other single-site-native options worth naming:** **Honey Health** submits and chases imaging PAs through RBM and payer portals, priced **per completed PA at roughly $1.50–$2** including status follow-up — the only genuinely single-site-native pricing model found (**Low-Medium**; source is the vendor's own comparison listicle). **Candid Health** at **3% of collections** (plus $6/claim with coding) scales down naturally with no license floor (**Medium**, third-party reported). **Staffingly** at **$399/week for one dedicated specialist** is outsourced human labour marketed alongside AI — **include it as the honest "do nothing clever" benchmark (~$20.7K/yr) against which agentic options must justify themselves.**

**Radiology-specific vs general.** Purpose-built: **Alpha Nodus/RamSoft, CodaMetrix** (radiology flagship), **Honey Health, Staffingly, Nakod**. Imaging in the market narrative but **not** confirmed deployments: **Tennr** (its own $101M Series C release does not mention radiology or imaging centers; all named customers are DME/home-medical — the radiology framing is trade press). Explicitly **not** covering radiology: **Assort Health** (radiology absent from its 23+ specialty list), **Abridge** and **Ambience** (no radiology product line). On the last two there is also a **category error worth naming: ambient conversation capture is built around a clinician–patient encounter, and diagnostic radiology reporting is dictation over images with no patient conversation.**

**Three kill-list items.** **Thoughtful AI** — sunsetting stand-alone services with a 90-day forced migration, and its entry tier assumed $100M+ revenue (**Medium**, single trade source — re-verify before citing publicly). **SmarterDx** — rule out on **fit**, not price: its unit of value is the **DRG discharge**, an inpatient construct an outpatient imaging center does not have. **Humata Health** — **R1 RCM closed its acquisition ~2026-09-16**, and Humata's July 2026 independent-provider push is the thing most at risk; treat as a diligence question, not an assumption. **Janus Health** and **Orby AI** — no substantive healthcare evidence found at all (Orby is general enterprise RPA, acquired by Uniphore; its inclusion in a healthcare list appears to be an error).

**The closest analogue to imaging prep/no-show outreach:** **Artera** (#1 Best in KLAS for Patient Communications, 2026) deployed at **Atlantic Health** for **colonoscopy patient outreach** — procedure-prep plus real-time reschedule, SMS and outbound voice. The pattern transfers directly to imaging prep. (**High** on the deployment; outcome figures VENDOR CLAIM.)

**On measured outcomes, the structural finding bears repeating:** the closest thing to a measured result in the entire set is **Humata/Allegheny Health Network — in the first month, 70% of requests for covered CPT codes approved with zero AHN staff involvement after EHR order entry** (named site, time-bounded, specific) — but it was **announced via vendor press release**. **CodaMetrix/OHSU** radiology figures (92% autonomously coded, ~70% reduction in coding-related denials, 27.7–28% coder workload decrease, 0.33% automated denial rate) are specific and radiology-relevant, but I had the page fetched and verified: **vendor-published, undated, promotional, no HIL architecture described, and no peer-reviewed JACR publication exists.** The most honest source encountered was a reviewer who self-flagged that vendor metrics are "not independently audited" and are "single-customer results, not averages." **Apply that caveat to every percentage in this subsection.**

#### Q3b. Human-in-the-loop: evidence, failure modes, and the governance stack

**🟢 The strongest authority is CMS's own pilot.** The **WISeR Model** (Wasteful and Inappropriate Service Reduction) — AI-assisted prior authorization and pre-payment review in **Original Medicare**, announced June 2025, **active 2026-01-01**, **six-year** run, in **six states including TEXAS** (Arizona, New Jersey, Ohio, Oklahoma, Texas, Washington). **CMS requires a human clinician to review every decision not to affirm coverage**: six private companies use AI to assist, but "**all recommendations for non-payment are determined by appropriately licensed clinicians.**" (**High**) **This is the federal government establishing that AI may recommend but a licensed human must decide anything adverse** — the single best available authority for the HIL architecture, and it is *CMS's own operating standard*.

Scope caveat: named services are high-risk/overused items (skin and tissue substitutes, electrical nerve stimulator implants), reported variously as 13 service categories or 17 outpatient services. **Imaging is NOT identified as in scope** — but the **authoritative CMS service list could not be obtained**, so that conclusion is **provisional, based on absence of mention (Medium)**. Contested outcome data (an advocacy-group figure that only 62% of AI denials were approved on human review vs 84% in traditional MA) is **Low-Medium, methodology unseen — do not present as established.** The EFF filed a March 2026 transparency lawsuit.

**Documented failure modes converge on three things, not on AI itself.** Across *Estate of Lokken v. UnitedHealth Group* (D. Minn. 0:23-cv-03514 — nH Predict alleged to deny post-acute care on **population-level algorithms rather than individual clinical circumstances**; motion to dismiss **denied in part 2025-02-13** with breach of contract and implied covenant proceeding; **broad discovery compelled 2026-03-09** into implementation, use and outcomes; **in discovery, no trial date, NO LIABILITY FINDING**) and Cigna's **PxDx** (ProPublica, March 2023: medical directors denied large batches without reviewing individual files — **over 300,000 claims in two months, averaging ~1.2 seconds per claim**; California class action July 2023, second nationwide action D. Conn. August 2023, **E.D. Cal. allowed the class action to proceed 2025-03-31**), the exposure attaches to: **(a)** population-level inference in place of the individual record; **(b)** adverse determinations with no genuine human examination; **(c)** *nominal* review — a signature with no examination.

**🔴 PxDx is directly imaging-relevant:** a lawsuit alleges Cigna violated the law by denying claims for **imaging** and other services in bulk. (**Medium**) And **1.2 seconds per claim is the number that makes "human review" indefensible.** The design lesson: **any HIL architecture must produce evidence of ACTUAL review, not just a reviewer field.**

**State AI utilization-review laws — eight enacted, and seven of eight bind PAYERS:**

| State | Bill | Effective | Core requirement |
|---|---|---|---|
| California | **SB 1120** (Physicians Make Decisions Act) | 2025-01-01 | Medical-necessity denial by a licensed physician/professional; AI must use the **individual's** clinical data, not generalized datasets; AI may not deny/delay/modify autonomously; AI use disclosed |
| **Texas** | **SB 815** | 2025-09-01 | **UR agents prohibited from using an automated decision system to make an adverse determination**; only a physician/licensed provider may determine medical necessity |
| Maryland | HB 820 | 2025-10-01 | Decisions based on the individual record; **final decision by a physician**; **quarterly AI-usage disclosure reports** |
| Nebraska | LB 77 | 2026-01-01 | AI output may not be the **sole basis**; AI use disclosed to providers and enrollees |
| Arizona | HB 2175 | 2026-07-01 | **Medical director must individually review** and exercise independent medical judgment |
| **Indiana** | **HB 1271** | 2026-07-01 | AI not sole basis for downcoding/denial; **🔴 PROVIDERS must review any AI-prepared claim before submission** |
| Washington | SB 5395 | 2026-06-11 | AI not the sole means; medical-necessity denials require licensed-provider review |
| Alabama | SB 63 | 2026-10-01 | Denial/delay/modification on medical necessity by a licensed physician or qualified professional |

California SB 1120 specifics (**High**): signed 2024-09-28, amends Health & Safety Code §1367.01 and Insurance Code §10123.135, binds plans, disability insurers, specialized plans **and contracted vendors performing UR functions**, with administrative penalties for willful violations. **Indiana HB 1271 is the one that binds the PROVIDER** — if the center ever bills into Indiana, a provider-side human-review step on AI-prepared claims is a statutory obligation, not a best practice (**Medium**; single aggregator — **verify against enrolled text before relying on it**). Nevada, Illinois and Connecticut are reported as enacted-or-considering; the exact tally varies by source. **The direction of travel is unambiguous; the precise count is not.**

**Professional-society guidance, strongest first:**
- **🟢 AMA Policy D-480.956** (2026 Annual Meeting) — supports oversight requiring a process that uses accurate clinical criteria from national specialty-society guidelines and peer-reviewed literature; includes **reviews by clinicians not incentivized to deny care, with expertise for the service under review**; and "**requires such reviews include human examination of patient records prior to a care denial.**" Core principle: augmented intelligence, whether assistive or fully autonomous, "is intended to co-exist with human decision-making and should not replace physician reasoning and knowledge." (**High**)
- **🟢 ACR's first Practice Parameter for Imaging AI** (ACR–SIIM, 2026): stand up an **AI governance group** (clinical, technical, compliance leaders, **including a radiologist**) responsible whether the AI is commercial or built in-house; maintain an **inventory of all AI tools with versions and intended use**; run **local acceptance testing before deployment and track results**; **human oversight throughout**; and **local governance must be led by physicians with meaningful authority — not delegated to vendors or IT.** (**Medium-High**) ⚠️ **It is scoped to imaging AI; its governance scaffolding transfers readily to administrative AI, but do not represent it as administrative-AI guidance.** ACR also has a published road map for Practice Accreditation for Radiology AI.
- **AHIMA** — a useful precision: "**AI attestation**" means documented human review and approval of coding completed through an automated workflow before submission, and **CMS materials reviewed do NOT establish a separate AI-specific attestation requirement for providers**. **Don't let anyone sell an "AI attestation requirement" that doesn't exist.** The 2026 AHIMA/ACDIS query-practice guidelines add that organizations **must not assume a vendor-supplied or EHR-integrated tool automatically produces compliant output** — professionals must be involved in selecting, configuring, evaluating and **monitoring** it on an ongoing basis. (**Medium-High**)
- **HHS OIG** — the February 2026 updated MA Individual Compliance Program Guidance specifically addresses **AI-generated coding prompts as a risk-adjustment abuse risk** (**Medium**); an **Audit of HHS Governance of Artificial Intelligence** is on the Work Plan (**High** that it exists); OIG continues scrutinizing outpatient billing for upcoding. A reported expectation that providers maintain an **inventory of AI systems with accountable owners** plus risk classification, human oversight, privacy/cyber controls, vendor governance, monitoring and escalation is **Low-Medium** (compliance-vendor synthesis, not quoted OIG text).
- **RBMA** — the 2026 SYNC meeting addressed **vendor-agreement provisions on data use, performance standards, liability when AI contributes to billing errors or denials, and audit readiness**. This is a **conference agenda, not published guidance**, but the **contracting checklist is directly usable** and dovetails with candidate #3. ACR and RBMA also jointly issued best practices for radiology benefit managers. (**Medium**)
- **HFMA** — thought-leadership on autonomous coding; **no human-review mandate found.** (**Low-Medium**)
- **State Attorneys General** — **no AG enforcement action or AG-issued guidance specific to healthcare administrative AI found.** The activity is legislative, with enforcement vested in insurance regulators. (**UNVERIFIED** that any AG has acted.)

**Deployed review architectures with published descriptions (not theory) — six patterns:**
1. **Confidence threshold + dual queue.** Confidence values route each item to a **"Confident" queue** (auto-submitted) or a **"Review" queue** (human). **The threshold is set manually with the customer, typically >95% — explicitly higher than typical inter-coder agreement between experienced human coders.** (**Medium**) *The most directly reusable architecture found.*
2. **Role inversion.** The coder's role **evolves into auditor and exception coder**, reviewing AI work through a built-in QA process and concentrating expertise on cases that don't qualify for automation. **Staffing implication: HIL is a redeployment, not a headcount add.** (**Medium**)
3. **Human validation as the shipped product design** (SmarterDx): AI "surfaces defensible revenue and quality findings **your team validates**" — not an option. (**High**)
4. **Pre-deployment simulation / "LLM as Judge"** (Artera): a separate LLM runs simulations **before any agent goes live**, verifying it achieves the intended outcome before it touches patients. **Pattern: validate the agent, not just the output.** (**Medium**)
5. **Deterministic escalation + context handoff.** Hyro routes anything clinical or urgent to a human by design; Parlance ships an **AI-generated call summary that briefs the live agent at the moment of transfer**. **Pattern: the handoff must carry context, or the human restarts from zero and the automation is net-negative.** (**Medium**)
6. **Vendor-side clinician review team** (Anterior) — the HIL is staffed by the vendor. (**Medium**)

**Synthesis — what the evidence actually supports.** The emerging consensus standard is narrow and consistent: **AI may draft, score, route and recommend; a licensed human must decide anything adverse, and must demonstrably examine the record.** CMS's own WISeR design, California SB 1120, and AMA D-480.956 all land in the same place. **Most published obligations bind payers, not providers — with three exceptions a provider must heed:** Texas TRAIGA (patient disclosure incl. scheduling and patient-facing agents), Indiana HB 1271 (provider review of AI-prepared claims pre-submission), and Texas SB 1188 (review of AI-created records, scope unverified), plus general upcoding/False-Claims exposure that OIG now ties explicitly to AI-generated coding prompts.

**This fully vindicates the HITL design already in the deck, and upgrades its framing.** GIO-STRATEGIC-ANSWERS line 251 says a human signs every submission and appeal in phase one, and line 254 calls HITL "the FDA boundary, not just a safety nicety." The evidence says it is more than that: **it is the emerging legal standard, it is CMS's own operating standard, and the deployed architecture that satisfies it is specific and documented** (confidence threshold → exception queue → auditors → sampling QA → pre-deployment validation). **And the graduation criterion the prior work already recommends specifying is exactly right — but it must be a sampling-QA design that still produces evidence of review, never a relaxation to zero review on adverse actions.** The 1.2-second PxDx number is the argument for why.

#### Q3c. The referring-physician channel

**Start with §2.9: the volume premise fails. What follows is what IS defensible.**

**Order intake — the honest picture.** National interoperability frameworks today move **records and priors, not orders**. **TEFCA definitively does not carry orders:** the governing **SOP: Exchange Purposes v5.1 (effective 2026-07-01)** was read directly and contains **ZERO occurrences of the word "order."** Authorized Exchange Purposes are framed as Query / QHIN Message Delivery / FHIR Push for **records**. "Treatment" inherits the 45 CFR §164.501 definition, which does include "the referral of a patient... from one health care provider to another" — but that is a **privacy-law purpose category, not an order transaction.** (**High**) A related Treatment XP Implementation SOP (effective 2026-08-03) makes TEFCA Required Treatment responses mandatory for provider-associated Responding Nodes — **relevant to retrieving priors (candidate #7), not to placing orders.** (**Medium-High**) **Carequality:** no evidence it carries imaging orders; it is query-based document exchange (**Medium**). **Direct Secure Messaging CAN** via the **IHE 360X** closed-loop referral profile, which uses HL7 v2 messages of the same family already established in radiology order workflows — ReferralMD announced Direct + 360X support 2026-08-18 (**VENDOR CLAIM**, imaging orders not specifically mentioned). **Health Gorilla** (a TEFCA QHIN) states its network allows electronic lab and imaging orders — a **vendor-network capability outside the TEFCA XP framework**, with **no measured adoption data** (**Medium**).

**🔴 Drop the fax statistic.** The widely repeated "**56% of healthcare referrals are still faxed**" traces to a **fax vendor citing "industry research" with no named study, survey, year, or URL.** Adjacent figures ("89% still use fax," "70% of clinical communication via fax," "9 billion fax pages") appear only on fax- and referral-vendor blogs citing each other circularly. **Do not use any of them.** (**High** that they are unsubstantiated) **What can be defended instead:** CAQH/DataSpring measures **medical prior-auth electronic adoption at 40%**, i.e. a 60% majority remains manual (portal/phone/fax/mail) — a real, methodologically documented figure, and the honest way to evidence "the manual channel still dominates."

**The most underrated finding in this section: referrer electronic order placement is a mature, shipping RIS feature that predates the current AI wave by over a decade.** The AI intake vendors are largely automating the *fax path*; several RIS platforms already offer a *structured electronic order* path that bypasses fax entirely. Strongest evidence: **Konica Minolta Exa PACS/RIS**, whose official *Physician Portal User's Manual v34.0.0* (April 2025) documents the referrer workflow verbatim — "Create and schedule an exam… You can create an order for an exam. Staff at your facility receive the order and can schedule an appointment" → ADD STUDY → CREATE ORDER → document UPLOAD — plus a documented **"Sign an order"** function with graphical signature that clears the exam from Exa's "Unsigned Orders" report. (**High** — vendor *technical manual*, not marketing.) Also: **RamSoft PowerServer** (referrer portal places orders + views results, **Medium-High**); **AbbaDox** (rule-based referrer self-scheduling, referrer-visible real-time exam status: Checked-in / No-Show / With Tech / Completed, **Medium-High**); **eRAD** markets "referrers can send electronic orders… with a single click" but this reads closer to document transmission than structured order entry — **UNRESOLVED**; **Sectra** portal with CPOE using ACR Appropriateness Criteria — **source dated 2011-10-19, currency must be re-verified before use**. View/status only, **not** order placement: Intelerad InteleConnect, Merative Merge, Nuance PowerShare, Ambra.

**Pitch consequence:** much of "referrer order intake" is a **vendor-selection question (candidate #3), not a build** — ask the shortlist to demonstrate structured referrer order entry and e-signature. The build opportunity is narrower and more defensible: the **fax/document path that remains**, and **incomplete-order chasing**.

**Incomplete orders — the best-evidenced problem in this section, with a hard caveat: no US outpatient rate exists.**
- **98.4% of outpatient imaging requests inadequate** by RI-RADS; only 1.6% grade A; complete clinical information in only **2.2%**; n=1,103 consecutive outpatient requests (US/MRI/CT/CR), Jan–Jun 2026, multicentre; orthopedics worst (OR 3.59), CT worse than MRI (OR 2.99); interobserver agreement only fair (Fleiss κ=0.376). (*Eur J Radiol* 2026;205:113217, PMID 42731498. **High** as peer-reviewed — but **SAUDI ARABIA**.)
- "**Incomplete Radiology Requests Are the Norm**" — 400 requisitions; 82% met a minimum threshold but only **67% stated the clinical purpose** and only **35% referenced prior imaging**; administrative fields completed more consistently than clinical fields. (*Cureus* 2025;17(12):e98353, PMID 41487743. **High** — **MOROCCO**.)
- The chasing step is automatable at scale: a BERT model on **131,683 requisitions** scored requisition quality with external test F1 **0.93**, κ 0.88. (*Eur Radiol* 2026;36(3):1616-1627, PMID 40836020. **High** — **TÜRKIYE**.)
- **🔴 NO EVIDENCE FOUND for a published incomplete-order or order-error rate in US outpatient radiology.** PubMed queries returned zero. **Any US figure must be labelled as extrapolated from non-US literature, or sourced from the client's own data.** (**High** on the gap)

**Order-to-protocol mapping** — real, with US data, but retrospective. Cleveland Clinic classified **94,501 abdominal CT studies over 4 years** into 11 protocol classes from free-text indication + ICD codes, best F1 **0.854**. (*J Digit Imaging* 2022;35(5):1120-1130, PMID 35654878. **High**) **Note: that is retrospective classification accuracy, not a deployed-workflow outcome**, and a review-level claim holds that automated protocol selection remains at "feasibility level" rather than routine deployment (**Medium**). Figures circulating for transformer protocol-selection accuracy (84–98%) and "protocoling occupies at least 6% of a radiologist's time" come from a ScienceDirect review that **returned HTTP 403 — UNVERIFIED, do not cite without reading the original.**

**Auth status callback to the referring office — a genuine white space, with a caveat that prevents overstating it.** No vendor was found productizing proactive prior-auth status notification back to the referring office; vendor auth-status tracking consistently flows to imaging-center staff and to the patient (**Medium-High**). **⚠️ But the payer already notifies the referrer, by fax.** Payer documentation confirms that on imaging-authorization approval "referring providers and rendering facilities are notified in writing by fax," and approval notifications go to beneficiary and referring provider; TRICARE/TriWest and Highmark expose referrer-visible auth status in portals; eviCore exposes status by web and phone. (**High**) **Correct framing: the opportunity is CONSOLIDATION AND PUSH, not first-ever visibility.** Referrers can get status today, but only pull-based, per-payer, fragmented across portals and inbound fax. **A pitch claiming referrers "fly blind" on auth status would be contradicted by payer documentation.**

**🟢 Report delivery and critical-results acknowledgment — the strongest defensible build in the referrer channel.**

The governing document is the **ACR Practice Parameter for Communication of Diagnostic Imaging Findings, Revised 2025 (Resolution 9)**, effective **2025-10-01** (chronology: 1991 → revised 1995, 1999, 2001, 2005, 2010, 2014, 2020 → amended 2021, 2023 → **Revised 2025**). Read in full. (**High**)

- Framing: "Quality patient care can only be achieved when study results are conveyed in a timely fashion," and notably "**Timely receipt of the report is more important than the method of delivery.**"
- **Reciprocal duty:** "There is a reciprocal duty of information exchange. **The referring physician or other relevant health care provider also shares in the responsibility for obtaining results of imaging studies ordered and acting on them.**" ← **Important for scoping liability; the center is not solely responsible.**
- **Three non-routine scenarios:** (i) findings suggesting **immediate or urgent intervention** (pneumothorax, pneumoperitoneum, significantly misplaced line or tube); (ii) findings **discrepant with a preceding interpretation** where failure to act may adversely affect health; (iii) findings the interpreting physician reasonably believes **significant and unexpected**, which may not need immediate attention but if not acted on may worsen over time and likely result in an adverse outcome.
- **Documentation:** "Interpreting physicians should document all nonroutine communications" — in the report, medical record, or department/personal log — "Inclusion of the **date and time, method of communication, and the name of the person to whom the communication was delivered** is an example of such documentation."
- **🟢 The clause to build on:** "**Electronic forms of communication are also an appropriate method to convey nonroutine communication as long as they provide documentation of receipt to demonstrate that the communication has been delivered and acknowledged.**"
- Preliminary-to-final discrepancies: a significant variation "should be reported in a manner that reasonably ensures receipt," with documentation of the discrepancy communication incorporated into the final report.
- **No numeric turnaround standard for routine reports anywhere in the parameter**, and the preamble explicitly disclaims establishing a legal standard of care (courts have split; it cites *Stanley v. McCarver*).

**The underlying ACR document requested:** Larson PA, Berland LL, Griffith B, Kahn CE Jr, Liebscher LA. "**Actionable findings and the role of IT support: report of the ACR Actionable Reporting Work Group.**" *JACR* 2014 Jun;11(6):552-8, PMID 24485759. Three categories of actionable findings requiring communication and clinical decision within **minutes (category 1), hours (category 2), or days (category 3)**; category 1 could lead to death or significant morbidity if not promptly recognized. The group explicitly **does not believe definitive lists are possible** but published illustrative lists. It recommends IT **document the communication and facilitate auditing**, that **vendors build locally customizable platforms**, and that systems be highly reliable and fit seamlessly into workflow. **Note it is 2014 — 12 years old**, and two published comments (*JACR* 2014;11(9):924-5 and 925-6) were not retrieved and may contain dissent. (**High** on content)

**Why this is the best build in the channel:** it converts "referrer communication" from a soft service claim into a **professional-standard obligation with a defined evidentiary artifact** — date, time, method, named recipient, and proof of delivery *and acknowledgment*. It is a **medico-legal risk-reduction** product, which is a language Fernando and Luis both speak; it is auditable; and **it does not depend on the failed TAT-volume premise.** The ACR Work Group even specifies the product requirements (document, audit, locally customizable, workflow-native).

**It also refines candidate #12** (currently "Buy (RIS/PACS) — Evidence: None found"). Routine report delivery is indeed standard RIS/PACS function. The **acknowledgment-tracked non-routine loop with escalation** is a distinct requirement, and whether a given small-center RIS satisfies it is a **vendor-evaluation question to add to candidate #3**. Intelerad InteleConnect does advertise critical-results acknowledgement — so ask the shortlist. (**High** on the requirement; **UNVERIFIED** whether small-center RIS products satisfy it.)

**Measured closed-loop outcomes:** the best artifact found is a UK ED QI project (two cycles, 50 patients each): follow-up CXR completion **32% → 70%** (p<0.001), closed-loop Critical Alert System inclusion **6% → 72%** (p<0.001), ED-initiated follow-up requests 42% → 86% (p=0.008), **no alert fatigue observed** (*Cureus* 2025;17(9):e92926, PMID 40988972. **High** on the study, **low transferability** — UK NHS ED, n=100). **NO EVIDENCE FOUND of a measured closed-loop critical-results outcome at a US freestanding outpatient imaging center.** (**High** on the gap)

**A useful adjacent finding on the radiologist-cost side:** at NYU Langone, **14,911 tickets** in six months, of which **11,401 (76.4%) were requests to "get the referring clinician on the phone"**; mean time to resolution **35.3 (±17.4) minutes**; 90% of radiologists reported being able to read a new study instead of waiting to communicate results; 87.5% reported reading more cases; **cost savings of up to $101.12 per ticket**. (*Clin Imaging* 2020;61:95-98, PMID 32004954. **High**) **This quantifies the communication burden in radiologist time and dollars — note it is radiologist cost, not referral volume, which is exactly the honest version of the argument.** It is also directly relevant to Luis as the reader.

**Referrer-facing analytics and scorecards — category is real, but NO independently measured outcome exists for any product in it.** **AbbaDox Referral Marketing CRM** is the most imaging-specific: measures referral volume by **completed and scheduled studies** (argued as more accurate than raw referral counts), marketing ROI, and **geographic market share by mapping referrer addresses around each center** (**VENDOR CLAIM, Medium**). **Nuance mPower Clinical Analytics** mines the PowerScribe reporting database and explicitly analyzes "ordering trends, scheduling patterns, and referring physician volumes" — report-derived, so it measures **realized volume**, not engagement (**VENDOR CLAIM, Medium**). **Inflo Health** claims "25X ROI" at an unnamed health system with undisclosed methodology — **DO NOT REUSE THAT FIGURE**. A physician-liaison/PRM CRM category exists (Tracking Works, TrackerPLUS, Tiller Hewitt, ReferralMD PRM, Redspot) tracking liaison visits, conversion rate by provider, territory maps (**Medium** category, individual claims unverified). **Analogic has NO referrer-analytics product — it is imaging hardware/OEM; this was an error in my research brief.** (**High**)

**🟢 The one genuinely useful framework, and it is NOT a vendor source.** Advisory Board, *Growing Imaging Referrals* (Imaging Performance Partnership, 2019, 36pp): segment referrers as **Loyalists (100–80% of revenue share), Splitters (80–20%), Dissenters (20–0.1%)** and prioritize outreach on **Splitters** — they already value the program and offer room for growth, and "splitters can become dissenters without support." (**High** that this is the published framework; **2019 vintage**.) **This is a defensible, non-vendor segmentation model for a referrer-scorecard section** — and it pairs naturally with the gold-card idea in §2.5, since the center's own data identifies which Splitters are near a 90% approval threshold.

#### Q3d. What a genuinely cutting-edge small center would do in 2027

Ranked by **evidence strength × feasibility for a 1–2 person shop**. Every item is grounded in something that exists; speculation is labelled.

**Tier 1 — strong evidence, high feasibility, nobody doing it at single-site scale:**
1. **DICOM-timestamp operational analytics with scanner-clock validation.** Peer-reviewed (Niffler, Emory, 715 scanners; JDI 2019 ultrasound with a documented >$10,000 saving), Tier-1 tags only, open-source tooling (Orthanc as a DICOMweb client as a sidecar). **Evidence High, feasibility High.** This is candidate #4, now properly evidenced.
2. **Pull and operationalize the public payer PA metrics** (§2.6) — per-payer approval, denial, appeal-overturn, extension rate, and the **published auth-required lists** — refreshed every March 31. **Evidence High (primary regulation), feasibility High, cost near zero.** Nobody has done this for El Paso.
3. **Closed-loop critical-results acknowledgment tracking** per ACR Revised 2025, capturing date, time, method, named recipient, and **proof of delivery and acknowledgment**, with escalation and audit. **Evidence High (primary standard), feasibility High.**
4. **Appeal-rate instrumentation as the owner's headline metric.** Already the deck's strongest idea; now reinforced by the 2026 AMA data (24% qualified-reviewer, 16% peer-to-peer) and by the post-service pre-payment risk in §2.10. **Evidence High, feasibility High.**

**Tier 2 — good evidence, moderate feasibility, genuinely differentiated:**
5. **Referrer gold-card instrumentation** (§2.5) — per-referrer, per-CPT approval tracking against the one-year, five-service, affiliate-aggregated threshold, surfaced to the referrer. **Evidence High on the statute; feasibility Medium; differentiation Highest in the brief.** Pair with the Advisory Board Splitter segmentation.
6. **RDSR routing configured at commissioning + ACR Dose Index Registry participation**, satisfying the Joint Commission dose-benchmark obligation while yielding dose analytics. **Evidence High, feasibility Medium** (requires scanner configuration at install — a one-time window that does not reopen).
7. **A Phase-1 DICOM metadata audit as a billable deliverable** — QIDO-RS or Orthanc against the candidate archive to measure actual population rates for Tier-2 tags and MPPS presence per scanner. **This converts the brief's two biggest DICOM unknowns into paid findings, and it fits the $12k Phase 1 / 90-day-gate structure.** **Evidence High, feasibility High.**
8. **Confidence-threshold + exception-queue architecture with documented pre-deployment validation**, per the published patterns in Q3b, with sampling QA that still produces evidence of review. **Evidence Medium-High, feasibility Medium.**

**Tier 3 — real but speculative or dependent on others:**
9. **Azure Change Feed + DICOMcast as the DICOM→FHIR operational spine.** Production-available components, but **no published small-center case study exists** — this is "a defensible architecture built from production-real parts," **not a proven small-center pattern.** Say it that way. **Evidence Medium, feasibility Medium. SPECULATIVE as a pattern.**
10. **FHIRcast context sync.** Spec real (STU2), radiology-canonical, RSNA demos with >20 vendors — but **no named production deployments found.** Name it as a roadmap capability, not a 2027 requirement. **SPECULATIVE.**
11. **Payer FHIR PA API consumption at go-live.** The regulation is firm; the per-payer onboarding cost and RBM reachability are not. **Design for it, do not promise a date. SPECULATIVE on timing.**
12. **Post-service pre-payment appeal capability for routine modalities** (§2.10). The threat is verified as an offering; its deployment in El Paso's payer mix is unknown. **Monitor and design for; do not size. SPECULATIVE on incidence.**

**Explicitly NOT on this list:** anything touching the image clinically (candidate #13 stands, declined); patient-facing voice (candidate #9 stands, buy not build — and TRAIGA now adds a disclosure obligation); and any claim that TAT improvements will raise referral volume.

#### Q3e. Economics and labor benchmarks

**🔴 VERDICT: imaging-specific administrative staffing benchmarks are effectively NOT PUBLICLY AVAILABLE at usable granularity. Do not approximate them.**

**The only radiology-specific FTE figure found, with a disqualifying caveat:** radiology median **1.52 total support staff per FTE physician**, vs 4.43 (physician-owned nonsurgical single-specialty) and 2.50 (hospital/IDS-owned). **⚠️ BASED ON ONLY 11 RADIOLOGY PRACTICES**, attributed to an MGMA cost survey via Radiology Business (direct fetch **HTTP 403**; figure from search extract, **not read in original**). (**Low-Medium**) **This must not anchor a staffing model:** n=11, mixed private/hospital settings, undated edition, unverified source, and it uses a radiology-hostile denominator — an imaging center's admin load scales with **study volume and payer mix**, not radiologist headcount.

**Paywall audit, so Rick knows exactly what is purchasable and at what price:**

| Source | Imaging-specific? | Access | Price |
|---|---|---|---|
| **MGMA DataDive** (Cost & Revenue / Financials & Operations) | Specialty cuts exist but **radiology n is tiny** | Paid + membership | Membership from **$399/yr individual**; **dataset pricing NOT public — quote required**. 2026 edition merges Cost & Revenue with Practice Operations, July 2026 |
| **RBMA Accounts Receivable Survey** | **YES — radiology-specific** | Purchasable; free to practices that submitted data | **Price not displayed**; most recent edition **2024** (prior 2023/2021/2018/2017) |
| **RBMA Radiology Administrative Compensation Survey** | Yes | Purchasable | **2022: member $325 / non-member $450**; 2023 member $125 |
| **RBMA DataMAXX** benchmarking | Yes | Paid tier | Contributing **$500/yr premium**; non-contributing **$500 basic / $1,000 premium** (via a **2014** source — likely stale) |
| **HFMA MAP Keys** | **NO — no imaging/radiology keys exist** | Definitions public; **values restricted** to MAP App / MAP Award applicants | Not disclosed |
| **ACR practice management** | — | **No published admin staffing benchmark found** | — |
| **2025 DataSpring (CAQH) Index** | **No radiology breakout** | Registration required | **Index Pro $899/user**; per-transaction table rendered as charts, not extractable |

(**High** on the paywall characterization — RBMA prices and the HFMA key list were read directly.)

**⚠️ FALSE-POSITIVE WARNING:** HFMA MAP Keys cost-to-collect (FM-6) includes "imaging" under HIM expenses — that means **document scanning/imaging, NOT radiology.** Do not mistake it for a radiology benchmark. (**High**)

**Prior-auth transaction costs** — see Q1c for the figures read directly from the official 2024 CAQH PDF (**provider cost: manual $12.88 / partial $8.93 / electronic $5.38**) and the resolution of the conflicting secondary figures. **🔴 CAQH has NO radiology or imaging breakout** — I had the specialty brief read in full: **zero mentions of radiology or imaging**, segmenting only generalists / specialists / behavioralists. (**High**) Closest usable proxy, read directly: **prior authorization, specialists — manual $15.99, partial $9.05, electronic $6.61** (generalists $11.00/$6.94/$4.47); switching fully manual → electronic saves **specialists $8.51** per transaction, and the specialist-vs-generalist gap exceeds $7, one of the largest unit-cost differences in the brief. **Label "specialists" as a proxy for imaging, never as an imaging figure, and label CAQH as industry self-report.**

**Days in A/R for radiology — one credible figure, paywalled.** **Median ~31 days**, from the **2023 RBMA Accounts Receivable Survey (2022 data)**, reported via Radiology Business (direct fetch **HTTP 403**; **not read in original**; full survey is a paid RBMA product). (**Medium**) **This is the single most defensible radiology A/R benchmark located — and it is behind a paywall.** Historical peer-reviewed anchor: 2004 mean days charges in A/R **56.11** (professional component) / 55.54 (global), median adjusted collection percentage deteriorating 87.3% → 85.1%, and global-fee practices billing in house achieving mean ACP **91.2%** vs **79.4%** using a billing service (*JACR* 2005;2(12):1019-29, PMID 17411986) — ⚠️ **RBMA members only, response rates 15% and 9%**, severe non-response bias, and **21 years old. High** on the publication, **Low** on 2026 applicability.

**🔴 Denial rate, clean claim rate, cost to collect — NO CREDIBLE IMAGING BENCHMARK FOUND.** Every "2026 radiology benchmark" located is a **billing-vendor marketing blog**, and they contradict each other irreconcilably: denial rate "5–10%" vs "below 5%" vs "15.6%" vs "15–22%" (**a 3–4x spread — unusable**); clean claim rate "92.4% median" vs "97%+" vs "95%+"; days in A/R "30–40" vs "36.8" vs "24–32"; cost to collect "5–10% in-house / 3–7% outsourced" vs "3.2¢ best-in-class / 5.4¢ average"; net collection rate "86.1%" vs "should be 96%+". The most-cited of these traces to **one RCM vendor's own active client base** (~500 rendering providers, 22 specialty cohorts, KPI definitions following HFMA MAP Keys). (**High** on the methodology description) **That is one vendor's book of business, not an industry benchmark** — client selection is endogenous, since practices that hire an RCM vendor differ systematically. **Cite it as "one RCM vendor's client-base median" or not at all.**

**Total administrative cost per imaging study: NO EVIDENCE FOUND.** No published figure exists in any free public source (a PubMed query returned 116 results, none addressing per-study administrative cost for outpatient imaging). The nearest constructible proxy is summing CAQH per-transaction provider costs across the transactions one study triggers (eligibility + prior auth + claim submission + claim status + payment). **⚠️ If the pitch does this it must be labelled a BUILT ESTIMATE, not a published benchmark**, and must disclose: CAQH is self-report; figures are "specialist" or all-industry, not imaging; transaction counts per study are assumed; and it **omits scheduling, protocoling, order chasing, report distribution, and denial rework entirely.** (**High** that no published figure exists)

**What this means for the pitch:** the honest position is that **the benchmark literature for imaging administration does not exist at the granularity an owner would want — which is itself an argument for instrumenting the center's own numbers from day one.** That is candidate #4, and this gap is the reason it matters.

---

## 4. Evidence gaps — what could NOT be answered, and why

### Regulation (Q1)
1. **Per-payer onboarding burden is unquantified for every payer.** No developer portal could be read directly (Aetna's returned a JS shell). Time, agreements, and whether a one-site provider is an accepted registrant: **UNVERIFIED. The largest cost unknown in candidate #1.**
2. **🔴 Whether imaging authorization delegated to an RBM is reachable through the payer's FHIR PA API: UNVERIFIED.** The most important open technical question in the build.
3. **No independently audited measured outcome from any payer FHIR PA API.** Best available is partner self-report with a **Q4-2023** window and no stated pilot-vs-production status.
4. **The absence of a delay to the 2027 dates rests on negative search**, not a primary source.
5. **The 2025 CAQH/DataSpring per-transaction table could not be read** (registration-gated, charts not text). The 2024 table was read directly and is the one to cite.
6. **Texas-specific prior-auth decision deadlines** potentially shorter than the federal 72-hour expedited timeframe: **NOT VERIFIED.** The rule defers to shorter state minimums, so this is a real open item.
7. **Whether Texas QHPs are "on the FFEs"** for this rule is inferred from Texas's use of the federally-facilitated exchange, not confirmed by a CMS determination.
8. **TRAIGA's §552.051(b)/(f) cross-reference ambiguity** (§2.11) — whether the disclosure duty binds a private provider is a construction question needing a Texas health-lawyer read.
9. **Texas SB 1188's "review of AI-created records" scope: UNVERIFIED** (secondary sources only).

### DICOM (Q2)
10. **Extra-cost API gating for every named PACS vendor.** No vendor publishes API pricing; requires direct quotes.
11. **Intelerad/InteleShare, Change Healthcare/Optum, Konica Exa, Novarad, PaxeraHealth, Hyland Acuo, Merative DICOMweb support: UNVERIFIED.** These may well support it; it simply cannot be evidenced from public documents.
12. **Whether Sectra/Fujifilm/Visage DICOMweb is base-license or a paid module** — conformance statements document *capability*, never *commercial packaging*.
13. **No litigation and no published per-study/per-GB PACS API fee exists** (absence from the public record, not proof of absence in private contracts). **No modern small-center migration cost benchmark** — best figures are 2007 and hospital-scale. **Recommend asserting no number.**
14. **Site-specific population rates for Operators' Name, Protocol Name, Body Part Examined, and MPPS presence per scanner.** The literature establishes these are unreliable *in general*; only scanning the actual archive gives real rates. **This should be a Phase 1 deliverable, not a pitch assertion.**
15. **Whether any specific PACS exposes MPPS/timestamps through its API** rather than merely storing them. Capability-to-access is the real commercial question and is undocumented publicly.
16. **AWS HealthImaging native C-STORE/DIMSE support: UNVERIFIED** — likely needs a DICOM router in front of modalities.
17. **Real cloud cost for this center** — unit prices verified, but totals depend on volume, instance counts (Azure charges per instance), retention and tiering. **Per-GB rates alone will mislead.**
18. **FHIRcast production deployments at small centers: NONE FOUND.**
19. **No published case study of a unified DICOM+FHIR operational layer at a small outpatient center.** The Erlangen pipeline is a large academic hospital doing research integration.
20. **Per-vendor IHE profile claims** — the verification *mechanism* is confirmed and documented (§Q2e), but per-vendor lookups were not executed (Gazelle Product Registry returned HTTP 503). **Running steps 1–3 on the shortlist is a fast, high-leverage next action.** Connectathon SEAL criteria also unverified.
21. **Full text of the JDI 2019 ultrasound paper** (abstract truncates at the savings figure) and the *Physica Medica* review (HTTP 403) — paywalled; claims rest on detailed abstracts.

### Agents, HITL, referrer channel (Q3)
22. **🔴 No vendor in the entire set has a named single-site outpatient imaging center reference customer.** Not one surfaced.
23. **No independently audited or peer-reviewed outcome study for agentic administrative automation anywhere.** Specifically, no peer-reviewed JACR publication of the CodaMetrix/OHSU radiology results exists; the Alpha Nodus 25% figure has no pilot cited.
24. **Pricing is unobtainable without a sales conversation** for Cohere, Rhyme, Humata/R1, Anterior, Latent, Adonis, SmarterDx, Notable, Hyro, Artera, Tennr, Abridge, Ambience, CodaMetrix, Alpha Nodus, Parlance, Syllable, Infinitus, Availity Essentials Pro. Every figure reported for Luma (~$250/user/mo), Notable ($5–15K/mo), Abridge ($200–800/provider/mo), Assort ($1,500/mo, $75K min), Candid (3%) and Honey (~$1.50–2/PA) is **third-party reported, not a vendor rate card — indicative only.**
25. **The authoritative CMS WISeR service list could not be obtained** (sources conflict: 13 categories vs 17 services). **The conclusion that imaging is out of WISeR scope is provisional, based on absence of mention.**
26. **Enrolled bill text for all state AI statutes except California, Texas HB 3459, Texas HB 3812 and Texas HB 149** (which I read directly). **Indiana HB 1271's provider-side obligation is the one most worth verifying against primary text**, because it is the only one that would bind the center outside Texas.
27. **Whether Humata's independent-provider motion survives the R1 acquisition**, and **whether Waystar's agentic tier is available at small-practice scale: UNVERIFIABLE from public sources.** Thoughtful AI's sunset rests on a single trade source.
28. **No state AG action on healthcare administrative AI found** — cannot prove a negative.
29. **🔴 No evidence that TAT or referrer communication changes referral VOLUME** — the single most important gap; **it does not exist in the published literature** (§2.9).
30. **No US outpatient radiology order-incompleteness rate.** Strong evidence is Saudi, Moroccan, Turkish.
31. **No imaging-specific admin staffing, denial rate, clean claim rate, cost-to-collect, or total-admin-cost-per-study benchmark** publicly available (§Q3e). Credible candidates are all paywalled; HFMA has no imaging keys at all.
32. **No measured closed-loop critical-results outcome at a US outpatient imaging center** — best evidence is a UK ED project, n=100.
33. **No independently measured outcome for any referrer analytics/scorecard product**, across the entire category.
34. **eRAD's "send electronic orders"** — structured RIS order entry or document transmission? **UNRESOLVED** (page truncated). **Sectra's CPOE with ACR Appropriateness Criteria** — only source is **2011**; must be re-verified.
35. **The Radiology Business article on payer post-service AI returned HTTP 403 twice.** The Avalon product page was verified directly instead, which is a better source — but the "denials coded as provider liability" characterization remains **UNVERIFIED against the original**, and Avalon's page does not state who bears a denied claim's cost.
36. **ACR Actionable Reporting Work Group published comments** (*JACR* 2014;11(9):924-5, 925-6) not retrieved; may contain dissent.
37. **The "71% of referring physicians send patients to multiple facilities" claim** (AJR, HTTP 403) — **UNVERIFIED, do not use.**

### Errors found in my own research brief, corrected
- **Analogic** has no referrer-analytics product (imaging hardware/OEM).
- **Orby AI** is not a healthcare vendor (general enterprise RPA, acquired by Uniphore).
- **Medicom Health** is hospital-marketing health risk assessments, divested 2021 — not order intake.
- **Tennr's** radiology positioning is trade-press framing its own materials do not support.
- **(0018,1152)** is Exposure (mAs), not CTDIvol — CTDIvol is **(0018,9345)**.
- **PS3.20** is CDA imaging reports, not the FHIR mapping.
- **MAWF** is retired; **REM** was omitted and should be named.
- **"NPSG.02.03.01"** is the Laboratory identifier; Ambulatory Health Care has no critical-results goal.

---

## 5. What to ASK Luis and Fernando

Ordered by how much the answer changes the build.

**Payer mix and authorization (closes gaps 1, 2, 6, and unlocks §2.6)**
1. **Which plans will actually dominate the book** — named: Medicare Advantage plans, Texas Medicaid MCOs, FFE marketplace issuers, commercial fully-insured, and **self-funded ERISA**, with the expected split? Everything in Q1 turns on how much of the mix is inside CMS-0057-F. Self-funded ERISA volume is pure manual/EDI exposure.
2. **🔴 Which radiology benefit managers do those plans delegate imaging authorization to** — eviCore, Carelon, Evolent/RadMD, Optum, or in-house? *The question I most want answered.* It determines whether the 2027 FHIR APIs touch the imaging workflow at all.
3. **From Fernando's Southwest X-Ray experience: what share of advanced imaging actually required authorization, what was denied, and what was appealed?** The deck carries no imaging-specific authorization or denial rate because **none is published**. His own operating history is the only credible source available.
4. Will they be **in-network on day one** with the major plans, or opening partly out-of-network while credentialing? Determines whether the Provider Access API is usable at opening.
5. **Have they seen post-service, pre-payment claim review on routine studies** (X-ray, ultrasound, non-cardiac nuclear medicine) from any payer? (§2.10) Fernando would recognize it if it is happening in this market.

**Vendor selection — time-sensitive, leverage expires at signature (closes gaps 10–15, 20)**
6. **What is the RIS/PACS shortlist, and how far along is the selection?** Candidate #3 is free only before signature and is the highest-ROI item in the deck.
7. Will they require of each shortlisted vendor: a **published IHE Integration Statement for the exact product AND version**, naming **SWF.b including MPPS actors and transactions**, plus **REM, IOCM, PDI**; a **DICOM Conformance Statement naming QIDO-RS/WADO-RS/STOW-RS per PS3.18 at no incremental license cost**; **structured referrer order entry and e-signature demonstrated**; **critical-results acknowledgment tracking demonstrated**; and **documented, fee-transparent export and migration terms** — all **demonstrated against the center's own test cases before signature**? (Declaration is vendor self-certified; only demonstration is proof.)
8. **🔴 Will the scanners be configured to emit RDSR at commissioning**, and will they participate in the ACR Dose Index Registry? **If RDSR routing is not set up at install, the dose data does not exist retroactively** — and DIR satisfies a Joint Commission dose-benchmark obligation they will have anyway.
9. **Who owns the scanner clocks, and will NTP sync be verified and monitored?** Sounds trivial, is not: the Emory work found five misconfigured clocks, and every duration and utilization number depends on it.
10. **Will technologists be individually identified in the scanner's Operators' Name field, or is it a shared login?** Determines whether any per-technologist metric is possible at all.

**Operations and the owner report (specifies candidate #4)**
11. **Which modalities, how many of each, and what hours of operation?** Utilization analytics is only meaningful against intended capacity.
12. **Fernando: what do you want on one page every Monday morning?** That answer *is* the specification for candidate #4 — still the single highest-leverage question of the evening.
13. **Luis: what turnaround time will you commit to, and who else will read?** Reader reconciliation needs the roster and the commitment.
14. **What are their own numbers for days in A/R, denial rate, and clean claim rate — and what did Southwest X-Ray run at?** No credible public imaging benchmark exists for any of these (§Q3e). His numbers would replace a vendor-blog range.
15. **What is the billing/RCM arrangement** — in-house, outsourced, or the RIS vendor — and will the center have direct access to 270/271 eligibility and claim/denial data? Candidates #1, #2 and #4 all depend on it.

**Referrers (closes gap 29, and tests the one surviving referrer idea)**
16. **Who are the expected top referrers, how many, and what is the expected concentration** — 20 practices or 200?
17. **How will orders arrive — fax, phone, RIS referrer portal, EHR interface, or Direct messaging — and from which referrer EHRs?** Order-intake scope is undefined without this, and much of it may be a vendor-selection answer rather than a build.
18. **🔴 Fernando: at Southwest X-Ray, did you ever observe referral volume move because of report turnaround or communication quality?** **I cannot substantiate that link from the published literature — the strongest study says cost and copay dominate.** His direct observation is worth more than another survey. **If he says no, that pitch section should shrink rather than be argued.**
19. **🟢 Would their referrers value help earning Texas gold-card exemptions?** The center holds the per-referrer, per-CPT approval data needed, the threshold is now a one-year window with affiliate aggregation, and the exemption is automatic. **The most differentiated referrer idea in the brief — test it on them before building it.**
20. **How will they position on price?** The conjoint evidence says cost dominates referrer and patient site selection. This is uncomfortable and it is the finding most likely to be raised by a former imaging-company founder.

**Scope**
21. **How many centers, and over what period?** (Already a logged open item; it changes the specification-reuse argument, not the build case.)
22. **Will any entity bill into states other than Texas** — specifically Indiana? (Gap 26: Indiana HB 1271 is the one statute found that imposes a provider-side human-review duty on AI-prepared claims.)

---

## 6. Citations

Retrieval date 2026-10-10 unless noted. Access notes affecting confidence are at the end.

**Federal regulation (primary, read directly)**
1. **CMS-0057-F**, "Advancing Interoperability and Improving Prior Authorization Processes...", **89 FR 8758**, published 2024-02-08, effective 2024-04-08, FR doc 2024-00895. Full text (pp. 8758–8988) downloaded and searched: https://www.federalregister.gov/documents/full_text/text/2024/02/08/2024-00895.txt · metadata https://www.federalregister.gov/api/v1/documents/2024-00895.json
2. **CMS-0062-P**, "Interoperability Standards and Prior Authorization for Drugs...", **91 FR 19890**, **PROPOSED**, published 2026-04-14, comments closed 2026-06-15. Full text downloaded: https://www.federalregister.gov/documents/full_text/text/2026/04/14/2026-07205.txt · docket https://www.regulations.gov/document/CMS-2026-1255-0001
3. CMS Fact Sheet, CMS-0057-F: https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f
4. HHS/CMS **Statement of Enforcement Discretion for Referral Certification and Authorization Transaction**, 2024-06-13: https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/frequently-asked-questions/hipaa-transaction-enforcement-discretion · https://www.cms.gov/files/document/statement-enforcement-discretion-referral-certification.pdf
5. HTI-1 final rule, 89 FR 1192 (2024-01-09); HTI-4 final rule, 90 FR 37130 — both as cited within the rules above.

**Texas statutes (primary, enrolled text read directly)**
6. **Texas HB 3459** (87R), enrolled — Insurance Code ch. 4201 Subchapter N, gold-carding; effective **2021-09-01**: https://capitol.texas.gov/tlodocs/87R/billtext/html/HB03459F.htm
7. **Texas HB 3812** (89R), enrolled — amends §§4201.152, 4201.651, 4201.653, 4201.655; effective **2025-09-01**: https://capitol.texas.gov/tlodocs/89R/billtext/html/HB03812F.htm
8. **Texas HB 149 (TRAIGA)** (89R), enrolled — Business & Commerce Code ch. 552, §552.051 disclosure; effective **2026-01-01**: https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00149F.htm
9. Texas SB 815 (UR automated decision systems, 2025-09-01) and SB 1188 (US data residency; AI record review, 2026-01-01) — secondary sourcing only; **scope UNVERIFIED**.

**Standards and implementation guides**
10. HL7 FHIR **Da Vinci PAS IG, STU 2.1.0**, generated 2024-12-20: https://hl7.org/fhir/us/davinci-pas/STU2.1/ · **DTR IG v2.2.0**: https://hl7.org/fhir/us/davinci-dtr/2.2.0/en/
11. **DICOM PS3.6 ch.6 Data Dictionary** (tags verified programmatically): https://dicom.nema.org/medical/dicom/current/output/chtml/part06/chapter_6.html · **PS3.18** Studies Service ch.10 and Worklist/UPS-RS ch.11: https://dicom.nema.org/medical/dicom/current/output/html/part18.html · **PS3.20** (CDA imaging reports, *not* the FHIR mapping): https://dicom.nema.org/medical/dicom/current/output/html/part20.html · DICOMweb RESTful structure: https://www.dicomstandard.org/using/dicomweb/restful-structure
12. **FHIR R4 ImagingStudy** (authoritative DICOM↔FHIR mapping; **Maturity 3 / Trial Use**): http://hl7.org/fhir/R4/imagingstudy.html
13. **IHE General Introduction Appendix F — Integration Statements** (source of the "vendors are solely responsible" / "have not evaluated or approved" disclaimers): https://profiles.ihe.net/GeneralIntro/ch-F.html · IHE Wiki Integration Statement + Registry: https://wiki.ihe.net/index.php/Integration_Statement · https://www.ihe.net/testing/ihe_product_registry/
14. **IHE Connectathon Results** (independently tested; 89 editions, 899 companies, 207 profiles): https://connectathon-results.ihe.net/ · **IHE Product Registry** (vendor self-declared): https://product-registry.ihe.net · Gazelle manual: https://connectathon.ihe-catalyst.net/gazelle-documentation/Product-Registry/user.html
15. **IHE Radiology Technical Framework** index and profiles: https://profiles.ihe.net/RAD/index.html · RAD TF Vol 1 Rev 22.0 (2024-06-25, records MAWF retirement): https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Rev22-0_Vol1_FT_2024-06-25.pdf · SWF.b supplement: https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_SWF.b_Rev1-7_2019-08-09.pdf · IOCM: http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_IOCM_Extension_Rev1.4_TI_2015-04-21.pdf
16. **IHE PCC 360X** closed-loop referral supplement: https://www.ihe.net/uploadedFiles/Documents/PCC/IHE_PCC_Suppl_360X.pdf
17. **FHIRcast** (STU2) — radiology use case present, no named deployments found: https://fhircast.org/
18. **TEFCA SOP: Exchange Purposes v5.1**, effective 2026-07-01 — read directly; **zero occurrences of "order"**: https://rce.sequoiaproject.org/wp-content/uploads/2026/07/Exchange-Purposes-SOP-v5.1_7.1.2026_508.pdf

**Professional standards, registries, accreditation (primary PDFs text-extracted locally)**
19. **ACR Practice Parameter for Communication of Diagnostic Imaging Findings, Revised 2025 (Resolution 9)**, effective 2025-10-01: https://gravitas.acr.org/PPTS/DownloadPreviewDocument?DocId=74 · portal https://gravitas.acr.org/PPTS
20. **ACR–SIIM Practice Parameter for Imaging AI** (2026): https://www.acr.org/News-and-Publications/Media-Center/2026/first-practice-parameter-for-imaging-ai · PDF https://gravitas.acr.org/PPTS/DownloadPreviewDocument?DocId=217 · JACR AI accreditation road map: https://www.jacr.org/article/S1546-1440(25)00112-7/fulltext
21. **ACR Dose Index Registry** startup guide (RDSR as sole transfer means; ACR Connect / DIR Link): https://nrdrsupport.acr.org/support/solutions/articles/11000101826-dose-index-registry-dir-start-up-guide · features https://nrdrsupport.acr.org/support/solutions/articles/11000028993-dose-index-registry-dir-features · overview https://cs.acr.org/Practice-Management-Quality-Informatics/Registries/Dose-Index-Registry · ACR QCDR https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Registries/Qualified-Clinical-Data
22. **Joint Commission National Performance Goals, Hospital, effective Jan 2026** (NPG.01.02.01): https://digitalassets.jointcommission.org/api/public/content/9ca80055182b4274842a5780a94f2c82 · **Ambulatory Health Care NPSGs 2026** (no critical-results goal): https://digitalassets.jointcommission.org/api/public/content/92c95c4e94304b2084e7e039d916719b?v=3c64fe83 · **Laboratory NPSGs 2026** (retains NPSG.02.03.01): https://digitalassets.jointcommission.org/api/public/content/3c7a110c215943bc80d9ce87e9d9ee9d?v=aef80e14
23. **AMA** prior-auth AI policy D-480.956: https://www.ama-assn.org/press-center/ama-press-releases/ama-adopts-policy-calling-more-oversight-ai-prior-authorization · AI principles PDF: https://www.ama-assn.org/system/files/ama-ai-principles.pdf · **AMA survey press release 2026-05-13**: https://www.ama-assn.org/press-center/ama-press-releases/ama-survey-prior-authorization-reform-pledge-falls-short-physicians
24. **AHIMA** AI attestation: https://journal.ahima.org/page/ai-attestation-an-issue-worth-discussing-in-coding · AHIMA/ACDIS 2026 query guidelines: https://journal.ahima.org/page/guidelines-for-achieving-a-compliant-query-practice-whats-new-in-the-2026-update
25. **RBMA** 2026 SYNC AI/contracting agenda: https://www.nelsonmullins.com/insights/events/radiology-business-management-association-s-rbma-2026-sync-annual-meeting · ACR/RBMA RBM best practices: https://radiologybusiness.com/topics/healthcare-management/medical-practice-management/acr-rbma-issue-best-practices-radiology-benefit-managers · RBMA A/R survey: https://www.rbma.org/ar
26. **HFMA** autonomous coding: https://www.hfma.org/revenue-cycle/building-confidence-in-the-transition-to-autonomous-coding/
27. **HHS OIG** AI governance audit: https://oig.hhs.gov/reports/work-plan/browse-work-plan-projects/audit-of-hhs-governance-of-artificial-intelligence/ · Spring 2026 SAR: https://oig.hhs.gov/documents/sar/11794/Spring_2026_SAR.pdf · Forvis Mazars OIG Q3 2026: https://www.forvismazars.us/forsights/2026/10/oig-work-plan-updates-compliance-implications-q3-2026

**Peer-reviewed literature**
28. **Kathiravelu P, et al.** "A DICOM Framework for Machine Learning and Processing Pipelines Against Real-time Radiology Images." *J Digit Imaging* 2021;34(4):1005-1013. **PMID 34405297**, PMC8455728. *(Niffler; 715 scanners at Emory; MRI operational efficiency, exam timeframes and idling times; more accurate than the clinical data warehouse; five scanners found with misconfigured clocks.)*
29. **"Use of Image-Based Analytics for Ultrasound Practice Management and Efficiency Improvement."** *J Digit Imaging* 2019. **PMID 30623273**. *(Exam length, room utilization, exams per operational hour, per-sonographer; >$10,000 saved in avoided probe replacement; required OCR and private tags.)*
30. **Little K, et al.** "AAPM Task Group Report 305: Guidance for standardization of vendor-neutral reject analysis in radiography." *J Appl Clin Med Phys* 2023;24(5):e13938. **PMID 36995917**, PMC10161059.
31. **Stephenson-Smith B, Neep MJ, Rowntree P.** "Digital radiography reject analysis of examinations with multiple rejects." *J Med Radiat Sci* 2021;68(3):245-252. **PMID 33826800**, PMC8424327. *(Australian ED — not a US outpatient benchmark.)*
32. **Noumeir R.** "Benefits of the DICOM modality performed procedure step." *J Digit Imaging* 2005;18(4). **PMID 15988627**.
33. Automated dose-monitoring software systematic review (49 studies; "requires skilled users, standardised protocol naming, and regular data verification"). *Physica Medica* 2025. **PMID 40694887**. *(Full text HTTP 403; abstract only.)*
34. **AAPM TG357 / EFOMP** joint report on fluoroscopy skin dose (RDSR importance). *Med Phys* 2021. **PMID 33930183**.
35. OpenREM + openSkin skin-dose investigation QI (**94% staff-time reduction**). *BMJ Open Qual* 2020. **PMID 31986118**. · Digital breast tomosynthesis LDRLs via OpenREM. *J Med Radiat Sci* 2025. **PMID 40561378**.
36. "Determining scanned body part from DICOM study description for relevant prior study matching." *Stud Health Technol Inform* 2013. **PMID 23920517**. · "Standardizing DICOM annotation: deep learning enhances body part description in X-ray image retrieval" (**116 header values → 36 SNOMED CT codes**). *BMC Med Imaging* 2025. **PMID 41390620**. · "Metadata Quality in Imaging Trials: A Knowledge Graph-Based Approach." *Stud Health Technol Inform* 2025. **PMID 40380518**.
37. "Large-Scale Integration of DICOM Metadata into HL7-FHIR for Medical Research" (Erlangen; ImagingStudy pipeline). *Methods Inf Med* 2024. **PMID 40233823**, PMC12133321.
38. "Radiology Reimagined: Interoperability and Lessons Learned from the Imaging AI in Practice Demonstration" (RSNA; >20 vendors; FHIRcast 2024). *Radiology* 2026. **PMID 42301015**. · "Integrating and Adopting AI in the Radiology Workflow: A Primer for Standards and IHE Profiles" (IRA profile). *Radiology*: https://pubs.rsna.org/doi/full/10.1148/radiol.232653
39. **🔴 Yuan C, Huang H, Dirschl D, Chintagunta P, Paushter D.** "Characterization and Targeting of the Main Drivers of Elective Imaging Utilization: A Cross-Sectional Study Applying Conjoint Analysis." *JACR* 2025;22(5):521-529. **PMID 39828000**. *(393 patients + 168 physicians; cost/copay dominates; TAT not a tested attribute.)*
40. UCSF referring-clinician satisfaction across 11 domains (results/reporting **OR 4.71**; n=729/2,720). *Clin Imaging* 2023;97:72-77. **PMID 36907042**.
41. TAT deterioration: **+113% 2014–2023**, 2.6M studies. *JACR* 2026;23(7):1244-1252. **PMID 41914942**. · **+27% in 2024, +177% 2014–2024**, 2.9M studies. *JACR* 2026 Aug 4. **PMID 42550124**. · Neiman HPI release 2026-08-04: https://www.neimanhpi.org/press-releases/imaging-interpretation-turnaround-time-continued-to-increase-in-2024-by-27/
42. **Larson PA, Berland LL, Griffith B, Kahn CE Jr, Liebscher LA.** "Actionable findings and the role of IT support: report of the ACR Actionable Reporting Work Group." *JACR* 2014;11(6):552-8. **PMID 24485759**.
43. **Moore W, et al.** "Enhancing communication in radiology using a hybrid computer-human based system" (NYU; 14,911 tickets, **76.4%** "get the referring clinician on the phone," 35.3 min mean TTR, **up to $101.12/ticket** saved). *Clin Imaging* 2020;61:95-98. **PMID 32004954**.
44. Closed-loop critical-alert QI (CXR follow-up 32%→70%; alert inclusion 6%→72%). *Cureus* 2025;17(9):e92926. **PMID 40988972**. *(UK ED, n=100.)*
45. Order-incompleteness: RI-RADS, **98.4% inadequate**, n=1,103, Saudi Arabia. *Eur J Radiol* 2026;205:113217. **PMID 42731498**. · "Incomplete Radiology Requests Are the Norm," n=400, Morocco. *Cureus* 2025;17(12):e98353. **PMID 41487743**. · BERT requisition-quality scoring, n=131,683, Türkiye. *Eur Radiol* 2026;36(3):1616-1627. **PMID 40836020**.
46. Order-to-protocol mapping, **94,501 abdominal CT studies**, best F1 0.854. *J Digit Imaging* 2022;35(5):1120-1130. **PMID 35654878**.
47. RBMA A/R historical anchor (2004 days in A/R 56.11; response rates 15%/9%). *JACR* 2005;2(12):1019-29. **PMID 17411986**.

**Cloud and vendor technical documentation (authoritative on what is offered, not on performance)**
48. Microsoft Azure Health Data Services **DICOM service** overview (page dated 2025-07-23) — DICOMweb Studies Service, UPS-RS Worklist, extended query tags, **Change Feed**, **DICOMcast**: https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicom-services-overview · conformance statement v2: https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicom-services-conformance-statement-v2 · pricing via the **Azure Retail Prices API** (web page renders `$-` via JS)
49. **AWS HealthImaging** pricing: https://aws.amazon.com/healthimaging/pricing/ · developer guide: https://docs.aws.amazon.com/healthimaging/latest/devguide/what-is.html
50. **Google Cloud Healthcare API** pricing (DICOM structured + blob storage; export batch/streaming; transcode): https://cloud.google.com/healthcare-api/pricing
51. **Orthanc** DICOMweb plugin: https://orthanc.uclouvain.be/book/plugins/dicomweb.html · **dcm4chee-arc-light**: https://web.dcm4che.org/dcm4chee-arc-light · RESTful services: https://github.com/dcm4che/dcm4chee-arc-light/wiki/RESTful-Services · **OHIF** DICOMweb data source: https://docs.ohif.org/configuration/datasources/dicom-web/
52. PACS/RIS conformance statements: **Sectra** 28.1 (2026-03): https://medical.sectra.com/wp-content/uploads/sites/3/2026/03/dicom.conformancestatement.sectrapacs-28.1.0.10183.pdf · **Fujifilm Synapse** (STOW-RS from 5.3.000): https://healthcaresolutions-us.fujifilm.com/wp-content/uploads/2023/02/DICOM_Conformance_Statement_v5-2_above.pdf · **Visage 7** (v12.00, 2026-06-18): https://www.visageimaging.com/downloads/Visage7/Visage7_DICOMConformanceStatement.pdf · **RamSoft** conformance index: https://www.ramsoft.com/conformance · **Merative/Merge**: https://www.merge.com/support/merge/merge-healthcare-statements
53. **Ambra/InteleShare public API reference** (grepped: zero DICOMweb/WADO/QIDO/STOW): https://access.dicomgrid.com/api/v3/api.html · Python SDK: https://dicomgrid.github.io/sdk-python/quickstart.html
54. **Konica Minolta Exa Physician Portal User's Manual v34.0.0** (doc 500-000802A, April 2025) — referrer order creation and e-signature: https://healthcare.konicaminolta.us/sites/default/files/2025-04/500-000802a_epr_34.0.0_php_um.pdf
55. **eRAD** PACS API: https://erad.com/news/pacs-api-radiology-hl7-solutions/ · **AbbaDox** referral marketing: https://www.abbadox.com/for-referral-marketing · **Nuance mPower**: https://www.nuance.com/en-gb/healthcare/medical-imaging/mpower-clinical-analytics.html

**Payer, RBM, and benefit-manager primary sources**
56. **Avalon Health Solutions, Routine Radiology Benefit Management** — post-service, pre-payment, no prior auth; X-ray/ultrasound/non-cardiac nuclear medicine; CT/MRI/PET excluded; "$1 PMPM savings potential," "~30% low-value" (**VENDOR CLAIM**): https://www.avalonhcs.com/solutions/benefit-management/routine-radiology/
57. **UnitedHealthcare/Surest outpatient radiology PA effective 2026-10-01** (CT, MRI/MRA, nuclear cardiology, PET): https://www.uhcprovider.com/content/provider/en/resource-library/news/2026/pa-surest-radiology-services.html
58. UHC outpatient radiology PA FAQ (referrer notified by fax): https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/radiology/COMM-Exchange-Radiology-Prior-Auth-FAQ.pdf · TriWest referrals/authorizations: https://tricare.triwest.com/en/provider/tricare-provider-handbook/tricare-referrals-and-authorizations/ · Highmark radiology/cardiology imaging PA guide: https://providers.highmark.com/content/dam/highmark/en/providerresourcecenter/pdfs/all/documents/pdfs/policies-and-programs/care-management/radiology-and-cardiology-imaging-prior-auth-ref-guide.pdf
59. Health Net/Evolent radiology benefit management: https://www.healthnet.com/content/healthnet/en_us/providers/support/radiology-benefit-management.html · https://providerlibrary.healthnetcalifornia.com/news/26-255-evolent-removes-prior-authorization-for-select-radiology-.html

**CAQH / DataSpring (industry self-report)**
60. **2024 CAQH Index full PDF** — per-transaction provider costs read directly: https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf
61. CAQH *Administrative Transaction Costs by Provider Specialty* brief (2023 Index) — **no radiology/imaging breakout**: https://www.caqh.org/hubfs/CAQH%20Insights_2023%20Index%20Report_Provider%20Specialty%20Issue%20Brief_Final.pdf
62. CAQH 2026 eSolutions Xchange slides (2025 Index headline figures): https://s3.amazonaws.com/amo_hub_content/Association361/files/CAQH_2026%20eSolutions%20Xchange%20Slides.pdf · 2023 Index: https://caqh.org/hubfs/43908627/drupal/2024-01/2023_CAQH_Index_Report.pdf

**Agentic vendors (VENDOR CLAIM unless noted)**
63. **Availity** CMS-0057-F suite: https://www.availity.com/cms-0057-f-interoperability-suite/ · **Humana + athenahealth + Availity case study** (Oct–Dec 2023): https://www.availity.com/case-studies/end-to-end-prior-authorizations-using-fhir-apis/ · **Waystar** CMS-0057-F: https://www.waystar.com/blog-cms-0057-f-take-these-4-steps-for-interoperable-prior-authorization/ · Waystar agentic launch (Aug 2026): https://www.waystar.com/news/waystar-launches-new-agentic-solutions-transforming-ai-into-action-across-the-revenue-cycle/
64. **RamSoft + Alpha Nodus "Gravity AI"**: https://www.ramsoft.com/press-releases/partners-with-alpha-nodus-automating-prior-authorizations-with-ai · Diagnostic Imaging coverage (2025-03-26, verified as vendor claim with no pilot cited): https://www.diagnosticimaging.com/view/new-collaboration-promise-automating-prior-authorizations-radiology-with-ai
65. **Cohere Health / Humana** diagnostic imaging expansion: https://www.prnewswire.com/news-releases/cohere-health-and-humana-expand-prior-authorization-partnership-adding-diagnostic-imaging-and-sleep-services-302123731.html · Cohere Unify: https://www.coherehealth.com/news/cohere-unify-agentic-ai-redesigning-health-plan-operations
66. **Humata Health / Allegheny Health Network** (first-month 70%): https://www.humatahealth.com/newsroom/humata-health-powers-first-touchless-prior-authorization---from-order-to-approval---with-allegheny-health-network · **R1 acquisition closed ~2026-09-16**: https://www.beckershospitalreview.com/finance/revenue-cycle-management/r1-closes-humata-health-deal-to-bolster-ai-prior-authorization/
67. **Anterior**: https://www.prnewswire.com/news-releases/anterior-closes-40-million-to-accelerate-health-plan-ai-adoption-bringing-total-funding-to-64-million-302685959.html · **Rhyme**: https://www.getrhyme.com/ · **Adonis**: https://adonis.io/resources/adonis-raises-40m-series-c-to-equip-healthcare-providers-with-ai-driven-revenue-cycle-operations · **SmarterDx**: https://www.smarterdx.com/ · **Notable**: https://www.notablehealth.com/ and referral case study https://www.notablehealth.com/customer-stories/optimizing-referral-management-with-ai · **Infinitus pricing** (no self-serve tier): https://www.infinitus.ai/pricing/ · **CodaMetrix OHSU** (verified vendor-published, undated, no peer review): https://www.codametrix.com/case-studies/ohsu-case-study · **Honey Health**: https://www.honeyhealth.ai/articles/10-best-ai-radiology-prior-authorization-tools-2026 · **Staffingly**: https://staffingly.com/labs-imaging/services/radiology-prior-authorization/
68. **Artera** #1 Best in KLAS 2026: https://www.prnewswire.com/news-releases/artera-named-1-best-in-klas-for-patient-communications-302699189.html · HIMSS26 "LLM as Judge": https://artera.io/blog/ai-agents-for-patient-communications-himss-recap/ · Atlantic Health colonoscopy outreach: https://www.mobihealthnews.com/news/artera-atlantic-health-deploy-ai-agents-colonoscopy-patient-outreach
69. **Tennr** $101M Series C (no radiology mention): https://www.prnewswire.com/news-releases/healthcare-referrals-are-where-patients-get-lost-tennr-raises-101m-to-bring-the-visibility-our-system-desperately-needs-302485255.html · **ReferralMD Direct + 360X** (2026-08-18): https://www.prweb.com/releases/referralmd-accelerates-healthcare-interoperability-with-direct-messaging-and-direct-360x-302854244.html · **Health Gorilla** orders: https://www.healthgorilla.com/home/markets/labs
70. **Mach7** legacy-PACS-replacement framing (competitor advocacy, useful language only): https://www.mach7t.com/blog/the-legacy-pacs-replacement-wave-what-to-demand-from-a-modern-vna · **Axis Imaging News 2007** migration costs (quotes solid, applicability Low): https://axisimagingnews.com/radiology-products/radiology-software/pacs/changing-pacs-time-money-and-dicom · AuntMinnie "9 ways to reduce your legal exposure to PACS problems" (**verified: does NOT discuss egress or data ownership**): https://www.auntminnie.com/imaging-informatics/enterprise-imaging/pacs-vna/article/15621134/9-ways-to-reduce-your-legal-exposure-to-pacs-problems · Northeast Radiology PACS **breach** suit dismissed (**not** a data-access case): https://www.auntminnie.com/imaging-informatics/enterprise-imaging/pacs-vna/article/15631021/lawsuit-over-pacs-hack-in-new-york-dismissed

**Litigation, state law, and HITL governance**
71. **Estate of Lokken v. UnitedHealth Group** (D. Minn. 0:23-cv-03514) — discovery order 2026-03-09: https://litigationtracker.law.georgetown.edu/wp-content/uploads/2023/11/Estate-of-Gene-B.-Lokken-et-al-v.-UnitedHealth-Group-Inc.-et-al_2026_3_9_ORDER-ON-MOTION-TO-COMPEL-DISCOVERY.pdf · https://www.hunton.com/hunton-insurance-recovery-blog/court-allows-discovery-into-insurers-use-of-ai-to-deny-claims · https://www.tresslerllp.com/thought-leadership/estate-of-gene-b-lokken-et-al-v-unitedhealth-group-inc-ai-risks-in-medical-insurance-coverage-disputes/
72. **Cigna PxDx** — https://www.healthcaredive.com/news/cigna-lawsuit-algorithm-claims-denials-california/688857/ · https://www.healthcaredive.com/news/cigna-lawsuit-claims-algorithm-denials-connecticut/694292/ · imaging named in bulk-denial allegations: https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/cigna-violated-law-denying-claims-imaging-and-other-services-bulk-lawsuit-alleges
73. **CMS WISeR Model** (active 2026-01-01; six states incl. **Texas**; human clinician must review every non-affirmation): https://www.crowell.com/en/insights/client-alerts/wiser-under-scrutiny-ai-claims-review-debate-reaches-cms · https://www.dinsmore.com/publications/is-ai-wiser-cms-models-ai-based-prior-authorization-process-in-six-states/
74. **California SB 1120**: https://www.fenwick.com/insights/publications/californias-sb-1120-regulates-ai-in-health-plan-utilization-review-and-management-activities-starting-in-january · https://www.nfp.com/insights/california-limits-ai-use-in-health-plan-utilization-reviews/ · **state AI-UR tracker** (eight-state table): https://www.ailawsbystate.com/tools/healthcare-ai-tracker
75. **TRAIGA** commentary (secondary; statute read directly at #8): https://txaims.com/blog/complete-guide-traiga-hb-149-texas-ai-law · https://enderezalaw.com/patient-transparency-and-ai-what-texas-healthcare-providers-need-to-know-about-new-ai-disclosure-laws/
76. Deployed HITL architectures: confidence threshold + dual queue https://asprcmsolutions.com/blog/autonomous-medical-coding/ · auditor role inversion https://mdaudit.com/blog/auditing-autonomous-medical-coding-systems/ · Parlance AI-briefed transfers https://www.prnewswire.com/news-releases/parlance-gives-healthcare-contact-centers-instant-configuration-control-and-ai-briefed-agent-transfers-302839592.html

**Payer pledge, surveys, and market framing (self-report or secondary)**
77. AHIP/BCBSA pledge progress (**trade-association self-report, unaudited**): https://www.ahip.org/news/articles/health-plans-reduce-prior-authorization-support-continuity-of-care-and-enhanced-consumer-communications · https://www.healthcaredive.com/news/insurer-prior-authorization-commitment-update-ahip-bcbsa/816819/ · https://www.fiercehealthcare.com/payers/insurers-have-eliminated-11-prior-authorizations-under-reform-pledge · physician skepticism: https://www.healthcaredive.com/news/physicians-skeptical-insurer-pledges-reform-prior-authorization-ama/820126/
78. **Advisory Board, *Growing Imaging Referrals*** (Imaging Performance Partnership, 2019) — Loyalist/Splitter/Dissenter segmentation; 50,484-MRI referral-routing analysis: https://www.advisory.com/content/dam/advisory/en/public/shared/Research/IPP/Research-Study/2019/Growing-Imaging-Referrals-IPP-2019-final.pdf
79. Forvis Mazars on using public payer PA data (secondary confirmation that CY2025 metrics posted 2026-03-31): https://www.forvismazars.us/forsights/2026/08/cms-0057-f-using-public-payor-prior-authorization-data
80. RBM concentration aggregation (**Low-Medium**, underlying filings unverified): https://nirmitee.io/blog/who-decides-prior-authorization-review-vendors-2026/ · **"56% of referrals faxed" — unsubstantiated, DO NOT USE**: https://avofax.com/blog/why-56-percent-healthcare-referrals-still-faxed · one RCM vendor's client-base benchmarks (**not an industry benchmark**): https://www.revenuesynergy.com/resources/2026-benchmark-report.html

**Access notes affecting confidence.** federalregister.gov and ecfr.gov returned HTTP 302 redirects to an interstitial on the standard fetch path; both rules were retrieved via the Federal Register API and full-text endpoints with an explicit user agent — the same primary text. **PubMed web fetch is cookie-blocked**; all abstracts came via the NCBI eutils API. **Joint Commission and ACR PDFs** returned unreadable binary to the fetch tool and were downloaded and text-extracted locally with `pdftotext -layout`, so all TJC and ACR quotations are from official documents. **Radiology Business returned HTTP 403 on every direct attempt** (Cloudflare), as did Becker's, AJR Online, ScienceDirect, HealthLeaders, Fierce Healthcare and GlobeNewswire — figures from those are flagged "not read in original" at each point of use. **statutes.capitol.texas.gov and texmed.org** served JavaScript shells or unparseable PDFs; the Texas statutes were obtained instead from capitol.texas.gov enrolled-bill HTML, which is the authoritative text. **Aetna's developer portal** returned a JS shell. The **Gazelle IHE Product Registry UI** returned HTTP 503 during the session.
