# Referrer Channel & Imaging Administration Benchmarks — Research Report

**Prepared:** 2026-10-10 · **Analyst:** read-only research pass · **Scope:** Topic A (referring physician channel automation) + Topic B (labor/financial benchmarks for outpatient imaging administration)

**Confidence legend:** High = primary source read directly (standards body document, peer-reviewed paper, official PDF). Medium = credible secondary/trade source or vendor technical doc. Low = single unverified source, dated, or vendor marketing only.

---

## ⚠️ HEADLINE FINDINGS — READ FIRST

Five findings change how the pitch should be written:

1. **THE PREMISE (A6) IS NOT SUPPORTED AT THE VOLUME LEVEL.** There is good evidence referrers *say* reporting/communication matters, and strong evidence TAT is *worsening nationally*. There is **NO EVIDENCE FOUND** of a published study showing that improving TAT or referrer communication **causes measurable referral-volume gain** at an imaging center. The best available study (JACR 2025 conjoint analysis) finds **cost/copay dominates** referrer site-selection — and TAT is not even a tested attribute. See §A6. **Do not claim TAT drives volume.**

2. **The Joint Commission requirement the pitch likely cites does not exist in the form usually cited.** Effective Jan 1 2026, hospitals are under **NPG.01.02.01** (NPSGs → "National Performance Goals"), not NPSG.02.03.01. More important: the **2026 Ambulatory Health Care NPSG set contains NO critical-results goal at all** — verified by reading the document. An outpatient imaging center accredited under AHC is **not** bound by a TJC critical-results NPSG. See §A4.

3. **ACR Practice Parameter for Communication was Revised 2025 (Resolution 9)** — effective Oct 1, 2025. This is current and *is* the real governing document for an outpatient imaging center. See §A4.

4. **The "56% of referrals are faxed" statistic is unsourced.** Traced to a fax vendor citing "industry research" with no study, no year, no link. **Do not use it.** See §A1.

5. **Imaging-specific admin staffing benchmarks essentially do not exist publicly.** The one radiology FTE figure found is from a sample of **11 practices**. CAQH has **no radiology breakout**. HFMA MAP Keys has **no imaging-specific keys**. See §B1.

---

# TOPIC A — THE REFERRING PHYSICIAN CHANNEL

## A1. Order intake: fax volume, fax-parsing automation, referral intake

### Fax prevalence — the numbers in circulation are not verifiable

**NO RELIABLE PRIMARY SOURCE FOUND** for any current fax-share-of-referrals statistic.

- The widely repeated **"56% of healthcare referrals are still faxed"** figure was traced to its apparent origin and is **UNVERIFIED**. The page attributes it only to "according to industry research" with **no named study, survey, year, or URL**. Source: [avofax.com](https://avofax.com/blog/why-56-percent-healthcare-referrals-still-faxed), fetched 2026-10-10. Confidence that it is **unsubstantiated: High**. **RECOMMENDATION: do not use this number.**
- Adjacent figures ("89% of healthcare organizations still use fax," "70% of clinical communication via fax," "9 billion healthcare fax pages") all surfaced **only on fax-vendor and referral-vendor blogs citing each other circularly**. No primary source located. **NO EVIDENCE FOUND** at primary-source level. Confidence: **Low** on all.

**What *can* be defended:** CAQH/DataSpring measures electronic adoption by transaction type, and for **medical prior authorization, electronic adoption reached 40%** — i.e. a 60% majority remains manual (portal/phone/fax/mail). This is a real, methodologically documented figure (see §B2) and is the honest way to evidence "manual channel still dominates" without inventing a fax statistic.

### Vendors — what is actually automated

Full vendor sweep conducted. Key correction up front: **of 11 named vendors, 5 have no role in the referrer→imaging-center channel at all.**

| Vendor | In this channel? | Imaging-specific? | Evidence quality |
|---|---|---|---|
| **Notable Health** | **Yes — strongest** | **YES, explicit** | Best-quantified artifact found |
| **Tennr** | Yes | **PARTIAL — radiology framing is trade press, not the company** | Vendor claims only |
| **Luma Health** | Yes | No imaging-specific evidence | Vendor claims only |
| **ReferralMD** | Yes | **YES — dedicated imaging-center page** | No measured outcomes |
| **Health Gorilla** | Infrastructure | Partial (order rails) | No measured outcomes |
| **Infinitus** | Provider↔**payer**, not referrer | Partial | Out-of-channel |
| **Phreesia** | Patient-facing | No radiology product found | Out-of-channel |
| **Hyro** | Patient-facing call center | No evidence found | Out-of-channel |
| **Klara** | Patient messaging | No order-intake capability found | Out-of-channel |
| **Orby AI** | **NOT a healthcare vendor** | None | General enterprise RPA; acquired by Uniphore |
| **Medicom Health** | **Wrong category** | Hospital marketing HRAs | Divested to Eruptr 2021 |

**Notable Health — the only well-quantified case in this channel.** Automates faxed-referral → order creation across 14 order types explicitly including **MRI, CT, ultrasound, mammography, DEXA, CTA, nuclear medicine, PET**. Vendor-published case study reports: 85% of order transcription automated; 10,000 faxed referrals auto-transcribed; **turnaround 48 hr → 10 min**; 12.5 FTEs on indexing reduced to 4 upskilled; 15% of inbound faxes handwritten. Source: [notablehealth.com](https://www.notablehealth.com/customer-stories/optimizing-referral-management-with-ai), no publication date. **VENDOR-PUBLISHED, site anonymized as "a Florida health system," NOT peer-reviewed, and a health system rather than a freestanding imaging center.** Separately labeled figures ("8,000 staff hours/year," "2.6x ROI") are **PROJECTED, not measured**. Confidence: **Medium-High** capability, **Medium** numbers.

**Tennr — material correction.** Trade press (Radiology Business, AuntMinnie) framed Tennr as an imaging-referral company. **Tennr's own $101M Series C press release does not mention radiology or imaging centers**, and all named customers are DME/home-medical (Norco, Home Medix, NEB Medical, King Drug). Funding facts are solid — **$101M Series C, $605M valuation, IVP-led, 10M documents/month**, [PR Newswire 2025-06-18](https://www.prnewswire.com/news-releases/healthcare-referrals-are-where-patients-get-lost-tennr-raises-101m-to-bring-the-visibility-our-system-desperately-needs-302485255.html), confidence **High**. All outcome claims ("75% faster referrals with 4X volume," "same-day intake from a 3-week backlog") are **VENDOR CLAIM**, no named imaging site, no peer review. Confidence that the radiology positioning is unsubstantiated: **High**.

**Tennr's one genuinely differentiated feature:** the "Tennr Network," where **referring providers see the status of every patient they've sent out**. This is the closest thing found to a true two-way referrer channel product. Confidence **High** it is marketed; **NO EVIDENCE FOUND** of imaging-center deployment.

### RIS-native referrer portals — the most underrated finding

**Electronic order placement by the referrer is a mature, shipping RIS feature and predates the current AI wave by over a decade.** The AI intake vendors are largely automating the *fax path*; several RIS platforms already offer a *structured electronic order* path that bypasses fax entirely.

- **Konica Minolta Exa PACS/RIS — primary-source confirmed (strongest evidence in this section).** Official *Physician Portal User's Manual v34.0.0* (doc 500-000802A, **April 2025**) documents the referrer workflow verbatim: *"Create and schedule an exam… You can create an order for an exam. Staff at your facility receive the order and can schedule an appointment"* → **ADD STUDY** → **CREATE ORDER** → document **UPLOAD**. Also a documented **"Sign an order"** function with graphical signature that clears the exam from Exa's "Unsigned Orders" report. Source: [Exa Physician Portal Manual](https://healthcare.konicaminolta.us/sites/default/files/2025-04/500-000802a_epr_34.0.0_php_um.pdf). Confidence **High** (vendor *technical manual*, not marketing).
- **RamSoft PowerServer** — referrer portal places exam orders + views results. Confidence **Medium-High**.
- **AbbaDox** — rule-based referrer self-scheduling; referrer-visible real-time exam status (Checked-in / No-Show / With Tech / Completed). Confidence **Medium-High**.
- **eRAD** — markets "referrers can send electronic orders… from any application with a single click." ⚠️ Ambiguous: reads closer to *document transmission* than structured RIS order entry. **UNRESOLVED** (page truncated on fetch).
- **Sectra** — portal with **CPOE using ACR Appropriateness Criteria**. ⚠️ **Source dated 2011-10-19.** Capability confidence Medium, **currency confidence Low — must be re-verified before use.**
- **View/status only (NOT order placement):** Intelerad InteleConnect (order *statuses*, reports, critical-results acknowledgement), Merative Merge, Nuance PowerShare (image/report exchange network), Ambra Health (inbound image upload).

### Does Direct Secure Messaging / Carequality / TEFCA carry imaging ORDERS today?

**Answer: TEFCA does NOT. Direct Secure Messaging CAN, via the 360X profile, but adoption evidence is absent.**

- **TEFCA — definitive NO, primary source.** Read the governing **SOP: Exchange Purposes (XPs) v5.1, effective 2026-07-01** directly. The document contains **ZERO occurrences of the word "order."** Authorized XPs are Treatment (T-TRTMNT), Payment, Health Care Operations, Public Health, Individual Access Services, Government Benefits Determination — all framed as **Query / QHIN Message Delivery / FHIR Push for records**, not order placement. "Treatment" inherits the 45 CFR §164.501 definition, which *includes* "the referral of a patient… from one health care provider to another" as a *permissible purpose*, **but that is a privacy-law purpose category, not an order transaction**. Source: [Exchange Purposes SOP v5.1](https://rce.sequoiaproject.org/wp-content/uploads/2026/07/Exchange-Purposes-SOP-v5.1_7.1.2026_508.pdf). Confidence: **High**.
  - Related: Treatment XP Implementation SOP effective **2026-08-03** makes **TEFCA Required Treatment** responses mandatory for provider-associated Responding Nodes. Relevant to retrieving **priors**, not to placing orders. Confidence **Medium-High**.
- **Direct Secure Messaging + IHE 360X** — 360X is the closed-loop referral profile, and it **uses HL7 v2 messages of the same family already established in radiology order workflows**. [IHE PCC 360X Supplement](https://www.ihe.net/uploadedFiles/Documents/PCC/IHE_PCC_Suppl_360X.pdf). **ReferralMD announced Direct Messaging + Direct 360X on 2026-08-18**, claiming electronic referral requests, acknowledgments, accept/decline, scheduling notifications, consult reports, and completion/status updates — **all VENDOR CLAIM**; imaging orders **not specifically mentioned**. [PRWeb 2026-08-18](https://www.prweb.com/releases/referralmd-accelerates-healthcare-interoperability-with-direct-messaging-and-direct-360x-302854244.html). Confidence **Medium**.
- **Health Gorilla** (TEFCA-designated QHIN) states its network "allows providers to place lab and imaging orders electronically." This is a **vendor-network capability outside the TEFCA XP framework**, not TEFCA itself. [healthgorilla.com](https://www.healthgorilla.com/home/markets/labs). Confidence **Medium**. **NO MEASURED ADOPTION DATA FOUND.**
- **Carequality** — **NO EVIDENCE FOUND** that Carequality carries imaging orders; it is query-based document exchange. Confidence **Medium** (absence of evidence, not proof of absence).

**Bottom line for the pitch:** national interop frameworks today move **records and priors**, not **orders**. The order channel remains fax, phone, payer/RIS portals, and point-to-point integrations. Confidence: **High**.

---

## A2. Order-to-protocol mapping; incomplete-order chasing

### Published order-incompleteness RATES — evidence is strong but almost entirely NON-US

This is the best-evidenced problem area in Topic A. **Critical caveat: no US outpatient rate found.**

| Finding | Source | Confidence |
|---|---|---|
| **98.4% of outpatient imaging requests inadequate** by RI-RADS; only **1.6% grade A**; complete clinical information in only **2.2%**; Grade D most frequent (51.9%); n=1,103 consecutive outpatient requests (US/MRI/CT/CR), Jan–Jun 2026, multicentre. Orthopedics worst (OR 3.59); CT worse than MRI (OR 2.99). Interobserver agreement only fair (Fleiss κ=0.376). | *Eur J Radiol* 2026 Sep;205:113217, [PMID 42731498](https://pubmed.ncbi.nlm.nih.gov/42731498/) | **High** (peer-reviewed) — but **SAUDI ARABIA**, not US |
| **"Incomplete Radiology Requests Are the Norm"** — 400 requisitions; 82% met minimum threshold (≥6 of 8 HAS criteria) but only **67% stated the clinical purpose** and only **35% referenced prior imaging**. Administrative fields completed more consistently than clinical fields. | *Cureus* 2025 Dec 2;17(12):e98353, [PMID 41487743](https://pubmed.ncbi.nlm.nih.gov/41487743/) | **High** (peer-reviewed) — **MOROCCO**, tertiary hospital |
| LLM auto-scoring of requisition quality: BERT model on **131,683 requisitions**, external test F1 **0.93**, κ 0.88. Demonstrates the *chasing* step is automatable at scale. | *Eur Radiol* 2026 Mar;36(3):1616-1627, [PMID 40836020](https://pubmed.ncbi.nlm.nih.gov/40836020/) | **High** — **TÜRKIYE** |

**Explicit known-unknown:** **NO EVIDENCE FOUND** for a published incomplete-order or order-error rate in **US outpatient radiology** specifically. PubMed queries for US-scoped order-indication/CDS rates returned **COUNT: 0**. Any US figure in the pitch must be labeled as extrapolated from non-US literature, or sourced from the client's own data. Confidence in this gap: **High**.

### Order-to-protocol mapping automation — real, with US data

- **Strongest US evidence:** Cleveland Clinic study, **94,501 abdominal CT studies over 4 years**, classifying into 11 protocol classes from **free-text indication + ICD codes**. Best F1 **0.854** (AutoML), 0.847 ULMFiT, 0.811–0.828 conventional ML. *J Digit Imaging* 2022 Oct;35(5):1120-1130, [PMID 35654878](https://pubmed.ncbi.nlm.nih.gov/35654878/). Confidence **High**. Note: this is **retrospective classification accuracy, not a deployed-workflow outcome.**
- Systematic review reports transformer NLP protocol-selection accuracy **84–98%** (MRI-limited tasks), GPT-3.5/BERT to ~91% on contrast/protocol selection, and that protocoling occupies **"at least 6% of a radiologist's time."** Source: [ScienceDirect S3050577126000046](https://www.sciencedirect.com/science/article/pii/S3050577126000046) — **direct fetch returned HTTP 403; figures are from search-result extracts, NOT read in the original.** Confidence **Low-Medium; verify before citing.**
- Review-level claim that automated positioning and protocol selection **remain at "feasibility level"** rather than routine deployment. Confidence **Medium**. **This tempers any claim that protocol automation is turnkey.**

---

## A3. Insurance/auth status callback to the referring office

**Finding: NO VENDOR FOUND productizing proactive prior-auth status notification back to the referring office. This is a genuine white space — with one important caveat that prevents overstating it.**

- Vendor auth-status tracking consistently flows to **imaging-center staff** and to the **patient** — the referring office is absent from every vendor description reviewed. Confidence **Medium-High**.
- **⚠️ CAVEAT THAT MUST BE STATED IN THE PITCH: the payer already notifies the referrer, by fax.** Payer documentation confirms that on imaging-authorization approval, **"referring providers and rendering facilities are notified in writing by fax,"** and approval notifications go to **beneficiary and referring provider**. TRICARE/TriWest and Highmark expose referrer-visible auth status in payer portals; eviCore exposes status by web and phone. Sources: [UHC outpatient radiology PA FAQ](https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/radiology/COMM-Exchange-Radiology-Prior-Auth-FAQ.pdf), [TriWest](https://tricare.triwest.com/en/provider/tricare-provider-handbook/tricare-referrals-and-authorizations/), [Highmark imaging PA guide](https://providers.highmark.com/content/dam/highmark/en/providerresourcecenter/pdfs/all/documents/pdfs/policies-and-programs/care-management/radiology-and-cardiology-imaging-prior-auth-ref-guide.pdf). Confidence **High**.
- **Correct framing: the opportunity is CONSOLIDATION AND PUSH, not first-ever visibility.** Referrers today can get status, but only pull-based, per-payer, fragmented across portals and inbound fax. **A pitch claiming referrers "fly blind" on auth status would be contradicted by payer documentation.**
- Closest existing analogues are status-visibility portals, none of which carry *auth* status: Tennr Network (referral status), AbbaDox (operational exam status), Intelerad InteleConnect (order status). **Infinitus** retrieves PA status *from payers* and writes it to the provider — the last mile to the referrer does not exist in its product.

---

## A4. Report delivery + critical results acknowledgment — CORRECTIONS REQUIRED

### ⚠️ Joint Commission — the commonly cited requirement has CHANGED and may NOT APPLY

**Three distinct corrections, all verified by reading the official Joint Commission PDFs directly:**

**(1) For HOSPITALS, the identifier changed effective Jan 1 2026.** NPSGs were reorganized into **"National Performance Goals" (NPGs)**. The critical-results requirement is now **NPG.01.02.01**: *"The hospital reports critical results of tests and diagnostic procedures on a timely basis."* Elements of Performance (verbatim):
> **EP 1** — The hospital develops and implements written procedures for managing the critical results of tests and diagnostic procedures that address the following: • The definition of critical results of tests and diagnostic procedures • By whom and to whom critical results of tests and diagnostic procedures are reported • The acceptable length of time between the availability and reporting of critical results of tests and diagnostic procedures. *Documentation is required.*
> **EP 2** — The hospital evaluates the timeliness of reporting the critical results of tests and diagnostic procedures.

Source: [National Performance Goals, Effective January 2026, Hospital Program](https://digitalassets.jointcommission.org/api/public/content/9ca80055182b4274842a5780a94f2c82) (report generated 2025-09-26). Confidence: **High**.

**(2) 🔴 For AMBULATORY HEALTH CARE — there is NO critical-results goal in 2026.** I read the complete *National Patient Safety Goals Effective January 2026 for the Ambulatory Health Care Program* (10 pages). The full goal set is **only**: NPSG.01.01.01 (patient ID), NPSG.03.04.01 / 03.05.01 / 03.06.01 (medication safety), NPSG.07.01.01 (hand hygiene), NPSG.16.01.01 (health outcomes for all), and UP.01.01.01 / 01.02.01 / 01.03.01 (Universal Protocol). **There is no Goal 2 and no critical-results requirement.** Source: [AHC 2026 NPSGs](https://digitalassets.jointcommission.org/api/public/content/92c95c4e94304b2084e7e039d916719b?v=3c64fe83). Confidence: **High**.
> **Implication:** TJC's AHC program covers "outpatient radiology and diagnostic settings." An imaging center accredited under AHC is **not** bound by a TJC critical-results NPSG in 2026. **Citing TJC as the compliance driver for an outpatient imaging center would be incorrect.** The real drivers are the **ACR Practice Parameter**, state law, payer/accreditation contracts, and malpractice exposure.

**(3) The Laboratory program retains the old numbering.** NPSG.02.03.01 still exists verbatim for **Laboratory** (EP 1 and EP 3, same substance). Source: [Lab 2026 NPSGs](https://digitalassets.jointcommission.org/api/public/content/3c7a110c215943bc80d9ce87e9d9ee9d?v=aef80e14). Confidence **High**. **So "NPSG.02.03.01" is not fictional — it is simply the wrong program for an imaging center.**

### ACR Practice Parameter for Communication of Diagnostic Imaging Findings — CURRENT: Revised 2025

Read the full document directly. **Development chronology:** 1991 (Res. 5) → Revised 1995, 1999, 2001, 2005, 2010, 2014, 2020 (Res. 37) → Amended 2021 (Res. 16; 17) → Amended 2023 (Res. 2c) → **Revised 2025 (Resolution 9)**. Practice parameters take effect **October 1 of the year revised**, so the current version is **effective 2025-10-01**. Source: [ACR Gravitas DocId 74](https://gravitas.acr.org/PPTS/DownloadPreviewDocument?DocId=74). Confidence: **High**.

**What it actually requires (verbatim extracts):**
- Framing: *"Quality patient care can only be achieved when study results are conveyed in a timely fashion."* And notably: **"Timely receipt of the report is more important than the method of delivery."**
- **Reciprocal duty:** *"There is a reciprocal duty of information exchange. The referring physician or other relevant health care provider also shares in the responsibility for obtaining results of imaging studies ordered and acting on them."* ← **Important for scoping liability claims in the pitch; the imaging center is not solely responsible.**
- **Three nonroutine-communication scenarios:** (i) findings suggesting need for **immediate or urgent intervention** (e.g. pneumothorax, pneumoperitoneum, misplaced line/tube); (ii) findings **discrepant with a preceding interpretation** where failure to act may adversely affect health; (iii) findings the interpreting physician believes **significant and unexpected**, may not need immediate attention but if not acted on may worsen over time.
- **Documentation:** *"Interpreting physicians should document all nonroutine communications"* — in report, medical record, or department/personal log, including **date and time, method of communication, and name of the person to whom it was delivered.**
- **Electronic methods permitted with a condition:** *"Electronic forms of communication are also an appropriate method… as long as they provide documentation of receipt to demonstrate that the communication has been delivered and acknowledged."* ← **This single clause is the strongest defensible compliance hook for a closed-loop acknowledgment product.** Confidence **High**.
- Note the preamble explicitly disclaims establishing a legal standard of care; courts have split (cites *Stanley v. McCarver*).

### ACR Actionable Reporting Work Group — the actual document

**Larson PA, Berland LL, Griffith B, Kahn CE Jr, Liebscher LA. "Actionable findings and the role of IT support: report of the ACR Actionable Reporting Work Group." *J Am Coll Radiol.* 2014 Jun;11(6):552-8.** doi:10.1016/j.jacr.2013.12.016. [PMID 24485759](https://pubmed.ncbi.nlm.nih.gov/24485759/). Confidence **High** (abstract retrieved via NCBI eutils; PubMed web fetch was cookie-blocked).

Three categories of actionable findings requiring communication and clinical decision within **minutes (category 1), hours (category 2), or days (category 3)**. Category 1 = could lead to death or significant morbidity if not promptly recognized. The group explicitly **does not believe definitive lists are possible** but published illustrative lists per category. Recommends IT **document the communication and facilitate auditing**, that **vendors build locally customizable platforms**, and that systems be **highly reliable and fit seamlessly into workflow**. Two published comments exist (*JACR* 2014 Sep;11(9):924-5 and 925-6) — **not retrieved**; may contain dissent. **Note the document is 2014 — 12 years old.** Confidence **High** on content, and this is the authentic "ACR document" requested.

### Closed-loop communication — measured outcomes

- Best measured closed-loop artifact found: UK ED QI project, two cycles of 50 patients. Follow-up CXR completion **32% → 70%** (p<0.001); closed-loop **Critical Alert System inclusion 6% → 72%** (p<0.001); ED-initiated follow-up requests 42% → 86% (p=0.008). No alert fatigue observed. *Cureus* 2025 Sep 22;17(9):e92926, [PMID 40988972](https://pubmed.ncbi.nlm.nih.gov/40988972/). Confidence **High** on the study; **low transferability** — UK NHS emergency department, n=100 total, not a US outpatient imaging center.
- **NO EVIDENCE FOUND**: no measured closed-loop critical-results outcome study at a **US freestanding outpatient imaging center**. PubMed yielded **COUNT: 2** for closed-loop radiology acknowledgment outcomes overall. Confidence in this gap: **High**.

---

## A5. Referrer-facing analytics / scorecards / "referrer experience"

Category is real and commercially established, but **almost entirely vendor-described — NO independently measured outcomes found for any product in it.**

- **AbbaDox Referral Marketing CRM** — most imaging-specific. Measures referral volume by **completed and scheduled studies** (argued as more accurate than raw referral counts), marketing ROI, and **geographic market share by mapping referrer addresses around each center**. [abbadox.com](https://www.abbadox.com/for-referral-marketing). **VENDOR CLAIM**, no measured outcomes. Confidence **Medium**.
- **Nuance mPower Clinical Analytics** — mines the PowerScribe reporting database; explicitly analyzes *"ordering trends, scheduling patterns, and referring physician volumes."* Report-derived, so it measures **realized volume**, not referrer engagement. [nuance.com](https://www.nuance.com/en-gb/healthcare/medical-imaging/mpower-clinical-analytics.html). **VENDOR CLAIM.** Confidence **Medium**.
- **Inflo Health** — follow-up/recommendation tracking, **not** referrer scorecards. A case study claims **"25X ROI" at "a large integrated health system"** — **VENDOR CLAIM, site unnamed, methodology undisclosed. DO NOT REUSE THIS FIGURE.** Confidence **Low** on the number.
- **Physician-liaison / PRM CRM category** — tracks liaison visits, outreach history, referral volume, **conversion rate by provider**, territory maps, liaison ROI. Named: Tracking Works CRM, TrackerPLUS, Tiller Hewitt PRM, ReferralMD PRM, Redspot/RSI. Category confidence **Medium**; individual claims unverified.
- **Analogic — NO EVIDENCE FOUND.** Analogic is imaging **hardware/OEM** (detection, ultrasound). No referrer-analytics product exists. **This appears to be an error in the source brief.** Confidence **High**.

**The one genuinely useful framework found — and it is NOT a vendor source.** Advisory Board, *Growing Imaging Referrals* (Imaging Performance Partnership, **2019**, 36pp): segment referrers as **Loyalists (100–80% revenue share), Splitters (80–20%), Dissenters (20–0.1%)** and prioritize outreach on **Splitters** — they already value the program and offer room for growth, and *"splitters can become dissenters without support."* Source: [advisory.com PDF](https://www.advisory.com/content/dam/advisory/en/public/shared/Research/IPP/Research-Study/2019/Growing-Imaging-Referrals-IPP-2019-final.pdf). Confidence **High** that this is the published framework; **2019 vintage**. **This is a defensible, non-vendor segmentation model for a referrer-scorecard section.**

**Trade-press "referrer experience as differentiator"** claims (easy to refer to, clear TAT communication, subspecialty reads, e-sign orders, critical-finding notification) are **advice/thought-leadership with no supporting data**. Confidence **Low** as evidence; usable only as market-sentiment color.

---

## A6. 🔴 THE PREMISE QUESTION — DOES TAT / COMMUNICATION DRIVE REFERRAL VOLUME?

### VERDICT: NO. The volume-linked claim is NOT SUPPORTED by published evidence. The pitch must be rewritten to the satisfaction/preference level, or reframed around cost and access.

The brief asked to distinguish **(a)** referrers *say* TAT/communication matters from **(b)** it actually changes referral **volume**. The distinction is decisive: **(a) is well supported. (b) has NO EVIDENCE FOUND.**

### (a) Evidence referrers SAY reporting/communication matters — GOOD, peer-reviewed

**Best study: UCSF, 11 domains of the radiology process map.** 2,720 clinicians surveyed, **729 responded (27%)**. Multivariate logistic regression identified strongest associations with overall satisfaction:
- **results/reporting overall — OR 4.71 (95% CI 2.15–10.23)** ← strongest of all 11 domains
- section worked with most closely — OR 3.39 (1.28–8.64)
- attending radiologist interactions — OR 3.71 (1.54–8.69)
- **timeliness of inpatient radiology results — OR 2.91 (1.01–8.09)** ← CI lower bound barely clears 1.0
- appointment availability for urgent outpatient studies — OR 2.01 (1.08–3.64)
- guidance for selecting correct imaging study — OR 1.88 (1.04–3.34)

Conclusion: *"Referring clinicians value most the accuracy of the radiology report and their interactions with attending radiologists."* *Clin Imaging* 2023 May;97:72-77, [PMID 36907042](https://pubmed.ncbi.nlm.nih.gov/36907042/). Confidence **High**.
> **Three limits that matter:** the outcome is **satisfaction, not volume**; it is a **single academic department**, not a freestanding outpatient center; and the headline driver is **report accuracy and radiologist relationships** — *timeliness ranked below those*, and the only timeliness variable that reached significance was **inpatient**.

Supporting, weaker: referring physicians' satisfaction with report completeness only moderate (mean **38.4 ± 24.3** on a −100/+100 scale), surgeons most dissatisfied ([*Eur J Radiol* 2025](https://www.sciencedirect.com/science/article/pii/S0720048X25001548), confidence **Medium**); and older work finding dissatisfaction high on "time to receipt of the written report" ([PMID 15719307](https://pubmed.ncbi.nlm.nih.gov/15719307/), German instrument, confidence **Medium**).

### (b) Evidence it changes referral VOLUME — NO EVIDENCE FOUND

**Systematic negative result.** Targeted PubMed queries via eutils returned:

| Query | Result |
|---|---|
| `radiology turnaround time referral retention` | **COUNT: 0** |
| `radiology report turnaround time market share` | **COUNT: 0** |
| `referring physician satisfaction radiology referral volume` | COUNT: 3 — **all irrelevant** (IR social media; AI narrative review; sustainability review) |
| `referring physician loyalty imaging center` | COUNT: 3 — **all irrelevant** (sustainability; palliative RO; unrelated) |

Web searching for a study measuring volume change after a TAT improvement, or volume loss after TAT degradation, returned **nothing**. Confidence in this negative finding: **High**.

### 🔴 The study that actively undercuts the premise

**Yuan C, Huang H, Dirschl D, Chintagunta P, Paushter D. "Characterization and Targeting of the Main Drivers of Elective Imaging Utilization: A Cross-Sectional Study Applying Conjoint Analysis." *J Am Coll Radiol.* 2025 May;22(5):521-529.** doi:10.1016/j.jacr.2025.01.009. [PMID 39828000](https://pubmed.ncbi.nlm.nih.gov/39828000/). Confidence **High**.

Design: **393 patients** (recent non-contrast shoulder/lumbar/knee MRI) + **168 physicians** (≥12 such MRIs ordered in past year). Conjoint choice screens, logistic model via MLE, plus latent class segmentation. This is the **methodologically strongest study on referrer site-selection** found — conjoint analysis measures *revealed trade-off weights*, not stated preference, making it much harder to dismiss than a satisfaction survey.

Findings:
- **"Both patients and referring physicians placed most value on copay and cost, with both groups containing a large segment that places almost all value on low costs."**
- Physicians also valued **image quality and a trusted radiologist**, with one physician segment weighting these above cost.
- Patients also valued **referring physician's recommendation** and **convenient appointment time and location**.
- **TAT / report turnaround / communication responsiveness were NOT among the dominant attributes reported.**

**Corroborating:** Chernew/Cooper et al. analysis of **50,484 lower-limb MRI scans** (2013 claims, large national insurer) found **"the key determinant of where a patient received MRI was referring physician recommendation,"** with patients bypassing **on average six lower-priced facilities** en route to the physician-recommended site (reported in the Advisory Board 2019 report). Confidence **Medium-High**. **This confirms the referrer controls routing — but says nothing about TAT influencing that choice.**

**Advisory Board's documented top five reasons referrals go out of network** (Crimson Medical Referrals data): **1 Patient preference 23.0% · 2 Provider directed 22.7% · 3 No specialist in network 15.4% · 4 Availability 12.5% · 5 Continuity of care 11.7%** (avg 29% of referrals out of network; 40% employed-PCP leakage). **Neither TAT nor report communication appears anywhere in the top five.** Confidence **Medium-High** (proprietary dataset, 2019).

### What IS strongly evidenced about TAT — a different and usable argument

TAT is **deteriorating nationally**, which is a real market condition even though it is not a demonstrated volume lever:
- **2014–2023: mean TAT +113%** (0.091 → 0.193 mean days to interpretation); by modality **CT +318%, MR +256%, US +140%, XR +63%**; flat through 2021 then sharp rise in 2022–2023; **2.6M outpatient studies**, 5% Medicare FFS sample. *J Am Coll Radiol* 2026 Jul;23(7):1244-1252, [PMID 41914942](https://pubmed.ncbi.nlm.nih.gov/41914942/). Confidence **High**. Also found longer TAT in **more disadvantaged / lower-income communities**.
- **Updated through 2024: +27% in one year; +177% over 2014–2024**; **2.9M studies**; 2023→2024 by modality US +49.1%, XR/fluoro +35.4%, CT +11.6%, MR +4.5%. *J Am Coll Radiol* 2026 Aug 4 (online), [PMID 42550124](https://pubmed.ncbi.nlm.nih.gov/42550124/); [Neiman HPI release 2026-08-04](https://www.neimanhpi.org/press-releases/imaging-interpretation-turnaround-time-continued-to-increase-in-2024-by-27/). Confidence **High**.
- Pay-for-performance can move TAT: completion-to-finalization **42.7 → 31.6 → 16.3 hours** across baseline/immediate/post periods ([*AJR*](https://ajronline.org/doi/10.2214/AJR.09.4164)). Confidence **Medium**. **TAT is manipulable — but the study measures TAT, not resulting volume.**

### 🔴 RECOMMENDED LANGUAGE FOR THE PITCH

**Defensible:**
> "Referring clinicians rate results/reporting as the single strongest driver of their overall satisfaction with a radiology service (OR 4.71, UCSF, n=729, *Clin Imaging* 2023), and national interpretation turnaround time has worsened 177% since 2014 (*JACR* 2026, 2.9M Medicare studies). Referrers control site-of-service routing (Chernew/Cooper, 50,484 MRIs). **Satisfaction and routing control are documented; a causal link from turnaround time to referral volume is not published, and we treat volume gain as a hypothesis to be measured, not an established benchmark.**"

**NOT defensible — do not write:**
> ~~"Faster turnaround drives referral volume"~~ · ~~"Better referrer communication increases referrals by X%"~~ · ~~"Imaging centers lose N% of referrals to slow reporting"~~ · ~~"56% of referrals are faxed"~~

**Also recommend confronting the cost finding head-on.** The strongest study in this space says **cost/copay dominates** referrer and patient choice. A pitch built on communication quality while ignoring price positioning is vulnerable to exactly one question from Fernando — a former imaging-company founder who will know this. Better to concede it: communication/ops excellence is a **retention and efficiency** play and a **tie-breaker among price-comparable sites** (physicians valuing *image quality and a trusted radiologist* is a real, measured segment in the JACR conjoint latent-class analysis), not a volume-acquisition engine.

---

# TOPIC B — LABOR AND FINANCIAL BENCHMARKS

## B1. Administrative staffing benchmarks for outpatient imaging

### 🔴 VERDICT: Imaging-specific administrative staffing benchmarks are effectively NOT PUBLICLY AVAILABLE at usable granularity.

**The only radiology-specific FTE figure found, with a disqualifying caveat:**
- **Radiology: median 1.52 total support staff per FTE physician**, vs 4.43 (physician-owned nonsurgical single-specialty) and 2.50 (hospital/IDS-owned nonsurgical single-specialty). **⚠️ BASED ON ONLY 11 RADIOLOGY PRACTICES.** Attributed to an MGMA cost survey via [Radiology Business](https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/mgma/mgma-survey-finds-office-payrolls-rising) (direct fetch **HTTP 403**; figures from search extract, **not read in original**). Confidence **Low-Medium**.
> **This figure should not anchor a staffing model.** n=11, mixed private/hospital settings, undated edition, source not directly verified, and it measures *support staff per physician* — a radiology-hostile denominator, since an imaging center's admin load scales with **study volume and payer mix**, not radiologist headcount.

**Paywall / availability audit:**

| Source | Imaging-specific? | Access | Price |
|---|---|---|---|
| **MGMA DataDive** (Cost & Revenue / Financials & Operations) | Specialty cuts exist but **radiology n is tiny** | **PAID + membership** | Membership from **$399/yr individual**; **dataset prices NOT publicly disclosed — quote required**. 2026 edition merges Cost & Revenue with Practice Operations, **July 2026** |
| **RBMA Accounts Receivable Survey** | **YES — radiology-specific** | **PURCHASABLE**; free to practices that submitted data | **Price not displayed** on [rbma.org/ar](https://www.rbma.org/ar); most recent edition **2024**; past editions 2023/2021/2018/2017 |
| **RBMA Radiology Administrative Compensation Survey** | YES | Purchasable | **2022: member $325.00 / non-member $450.00** (verified on RBMA store); 2023 member $125.00 |
| **RBMA DataMAXX** benchmarking | YES | Paid tier | Contributing practices **$500/yr premium**; non-contributing **$500 basic / $1,000 premium** (figures via [Radiology Today](https://radiologytoday.net/archive/rt0814p14.shtml), **2014 vintage — likely stale**) |
| **HFMA MAP Keys** | **NO — no imaging/radiology keys exist** | Definitions public; **benchmark VALUES not public** (MAP App / MAP Award applicants only) | Not disclosed |
| **ACR practice management** | — | **NO published admin staffing benchmark found** | — |

Confidence on the paywall characterization: **High** (RBMA prices and HFMA key-list read directly).

**⚠️ FALSE-POSITIVE WARNING:** HFMA MAP Keys cost-to-collect (FM-6) includes "imaging" under HIM expenses — this means **document scanning/imaging**, NOT radiology. Do not mistake this for a radiology benchmark. Confidence **High**.

**Explicit known-unknowns:**
- **NO EVIDENCE FOUND** for FTEs per modality, FTEs per study volume, or FTEs per dollar of revenue for outpatient imaging administration, in any free public source.
- **NO EVIDENCE FOUND** for a freestanding/outpatient-imaging-center-specific administrative staffing benchmark anywhere.
- Where benchmarks exist they are at **"all physician practices"** or **hospital/health-system** level, not imaging. Confidence **High**.

## B2. Prior auth cost, cost to collect, A/R, denial and clean-claim rates

### CAQH Index — now the "DataSpring Index"; figures read directly from source PDFs

**⚠️ Rebrand:** CAQH Index → **DataSpring Index**. caqh.org/insights/index-report **301-redirects** to dataspring.com. Methodology stated unchanged. The **2025 Index is the 13th edition** (covering 2024 activity, released ~**2026-02-19**). Confidence **High**.

**Access change that matters:** the 2025 Index **now requires account registration**; Executive and Methodology reports free with an account, and **Index Pro is $899/user** (Interactive Chartbook, ROI Calculator, Ask the Index, 1-hr advisory). **I could not read the full 2025 per-transaction cost table** — it is rendered in charts, not extractable text, in the public slide deck. Confidence **High** on the access terms.

**2025 Index (13th ed.) figures I could verify from the official CAQH slide deck** ([CAQH 2026 eSolutions Xchange slides](https://s3.amazonaws.com/amo_hub_content/Association361/files/CAQH_2026%20eSolutions%20Xchange%20Slides.pdf), © 2026 CAQH):
- Prior authorization **medical cost savings opportunity: $461M**
- **15 minutes** — time medical providers save per prior auth using the **X12 278 standard** instead of fax/email/mail
- **$21 billion** total industry savings opportunity; **$258B** administrative cost avoided in 2024; **>600 organizations**, ~**63% of insured lives**
- Medical prior auth **electronic adoption 40%** (up from 31% in the 2023 Index)
Confidence **High** (official deck) / **Medium** for the adoption and $258B figures (press-release level).

**2024 CAQH Index — per-transaction costs read DIRECTLY from the official 80-page PDF** ([CAQH_IndexReport_2024_FINAL.pdf](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf)). Confidence **High**:

| Prior Authorization | Plan cost | **Provider cost** | Industry cost | Provider savings opp. |
|---|---|---|---|---|
| Manual | $3.41 | **$12.88** | $16.29 | $7.50 |
| Partial (portal/IVR) | $0.05 | **$8.93** | $8.98 | $3.55 |
| Electronic (X12 278) | $0.05 | **$5.38** | $5.43 | — |

Also from the same table — **eligibility & benefit verification** provider cost **$8.57 manual / $4.46 partial / $2.00 electronic**; **claim status inquiry** provider cost **$13.80 manual / $5.24 partial / $3.64 electronic**. Reported provider time: **24 minutes** per auth by phone/fax/email, **16 minutes** via plan portal; average time savings opportunity **14 minutes**. Electronic prior auth cost savings opportunity (2024 Index): **$515M** medical industry.

> **🔴 RESOLVES A CONFLICT IN CIRCULATING FIGURES.** Secondary sources variously quote manual/electronic prior auth as "$11.44 / $3.82," "$11.17 / $1.89," and "$8.03 / $2.65." **None matches the official 2024 table ($12.88 / $5.38 provider cost).** These are different editions, different cost bases (provider-only vs industry), or simply wrong. **Use the figures above with the edition named, or do not use them.** Confidence **High**.

### 🔴 CAQH has NO radiology or imaging breakout

I read the **CAQH *Administrative Transaction Costs by Provider Specialty*** brief (2023 Index) in full: **zero mentions of radiology or imaging**. It segments only **generalists / specialists / behavioralists**. Source: [CAQH specialty brief PDF](https://www.caqh.org/hubfs/CAQH%20Insights_2023%20Index%20Report_Provider%20Specialty%20Issue%20Brief_Final.pdf). Confidence **High**.

Closest usable proxy — **"specialists"**, read directly from that brief:
- Prior authorization, specialists: **manual $15.99**, partial $9.05, electronic $6.61 (behavioralists $18.35 / $11.18 / $6.83; generalists $11.00 / $6.94 / $4.47)
- Switching fully manual → electronic saves **specialists $8.51** and behavioralists $8.09 per transaction; specialist-vs-generalist gap **>$7**, one of the largest unit-cost differences in the brief
- Claim status inquiry, specialists: manual $7.40 partial / $5.40 electronic (generalists $6.20 / $3.15)

**Caveat to state in the pitch: CAQH/DataSpring is INDUSTRY SELF-REPORT.** Costs and times come from surveyed plans and provider organizations, not audited accounting. The brief is explicit that estimates were omitted for dental due to low response. **Label as self-reported industry estimate, and label "specialists" as a proxy for imaging, never as an imaging figure.** Confidence **High**.

### Days in A/R for radiology — one credible figure, one peer-reviewed historical anchor

- **Median ~31 days in A/R**, from the **2023 RBMA Accounts Receivable Survey (2022 data)**. Reported via [Radiology Business](https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/we-can-do-better-practices-leaving-money-table-2023-rbma-accounts-receivable-survey-shows) (direct fetch **HTTP 403**; figure from search extract, **not read in original**; **full survey is a paid RBMA product**). Confidence **Medium**. **This is the single most defensible radiology A/R benchmark located — and it is behind a paywall.**
- Peer-reviewed historical anchor: **2004 mean days charges in A/R 56.11 (professional component) and 55.54 (global)**, vs 2003's 63.74 and 77.33; median professional-component **adjusted collection percentage deteriorated 87.3% → 85.1%**; global-fee practices billing in house achieved mean ACP **91.2%** vs **79.4%** using a billing service. ⚠️ **RBMA surveyed members only, response rates 15% and 9%** — severe non-response bias, and authors note RBMA-member practices outperformed ACR-surveyed practices. *J Am Coll Radiol* 2005 Dec;2(12):1019-29, [PMID 17411986](https://pubmed.ncbi.nlm.nih.gov/17411986/). Confidence **High** on the publication, **Low** on 2026 applicability (**21 years old**).

### 🔴 Denial rate, clean claim rate, cost to collect — NO CREDIBLE IMAGING BENCHMARK FOUND

Every "2026 radiology benchmark" located is a **billing-vendor marketing blog**, and they **contradict each other irreconcilably**:

| Metric | Circulating claims | Assessment |
|---|---|---|
| Denial rate | "5–10%" · "below 5% best" · **"15.6%"** · "15–22%" | **3–4x spread. Unusable.** |
| Clean claim rate | "92.4% median" · "97%+ for diagnostic radiology" · "95%+ strong" | Contradictory |
| Days in A/R | "30–40 high performers" · "36.8 median" · "24–32 professional-only" | Contradictory |
| Cost to collect | "5–10% in-house / 3–7% outsourced" · "3.2¢ best-in-class / 5.4¢ average" | Contradictory |
| Net collection rate | "86.1%" vs "should be 96%+" | Contradictory |

I traced the most-cited of these (revenuesynergy.com 2026 benchmark report) to its methodology: **anonymized aggregate data from that vendor's own active client base — ~500 rendering providers, 22 specialty cohorts, no single client >4% of a cohort**, KPI definitions following **HFMA MAP Keys** where applicable, sanity-checked against MGMA DataDive and AAPC. Source: [revenuesynergy.com](https://www.revenuesynergy.com/resources/2026-benchmark-report.html). Confidence **High** on the methodology description.
> **This is one RCM vendor's own book of business, not an industry benchmark.** It is not a random or representative sample of imaging centers, and client selection is endogenous (practices that hire an RCM vendor differ systematically). **Cite it as "one RCM vendor's client-base median" or not at all.**

**Explicit known-unknown:** **NO EVIDENCE FOUND** for a methodologically sound, imaging-specific, publicly available denial rate, clean claim rate, or cost-to-collect benchmark. The credible candidates (RBMA A/R Survey, MGMA DataDive, HFMA MAP App) are **all paywalled**, and HFMA has **no imaging keys at all**. Confidence **High**.

## B3. Total administrative cost per imaging study or per encounter

**NO EVIDENCE FOUND.** No published total administrative cost per imaging study or per imaging encounter was located in any free public source. Confidence **High**.

- PubMed `administrative cost per imaging study` returned COUNT: 116, but inspection showed **none** addressing per-study administrative cost for outpatient imaging.
- The nearest constructible proxy is **summing CAQH per-transaction provider costs** across the transactions one study triggers (eligibility verification + prior auth + claim submission + claim status + payment). **⚠️ If the pitch does this, it must be labeled a BUILT ESTIMATE, not a published benchmark**, and must disclose: CAQH is self-report; figures are "specialist" or all-industry, not imaging; transaction counts per study are assumed; and it omits scheduling, protocoling, order chasing, report distribution, and denial rework entirely. Confidence that no published figure exists: **High**.

---

# WHAT I COULD NOT VERIFY, AND WHY

### Paywalled / registration-gated
| Item | Barrier |
|---|---|
| **RBMA A/R Survey 2024** (full radiology A/R, write-offs, bad debt recovery, billing/collection cost) | Paid RBMA product; **price not displayed**. The ~31-day median is secondhand |
| **RBMA DataMAXX** benchmarking | Paid tiers ($500–$1,000/yr, 2014-era pricing) |
| **RBMA Practice Management Survey** | Could not confirm a current edition exists under that exact name; store shows Compensation and A/R surveys |
| **MGMA DataDive Cost & Revenue / Financials & Operations** | Membership from $399/yr **plus** dataset purchase; **dataset pricing not public — quote required** |
| **2025 DataSpring (CAQH) Index full report** | Registration required; **Index Pro $899/user**; per-transaction cost table rendered as charts, not extractable |
| **HFMA MAP Keys benchmark VALUES** | Definitions public, values restricted to MAP App / MAP Award applicants; **and no imaging keys exist regardless** |

### Blocked by HTTP 403 / anti-bot (figures taken from search extracts, NOT read in original)
- Radiology Business (multiple articles — MGMA radiology staffing figures; 2023 RBMA A/R coverage; cost-is-king coverage)
- AJR Online (`ajronline.org`) — *Customer Service and Satisfaction in Radiology*; could not verify the **"71% of referring physicians send patients to multiple facilities"** claim → **treat as UNVERIFIED**
- ScienceDirect — protocol-automation systematic review (the "84–98% accuracy" and **"6% of radiologist time"** figures are **UNVERIFIED**; do not cite without reading the original)
- HealthLeaders Media, Fierce Healthcare, GlobeNewswire (2025 CAQH Index release)
- jointcommission.org main standards page (403) — **worked around by reading the official program PDFs directly, which is a stronger source anyway**

### Technically blocked, successfully worked around
- **PubMed web fetch is cookie-blocked.** All abstracts in this report were retrieved via the **NCBI eutils API** (`efetch`/`esearch`), per the brief. This worked reliably.
- **Joint Commission and ACR PDFs** returned unreadable compressed binary to the fetch tool; resolved by downloading and running **`pdftotext -layout`** locally. All TJC and ACR quotations here are from locally extracted official PDFs.

### Not published / not at this granularity (genuine known-unknowns)
1. **Evidence that TAT or referrer communication changes referral VOLUME** — does not exist in published literature. Multiple PubMed queries returned COUNT: 0. **This is the single most important gap and it invalidates a volume-based pitch claim.**
2. **US outpatient radiology order-incompleteness rate** — the strong RI-RADS evidence is Saudi, Moroccan, and Turkish. No US figure found.
3. **Imaging-specific admin staffing benchmarks** (FTE per modality / per study volume / per revenue) — not public anywhere; the one radiology figure has **n=11**.
4. **Radiology/imaging breakout in CAQH** — confirmed absent; only generalist/specialist/behavioralist.
5. **Total administrative cost per imaging study** — no published figure.
6. **Measured closed-loop critical-results outcomes at a US outpatient imaging center** — none; best evidence is a UK ED QI project (n=100).
7. **Any peer-reviewed or independently measured outcome for referral-intake automation** — zero across 11 vendors; no case study names a freestanding outpatient imaging center.
8. **Any independently measured outcome for referrer analytics/scorecard products** — none found in the entire category.
9. **Fax share of imaging referrals** — no primary source exists; the "56%" is unattributed vendor content.
10. **eRAD**: whether "send electronic orders from any application" is structured RIS order entry or document transmission — **UNRESOLVED** (page truncated).
11. **Sectra CPOE with ACR Appropriateness Criteria** — only source is **2011**; current product state **unverified**.
12. **ACR Actionable Reporting Work Group published comments** (*JACR* 2014;11(9):924-5 and 925-6) — not retrieved; may contain dissent from the three-category framework.

### Source-brief errors identified
- **Analogic** has no referrer-analytics product — it is imaging hardware/OEM.
- **Orby AI** is not a healthcare vendor (general enterprise RPA, acquired by Uniphore).
- **Medicom Health** is hospital-marketing health risk assessments, divested to Eruptr in 2021 — not order intake.
- **Tennr's** radiology positioning is **trade-press framing its own materials do not support**.
- **"NPSG.02.03.01"** is the **Laboratory** program identifier; hospitals use **NPG.01.02.01** as of 2026, and **Ambulatory Health Care has no critical-results goal at all**.
