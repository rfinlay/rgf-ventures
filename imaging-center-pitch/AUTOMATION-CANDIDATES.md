# Automation Candidates: Greenfield Outpatient Imaging Center, El Paso

**Prepared:** 2026-10-01, for the 2026-10-20 dinner with Dr. Luis Ramos and [PARTNER NAME]
**Basis:** every evidence claim below traces to the Sherlock research brief of 2026-10-01 and its citation list. Where the research found no defensible evidence, this document says so instead of filling the gap.
**Operator assumption:** a one-to-two-person shop (Rick, possibly one contractor), building for one site that Rick personally operates. Effort and risk ratings are for that shop, not for a vendor.

## How to read the ratings

- **Recommendation:** Build (custom, Rick builds), Buy (a vendor or the RIS provides it), Integrate (buy it, Rick specifies, evaluates, connects, and supervises it), Decline (real, but Rick should not take it on).
- **Effort:** Small (weeks, one person), Medium (one to three months, one person), Large (more than a quarter, or needs a second person).
- **Risk:** the blast radius if it fails in production, not the probability of failure.
- **Evidence:** High, Medium, or Low, following the research brief's confidence ratings.

---

## Priority order

| # | Candidate | Recommendation | Effort | Risk | Evidence | Phase |
|---|---|---|---|---|---|---|
| 1 | Prior authorization orchestration and appeals | **Build** | Large | Medium | High | Lead product, design now |
| 2 | Eligibility verification at scheduling | **Build** (with #1) | Medium | Low | High | With #1 |
| 3 | Vendor contract access terms | **Advise now** | Small | None | High | This month, free |
| 4 | Owner operational reporting and reader reconciliation | **Build** | Small to Medium | Low | Low (no external evidence) | First thing built after opening |
| 5 | Cancellation backfill and waitlist | **Build, small** | Medium | Medium (TCPA) | High | After RIS is live |
| 6 | Inbound records requests (release of information) | **Build, selectively** | Medium | Medium (OCR enforcement) | High | Before opening |
| 7 | Outbound prior-study retrieval | **Build, selectively** | Medium to Large | Low | High on the gap, Low on the solution | After opening |
| 8 | Appointment reminders, self-scheduling, intake forms | **Buy (the RIS)** | None | Low | High | Vendor selection |
| 9 | Inbound patient voice (phones) | **Integrate** (buy a vendor) | Medium to integrate | High | High on the constraint | Phase two, if at all |
| 10 | Outbound patient notifications beyond reminders (results ready, instructions) | **Buy (RIS) or fold into #5** | Small | Medium (TCPA) | High on constraints | With #5 |
| 11 | Balance-due and payment reminders | **Decline for phase one** | Small | High (TCPA) | High on constraint | Not until a separate consent basis exists |
| 12 | Referring physician communication and report delivery | **Buy (RIS/PACS)** | None | Low | None found | Vendor selection |
| 13 | Protocol selection, clinical appropriateness, anything touching the image | **Decline** | n/a | Very high (FDA) | High | Never without an FDA pathway |

---

## 1. Prior authorization orchestration and appeals

**The manual process.** For each advanced imaging order (CT, CTA, MRI, MRA, PET, PET-CT) covered by a commercial or Medicare Advantage plan, staff determine whether authorization is required, assemble clinical documentation from the referrer, submit through the plan or its radiology benefit manager, track the decision against the deadline, and on denial either file an appeal or let it go. Most practices let it go.

**Evidence it is costly.**
- Physicians and staff spend an average of 13 hours per week on prior authorization, about 40 requests per physician per week; 40% of physicians report staff who work exclusively on it (AMA 2025 Prior Authorization Physician Survey, n=1,000, self-reported). Evidence: High as a survey.
- In Medicare Advantage in 2024, 4.1 million prior authorization requests were denied (7.7% of 52.8 million). Only 11.5% of denials were appealed; 80.7% of appeals were partially or fully overturned (KFF, 2026-01-28, from data insurers report to CMS). Evidence: High. Not imaging-specific; CMS does not report by service type.
- Of physicians who do not appeal, 59% do not expect to win and 52% cite insufficient staff time (AMA 2025).
- CMS estimated its prior authorization rule would save at least 220 million provider hours and $16 billion over ten years (CMS-0057-F, 89 FR 8758, Regulatory Impact Analysis). A projection, not measured savings.
- Of 17,913 outpatient MRI prior authorization requests at one institution over 2019 to 2022, 4.94% were denied (Harrer et al., J Am Acad Orthop Surg 2025, PMID 39729599). The process approves about 95% of what it touches, which is the profile of a process to automate rather than staff.

**Recommendation: BUILD. This is the lead product.** The vendor category (Availity, Waystar, Rhyme, Cohere Health, Infinitus, Humata Health) is oriented to health systems and large groups, and much of it is payer-funded. A single site is an awkward customer for all of them. The appeal gap is a workflow failure, not a technology gap: nobody has time to file.

**What the agent does.** Detects authorization-required orders at scheduling. Assembles the documentation packet from the referral and the RIS. Submits via the payer's API where one exists (see dependencies), via EDI 278 where supported, and otherwise prepares a complete packet for a human to submit. Tracks every open request against the 7-calendar-day standard and 72-hour expedited timeframes that bind impacted payers from 2026-01-01. On denial, drafts the appeal with the clinical rationale and queues it for a human signature. Reports the appeal rate and overturn rate weekly, which is the number the owner should watch.

**Effort:** Large. The orchestration logic is Medium; payer connectivity is what makes it Large, because each payer and radiology benefit manager is its own integration.

**Risk:** Medium. A missed deadline delays a scan; it does not harm a patient directly. A human signs every submission and every appeal in phase one.

**Dependencies.**
- RIS order and scheduling feed (HL7 v2 ORM/SIU, or the RIS's own API; make this a contract term, see #3).
- Payer FHIR Prior Authorization APIs, required of impacted payers by 2027-01-01 under CMS-0057-F. The rule covers Medicare Advantage, Medicaid and CHIP (fee-for-service and managed care), and QHP issuers on federally facilitated exchanges. It binds payers, not providers, and guarantees nothing about data quality or ease of connection. Almost 63% of medical plans report they are developing such an API (2025 CAQH Index, payer self-report).
- Commercial plans outside the rule: EDI 278 or human submission.
- Payer mix: not verified for El Paso. Ask [PARTNER NAME].

**Compliance constraints.**
- Business associate agreement with the center before any PHI flows (45 CFR 164.502(e); settled).
- The AI vendor's BAA envelope: Anthropic's agreement covers Skills, Web Search, Memory, Bash tool, and Text Editor tool, but excludes Computer Use and Web Fetch. Those are the two capabilities one would reach for to drive a payer portal with no API. **Portal screen-driving against PHI is not available inside the BAA.** Design through APIs, EDI, and a human step. Coverage depends on BAA version (Enterprise features for versions accepted after 2025-12-02; Messages API features after 2026-04-01). Confirm the applicable version in writing.
- Texas SB 1188: electronic health records with Texas patient data must be physically stored in the US as of 2026-01-01. Verify US residency for every component including the model provider.
- Texas HB 300: broad covered-entity definition likely reaches Rick directly. Exact training interval and records deadline not verified; do not quote them.
- FDA: "claims or billing information" and "determination of health benefit eligibility" are named in the administrative support exclusion at 21 U.S.C. 360j(o)(1)(A). Not a device. The agent must never recommend which study to order or whether a study is clinically appropriate; that leaves the exclusion.

**Market note.** Olive AI, once the flagship of this category, shut down in 2023 and sold its prior auth assets to Waystar and Humata Health. It sold broad automation to hospital systems on long cycles, which is close to the opposite of a narrow agent for one observable site.

---

## 2. Eligibility verification at scheduling

**The manual process.** Before or at scheduling, staff confirm active coverage, benefits, copay, and whether the plan requires authorization for the ordered study, by portal lookup or phone call.

**Evidence it is costly.** Shares the AMA and CMS evidence above; eligibility is the front half of the same workflow. No separate defensible benchmark on eligibility cost exists for imaging centers; the research specifically could not verify per-transaction costs and says not to quote them.

**Recommendation: BUILD, as the first stage of #1.** Eligibility is where the authorization-required determination happens, so the two are one pipeline. EDI 270/271 eligibility transactions are the oldest and most standardized surface in this space; the center's clearinghouse or billing vendor will expose them.

**Effort:** Medium. **Risk:** Low; a wrong eligibility result is caught at check-in.

**Dependencies.** Clearinghouse or billing vendor access to 270/271 (contract term). RIS scheduling feed.

**Compliance.** Same as #1. "Determination of health benefit eligibility" is named verbatim in 21 U.S.C. 360j(o)(1)(A).

---

## 3. Vendor contract access terms

**The process.** Not an automation. It is the precondition for every automation on this list, and it is free only before the RIS, PACS, billing, and phone contracts are signed.

**Evidence.** The research's integration findings: HL7 v2 is the real lingua franca at a small center; FHIR on the RIS side is aspirational; DICOM (Modality Worklist, C-FIND/C-MOVE, DICOMweb) is the most reliably accessible surface because it is standardized. Vendor interface fees are customary and quoted per interface (specific ranges not verified; do not quote). Mirth Connect, the usual free HL7 engine, went closed-source commercial at version 4.6 in March 2025; the last open release is 4.5.2 from 2024-09-23, unmaintained, which is a security consideration on a PHI pathway. Evidence: High.

**Recommendation: ADVISE NOW.** Four terms in every contract: named API access to the center's own data; HL7 interface count and fee schedule fixed at signature; data export rights in standard formats at no charge; DICOM query permissions for systems the center authorizes.

**Effort:** Small. Rick drafts the language this month. **Risk:** None. **Dependencies:** none; this is the dependency.

---

## 4. Owner operational reporting and reader reconciliation

**The manual process.** The owner pulls RIS reports for volume and turnaround, pulls billing reports for revenue, and reconciles them by hand or not at all. Referrer-level and revenue-per-slot views require joining the two. Luis, as a 1099 reader, separately reconciles what he read against what he was paid.

**Evidence it is costly.** **None found, and the research says so plainly.** There is no benchmark literature on what imaging center owners want from dashboards, and no study of the gap between RIS-native reporting and owner needs. The structural claim is defensible without a study: RIS reporting is built for radiology operations, and the owner's view requires joining RIS data to billing data, which are usually different systems.

**Recommendation: BUILD.** Custom by nature because it encodes one owner's definition of the numbers that matter. Smallest compliance envelope of the five (no patient-facing surface). Cheapest to build. It is the artifact the owner personally looks at, which keeps Rick in the room. The reader-reconciliation view is the same engine and already has a customer in Luis.

**Effort:** Small to Medium, depending on billing data access. **Risk:** Low.

**Dependencies.** RIS reporting export or database access; billing system export. Both are contract terms under #3. Ask [PARTNER NAME] what he wants on one page every Monday morning; that answer is the specification.

**Compliance.** "Business analytics" and "practice and inventory management" are named in 21 U.S.C. 360j(o)(1)(A). PHI is present in the data, so the BAA and SB 1188 residency still apply, but no patient communication is involved.

---

## 5. Cancellation backfill and waitlist

**The manual process.** A patient cancels. The slot sits empty unless a scheduler remembers to call someone on a paper or spreadsheet waitlist.

**Evidence it is costly.**
- At a University of California, Irvine outpatient radiology service, 24.3% of 19,262 exams were missed: 22.3% cancellations and 2.0% no-shows. 70.19% of cancellations were patient-initiated (Aijaz et al., Acad Radiol 2024, PMID 38705764). Evidence: High as a single-center finding, Medium as a benchmark.
- Across 2,893,626 outpatient imaging visits over 16 years, scheduling lead time over six months carried an odds ratio of 3.18 for no-show versus booking within one week; mammography had the highest modality no-show rate at 6.99% versus 1.25% for radiography (Rosenbaum et al., J Am Coll Radiol 2018, PMID 29755001). Shortening time-to-appointment reduces no-shows on its own, and backfill is how you shorten it.

**Recommendation: BUILD, small.** The cancellation stream is roughly ten times the no-show stream and mostly arrives with lead time. The custom piece is the ranking logic: which waitlisted patients to offer a freed slot to, in what order, within the contact caps. It sits on top of whatever RIS they choose; the RIS supplies the schedule and the cancellation event.

**Effort:** Medium. **Risk:** Medium, entirely from TCPA.

**Dependencies.** RIS cancellation events (HL7 SIU or API), patient contact preferences and consent captured at intake, a per-patient message rate governor shared with #8 and #10.

**Compliance constraints.**
- TCPA wireless healthcare exemption, 47 CFR 64.1200(a)(9)(iv): sent only to the number the patient provided; provider name and contact at the start; content limited to appointment confirmations, reminders, pre-registration instructions, and the other enumerated categories; no billing or financial content; 160 characters or less for text; **one message per day and three per week per patient, voice and text combined**; opt-out in every message, honored immediately; not charged to the patient.
- A backfill offer plus a reminder sequence plus a results notice can collide with the weekly cap. The system needs a per-patient rate governor across all senders, not a send queue.
- Statutory damages: $500 per violation, up to $1,500 if willful or knowing. $1,500 is the treble ceiling, not a fixed amount.
- An AI-generated voice is an "artificial voice" under the FCC's February 2024 ruling (FCC 24-17); the healthcare exemption survived that ruling.
- Spanish-language messages are a requirement, not an option: 26.5% of El Paso County residents aged 5 and over speak English less than "very well" (ACS 2024 5-year, B16004).
- FDA: "appointment schedules" is named in 21 U.S.C. 360j(o)(1)(A).

---

## 6. Inbound records requests (release of information)

**The manual process.** A patient, attorney, insurer, or other provider requests images or reports. Staff log the request, locate the study (possibly on archival storage or a legacy PACS), produce the copy, calculate a fee, deliver, and track the deadline. Requests that sit in a pile are already consuming the clock.

**Evidence it is costly.**
- The 30-day HIPAA clock runs from receipt, not from when the request reaches the right desk. One extension of up to 30 more days is allowed, only with written notice inside the original 30 days. Outer limit 60 days (45 CFR 164.524). Evidence: High.
- Fees must be reasonable and cost-based, and the permitted components are an exhaustive list: copying labor, supplies, postage if mailing is requested, and an agreed summary. **Search and retrieval labor is explicitly not chargeable.** Billable labor begins only once the responsive PHI "has been identified, retrieved or collected, compiled and/or collated, and is ready to be copied" (2016 HHS guidance as quoted in Ciox Health v. Azar). For an imaging center, the expensive half of the work cannot be billed. Evidence: High.
- The $6.50 flat-fee option survived Ciox; the court held the fee-method listing was not reviewable agency action and never reached the merits (435 F. Supp. 3d 30, D.D.C. 2020).
- OCR's Right of Access Initiative has produced more than 50 enforcement actions, typically five-figure settlements for small providers. Evidence: Medium-High on the pattern; individual cases not verified.
- Texas Chapter 181 (HB 300) sets a shorter deadline than HIPAA's 30 days. **Exact day-count not verified; do not quote it.**
- Cost or volume per request for an imaging center: no defensible source. Vendor pages quote figures; do not use them.

**Recommendation: BUILD, selectively.** Intake, deadline tracking, fee calculation against the permitted-components list, and status reporting are a small custom build with clear regulatory specifications and hard deadlines. The actual study retrieval is a DICOM query/retrieve against the PACS, which is the most standardized surface available.

**Effort:** Medium. **Risk:** Medium; the failure mode is a missed statutory deadline and an OCR complaint, which is why deadline tracking is the first feature, not the last.

**Dependencies.** PACS DICOM query/retrieve permission (contract term under #3). A request intake channel (fax still exists; web form; portal). The Texas deadline, verified against the statute before the specification is final.

**Compliance.** 45 CFR 164.524 in full. Texas Chapter 181. BAA. SB 1188 residency. Patient identity verification before release is a human step in phase one.

---

## 7. Outbound prior-study retrieval

**The manual process.** A new center opens with zero priors on file. For every comparison study, staff call the prior facility, fax a request, wait, receive a CD or a portal link, and import. Patients frequently carry their own discs.

**Evidence it is costly.** RSNA's March 2026 comment letter to ASTP/ONC identifies the prior-study retrieval gap directly, notes that patients still act as couriers for their own imaging, and flags the problem specifically for small community imaging centers. DICOM exchange is not currently a TEFCA QHIN requirement; RSNA is asking for it to become one. TEFCA as of 2026 moves documents at scale but is not an imaging-exchange solution. Evidence: High on the existence of the gap. No cost-per-retrieval benchmark exists; do not quote vendor figures.

**Recommendation: BUILD, selectively, and be honest that it is partly unsolved.** This is the most defensible custom work in the portfolio because no vendor has solved it for a small center. The buildable part: a request tracker that knows which El Paso facilities (hospital systems: The Hospitals of Providence, Las Palmas Del Sol, University Medical Center, Texas Tech; Southwest X-Ray's five Akumin locations; independent groups) accept which request channel, generates the request, tracks it, and imports what comes back via DICOM. The unsolvable part today: there is no network to query. Say so.

**Effort:** Medium to Large. **Risk:** Low; a missing prior delays a read and the radiologist already knows to ask.

**Dependencies.** PACS DICOM import. A directory of local facilities and their release processes, built by hand in the first months of operation. TEFCA/DICOM developments, which should be monitored but not relied on.

**Compliance.** Outbound requests carry PHI (patient identity and the fact of a study); BAA and residency apply. Patient authorization for third-party release is governed by the sending facility's process.

---

## 8. Appointment reminders, self-scheduling, intake forms

**The manual process.** Phone reminders by staff; paper or kiosk intake; scheduling by phone.

**Evidence.**
- Adding a text reminder to an existing phone reminder reduced MRI no-shows from 5.1% to 3.8% in a randomized study of 6,989 patients at Massachusetts General Hospital (p=0.02, odds ratio 0.75). It did not improve arrival punctuality. Only 67.5% of the texting arm was reachable by text (Liu et al., J Am Coll Radiol 2017, PMID 28583321). Evidence: High. This is a 1.3-point absolute reduction; do not restate it as 25%.
- Adding an interactive voice call to text reminders was reported to lower no-shows a further 1.7 points (9.6% versus 11.3%) in a NEJM Catalyst study. Evidence: Medium-High; figures seen through search, article paywalled and not read.
- Modern cloud imaging RIS products bundle self-scheduling, automated notifications, and patient-app intake. RamSoft's imaging-center page claims all three, plus a zero-code workflow designer and no per-user or per-modality charges (vendor's own page, 2026-10-01). Which features are bundled versus paid modules, and any price, could not be verified for any RIS vendor.

**Recommendation: BUY. The RIS does this. Do not pitch it as novel.** The only custom work is confirming during vendor selection that the RIS's reminder engine honors the TCPA caps and supports Spanish, and that its events are exposed to #5.

**Effort:** None beyond vendor evaluation. **Risk:** Low. **Dependencies:** RIS selection. **Compliance:** the RIS vendor's reminder engine must comply with 47 CFR 64.1200(a)(9)(iv); verify this in evaluation, and make sure the center's own backfill messages (#5) and the RIS reminders share one per-patient cap.

---

## 9. Inbound patient voice

**The manual process.** Front desk staff answer every call: scheduling, directions, prep instructions, results status, insurance questions, and occasionally a patient describing symptoms.

**Evidence.**
- 26.5% of El Paso County residents aged 5 and over (215,186 of 813,194) speak English less than "very well"; 97.8% of that group speaks Spanish (ACS 2024 5-year, Table B16004, computed from raw counts). Roughly one in four patients cannot be reliably served by an English-first phone system. Evidence: High.
- Call volume per study, abandonment rates, and time-to-schedule benchmarks for imaging schedulers: **none found.** Do not quote any.
- An AI voice is an "artificial voice" under the TCPA per FCC 24-17 (February 2024); the healthcare exemption at 64.1200(a)(9) was expressly preserved. Inbound calls initiated by the patient are outside the autodialer and artificial-voice restrictions that govern outbound calls, but any outbound callback or follow-up from the voice system falls back under them.

**Recommendation: INTEGRATE. Buy a healthcare voice vendor; Rick specifies, evaluates, integrates, and supervises.** This is the most crowded and best-funded category of the five (Hyro, Assort Health, Infinitus, Parlance, Syllable, and others). A one-to-two-person shop cannot build a telephony-grade voice stack that beats a funded team on cost or reliability. It is also the highest-blast-radius failure on the list: a voice agent that mishandles a patient describing chest pain, or garbles Spanish, is a clinical-safety and reputational event, not a bug. The Spanish quality bar in El Paso is higher than almost anywhere in the country, which makes it the worst place to learn voice.

Alternatively: do not do it at all in phase one, and let the front desk answer the phone while #1 removes the prior auth load from them.

**Effort:** Medium to integrate (RIS scheduling API, escalation to a human, Spanish evaluation protocol). **Risk:** High.

**Dependencies.** RIS scheduling API for the vendor to book against (contract term). A vendor BAA. An escalation path to a human on any symptom language. A Spanish evaluation set built with Luis.

**Compliance.** Vendor BAA; SB 1188 US-only storage including the vendor's telephony and transcript storage; TCPA for any outbound leg; TRAIGA (Texas HB 149, effective 2026-01-01) extends an AI disclosure obligation to healthcare providers, scope not fully verified; plan for a disclosure at the start of the call.

---

## 10. Outbound patient notifications beyond reminders

**The manual process.** Staff call patients when results are ready for pickup, when prep instructions change, or when a scan is rescheduled.

**Evidence.** The TCPA exemption's enumerated content list covers appointment and exam confirmations and reminders, pre-registration and pre-operative instructions, lab results, and prescription notifications. Evidence: High, read at the regulation.

**Recommendation: BUY (the RIS) where it supports it; otherwise fold into the #5 message engine so one rate governor covers everything.** Not a separate build.

**Effort:** Small. **Risk:** Medium (TCPA caps collide here). **Compliance:** identical to #5.

---

## 11. Balance-due and payment reminders

**The manual process.** Statements by mail; phone calls by billing staff.

**Evidence.** The wireless healthcare exemption explicitly excludes "accounting, billing, debt-collection, or other financial content." Any automated billing message needs its own prior express consent basis and cannot ride the healthcare exemption. Evidence: High.

**Recommendation: DECLINE for phase one.** Real and automatable, but it requires a separate consent architecture captured at intake, and the downside of getting it wrong is statutory damages per message. Revisit after the billing vendor is chosen and the consent language is in the intake forms. This is a candidate Rick should name and decline, not quietly omit.

---

## 12. Referring physician communication and report delivery

**The manual process.** Reports faxed or portal-delivered to referrers; critical results called.

**Evidence.** None gathered by the research; this is standard RIS/PACS functionality.

**Recommendation: BUY (RIS/PACS).** Not a differentiator and already solved. The only custom touch is that referrer volume data feeds the owner reporting view in #4.

---

## 13. Protocol selection, clinical appropriateness, anything touching the image

**Why it is listed.** Someone at the dinner may ask whether the agents can help pick protocols or check appropriateness. The answer must be no.

**Evidence.** The moment software interprets image data, or recommends which study to order, it leaves the administrative support exclusion at 21 U.S.C. 360j(o)(1)(A) and enters device-regulated territory, where the Clinical Decision Support criteria at 360j(o)(1)(E) apply (guidance revised 2026-01-06 and 2026-01-29). Texas SB 1188 separately requires disclosure of AI used for diagnostic purposes. Evidence: High.

**Recommendation: DECLINE, and say so out loud.** The agents stop at the clinical boundary. This is also the discipline that keeps RadAssist on the right side of the line.

---

## What this inventory deliberately does not contain

- Any cost-structure percentage for an imaging center. Ask Fernando for his own actual numbers from Southwest X-Ray. Do NOT name Desert Imaging; he did not found it.
- Any CAQH per-transaction cost, vendor price, HL7 interface fee range, imaging prior auth denial rate above the verified 4.94% and 7.7%, percentage of advanced imaging requiring authorization, Texas HB 300 day-count or training interval, records cost per request, or count of independent imaging centers. The research could not verify any of them. See Section 8 of the research brief.
- A market-sizing argument. This is a bespoke build for one center that Rick personally operates. Consolidation (RadNet, SimonMed, Akumin, Rayus, Touchstone, US Radiology Specialists) is removing the single-site prospects that would be a market, and the partner lived that from the selling side.
