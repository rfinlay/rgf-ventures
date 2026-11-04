# RIS / PACS / Dictation / RCM Landscape for a New El Paso Outpatient Imaging Center

Prepared by Sherlock, 2026-11-03, for Rick (Phase 2 vendor selection). Context: single site, MRI signed, CT likely, opening about June 2027, 1 to 3 radiologists, Medicare / MA / commercial / TRICARE.

**Confidence key:** HIGH = primary source or KLAS published result read today. MEDIUM = consistent across independent secondary sources or long-standing industry knowledge. LOW = my working knowledge, not re-verified today; confirm in RFP. **[MKT]** = vendor marketing claim, not independently verified.

**Method limits, stated plainly:** KLAS segment detail pages (scores, sample sizes) sit behind a paywall, so I used the published 2026 Best in KLAS winner list (via HIT Consultant, Feb 4 2026) plus vendor pages. Almost no vendor in this market publishes list pricing; every price below is a range to validate in quotes, not a fact. One search provider failed late in the session, so Optum's current radiology product status is LOW confidence.

---

## Page 1: Plain-English Summary

1. **The big-hospital KLAS winners are the wrong yardstick.** 2026 Best in KLAS went to Sectra (PACS over 300K studies) and Agfa Enterprise Imaging (PACS under 300K studies). HIGH. But "small" in KLAS means up to 300,000 studies a year, which is a community hospital. A single MRI/CT center does roughly 8,000 to 20,000 studies a year. Neither Sectra nor Agfa is built or priced for that. KLAS does not run a separate "imaging center RIS/PACS" award, so you need KLAS's lower-volume vendor data plus reference calls.

2. **For a center this size, the real buy is an integrated RIS + PACS (+ optional billing) on one database, cloud-hosted, priced per study.** That removes the most expensive and fragile part of a small center: the interface between a separate RIS and PACS. The vendors that actually sell this to independent centers are **Konica Minolta Exa PACS|RIS**, **RamSoft (PowerServer / OmegaAI)**, **Novarad**, and **Intelerad (InteleOne/InteleRIS, plus Ambra cloud)**. MEDIUM.

3. **Dictation: the market changed hands.** PowerScribe One is now Microsoft. Fluency for Imaging left Solventum (ex-3M) and was combined with Smart Reporting into a new company, **Jacobian**, closed end of December 2025; Fluency won 2026 Best in KLAS for imaging speech recognition. HIGH. For 1 to 3 radiologists, the cheapest clean path is often the **RIS's built-in dictation** or a cloud reporting product. Ask the radiologist group what they already use before you choose; if they read for other sites, they will want their own tool.

4. **Billing: outsource it at opening.** A new center with no billing staff and a TRICARE/MA mix should use a radiology-specialized RCM firm (percent of collections) on top of the RIS's billing module or the RCM firm's own system. Keep the clearinghouse and the data in your name.

5. **Interface fees are the hidden cost.** Expect per-interface charges for HL7 orders/results, referrer EHR links, billing feeds, and the dictation link. Negotiate them into the base price, cap future ones, and write data export at the end of contract into the agreement at no or fixed cost.

6. **Recommended shortlist (for RFP, not a decision):** Konica Minolta Exa PACS|RIS, RamSoft OmegaAI, Novarad, Intelerad. One alternate if the radiologists insist on a premium viewer: Visage or Sectra PACS paired with a separate RIS, at a higher cost.

### Comparison Table

| Vendor / product | Deployment | Integrated RIS + PACS + billing? | 2026 KLAS signal | Best-fit size | Pricing model (to verify) | Notes / flags |
|---|---|---|---|---|---|---|
| Konica Minolta Exa PACS\|RIS | On-prem server or cloud | RIS + PACS single database [MKT, but consistent with users]; billing module available | No segment award; KLAS rates Exa PACS | Single site to multi-site outpatient, ortho | Modular license or per-study | Strong imaging-center footprint; ask about Exa Billing maturity. MEDIUM |
| RamSoft PowerServer / OmegaAI | OmegaAI cloud-native; PowerServer on-prem/hybrid | RIS + PACS; billing via partners | No award | Small to midsize outpatient, 800+ practices claimed [MKT] | Subscription / usage-based | Cloud-native is real advantage for no-IT-staff owners; check maturity of OmegaAI vs PowerServer. MEDIUM |
| Novarad (NovaPACS / NovaRIS) | On-prem, hybrid, cloud | RIS + PACS | No award | Small hospitals, imaging centers | Quote | Historically good value and service; smaller company, check roadmap. LOW to MEDIUM |
| Intelerad (InteleOne, InteleRIS, Ambra) | On-prem, hybrid; Ambra cloud | RIS + PACS (InteleRIS); billing not core | 2026 KLAS UK/Ireland PACS winner (InSight); no US award | Outpatient groups, teleradiology | Per-study common | Large private-equity-owned roll-up of many products; ask which code base you get. MEDIUM |
| Fujifilm Synapse (PACS, RIS) | On-prem, hybrid, cloud | Separate products | Strong in VNA historically | Hospitals, larger groups | Quote | Good data portability reputation; likely oversized. MEDIUM |
| Sectra PACS | On-prem, Sectra One Cloud (Azure) | PACS only; RIS from partner | 2026 Best in KLAS PACS large (13 yrs US #1) | Large hospitals | Per-study or license | Excellent but priced and staffed for large buyers. HIGH (award) |
| Agfa Enterprise Imaging | On-prem, cloud-enabled | PACS + VNA + viewer | 2026 Best in KLAS PACS small, VNA, universal viewer | Hospitals up to 300K studies | Quote | "Small" here is still hospital scale. HIGH (award) |
| Merge (Merative) | On-prem, cloud | PACS, RIS | Recognized | Epic-integrated systems | Quote | Fit is health systems on Epic. MEDIUM |
| GE HealthCare (True PACS / Centricity legacy) | Hybrid | PACS; RIS legacy | Largest install base | Hospitals | Quote | Not an imaging-center first choice. MEDIUM |
| Philips (HealthSuite Imaging) | Cloud (AWS) | PACS | No award | Systems | Subscription | Philips has narrowed its IT portfolio; confirm commitment. LOW |
| Optum (ex-Change Healthcare Radiology) | On-prem, cloud | PACS, RIS, cardiology | No award | Hospitals | Quote | Product status after 2024 cyberattack and reorganizations unclear. LOW, verify |
| Candelis ImageGrid | Appliance, cloud | PACS, light RIS | Niche | Very small sites | Low entry cost | Worth a look only as a budget floor. LOW |

---

## 1. RIS / PACS Detail

### What actually matters for this center
- **Volume:** one MRI (plus likely CT, possibly X-ray/US later). Realistic year-one volume is in the thousands to low tens of thousands of studies. Per-study pricing scales with ramp-up, which protects cash in year one. MEDIUM.
- **No IT department.** Cloud or vendor-hosted removes server rooms, backups, patching, and disaster recovery from the owners. Security responsibility shifts to the vendor contract (BAA, SOC 2 Type II, HITRUST if available, breach notice terms).
- **Single database RIS+PACS** removes the RIS-to-PACS HL7 interface entirely and keeps scheduling, exam status, images, and reports consistent.
- **Referrer access:** a web portal for referring physicians and patient image sharing matters more to a new center's growth than any viewer feature.

### Vendor notes
- **Konica Minolta Exa PACS|RIS.** Vendor states single-database RIS+PACS that "scales from a single facility to an enterprise" and includes a performance dashboard tracking exam volume, radiologist performance, and referrer ordering [MKT, HIGH that the claim is published] (healthcare.konicaminolta.us). Independent secondary review places Exa as a fit for imaging centers and orthopedic groups with modular licensing (pacscribe.com, Jul 2026; note: that site sells a competing PACS). Konica Minolta also sells modalities (DR), so watch for bundling pressure.
- **RamSoft.** Markets cloud PACS, RIS and VNA "in one AI-driven platform," "800+ practices in 30+ countries" [MKT] (ramsoft.com). Secondary review describes OmegaAI as cloud-native with usage-based subscription. Long history in independent outpatient centers. MEDIUM.
- **Intelerad.** Owns InteleOne/InteleViewer, InteleRIS, Ambra (cloud image exchange and PACS), and others from acquisitions. Won the 2026 KLAS UK/Ireland PACS segment with InSight PACS (Insignia acquisition) (HIGH). Ask which product line is strategic in the US and the roadmap for the one you would buy.
- **Novarad.** Utah-based, sells RIS/PACS to small hospitals and outpatient centers. LOW to MEDIUM; verify current ownership and KLAS data in Phase 2.
- **Sectra / Agfa.** Award winners, verified (HIGH), but sized for hospitals. Sectra's own page confirms 7 Best in KLAS awards in 2026 and 13 consecutive US years at #1 (medical.sectra.com). The independent secondary source says Sectra is "too much system for small imaging centers" (MEDIUM).

### Lock-in and data export
- Insist on: full DICOM export of all images, reports in HL7/PDF/structured form, RIS data (patients, orders, schedules, billing history) in a documented format, at a fixed price, within a stated time after termination. MEDIUM (standard contract practice).
- Images stored in proprietary compressed formats can cost real money to migrate later. Ask whether the archive stores native DICOM. MEDIUM.
- The federal information blocking rules (21st Century Cures Act, ONC/ASTP HTI rules) restrict practices that block access to electronic health information, and they apply to certified health IT developers. Many RIS/PACS vendors are not ONC-certified, so do not rely on the rule; rely on the contract. MEDIUM; confirm with counsel.

### API openness
- Ask for: DICOMweb (QIDO/WADO/STOW), HL7 v2, FHIR R4 endpoints, and documented REST APIs, and whether API access costs extra. This matters directly for RadAssist integration and owner reporting. MEDIUM.

---

## 2. Voice Recognition / Dictation

| Product | Owner (2026) | Notes | Confidence |
|---|---|---|---|
| PowerScribe One | Microsoft (Nuance) | Cloud reporting, speech, structured reporting, quality tools (learn.microsoft.com). Dominant US share; a secondary site cites about 80% of US radiologists [unverified]. Expensive for 1 to 3 rads; per-radiologist subscription typical. | HIGH ownership, LOW share figure |
| Fluency for Imaging | Jacobian (Fluency + Smart Reporting; close completed end of Dec 2025) | 2026 Best in KLAS, Speech Recognition Front-End Imaging. Formerly 3M, then Solventum. | HIGH |
| Rad AI (Omni reporting, Impressions) | Rad AI | Launched its own speech recognition Dec 1 2025 [MKT]; historically ran alongside PowerScribe. | MEDIUM |
| RIS built-in dictation | Exa, RamSoft, Intelerad, others | Often uses a licensed speech engine; cheapest and no interface. Quality varies; demo with your radiologists. | MEDIUM |
| Others: DeepHealth, Sirona, New Lantern, RadPair | Various | DeepHealth is owned by RadNet, an imaging operator that could be a local competitor; consider that when sharing data. | MEDIUM |

**Rule:** the reading radiologists choose the dictation tool, the owners choose the contract. If the group is contracted (not employed), they may already carry PowerScribe or Fluency licenses and only need an integration.

**Integration:** reporting systems typically integrate with the RIS by HL7 (orders in, reports out) and with PACS by a desktop context link. Each link is a likely interface fee.

---

## 3. Billing / RCM and Clearinghouse

- **Model:** at opening, outsource to an imaging-specialized RCM company, typically paid a percentage of net collections (commonly mid-single-digit percent for technical-component imaging billing; LOW, get three quotes). Keep a short contract (12 to 24 months), data ownership in your name, and clear handover terms.
- **System:** either the RIS's billing module (Exa Billing, RamSoft partners) or the RCM firm's own platform fed by an HL7 charge interface.
- **Clearinghouses commonly used:** Waystar, Availity, Trizetto (Cognizant), Office Ally for small practices, Quadax (2026 Best in KLAS, Claims Management and Clearinghouse, HIGH). Change Healthcare was the largest until its February 2024 cyberattack outage, which is a useful lesson: have a second clearinghouse path documented.
- **Payer specifics to test in the RFP:** TRICARE (Humana Military is the East Region contractor; El Paso and Fort Bliss sit in the TRICARE West Region, administered by TriWest from January 2025; verify current), Medicare MAC for Texas (Novitas JH), prior authorization workflows for MA and commercial (RBM vendors such as Evolent, Carelon), and the CMS Appropriate Use Criteria program, which CMS paused and then rescinded in the CY2024 rule (MEDIUM; confirm nothing new for 2027).

---

## 4. Interface (HL7/DICOM) Fees

**What is customary (MEDIUM; ranges are LOW, confirm by quote):**
- One-time build fee per HL7 interface (common ranges are low thousands to tens of thousands of dollars), plus annual maintenance often around 15 to 20 percent of the license or interface fee.
- DICOM modality connections are usually included or cheap; HL7 interfaces (ADT, orders, results, charges) and EHR-specific connections (Epic, athena, eClinicalWorks for referrers) are where fees pile up.
- Some vendors charge both sides (RIS vendor and the receiving system each bill).

**What to negotiate:**
1. A defined list of included interfaces in the base price: modality worklist and DICOM for every modality, dictation link, billing/charge feed, referrer portal, one HIE or EHR link.
2. A capped price for each future interface, fixed for the term.
3. No charge for interface upgrades caused by the vendor's own version changes.
4. Exit terms: data export format, price, and timeline written in.
5. API access included, not a premium module.
6. Uptime SLA with service credits, and a security addendum (BAA, breach notice in hours not days, cyber insurance on the vendor).

---

## 5. Shortlist and Evaluation Criteria

### Shortlist (RFP invite list)
1. **Konica Minolta Exa PACS|RIS**: integrated single database, imaging-center fit, optional billing. Watch modality bundling.
2. **RamSoft OmegaAI**: cloud-native, subscription, independent-center focus. Verify product maturity with reference sites of similar size.
3. **Novarad**: value option with RIS+PACS. Verify company stability.
4. **Intelerad**: breadth and cloud image sharing (Ambra). Verify which product line and support model.

Alternate: Sectra or Visage viewer with separate RIS if the radiologists demand a premium reading experience and owners accept the cost and an extra interface.

**Why:** a lean, no-IT-staff, single-site owner group needs one vendor, one database, hosted, priced to volume, with export rights. The award winners solve a different problem (enterprise scale).

### Evaluation criteria (suggested weights)
| Criterion | Weight |
|---|---|
| Radiologist reading experience (hands-on demo with your rads, MRI and CT cases) | 20% |
| Total 5-year cost, including interfaces, storage growth, and dictation | 20% |
| Integrated RIS/PACS/billing workflow, front desk to claim | 15% |
| Security and hosting (SOC 2 Type II, BAA, backup and disaster recovery, uptime SLA) | 15% |
| Data ownership, export terms, API openness (DICOMweb, FHIR, HL7) | 10% |
| Reference checks with 2 or 3 single-site centers of similar volume | 10% |
| Implementation timeline vs June 2027 opening, training, support responsiveness | 10% |

**Timeline note:** to open June 2027, contract by about February 2027 leaves room for build, interface testing, modality connection, and staff training. MEDIUM (typical 3 to 5 month implementations for cloud single-site; vendors will quote shorter).

### Marketing vs verified
- Verified: 2026 Best in KLAS winners listed above; Jacobian ownership of Fluency and Dec 2025 close; Microsoft ownership of PowerScribe One.
- Marketing only: RamSoft "800+ practices"; Exa "scales to enterprise" and single-database claims; Rad AI speech recognition "dramatically improves" accuracy; PowerScribe "80% of radiologists"; any "AI" claims in RIS/PACS.

---

## Citations
1. KLAS, 2026 Best in KLAS Awards, Software and Services: https://klasresearch.com/report/2026-best-in-klas-awards-software-and-services/3906 (winner list as reported by HIT Consultant, Feb 4 2026: https://hitconsultant.net/2026/02/04/2026-best-in-klas-winners-full-list-software-services/)
2. Sectra, Best in KLAS page: https://medical.sectra.com/about-sectra/sectra-pacs-best-in-klas/
3. Jacobian, closing announcement: https://www.jacobian.com/news/jacobian-announces-successful-closing ; acquisition announcement Oct 23 2025: https://www.prfire.com/news-releases/smart-reporting-set-to-acquire-fluency-for-imaging-to-create-jacobian/ ; Signify Research analysis: https://www.signifyresearch.net/signify-premium-insights/spi-medical-imaging-jacobian-unites-speech-and-structure-in-radiology-reporting/
4. Microsoft PowerScribe One documentation: https://learn.microsoft.com/en-us/industry/healthcare/powerscribe-one/
5. Rad AI speech recognition launch, Dec 1 2025: https://www.radai.com/news/rad-ai-unveils-next-generation-speech-recognition-that-redefines-radiology-reporting
6. Konica Minolta Exa PACS|RIS: https://healthcare.konicaminolta.us/healthcare-it/exa-pacsris
7. RamSoft: https://www.ramsoft.com/
8. PACScribe, "13 Best PACS Systems for Radiology in 2026" (Jul 27 2026; competitor-authored, use with caution): https://pacscribe.com/blogs/13-best-pacs-systems-for-radiology-in-2026/
9. Radiological.ai vendor ownership map 2026 (secondary): https://radiological.ai/blog/who-owns-radiology-reporting-software

## Open items for Phase 2
- Buy the KLAS imaging-center or ambulatory RIS/PACS segment data, or ask vendors for their KLAS scores with sample sizes.
- Confirm Optum radiology product status, Novarad ownership, and TRICARE West contractor.
- Ask the radiologist group which dictation they already license.
