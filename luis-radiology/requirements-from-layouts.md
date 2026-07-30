# Requirements Captured from Luis's Layouts (de-identified)
**Source:** Dr. Luis Ramos emailed Rick native screenshots of his real workstation, titled by study type. First: **"BRAIN MRI NO PREVIOUS STUDIES"** (2026-07-30).

> **PHI handling:** The source screenshots contain real patient identifiers (name, ID, DOB, referring physician). Only **de-identified, non-patient** requirements detail is recorded below. Raw images are NOT stored in this repo, NOT committed, NOT synced. See the PHI note at bottom.

## 1. Report template structure (pre-fill target — REQ-004)
The report editor (center monitor) uses the **Southwest X-Ray** letterhead and a **template-driven, bracketed-default** structure. This is the key insight for boilerplate pre-fill:

- **Header fields:** Patient Name, Patient ID, Date of Birth, Date of Exam, Referring Physician, Type of Exam.
- **Combined-report capability:** one report can cover two ordered exams (e.g., "MR BRAIN W/WO IV CONTRAST" + "MRI FACE, IACs AND ORBITS W/WO IV CONTRAST").
- **Fixed sections:** COMPARISON, INDICATIONS, IMAGING DEVICE (e.g., 1.5 Tesla MRI), CONTRAST, TECHNIQUE (multiplanar multisequence per institution standardized protocol), FINDINGS, then impression.
- **FINDINGS is a fixed anatomic checklist**, each region pre-loaded with a **normal-default statement in square brackets** that the radiologist keeps or overwrites. For MRI Brain/Orbits the regions are: SELLAR REGION, GLOBES, EXTRAOCULAR MUSCLES, OPTIC NERVES / CHIASM, INTRACONAL SPACES, EXTRACONAL SPACES, CAVERNOUS SINUS, IACs.
- **The automation opportunity is now concrete:** the template already carries normal-default boilerplate per region. Pre-fill = load the right template + normal defaults by exam type; the radiologist edits only the abnormals. RadAssist should key templates to `Type of Exam` and auto-select the matching section set.
- **Editor actions observed:** e-Sign & Approve, Approve and Next, Not Approve, Save, Skip, Pre-Approve. Template selector + "Flag (AUTH APPROVED)" + rich-text controls (Times New Roman). Autosave present.

## 2. MESA calcium-score calculator (REQ-001/002/003)
Right monitor showed the exact tool in use:
- **Tool:** MESA "CAC Score Reference Values" (Coronary Artery Calcium), hosted at **mesa-nhlbi.org** (`/researchers/tools/cac-score-reference-values`).
- **Inputs:** Age (valid range **45–84**), Gender, Race/Ethnicity (**White, African-American, Hispanic, or Chinese** — the four supported categories), and the **Observed Agatston Calcium Score**.
- **Outputs:** estimated probability of non-zero calcium, the **25th/50th/75th/90th percentiles**, and the **observed score's percentile** for that age/sex/ethnicity.
- **Guideline citation baked into the tool:** McClelland RL, Chung H, Detrano R, Post W, Kronmal RA. *Distribution of coronary artery calcium by race, gender, and age: results from MESA.* Circulation 2006;113(1):30–37.
- **Build implication:** this is a public web tool with a small, fixed input set. The pilot automates: read Age/Sex/Ethnicity + Agatston score from the study/report → submit to the MESA tool → capture percentile + non-zero probability → write back into the report. Note the **45–84 age gate and 4 ethnicity categories** as validation edges (out-of-range must be handled, tool literally shows "Out of Range").

## 3. PACS integration detail (REQ-006/007/012)
- **Exa PACS is browser-hosted** at **`exa.swrxsyonline.com`** (confirmed in the address bar; "swrxsy" = Southwest X-Ray). Confirms the **browser-extension/overlay** integration path.
- **Three-monitor workspace:** PACS images (left), report editor (center), reference/calculator web tools + worklist (right). Any overlay must coexist across all three.

## 4. Hanging protocol — Brain MRI, no priors (REQ-006)
- Dense multi-row pane grid of the standard brain sequences (DWI + ADC, T1, T2/FLAIR, sagittal T1, plus dedicated orbit/sellar coronal + axial series), left-hand series **Navigator** with thumbnails.
- "No previous studies" is an explicit layout variant → implies there is a **different** layout when priors exist (side-by-side compare). Expect Luis to send that variant separately. Layout selection should therefore branch on **exam type × priors-available**.

## 5. Layout — Brain MRI WITH prior study (e.g., previous CT) — REQ-007
Second capture: **"BRAIN MRI WITH PREVIOUS CT"** (2026-07-30). This is the priors-available variant of section 4, and it pins down the prior-comparison workflow:
- **Three-monitor arrangement:** current MRI images (left PACS), current report editor (center), and the **prior report opened side-by-side on the right monitor**.
- **Exa exposes a "Prior Reports" viewer** (`exa.swrxsyonline.com/.../studyReports...`) that lists all priors by **modality + date** (e.g., MRI C-spine, MRI L-spine, CT head/brain, US abdomen). The radiologist **manually picks** the relevant prior from that list; the left PACS navigator also shows the chronologic prior-study list.
- **Workflow:** he reads the prior report's findings while dictating the current study, and sets the report's **COMPARISON** field to the prior's modality + date (e.g., "CT <date>").
- **Automation target (concrete):** auto-detect relevant priors by body region/modality, surface the matching **prior report text** (not just images) side-by-side, and **auto-populate the COMPARISON field** with the prior's modality + date. This is the highest-value slice of REQ-007 and it's now fully specified.
- **Report format confirmed:** FINDINGS = narrative bullet statements; **IMPRESSION = numbered list**; same Southwest X-Ray template. Confirms the impression-draft target for REQ-005.
- **Layout selection rule confirmed:** layout branches on **exam type × priors-available** (no-priors grid vs. priors side-by-side-with-report). RadAssist must detect prior existence and pick the layout accordingly.

## PHI note / recommended handling
The screenshots are **live PACS captures with real patient data**. For a HIPAA-safe engagement:
1. **Preferred:** ask Luis to **black out the patient banner** (name/ID/DOB/referring) before sending, or send template/layout mockups with dummy data.
2. **Or** stand up a **BAA + secure, encrypted, non-cloud store** before collecting more real-PHI captures.
3. Gio's handling this session: extracted only de-identified requirements above, then **deleted the local raw image**; originals remain solely in Rick's email.
