# Systems Gap Audit: Everything an Independent MRI + CT Center Needs at Opening

Prepared by Sherlock, 2026-11-03, for Rick. Scope: one independent outpatient center, MRI plus CT, 1 to 3 radiologists, El Paso TX, opening about June 2027. Compared against: AUTOMATION-CANDIDATES.md (#1 to #14, RIS/PACS position, Phase 2 system list), the 2026-11-05 deck (scorecard, Phase 2 line, architecture), REVIEW-CHANGES-2026-11-02.md R9 to R20, and SHERLOCK-RIS-PACS-LANDSCAPE-2026-11-03.md.

**Confidence key.** HIGH = rule or standard I can name to the section and am confident of its current text. MEDIUM = standard practice or a requirement I know well but did not re-read today. VERIFY = real, but the current text or effective date must be confirmed in Phase 1 before anyone quotes it. Sources are named so Phase 1 can pull them; none were re-fetched today (method limit, stated plainly).

---

## Plain-English summary

1. **The plan covers the business systems well and the clinical-compliance systems thinly.** RIS, PACS, dictation, billing, clearinghouse, phones, prior auth, portal, fax, modality integration, reading workstations and IT/security are all on the Phase 2 list (R9). What is missing is the layer accreditation and licensing inspect: CT dose tracking, MRI safety screening, contrast and injector records, critical results communication, radiologist peer review, and the accreditation binder itself. None of these is a big build. All of them are things the ACR or Texas DSHS will ask to see, and Medicare will not pay for MRI or CT until ACR (or IAC or Joint Commission) accreditation is in hand.
2. **Voice recognition and patient phones are two different systems, and the plan should say so everywhere.** (a) Radiologist voice recognition (dictation: PowerScribe One, Fluency, or the RIS's built-in tool) is a clinical reporting tool, chosen in Phase 2, and it is where RadAssist plugs in. (b) The patient phone system (call routing, hold queues, recording, the Spanish menu, optionally an AI voice agent for scheduling calls and reminders) is a front-office system. The current docs say "phones" and "dictation" separately, which is right; the deck scorecard row #9 "Inbound patient voice" should never be shortened to "voice" next to dictation.
3. **Enrollment and credentialing is the longest lead item and it is not on any list.** Medicare IDTF enrollment (CMS-855B with a site visit), Texas Medicaid, TRICARE, every commercial payer, and radiologist credentialing (CAQH) commonly take 90 to 180 days. If it starts in May, the center opens unable to bill. It needs an owner and a start date in Phase 1, even if a credentialing service does the work.
4. **Several small items will bite on day one:** No Surprises Act good-faith estimates for self-pay patients, point-of-care creatinine testing (needs a CLIA certificate of waiver), CD burn and import, a patient payment terminal, and after-hours reading coverage.
5. **Nothing here changes the $45,000.** Most gaps are Buy (inside the RIS, or a small vendor) and belong on the Phase 2 selection list or the Phase 1 opening checklist. Two are worth adding as Integrate items: dose monitoring and enrollment tracking. None should be added as a Rick build.

### MISSING or PARTIAL, ranked by importance at opening

| Rank | Item | Status | Why it ranks here |
|---|---|---|---|
| 1 | Payer enrollment and radiologist credentialing (855B IDTF, Texas Medicaid, TRICARE, commercial, CAQH) | MISSING | No enrollment, no revenue. Longest lead time of anything on this list. |
| 2 | Accreditation program and documentation (ACR MRI and CT) | MISSING | Medicare requires accreditation for MRI and CT technical billing; the clock (submit images after go-live) affects cash flow. |
| 3 | CT dose monitoring and registry (DIR) | MISSING | ACR CT accreditation and Texas rules expect dose records and protocol review. |
| 4 | MRI safety screening and zone control | MISSING | ACR MR accreditation requires written safety policy, screening, named MR safety roles. Patient-harm risk. |
| 5 | Radiologist peer review and QA | MISSING | ACR accreditation requires a physician peer review program. |
| 6 | Critical results communication and tracking | PARTIAL | Named only as "critical results called" inside #12. Needs a logged, closed-loop workflow. |
| 7 | Texas DSHS CT registration, shielding, physicist surveys, operator credential records | MISSING | Cannot operate CT without registration; inspection item. |
| 8 | Contrast and injector records, reaction kit, point-of-care creatinine (CLIA waiver) | MISSING | Inspection and patient-safety item; CLIA certificate needed before the first fingerstick. |
| 9 | Good-faith estimates (No Surprises Act) and patient payment/POS | MISSING | Federal requirement for self-pay patients; front desk cannot collect copays without a terminal. |
| 10 | Teleradiology / after-hours and overflow reading | MISSING | 1 to 3 radiologists means vacations and sick days; a plan is needed day one. |
| 11 | Image exchange: CD burn and import, cloud image share | PARTIAL | #7 covers inbound priors; outbound CDs for patients and referrers are not named. |
| 12 | Compliance training (HIPAA, HB 300), policies, incident response plan | PARTIAL | HB 300 is analyzed for Rick personally; the center's own staff training system and IR plan are not listed. |
| 13 | Identity, MFA, endpoint/MDM, Wi-Fi, firewall, security monitoring | PARTIAL | Folded into "IT infrastructure, security and backup"; needs to be itemized so it gets selected and priced. |
| 14 | Physical security: badging, cameras, MRI Zone III/IV access control | MISSING | MR safety and HIPAA physical safeguards both depend on it. |
| 15 | Equipment service contracts and uptime monitoring | MISSING | MRI and CT service contracts are large and negotiated with the purchase. |
| 16 | HR, payroll, staff scheduling, staff credential tracking (ARRT, BLS, TMB MRT) | MISSING | Ordinary business system, but credential expiry tracking is an inspection item. |
| 17 | Coding and charge capture | PARTIAL | Implied by billing/RCM; no one is named as owning CPT/ICD-10 coding and charge reconciliation. |
| 18 | Email / M365, business productivity | MISSING | Trivial but needs a BAA and must be set up before staff are hired. |
| 19 | Inventory and supply (contrast, IV supplies, linens) | MISSING | Small; often a spreadsheet at opening. "Inventory management" is already in the FDA exclusion text the docs cite. |
| 20 | HIE / TEFCA connection | PARTIAL | TEFCA is mentioned; no decision on whether the center joins an HIE at opening. Optional at opening. |
| 21 | Referrer EHR integration | PARTIAL | Report delivery is covered (#12); order intake from referrer EHRs (e-orders vs fax) is not specified. |

---

## Full inventory

Phase key: P1 Discovery and Requirements, P2 Vendor Selection, P3 Design, P4 Build, P5 Test and Go-live. "Opening checklist" means a pre-opening operational task that is not a system selection; it should appear in the P1 requirements as an owner-assigned item, not as Rick's build.

### A. Clinical imaging core

| System | What it does | Covered? | Buy / build / integrate | Phase | Source |
|---|---|---|---|---|---|
| RIS | Orders, scheduling, registration, exam status, reporting workflow | COVERED (P2 list, one cloud RIS+PACS position) | Buy, integrated with PACS | P2 | Plan; RIS/PACS landscape |
| PACS (storage, viewer, worklist) | Stores and displays images; radiologist worklist | COVERED | Buy, same vendor as RIS | P2 | Plan |
| VNA / long-term archive | Vendor-neutral copy of images for retention and migration | PARTIAL (export terms #3; no archive decision) | Buy: confirm the cloud PACS stores native DICOM with a second copy; separate VNA not needed at one site | P2 | Texas medical record retention (22 TAC 165.1, 7 years adults, longer for minors), MEDIUM; contract terms #3 |
| Modality worklist (DICOM MWL) and MPPS | Pushes patient and order to the scanner; no retyping | COVERED (modality integration on P2 list) | Integrate; test during scanner install | P2, P5 | DICOM PS3.4; plan |
| Radiologist voice recognition / dictation | Clinical reporting: speech to text, templates, sign-off (PowerScribe One, Fluency, RIS built-in) | COVERED (R9, R10; landscape section 2) | Buy; RadAssist interfaces to it | P2 | Landscape doc |
| Reading workstations and diagnostic displays | Calibrated monitors for diagnosis, home reading setups | COVERED (P2 list) | Buy; include DICOM GSDF calibration | P2 | ACR-AAPM-SIIM Technical Standard for Electronic Practice of Medical Imaging, MEDIUM |
| Report assistance (RadAssist) | Structured drafting the radiologist signs | COVERED (#14) | Build (existing product) | P2 spec | Plan |
| CT dose monitoring and ACR Dose Index Registry | Captures dose per exam (RDSR), flags outliers, submits to DIR, supports protocol review | MISSING | Buy or integrate (vendor dose tool or PACS module; DIR participation through ACR NRDR) | P2 select, P5 live | ACR CT Accreditation Program requirements (dose index review, physicist annual survey), HIGH; Joint Commission diagnostic imaging standards on CT dose recording, MEDIUM; 25 TAC 289.227, VERIFY current CT dose provisions |
| MRI safety screening and zone control | Patient and staff screening forms, implant lookup, Zone III/IV access, ferromagnetic detection | MISSING | Buy (screening inside RIS intake or e-form vendor; implant reference subscription); physical access via badging | P2, P5 | ACR Manual on MR Safety (2024); ACR MR Accreditation requires an MR safety policy and named MR Medical Director / MR Safety Officer roles, HIGH |
| Contrast and power injector records | Logs agent, lot, dose, reactions; injector integration | MISSING | Buy (RIS or PACS fields; injector data via DICOM where supported) | P2 | ACR Manual on Contrast Media, HIGH as a reference standard |
| Point-of-care creatinine / eGFR | Kidney function check before contrast when no recent lab | MISSING | Buy device; obtain CLIA certificate of waiver | Opening checklist (P1 owner) | 42 CFR Part 493 (CLIA), HIGH that any patient testing requires a certificate |
| Critical results communication | Closed-loop notice of urgent findings to referrer, with log and escalation | PARTIAL (#12 says "critical results called") | Buy (RIS/PACS or dictation module); require audit log | P2 | ACR Practice Parameter for Communication of Diagnostic Imaging Findings, HIGH; Joint Commission NPSG.02.03.01, MEDIUM |
| Peer review and QA | Random double reads, discrepancy scoring, radiologist QA reports | MISSING | Buy (PACS module or ACR RADPEER) | P2, live at opening | ACR accreditation requires a physician peer review program, HIGH |
| Teleradiology / after-hours and overflow | Coverage when the 1 to 3 radiologists are out | MISSING | Buy a teleradiology contract; PACS must support external readers | P2 | Operational necessity; credentialing applies to every reader, MEDIUM |
| Clinical decision support / AUC | Appropriate-use checks at order time | NOT NEEDED (correctly declined, #13) | Decline | n/a | CMS AUC program was paused and its regulations rescinded in the CY2024 PFS final rule, MEDIUM, VERIFY no revival |

### B. Patient access and front office

| System | What it does | Covered? | Buy / build / integrate | Phase | Source |
|---|---|---|---|---|---|
| Scheduling and reminders | Booking, confirmations, TCPA-capped reminders, Spanish | COVERED (#8, inside RIS) | Buy | P2 | Plan; 47 CFR 64.1200(a)(9)(iv) |
| Cancellation backfill | Fills freed slots from a waitlist | COVERED (#5) | Build | P3, P4 | Plan |
| Patient portal, intake, consent, e-signature | Pre-registration, history, MRI screening form, consents, results access | COVERED (P2 list, #8) | Buy (RIS portal); confirm e-signature meets the Texas UETA (Bus. and Com. Code ch. 322) | P2 | Plan; UETA, MEDIUM |
| Patient phone system (telephony) | Lines, call routing, queues, recording, Spanish menu, after-hours message | COVERED ("phones" on P2 list) | Buy cloud phone system with a BAA | P2 | Plan; HIPAA BAA, 45 CFR 164.502(e) |
| Patient IVR / AI voice answering | Automated answering for scheduling and status calls; distinct from dictation | COVERED as optional (#9, Integrate, "phase two, if at all") | Integrate a vendor, or defer | After opening | Plan; FCC 24-17; TRAIGA HB 149, VERIFY scope |
| Good-faith estimates (No Surprises Act) | Written estimate for uninsured and self-pay patients within set deadlines | MISSING | Buy (RIS or RCM feature, or estimate tool) | P2 | 45 CFR 149.610, HIGH |
| Patient payment / POS | Card terminal, copay and self-pay collection, payment plans, receipts | MISSING | Buy (RCM vendor's or RIS-integrated processor); PCI DSS scope | P2 | PCI DSS v4.0, HIGH that it applies to card acceptance |
| Itemized bills before collection | Texas requires an itemized bill before sending a patient to collections | MISSING | Buy (RCM vendor configuration) | P2 | Texas SB 490 (2025), VERIFY effective date and scope for IDTFs |
| Eligibility verification | 270/271 at scheduling | COVERED (#2) | Build with #1 | P3, P4 | Plan |
| Prior authorization | Detect, assemble, submit, track, appeal | COVERED (#1) | Build | P3 to P5 | Plan |
| Language access | Interpreter line, translated forms and notices | MISSING | Buy an interpreter phone service; translated taglines | Opening checklist | ACA Section 1557, 45 CFR 92.11, HIGH for Medicare-participating providers |

### C. Revenue cycle and enrollment

| System | What it does | Covered? | Buy / build / integrate | Phase | Source |
|---|---|---|---|---|---|
| Billing / RCM | Claims, denials, payment posting, A/R | COVERED (P2 list; outsource recommended) | Buy RCM firm | P2 | Landscape doc |
| Clearinghouse | Routes 837/835/270/271/278 | COVERED (P2 list) | Buy, in the center's name | P2 | Plan |
| Coding and charge capture | CPT/ICD-10 coding from the signed report; reconciles exams to charges | PARTIAL (implied by RCM) | Buy (RCM firm codes); owner reporting (#4) reconciles exams vs charges | P2 | MEDIUM |
| Medicare IDTF enrollment | CMS-855B, supervising physician, site visit, IDTF performance standards | MISSING | Buy a credentialing service or assign an owner; start early | P1 start | 42 CFR 410.33 (IDTF standards: supervising physician, liability insurance, signage, complaint log, equipment calibration records), HIGH |
| Accreditation for Medicare billing | ACR MRI and CT accreditation (or IAC, TJC) | MISSING | Buy (ACR application; physicist; image submission after go-live) | P1 plan, P5 submit | MIPPA, 42 CFR 414.68, HIGH |
| Texas Medicaid, TRICARE, commercial enrollment | Payer contracts and enrollment | MISSING | Buy credentialing service | P1 start | TMHP; TRICARE West, MEDIUM |
| Radiologist credentialing | CAQH profiles, payer credentialing, privileges file | MISSING | Buy; track expirations | P1 start | MEDIUM |
| NPI and taxonomy | Organization NPI for the IDTF | MISSING (verify done) | Opening checklist | P1 | NPPES, HIGH |

### D. Communication, records and interoperability

| System | What it does | Covered? | Buy / build / integrate | Phase | Source |
|---|---|---|---|---|---|
| Referrer portal and report delivery | Web access to reports and images; auto fax/portal delivery | COVERED (#12) | Buy (RIS/PACS) | P2 | Plan |
| Referrer order intake / EHR integration | Electronic orders from referrer EHRs instead of fax | PARTIAL | Integrate selectively; fax intake at opening | P2 decide | MEDIUM |
| Fax / eFax | Inbound orders and records; outbound reports | COVERED (P2 list) | Buy HIPAA cloud fax with a BAA | P2 | Plan |
| Document management | Scans orders, IDs, insurance cards, consents into the chart | COVERED (P2 list) | Buy (RIS document module) | P2 | Plan |
| Release of information | Inbound records requests, 15-business-day Texas clock | COVERED (#6) | Build selectively | P3, P4 | Plan; 45 CFR 164.524; Texas HSC 181.102 |
| Outbound prior-study retrieval | Requests and imports outside priors | COVERED (#7) | Build selectively | P3 spec | Plan |
| CD/DVD burn and import | Patient and referrer CDs out; outside CDs in | PARTIAL (import implied by #7) | Buy a disc publisher and import station, or the PACS's | P2 | MEDIUM; Luis's report that priors arrive on CD |
| Cloud image share | Link-based image sharing to patients and outside providers | PARTIAL (mentioned in landscape) | Buy (PACS feature or Ambra-type service) | P2 | Landscape doc |
| HIE / TEFCA | Exchange records with the regional HIE or a QHIN | PARTIAL | Defer; decide in P2 | After opening | TEFCA (ASTP/ONC), MEDIUM |
| Email / M365 | Staff email, calendar, files | MISSING | Buy with a BAA; MFA from day one | P2 | HIPAA BAA, HIGH |

### E. Operations

| System | What it does | Covered? | Buy / build / integrate | Phase | Source |
|---|---|---|---|---|---|
| Owner reporting | Volumes, turnaround, revenue, reader reconciliation | COVERED (#4) | Build | P3, P4 | Plan |
| Equipment service and uptime | OEM service contracts, uptime guarantees, remote monitoring, helium alerts | MISSING | Buy with the scanner purchase; negotiate uptime and response terms | P2 (with modality purchase) | MEDIUM |
| QC and physicist program | Annual physicist surveys, daily/weekly QC logs for MRI and CT | MISSING | Buy (medical physicist contract); log in a QC tool or binder | P1 plan, P5 | ACR MRI and CT QC requirements, HIGH; 25 TAC 289.227, VERIFY |
| Texas DSHS radiation machine registration and shielding | Registers the CT, shielding plan, radiation safety officer, operator credential records, dosimetry | MISSING | Opening checklist with physicist | P1 start | 25 TAC 289.226 (registration) and 289.227 (healing arts use), HIGH that registration is required; Texas Medical Board MRT certification for operators, MEDIUM |
| Personnel dosimetry | Badges for CT staff | MISSING | Buy a dosimetry service | P1 | 25 TAC 289.202, MEDIUM |
| Inventory and supply | Contrast, IV, linens, reorder points | MISSING | Buy simple tool or RIS module | P2 | MEDIUM |
| Staff scheduling, payroll, HR | Shifts, pay, onboarding | MISSING | Buy (payroll/HR service) | Opening checklist | MEDIUM |
| Staff credential tracking | ARRT, MRT, BLS/ACLS, MR safety training expiry | MISSING | Buy (HR tool feature) | Opening checklist | ACR and Texas rules on qualified personnel, MEDIUM |
| Compliance training | HIPAA and HB 300 training within 90 days of hire, signed acknowledgments kept 6 years | PARTIAL (HB 300 analyzed for Rick) | Buy an LMS or training service | P5 | Texas HSC 181.101, HIGH; 45 CFR 164.308(a)(5) |
| Policies and accreditation binder | Written policies, logs, evidence for ACR, DSHS, CMS, HIPAA | MISSING | Buy a compliance document tool, or a shared drive with an index | P1 to P5 | ACR, 42 CFR 410.33, 45 CFR 164.316 |

### F. IT, security and facilities

| System | What it does | Covered? | Buy / build / integrate | Phase | Source |
|---|---|---|---|---|---|
| Network, firewall, segmented modality VLAN | Isolates scanners from office and guest traffic | PARTIAL (inside "IT infrastructure") | Buy and configure; itemize | P2, P4 | HIPAA 164.312(e); FDA medical device cybersecurity guidance, MEDIUM |
| Wi-Fi (staff and guest, separated) | Connectivity; guest isolation | PARTIAL | Buy | P2 | MEDIUM |
| Internet circuits with failover | Cloud RIS/PACS is down when the line is down | MISSING | Buy two carriers or cellular failover | P2 | HIPAA contingency plan, 164.308(a)(7), HIGH |
| Identity and MFA | Single sign-on, MFA for every remote and admin login | PARTIAL | Buy | P2, P4 | 45 CFR 164.312(d); HHS 2025 Security Rule NPRM would mandate MFA, VERIFY final status |
| Endpoint protection and MDM | Antivirus/EDR, encryption, remote wipe, patching | PARTIAL | Buy | P2 | 164.308 and 164.312; NPRM, VERIFY |
| Backup and disaster recovery | Restorable copies, tested restore, downtime procedures | PARTIAL | Buy; vendor SLA for cloud systems plus local downtime kit | P3 design, P5 test | 45 CFR 164.308(a)(7), HIGH |
| Security monitoring and risk analysis | Logs, alerts, annual risk analysis, penetration test | PARTIAL (in running costs) | Buy managed service | P3, P5 | 45 CFR 164.308(a)(1), HIGH |
| Incident response and breach notification | Written plan, Texas 60-day notice, AG notice at 250+ Texans | MISSING | Build the plan (document), no software | P5 | 45 CFR 164.400 to 414; Texas Bus. and Com. Code 521.053, HIGH |
| Physical security: badging, cameras, alarm | Controls Zone IV and server/network closet access; records | MISSING | Buy | P2 | 45 CFR 164.310, HIGH; ACR MR zones, HIGH |
| Office phones for staff | Same platform as patient phones | COVERED ("phones") | Buy | P2 | Plan |

---

## What to change in the plan (suggested, not applied)

1. Add to the Phase 2 list: CT dose monitoring, MRI safety screening, peer review, critical results, teleradiology, good-faith estimates and payments, CD and image share, equipment service, email. Most are checkboxes inside the RIS/PACS RFP.
2. Add a Phase 1 "opening checklist" deliverable with named owners: enrollment and credentialing, ACR accreditation plan, DSHS registration and physicist, CLIA waiver, dosimetry, HR and training. Rick tracks; the center or its vendors do the work. State that these are not in the $45,000.
3. Itemize "IT infrastructure, security and backup" into network, Wi-Fi, failover, identity and MFA, endpoint, backup, monitoring, physical security, incident response.
4. Keep "radiologist voice recognition (dictation)" and "patient phones and optional AI voice answering" as separately named rows on slide 29 and in the leave-behind.

## Method limits

No sources were fetched in this pass; citations are named for Phase 1 verification. Items marked VERIFY (Texas SB 490, TRAIGA scope, the HIPAA Security Rule NPRM, 25 TAC 289.227 CT dose text, AUC status) must not be quoted to Luis or Fernando until read at the source.

---

# Section 2: Tiered findings and high-leverage ideas (Rick, 17:23)

## Tier 1: what the owners asked about, and what is required to open

**What the owners asked about, and where it stands.**

| Owner ask | Plan item | Gap from Section 1 that belongs here |
|---|---|---|
| Scheduling | #8 (RIS), #5 backfill | Good-faith estimates for self-pay patients (45 CFR 149.610); language access line |
| Answering patients | Phones on the P2 list; #9 AI voice optional | Keep patient phones separate from radiologist dictation; internet failover (a cloud phone and RIS are down when the line is) |
| Records | #6 inbound, #7 outbound priors, #12 report delivery | CD burn and import station; critical results logging (inside #12) |
| Prior auth | #1, #2 | Structured order intake (see idea 1 below; it is Tier 2 by request but it feeds #1 directly) |
| Owner numbers | #4 | Exam-to-charge reconciliation inside #4 |

**Required to open (not optional, not Rick's build; owner-assigned on a Phase 1 opening checklist, outside the $45,000):**
1. Payer enrollment and radiologist credentialing (Medicare IDTF 855B and 42 CFR 410.33, Texas Medicaid, TRICARE, commercial, CAQH). Start in Phase 1.
2. ACR accreditation for MRI and CT (42 CFR 414.68), with its components: CT dose records, MR safety policy and roles, physician peer review, physicist QC program.
3. Texas DSHS CT registration, shielding, dosimetry, operator credentials (25 TAC 289.226, 289.227, 289.202).
4. CLIA certificate of waiver before any fingerstick creatinine (42 CFR 493).
5. HIPAA Security Rule basics: risk analysis, MFA and endpoint protection, backup and downtime plan, incident response and Texas breach notice (45 CFR 164.308 to 164.316; Bus. and Com. Code 521.053).
6. HB 300 staff training within 90 days of hire, signed statements kept (HSC 181.101).
7. Card acceptance under PCI DSS, Section 1557 language access notices, an email system with a BAA.

## Tier 2: gaps they did not ask about

Teleradiology coverage, cloud image share, structured referrer orders, patient cost estimates at scheduling (beyond the legal minimum), no-show risk scoring, coding and charge capture review, inventory, HR and credential tracking, equipment uptime monitoring, HIE/TEFCA, referrer EHR integration.

### Method for picking the top ideas

Searched PubMed (NCBI E-utilities; the general web search provider was down this session, stated plainly). Kept only ideas that either feed #1, #2, #5, #4 or measurably cut a cost line, and that had at least one sourced number. Teleradiology and charge capture are real cost lines but I found **no published pricing or leakage figures** I would stand behind; they are listed at the end as "get quotes" items, not ideas.

### Idea 1: Structured electronic order intake (make the order carry what prior auth needs)

- **What it is.** Referrers order through the RIS's referrer portal or an e-order form with required fields (indication, relevant history, prior conservative treatment, prior imaging), instead of free-text faxes. Fax stays as a fallback, with staff keying into the same fields.
- **Evidence.** In 1,858 abdominal CT orders at Emory, only 51% of requisitions included the patient's cancer history; 71.3% of final reports did (Driessen et al., Curr Probl Diagn Radiol 2026, PMID 40517119). Outpatient orders were more complete than ED orders (OR 10.5). An LLM study at a Toronto department generated clinical histories for oncologic requisitions from the chart (Bhayana et al., Radiology 2025, PMID 39903072), showing the gap is recognized and addressable. No study I found measures prior auth denial or delay caused by incomplete orders at an imaging center. **The link to denials is my inference, not a sourced number.**
- **How it connects.** It is the input to #1: the prior auth packet is only as good as the order. Required fields mean fewer chase calls to the referrer's office, which is the slow step. Also feeds #4 (referrer-level volume and order quality).
- **Cost vs savings.** Cost: usually included in the RIS referrer portal (verify in P2); Rick's work is the field specification in P3, small. Savings: staff time on documentation chasing; **not quantified, estimate only.** The AMA figure of 13 hours per physician per week on prior auth (cited in the plan) is the size of the pool, not the share this recovers.
- **Risk.** Low. Referrers may ignore the portal; fax fallback covers it. Required fields must never become clinical appropriateness advice (FDA boundary, #13).
- **Pitch line.** "If the order arrives complete, prior auth is mostly paperwork; if it doesn't, it's phone calls, so we make the order carry what the payer will ask for."

### Idea 2: Staff-generated out-of-pocket estimates at scheduling (do the good-faith estimate well)

- **What it is.** The legal minimum is a good-faith estimate for uninsured and self-pay patients. The idea is to give every patient a staff-produced out-of-pocket estimate at scheduling, using the 271 eligibility response #2 already pulls (deductible remaining, coinsurance).
- **Evidence.** Across 470,422 outpatient imaging encounters at UC Irvine, patients with a staff-generated out-of-pocket estimate had nearly twice the odds of completing their imaging appointment (OR 1.91, 95% CI 1.87 to 1.95); self-generated estimates, mostly from self-pay patients, were associated with lower completion (OR 0.29) (Rashidi et al., Clin Imaging 2025, PMID 39736182). **This is an association, not a trial**; patients who ask for estimates may differ from those who do not.
- **How it connects.** Rides on #2 (same eligibility data), reduces cancellations that #5 then has to backfill, and satisfies the No Surprises Act requirement in the same step. Collected-at-scheduling amounts feed #4.
- **Cost vs savings.** Cost: an estimate feature in the RIS or RCM tool (often bundled; verify in P2) plus a small extension of #2, **estimate: weeks, not months.** Savings: more completed exams; Sherlock found no sourced figure for point-of-service collection rates and will not quote the commonly repeated ones.
- **Risk.** Medium. A wrong estimate is a patient complaint, and for self-pay patients a federal dispute process (patient-provider dispute resolution when the bill exceeds the GFE by $400 or more, 45 CFR 149.620, HIGH). Show estimates as estimates; a person reviews self-pay GFEs.
- **Pitch line.** "Patients who know what they'll owe are more likely to show up, and we already pull the numbers for prior auth, so the estimate is nearly free."

### Idea 3: Import outside priors into the PACS, and share images by link instead of CD

- **What it is.** Every outside prior that arrives (CD, courier, or a cloud share) is imported into the center's PACS and matched to the patient before the read; outbound, patients and referrers get a secure link, with CD as the fallback.
- **Evidence.** At UCSF, among 267 patients with CT or MRI before a procedure, repeat imaging was 72% when outside images were unavailable, 52% when they were on CD but not imported, and 11% when imported into PACS, the same as patients imaged only in-house (13%) (Lu et al., AJR 2012, PMID 22358003). Hospital procedure population, not an outpatient center; **direction is solid, the magnitude may not transfer.** Luis reported that outside priors arrive on CD and studies are read without them after five days (plan, #7).
- **How it connects.** It is the receiving end of #7 (outbound prior retrieval): retrieval is wasted if the CD sits in a drawer. Imported priors make RadAssist comparisons possible. Turnaround waiting on priors becomes a #4 metric.
- **Cost vs savings, honestly.** For a fee-for-service center, avoided repeats are **not** a savings; they are revenue the center does not earn. The case is quality and referrer trust (fewer "why did you scan my patient again" calls), radiologist time, and fewer burned CDs and courier runs. Cost: an import station or the PACS's built-in import and a cloud share feature (often bundled; verify in P2).
- **Risk.** Low. The main failure is a mismatched patient on import; require a two-identifier match.
- **Pitch line.** "A prior on a CD in a drawer is the same as no prior; we put it in front of the radiologist and send ours out as a link."

### Idea 4: A no-show risk score feeding the backfill engine (an experiment, not a promise)

- **What it is.** Use the RIS's own history (lead time, prior no-shows, exam type, day and time) to flag high-risk appointments for an extra human reminder call and to prioritize those slots for #5's waitlist offers.
- **Evidence, mixed and stated as such.** At a Singapore hospital (32,957 MRI appointments), calling the top 25% predicted-risk patients cut the no-show rate from 19.3% to 15.9%, a 17.2% relative reduction (Chong et al., AJR 2020, PMID 32901567). A 2026 hospital study (38,141 MRI appointments) found the model degraded with data drift and the call intervention produced **no overall change** (21.9% vs 22.0%) (JAMIA Open 2026, PMID 42553932). The plan already cites lead time over six months at OR 3.18 for no-shows (Rosenbaum 2018). Both prediction studies had no-show rates far above this center's likely rate, so the absolute gain here would be smaller.
- **How it connects.** Pure reuse: same events #5 consumes, same TCPA rate governor, same owner reporting. Without a year of the center's own data, start with a rule (lead time plus prior no-show), not a model.
- **Cost vs savings.** Cost: small inside #5 (**estimate: one to two weeks**, after six months of data). Savings: unproven at this site; measure it in #4 before claiming any.
- **Risk.** Low clinically; Medium on TCPA if it adds automated calls (keep the extra contact a human call, or inside the governor's caps). Fairness: risk scores can correlate with race and income; never use it to deny or double-book, only to add a reminder.
- **Pitch line.** "Once we have six months of your own data, we'll test whether an extra call to the likeliest no-shows pays off, and the owner report will tell you if it doesn't."

### Considered and not ranked (no sourced numbers found)

- **Teleradiology / after-hours reading.** Required as a coverage plan (Tier 1 operationally), but its cost lever is the contract: per-study rate, turnaround SLA, and whether it reads in the center's PACS. No published price I would quote; get three quotes in P2.
- **Charge capture reconciliation.** Matching every completed exam to a submitted claim is a natural #4 report and likely the cheapest real money in this list, but I found no defensible leakage rate. Build it as a #4 report; do not promise a number.
- **Interface fees.** Already covered by the four contract terms (#3); the single-database RIS+PACS position removes the largest interface.

### Source list for Section 2
- Driessen R, et al. Completeness and accuracy of malignancy history in abdominal CT order requisitions and final radiology reports. Curr Probl Diagn Radiol 2026;55(1):25-30. PMID 40517119.
- Bhayana R, et al. Leveraging large language models to generate clinical histories for oncologic imaging requisitions. Radiology 2025;314(2):e242134. PMID 39903072.
- Rashidi A, et al. Association between price transparency and patient decision to complete outpatient imaging. Clin Imaging 2025;119:110397. PMID 39736182.
- Lu MT, et al. Reducing the rate of repeat imaging: import of outside images to PACS. AJR 2012;198(3):628-34. PMID 22358003.
- Chong LR, et al. Artificial intelligence predictive analytics in the management of outpatient MRI appointment no-shows. AJR 2020;215(5):1155-62. PMID 32901567.
- From prediction to practice: machine learning models and real-world interventions for MRI appointment no-shows in a hospital setting. JAMIA Open 2026. PMID 42553932.
- 45 CFR 149.610 and 149.620 (good-faith estimates; patient-provider dispute resolution).
