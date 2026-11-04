# Integration Readiness: RIS/PACS, Dictation, Billing, Phones vs Rick's Five Builds

Prepared by Sherlock, 2026-11-03. Companion to `SHERLOCK-RIS-PACS-LANDSCAPE-2026-11-03.md` and `AUTOMATION-CANDIDATES.md`.

**Read this first: method limits.** The web search provider failed for this entire session, so this report rests on (a) vendor pages and developer docs I fetched directly today, and (b) my working knowledge. Most RIS/PACS vendors in this market keep HL7 specs, API docs and sandbox terms behind a customer or partner login, so "not public" is itself a finding, not a gap in my effort. Every score below is a **provisional desk score to be replaced by RFP answers**. Confidence key: **HIGH** = read on a primary source today. **MEDIUM** = consistent long-standing industry knowledge or a vendor statement without technical detail. **LOW / UNVERIFIED** = my expectation; must be confirmed in the RFP. **[MKT]** = marketing claim.

---

## Plain-English summary

1. **Only one shortlisted vendor publishes a real, open developer API today: Intelerad's Ambra (InteleShare) v3 API.** I read it directly: public documentation, OAuth login, study search and C-FIND, HL7 inbound and outbound endpoints including report extraction and templating, HL7 transform rules, and a full webhook system (add, list, run, event). HIGH. That makes Intelerad/Ambra the easiest platform for Rick's event-driven builds (backfill, records tracker) if the center picks it. Caveat: Ambra is the cloud image-exchange and archive layer; the RIS (InteleRIS) API is not public, so scheduling events may still mean HL7 SIU.

2. **RamSoft OmegaAI is the best bet for an integrated, cloud-native RIS+PACS with modern APIs, but the API is not public.** RamSoft states OmegaAI is "built on HL7 and FHIR standards" [MKT, HIGH that the statement is published]. No public developer portal or sandbox found. Ask for the FHIR resource list, write access, and sandbox in the RFP.

3. **Konica Minolta Exa is the strongest imaging-center product with the weakest public integration story.** No public API or HL7 spec on its pages (HIGH that none is published). Our own earlier evaluation note flagged that Exa documents only outbound report paths; inbound ORU acceptance from RadAssist is the single most important thing to verify with Exa. Until verified, Exa scores lowest on RadAssist fit among the four.

4. **Novarad is an HL7-first, conservative integrator.** A customer quote on its site calls HL7 integration a top feature [MKT]. No public API or FHIR documentation found. Expect HL7 v2 plus DICOM, and little else. MEDIUM.

5. **Agfa (and Sectra) publish conformance statements; that is how enterprise vendors signal readiness.** Agfa's site links public DICOM, HL7 and FHIR conformance statements and IHE integration statements (HIGH). Sectra publishes DICOM conformance and IHE statements (MEDIUM). They are more integration-ready on paper than the small-center vendors, but sized and priced for hospitals, as the landscape report says.

6. **Every build Rick specified can run on HL7 v2 plus DICOM alone.** APIs and webhooks make the builds cheaper and less fragile, but none of the five builds requires a vendor API. That is the most important finding for contract strategy: write HL7 SIU/ORM/ADT outbound, ORU inbound, DICOM MWL and Q/R, and a nightly bulk export into the contract, and every build is protected regardless of vendor.

7. **Dictation:** if the radiologists use the RIS built-in dictation, RadAssist has to hand its draft to that RIS (inbound ORU or a paste/context integration). If they use PowerScribe One, the draft path is PowerScribe's own integration surface, which Microsoft documents publicly for administrators but which, for third-party content insertion, is partner-gated (LOW). Rad AI integrates alongside PowerScribe historically [MKT]. Pick the dictation tool with RadAssist's hand-off in mind.

8. **Billing and phones:** clearinghouses with public APIs and sandboxes (Availity developer portal, Stedi) make the prior-auth agent's EDI 278 and 270/271 path buildable without a sales cycle (MEDIUM). Waystar's APIs are partner-gated (LOW). For phones, buy a vendor that signs a BAA and exposes call events (RingCentral, Zoom Phone, Twilio under its BAA tier) (MEDIUM).

9. **Interface fees:** none of these vendors publish interface pricing (HIGH that none found). Industry practice remains a per-interface build fee plus annual maintenance; for a center with five builds, that is potentially four or five interfaces. Negotiate a bundled "open interface" clause. Single highest-value contract line for Rick.

### Readiness table (provisional, out of 100)

| Product | HL7 out (SIU/ORM/ADT) | Inbound ORU | DICOM MWL + Q/R | Public, documented API | Webhooks / events | Sandbox | Bulk export | Score | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| Intelerad (InteleRIS + Ambra) | Yes (expected) | Yes, Ambra HL7 endpoints (HIGH) | Yes | **Yes, Ambra v3 public (HIGH)** | **Yes, documented (HIGH)** | Partial; ask | Via API (HIGH) | **82** | MEDIUM-HIGH |
| RamSoft OmegaAI | Yes (expected) | Likely; verify | Yes | FHIR stated, not public [MKT] | Unknown | Not public | Ask | **70** | MEDIUM |
| Agfa Enterprise Imaging (contrast) | Yes, conformance published (HIGH) | Yes (expected) | Yes | FHIR conformance published (HIGH) | Unknown | Partner | Yes | **72** | MEDIUM |
| Sectra PACS (contrast) | PACS side; RIS from partner | Yes (expected) | Yes, DICOMweb (MEDIUM) | Partner-gated | Unknown | Partner | Yes | **62** | LOW-MEDIUM |
| Novarad (NovaRIS/NovaPACS) | Yes (MKT customer quote) | Likely; verify | Yes | Not found | Not found | Not found | Ask | **55** | LOW-MEDIUM |
| Konica Minolta Exa PACS\|RIS | Yes (expected) | **Unverified; prior note says outbound only** | Yes | Not found | Not found | Not found | Ask | **50** | LOW-MEDIUM |
| PowerScribe One (dictation) | Receives orders, sends ORU | n/a (it is the report source) | n/a | Admin docs public (HIGH); 3rd-party API gated | Unknown | Partner | n/a | **60** | LOW |
| Fluency for Imaging (Jacobian) | Same pattern | n/a | n/a | Not found | Unknown | Unknown | n/a | **50** | LOW |
| Rad AI | Integrates beside PowerScribe [MKT] | n/a | n/a | Not public | Unknown | Unknown | n/a | **55** | LOW |
| RIS built-in dictation | Native, no interface | n/a | n/a | Inherits RIS | Inherits RIS | Inherits RIS | Inherits RIS | **inherits RIS** | MEDIUM |
| Availity (clearinghouse) | EDI 270/271, 278, 837 | n/a | n/a | Public developer portal (MEDIUM) | Polling mostly | Yes (MEDIUM) | Reports | **75** | MEDIUM |
| Stedi (clearinghouse API) | EDI as JSON API | n/a | n/a | Public docs (MEDIUM) | Yes (MEDIUM) | Yes (MEDIUM) | Yes | **80** | MEDIUM |
| Waystar | EDI | n/a | n/a | Partner-gated (LOW) | Unknown | Partner | Reports | **55** | LOW |
| Office Ally | EDI via SFTP | n/a | n/a | Limited (LOW) | No | Limited | SFTP | **40** | LOW |
| Phones: RingCentral / Zoom Phone / Twilio | n/a | n/a | n/a | Public APIs (MEDIUM) | Yes (MEDIUM) | Yes | Call logs | **75** | MEDIUM |

---

## Scoring weights and why

| Criterion | Weight | Why this weight |
|---|---|---|
| HL7 v2 outbound (SIU, ORM, ADT) | 20 | Feeds prior auth (ORM), backfill (SIU cancellation) and reporting. Four of five builds need it. |
| Inbound ORU acceptance | 15 | The only path for RadAssist's signed report into the RIS. One build, but it is the existing product. |
| DICOM MWL + Q/R (or DICOMweb) | 15 | Records tracker retrieval and RadAssist study context. Standardized, usually available. |
| Public, documented REST/FHIR API | 15 | Cuts build effort and fragility; needed for clean reporting reads. |
| Webhooks / events | 10 | Real-time backfill and deadline triggers without polling or HL7 engines. |
| Sandbox / test environment | 10 | Rick builds before opening (build ~Mar 2027); without a sandbox, no pre-opening testing. |
| Bulk data export | 10 | Owner reporting and exit protection. |
| Fee transparency, BAA | 5 | All serious vendors sign a BAA (MEDIUM); fees are nowhere public, so this barely separates them. |

Scores above are my estimate against these weights from what is published. An "unknown" scored half credit; "not found publicly" scored a quarter. Expect every non-Ambra score to move up to 15 points once RFP answers arrive.

---

## Best pairings per build

| Rick's build | What it needs | Easiest pairing | Fallback that still works |
|---|---|---|---|
| **#1 Prior-auth agent reading orders** | ORM or order API from RIS; payer FHIR PA APIs (2027-01-01 for impacted payers) and EDI 278 | **RamSoft OmegaAI (FHIR) or Intelerad + Stedi or Availity** for the 278 leg | Any RIS with HL7 ORM out into an interface engine; human submission for commercial plans |
| **#5 Cancellation backfill** | Cancellation events (SIU S15 or webhook), write-back to book a slot, SMS under a BAA | **Intelerad/Ambra webhooks** if scheduling events surface there; else **OmegaAI** API | HL7 SIU feed plus scheduler doing the actual booking by hand (agent offers, human books) |
| **#6/#7 Records inbound/outbound tracker** | DICOM Q/R or DICOMweb against PACS, import of outside studies | **Intelerad/Ambra** (public study, C-FIND, push and share endpoints, HIGH) | Any PACS with DICOM C-FIND/C-MOVE permission written into contract |
| **#4 Owner reporting agent** | Bulk or API read of RIS + billing data | **Intelerad (API) or OmegaAI (FHIR)** + a billing vendor with exportable reports | Nightly database export or scheduled CSV; contract term under #3 |
| **#14 RadAssist drafting into RIS** | MWL/Q/R for context; inbound ORU (or dictation integration) for the draft | **Intelerad (Ambra HL7 inbound, HIGH)** or **RamSoft** if inbound ORU confirmed; with **RIS built-in dictation** | PowerScribe One if rads already license it, via partner integration; **Exa only after inbound ORU is proven in a demo** |

**Overall easiest stack for Rick's builds (provisional):** Intelerad (InteleRIS + Ambra) or RamSoft OmegaAI, RIS built-in dictation, Stedi or Availity for eligibility and 278, a radiology RCM firm on top, and a BAA-signed phone platform with an API. **Hardest:** Exa or Novarad with PowerScribe One and Waystar, all behind partner gates. Note that "easiest to integrate" is one input; the landscape report's reading experience and cost criteria still dominate the vendor choice.

---

## Per-product notes

**Intelerad / Ambra.** Read today at access.ambrahealth.com/api/v3/api.html (branded InteleShare): public v3 Services API with session and OAuth endpoints, `/study/list`, `/study/cfind`, `/study/push`, `/study/push/hl7`, an `/hl7/*` family (add, list, outbound list, extract report, study report, templates, transforms with a test endpoint), and a `/webhook/*` family (add, set, list, run, event). The page also references FHIR. HIGH that these are documented. Not verified: whether the US InteleRIS scheduling module emits events through Ambra, sandbox cost, and API fees. Pain point (MEDIUM): Intelerad is a roll-up of acquired products; confirm which code base and whether Ambra is included or a separate contract.

**RamSoft OmegaAI.** Vendor page: "built on HL7 and FHIR standards" [MKT]. Also offers a patient portal (Blume) and its own AI scheduling and reporting modules [MKT], which could overlap with Rick's backfill build; ask whether the API lets a third party book and cancel. No public developer docs found. Ask: FHIR R4 resource list (Appointment, ServiceRequest, ImagingStudy, DiagnosticReport), write scopes, SMART on FHIR, sandbox, fees.

**Konica Minolta Exa.** Product pages carry no technical integration detail (HIGH); manuals sit in a resource library. Prior project note: only outbound report paths documented. Treat inbound ORU as a pass/fail demo item. Expect HL7 v2 and DICOM to be solid (MEDIUM, large installed base).

**Novarad.** HL7 integration praised in a customer quote on its homepage [MKT]. No public API, FHIR or sandbox found. Confirm ownership and roadmap (open item from landscape report).

**Agfa / Sectra (contrast).** Agfa publicly links DICOM, HL7 and FHIR conformance statements and IHE integration statements (HIGH). Sectra publishes DICOM conformance and IHE statements and supports DICOMweb (MEDIUM). Their readiness is real but sold through enterprise integration teams, not a self-serve sandbox (LOW).

**Dictation.** PowerScribe One administrator documentation is public on Microsoft Learn, last updated Oct 2026 (HIGH); typical integration is orders in by HL7, signed report out by HL7 ORU, desktop context link to PACS (MEDIUM). A third-party draft-insertion API is not publicly documented (LOW). Fluency (Jacobian) and Rad AI: no public API docs found today; Rad AI historically runs beside PowerScribe [MKT]. RIS built-in dictation removes one interface entirely and is the simplest RadAssist target if the RIS accepts inbound ORU or offers a report-draft API.

**Clearinghouses.** Availity runs a public developer portal with sandbox (MEDIUM, not re-read today). Stedi publishes API docs for 270/271 eligibility and claims and signs BAAs (MEDIUM, not re-read today; confirm 278 support, UNVERIFIED). Waystar and Office Ally: limited or partner-gated (LOW). Quadax is the 2026 Best in KLAS clearinghouse (HIGH from landscape report) but its API posture is unknown.

**Phones/IVR.** RingCentral, Zoom Phone and Twilio sign BAAs on specific plans and expose call-event APIs (MEDIUM). This matters for the backfill outbound leg and for any future voice vendor integration. TCPA caps apply regardless of vendor.

---

## Known integration pain points (MEDIUM unless noted)
- Interface fees charged by both sides (RIS and receiving system).
- HL7 v2 "standard" messages vary by vendor; every interface needs mapping and a test cycle. Budget an interface engine (Mirth/NextGen Connect or a cloud equivalent) in the run costs.
- Vendors restricting write access (booking, cancelling) through APIs while allowing reads; backfill needs write or a human step.
- Sandboxes offered only after contract signature; get it written in so Rick can build from ~Mar 2027.
- Version upgrades that break interfaces; contract clause: vendor-caused rework at no charge.
- Bulk export priced at exit; fix price and format at signature.

## RFP questions to send every vendor (copy-ready)
1. List every HL7 v2 message you send and accept (SIU S12-S15, ORM O01, ORU R01 inbound and outbound, ADT, DFT). Provide the spec.
2. Do you accept an inbound ORU R01 preliminary or draft report from a third-party reporting tool? Demo it.
3. DICOM MWL, C-FIND/C-MOVE, and DICOMweb (QIDO, WADO, STOW) for a third-party application: included, and at what fee?
4. Is your REST or FHIR API publicly documented? Read and write scopes? SMART on FHIR?
5. Do you emit webhooks or event notifications for scheduling changes and report status?
6. Sandbox availability before go-live, and cost.
7. Nightly bulk export of RIS and billing data: format and fee.
8. Interface fee schedule, fixed for the term; BAA, US data residency (Texas SB 1188), SOC 2 Type II.

## Sources read today
- Intelerad/Ambra v3 Services Public API: https://access.ambrahealth.com/api/v3/api.html (HIGH)
- RamSoft home and OmegaAI product page: https://www.ramsoft.com/ ; https://www.ramsoft.com/solutions/products/omegaai [MKT]
- Konica Minolta Exa PACS|RIS: https://healthcare.konicaminolta.us/healthcare-it/exa-pacsris
- Novarad home: https://www.novarad.net/ [MKT]
- Agfa HealthCare Enterprise Imaging (footer links to DICOM, HL7, FHIR conformance): https://www.agfahealthcare.com/enterprise-imaging/
- Microsoft PowerScribe One documentation hub: https://learn.microsoft.com/en-us/industry/healthcare/powerscribe-one/
- Everything else: working knowledge, marked LOW or MEDIUM. Re-run with a working search provider before any of this goes in front of Luis or Fernando.
