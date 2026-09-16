# RadAssist Calcium-Score Pilot
## Testing & Training Guide

**Prepared for:** Dr. Luis Ramos
**Prepared by:** Rick Finlay, RGF Global Ventures
**Version:** Pilot 1 (standalone)

---

### What this is
A standalone tool that turns your coronary calcium-score inputs into a **complete, ready-to-paste report** — the exact loop you showed us: per-vessel Agatston scores → total → MESA percentile → finished report text.

It runs **entirely on your own computer.** No patient data leaves the machine, and it needs no internet connection.

### What it does *not* do (yet, by design)
- It does **not** read from Exa or write into your report automatically. That is the next phase. This pilot is the standalone calculator and report generator: you enter the numbers, it hands you the finished report text to paste.
- It does **not** interpret images. You are the radiologist. RadAssist only handles the pre-cognitive work around the read.

---

### How to open it
Double-click **`RadAssist-CalciumScore.html`**. It opens in your web browser and works **offline** — nothing installs, nothing uploads. You can bookmark it or keep it on your desktop.

### How to use it (the loop)
1. **Enter the four per-vessel Agatston scores:** Left Main, LAD, LCx, RCA. *(If you already have the aggregate total, use the Total field instead.)*
2. **Enter the patient factors:** Age (45–84), Gender, and Race/Ethnicity (White, African-American, Hispanic, or Chinese).
3. **Click Generate.**
4. It shows the **total Agatston score**, the **MESA percentile**, and the **probability of non-zero calcium**.
5. It produces the **complete report** — PROCEDURE, TECHNIQUE, BACKGROUND, FINDINGS (your vessel scores), IMPRESSION (total + percentile), and the citation.
6. Click **Copy** and paste it into your report.

---

### Please put it through these tests
Run it the way you actually work, and try these specifically:

1. **A normal case.** A typical calcium-score read from your day. Does the generated report match how you would write it?
2. **Zero calcium** (all vessels 0). Does the impression read correctly?
3. **Total-only entry.** Enter just an aggregate total, leave the vessels blank. Confirm it does **not** invent vessel numbers.
4. **Out-of-range age** (try 40 or 90). Confirm it clearly warns that the MESA percentile is only valid for ages 45–84.
5. **Percentile check.** For the same inputs, compare its percentile to what the **official MESA tool** gives you. They should match.
6. **The wording.** Read the boilerplate (TECHNIQUE, BACKGROUND). How close is it to your real template? Where does it differ?

### What we most want your eyes on
- **Percentile accuracy** versus your MESA tool.
- **Is the report paste-ready,** or does the wording need changes?
- **Your exact template language.** We drafted the boilerplate from your screenshots; tell us the precise wording you want and we will make it match exactly.
- **Anything missing** or anything that would slow you down.

### Known limits (this pilot, on purpose)
- The MESA percentile is valid for **ages 45–84** and the **four ethnicity categories** — those are the MESA tool's own limits, not ours.
- The boilerplate wording is our **best draft from your screenshots.** Nailing down your exact template text is one of the main goals of this test.
- **Standalone only:** no Exa read/write yet. That is the next phase, and it needs a short call with your IT group.

---

### How to send feedback
Inside the tool there is a **Feedback** button. Click it, jot down what worked, what did not, any wording you want changed, and anything missing. Click **Copy feedback**, then send it to **Rick** (text or email). That is the whole loop — your notes go straight to Rick, and we turn them into the next version.

*Prefer paper? There is a one-page feedback sheet attached you can fill in and hand back to Rick instead.*

---

*RadAssist runs locally and stores nothing. This guide and the tool contain no patient health information. Questions go to Rick, and Rick brings them to us.*
