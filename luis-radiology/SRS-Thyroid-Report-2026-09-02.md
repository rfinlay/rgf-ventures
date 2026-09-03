# Software Requirements Specification: RadAssist Thyroid Report Module

**Prepared by:** Rick Finlay / RGF Global Ventures  
**Date:** 2026-09-02  
**Primary source:** Luis Ramos workflow session, 2026-09-02, Plaud transcript and screen walkthrough  
**Status:** Draft v0.1 for stakeholder confirmation

## 1. Purpose and Scope

Build a web-based RadAssist module that converts Luis's thyroid-ultrasound findings into a consistent structured report faster than his current voice-recognition workflow. Version one supports physician-entered findings, optional detailed TI-RADS scoring, automatic numbering and guideline logic, and editable report generation. It does **not** interpret raw ultrasound images or make autonomous diagnoses.

## 2. Actors

- **Radiologist:** reviews images, determines findings, confirms TI-RADS classification, edits and approves the report.
- **Ultrasound technologist:** supplies measurements and descriptive characteristics with variable quality and formatting.
- **RGF administrator:** configures templates, licensed modules, users, and releases.
- **Facility IT:** approves any future Exa/PACS or DICOM integration.

## 3. Functional Requirements

| ID | The system shall | Priority | Source | Acceptance criteria |
|---|---|---|---|---|
| THY-001 | Provide fields for indication and comparison, including “no prior available.” | Must | 00:26–00:28, 00:39 | Both fields appear in the generated report and remain editable. |
| THY-002 | Capture gland size, echogenicity/echotexture, and vascularity through dropdowns. | Must | 00:31–00:40 | Luis can complete the gland section without dictation. |
| THY-003 | Capture three dimensions and volume for each lobe and an isthmus measurement. | Must | Email samples and 00:39–00:41 | Values retain units and decimals and populate the correct side. |
| THY-004 | Support any number of nodules across right lobe, left lobe, and isthmus. | Must | 00:27–00:29, 00:44–00:50 | Users can add, edit, delete, reorder, and automatically number nodules. |
| THY-005 | Capture each nodule's maximum size, region/pole, and final TR category. | Must | 00:41–00:54 | Generated findings identify location, size, and TR category for every entered nodule. |
| THY-006 | Offer two documentation modes: simplified final TR category or detailed ACR feature scoring. | Must | 01:31–01:35 | User can choose final-category entry or composition/echogenicity/shape/margin/echogenic-foci scoring without losing data. |
| THY-007 | Calculate a proposed TI-RADS score/category from detailed feature selections. | Should | 01:31–01:35 | Calculation matches the validated reference set; physician confirmation is required. |
| THY-008 | Apply size- and category-specific recommendation logic to clinically significant nodules only. | Must | 00:50–00:55 | Subthreshold nodules do not receive inappropriate biopsy or follow-up recommendations. |
| THY-009 | Draft an editable impression summarizing gland findings and clinically significant nodules. | Must | 00:50–00:55 | Impression correctly counts qualifying nodules and links each recommendation to the relevant nodule. |
| THY-010 | Generate, preview, copy, and reset the complete report. | Must | 00:44–00:46, 01:23 | Nothing is copied or cleared without an explicit user action. |
| THY-011 | Provide light/dark mode and English/Spanish interfaces. | Should | 01:23 | Both modes and languages preserve fields and report logic. |
| THY-012 | Run behind the same MFA-protected RadAssist login with module-based licensing. | Must | 00:58–01:00, 01:30–01:36 | Authorized users see only licensed modules; authentication is shared. |
| THY-013 | Optionally extract lobe measurements from a de-identified screenshot for physician confirmation. | Should | Email samples; 00:29–00:31 | Uncertain or conflicting OCR values are flagged and never silently accepted. |
| THY-014 | Offer a selectable TI-RADS report detail level, independent of the input mode: concise final category, or a justified breakdown printing every scored feature and the point total that produced the category. | Must | 01:32–01:34 | The same case renders at both detail levels with no contradiction. Default is per-user in Settings, with a per-study override. Luis's default is concise. |
| THY-015 | Print the score justification honestly when the physician overrides the computed category, showing both the feature-derived score and the physician's final category. | Must | 01:32–01:34 | An overridden nodule never presents the computed point total as if it produced the final category, and the disagreement is visible rather than hidden. |

## 4. Non-Functional Requirements

- **Privacy:** PHI processing stays browser-local for the MVP; no screenshot or patient value is transmitted to a model provider.
- **Clinical control:** Every extracted, calculated, recommended, and generated value remains editable and requires physician review.
- **Performance:** A routine report should be prepared in seconds after findings are entered.
- **Compatibility:** Current target is Windows and Chrome alongside web-based Exa.
- **Usability:** The module must reduce dictation and disorganized technologist input, not reproduce it.
- **Safety:** Decimal values, laterality, units, nodule identity, and recommendation thresholds require deterministic validation.

## 5. User Stories

- As a radiologist, I want dropdown-driven thyroid reporting so that poor voice recognition does not consume my time.
- As a radiologist, I want simplified and detailed TI-RADS modes so that I can choose the documentation depth appropriate to the case.
- As a radiologist who documents defensively, I want every scored feature and the resulting point total printed in the report so that the record shows why each TR category was assigned if my read is later questioned.
- As a radiologist, I want automatic numbering and recommendations so that multiple nodules remain consistent and traceable.
- As a radiologist, I want an editable impression and report so that I retain final clinical authority.

## 6. Business Rules and Constraints

- TR5 is Highly Suspicious; the earlier TR4 label was a source typo.
- The largest relevant dimension drives guideline thresholds unless Luis confirms otherwise.
- Nodules below the applicable threshold must not generate unnecessary follow-up or FNA language.
- The application assists documentation and guideline application. It does not diagnose malignancy.
- Version one is screen/form based. Direct Exa, PACS, and DICOM access requires facility approval and a separate compliance/integration phase.

## 7. Data and Integrations

Core entities: Study, Gland Findings, Lobe Measurement, Isthmus Measurement, Nodule, TI-RADS Feature Set, Recommendation, Impression, Report Template, User, License Module.

Current external references: ACR TI-RADS rules and Luis's preferred calculator at pcheng.org. Future integration candidates are Exa/PACS and raw DICOM, subject to IT approval.

## 8. Assumptions

- Luis remains the final interpreter and approver.
- The first module can create material value without raw-image interpretation.
- Representative de-identified examples will be available for validation.

## 9. Dependencies

- Luis confirmation of exact recommendation thresholds and preferred language.
- Validated ACR TI-RADS rule set and test cases.
- Representative normal, single-nodule, multinodule, threshold, and exception cases.
- Facility approval before any direct PACS/DICOM integration.

## 10. Risks

- Variable output from 25 machines and 14 technologists may reduce OCR reliability.
- Incorrect laterality, decimal placement, or recommendation logic could affect patient care.
- Scope could drift from report automation into raw-image diagnosis.
- Current productivity baseline is incomplete, weakening pricing and ROI evidence.

## 11. Open Questions

1. Confirm the exact ACR version, thresholds, follow-up intervals, and report wording.
2. ~~Should detailed scoring store every feature in the report or only the final category?~~ **CLOSED 2026-09-02 — both, physician-selectable.** The transcript answers this at 01:32–01:34: "Many of the radiologists like to put each one of these characteristics per value. You could have it as an option." Luis does not want it for himself ("I don't like to put that in the report") but identifies it as defensive documentation others rely on ("Some people like to protect themselves by putting each one of them characteristics in there"), and as what makes the tool complete. This is a **market requirement, not a Luis requirement** — it widens the product beyond the pilot user. Captured as THY-014 and THY-015.
3. Should the impression be fully generated, generated then edited, or manually entered by default?
4. How should prior biopsies, interval growth, and previously characterized nodules modify recommendations?
5. What is the maximum number of nodules reported per study and per lobe?
6. What is the desired Spanish report output, interface only or interface plus report?
7. What time-per-study target defines MVP success?

## 12. Action Items

- Rick/RGF: convert this draft into the MVP backlog and clickable workflow.
- Luis: confirm rules, wording, and the three open scope choices above.
- Rick/RGF and Luis: validate against a representative de-identified case set before clinical use.
- Rick/RGF: keep raw-image interpretation, DICOM calcium quantification, and lung-nodule management as separate discovery tracks.

