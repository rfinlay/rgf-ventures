# RadAssist Unified Product Requirements

**Prepared by:** Rick Finlay / RGF Global Ventures  
**Date:** 2026-09-02  
**Sources:** Luis Ramos emails, sample reports, RadAssist pilot feedback, and 2026-09-02 Plaud workflow session  
**Status:** Draft v0.2, pending Luis confirmation and market research

## 1. Product Definition

**RadAssist is one modular, web-based radiology workflow platform.** Users authenticate once through MFA and receive access to separately licensed clinical workflow modules. The shared shell provides English/Spanish interfaces, light/dark modes, physician review controls, common templates, auditability, and future integration services.

The platform is not a collection of unrelated apps. Calcium Score, Thyroid Report, Lung Nodule, and future clinical workflows are modules behind the same RadAssist identity, licensing, navigation, and security boundary.

## 2. Product Opportunity

Luis identified a repeated market problem: radiologists spend disproportionate time on lower-paid, guideline-heavy studies and incidental findings, reducing capacity for higher-paid MRI and CT interpretations. RadAssist removes repetitive data entry, calculations, report assembly, and guideline lookup while preserving physician interpretation and approval.

Potential customers identified in the session:

1. **Independent and freelance radiologists** who need portable tools to deliver services across hospitals.
2. **Radiology groups** that need consistent structured reporting and faster throughput.
3. **Hospitals and imaging centers** that lack post-processing software or subspecialty coverage.
4. **Imaging-equipment and PACS vendors** that may partner, license, acquire, or embed validated modules.
5. **Luis's proposed imaging center**, which could become a design partner and reference environment.

Luis relayed possible Siemens interest after a conversation with a regional finance leader. This is an **unverified commercial lead**, not a buyer commitment.

## 3. Shared Platform Requirements

| ID | The system shall | Priority | Source |
|---|---|---|---|
| PLT-001 | Provide one RadAssist web application and one MFA-protected account across all modules. | Must | 00:58–01:00; 01:30–01:36 |
| PLT-002 | Enable modules through separate user or organization licenses. | Must | 01:20–01:24; 01:30–01:36 |
| PLT-003 | Support English and Spanish interfaces and reports where configured. | Must | 01:23 |
| PLT-004 | Support light and dark interface modes. | Must | 01:23 |
| PLT-005 | Permit multiple module windows/tabs under the same authenticated session. | Should | 01:35–01:36 |
| PLT-006 | Require physician review before report text, measurements, calculations, classifications, or recommendations are accepted. | Must | Throughout workflow walkthrough |
| PLT-007 | Provide Generate, Preview, Copy, Edit, and New Study controls consistently across modules. | Must | Current RadAssist and 00:44–00:46 |
| PLT-008 | Clear patient data and images between studies and prevent cross-case leakage. | Must | Existing RadAssist safety requirement |
| PLT-009 | Keep PHI browser-local for screen/form MVP functions and prohibit new egress without an approved architecture. | Must | Existing architecture; 01:15–01:17 |
| PLT-010 | Expose approved integration connectors without coupling every module directly to PACS. | Should | 01:18–01:20; 01:30–01:36 |
| PLT-011 | Record module use, physician corrections, processing time, and failures without storing unnecessary PHI. | Should | ROI gap and learning objective |
| PLT-012 | Support organization-level templates, rule versions, and controlled releases. | Should | Commercialization discussion |

## 4. Module A: Calcium Score Reporting

### Current capability

- Browser-local OCR from a calcium-score report screenshot.
- Vessel and total score extraction with decimal and arithmetic validation.
- MESA percentile support and guideline-aligned report generation.
- Full-screen detection plus manual crop and correction fallback.

### Near-term requirements

| ID | Requirement | Priority |
|---|---|---|
| CAC-001 | Continue to accept both full-screen and cropped source images. | Must |
| CAC-002 | Preserve vessel, total, percentile, laterality, and decimal accuracy with physician confirmation. | Must |
| CAC-003 | Capture correction and time-saved metrics for commercial proof. | Must |
| CAC-004 | Support guideline/version management and editable output templates. | Must |

### Luis acceptance feedback from the 2026-09-02 session

- The previous workflow could lose decimal points, including a value such as `26.9`, when Luis pasted a full-screen Snipping Tool capture with lower effective text resolution.
- A tight crop of the pertinent measurement table worked reliably and remained faster than manual reporting.
- Luis double-checks all extracted values before use.
- Luis said he had **not tested the latest full-screen deployment** during the session. The deployed automatic focus, crop-before-upscale, decimal-conflict protection, missing-field reconciliation, and memory cap remain pending real-case acceptance testing.
- Manual tight crop is the proven fallback until the full-screen release passes Luis's representative cases.

| ID | Requirement | Priority |
|---|---|---|
| CAC-005 | Preserve decimal values in full-screen and tightly cropped source images, including representative values such as `26.9` and `49.4`; never silently convert them to `269` or `494`. | Must |
| CAC-006 | When OCR passes disagree or arithmetic validation fails, retain the safer result or require physician review rather than silently overwriting a value. | Must |
| CAC-007 | Validate the current full-screen release on paired full-screen and tight-crop images from Luis's real layouts before closing the decimal-loss defect. | Must |

## 5. Module B: Coronary Calcium Quantification

This is a future RadAssist license that calculates Agatston scores from CT data rather than consuming scores produced by another system.

| ID | Requirement | Priority | Status |
|---|---|---|---|
| AGT-001 | Import the appropriate noncontrast cardiac CT series in DICOM format. | Must | Discovery |
| AGT-002 | Validate acquisition metadata, including slice thickness and pixel geometry. | Must | Discovery |
| AGT-003 | Detect candidate calcified regions above the validated attenuation threshold. | Must | Discovery |
| AGT-004 | Permit physician/technologist vessel assignment and correction for left main, LAD, LCx, RCA, and configured vessels. | Must | Confirmed concept |
| AGT-005 | Calculate lesion, vessel, and total Agatston scores using a validated published method. | Must | Discovery |
| AGT-006 | Present segmentation overlays and require human confirmation before committing scores. | Must | 01:03–01:10 |
| AGT-007 | Send confirmed results into the existing Calcium Score Reporting module. | Must | 01:05–01:08 |
| AGT-008 | Support the majority normal-anatomy workflow while routing variants and low-confidence cases for manual review. | Must | 01:09–01:10 |

**Constraint:** compressed screen recordings or viewer screenshots must not be assumed equivalent to raw DICOM for quantitative scoring. Feasibility, performance, and regulatory status require formal validation.

## 6. Module C: Thyroid Report

The detailed requirements live in `SRS-Thyroid-Report-2026-09-02.md`. Core functions are gland dropdowns, three dimensions plus volume per lobe, multiple nodules by region, simplified or detailed ACR TI-RADS entry, automatic numbering, threshold-based recommendations, editable impression, and physician-confirmed report generation.

## 7. Module D: Lung Nodule Reporting

| ID | Requirement | Priority | Status |
|---|---|---|---|
| LNG-001 | Capture incidental lung-nodule size, location, attenuation/type, and applicable patient factors. | Must | Draft |
| LNG-002 | Support physician marking/measurement input from a screenshot or approved integration. | Should | Draft |
| LNG-003 | Apply a validated lung-nodule guideline rule set and version. | Must | Draft |
| LNG-004 | Generate editable finding and recommendation text for no follow-up, interval CT, PET/CT, or biopsy pathways as supported by the chosen guideline. | Must | Draft |
| LNG-005 | Require physician confirmation and allow override with a reason. | Must | Draft |
| LNG-006 | Insert the lung-nodule finding and recommendation into the active RadAssist report workflow. | Must | Draft |

**Terminology open:** the transcript says “LIRAD classification” but also names the Fleischner Society. This is likely a transcription or terminology error. The correct rule set must be established before build.

## 8. Future Local Clinical Agent

The long-term agent may operate licensed RadAssist modules, prepare a queue of draft outputs, learn nonclinical workflow preferences, and surface exceptions for physician review. It must not autonomously interpret, sign, communicate, or finalize clinical results.

Local execution alone does not establish HIPAA compliance. Facility authorization, BAAs where applicable, least privilege, encryption, audit logs, patching, retention controls, and validated PHI boundaries remain required.

## 9. Commercial and Packaging Requirements

- Sell modules separately under one platform subscription.
- Support individual radiologist and organization licensing.
- Preserve data portability and prevent one module purchase from exposing another.
- Measure value through minutes saved, additional higher-value studies completed, correction rate, and deployment/support cost.
- Maintain a vendor-partnership path without depending on acquisition.
- Protect product IP and do not represent informal vendor interest as a sale.

## 10. Recommended Build Sequence

1. **Thyroid structured-report MVP:** fastest path to Luis value using known forms and rules.
2. **Shared module shell and licensing:** formalize the current RadAssist platform without rewriting proven calcium reporting.
3. **Lung nodule structured-report discovery/MVP:** guideline-driven workflow after terminology and inputs are confirmed.
4. **Exa/PACS/DICOM connector discovery:** read-only integration with facility IT approval.
5. **Agatston quantification spike:** validate DICOM ingestion, scoring math, overlays, and human correction on de-identified datasets.
6. **Regulatory/commercial gate:** determine whether quantification crosses into regulated medical-device software before product release.
7. **Local clinical agent:** only after modules, data boundaries, auditability, and economics are proven.

## 11. Critical Open Questions

1. Which exact guidelines and versions govern thyroid and lung recommendations?
2. What is Exa's approved integration surface: DICOMweb, query/retrieve, export, API, or screen only?
3. Can Southwest X-Ray authorize de-identified DICOM export for development and validation?
4. Who performs calcium segmentation in the target customer workflow: radiologist, technologist, or AI with correction?
5. What sensitivity, specificity, repeatability, and failure-rate thresholds are required for quantification?
6. What FDA classification and quality-system obligations apply to each module?
7. What are the real weekly volumes, minutes per study, correction rates, and revenue effects?
8. Is Spanish required for interface only, report output, or both?

## 12. Immediate Actions

- Confirm this unified platform definition with Luis.
- Groom the Thyroid MVP backlog from the detailed SRS.
- Obtain representative de-identified thyroid cases and exact report language.
- Preserve RadAssist usage metrics without PHI.
- Research competitors, open-source components, DICOM standards, and regulatory boundaries before selecting the Agatston and lung-nodule architecture.
