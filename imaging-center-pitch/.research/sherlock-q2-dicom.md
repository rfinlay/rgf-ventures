# Q2 — DICOM / Imaging Data Access for Small US Outpatient Imaging Centers

Research date: 2026-10-10. Prepared for the RGF Ventures imaging-center engagement (Luis + Fernando Escarzaga, El Paso greenfield).

**Confidence legend:** High = primary technical doc or peer-reviewed source directly verified. Medium = credible secondary source, or primary source seen only via search index. Low = inference, single weak source, or marketing-only.
**VENDOR CLAIM** = vendor marketing/sales page, not a technical specification.
**UNVERIFIED** = could not confirm; see the "Could Not Verify" section at the end.

---

## Executive summary — the three findings that matter for the pitch

1. **DICOMweb is real and broadly specified, but unevenly implemented, and "has an API" is not the same as "has DICOMweb."** Sectra, Fujifilm Synapse and Visage document genuine QIDO-RS/WADO-RS/STOW-RS. Ambra/InteleShare and eRAD expose *proprietary* REST APIs instead. That distinction is the single most important contract question (Q2a).
2. **The "data hostage" narrative is NOT well documented for small outpatient centers.** I found no litigation and no published per-study API-access fee schedule. The credible, citable costs are *migration* costs, and the best hard figures are from 2007 and hospital-scale. Do not use a dollar figure for "API fees" in the pitch — there is no source for one (Q2b). This is a significant negative finding and it changes how the risk should be framed.
3. **The operational metadata thesis is sound, and it is strongest where it is least glamorous.** Study/series/acquisition timestamps, station name and modality are reliably populated because the *scanner* writes them. Operator name, protocol name, body part and CTDIvol are the ones that break in practice, and there is peer-reviewed evidence of exactly that (Q2c). Build the value story on timestamps, not on dose.

A fourth, pitch-relevant correction appears in Q2c: **(0018,1152) is "Exposure" (mAs), not CTDIvol.** CTDIvol is (0018,9345). The brief conflated these. Using the wrong tag in front of Fernando — a 40-year RDMS/RPA sonographer-turned-owner — would be costly.

---

## Q2a. DICOMweb support among PACS/RIS vendors serving small US outpatient centers

### The standard itself (baseline, High confidence)

DICOMweb is the family of RESTful services defined in **DICOM PS3.18**: QIDO-RS (query), WADO-RS (retrieve), STOW-RS (store), plus legacy WADO-URI.
Source: [DICOM Standard, DICOMweb RESTful structure](https://www.dicomstandard.org/using/dicomweb/restful-structure) — accessed 2026-10-10 — **High**.

Azure's docs usefully name the two PS3.18 service families a buyer should ask about by name: the **Studies Service** (PS3.18 ch.10) and the **Worklist Service / UPS-RS** (PS3.18 ch.11).
Source: [Microsoft Learn, DICOM service overview](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicom-services-overview), doc dated 2025-07-23 — **High**.

### Vendor-by-vendor

| Vendor / product | DICOMweb documented? | Evidence class | Extra-cost module? | Confidence |
|---|---|---|---|---|
| **Sectra** PACS / VNA | **Yes** — QIDO-RS provider + client | Published DICOM conformance statement | UNVERIFIED | High |
| **Fujifilm Synapse** PACS | **Yes** — WADO-URI, WADO-RS, QIDO-RS, STOW-RS | Published DICOM conformance statement | UNVERIFIED | High |
| **Visage 7** | **Yes** — QIDO-RS, WADO-RS/URI, STOW-RS | Conformance statement + product page | AI Open API is **invitation-only** | Medium–High |
| **RamSoft** PowerServer / OmegaAI | **Partial/likely** — OmegaAI marketed as built on DICOMweb + FHIR R4; conformance page lists DICOM + FHIR statements but **no DICOMweb-specific doc** | VENDOR CLAIM + conformance index | UNVERIFIED | Medium |
| **Ambra Health / Intelerad InteleShare** | **Proprietary REST, not DICOMweb** — see below | Public API reference, directly inspected | UNVERIFIED | High |
| **Intelerad** (IntelePACS) | InteleShare claimed to expose WADO-RS/QIDO-RS/STOW-RS; **no public developer portal found** | Search-index snippet only | UNVERIFIED | Low–Medium |
| **eRAD** (RadNet) | **Proprietary HTTP API**, explicitly described as "a collection of HTTP commands"; DMWL for worklist. No DICOMweb claim found | Vendor pages | UNVERIFIED | Medium |
| **Merative / Merge** (Unity PACS, Merge PACS) | Conformance statements found cover **DIMSE network interfaces, media storage, modality worklist** — DICOMweb **not** evidenced | Conformance statement index | UNVERIFIED | Low–Medium |
| **Konica Minolta Exa** | Has "a new API" per trade press; **no DICOMweb conformance doc found** | Trade press + VENDOR CLAIM | UNVERIFIED | Low |
| **Novarad** | "DICOM-compliant"; no DICOMweb doc found | VENDOR CLAIM | UNVERIFIED | Low |
| **PaxeraHealth** | "DICOM integration"; no DICOMweb doc found | VENDOR CLAIM | UNVERIFIED | Low |
| **Hyland / Lexmark Acuo** VNA | DICOM + "DICOMweb integrations" asserted; conformance page exists, DICOMweb statement not located | VENDOR CLAIM | UNVERIFIED | Low |
| **Change Healthcare / Optum** enterprise imaging | **UNVERIFIED** — no accessible conformance or developer doc found | — | UNVERIFIED | — |

### Primary sources

- Sectra: [DICOM Conformance Statement, PACS & VNA v28.1](https://medical.sectra.com/wp-content/uploads/sites/3/2026/03/dicom.conformancestatement.sectrapacs-28.1.0.10183.pdf) (2026-03) and [v27.1](https://medical.sectra.com/wp-content/uploads/sites/3/2025/03/conformance-statement-27-1.pdf) (2025-03). Sectra runs a **QIDO Provider** application (responds to QIDO from remote AEs) and a QIDO *client* that can fan a query across several QIDO-RS providers. Study searches restricted to `application/dicom+json`; `limit`/`offset` supported. — **High**
- Fujifilm: [Synapse DICOM Conformance Statement](https://healthcaresolutions-us.fujifilm.com/wp-content/uploads/2023/02/DICOM_Conformance_Statement_v5-2_above.pdf). Supports WADO-URI, WADO-RS, QIDO-RS, STOW-RS; **STOW-RS and extended WADO-RS added in Synapse 5.3.000** — a useful version floor to write into a contract. — **High**
- Visage: [Visage 7 DICOM Conformance Statement](https://www.visageimaging.com/downloads/Visage7/Visage7_DICOMConformanceStatement.pdf) (v12.00, 2026-06-18) and [Visage 7 IHE Integration Statement](https://www.visageimaging.com/downloads/Visage7/Visage7_IHEIntegrationStatement.pdf). — **Medium–High**
- RamSoft: [Conformance Statements & Resources](https://www.ramsoft.com/conformance) — directly fetched 2026-10-10. Publishes *PowerServer v6.7 DICOM Conformance*, *OmegaAI DICOM Conformance*, *OmegaAI FHIR Capability Statement*, and **three** PowerServer v6.0 IHE statements (PowerServer Lite/Gateway Viewer; PowerServer PACS/Tele Lite/Gateway Mammo Viewer; PowerServer RIS/PACS). **No DICOMweb-specific document is listed.** OmegaAI marketing claims HL7 FHIR R4 + DICOMweb + open APIs — VENDOR CLAIM. — **High** for the index, **Medium** for the DICOMweb claim.
- eRAD: [Radiology PACS API](https://erad.com/news/pacs-api-radiology-hl7-solutions/). Notably for this engagement, eRAD states **"logging and statistical information is available to be used in applications such as third-party dashboards and management reporting"** — i.e. the operational-analytics use case is an advertised capability. — **Medium**
- Merative: [Merge Healthcare Statements](https://www.merge.com/support/merge/merge-healthcare-statements) (redirected from merative.com). — **Medium**

### The Ambra finding — material, and worth stating plainly

Ambra Health (acquired by Intelerad, rebranded InteleShare) publishes a genuinely complete public API reference at
**https://access.dicomgrid.com/api/v3/api.html** (HTTP 200, 1.65 MB, fetched 2026-10-10).

I grepped the full document. Result:

```
DICOMweb: 0    WADO: 0    QIDO: 0    STOW: 0   (case-insensitive variants: 1 incidental)
```

The API is JSON over HTTPS, base `https://access.dicomgrid.com/api/v3` (alias `access.ambrahealth.com`), authenticated by session id from `POST /session/login` passed as a parameter or `X-AmbraHealth-SID` header. It covers studies, patients, users, groups, accounts, namespaces, sharing, storage/images and webhooks — including **per-study audit trail** and **webhooks**, both directly useful for operational analytics. A Python SDK exists ([dicomgrid.github.io/sdk-python](https://dicomgrid.github.io/sdk-python/quickstart.html)).

**Interpretation (Medium):** Ambra/InteleShare offers an excellent *proprietary* API and essentially no DICOMweb surface in its public docs. For the pitch this is the cleanest illustration of the real risk: the lock-in is not "no API," it is "an API you cannot port." A proprietary API means every integration you build is a sunk cost if you change vendors; a DICOMweb API means the integration survives the vendor. That is the argument, and it does not require alleging anyone charges a fee.

### Extra-cost gating

**I could not verify extra-cost API gating for any named PACS vendor.** No vendor publishes an API price list. The only concrete adjacent evidence is interface/integration fees (see Q2b). Treat "is DICOMweb included in the base license, at no incremental cost, for the life of the agreement?" as an open contract question, not a known fact.

---

## Q2b. The "data hostage" problem — what is actually documented

### Headline: the strong version of this claim is not supported by the public record

I searched trade press (AuntMinnie, Radiology Business, Axis Imaging News, HealthExec), KLAS coverage, legal/forum sources and general web for: imaging centers charged for API access, data egress fees, or extraction fees; and for litigation.

**Findings:**

- **No litigation found** over PACS API access, data egress, or data-extraction fees. The PACS lawsuits that surface are **data-breach** cases, not data-access cases — e.g. the Northeast Radiology / Alliance Healthcare Services class action over a PACS breach exposing ~61 million images, **dismissed** by the US District Court for SDNY. Source: [AuntMinnie](https://www.auntminnie.com/imaging-informatics/enterprise-imaging/pacs-vna/article/15631021/lawsuit-over-pacs-hack-in-new-york-dismissed) and [HIPAA Journal](https://www.hipaajournal.com/radiology-specialists-facing-class-action-lawsuit-over-pacs-data-breach/) — **Medium**. **This is a different problem and must not be cited as data-hostage evidence.**
- **No published per-study or per-GB API-access fee schedule** from any PACS vendor. — **High confidence that it is absent from the public record**; this is an absence-of-evidence finding, not proof of absence in private contracts.
- I checked the one trade-press article that looked most promising, AuntMinnie's ["9 ways to reduce your legal exposure to PACS problems"](https://www.auntminnie.com/imaging-informatics/enterprise-imaging/pacs-vna/article/15621134/9-ways-to-reduce-your-legal-exposure-to-pacs-problems) (Herman Oosterwijk, 2018-09-03). **It does not discuss egress, extraction, API fees, or data ownership at all.** — **High**. Flagging this because the title is misleading and it would be easy to miscite.

### What IS documented: migration cost, and proprietary non-pixel data

The real, citable problem is *migration*, and the mechanism is that **pixels port but context does not**.

- **"[E]ach vendor's database structure remains proprietary."** Images migrate fine, but "textual information about patients and examinations, pointers to the associated image data files, and other data fields are imported incorrectly." And on vendor cooperation: **"there is little incentive for the legacy vendor to make a deal."**
  Dollar figures: Orange Regional estimated **"about 2 years and several hundred thousand dollars"**; generally, for hospital archives with years and multiterabytes, **"the cost can be more than $400,000."**
  Source: Tor Valenza, ["Changing PACS: Time, Money, and DICOM," Axis Imaging News, 2007-06-01](https://axisimagingnews.com/radiology-products/radiology-software/pacs/changing-pacs-time-money-and-dicom) — **High for the quotes, Low for present-day applicability.**
  ⚠️ **Caveat for the pitch: this is 2007 and hospital-scale. A new single-site El Paso center is neither. Do not present $400,000 as a number Luis and Fernando would face.** Its legitimate use is to make the *structural* point — proprietary schema, misaligned incentives at exit — not to size a cost.

- Annotations and key-image flags are often stored in proprietary formats requiring custom programming and cooperation of both vendors. — Medium, secondary.

- **Interface/integration fees are a documented hidden cost.** Vendors commonly bill separately for HL7 interface configuration and EMR integration, often as one-time setup plus annual maintenance. Independent interface-engine licensing (Mirth Connect, Cloverleaf, Rhapsody) is cited at **$15,000–$80,000/year** depending on message volume and deployment. Some vendors (e.g. Dicom Systems) advertise unlimited HL7 interfaces at no extra cost — presented as the exception.
  Sources: [Dextro Imaging, "Radiology PACS Pricing: 2026 Guide to TCO"](https://blog.radmadesimple.com/post/radiology-pacs-pricing-the-2026-guide-to-total-cost-of-ownership) (2026) — **Low–Medium, vendor-adjacent blog**; [Dicom Systems HL7 Integration Engine](https://dcmsys.com/solutions/hl7integration-engine/) — **VENDOR CLAIM**. The $15k–$80k range is the most defensible cost figure in this whole section, and it is about *interface engines*, not API access.

- A cloud migration list price data point: OmniPACS **$1,500 for a 250 GB data migration**. — **Low** (single vendor page, via search index; not independently confirmed).

### The vendor framing of the problem (useful language, but it is marketing)

Mach7 Technologies, ["The Legacy PACS Replacement Wave: What to Demand From a Modern VNA," 2026-09-10](https://www.mach7t.com/blog/the-legacy-pacs-replacement-wave-what-to-demand-from-a-modern-vna) — **VENDOR CLAIM**, directly fetched and quoted:

- **"Egress charges, retrieval fees, and interface work can sit quietly inside a bundled price."**
- **"A future move is a known quantity rather than a hostage negotiation."**
- Demands "[d]ocumented, fee-transparent export and migration terms in the contract."

This is a competitor-VNA vendor arguing against incumbents, so it is advocacy, not evidence. But it is *well-phrased* advocacy and it independently converges with the Axis 2007 structural analysis. Cite it as "this is how the market talks about the risk," never as proof that fees were charged.

### Recommended framing for Luis and Fernando

Given Fernando's active litigation against Akumin (per standing project context — **never raise Akumin, scale, platform, or roll-up**), an unsupported "vendors hold your data hostage and sue you" narrative is both unsourced and tonally wrong. The defensible framing is prospective and contractual:

> We cannot show you a published price list for data egress, because vendors do not publish one. That is precisely the problem. The cost is unknown at signing and discovered at exit. So we fix it at signing: DICOMweb conformance named in the contract, export terms and fees documented up front, and no proprietary dependency we cannot reproduce.

That is honest, it is sourced, and it is stronger than a scare number.

---

## Q2c. MOST IMPORTANT — operationally valuable structured metadata beyond pixels

### Tag verification method

I verified every tag below against the **authoritative DICOM Data Dictionary, PS3.6 Chapter 6** (`https://dicom.nema.org/medical/dicom/current/output/chtml/part06/chapter_6.html`), parsed programmatically on 2026-10-10. Names and VRs are exact. — **High**

### ⚠️ Correction to the brief

The brief paired "(0018,1152)/CTDIvol." These are different attributes:

| Tag | Correct name | VR |
|---|---|---|
| **(0018,1152)** | **Exposure** (mAs — radiography/fluoro) | IS |
| **(0018,9345)** | **CTDIvol** | FD |

Using (0018,1152) to mean CTDIvol in front of a clinically experienced owner would undermine credibility. CTDIvol is **(0018,9345)**.

### Verified tag inventory, with practical-reliability assessment

**Reliability ratings** reflect who writes the value. Machine-generated, standard-required values are dependable. Free-text and human-entered values are not. This is the analytically load-bearing distinction in this entire section.

#### Tier 1 — Reliably populated. Build the product on these.

| Tag | Name | VR | Operational use | Reliability |
|---|---|---|---|---|
| (0008,0020) | Study Date | DA | Volume, daily throughput | **High** |
| (0008,0030) | Study Time | TM | Arrival/start distribution | **High** |
| (0008,0021) | Series Date | DA | Intra-exam sequencing | **High** |
| (0008,0031) | Series Time | TM | **Series-to-series gaps** | **High** |
| (0008,0032) | Acquisition Time | TM | Acquisition-level timing | **High** (modality-dependent) |
| (0008,0022) | Acquisition Date | DA | — | **High** (modality-dependent) |
| (0008,0033) | Content Time | TM | Fallback when Acquisition absent | **High** |
| (0008,0060) | Modality | CS | Segmentation by modality | **High** (enumerated, required) |
| (0008,1010) | Station Name | SH | **Per-scanner / per-room attribution** | **High** — machine-written |
| (0020,0011) | Series Number | IS | Series ordering/counts | **High** |
| (0008,103E) | Series Description | LO | Series labeling | **Medium** (free text) |

**Why Tier 1 is the real product.** Timestamps and Station Name are written by the scanner without human intervention, are present in effectively every instance, and are exactly what you need for utilization math. Room/scanner utilization, exam duration, gap-between-exams and exams-per-operational-hour are all computable from (0008,1010) + series/acquisition times alone — no vendor cooperation, no extra module, no dose system.

#### Tier 2 — Available but frequently unreliable. Verify before promising.

| Tag | Name | VR | Intended use | Reliability in practice |
|---|---|---|---|---|
| (0008,1070) | **Operators' Name** | PN | Technologist attribution | **LOW–MEDIUM** ⚠️ Type 3 (optional). Depends on tech logging in; commonly blank, shared logins, initials, or free-text. **Do not promise per-tech analytics without site-specific audit.** |
| (0008,1050) | Performing Physician's Name | PN | Physician attribution | **LOW–MEDIUM** — same class of problem |
| (0018,1030) | **Protocol Name** | LO | Protocol-level comparison | **LOW–MEDIUM** ⚠️ Free text, locally invented, drifts. Peer-reviewed evidence below. |
| (0018,0015) | **Body Part Examined** | CS | Anatomy segmentation | **LOW–MEDIUM** ⚠️ Documented as too generic / inconsistent. Evidence below. |
| (0008,1030) | Study Description | LO | Exam type | **MEDIUM** — free text but practically usable; literature shows it's often *better* than Body Part Examined |
| (0018,9345) | CTDIvol | FD | CT dose | **MEDIUM** — CT only, and RDSR is the better path |
| (0018,1152) | Exposure (mAs) | IS | Radiography technique | **MEDIUM** |
| (0018,0060) | KVP | DS | Technique | **MEDIUM** |
| (0028,0301) | Burned In Annotation | CS | PHI-in-pixels risk flag | **MEDIUM** — security-relevant, see note |

#### Tier 3 — MPPS attributes: highest operational value, lowest availability

| Tag | Name | VR |
|---|---|---|
| (0040,0244) | Performed Procedure Step Start Date | DA |
| (0040,0245) | Performed Procedure Step Start Time | TM |
| (0040,0250) | Performed Procedure Step End Date | DA |
| (0040,0251) | Performed Procedure Step End Time | TM |
| (0040,0253) | Performed Procedure Step ID | SH |
| (0040,0254) | Performed Procedure Step Description | LO |

MPPS start/end times are the **only** attributes that directly express true procedure duration rather than requiring it to be inferred from image timestamps. MPPS is a network transaction initiated by the modality at the beginning and end of acquisition, sent to PACS and/or RIS, carrying "information about what really has been performed."
Source: Noumeir R., ["Benefits of the DICOM modality performed procedure step," *J Digit Imaging* 2005;18(4) — PMID 15988627](https://pubmed.ncbi.nlm.nih.gov/15988627/) — **High**.

⚠️ **Critical caveat.** That paper's own stated purpose is to "bridge the gap between MPPS implementation and deployment" — i.e. **MPPS was specified and under-deployed, and the paper exists because of that gap.** In small outpatient centers with mixed/older modality fleets, assume MPPS is **absent until proven present**. Verify per-scanner before designing anything that depends on it.

**Design consequence:** compute duration from series/acquisition timestamps as the primary method, and treat MPPS as a precision upgrade where available. That ordering is the opposite of what the standard would suggest and it is the correct engineering call.

### Derived metrics and how to compute them

| Metric | Computation | Dependency | Feasibility |
|---|---|---|---|
| Exam duration | last − first image timestamp within study | Tier 1 only | **High** |
| Exam duration (precise) | PPS End − PPS Start | MPPS | Medium (availability-gated) |
| Inter-exam gap / scanner idle | next study start − prior study end, grouped by (0008,1010) | Tier 1 only | **High** |
| Room operational day length | first → last study per station per day | Tier 1 only | **High** |
| Exams per operational hour | count ÷ operational window | Tier 1 only | **High** |
| Series counts per exam | distinct (0020,0011) | Tier 1 only | **High** |
| Per-technologist throughput | group by (0008,1070) | Tier 2 | **Low–Medium** ⚠️ audit first |
| Protocol-level comparison | group by (0018,1030) | Tier 2 | **Low–Medium** ⚠️ needs normalization |
| CT dose / DRL benchmarking | RDSR, else (0018,9345) | RDSR availability | Medium |
| Reject/repeat rate | vendor reject-analysis + DICOM | vendor-specific | Medium |

### Peer-reviewed evidence

**The single best proof that this works commercially — and the best pitch citation.**
Source: ["Use of Image-Based Analytics for Ultrasound Practice Management and Efficiency Improvement," *J Digit Imaging* 2019 — PMID 30623273](https://pubmed.ncbi.nlm.nih.gov/30623273/) — **High**.

Verbatim-grounded findings: system collects from "tens of thousands of DICOM images," using "structured reporting, public and private DICOM headers, and text within the images via optical character recognition (OCR)." Computes "median exam length (time from the first image to last), transducer models used in an exam, and exams performed in a particular room, practice location, or by a given sonographer," plus "the length of a scan room's operational day, the number and type of exams performed, the time between exams, and summary data such as exams per operational hour and time-based room utilization."

**Documented financial outcome: "two defective probes were not replaced (a savings of over $10,000) when utilization data showed that thr[ee]..."** (abstract truncates).

Three things to note. (1) This validates the exact metric set above, in an **outpatient-relevant modality (ultrasound)**, in a peer-reviewed journal. (2) The documented saving is **equipment capital avoidance driven by utilization data** — a concrete, defensible, non-speculative benefit type. (3) They needed **OCR and private tags**, which honestly signals that standard public tags alone were insufficient for their full metric set.

**Body Part Examined is documented as inadequate.**
["Determining scanned body part from DICOM study description for relevant prior study matching," *Stud Health Technol Inform* 2013 — PMID 23920517](https://pubmed.ncbi.nlm.nih.gov/23920517/) — **High**. States the Body Part Examined field "can be very generic" — a pancreatitis study and a renal-stone study both carry "abdomen" — and therefore derives body part from the free-text **Study Description** instead, reaching 99.94% accuracy on 404 test descriptions (trained on 1,200). Conclusion: **(0008,1030) Study Description is often more informative than (0018,0015) Body Part Examined**, which inverts the naive assumption.

["Standardizing DICOM annotation: deep learning enhances body part description in X-ray image retrieval," *BMC Med Imaging* 2025 — PMID 41390620](https://pubmed.ncbi.nlm.nih.gov/41390620/) — **High**. On 20k routine PACS X-rays: reduced **116 distinct DICOM header body-part entries down to 36 SNOMED CT codes**. That 116→36 collapse is direct quantitative evidence of real-world body-part tag chaos. Accuracy 0.889 (examined) / 0.853 (visible).

**Metadata completeness is a recognized research problem.**
["Metadata Quality in Imaging Trials: A Knowledge Graph-Based Approach," *Stud Health Technol Inform* 2025 — PMID 40380518](https://pubmed.ncbi.nlm.nih.gov/40380518/) — **High**. Builds a knowledge graph from DICOM metadata specifically to assess "metadata quality ... through custom metrics, e.g., regarding attribute completeness," for "automated quality checks." The existence and framing of this work confirms attribute completeness cannot be assumed.

**Dose monitoring: deployed, effective, and conditional on data hygiene.**
["Automated radiation dose monitoring software packages: impact on CT dose management and optimisation, implementation challenges, and practical considerations: a systematic review," *Physica Medica* 2025, DOI 10.1016/j.ejmp.2025.105056 — PMID 40694887](https://pubmed.ncbi.nlm.nih.gov/40694887/) — **High**. PRISMA review, 1,293 screened → **49 included**. DMS enables "dose benchmarking against diagnostic reference levels, inter-hospital and scanner comparisons, dose calculations, cumulative dose tracking." Crucially: **"effective implementation requires skilled users, standardised protocol naming, and regular data verification."**

That sentence is the empirical backbone of the Tier 2 warning. A systematic review of 49 studies concludes that **standardised protocol naming** is a prerequisite — which is precisely to say that (0018,1030) is not dependable as found. Any protocol-level analytics offering must include a normalization step, and should be scoped and priced as such.

Deployment footprint across the literature: Radimetrics in 20 studies (Europe/N. America/Asia), DoseWatch in 12, Qaelum DOSE in 4, **Imalogix in North America**. Source: [BIS Research, radiation dose management market](https://bisresearch.com/industry-report/global-radiation-dose-management-market.html) — **Low–Medium, paywalled market report via search index**. DoseWatch is described as ingesting from **RDSR, image headers, MPPS, and OCR** — the multi-source fallback chain is itself evidence that no single source is complete. — **Medium**.

**OpenREM (open source) has documented operational wins.**
["Improving the effectiveness and efficiency of a skin dose investigation protocol in interventional radiology," *BMJ Open Qual* 2020 — PMID 31986118](https://pubmed.ncbi.nlm.nih.gov/31986118/) — **High**. openSkin + OpenREM across three PDSA cycles "eliminated the possibility of a high skin dose procedure failing to trigger an investigation" and **reduced staff time on skin-dose investigations by an estimated 94%.** A quantified automation benefit from a free tool — directly relevant to an automation-themed pitch.
["Local Diagnostic Reference Levels in Digital Breast Tomosynthesis," *J Med Radiat Sci* 2025 — PMID 40561378](https://pubmed.ncbi.nlm.nih.gov/40561378/) — **High**. AGD collected via OpenREM; LDRLs by compressed-breast-thickness band (1.5 / 2.70 / 3.90 / 4.70 mGy). Demonstrates mammography dose analytics on open-source tooling.

**RDSR is the right dose source, per AAPM/EFOMP.**
["Estimation of patient skin dose in fluoroscopy: summary of a joint report by AAPM TG357 and EFOMP," *Med Phys* 2021 — PMID 33930183](https://pubmed.ncbi.nlm.nih.gov/33930183/) — **High**. Situates "the importance of the DICOM standard detailing pertinent information contained in the Radiation Dose Structured Report (RDSR) and DICOM image headers." Note the report exists partly to address a "knowledge gap regarding skin dose-related patient information from fluoroscopy devices" — again, specified ≠ delivered.

**Reject/repeat analysis: standardization is explicitly missing.**
["AAPM Task Group Report 305: Guidance for standardization of vendor-neutral reject analysis in radiography," *J Appl Clin Med Phys* 2023 — PMID 36995917](https://pubmed.ncbi.nlm.nih.gov/36995917/) — **High**. States plainly: **"Due to the lack of standardization, reject data often cannot be easily compared between radiography systems from different vendors."** TG305 proposes essential data elements and a reject-reason classification schema. **Implication: cross-vendor reject-rate comparison is not available from DICOM alone — it requires vendor reject-analysis features plus TG305-style normalization. Name TG305 in the contract.**

Benchmark figures: ["Digital radiography reject analysis of examinations with multiple rejects," *J Med Radiat Sci* 2021 — PMID 33826800](https://pubmed.ncbi.nlm.nih.gov/33826800/) — **High**. 11,596 images, Australian ED: **overall reject rate 10.3%**, multiple-reject rate 1.3%. Worst projections: AP chest 18.1%, AP pelvis 22.5%, horizontal-beam hip 33.5%, horizontal-beam knee 30.5%. Top reasons: **positioning 67.1%**, anatomy cut-off 8.4%. Data came from reject-analysis software embedded in the X-ray unit — i.e. **modality-side, not PACS-side**. ⚠️ Australian ED, not US outpatient; use as order-of-magnitude only, and note that positioning dominance makes reject rate a *training* signal.

**Security note (standing project lens):** (0028,0301) Burned In Annotation flags pixel-burned PHI, which defeats header-level de-identification and matters for any outbound data flow, AI vendor, or research sharing. Worth a line in any data-governance section.

---

## Q2d. Is there a credible "DICOM + FHIR unified operational data layer" in production?

**Verdict: the cloud DICOMweb layer is production-real and GA. The DICOM→FHIR mapping is real but Trial Use. FHIRcast is emerging, not yet dependable. Operational analytics on DICOM metadata is production-real.**

### ⚠️ Correction to the brief: PS3.20 is not the FHIR ImagingStudy mapping

The brief referenced "the DICOM standard's own FHIR mapping, PS3.x." I verified:

- **DICOM PS3.20 is "Imaging Reports using HL7 Clinical Document Architecture" — CDA R2, not FHIR ImagingStudy.** Source: [PS3.20](https://dicom.nema.org/medical/dicom/current/output/html/part20.html), [PDF 2025c](https://dicom.nema.org/medical/Dicom/2025c/output/pdf/part20.pdf) — **High**. (My first attempt at a PS3.20 FHIR-mapping URL returned **HTTP 404** — the section does not exist.)
- The **authoritative DICOM↔FHIR mapping lives in the HL7 FHIR specification**, on the ImagingStudy resource, which "provides mappings of its elements to DICOM attributes," identifying DICOM attributes by 32-bit tag "e.g. (0008,103E)"; Study Description maps from (0008,1030); series modality uses DICOM Context Group 29 (OID 1.2.840.10008.6.1.19); body site references DICOM Part 16 Annex L for SNOMED CT. Source: [FHIR R4 ImagingStudy](http://hl7.org/fhir/R4/imagingstudy.html) — **High**.
- **ImagingStudy in R4 is Maturity Level 3, standards status "Trial Use" — NOT normative.** — **High**. Contractually meaningful: do not let a vendor claim "FHIR-normative imaging" as settled.
- Related work in progress: [HL7 Confluence, Mapping of DICOM SR to FHIR](https://confluence.hl7.org/display/IMIN/Mapping+of+DICOM+SR+to+FHIR); [DICOM SR → FHIR Observation Mapping IG Proposal](https://confluence.hl7.org/display/FHIR/DICOM+SR+to+FHIR+Observation+Mapping+IG+Proposal); [Imaging ServiceRequest IG (MWL Requested Procedure mapping)](https://build.fhir.org/ig/HL7/imaging-service-request-ig/branches/__default/en/StructureDefinition-requested-procedure-imaging-study-definitions.html) — **Medium**, proposals/CI-build, not published standards.

### Production evidence for DICOM→FHIR at scale

["Large-Scale Integration of DICOM Metadata into HL7-FHIR for Medical Research," *Methods Inf Med* 2024 — PMID 40233823](https://pubmed.ncbi.nlm.nih.gov/40233823/) / [PMC12133321](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12133321/) — **High**. German Medical Informatics Initiative; pipeline extracts, converts and pseudonymizes DICOM metadata into **ImagingStudy** FHIR resources, deployed at the Data Integration Center of University Hospital Erlangen, "integrates seamlessly into the hospital's research IT infrastructure," evaluated at large scale across two departments.

**Classification: production-real for *research* data integration, at a large academic hospital.** Not a small-outpatient operational deployment. Honest read: the *pattern* is proven; the *context* is not analogous to a single El Paso site.

### FHIRcast — emerging, do not depend on it

- Mechanism: publish/subscribe context sync; radiologist opens a study and viewer + dictation follow. — **Medium**
- Adoption is **limited but growing**: "not many vendors have committed," and a chicken-and-egg dynamic ("because there aren't many vendors with FHIRcast enabled, it's hard to justify building it"). Source: [Rad AI engineering blog](https://eng.radai.com/p/the-evolution-of-radiology-reporting) — **Medium, vendor-authored**.
- [2026 State of FHIR Report, Firely](https://fire.ly/2026-state-of-fhir-report/): FHIRcast at **40% "extent of use"** among respondents. — **Low–Medium** (self-selected respondents, vendor-published, and "extent of use" is undefined here; do not quote this as 40% adoption).
- Peer-reviewed: ["Radiology Reimagined: Interoperability and Lessons Learned from the Imaging AI in Practice Demonstration," *Radiology* 2026 — PMID 42301015](https://pubs.rsna.org/doi/10.1148/radiol.252225) — **High**. RSNA demonstration since 2020; **>20 vendor partners**; "improved support for FHIRcast in 2024." ⚠️ This is an **annual conference demonstration**, which is strong evidence of vendor engagement and *weak* evidence of production deployment. Say so.
- Commercial signal: [AGFA HealthCare + Rad AI collaboration](https://www.radai.com/news/agfa-healthcare-and-rad-ai-announce-strategic-collaboration-to-enhance-radiology-workflows) including FHIRcast integration — **VENDOR CLAIM / press release**.
- Also useful: ["Integrating and Adopting AI in the Radiology Workflow: A Primer for Standards and IHE Profiles," *Radiology*](https://pubs.rsna.org/doi/full/10.1148/radiol.232653) — **Medium–High**. The **Integrated Reporting Applications (IRA)** profile is the IHE profile that frames FHIRcast-based context sync.

**Verdict: FHIRcast is a "name it as a desired roadmap capability" item, not a 2026 requirement for a small center.**

### Open-source stack — production-real, zero license cost

| Project | DICOMweb | License | Confidence |
|---|---|---|---|
| **Orthanc** (DICOMweb plugin) | **WADO-URI, WADO-RS, QIDO-RS, STOW-RS**, per PS3.18; **both server and client** | Open source (docs CC-BY-SA 4.0) | **High** |
| **dcm4chee-arc-light 5** | **QIDO-RS, WADO-RS, STOW-RS**; REST at `/dcm4chee-arc/aets/{aet}/rs` | **Tri-licensed MPL 1.1 / GPL 2.0+ / LGPL 2.1+** | **High** |
| **OHIF Viewer** | Client; `qidoRoot`/`wadoRoot`/`stowRoot` independently configurable | Open source | **High** |

- Orthanc: [DICOMweb plugin docs](https://orthanc.uclouvain.be/book/plugins/dicomweb.html) — "a basic, reference implementation of WADO-URI, WADO-RS, QIDO-RS and STOW-RS, following DICOM PS3.18"; plugin v1.25 referenced. The **client** role matters — Orthanc can query a remote DICOMweb server, which is exactly the "sidecar analytics without touching the PACS" pattern. — **High**
- dcm4chee: [web.dcm4che.org/dcm4chee-arc-light](https://web.dcm4che.org/dcm4chee-arc-light), [RESTful Services wiki](https://github.com/dcm4che/dcm4chee-arc-light/wiki/RESTful-Services) — **High**
- OHIF: [DICOMweb data source config](https://docs.ohif.org/configuration/datasources/dicom-web/), [Deployment](https://docs.ohif.org/deployment/). Documented-compatible archives: **DCM4CHEE 5.x, Orthanc, DICOMcloud, OsiriX, Horos**. Requires archive exposure + **CORS** headers. Also [DICOMweb Proxy](https://docs.ohif.org/configuration/datasources/dicom-web-proxy/) and [Azure integration](https://docs.ohif.org/deployment/azure/) / [microsoft/dicom-ohif](https://github.com/microsoft/dicom-ohif). — **High**

### Cloud services: GA status, DICOMweb, and ACTUAL published pricing

All three are **GA** and all three **support DICOMweb**. Pricing below was scraped from live pricing pages / official pricing API on **2026-10-10**, not from memory.

#### Google Cloud Healthcare API — DICOM store

GA. Source: [cloud.google.com/healthcare-api/pricing](https://cloud.google.com/healthcare-api/pricing) — **High** (scraped directly; WebFetch truncated the tables, so figures came from raw HTML extraction).

Google bills DICOM as **two** storage components — metadata index (Structured) + pixels (Blob):

| Component | Tier | Price |
|---|---|---|
| Structured Storage | 0–1 GiB-month | **$0.00 (free)** |
| Structured Storage | 1–1,024 GiB-month | **$0.000328767 / GiB-hour** (≈ **$0.24/GiB-month**) |
| Structured Storage | >1,024 GiB-month | **$0.000260274 / GiB-hour** (≈ **$0.19/GiB-month**) |
| Blob Storage | 0–1 GiB-month | **$0.00 (free)** |
| Blob Storage | >1 GiB | **$0.000027397 / GiB-hour** (≈ **$0.02/GiB-month**) |

Colder DICOM classes: Nearline **$0.000027397**/GiB-hr, Coldline **$0.000013699**/GiB-hr, Archive **$0.00000411**/GiB-hr. Retrieval: Standard **$0**, Nearline **$0.01/GiB**, Coldline **$0.02/GiB**, Archive **$0.05/GiB**. Coldline carries a **90-day minimum** with an early-deletion fee (worked example on the page: 1,000 GB deleted at day 60 still costs the full $30).

Requests (shared tiers): first **25,000 free**; Standard **$0.39 / 100k**, Complex **$0.69 / 100k**, Multi-operation **$0.39 / 100k**, Advanced **$0.99 / 100k**.

**ETL / egress-shaped operations — the lock-in-relevant line items:**

| Operation | Price |
|---|---|
| Export batch | **$0.19/GiB** (0–1 GiB) → **$0.14** (1–1,024) → **$0.09** (>1,024) |
| Export streaming | **$0.34/GiB** → **$0.29** → **$0.24** |
| Transcode DICOM | free <1 GiB → **$0.004/GiB** → **$0.003/GiB** |

**Note for the pitch:** this is the clearest *published* "it costs money to get your data out" schedule I found anywhere — and it is from a **hyperscaler, not a PACS vendor**. Export batch at $0.09–$0.19/GiB is transparent and modest, which is exactly the contrast to draw: the problem with PACS vendors isn't that egress costs something, it's that the price is undisclosed.

#### AWS HealthImaging

GA, **HIPAA-eligible**. Sources: [pricing](https://aws.amazon.com/healthimaging/pricing/), [What is AWS HealthImaging](https://docs.aws.amazon.com/healthimaging/latest/devguide/what-is.html) — **High**.

| Item | Price |
|---|---|
| Frequent Access storage | **$0.105 / GB-month** |
| Archive Instant Access storage | **$0.006 / GB-month** |
| Data import | **Free** — "Data imports into HealthImaging are always free" |
| API calls | **$0.005 / 1,000 API calls** |
| Minimum billable image set | **5 MB** |
| Structured (metadata) storage | pre-provisioned **10 GB** per data store |
| Data transfer out | **charged**; free to AWS services in-region |

Auto-tiering after **30 days** of inactivity.

⚠️ **Architectural caveats that matter.** HealthImaging does **not** store plain DICOM P10 as-is: it reorganizes into **image sets** mapped to DICOM series, **normalizes** patient/study/series metadata to resolve inter-SOP-instance inconsistency, exposes metadata by **human-readable keywords rather than hex tags**, and returns pixels as **HTJ2K**. It offers "DICOMweb conformant APIs" **plus cloud-native APIs for actions not supported by the DICOMweb standard, like metadata update." Import stages via **Amazon S3**. — **High**.
**Implication: the developer-friendly normalization is genuinely useful for analytics, but it is a transformation, not a faithful archive, and the non-DICOMweb cloud-native API surface is itself a portability consideration.** Also: **$0.105/GB-month frequent-access is ~5x Google's ~$0.02/GiB-month blob rate** — the two are not comparing like with like (normalization, HTJ2K, free import, performance), but a naive per-GB comparison would mislead.

**Not verified:** native C-STORE/DIMSE support. HealthImaging appears S3/API-import oriented; a DICOM router (e.g. Orthanc, dcm4chee, Dicom Systems) would likely be needed in front of modalities. — **Low / UNVERIFIED**.

#### Azure Health Data Services — DICOM service

GA, available in all Azure Health Data Services regions; designed for PHI (HIPAA, GDPR, CCPA); LRS replication; RBAC. Source: [DICOM service overview](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicom-services-overview) (doc dated 2025-07-23) — **High**.

Supports **Studies Service** (PS3.18 ch.10) incl. a **nonstandard delete** transaction, and **Worklist Service (UPS-RS)** Push and Pull SOPs. — **High**.

Pricing retrieved from the **official Azure Retail Prices API** on 2026-10-10 (the pricing web page renders values as `$-` via JS, so the API is the reliable route):

| Meter | Price | Unit |
|---|---|---|
| Structured Storage | **$0.39** | 1 GB/month |
| Structured Storage (free tier) | **$0.00** | 1 GB/month |
| Blob Storage | **$0.023** | 1 GB/month |
| Blob Storage (free tier) | **$0.00** | 1 GB/month |
| API Requests | **$0.54** | per 100K |
| API Requests (free tier) | **$0.00** | per 100K |
| Transcode DICOM | **$0.004** | 1 GB |
| Export Batch | **$0.19** → **$0.139992** (tier ≥1) | 1 GB |
| Export Streaming | **$0.34** → **$0.289986** (tier ≥1) | 1 GB |
| Notifications | **$0.59** | per 1M |
| Structured De-Identification | **$1.14** | 1 GB |
| Transformations | **$1.14** | 1 GB |

Billing mechanics worth knowing: **initial-mode import does not incur charge**; responses with status **≥500 or 429 are not charged**; **multi-part DICOMweb requests are charged per DICOM instance** stored or retrieved — a real cost-modeling trap for high-instance-count CT/MR. — **High**.

**Two Azure features are directly on-thesis for operational analytics:**
- **Change Feed** — "ordered, guaranteed, immutable, read-only logs of all changes," readable independently and in parallel at the client's own pace. This is a proper event stream for building analytics without polling.
- **DICOMcast** — open-source, self-hosted in Azure; "inject[s] DICOM metadata into a FHIR service or FHIR server as an imaging study resource." **This is a shipping implementation of the DICOM→FHIR ImagingStudy pattern** from a hyperscaler.
- Also: **Extended query tags** — index on standard *or private* DICOM tags beyond the conformance statement defaults. Relevant given the ultrasound-analytics paper needed private tags.
— **High**

**Pricing-shape comparison (metadata/structured storage, approx, per GB-month): Azure $0.39 > Google ~$0.24 > AWS (10 GB pre-provisioned). Pixel/blob: AWS $0.105 > Google ~$0.02 ≈ Azure $0.023.** Different architectures; do not reduce to one number.

### Production-real vs research-only — summary

| Pattern | Status |
|---|---|
| DICOMweb on managed cloud (GCP / AWS / Azure) | **Production-real, GA** — High |
| Orthanc / dcm4chee / OHIF stack | **Production-real** — High |
| DICOM metadata → operational analytics | **Production-real** (JDI 2019 ultrasound) — High |
| Dose monitoring from RDSR | **Production-real**, 49-study review — High |
| DICOM → FHIR ImagingStudy pipeline | **Production-real for research** (Erlangen); ImagingStudy still **Trial Use** — High |
| Azure DICOMcast (DICOM→FHIR, shipping) | **Production-available** — High |
| FHIRcast context sync | **Emerging**; conference demos + early commercial — Medium |
| Unified DICOM+FHIR *operational* layer for a small outpatient center | **No published case study found** — see Could Not Verify |

---

## Q2e. IHE profiles worth naming in a vendor contract

### Status verified against the IHE Radiology Technical Framework

Source: [profiles.ihe.net/RAD/index.html](https://profiles.ihe.net/RAD/index.html), fetched 2026-10-10 — **High**.

TF structure: **Vol 1** Integration Profiles, **Vol 1x** appendices, **Vol 2** Transactions, **Vol 2x** appendices, **Vol 3** Cross-Transaction & Content, **Vol 4** National Extensions.

| Profile | Acronym | Status | Contract leverage |
|---|---|---|---|
| Scheduled Workflow.b | **SWF.b** | **Final Text** (Rev 19.0, 2020-09-18) | **The anchor profile.** Order→schedule→acquire→store consistency; includes MWL and MPPS transactions |
| Portable Data for Imaging | **PDI** | **Final Text** | Patient/outside-provider media; relevant to a new center building referral relationships |
| Imaging Object Change Management | **IOCM** | **Final Text** (Rev 14.0, 2014-07-30) | Correction/deletion propagation — **data-integrity leverage** |
| Cross-enterprise Document Sharing for Imaging | **XDS-I.b** | **Final Text** (2012-07-24; deprecated XDS-I replaced) | Cross-enterprise sharing; **Imaging Document Source must be grouped with ATNA Secure Node** |
| Radiation Exposure Monitoring | **REM** | **Final Text** (Rev 12.0, 2012-07-24) | **The dose profile to name** — RDSR conveyance. Brief omitted it; include it |
| Mammography Acquisition Workflow | **MAWF** | ⚠️ **RETIRED 2024-06-25** | **Do NOT name in a 2026 contract** |
| Integrated Reporting Applications | **IRA** | Framework for FHIRcast-based context sync | Forward-looking only — Medium |

**Two corrections to the brief.** (1) **MAWF is retired** as of 2024-06-25 — naming a retired profile signals the requirements were copied from a stale template. (2) **MPPS is a transaction set inside SWF.b, not a standalone profile** — ask for SWF.b conformance *including the MPPS actors/transactions*, which is both more precise and harder to wriggle out of.

Also note the **ATNA grouping requirement** for XDS-I.b Imaging Document Source (security lens: auditing and node authentication come bundled, which is a benefit to claim, not a cost).

Supporting IHE sources — **High**:
[RAD TF Vol 1 (2025)](https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol1.pdf) · [Vol 1 Rev 22.0 (2024-06-25)](https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Rev22-0_Vol1_FT_2024-06-25.pdf) · [SWF.b Supplement Rev 1.7 (2019-08-09)](https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_SWF.b_Rev1-7_2019-08-09.pdf) · [IOCM Extension Rev 1.4 (2015-04-21)](http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_IOCM_Extension_Rev1.4_TI_2015-04-21.pdf) · [RAD TF Vol 3](https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Rev18-0_Vol3_FT_2019-08-09.pdf)

### How to verify a vendor's claim — two published, independent sources

**⚠️ Read this first.** IHE states that **"IHE Integration Profiles are not statements of conformance to standards, and IHE is not a certifying body,"** and that **"vendors publishing IHE Integration Statements accept full responsibility for their content."** Registry data is **"exclusively entered by vendors."** So an Integration Statement is a **vendor self-declaration** — contractually useful as a representation you can bind them to, but not third-party proof.
Sources: [IHE Wiki, Integration Statement](https://wiki.ihe.net/index.php/Integration_Statement), [Integration Statement Registry](https://wiki.ihe.net/index.php/Integration_Statement_Registry), [IHE Product Registry](https://www.ihe.net/testing/ihe_product_registry/) — **High**.

**Source 1 — IHE Product Registry (self-declared).**
- `https://product-registry.ihe.net` (**HTTP 200** verified 2026-10-10)
- Gazelle-hosted UI: [connectathon.ihe-catalyst.net/PR/pr/introPR.seam](https://connectathon.ihe-catalyst.net/PR/pr/introPR.seam) (returned **HTTP 503** at fetch time — intermittent; the registry itself resolves)
- [User manual](https://connectathon.ihe-catalyst.net/gazelle-documentation/Product-Registry/user.html)
- Vendors create/manage/publish Integration Statements; users browse systems by **IHE Actor and Profile**. Note IHE's own guidance: the database is easier to search, but **the vendor-published Integration Statement document is the primary source**.

**Source 2 — IHE Connectathon Results (independently tested). This is the stronger check.**
- **[connectathon-results.ihe.net](https://connectathon-results.ihe.net/)** (**HTTP 200**, 222 KB, verified 2026-10-10) — **High**
- Scope: **89 editions, 899 companies, 207 unique profiles tested**, "thousands of vendor-to-vendor connections."
- Per-company pages with business details, **test results**, and **IHE Connectathon SEAL** earned.
- Two search modes: **Company Search** (browse by name, then filter by year / actor / profile) and a **Custom Search Matrix** (filter by company + profile + actor simultaneously).
- Result fields: vendor test results, profiles tested, actor types, Connectathon year, SEAL achievements.

### Recommended verification procedure (and contract language)

1. **Get the artifact.** Require the vendor's own **IHE Integration Statement PDF** for the exact product **and version** being sold. Version matters — RamSoft publishes *three separate* PowerServer v6.0 statements by component, and Fujifilm's STOW-RS support begins at **Synapse 5.3.000**. A statement for a different edition or version is not evidence about yours.
2. **Cross-check self-declaration.** Look the product up in the **Product Registry** and confirm the claimed Actors/Profiles match the PDF.
3. **Cross-check independent testing.** Search the vendor on **connectathon-results.ihe.net**, filter to the profile (e.g. SWF.b) and actor, and confirm a **recent year**. A gap between what's claimed in the Integration Statement and what was actually tested at a Connectathon is the highest-value question you can ask in a vendor meeting.
4. **Require the DICOM Conformance Statement separately.** IHE conformance ≠ DICOMweb support. Demand the PS3.18 section naming **QIDO-RS, WADO-RS, STOW-RS** explicitly, and confirm whether the **Worklist Service (UPS-RS)** is included.
5. **Bind it.** Name in the contract: product + version; **SWF.b including MPPS actors/transactions**; **REM**; **IOCM**; **PDI**; **XDS-I.b** if cross-enterprise sharing is in scope; **DICOMweb QIDO-RS/WADO-RS/STOW-RS per PS3.18 at no incremental license cost**; **AAPM TG305** data elements if reject analysis matters; and **documented, fee-transparent export and migration terms**. Do **not** name MAWF.

---

## What I could NOT verify, and why

### Q2a
1. **Extra-cost API gating for every named vendor.** No PACS vendor publishes API pricing. Requires direct quotes/contracts.
2. **Intelerad IntelePACS / InteleShare DICOMweb** — the WADO-RS/QIDO-RS/STOW-RS claim came from a **search-index snippet**; no public developer portal or conformance statement located. The only Intelerad "API profile" found is a **third-party** write-up ([api-evangelist/intelerad](https://github.com/api-evangelist/intelerad)), not a vendor source. **Low.**
3. **Change Healthcare / Optum enterprise imaging** — no accessible conformance or developer documentation found at all. Complete gap.
4. **Konica Minolta Exa, Novarad, PaxeraHealth, Hyland Acuo** — no DICOMweb conformance document located; only marketing and trade press. These may well support DICOMweb; I simply cannot evidence it.
5. **Merative/Merge DICOMweb** — statements found cover DIMSE, media storage and MWL. Absence in my sample ≠ absence in the product; I did not open every version PDF.
6. **Whether Sectra/Fujifilm/Visage DICOMweb is base-license or licensed module.** Conformance statements document *capability*, never *commercial packaging*.

### Q2b
7. **Any litigation** over API access, egress or extraction fees — **none found**. Searched trade press, legal and general sources. The PACS lawsuits in the record are **breach** cases.
8. **Any published per-study/per-GB PACS API-access fee** — none found.
9. **Current (2020s) small-outpatient migration cost range.** Best figures are **2007 and hospital-scale** ($400k+). No modern small-center benchmark located. **This is the biggest single gap in the brief and I recommend not asserting a number.**
10. **The OmniPACS $1,500 / 250 GB figure** — seen only via search index; not confirmed on the vendor page.
11. **Practitioner forum accounts** (Reddit/AuntMinnie forums) of being charged to export — searched twice, nothing retrievable. May exist in non-indexed or login-gated forums.
12. **KLAS reports** — paywalled. I used secondary Radiology Business coverage (>30% of PACS users considering replacement; RIS/PACS integration drives satisfaction) and did not see primary KLAS data on contract/egress terms.

### Q2c
13. **Site-specific population rates** for (0008,1070) Operators' Name, (0018,1030) Protocol Name, (0018,0015) Body Part Examined. The literature establishes these are *unreliable in general*; only a scan of the actual archive gives real rates. **This should be a Phase 1 deliverable, not a pitch assertion.** Cheap to do via QIDO-RS/Orthanc.
14. **MPPS deployment rate in US small outpatient centers** — no survey found. The 2005 paper implies a deployment gap; current prevalence unknown. **Verify per scanner.**
15. **Full text of the JDI 2019 ultrasound paper** — the abstract truncates mid-sentence at the savings figure ("over $10,000 ... when utilization data showed that thr..."). The >$10,000 figure is solid; the surrounding detail is not. Paywalled.
16. **US outpatient reject-rate benchmarks** — the 10.3% figure is an **Australian ED**. No US outpatient equivalent found.
17. **Physica Medica full text** — direct PDF returned **HTTP 403**; findings above are from the PubMed abstract (which is detailed and sufficient for the claims made).
18. **Whether any specific PACS exposes MPPS/timestamps through its API** rather than only storing them. Capability-to-access is the actual commercial question and is undocumented publicly.

### Q2d
19. **AWS HealthImaging native C-STORE/DIMSE support** — not confirmed; appears S3/API-import oriented, likely needing a DICOM router in front of modalities. **Low.**
20. **Real-world cloud cost for a specific center.** Unit prices are verified; total cost depends on study volume, instance counts (Azure charges **per instance** on multi-part requests), retention and tiering. Needs modeling against Luis's projected volumes — the per-GB rates alone will mislead.
21. **FHIRcast production deployments at small centers** — none found. Evidence is RSNA demonstrations and vendor press releases. The Firely "40%" is self-selected-survey, vendor-published, with an undefined metric.
22. **A published case study of a unified DICOM+FHIR operational data layer at a small outpatient imaging center.** **None found.** The Erlangen pipeline is a large academic hospital doing *research* integration. **If the pitch implies this is a proven pattern at small-center scale, that is not supported — it is a defensible architecture built from production-real components, which is a different and more honest claim.**
23. **Google Cloud Healthcare API explicit "GA" wording** — not captured verbatim in my scrape; GA status is inferred from published production pricing and general availability. **Medium.**

### Q2e
24. **Which specific vendors currently claim SWF.b / REM / IOCM / XDS-I.b conformance.** The verification *mechanism* is confirmed and documented above, but I did not execute per-vendor lookups — the Gazelle Product Registry UI returned **HTTP 503** during this session. Running step 2–3 of the procedure for the 2–3 shortlisted vendors is a concrete, fast next action.
25. **Connectathon SEAL criteria** — the site references a SEAL; I did not verify what earning one requires.

---

## Suggested next actions

1. **Run the IHE verification procedure (steps 1–3) against the 2–3 shortlisted vendors.** Highest leverage per hour of any item here; blocked only by a transient 503.
2. **Decide the vendor shortlist on DICOMweb evidence.** On documented DICOMweb alone, **Sectra, Fujifilm Synapse and Visage** are evidenced; **RamSoft OmegaAI** is plausible and worth a direct conformance request given its small-center fit. Ambra/InteleShare and eRAD should be understood as proprietary-API platforms.
3. **Scope a Phase 1 metadata audit as a deliverable.** QIDO-RS (or Orthanc as a DICOMweb client) against the existing/candidate archive to measure actual population rates for Tier 2 tags and MPPS presence per scanner. This converts gaps #13 and #14 from risks into billable findings — and fits the $12k Phase 1 / 90-day-gate structure.
4. **Build the pitch on Tier 1 timestamps + Station Name.** Utilization, idle time, exams-per-hour and room-day length need nothing unreliable, and the JDI 2019 ultrasound paper is a peer-reviewed precedent with a documented five-figure saving in an outpatient-relevant modality.
5. **Drop any "data hostage" dollar figure.** Reframe as the contractual-unknown argument (see Q2b). It is better sourced, and it avoids a narrative that sits badly next to Fernando's Akumin litigation.
6. **Fix the two technical errors before the deck is built:** CTDIvol is **(0018,9345)**, not (0018,1152); and **MAWF is retired** — use **REM** for dose.
