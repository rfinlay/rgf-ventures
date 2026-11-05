# Automation Candidates: Greenfield Outpatient Imaging Center, El Paso

**Prepared:** 2026-10-01; **updated 2026-10-22** after the Luis rehearsal, **2026-11-02** after Rick's review round, and **2026-11-03** (Rick's evening review: system coverage, RIS/PACS position, running costs and the TCO deliverable), and **2026-11-04** (final round after Rick's review with Luis: RadAssist, dates-depend-on and what-I-need moved to the appendix; records slide rewritten with the QR envelope idea; Exa as the likely RIS/PACS), for the briefing on Thursday 2026-11-05 at 3:30 PM with Dr. Luis Ramos, Fernando Escarzaga, and Jesse Martinez
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
| 1 | Prior authorization orchestration and appeals | **Build** | Large | Medium | High | Lead product. Demo on synthetic data exists today; designed in Phase 3; built against the real RIS and payers in Phase 4 (Mar to Apr 2027), tested and live in Phase 5, before opening |
| 2 | Eligibility verification at scheduling | **Build** (with #1) | Medium | Low | High | With #1 |
| 3 | Vendor contract access terms | **Advise now** | Small | None | High | This month, free |
| 4 | Owner operational reporting and reader reconciliation | **Build** | Small to Medium | Low | Low (no external evidence) | Designed in Phase 3; built in Phase 4 |
| 5 | Cancellation backfill and waitlist | **Build, small** | Medium | Medium (TCPA) | High | After RIS is live |
| 6 | Inbound records requests (release of information) | **Build, small** | Medium | Medium (OCR enforcement) | High | Before opening |
| 7 | Outbound prior-study retrieval | **Build, small** | Medium to Large | Low | High on the gap, Low on the solution | Specified in design; build priced from its spec |
| 8 | Appointment reminders, self-scheduling, intake forms | **Buy (your RIS)** | None | Low | High | Vendor selection |
| 9 | Inbound patient voice (phones) | **Integrate** (buy a vendor) | Medium to integrate | High | High on the constraint | Phase two, if at all |
| 10 | Outbound patient notifications beyond reminders (results ready, instructions) | **Buy (RIS) or fold into #5** | Small | Medium (TCPA) | High on constraints | With #5 |
| 11 | Balance-due and payment reminders | **Decline for phase one** | Small | High (TCPA) | High on constraint | Not until a separate consent basis exists |
| 12 | Referring physician communication and report delivery | **Buy (RIS/PACS)** | None | Low | None found | Vendor selection |
| 13 | Protocol selection, clinical appropriateness, anything touching the image | **Decline** | n/a | Very high (FDA) | High | Never without an FDA pathway |
| 14 | Radiology report assistance (RadAssist, extended to the center) | **Build** (existing product, extended) | Medium | Low (the radiologist signs every report) | Medium (in daily use; one radiologist's own figure, no literature) | Interface terms now; specified in Phase 2 |

## Update 2026-10-22: timeline, agent types, build pricing, demo

Decided by Rick after the 2026-10-22 rehearsal with Luis. Every sibling document (deck, leave-behind, speaking notes, runbook, architecture) carries the same changes.

- **Timeline.** The opening is targeted around **June 2027, April at the earliest**. The **build starts around March 2027** so prior authorization (#1, #2) is working **before** opening. Documents say only "your new center": no building, property, address, or prior business at the site.
- **Two kinds of agent, in plain language** (deck slide 6, architecture page 7). An **operations agent** runs one workflow inside the center's systems (#1, #5, #6) through the RIS and payer APIs, and a person approves anything that leaves the building. An **owner's agent** (#4) the owner texts or calls for answers, plus a Monday report: volumes by modality, reader, and referrer; authorization and denial rates; reconciliation. Guardrails: a person signs anything clinical or outbound; numbers are calculated and checked, never guessed; HIPAA BAAs; US data residency.
- **Working demo as a deliverable.** A clickable prior authorization demo on synthetic data exists today, built by Alan and live at https://rfinlay.github.io/imaging-priorauth-demo/, linked from the deck and leave-behind. The production version is built in Phase 4.
- **Pricing, APPROVED by Rick 2026-11-02: one fixed-fee engagement for the new center, $45,000 in five phases, November 2026 to May 2027, ready for a ~June 2027 opening with about a month of buffer.** Phase 1 Discovery and Requirements, Nov to mid-Dec, $7,000 ($4,000 at signing, $3,000 on delivery; deliverable: signed Requirements and Roadmap, five parts set by Rick 2026-11-03: requirements for every system, patient-flow map (order to signed report to paid claim), vendor contract terms to demand, make-or-buy recommendation for each requirement (met by a system you buy, or a piece Rick builds, with a ballpark running cost for anything built, so build and buy compare on total cost; R28), vendor shortlist and evaluation criteria for Phase 2). Phase 2 Vendor and System Selection, mid-Dec to Jan, $8,000 ((1) scheduling; (2) RIS and PACS, evaluated both as one bundled cloud system and as separate best-of-breed RIS plus PACS (Exa is one example); (3) prior authorization and eligibility; (4) patient phones, IVR and AI answering; (5) radiologist voice recognition and dictation; (6) billing and clearinghouse; (7) imaging-specific: modality integration and worklist, reading workstations, image sharing (CD and cloud); interface fees fixed up front, confirmed by Rick 2026-11-03 as the fees meant in R13; deliverable: Vendor Selection Report: side-by-side comparison of the shortlisted systems in each category, a weighted scoring matrix against the Phase 1 requirements (integration readiness a named criterion), pros and concerns for each, and a 5-year total cost of ownership per option (license or subscription, implementation, interface fees, support, hardware), with a recommendation; plus the contracts to sign; the system list was widened by Rick 2026-11-03 and the final list is his to confirm). Phase 3 Design and Staffing Plan, Feb, $7,000 (architecture, workflows, security/HIPAA, how each role's work runs; never headcount reduction; plus, added by Rick 2026-11-03, the deliverable "Total cost of ownership and operating budget": three hosting options, pros and cons, ranges, one-time and monthly and three-year cost including support labor, the owner picks; see "Running costs and hosting" below). Phase 4 Build and Configure, Mar to Apr, $14,000 ($7,000 Mar 1, $7,000 Apr 1; deliverable: every system, bought and built, set up, connected and passing end-to-end tests, vendors configure their own products and Rick manages them, connects everything and runs the tests (R26); depends on Phases 2 and 3 and vendor lead times). Phase 5 Testing, Training and Go-Live, May, $9,000 (deliverable: signed go-live readiness plus opening-week support). Phases 2, 3 and 5 are paid in full at the start; each phase starts only after the previous sign-off. Work outside the phases: $150/hr, approved first, against a retainer the client tops up. The timeline flexes with the opening date; the price does not. Running costs (hosting, database, model usage, texting, clearinghouse transactions, security, backups, monitoring) are not in the $45,000: a ballpark range in Phase 1, a firm operating budget in Phase 3, accounts in the center's name billed at cost with a monthly statement (Rick, 2026-11-03; see "Running costs and hosting" below). The engagement is priced for one center with one selected system per category; additional centers, or a different system chosen for another center, are quoted before work starts. The earlier design/build split ($30,000 + $40,000) and the proposed support fee are withdrawn.
- **Assumptions the build dates depend on (slide 35; aligned with slide 24, leave-behind, runbook, Rick 2026-11-03):** signed contract; vendors selected and contracted in Phase 2, one pick per system, with API, HL7, and DICOM sandbox access; vendor contracts and BAAs signed before Phase 4, hosting option chosen by the end of Phase 3; payer FHIR and EDI test access, and payer enrollment and credentialing started early enough to bill at opening; a named owner contact for approvals; real volumes or payer mix before payer-specific design; equipment delivery dates. If an assumption slips, the dates move; the price does not. Engagement assumptions: one center, one pick per system, extra work quoted and approved first; running costs billed at cost in the center's accounts, estimated Phase 1, budgeted Phase 3; outside work $150/hr approved first.
- **Exa.** The PACS vendor may build similar features. Position: vendor-neutral, built on the center's data and contract terms, works with whatever RIS and PACS they pick; the four access terms (#3) protect the center either way. Never disparage Exa.
- **RadAssist (#14) roadmap, per Luis (updated 2026-11-01):** the Spine MRI module (cervical, thoracic, lumbar) shipped 2026-10-31, built from Luis's template and his answers. RadAssist is a one-minute spoken overview on slide 34 (appendix since 2026-11-04, pulled from the main flow by Luis), not a live demo (Luis's feedback, 2026-11-03); the walkthrough stays in archive/DEMO-SCRIPT.md Part A, unused. Out loud it is "Luis sent me his template and his rules. Every rule in it is his," with no claim about how fast it was built (Rick, 2026-11-02). Still on the roadmap: voice dictation integration, then brain and cardiac CTA (CAD-RADS) modules. Luis also wants technologist data capture at the ultrasound station to pre-fill reports. **AI image auto-fill** (upload the per-level images and have the software fill the level findings) is Luis's stated vision; it is diagnostic software, so it is listed only as a future item with a regulatory path, never promised or dated. Selling it to other centers is **not** raised in front of Fernando, and no arrangement of Luis's is described in any pitch document (Rick, 2026-11-03).
- **Prior-records reality, per Luis:** outside priors arrive by courier on CD or DVD; after five days the study is read without them. This sharpens #7.

---

## 1. Prior authorization orchestration and appeals

**The manual process.** For each advanced imaging order (CT, CTA, MRI, MRA, PET, PET-CT) covered by a commercial or Medicare Advantage plan, staff determine whether authorization is required, assemble clinical documentation from the referrer, submit through the plan or its radiology benefit manager, track the decision against the deadline, and on denial either file an appeal or let it go. Most practices let it go.

**Evidence it is costly.**
- Physicians and staff spend an average of 13 hours per week on prior authorization, about 40 requests per physician per week; 40% of physicians report staff who work exclusively on it (AMA 2025 Prior Authorization Physician Survey, n=1,000, self-reported). Evidence: High as a survey.
- In Medicare Advantage in 2024, 4.1 million prior authorization requests were denied (7.7% of 52.8 million). Only 11.5% of denials were appealed; 80.7% of appeals were partially or fully overturned (KFF, 2026-01-28, from data insurers report to CMS). Evidence: High. Not imaging-specific; CMS does not report by service type.
- Of physicians who do not appeal, 59% do not expect to win and 52% cite insufficient staff time (AMA 2025).
- CMS estimated its prior authorization rule would save at least 220 million provider hours and $16 billion over ten years (CMS-0057-F, 89 FR 8758, Regulatory Impact Analysis). A projection, not measured savings.
- Of 17,913 outpatient MRI prior authorization requests at one institution over 2019 to 2022, 4.94% were denied (Harrer et al., J Am Acad Orthop Surg 2025, PMID 39729599). The process approves about 95% of what it touches, which is the profile of a process to automate rather than staff.

**Recommendation: BUILD. This is the lead product.** The vendor category (Availity, Waystar, Rhyme, Cohere Health, Infinitus, Humata Health) is priced and implemented for health systems and large groups, and much of it is payer-funded. At this center's size, whether that is one site or three, it is the customer those vendors take last and configure least. The appeal gap is a workflow failure, not a technology gap: nobody has time to file. If the partners open three centers, the specification is written once and deployed three times, which makes the design engagement more valuable, not less. Scope rule (Rick, 2026-11-03): the engagement covers this center and one pick per system; another center on the same picks is a smaller follow-on, mostly Phases 4 and 5; a center that wants a different system is its own selection for those categories, quoted and approved in writing first.

**What the agent does.** Detects authorization-required orders at scheduling. Assembles the documentation packet from the referral and the RIS. Submits via the payer's API where one exists (see dependencies), via EDI 278 where supported, and otherwise prepares a complete packet for a human to submit. Tracks every open request against the 7-calendar-day standard and 72-hour expedited timeframes that bind impacted payers from 2026-01-01. On denial, drafts the appeal with the clinical rationale and queues it for a human signature. Reports the appeal rate and overturn rate weekly, which is the number the owner should watch; the appeal rate is the headline of the Monday owner report (#4), because it starts near zero for a new center, is measurable from week one, and is entirely attributable to the system. The denied-and-never-appealed volume is abandoned revenue, not labor savings; no recovered-dollar forecast is possible without the center's payer mix and denial volume, and none is promised.

**How it is built.** Two deliverables, per the architecture standard at the end of this document: a deterministic service (order detection, packet assembly, submission, deadline tracking) that works without any model, and an agent surface that operates it. The service is what goes in the specification and what any integrator can take over. The agent is the replaceable part.

**Effort:** Large. The orchestration logic is Medium; payer connectivity is what makes it Large, because each payer and radiology benefit manager is its own integration.

**Risk:** Medium. A missed deadline delays a scan; it does not harm a patient directly. A human signs every submission and every appeal in phase one. That sign-off is deliberate design and the FDA boundary, not a cost. **Graduation criterion, stated in the specification:** sign-off moves from every item to a sample only after a defined volume at a defined accuracy, measured, and only with the owner approving the change. Until then, every item.

**Dependencies.**
- RIS order and scheduling feed (HL7 v2 ORM/SIU, or the RIS's own API; make this a contract term, see #3).
- Payer FHIR Prior Authorization APIs, required of impacted payers by 2027-01-01 under CMS-0057-F. The rule covers Medicare Advantage, Medicaid and CHIP (fee-for-service and managed care), and QHP issuers on federally facilitated exchanges. It binds payers, not providers, and guarantees nothing about data quality or ease of connection. Almost 63% of medical plans report they are developing such an API (2025 CAQH Index, payer self-report).
- Commercial plans outside the rule: EDI 278 or human submission.
- Payer mix: not verified for El Paso. Ask Fernando.

**Compliance constraints.**
- Business associate agreement with the center before any PHI flows (45 CFR 164.502(e); settled).
- The AI vendor's BAA envelope: Anthropic's agreement covers Skills, Web Search, Memory, Bash tool, and Text Editor tool, but excludes Computer Use and Web Fetch. Those are the two capabilities one would reach for to drive a payer portal with no API. **Portal screen-driving against PHI is not available inside the BAA.** Design through APIs, EDI, and a human step. Coverage depends on BAA version (Enterprise features for versions accepted after 2025-12-02; Messages API features after 2026-04-01). Confirm the applicable version in writing.
- Texas SB 1188: electronic health records with Texas patient data must be physically stored in the US as of 2026-01-01. Verify US residency for every component including the model provider.
- Texas HB 300 (Health and Safety Code ch. 181), verified against the statute text by Sherlock 2026-11-03: the covered-entity definition reaches Rick directly (storing, transmitting, or possessing PHI; contractor of a covered entity). Training within 90 days of hire with a signed statement kept 6 years; retraining only after a material change in law (no fixed refresher; never "every two years"). Electronic record to the patient within 15 business days of a written request. AG penalties up to $5,000 negligent, $25,000 knowing, $250,000 for financial gain, $1.5M a year for a pattern; a $250,000 yearly cap where the data was encrypted or policies and training were in place, which is the design argument for encryption and a training record. Since 2025-09-01 (HB 4224, 181.105) the center must post record-request and complaint instructions on its website and at the facility; that duty is the center's.
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

## 4. Owner operational reporting

**Scope rule (Rick, 2026-11-04, revised 09:57: two views of one system; revised again in the final round: all three owners see both views, the business-health view is owned by the practice; Luis OK'd). The slide 17 heading is "One system, two views. All three of you see both."** The operations view carries operations: volume by modality, turnaround, scheduled versus completed, no-shows, open slots, payer authorization turnaround, appeal status counts, scanner uptime, staff hours and running costs against budget. The practice's view (Dr. Ramos) carries revenue: collections, denials and appeals won, revenue by payer. Why: the owners earn through the operating company's fixed fees, so their numbers are costs, uptime and operations; equipment uptime matters because the equipment company carries the loan; practice revenue belongs to the practice. No revenue per slot, no referrer value, no paid-versus-read view in either. Referral trends, if the owners ask for them, are a volume count framed as operations, and by default stay out of both views.

**The manual process.** The owner pulls RIS reports for volume and turnaround and the authorization status out of whatever tracks it, and puts them on one page by hand or not at all.

**Evidence it is costly.** **None found, and the research says so plainly.** There is no benchmark literature on what imaging center owners want from dashboards, and no study of the gap between RIS-native reporting and owner needs. The structural claim is defensible without a study: RIS reporting is built for radiology operations, and the owner's one page needs RIS data and the authorization queue together.

**Recommendation: BUILD.** Custom by nature because it encodes one owner's definition of the numbers that matter. Smallest compliance envelope of the five (no patient-facing surface). Cheapest to build. It is the artifact the owner personally looks at, which keeps Rick in the room. The appeal status counts from #1 are the headline of the Monday report.

**The owner agent (decided by Rick, 2026-10-06).** On top of the reporting service, a read-only conversational agent the partners can ask open questions of, each over their own view: volumes by modality, cancellations, no-shows, open slots, turnaround, authorizations waiting, appeal status counts, scanner uptime, staff hours and running costs against budget for the owners; collections, denials and appeals won, revenue by payer for the practice. It reads the center's own database and answers in plain words. Lowest risk of any agent in this inventory: read-only, no action on the world, no patient contact, no clinical surface, and it sees nothing the owner does not already see. Because it reads the center's own data, the AI vendor's BAA exclusions (Computer Use, Web Fetch) do not apply to it. Specified in Phase 2 at no change to the Phase 2 price. Strongest candidate for the first demonstration.

**Effort:** Small to Medium, depending on billing data access. **Risk:** Low.

**Dependencies.** RIS reporting export or database access, a contract term under #3; the authorization queue from #1. Ask Fernando what he wants on one page every Monday morning; that answer is the specification.

**Compliance.** "Business analytics" and "practice and inventory management" are named in 21 U.S.C. 360j(o)(1)(A). PHI is present in the data, so the BAA and SB 1188 residency still apply, but no patient communication is involved. The owner agent stays inside the same exclusion: it answers questions about the business and never reads an image, selects a protocol, recommends a study, or addresses a patient's care.

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
- Texas Chapter 181 (HB 300) sets a shorter deadline than HIPAA's 30 days: **15 business days from a written request for an electronic record** (181.102, verified 2026-11-03). The tracker's clock is built to this one.
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

**The QR envelope (Luis's idea, 2026-11-04 final round; on slide 16).** The agent generates the request packet together with a QR-coded envelope label; the disc comes back in that envelope; staff scan the QR and the imported images route to the right patient and study, and the radiologist is notified. The tracker shows every open request and its days outstanding. Spoken line: "The exchange between facilities is still manual nationwide; I automate everything on our side of it."

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

**Recommendation: BUY (RIS/PACS).** Not a differentiator and already solved. No custom touch: referrer-level detail stays out of the owner reporting view in #4 (Rick, 2026-11-04); a referral volume count can be added as an operations requirement if the owners ask.

---

## 13. Protocol selection, clinical appropriateness, anything touching the image

**Why it is listed.** Someone at the table may ask whether the agents can help pick protocols or check appropriateness. The answer must be no.

**Evidence.** The moment software interprets image data, or recommends which study to order, it leaves the administrative support exclusion at 21 U.S.C. 360j(o)(1)(A) and enters device-regulated territory, where the Clinical Decision Support criteria at 360j(o)(1)(E) apply (guidance revised 2026-01-06 and 2026-01-29). Texas SB 1188 separately requires disclosure of AI used for diagnostic purposes. Evidence: High.

**Recommendation: DECLINE, and say so out loud.** The agents stop at the clinical boundary. This is also the discipline that keeps RadAssist on the right side of the line.

---

## 14. Radiology report assistance (RadAssist, extended to the center)

**Why it is listed (added 2026-10-14).** The partner's three stated wants, in Rick's 10-10 email to Luis, were "scheduling, answering patients, and requesting medical records." In a radiology practice "records" runs in two directions: the report the radiologist produces and sends out, and the prior studies and outside records the center requests and brings in. #6 and #7 cover the second direction. This candidate is the first, and it is the one thing in the inventory that already exists and is in daily use. The two must not be conflated; the deck asks Luis which direction the partner meant.

**The manual process.** The radiologist reads the scanner's calcium score output, transcribes per-vessel and total Agatston scores, looks up the MESA percentile, and dictates or types the report. Luis's own figure before pre-fill: fifteen calcium score studies at about twenty minutes each (Luis to Rick, 2026-08). That is one radiologist's number, not a benchmark; no literature benchmark is used.

**What exists today (updated 2026-11-01).** RadAssist (radassist.app): browser-based structured reporting with three modules in production and in daily use by Dr. Ramos: calcium scoring, thyroid ultrasound (ACR TI-RADS), and Spine MRI (cervical, thoracic, lumbar; shipped 2026-10-31, from his template and his answers, every rule his). For calcium the radiologist snips the scanner's report or dose screen and pastes it; RadAssist reads the per-vessel scores, total, age, sex, and DLP, shows every value with a confidence mark, and applies nothing until he clicks Apply. For thyroid and spine he enters what he graded, one dropdown per sentence, and the impression writes itself in the order he set; unreviewed spine levels never print as normal. It drafts the report from his own template. No PHI is stored server-side; patient inputs are computed in the browser. It does not read DICOM, does not touch the PACS, and does not interpret an image. The Exa viewer at Luis's current site is server-side rendered and never exposes a DICOM object to the browser, which is why the screen-capture path exists at all (research brief, 2026-09-16).

**Recommendation: BUILD, as an extension of existing product.** At a center that owns its PACS and RIS, the integration path is named and both halves are contract terms under #3:

- **Study context in:** DICOM Modality Worklist and C-FIND/C-MOVE query/retrieve, or DICOMweb where the PACS documents it, so the report assistant knows the study it is drafting against. Contract term four.
- **Signed report out:** HL7 v2 ORU, the standard result message, into the RIS. Contract term two (interface count and fee fixed at signature). Verify before signature that the RIS accepts an inbound ORU result; Konica Minolta's Exa, for one, documents only outbound report paths. This is a Phase 1 evaluation item, not an assumption.

**The autonomy boundary, which is the point.** The agent drafts; the radiologist signs. Nothing clinical leaves the center without a human signature, and the sign-off does not graduate to a sample the way #1 may: a report is a clinical document and every one is signed. This is also the FDA line: the tool formats numbers the scanner already measured against the radiologist's own template. It does not interpret an image, select a protocol, or recommend a study. Anything that would (follow-up interval recommendation, growth flagging) is #13 and declined.

**Effort:** Medium. The reporting modules exist; the work is the two interfaces and per-center configuration. **Risk:** Low; a wrong value is caught by the radiologist at Apply, before signature, the same place it is caught today.

**Dependencies.** PACS DICOM worklist and query permission (#3). RIS inbound ORU interface, verified in evaluation. A per-center instance (see deployment standard below).

**Compliance.** BAA with each center; SB 1188 US residency; HB 300. Texas SB 1188's AI disclosure for diagnostic use: the radiologist is the diagnostician and the tool is his drafting aid, but the specification states the disclosure position explicitly rather than assuming it.

**Ownership.** Tier 3: Rick's existing product, extended for the center; how the center uses it is written into the contract. No license terms are discussed at the table and no arrangement of Luis's is described in any pitch document (Rick, 2026-11-03; "perpetual" was already out 11-02). Per-center templates, mappings, and configuration are Tier 2, the center's outright.

---

## Deployment across centers: one environment, isolated instances, never one shared database

Deployment standard set by Rick, 2026-11-02 (superseding the same-day "one shared stack for same owners" rule and the 2026-10-14 one-instance-per-center standard), carried on the report assistance slide (last block) and on page 6 of the architecture document. **The default is the industry standard, security first.** One specification, written once and reused for every center. One environment, under one contract, which keeps the cost low. Inside it, each organization (each center, or each owning entity) runs in its own isolated instance: its own database and its own encryption keys, its own credentials with role-based access, and its own audit log, plus its own model account under its own BAA. No organization can see another's data, by construction, not by a filter.

**The two variants.** One owner, or one joint venture, owning all the centers: the default fits as it stands. Separately owned centers where an owner wants fully separate hosting and separate books: a fully separate stack for that center, at higher cost, as that owner's choice. Either works. What is never built is one shared database with a center column.

**Why the default runs that way.** The isolation lives at the data layer, where a regulator, an auditor, or a partner's lawyer expects to find it, so one environment can be operated, patched and monitored once while nothing that holds a patient is shared. Fully separate stacks add nothing for security that the isolated instance does not already provide; they add separate hosting bills and separate books, which is a legitimate reason for a separately owned center and not a security argument. Any view that spans organizations is a later, explicit decision by all the principals, built read-only over the separate databases, never as a merged record.

**What is shared in both variants.** The specification (Tier 1), written once. Rick's engines (Tier 3), used by the center under the contract. Runbooks and vendor evaluation criteria. In the default, the environment and its operations. Never a database, a key, a login, or an audit log.

**Not a settled fact.** Whether the centers share owners, a back office, or a vendor stack is a question for Luis, and the design survives either answer. Staff can be shared without the data being shared. The count of vendor contracts that carry the four access terms (#3) changes with the answer; the data boundary does not.

## Architecture standard: the software is the capability, the agent is the operator

Decided by Rick, 2026-10-06, and applied to every build in this inventory. Every automation is two deliverables. First, a deterministic service with a clean interface that works without any model: order detection, packet assembly, deadline tracking, the waitlist ranking, the records clock, the reporting joins. Second, an agent surface that operates the service. The service is auditable, testable, survives any model change, is what the specification describes, and is what any integrator can take over, which is what keeps the continuity promise honest. The agent is the replaceable part: the model vendor, the BAA envelope, and the pricing can all change without breaking the center.

Three kinds of agent, by blast radius:

| Tier | Agent | Risk | Status |
|---|---|---|---|
| A | Owner agent (#4): read-only questions over the two views (operations and costs for the owners, revenue for the practice) | Lowest. Reads, never acts. No patient contact, no clinical surface. Named in the FDA exclusion as business analytics and practice management. | Specified in Phase 2. No price change. |
| B | Workflow agents (#1, #5, #6): act on the world, a human signs | Medium. Bounded, human-signed, with a written graduation criterion. | As already specified. |
| B | Report assistance (#14): drafts, the radiologist signs | Low. A clinical document, so every report is signed and the sign-off never graduates to a sample. | Exists; extended per center. |
| C | Patient-facing voice (#9) | Highest. Chest pain and Spanish are safety and reputation events. | Buy from a vendor. Unchanged. |

A locally hosted model is a specification-phase option for the no-API payer portal (it keeps the AI step inside the center's environment and sidesteps the vendor BAA's Computer Use exclusion), for SB 1188 residency, and for high-volume low-complexity classification. It does not replace reasoning-heavy work such as drafting an appeal. Portal automation is the most fragile item in this inventory and is not promised at the table. **Privacy, stated precisely (Rick, 2026-11-03):** with an external model API the prompt data is sent to the provider; the BAA makes the provider a business associate and zero-retention terms govern storage and training. Swapping names, MRNs, member IDs, dates of birth and phone numbers for tokens before the call reduces what the provider sees but does not remove PHI, because a prior authorization packet or an appeal has to carry the clinical story, which in context is still health information about an identifiable patient; it is not de-identification and the BAA is still required. Only a model running at the center keeps PHI away from an AI provider, and even then PHI still leaves for the payer, the clearinghouse, texting, and encrypted offsite backup. Never say "no data leaves." The three hosting options are compared under "Running costs and hosting" below.

## RIS and PACS: one cloud system for a single center (Rick, 2026-11-03)

**Position.** For one center, recommend one cloud-hosted system that bundles RIS and PACS: one vendor, one support line, one contract; no RIS-to-PACS interface to buy, maintain or break; one worklist; faster go-live; the lean control the owners want. The cost is lock-in and giving up best-of-breed, mitigated by the four contract terms (#3): data export in DICOM and HL7 at no penalty, interface fees fixed at signature, API access, worklist access. Split RIS from PACS only if the radiologists have a strong PACS preference or want multi-site reading from day one. Dictation is selected separately, and the reading radiologists choose it. Exa is named only as one example of an integrated RIS, PACS and billing system; no vendor is the pick until Phase 2.

**Spoken line.** "For a center your size I'd lean toward one cloud system for RIS and PACS: one vendor, fewer interfaces, faster opening. The contract is what keeps you free to leave. Picking the vendor is Phase 2."

**Exa, the likely pick (Rick, 2026-11-04 final round; slide 28 carries it).** Exa is the likely RIS and PACS because one of the group's centers (Binton) has already signed it; the name stays off client-facing documents. Recommendation: negotiate as three centers for volume pricing, and put the four access terms (API access, HL7 interface count and fee schedule, data export, DICOM query) into the Exa contract. The final pick is still Phase 2, with the radiologists in the demos.

**Starting shortlist (Sherlock, `SHERLOCK-RIS-PACS-LANDSCAPE-2026-11-03.md`; RFP invite list, not a decision).** RIS and PACS: Konica Minolta Exa PACS|RIS, RamSoft OmegaAI, Novarad, Intelerad; the 2026 Best in KLAS PACS winners (Sectra, Agfa) are sized and priced for hospitals; a premium viewer (Sectra or Visage) with a separate RIS only if the radiologists insist. Dictation: the RIS's built-in dictation, PowerScribe One (Microsoft), Fluency for Imaging (Jacobian; 2026 Best in KLAS, imaging speech recognition), Rad AI; ask the radiologist group what it already licenses. Billing: outsource to an imaging-specialized RCM firm at opening on a short contract, clearinghouse and data in the center's name; clearinghouses in common use are Waystar, Availity, TriZetto, Office Ally, Quadax (2026 Best in KLAS); document a second clearinghouse path. Evaluation criteria and weights, as a starting point: radiologist reading experience 20%, five-year total cost including interfaces, storage growth and dictation 20%, integrated workflow front desk to claim 15%, security and hosting 15%, data ownership, export and API openness 10%, single-site references 10%, timeline and support 10%. Contract by about February 2027 for a June opening. No list prices, market shares or interface fees are sourced; every price in this market is a quote. Deck slide 28 carries the shortlist.

**Integration readiness (R21, Rick 2026-11-03).** `SHERLOCK-INTEGRATION-READINESS-2026-11-03.md` is internal reference only: no score, ranking or vendor winner from it goes into the deck or leave-behind. Client-facing wording is one line (slide 28): every system is scored on how easily it connects to the rest, and the integration terms go into the contract; integration readiness is a named weighted criterion in the Vendor Selection Report, with no weights or scores shown before Phase 2.

**Systems selected in Phase 2 (Rick, 2026-11-03 17:48, final: owners' asks first, then imaging-specific).** (1) scheduling; (2) RIS and PACS, evaluated both as one bundled cloud system and as separate best-of-breed RIS plus PACS (Exa is one example); (3) prior authorization and eligibility; (4) patient phones, IVR and AI answering; (5) radiologist voice recognition and dictation; (6) billing and clearinghouse; (7) imaging-specific: modality integration and worklist, reading workstations, image sharing (CD and cloud). Removed as generic, non-imaging items: patient portal and intake, fax and document management, IT, security and backup as a separate line (they are covered inside the RIS selection and the Phase 3 design). Patient phones/IVR (patient-facing) and radiologist dictation (clinical) stay as two separate named rows.

## Running costs and hosting: not in the fee, the center's accounts, three options (Rick, 2026-11-03)

**The rule.** Everything that keeps the build running after opening (cloud hosting, model usage, texting, clearinghouse transactions, interface engine, security monitoring, penetration test, backups) is outside the $45,000. Each account is opened in the center's name on the center's card, the center signs each BAA, Rick is an administrator, nothing is marked up, and the center gets a one-page monthly statement: each vendor's bill, the volume handled, cost per authorization, hours saved. The estimate comes with a cap Rick cannot exceed without written approval. Phase 1 gives a ballpark range per build item (inside the make-or-buy); Phase 3 delivers "Total cost of ownership and operating budget," which the owner picks from.

**Estimate (Sherlock, `SHERLOCK-RUN-COSTS-2026-11-03.md`; every line is a published list price to re-check or Sherlock's estimate, none is a quote).** At an expected 650 studies and 300 prior authorizations a month, vendors run about $930 (low) / $1,950 (expected) / $4,180 (high) a month in the cloud option: hosting $370 to $880 (mostly fixed), model tokens $60 to $400 (the small line even at 900 studies a month), texting $0 to $600 (use the RIS vendor's texting under its BAA or a HIPAA-eligible SMS vendor; Twilio's BAA tier carries a commitment), clearinghouse $100 to $1,000 (often inside the billing contract already; ask the billing vendor first), interface engine $0 to $300 (a community fork of the last open Mirth or a small custom HL7 listener; commercial Mirth is now licensed), monitoring, security and an amortized annual penetration test $400 to $1,000. One-time setup outside the fee about $6,000 to $25,000 (penetration test, clearinghouse enrollment, RIS interface fee, SMS registration), most of it negotiable through the RIS contract. Frame it against staff time, never against "AI".

**The three hosting options for the Phase 3 deliverable.** A, fully hosted in the center's own cloud account under the cloud provider's BAA, model via Bedrock or Anthropic under a BAA with zero retention: highest uptime, least maintenance, best model quality, no new facility duties; clinical content goes to the model provider under the BAA; one-time $6,000 to $25,000; vendors about $930 / $1,950 / $4,180 a month. B, hybrid, a Mac mini at the center running the agents and a tokenization layer, cloud database and backups: names and IDs never reach the model provider, but clinical content still does so the BAA is still required; two environments to patch; the agents pause in a power or internet outage; the tokenizer is custom code that must be tested against every packet type; the center takes on physical-safeguard duties (45 CFR 164.310); one-time $12,000 to $37,000; vendors about $1,050 / $2,050 / $4,300 a month plus $500 to $1,500 a month of extra labor. C, fully on-site with an open-weight model on Mac Studio class hardware with a spare: no AI provider sees PHI; no per-token cost; but open models in the 70B to 120B class are noticeably weaker at long, rule-heavy work such as matching payer criteria and drafting appeals, so quality must be measured on synthetic packets before committing; slower; Rick owns model selection, upgrades and re-validation; single-site uptime, theft risk and the full safeguard burden; hardware obsolete in three to four years; one-time $27,000 to $52,000; vendors about $1,200 / $2,000 / $3,500 a month plus $2,250 to $4,500 a month of extra labor. Recommendation: A, with B's tokenization step run inside the cloud account if the owners want identifiers kept from the model provider; B's on-site box only if the RIS forces a local HL7 endpoint; C not for opening, offered later as a measured side-by-side pilot. Support after opening (APPROVED by Rick 2026-11-03 17:54): a support plan at $3,000 a month for up to 20 hours, $150 an hour beyond, from June 2027, 12-month term with a 90-day check-in, separate from the $45,000; covers monitoring, fixes, updates to Rick's builds, vendor coordination and a response-time promise; "or a role on your team" stays the alternative. Sherlock's three-year totals assumed a $4,000 retainer and are superseded; no three-year total is quoted until Phase 3 produces one. Contract clause draft: `private/RUN-COSTS-CONTRACT-CLAUSE-2026-11-03.md`.

## Opening checklist and ideas worth a look (R24, R24a, Rick 2026-11-03)

**Opening checklist (deck slide 30; required to open and bill, not Rick's build, outside the $45,000, each with a named owner in the Phase 1 Requirements and Roadmap; from `SHERLOCK-SYSTEMS-GAP-AUDIT-2026-11-03.md`).** Payer enrollment and radiologist credentialing (Medicare IDTF 855B, 42 CFR 410.33, Texas Medicaid, TRICARE, commercial, CAQH; must start in Phase 1; longest lead item); ACR accreditation for MRI and CT (42 CFR 414.68) with CT dose records, MR safety policy and roles, physician peer review, physicist QC; Texas DSHS CT registration, shielding, dosimetry, operator credentials (25 TAC 289.226, 289.227, 289.202); CLIA certificate of waiver before any fingerstick creatinine (42 CFR 493); HIPAA Security Rule basics (45 CFR 164.308 to 164.316; Texas breach notice); HB 300 staff training within 90 days of hire (HSC 181.101). Compliance-only systems (dose monitoring and DIR, MRI safety screening, contrast and injector logs) are bought inside the RIS/PACS or a dose tool and never pitched as value.

**Ideas worth a look (deck slide 31; not in the fee; scoped only if asked; from `SHERLOCK-IMAGING-GAP-VALUE-2026-11-03.md` and the gap audit).** Lead: follow-up recommendation tracking on top of closed-loop critical results (tracked follow-up completed 78% vs 52%, Respir Med 2022, PMID 35051877; a private group's tool raised lung-nodule follow-up from 26.5% to 59.7%, BMJ Open Qual 2019, PMID 31206047; hospital settings; outreach via the referrer only; no malpractice dollar figure exists; Rick build, 3 to 5 weeks estimate). Second: staff-generated good-faith cost estimates at scheduling (UC Irvine, 470,422 encounters, OR 1.91 for completion, Clin Imaging 2025, PMID 39736182; association, not causation; RIS or RCM feature plus a small extension of #2). One-liners: structured referrer e-orders (Emory, 51% of abdominal CT requisitions carried the cancer history, PMID 40517119; the denial link is inference); peer learning instead of score-based peer review (PMID 38113549; bought); contrast pre-screening plus point-of-care creatinine (needs the CLIA waiver; bought).

## Ownership, in three tiers

Decided by Rick, 2026-10-06. The specification: the center's outright. Center-specific code (configuration, workflows, integrations, data mappings, reports): the center's outright, in a repository under its organization, with Rick's access revocable. Existing product of Rick's that he extends for the center (the prior auth engine, the backfill engine, the reporting core): Rick's, with the center's use of it written into the contract, so it can keep running it for its own operations. At the table the positioning is a scope of work, a design for one imaging center that can be put anywhere; the contract settles who owns what, and the center owns its configuration and its data (Rick, 2026-11-03). This is what keeps the engagement price where it is.

## What this inventory deliberately does not contain

- Any cost-structure percentage for an imaging center. Ask Fernando for his own actual numbers from Southwest X-Ray. Do NOT name Desert Imaging; he did not found it.
- Any CAQH per-transaction cost, vendor price, HL7 interface fee range, imaging prior auth denial rate above the verified 4.94% and 7.7%, percentage of advanced imaging requiring authorization, records cost per request, or count of independent imaging centers. The research could not verify any of them. See Section 8 of the research brief.
- A market-sizing argument. This is a build for one center, which is the reference implementation, operated by Rick, with that center's service terms fixed in writing. Consolidation (RadNet, SimonMed, Akumin, Rayus, Touchstone, US Radiology Specialists) is removing the single-site prospects that would be a market, and the partner lived that from the selling side.
