# Response log: Rick's review round of 2026-11-02

Applied 2026-11-02/03 by Alan. Inputs: the marked-up speaking notes (.docx, 4 comments + 151 yellow runs merged to 140 passages), the marked-up deck (.pdf, 6 highlight annotations with popups; pypdf lists 12 annotation objects because each highlight carries a popup), and the verbal items R1 to R6 in `REVIEW-CHANGES-2026-11-02.md`. Meeting is now **lunch, Thursday 2026-11-05**, with Luis, Fernando Escarzaga and Jesse Martinez.

Files touched: `imaging-center-automation-deck-2026-10-20.html`, `SPEAKING-NOTES-2026-10-20.md`, `imaging-center-automation-leavebehind-2026-10-20.html`, `RUNBOOK-2026-10-20.md`, `DEMO-SCRIPT.md`, `demo-script.html`, `AUTOMATION-CANDIDATES.md`, `imaging-center-architecture-2026-10-20.html`, plus all eight PDFs re-rendered. Workspace script `scripts/md-to-pdf.py` gained `==text==` highlight support (renders as `<mark>`, yellow).

## Word comments (speaking notes .docx)

| # | Anchored text | Rick's comment | What changed | Files |
|---|---|---|---|---|
| C1 | "If he names several companies, you are talking to a serial operator: do not explain the software category to him at any point tonight." (slide 1 BEAT) | "Not sure what you mean by this." | Reworded plainly: if he names several companies he has built and run this kind of business more than once; do not explain what a RIS, a billing system, or an interface is; explain only what the agents do. | SPEAKING-NOTES |
| C2 | "not" in "Your ratio will differ. The shape will not." (slide 13 caveat) | "Not sure what is meant by the shape argument." | Caveat now reads: "Your numbers will differ. The pattern will not: cancellations outnumber no-shows many times over, and most of them come with notice." Same change in the slide 13 BEAT, Drill 1 table, deck slide 13 presenter note, and RUNBOOK number 5. | SPEAKING-NOTES, deck (notes), RUNBOOK |
| C3 | "It was live and tested the same day. Every rule in it is his. One case, three minutes." (slide 19 SAY) | "Not sure we have to say this." | Dropped "It was live and tested the same day." (= R3). Kept "Luis sent me his template and his rules. Every rule in it is his." Same cut in DEMO-SCRIPT.md, demo-script.html, the deck slide 19 presenter note, the notes header, the RUNBOOK header, AUTOMATION-CANDIDATES, and the deck slide 19 module caption and leave-behind row 6 (both printed "live and tested in a day"; now "built from his own template and rules" so the screen does not claim what he no longer says). | SPEAKING-NOTES, DEMO-SCRIPT, demo-script.html, deck, leave-behind, RUNBOOK, AUTOMATION-CANDIDATES |
| C4 | The "$150 an hour" answer (slide 29 DEPTH) | "I like this, but I am not sure if 150 is too much... They may want to bring me in full time salaried, who knows." | No change to the rate (pricing stays as approved). Logged as QUESTION 1 and 2 below. The lawyer comparison in the same answer was removed per PDF annotation A6. | none (question) |

## PDF annotations (deck .pdf)

| # | Page / slide | Highlighted | Rick's comment | What changed | Files |
|---|---|---|---|---|---|
| A1 | 16, Records | The outbound paragraph sitting on the Sources footer | "Can we fix the overlap here?" | Root cause: the source footer is absolutely positioned, so a slide's last paragraph could land on it. Added `.slide:has(> .source)` bottom padding (screen and print). Re-rendered and checked slide 16: clear. | deck |
| A2 | 17, Owner numbers | "Luis's 'am I being paid correctly for what I read' reconciliation is the same engine with a different view, and that one already has a customer." | "This is true, but I don't like the comment. It's a different context focus on what an owner manager or key employees in the staffing plan would like to see." | Replaced with an owner user story: "As an owner, I want to ask one question on a Monday morning, which referrer went quiet, what is the appeal rate, are we being paid for what we read, and get the answer from my own numbers, so that I run the center on facts and not on a report someone has to build for me. The manager and the front desk lead see the same numbers from their side: today's schedule, the open authorizations, the slots that just opened." Spoken version added to slide 17 SAY; Luis line dropped (= R2b). Presenter note explains the user-story framing. | deck, SPEAKING-NOTES |
| A3 | 20, Report assistance | "The records: a different build" column running off the page | "Is this messed up?" | Yes, it overflowed. Slide now uses a `dense` class (tighter column type) and the right column was rewritten for R5/R5d, which is shorter. Re-rendered and checked: all four blocks on the page. | deck |
| A4 | 21, FDA | The "Every candidate on the scorecard..." line almost on the Source footer | "Almost overlap, let's see if we can fix this." | Same fix as A1. Checked: clear. | deck |
| A5 | 23, Bus question | "you hold under a perpetual license with the source in your hands." | "Not so sure I want to say perpetual license. In Luis case it will be different from Fernando and Jesse." | Slide bullet now: "Existing product of mine that I extend for you stays licensed to the center, on terms we put in writing, so you are never hostage to me." "Perpetual" removed from every spoken line and document: notes slide 23 SAY and DEPTH (with a "do not say perpetual" note explaining the Luis arrangement is separate), Drill 3, Drill 5, deck presenter note, leave-behind ownership bullet, RUNBOOK bus answer and three tiers, AUTOMATION-CANDIDATES ownership sections, architecture page 5 Tier 3 panel. Logged as QUESTION 3 (what the license terms should say). | deck, SPEAKING-NOTES, leave-behind, RUNBOOK, AUTOMATION-CANDIDATES, architecture |
| A6 | 29, Pricing | "...billed at $150 an hour against a retainer you top up, the way your lawyer works. If the opening date moves..." | "Don't mention the lawyer stuff. Also, not sure on hourly rate is 150 fair?" | "the way your lawyer works" removed from the slide, the deck presenter notes (two places), the notes (slide 29 table note, two DEPTH answers), and the RUNBOOK (two answers). Rate unchanged; see QUESTION 1. | deck, SPEAKING-NOTES, RUNBOOK |

## Verbal items

| Item | Rick | What changed | Files |
|---|---|---|---|
| R1 | Transitions go on the previous slide, as its final block. All slides. | Four questions moved to the slide before them: the RIS/billing vendor question (now closes slide 2, before 3); the cancellation question (closes slide 12, before 13); the chest-pain phone question (closes slide 14, before 15); the Monday-morning question (closes slide 16, before 17); the records-direction question (closes slide 19, before 20). The receiving slides now say where the question lives. Questions asked on a slide (slides 5, 9, 23, 25) were not transitions and stay. Deck presenter notes did not carry those "ask before" lines, so no deck change. | SPEAKING-NOTES |
| R1a | Label each lead-in clearly. | Heading is **LEAD-IN TO SLIDE N (say before you advance)**; defined in "How each slide block works" and the header note. | SPEAKING-NOTES |
| R2a | Reword "if he lights up at something you ask" as requirements elicitation. | Slide 17 BEAT: "If he lights up at any of it, treat it as a requirement, not a reaction: ask what he would want it to answer first, and write his exact words down. The first question he names is the first report the system has to answer." | SPEAKING-NOTES |
| R2b | Drop the Luis "paid correctly / same engine" line; replace with an owner user story and what an owner wants to see; slide too. | Done, see A2. | deck, SPEAKING-NOTES |
| R3 | Drop "It was live and tested the same day." | Done, see C3. `grep "same day"` is clean across the sources (the remaining phrase "open the demo yourself the same day" was changed to "Thursday morning"). | SPEAKING-NOTES, DEMO-SCRIPT, demo-script.html, deck, RUNBOOK, AUTOMATION-CANDIDATES, leave-behind |
| R4 | Thursday 2026-11-05, LUNCH. Sweep dinner/evening wording and the prep checklist. | Every "dinner", "tonight", "evening" and "the night" in the deck notes, speaking notes, runbook, demo script, leave-behind and candidates is now lunch/today/Thursday; `grep -iE "\b(dinner|tonight)\b"` returns 0 across all eight sources. Notes title and runbook title say Lunch; headers state the locked date; Part 4 is "PRE-LUNCH CHECKLIST. READY BY THURSDAY MORNING" (Wednesday night list, re-run sign-in and hotspot Thursday morning); runbook demo checklist says the same. Deck title slide and leave-behind kicker now read "November 2026" (were "October 2026"). Rick's own edit of "Dinner." to "Lunch." on the last line of slide 31 is in. | all |
| R4a | Fernando + Jesse confirmed with Luis. | Both named on the deck title slide, leave-behind header, notes header and runbook header; the lunch line names all three. No change needed beyond R4. | none |
| R5a | "Spec written once either way" read as one shared stack; reword plainly, answer the shared-stack option honestly. | Rewritten per R5d (below). The spoken line says "One specification, written once and reused for every center" and then states the rule. The honest answer to "can one stack serve different owners": yes, with tenant segregation, defensible; separate instances recommended because the boundary is then physical. | deck, SPEAKING-NOTES, RUNBOOK, AUTOMATION-CANDIDATES, architecture, leave-behind |
| R5b | Move the caveat after the RadAssist and records content, as the last block. | Slide 20 notes order is now SAY, DEPTH, BEAT, then **THEN SAY, LAST ON THIS SLIDE, AND ONLY IF MORE THAN ONE CENTER COMES UP**. Deck presenter note says the same. On the slide itself "Which did you mean?" now comes before the stack block. | deck, SPEAKING-NOTES |
| R5c | Records text ran off the page. | Done, see A3. | deck |
| R5d | Two options with a rule: same owners, one shared stack with per-center segregation; different owners, separate instance per center. Why, and either works. | Spoken rule (notes, deck note, runbook objection): same owners, one shared stack, each center's data kept apart, every login scoped to one center; different owners, a separate instance each with its own database, credentials and audit log; either works; no patient record from one center is readable from another. Why: shared owners means one set of books and principals, so the line is already drawn and one stack is simpler and cheaper to run; different owners need a line visible in the system itself. Slide 20 right column, leave-behind row 6, AUTOMATION-CANDIDATES deployment section, architecture page 6 (title, sub, three bottom panels, footer) all restated. The old "costs more, three hosts" line survives only inside the different-owners case. | deck, SPEAKING-NOTES, RUNBOOK, AUTOMATION-CANDIDATES, architecture, leave-behind |
| R6 | Expand HB 300 as DEPTH/IF ASKED, no numbers. | Slide 22 DEPTH now has a six-bullet block on Texas Health and Safety Code chapter 181: who it reaches (broader than HIPAA, reaches Rick directly), training (within a set time of hire, retraining on a material change in law, signed record; no fixed refresher interval, per Sherlock's 2026-11-03 verification), electronic records on a written request faster than HIPAA, no sale of PHI, notice of electronic disclosure, Attorney General enforcement with scaled civil penalties. No day-count, interval or penalty amount; the line to say is "verified against the statute in the specification." Deck slide 22 presenter note carries a one-paragraph version; RUNBOOK never-say list updated. | SPEAKING-NOTES, deck (notes), RUNBOOK |

## Verification

- Page counts (pdfinfo): deck 31, deck no-numbers 27, leave-behind 2, leave-behind no-numbers 2, architecture 8, runbook 25, speaking notes 40 (was 39; the HB 300 block and five lead-ins added a page), demo script 7.
- Deck slides rendered to PNG and checked one by one: no text runs off a slide or onto a source footer (slides 16, 17, 20, 21 re-checked individually at higher resolution).
- Architecture page 6 and leave-behind page 1 rendered and checked after the text changes: everything inside its panel.
- Speaking notes PDF: yellow highlights visible (checked pages 2 and 21); no literal `==` survives in the PDF text.
- grep across all eight sources: 0 hits for dinner/tonight, 0 for "same day", 0 em dashes (the one in the demo script, a UI quote, now uses a comma), "perpetual" and "lawyer" survive only inside "do not say" instructions and the governance phrase "a partner's lawyer can see".
- Render pipeline reused as in the repo: Chrome headless print-to-pdf for the HTML sources, `scripts/md-to-pdf.py` for the notes and runbook (same fonts as the shipped PDFs).

## Highlight placement (140 passages)

Every yellow passage from the .docx is marked in the markdown with `==...==` and renders yellow in the PDF. Where a comment or an R-item rewrote the passage, the new wording is highlighted; where R1 moved a question to the previous slide, the lead-in block is highlighted. One passage (docx paragraph 169) began mid-paragraph and the whole paragraph is marked. Nothing is unplaced.

| # | Docx para | Rick highlighted (start) | Now at md line | Section | Note |
|---|---|---|---|---|---|
| 1 | 19 | "Luis, Fernando, thank you for dinner. | 46 | The first 90 seconds, verbatim | reworded dinner to lunch (R4) |
| 2 | 20 | One sentence on who I am. I build and operate agent systems, and Luis ... | 48 | The first 90 seconds, verbatim | tonight to today (R4) |
| 3 | 21 | I am not here to sell you software tonight. I am here to tell you whic... | 50 | The first 90 seconds, verbatim | tonight to today (R4) |
| 4 | 22 | Before I start, one thing I would rather hear from you than secondhand... | 52 | The first 90 seconds, verbatim | verbatim |
| 5 | 23 | Then stop. Let him answer. Write down the numbers he gives you. Everyt... | 54 | The first 90 seconds, verbatim | night to lunch (R4) |
| 6 | 74 | "I am not here to sell you software tonight. I am here to tell you whi... | 99 | SLIDE 1 · Six months of free decisions · 0:00 to 1:00 | tonight to today (R4) |
| 7 | 82 | "Here is where you are, as I understand it. The MRI is signed. Nobody ... | 115 | SLIDE 2 · Where you are · 1:00 to 3:00 | verbatim |
| 8 | 83 | Today, every operational decision you make is cheap, and you can rever... | 117 | SLIDE 2 · Where you are · 1:00 to 3:00 | verbatim |
| 9 | 84 | On January first, the federal prior authorization APIs go live at the ... | 119 | SLIDE 2 · Where you are · 1:00 to 3:00 | verbatim |
| 10 | 85 | Around March, the build starts, so prior authorization is working befo... | 121 | SLIDE 2 · Where you are · 1:00 to 3:00 | verbatim |
| 11 | 86 | Your target is to open your new center around June, April at the earli... | 123 | SLIDE 2 · Where you are · 1:00 to 3:00 | verbatim |
| 12 | 87 | Greenfield is the entire argument tonight. By the time you open there ... | 125 | SLIDE 2 · Where you are · 1:00 to 3:00 | tonight to today (R4) |
| 13 | 91 | Ask here, before slide 3: "Which RIS and billing vendors are you looki... | 139 | SLIDE 2 · Where you are · 1:00 to 3:00 | moved: LEAD-IN TO SLIDE 3 (R1) |
| 14 | 97 | "Whatever you decide about me, do this. Put four things in every vendo... | 147 | SLIDE 3 · The free move · 3:00 to 5:00 | verbatim |
| 15 | 98 | One. API access to your own data, named in the contract. Not 'availabl... | 149 | SLIDE 3 · The free move · 3:00 to 5:00 | verbatim |
| 16 | 99 | Two. The HL7 interface count and the fee schedule, fixed at signature.... | 151 | SLIDE 3 · The free move · 3:00 to 5:00 | verbatim |
| 17 | 100 | Three. Data export rights, in standard formats, on demand, at no charg... | 153 | SLIDE 3 · The free move · 3:00 to 5:00 | verbatim |
| 18 | 101 | Four. DICOM query permissions, worklist, query and retrieve, DICOMweb,... | 155 | SLIDE 3 · The free move · 3:00 to 5:00 | verbatim |
| 19 | 102 | Before signature these are contract terms. After signature they are ho... | 157 | SLIDE 3 · The free move · 3:00 to 5:00 | verbatim |
| 20 | 115 | "In 2024, Medicare Advantage insurers denied 4.1 million prior authori... | 183 | SLIDE 4 · The headline number · 5:00 to 8:00 | verbatim |
| 21 | 116 | Four in five appeals win. Almost nobody files one." | 185 | SLIDE 4 · The headline number · 5:00 to 8:00 | verbatim |
| 22 | 119 | "That is Medicare Advantage, all services. It is not an imaging number... | 191 | SLIDE 4 · The headline number · 5:00 to 8:00 | verbatim |
| 23 | 127 | Say "four in five," then stop. Count to five in your head if you have ... | 207 | SLIDE 4 · The headline number · 5:00 to 8:00 | verbatim |
| 24 | 131 | "Forty percent of physicians report having staff who work exclusively ... | 215 | SLIDE 5 · Why greenfield matters · 8:00 to 10:00 | verbatim |
| 25 | 132 | You have not hired that person yet. | 217 | SLIDE 5 · Why greenfield matters · 8:00 to 10:00 | verbatim |
| 26 | 133 | Two in five practices end up hiring someone whose entire job is prior ... | 219 | SLIDE 5 · Why greenfield matters · 8:00 to 10:00 | verbatim |
| 27 | 135 | "That is the AMA's 2025 survey of a thousand physicians. It is self-re... | 223 | SLIDE 5 · Why greenfield matters · 8:00 to 10:00 | verbatim |
| 28 | 141 | Pause after "you have not hired that person yet." That is the whole gr... | 235 | SLIDE 5 · Why greenfield matters · 8:00 to 10:00 | verbatim |
| 29 | 145 | "Before any more numbers, let me say what I mean by an agent, because ... | 243 | SLIDE 6 · What an AI agent is · 10:00 to 12:00 | verbatim |
| 30 | 146 | There are two kinds. The first does a job inside your systems. Think o... | 245 | SLIDE 6 · What an AI agent is · 10:00 to 12:00 | verbatim |
| 31 | 147 | The second one you talk to. You text it or call it: how many MRIs did ... | 247 | SLIDE 6 · What an AI agent is · 10:00 to 12:00 | verbatim |
| 32 | 148 | Four guardrails, and they do not bend. A person signs anything clinica... | 249 | SLIDE 6 · What an AI agent is · 10:00 to 12:00 | verbatim |
| 33 | 159 | "You asked Luis about scheduling, phones, and records. Those are real.... | 271 | SLIDE 7 · Part one: the thing you did not ask about · 10:00 | verbatim |
| 34 | 160 | Prior authorization and eligibility verification. It is larger, and it... | 273 | SLIDE 7 · Part one: the thing you did not ask about · 10:00 | verbatim |
| 35 | 168 | "Physicians and their staff spend an average of 13 hours a week on pri... | 289 | SLIDE 8 · What it costs in time · 10:00 to 14:00 | verbatim |
| 36 | 169 | Of the physicians who do not appeal denials, 59% say they do not expec... | 291 | SLIDE 8 · What it costs in time · 10:00 to 14:00 | whole paragraph marked (highlight began mid-paragraph) |
| 37 | 171 | "Survey data, self-reported, physician practices of all kinds, not ima... | 295 | SLIDE 8 · What it costs in time · 10:00 to 14:00 | verbatim |
| 38 | 177 | "CMS used that same hours figure to price the burden at 220 million pr... | 307 | SLIDE 8 · What it costs in time · 10:00 to 14:00 | verbatim |
| 39 | 178 | "That is CMS's projection in the rule. It is not measured savings. Nob... | 309 | SLIDE 8 · What it costs in time · 10:00 to 14:00 | verbatim |
| 40 | 185 | "Since January first of this year, the payers under this rule have to ... | 323 | SLIDE 9 · The dates land on your opening · 14:00 to 17:00 | verbatim |
| 41 | 186 | On January first next year, they have to operate a FHIR Prior Authoriz... | 325 | SLIDE 9 · The dates land on your opening · 14:00 to 17:00 | verbatim |
| 42 | 187 | Your target opening is about five months after that, with prior author... | 327 | SLIDE 9 · The dates land on your opening · 14:00 to 17:00 | verbatim |
| 43 | 189 | "The rule binds payers, not providers. It creates APIs my side can con... | 331 | SLIDE 9 · The dates land on your opening · 14:00 to 17:00 | verbatim |
| 44 | 206 | "Here is the other side of it. At one institution, over four years, 17... | 365 | SLIDE 10 · What a prior auth process actually does all day · 17:00 to 19:00 | verbatim |
| 45 | 207 | A process that approves 95% of what it touches is one you automate, no... | 367 | SLIDE 10 · What a prior auth process actually does all day · 17:00 to 19:00 | verbatim |
| 46 | 209 | "That is one institution, one modality, four years. The national all-s... | 371 | SLIDE 10 · What a prior auth process actually does all day · 17:00 to 19:00 | verbatim |
| 47 | 224 | "Let me make that concrete. An MRI order arrives at nine on a Tuesday. | 401 | SLIDE 11 · One order through prior authorization · 21:00 to 23:00 | verbatim |
| 48 | 225 | It comes in from the referring office and lands in your RIS. The agent... | 403 | SLIDE 11 · One order through prior authorization · 21:00 to 23:00 | verbatim |
| 49 | 226 | And you will not have to take my word for it. The demo exists today, o... | 405 | SLIDE 11 · One order through prior authorization · 21:00 to 23:00 | verbatim |
| 50 | 245 | "A University of California, Irvine study of about nineteen thousand o... | 447 | SLIDE 13 · Scheduling: the empty slot is not a no-show · 19:00 to 22:00 | verbatim |
| 51 | 246 | Nearly everyone pitching imaging automation pitches no-show reduction.... | 449 | SLIDE 13 · Scheduling: the empty slot is not a no-show · 19:00 to 22:00 | verbatim |
| 52 | 247 | What I would build here is small. A waitlist that sees a cancelled slo... | 451 | SLIDE 13 · Scheduling: the empty slot is not a no-show · 19:00 to 22:00 | verbatim |
| 53 | 249 | "That is one academic center over 2022 and early 2023. Your ratio will... | 455 | SLIDE 13 · Scheduling: the empty slot is not a no-show · 19:00 to 22:00 | rewritten (comment 2, "shape") |
| 54 | 261 | "A randomized trial at Massachusetts General, about seven thousand MRI... | 479 | SLIDE 14 · Scheduling: what reminders honestly do · 22:00 to 23:00 | verbatim |
| 55 | 263 | "That is 1.3 percentage points absolute. Vendors will tell you that is... | 483 | SLIDE 14 · Scheduling: what reminders honestly do · 22:00 to 23:00 | verbatim |
| 56 | 264 | Your RIS will do this. Let it." | 485 | SLIDE 14 · Scheduling: what reminders honestly do · 22:00 to 23:00 | verbatim |
| 57 | 275 | Ask before the slide: "Who takes the phone call when a patient describ... | 505 | SLIDE 14 · Scheduling: what reminders honestly do · 22:00 to 23:00 | moved: LEAD-IN TO SLIDE 15 (R1) |
| 58 | 277 | "Phones are a real cost. You are right about that. My recommendation i... | 513 | SLIDE 15 · Answering patients: buy it, do not build it · 23:00 to 25:00 | verbatim |
| 59 | 278 | Here is why. 26.5% of El Paso County residents over five speak English... | 515 | SLIDE 15 · Answering patients: buy it, do not build it · 23:00 to 25:00 | verbatim |
| 60 | 279 | A voice agent that mishandles a patient describing chest pain, or garb... | 517 | SLIDE 15 · Answering patients: buy it, do not build it · 23:00 to 25:00 | verbatim |
| 61 | 280 | I would rather tell you to buy something than build something that is ... | 519 | SLIDE 15 · Answering patients: buy it, do not build it · 23:00 to 25:00 | verbatim |
| 62 | 292 | "Records requests. Two rules work in your favor here, and one problem ... | 543 | SLIDE 16 · Records: the clock and the fee rule both favor automation · 25:00 to 27:00 | verbatim |
| 63 | 293 | The first rule. The 30-day HIPAA clock runs from the day the request i... | 545 | SLIDE 16 · Records: the clock and the fee rule both favor automation · 25:00 to 27:00 | verbatim |
| 64 | 294 | The second rule. The fee you can charge covers the labor to copy, supp... | 547 | SLIDE 16 · Records: the clock and the fee rule both favor automation · 25:00 to 27:00 | verbatim |
| 65 | 295 | The problem. The harder side is outbound. A new center opens with zero... | 549 | SLIDE 16 · Records: the clock and the fee rule both favor automation · 25:00 to 27:00 | verbatim |
| 66 | 297 | "Texas has its own records deadline that is shorter than the federal 3... | 553 | SLIDE 16 · Records: the clock and the fee rule both favor automation · 25:00 to 27:00 | verbatim |
| 67 | 310 | Cut this slide first if you are running long at 28:00. | 583 | SLIDE 17 · The fifth candidate: the numbers the owner actually looks at · 27:00 to 28:00 | verbatim |
| 68 | 311 | Ask before or on the slide: "What do you want to see on one page every... | 577 | SLIDE 16 · Records: the clock and the fee rule both favor automation · 25:00 to 27:00 | moved: LEAD-IN TO SLIDE 17 (R1) |
| 69 | 313 | "The fifth one is the numbers the owner actually looks at. Studies by ... | 587 | SLIDE 17 · The fifth candidate: the numbers the owner actually looks at · 27:00 to 28:00 | verbatim |
| 70 | 314 | All of it already lives in the RIS and the billing system. The problem... | 589 | SLIDE 17 · The fifth candidate: the numbers the owner actually looks at · 27:00 to 28:00 | verbatim |
| 71 | 315 | I have no study to show you here. I have the fact that you will want a... | 591 | SLIDE 17 · The fifth candidate: the numbers the owner actually looks at · 27:00 to 28:00 | Luis line dropped; new owner story highlighted too (R2b) |
| 72 | 316 | And the version I would build is one you can ask questions of. Not a d... | 595 | SLIDE 17 · The fifth candidate: the numbers the owner actually looks at · 27:00 to 28:00 | verbatim |
| 73 | 332 | "Prior authorization and eligibility: build. Strongest evidence, the v... | 625 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 74 | 333 | Reminders and self-scheduling: buy. That is the RIS. | 627 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 75 | 334 | Cancellation backfill: build, small, on top of the RIS. That addresses... | 629 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 76 | 335 | Voice: buy. I integrate. | 631 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 77 | 336 | Records: build, selectively. | 633 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 78 | 337 | Owner reporting: build. | 635 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 79 | 338 | Billing, claims, and the eligibility feed: buy. That is a clearinghous... | 637 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 80 | 339 | Three of the seven, I am telling you to buy." | 639 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 81 | 343 | "Billing is a buy and I am not touching the claims work. What I evalua... | 647 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 82 | 346 | "I am not building an eligibility system. Your billing vendor already ... | 653 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 83 | 349 | "Three of the seven, I am telling you to buy" is the point of the slid... | 659 | SLIDE 18 · The scorecard · 28:00 to 29:00 | verbatim |
| 84 | 354 | "Enough slides. This is RadAssist. Structured radiology reporting, in ... | 669 | SLIDE 19 · Proof: RadAssist, live · 29:00 to 33:00 | verbatim |
| 85 | 355 | The spine module is the one I want to show you, because of how it got ... | 671 | SLIDE 19 · Proof: RadAssist, live · 29:00 to 33:00 | rewritten (R3, "same day" dropped) |
| 86 | 364 | Then hand the table to Luis. "Luis, tell him about a Tuesday. What bro... | 693 | SLIDE 19 · Proof: RadAssist, live · 29:00 to 33:00 | verbatim |
| 87 | 376 | Ask before the slide, to Luis as much as to Fernando: "When your partn... | 715 | SLIDE 19 · Proof: RadAssist, live · 29:00 to 33:00 | moved: LEAD-IN TO SLIDE 20 (R1) |
| 88 | 378 | "One more thing before the boundaries, because it is the one piece of ... | 725 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | verbatim |
| 89 | 379 | The agent drafts. The radiologist signs. Nothing clinical leaves this ... | 727 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | verbatim |
| 90 | 380 | That is RadAssist today, and you just watched it. Calcium reads the sc... | 729 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | verbatim |
| 91 | 381 | Requesting records runs the other way, and it is a different build. DI... | 731 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | verbatim |
| 92 | 382 | Which one did you mean? They are two different builds, and I would rat... | 733 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | verbatim |
| 93 | 384 | "One instance per center, not one shared stack. That costs more, not l... | 759 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | rewritten + moved to last block (R5/R5d) |
| 94 | 393 | "Which direction, and against which RIS. Then I can scope it." | 751 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | verbatim |
| 95 | 395 | Say the heading slowly, then let Luis answer the direction question. W... | 755 | SLIDE 20 · Radiology report assistance · 33:00 to 34:00 | verbatim |
| 96 | 399 | "The FDA question, answered by the statute and not by me. Federal law ... | 769 | SLIDE 21 · Boundaries: the FDA question, answered by the statute · 34:00 to 35:00 | verbatim |
| 97 | 400 | Every candidate on that scorecard is on the list by name. | 771 | SLIDE 21 · Boundaries: the FDA question, answered by the statute · 34:00 to 35:00 | verbatim |
| 98 | 401 | And the agents stop at the clinical boundary. Nothing interprets an im... | 773 | SLIDE 21 · Boundaries: the FDA question, answered by the statute · 34:00 to 35:00 | verbatim |
| 99 | 414 | "Four constraints I am going to design around, stated before you ask. | 799 | SLIDE 22 · Boundaries: what I will design around, stated before you ask · 35:00 to 36:00 | verbatim |
| 100 | 415 | Texas SB 1188. Electronic health records with Texas patient data have ... | 801 | SLIDE 22 · Boundaries: what I will design around, stated before you ask · 35:00 to 36:00 | verbatim |
| 101 | 416 | TCPA, the Telephone Consumer Protection Act. That is the federal law o... | 803 | SLIDE 22 · Boundaries: what I will design around, stated before you ask · 35:00 to 36:00 | verbatim |
| 102 | 417 | The AI vendor's business associate agreement. Anthropic's agreement no... | 805 | SLIDE 22 · Boundaries: what I will design around, stated before you ask · 35:00 to 36:00 | verbatim |
| 103 | 418 | Texas HB 300. Its definition of a covered entity is broad enough to re... | 807 | SLIDE 22 · Boundaries: what I will design around, stated before you ask · 35:00 to 36:00 | verbatim |
| 104 | 420 | "The coverage depends on which version of the agreement is signed and ... | 811 | SLIDE 22 · Boundaries: what I will design around, stated before you ask · 35:00 to 36:00 | verbatim |
| 105 | 432 | "The question you are going to ask is what happens when I get hit by a... | 844 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | verbatim |
| 106 | 433 | You own the specification. It is written for a competent engineer who ... | 846 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | verbatim |
| 107 | 434 | You own the code. It lives in a repository under your organization's a... | 848 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | verbatim |
| 108 | 435 | One distinction, and I would rather raise it myself than have you find... | 850 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | rewritten (A5, no "perpetual") |
| 109 | 436 | Runbooks, not memory. Every operational procedure is written down: how... | 852 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | verbatim |
| 110 | 437 | No proprietary runtime. Standard interfaces, HL7 version 2, DICOM, pay... | 854 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | verbatim |
| 111 | 438 | Buy where buying is right. The RIS and the voice vendor are contracted... | 856 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | verbatim |
| 112 | 439 | The design engagement exists so that this question has a boring answer... | 858 | SLIDE 23 · The question you are going to ask · 36:00 to 37:00 | verbatim |
| 113 | 455 | "What I recommend you do not buy from me. | 892 | SLIDE 24 · The most important slide · 37:00 to 38:00 | verbatim |
| 114 | 456 | A custom voice agent. Buy a vendor. I will specify, evaluate, and inte... | 894 | SLIDE 24 · The most important slide · 37:00 to 38:00 | verbatim |
| 115 | 457 | Reminders, self-scheduling, and intake forms. Your RIS does this. Make... | 896 | SLIDE 24 · The most important slide · 37:00 to 38:00 | verbatim |
| 116 | 458 | Anything built to resell to other centers. I am not building a product... | 898 | SLIDE 24 · The most important slide · 37:00 to 38:00 | verbatim |
| 117 | 459 | Anything that touches the image clinically. Not from me, not from anyo... | 900 | SLIDE 24 · The most important slide · 37:00 to 38:00 | verbatim |
| 118 | 473 | "If it were my money, I would do three things before signing another v... | 928 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 119 | 474 | Put the four access terms into every contract this month. It is free. | 930 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 120 | 475 | Decide now whether the prior authorization desk is a hire or a system.... | 932 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 121 | 476 | And tell me what front desk and prior authorization actually cost you ... | 934 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 122 | 477 | One question for you. What would you do differently this time, knowing... | 936 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 123 | 478 | Then stop and listen. | 938 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 124 | 482 | "And to be clear about what I am not saying. Staff for the manual work... | 946 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 125 | 490 | Ask the closing question and then do not fill the silence. A man with ... | 962 | SLIDE 25 · If it were my money · 38:00 to 38:30 | verbatim |
| 126 | 494 | "The build starts around March so prior authorization works before you... | 970 | SLIDE 26 · What the dates depend on · 39:00 to 40:00 | verbatim |
| 127 | 497 | . The one most likely to slip is vendor selection, because it runs on ... | 976 | SLIDE 26 · What the dates depend on · 39:00 to 40:00 | partial: from "The one most likely" onward |
| 128 | 498 | Do not promise anything beyond the list. If pushed for a guarantee: "T... | 978 | SLIDE 26 · What the dates depend on · 39:00 to 40:00 | verbatim |
| 129 | 499 | Staffing, unprompted: "Staff for the manual workflow at opening. I am ... | 980 | SLIDE 26 · What the dates depend on · 39:00 to 40:00 | verbatim |
| 130 | 505 | "Every one of these decisions is reversible today. None of them will b... | 992 | SLIDE 27 · Thank you · 38:30, then stop selling or turn to the appendix | verbatim |
| 131 | 506 | Thank you, all three of you. Here is a summary you can keep." | 994 | SLIDE 27 · Thank you · 38:30, then stop selling or turn to the appendix | verbatim |
| 132 | 514 | "The rest is reference. It is what it would cost to have me take the n... | 1010 | SLIDE 28 · Appendix: scope and investment · 38:30 | verbatim |
| 133 | 523 | "One engagement for the new center. Forty-five thousand, fixed fee, fi... | 1028 | SLIDE 29 · What I am proposing: one engagement, five phases, $45,000 · 40:00 to 41:30 | verbatim |
| 134 | 525 | "Four thousand when we sign and three when you have the requirements. ... | 1032 | SLIDE 29 · What I am proposing: one engagement, five phases, $45,000 · 40:00 to 41:30 | verbatim |
| 135 | 570 | Outside the phases: $150 an hour, approved first, against a retainer t... | 1047 | SLIDE 29 · What I am proposing: one engagement, five phases, $45,000 · 40:00 to 41:30 | rewritten (lawyer comparison removed, A6) |
| 136 | 586 | "We start in November with discovery, six weeks, and you sign the requ... | 1079 | SLIDE 30 · The seven months, on one page · 41:30 to 42:30 | verbatim |
| 137 | 587 | Then the point of the picture, once: "Every diamond is a document you ... | 1081 | SLIDE 30 · The seven months, on one page · 41:30 to 42:30 | verbatim |
| 138 | 588 | Then stop and let him look. | 1083 | SLIDE 30 · The seven months, on one page · 41:30 to 42:30 | verbatim |
| 139 | 599 | : "This is what each phase needs from you, so nothing on my side is ev... | 1105 | SLIDE 31 · What I need from you · 42:30 to 43:00 | partial: from the quote onward |
| 140 | 612 | Lunch. | 1126 | SLIDE 31 · What I need from you · 42:30 to 43:00 | Rick's own edit (Lunch.) |

## QUESTIONS FOR RICK

1. **The $150 an hour.** You asked whether it is too much (Word comment on slide 29; PDF note on slide 29). I left it at $150 because the engagement pricing was approved 2026-11-02 and nothing in the markup names another number. If you want it lower, tell me the rate and I will carry it through the deck, leave-behind, notes and runbook; the five-phase fee does not depend on it.
2. **Full-time salaried.** You raised that they may want to bring you in full time. The documents do not address it. Do you want an IF ASKED line prepared for that (for example, "I would want to hear it; let us finish Phase 1 first, that is the job to judge me on"), or leave it unscripted?
3. **License wording.** "Perpetual license" is out everywhere; the documents now say the product pieces are "licensed to the center on terms we put in writing." What do you want the terms to be for Fernando and Jesse, and should the Luis/RadAssist arrangement be described anywhere in these documents at all (right now it is not)?
4. **Shared stack as the recommendation.** Per R5d the rule now says same owners, one shared stack. The earlier research position (10-14) recommended separate instances in all cases. If you want the shared-stack option to carry a stated cost or infrastructure line, say so; nothing is priced for it.
5. **Luis picking you up.** The 11-01 note said Luis picks you up; it was written for an evening. Still true for a Thursday lunch? The runbook header keeps it.
6. **The OneDrive Word file.** `Imaging-Center-SPEAKING-NOTES-2026-10-20.docx` in the OneDrive folder is the pre-review version you marked up. I did not regenerate a .docx (no converter on this Mac); the PDF is the reviewed artifact. Do you want a fresh .docx too?
