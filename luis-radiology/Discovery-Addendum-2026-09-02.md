# Luis Workflow Discovery Addendum: 2026-09-02

## Decisions reached

- Build the **Thyroid Report module first** as structured reporting with dropdowns, physician-entered findings, optional detailed scoring, automatic numbering, recommendations, and editable output.
- Deliver through the existing web-based, MFA-protected RadAssist platform with modules enabled by license.
- Preserve the physician as final authority. Generated content is reviewed, edited, and accepted before use.
- Support both simplified TR-category entry and detailed characteristic-based calculation.
- Treat Exa/PACS integration as a later approved integration, not an MVP dependency.

## Economic value statement

Luis receives many low-paying thyroid and calcium-score studies that consume time he could use for higher-paying MRI and CT work. The product's value is not the fee for the automated study alone. It is the higher-value reading capacity recovered by removing repetitive documentation and guideline work.

## Separate future discovery tracks

### A. Calcium-score quantification from raw DICOM

Luis proposed adding Agatston-score post-processing: identify coronary calcium, assign vessel identity, calculate lesion/vessel/total scores, and feed RadAssist's existing report engine. This requires raw DICOM access, validated quantitative imaging, clinical performance evidence, PACS/vendor integration, and likely a materially different regulatory analysis. A screen recording or compressed Exa viewer stream is not an adequate assumed substitute for raw DICOM.

### B. Lung-nodule module

Luis proposed a separate module that captures nodule size, attenuation, patient factors, and guideline logic to generate follow-up, PET/CT, biopsy, or no-follow-up recommendations. The transcript called the classification “LIRAD,” but the cited guideline family was the **Fleischner Society**. The exact classification terminology and rule set remain open and must be confirmed before specification.

### C. Local clinical agent/appliance

The long-term concept remains a local agent that can operate approved RadAssist modules and prepare a physician review queue. The session did not establish that local processing alone makes the system automatically HIPAA compliant or contractually permitted. BAAs, facility policy, access controls, auditability, and PACS/DICOM authorization still apply.

## Corrections to avoid carrying forward

- MFA is one safeguard, not proof that a tool “meets all HIPAA requirements.”
- A locally installed agent may still create HIPAA, security, contractual, and medical-device obligations.
- The system must not claim it can learn diagnostic behavior merely by watching screen activity without a defined labeled-data, validation, and governance program.
- Siemens interest was relayed verbally by Luis and is a lead to validate, not a committed buyer or purchase offer.

## Missing evidence

- Current thyroid studies per week and minutes per study.
- Current calcium studies per week and before/after minutes per study.
- Error and correction rates by field and source layout.
- Representative examples from the claimed 25 machines and 14 technologists.
- Exact Exa/PACS/DICOM export and integration capabilities.
- Facility and client authorization for recording, exporting, or processing clinical data.

