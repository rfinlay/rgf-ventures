# Speaking Notes: Imaging Center Dinner

**El Paso, about 2026-10-20. 40 minutes. 25 slides.**
**In the room:** Dr. Luis Ramos (uses RadAssist daily; your champion) and Fernando Escarzaga (founded Southwest X-Ray and sold it in 2019; the skeptic and the signer).

This is a rehearsal sheet, not a reference. Read it aloud, top to bottom, in order. The RUNBOOK is for lookup. This is for practice.

How each slide block works:

- **SAY** is the spoken line. Read it aloud until it sounds like you and not like a page.
- **THEN SAY** is the caveat. It is its own line so you say it unprompted, never as an afterthought when challenged.
- **DEPTH / IF ASKED** is what stands behind the claim: the supporting figures, the source and its limits, what the number is not. Know it. Do not recite it.
- **BEAT** is the physical instruction: where to pause, where to stop, where to write.

---

# PART 1: THE COLD-OPEN CARD

## The first 90 seconds, verbatim

"Luis, Fernando, thank you for dinner.

One sentence on who I am. I build and operate agent systems, and Luis uses one of them every day on real patients. That is the only credential that matters tonight.

I am not here to sell you software tonight. I am here to tell you which decisions you are about to make that are free right now, and will not be free in April.

Before I start, one thing I would rather hear from you than secondhand. Luis told me you built and sold imaging here in El Paso before this. What did you build, and how many centers were you running at the end?"

Then stop. Let him answer. Write down the numbers he gives you. Everything you say about his history for the rest of the night comes from that answer, not from a file.

## Names

- **Fernando.** Never Jesus. His legal first name is Jesus and every business source uses Fernando.
- **Spell it Escarzaga.** Not Escargaza, not Escarcega. Both appear in public records and both are wrong.
- **Veronica Escarzaga** was a named co-seller of Southwest X-Ray. He may not be the only decision-maker. Do not discover her at the table.

## The landmine strip: never say these

| Never say | Why, in five words |
|---|---|
| The Akumin lawsuit, in any form | Active litigation. Knowing it reveals digging. |
| Desert Imaging | Different man, different company. |
| Scale, platform, roll-up, synergies | The vocabulary of the buyer. |
| "Density in key markets" | Near-verbatim from the buyer's press release. |
| "When you sold to private equity" | He sold to a public company. |
| Akumin or Stonepeak as a reference or model | Never praise the buyer. |
| Headcount reduction, displaced FTEs, layoffs | He knows the people who answer phones. |
| His founding year | Three sources, three years. Let him say it. |
| His age | Never. |
| "Jesus" | Fernando. |

If he raises any of it himself: listen, say little, ask nothing, move on.

**The reframe behind every line tonight:** he is not looking to grow. He is reclaiming operational control and building lean on purpose. Say "run this center with a lean front office." Never say "grow."

---

# PART 2: THE 25 SLIDES, IN ORDER

### SLIDE 1 · Six months of free decisions · 0:00 to 1:00

**SAY**

The cold-open card above, word for word. The framing line is the one to get right:

"I am not here to sell you software tonight. I am here to tell you which decisions you are about to make that are free right now, and will not be free in April."

**DEPTH / IF ASKED**

Nothing to defend here. The only claim is that Luis uses RadAssist daily on real patients, and Luis is sitting there.

**BEAT**

Deck on slide 1 while they sit down. Say the framing line slowly. Ask the "what did you build" question before you advance. Write his answer down. If he names several companies, you are talking to a serial operator: do not explain the software category to him at any point tonight.

---

### SLIDE 2 · Where you are · 1:00 to 3:00

**SAY**

"Here is where you are, as I understand it. Equipment is being signed. Real estate is being toured. Nobody is hired, and no systems are chosen.

Today, every operational decision you make is cheap, and you can reverse it.

On January first, the federal prior authorization APIs go live at the payers.

Around April, you open. Whatever is in the vendor contracts by then is what you live with.

Greenfield is the entire argument tonight. In six months there will be a RIS, a billing vendor, a phone system, and people hired around whatever those systems cannot do. Nothing I am going to show you can be done this cheaply after you open."

**DEPTH / IF ASKED**

The January date is CMS-0057-F, the Interoperability and Prior Authorization Final Rule, 89 FR 8758, published 2024-02-08. Compliance dates were verified in the rule text itself: decision timeframes and public reporting from 2026-01-01, the FHIR Prior Authorization API and the Patient Access, Provider Access, and Payer-to-Payer APIs by 2027-01-01. It binds payers, not providers, and covers Medicare Advantage, Medicaid and CHIP, and the federally facilitated exchange plans. Do not expand on it here. It gets its own slide at 9.

Ask here, before slide 3: "Which RIS and billing vendors are you looking at, and have you signed anything yet?" The answer tells you whether the next slide is still free.

**BEAT**

Say the obvious thing plainly. Do not oversell the January date yet.

---

### SLIDE 3 · The free move · 3:00 to 5:00

**SAY**

"Whatever you decide about me, do this. Put four things in every vendor contract before you sign. They cost nothing today.

One. API access to your own data, named in the contract. Not 'available on request.'

Two. The HL7 interface count and the fee schedule, fixed at signature. Not quoted per interface later.

Three. Data export rights, in standard formats, on demand, at no charge.

Four. DICOM query permissions, worklist, query and retrieve, DICOMweb, for the systems you authorize.

Before signature these are contract terms. After signature they are hostage terms. I will give you the exact language."

**DEPTH / IF ASKED**

Why DICOM specifically: it is the one standardized surface that does not depend on vendor goodwill. HL7 version 2 is what the RIS will actually speak. FHIR on the RIS side is aspirational at a small center; the FHIR that matters is on the payer side, by federal rule.

Interface fees are customary and quoted per interface. That sentence is the whole statement. A dollar range for HL7 interfaces circulates widely and could not be verified at any primary source. Do not quote one.

Why export rights matter more than they used to: Mirth Connect, the usual free HL7 engine, went closed-source commercial at version 4.6 in March 2025. The last open release is 4.5.2 from 2024-09-23, unmaintained, which is a security consideration on a path carrying patient data. Verified at the GitHub releases API. You cannot assume a free integration engine anymore, so the data has to be reachable by contract. (Research brief, sections 5.1 and 5.2.)

**BEAT**

This is the slide that proves you are on their side of the table, and it does not matter whether they hire you. Fernando has negotiated these contracts. Watch him. If he nods at "hostage terms," do not explain further.

---

### SLIDE 4 · The headline number · 5:00 to 8:00

**SAY**

"In 2024, Medicare Advantage insurers denied 4.1 million prior authorization requests. Only 11.5% of those denials were appealed. Of the appeals that were filed, 80.7% were partially or fully overturned.

Four in five appeals win. Almost nobody files one."

Stop talking.

**THEN SAY (the caveat)**

"That is Medicare Advantage, all services. It is not an imaging number, because CMS does not collect prior authorization data by type of service. It is the only audited, payer-reported, national figure that exists, and it describes the system your center bills into."

**DEPTH / IF ASKED**

Source: KFF, "Medicare Advantage Insurers Made Nearly 53 Million Prior Authorization Determinations in 2024," published 2026-01-28, analyzing data insurers are required to report to CMS. Mandatory reporting, not a survey.

Supporting figures from the same source: 52.8 million determinations in 2024, up from 49.8 million in 2023. 4.1 million denied, which is 7.7%, up from 6.4% in 2023 and 7.4% in 2022. The appeal rate was 11.7% in 2023 and 7.5% in 2019. The overturn rate was 81.7% in 2023. Over 90% of requests were fully favorable. Ninety-nine percent of Medicare Advantage enrollees are in plans that require prior authorization for some services.

What this number is not: a labor-savings number. It is an abandoned-revenue number. The binding constraint it reveals is staff capacity and follow-through, not clinical merit.

If he quotes an imaging denial rate of 25 to 40% at you: do not confirm it. Those are vendor-blog numbers with no methodology. Say, "I have seen that number and I could not trace it to a source I trust, so I will not use it." The peer-reviewed imaging figure is 4.94%, and it is coming at slide 10.

**BEAT**

Say "four in five," then stop. Count to five in your head if you have to. Let Fernando connect it. He will.

---

### SLIDE 5 · Why greenfield matters · 8:00 to 10:00

**SAY**

"Forty percent of physicians report having staff who work exclusively on prior authorization.

You have not hired that person yet.

Two in five practices end up hiring someone whose entire job is prior auth. For you, the decision to automate or to staff is live right now. It will never be live again."

**THEN SAY (the caveat)**

"That is the AMA's 2025 survey of a thousand physicians. It is self-reported."

**DEPTH / IF ASKED**

Source: American Medical Association, 2025 AMA Prior Authorization Physician Survey. 1,000 practicing physicians, 400 primary care and 600 specialists, nationwide. Figures read directly from the report.

Frame it as revenue capture and capacity, never as headcount. Two reasons. First, El Paso wages run about 25% below the national average across all occupations: the El Paso metro all-occupation mean is $24.94 an hour against $33.54 nationally (BLS, May 2025 El Paso release 26-1364-DAL, dated 2026-08-13). A displaced-FTE argument is worth less here than it sounds. Second, Fernando came up as a technologist and has run departments. If he hears layoffs, he disengages politely and you never find out why. The line is: the work gets done without a bigger org chart.

Ask here: "How many prior authorizations a day were you running at steady state, and who did them?" His answer tells you whether he already lived this statistic.

**BEAT**

Pause after "you have not hired that person yet." That is the whole greenfield argument in one sentence.

---

### SLIDE 6 · Part one: the thing you did not ask about · 10:00

**SAY**

"You asked Luis about scheduling, phones, and records. Those are real. The thing I would put first is the one you did not mention.

Prior authorization and eligibility verification. It is larger, and it has the best evidence."

**DEPTH / IF ASKED**

Nothing to defend. This is a transition.

**BEAT**

Plainly, without any edge. This is not a gotcha. Say it and advance.

---

### SLIDE 7 · What it costs in time · 10:00 to 13:00

**SAY**

"Physicians and their staff spend an average of 13 hours a week on prior authorization. About 40 requests per physician per week.

Here is the part that ties back to the appeal rate. Of the physicians who do not appeal denials, 59% say they do not expect to win, and 52% say they do not have the staff time. Those are exactly the two things an agent removes. Nobody has time, and nobody tracks the odds."

**THEN SAY (the caveat)**

"Survey data, self-reported, physician practices of all kinds, not imaging centers specifically."

**DEPTH / IF ASKED**

Same AMA 2025 survey. Other figures from it if pressed: 32% say prior authorizations are often or always denied. 74% say denials increased over the past five years. 21% always appeal. 95% report care delays. 94% say it contributes to burnout.

Eligibility verification is the front half of the same workflow: it is where the "does this plan require authorization" determination happens. The EDI 270 and 271 eligibility transactions are the oldest and most standardized surface in this space, and the clearinghouse or billing vendor exposes them. There is no separate defensible benchmark on eligibility cost for imaging centers, so do not invent one.

If someone notices the 13 hours here against the 14 hours on the next slide: 13 is the 2025 AMA survey. 14 is the earlier AMA figure CMS cited in its 2024 rule. Say exactly that.

**BEAT**

The two percentages at the bottom are the bridge to the agent. Slow down on "nobody has time, and nobody tracks the odds."

---

### SLIDE 8 · The federal government's own estimate · 13:00 to 15:00

**SAY**

"In its 2024 prior authorization rule, CMS estimated the rule would save providers at least 220 million hours and 16 billion dollars over ten years. They based that on AMA data showing 14 hours per physician per week."

**THEN SAY (the caveat)**

"That is CMS's projection in the rule. It is not measured savings. Nobody has gone back and counted yet."

**DEPTH / IF ASKED**

Source: CMS-0057-F, 89 FR 8758, published 2024-02-08, Regulatory Impact Analysis. Verified in the Federal Register full text.

Why this one lands differently: the source is a binding federal rule, not a vendor and not a consultant. It pre-empts "this is AI hype" before anyone says it. It is still a projection, which is why the caveat is mandatory.

**BEAT**

Give the caveat the same weight as the number. Volunteering it is the point.

---

### SLIDE 9 · The dates land on your opening · 15:00 to 18:00

**SAY**

"Since January first of this year, the payers under this rule have to decide a standard prior authorization in seven calendar days and an expedited one in 72 hours, and they have to publish their numbers.

On January first next year, they have to operate a FHIR Prior Authorization API, plus Patient Access, Provider Access, and Payer-to-Payer APIs.

You open about three months after that, with no legacy process to unwind. And almost 63% of medical plans say they are already building the prior authorization API ahead of the deadline."

**THEN SAY (two caveats, both mandatory)**

"The rule binds payers, not providers. It creates APIs my side can consume. It does not obligate your center to do anything, and it guarantees nothing about data quality or how easy the connection is."

"And it covers Medicare Advantage, Medicaid and CHIP, and the exchange plans. Not every commercial plan."

**DEPTH / IF ASKED**

Source for the dates: CMS-0057-F rule text. For Medicaid and CHIP managed care, the 2027 dates run from the rating period beginning on or after 2027-01-01; for exchange issuers, from plan years beginning on or after that date.

Source for the 63%: 2025 CAQH Index, FHIR and Interoperability module, published by DataSpring (formerly CAQH) on 2026-02-19. Payer self-report.

Commercial plans outside the rule: the design falls back to EDI 278 where supported, and otherwise a complete packet prepared for a human to submit.

A small signal that you read the rule and not a summary: drugs are excluded from CMS-0057, and CMS proposed to close that gap in April 2026. Irrelevant to imaging. Use it only if the conversation is already in the rule.

Ask here: "What is your payer mix going to look like?" If he expects heavy commercial, say so out loud and put less weight on the January date. El Paso payer mix and uninsured rate were not verified by the research. Do not quote either.

**BEAT**

Both caveats, every time. They are the two obvious counterattacks and you want to be the one who says them.

---

### SLIDE 10 · What a prior auth process actually does all day · 18:00 to 20:00

**SAY**

"Here is the other side of it. At one institution, over four years, 17,913 outpatient MRI prior authorization requests went in. 4.94% were denied. The other 95% were approved.

A process that approves 95% of what it touches is one you automate, not one you staff."

**THEN SAY (the caveat)**

"That is one institution, one modality, four years. The national all-service denial rate from the KFF data was 7.7%. Both say the same thing: most of the work is approvals."

**DEPTH / IF ASKED**

Source: Harrer S et al., J Am Acad Orthop Surg, 2025 Feb 15;33(4):e244-e252, PMID 39729599. Cooper University Health Care, orthopaedics, New Jersey payer mix, January 2019 through December 2022. 885 of 17,913 denied. Spine MRI was less likely to be authorized than extremity studies, and two Medicaid payers were significantly less likely to authorize. The authors' own conclusion: the low denial rate "underscores the questionable utility of the prior authorization process."

This is the opposite of a scare statistic, and that is deliberate. Fernando has reconciled real remittances. Do not quote any inflated imaging denial rate; he will know.

Recommendation: build. This is the lead product. What the agent does: detects authorization-required orders at scheduling, assembles the documentation packet from the referral and the RIS, submits through the payer API where one exists, through EDI 278 where supported, and otherwise prepares a complete packet for a human to submit. Tracks every open request against the seven-day and 72-hour clocks. On denial, drafts the appeal with the clinical rationale and queues it for a human signature. Reports the appeal rate and overturn rate weekly, which is the number the owner should watch. A human signs every submission and every appeal in phase one.

Why not a vendor: the category exists (Availity, Waystar, Cohere Health, Humata Health, Infinitus), but it is built for health systems and large groups, and much of it is payer-funded. A single-site center is an awkward customer for all of them. And the appeal gap is not a technology gap. Nobody has time to file. That is a workflow problem a narrow agent and a human sign-off fix.

If he raises Olive AI: "Yes. Olive raised an enormous amount of money, shut down in 2023, and sold its prior authorization assets to Waystar and Humata Health. It sold broad automation to hospital systems on long implementation cycles. That is close to the opposite of one person building a narrow agent for one site he can watch directly."

**BEAT**

Land the last sentence and let it sit for a beat before you move to Part two.

---

### SLIDE 11 · Part two: the three things you did ask about, corrected · 20:00

**SAY**

"Now the three things you did ask about. Scheduling. Answering patients. Requesting records. All three are real. Two of them are not what they look like."

**BEAT**

Eight minutes for slides 12 through 15. Keep moving.

---

### SLIDE 12 · Scheduling: the empty slot is not a no-show · 20:00 to 23:00

**SAY**

"A University of California, Irvine study of about nineteen thousand outpatient radiology exams found 22.3% were cancelled and 2.0% were no-shows. Seventy percent of the cancellations were patient-initiated. Most empty slots are known in advance. That is a backfill problem, not a reminder problem.

Nearly everyone pitching imaging automation pitches no-show reduction. That is the 2% number. The cancellation stream is ten times larger, and most of it arrives with lead time.

What I would build here is small. A waitlist that sees a cancelled slot and works a ranked list of patients who want to come in sooner. It sits on top of whatever RIS you choose."

**THEN SAY (the caveat)**

"That is one academic center over 2022 and early 2023. Your ratio will differ. The shape will not."

**DEPTH / IF ASKED**

Source: Aijaz A et al., "Sociodemographic Factors Associated with Outpatient Radiology No-shows Versus Cancellations," Acad Radiol, 2024 Aug;31(8):3406-3414, PMID 38705764. UC Irvine. 19,262 exams, 9,713 patients. 24.3% missed in total: 22.3% cancellations, 2.0% no-shows. 70.19% of cancellations patient-initiated. The same study found uninsured and publicly insured patients 1.3 to 4.9 points more likely to miss, and residence in a disadvantaged neighborhood added 4.9 points. Both matter in El Paso. Single tertiary academic center, so high confidence as a finding and medium as a benchmark.

Pocket figure: across 2,893,626 outpatient imaging visits over sixteen years, booking more than six months out carried an odds ratio of 3.18 for no-show versus booking within a week. Shortening time-to-appointment reduces no-shows on its own, and backfill is how you shorten it. (Rosenbaum JI et al., J Am Coll Radiol, 2018 Jul;15(7):944-950, PMID 29755001.) That institution's overall no-show rate was between 2.26% and 3.36%; mammography was highest at 6.99%, radiography lowest at 1.25%.

Do not quote general no-show benchmarks of 10 to 20%, "no-shows cost a practice a million a year," or "$200 per unfilled slot." All of those are vendor material with no methodology, and they contradict the peer-reviewed rates.

The one real risk in this build is TCPA: a backfill offer counts against the same three-per-week cap as reminders. That is the rate governor on slide 20.

Ask before you lean on this: "What was your cancellation rate, and what did you do with the empty slot?"

**BEAT**

Ask the cancellation question before the slide, if the flow allows. If his number is nowhere near 22%, say so and keep the shape argument, not the figure.

---

### SLIDE 13 · Scheduling: what reminders honestly do · 23:00 to 24:00

**SAY**

"A randomized trial at Massachusetts General, about seven thousand MRI patients, added a text reminder on top of the phone call they were already making. No-shows went from 5.1% to 3.8%. It did not improve arrival punctuality."

**THEN SAY (the caveat)**

"That is 1.3 percentage points absolute. Vendors will tell you that is a 25% reduction. Same study. And only about two thirds of the texting group could actually be reached by text.

Your RIS will do this. Let it."

**DEPTH / IF ASKED**

Source: Liu C et al., "Text Message Reminders Reduce Outpatient Radiology No-Shows But Do Not Improve Arrival Punctuality," J Am Coll Radiol, 2017 Aug;14(8):1049-1054, PMID 28583321. Massachusetts General Hospital. n = 6,989, randomized by day, p = 0.02, odds ratio 0.75 with a 95% confidence interval of 0.59 to 0.94. Only 67.5% of the texting arm was reachable by text. 2016 data, which is its main weakness.

It measures the incremental effect of texting on top of phone calls already being made, which is the real decision a center faces.

There is a NEJM Catalyst study reporting that adding an automated voice call to texts lowered no-shows a further 1.7 points (9.6% versus 11.3%). The article is paywalled and was not read; the figures came through a search summary. Do not lead with it.

Recommendation: buy, meaning the RIS. Self-scheduling, reminder sequences, and intake forms are bundled into modern cloud imaging RIS products.

If he says "doesn't our RIS already do this?": "For scheduling, reminders, self-scheduling, and intake forms: yes, and it should. I am telling you to buy that and use it. RamSoft's imaging-center product, for one, advertises self-scheduling, automated notifications, and a workflow designer. What I have not seen any RIS in this tier claim is eligibility verification or prior authorization. That gap is where the strongest evidence is, and it is the piece you did not ask about." Hold that line exactly: you have not seen it advertised. Do not claim the RIS definitely lacks a prior auth module. The specification verifies it against whichever RIS they pick.

**BEAT**

Quote the absolute numbers and let him do the arithmetic. An exited founder will smell the relative-risk trick, so be the one who names it.

---

### SLIDE 14 · Answering patients: buy it, do not build it · 24:00 to 26:00

Ask before the slide: "Who takes the phone call when a patient describes chest pain?" His answer makes the recommendation obvious before you state it.

**SAY**

"Phones are a real cost. You are right about that. My recommendation is to buy a healthcare voice vendor, not to have me build one. I will write the specification, run the evaluation, integrate it, and supervise it. And I will tell you when it is not good enough in Spanish.

Here is why. 26.5% of El Paso County residents over five speak English less than very well, and 97.8% of them speak Spanish. One in four of your patients cannot be served by an English-first system.

A voice agent that mishandles a patient describing chest pain, or garbles Spanish, is a clinical safety event and a reputational event. It is not a bug. Voice is the highest blast-radius failure on this whole list, and it is a funded category I cannot beat on cost.

I would rather tell you to buy something than build something that is not mine to build."

**DEPTH / IF ASKED**

Source: American Community Survey 2024 five-year, Table B16004, El Paso County. Population five and over of 813,194. 215,186 speak English less than "very well," which is 26.5%. 537,316 speak Spanish at home, which is 66.1%. Computed from raw ACS counts via Census Reporter, because census.gov blocked automated access. Say 26.5%, not 66%: the operational number is the limited-English number, and knowing the difference shows you understand a requirement versus a demographic.

Vendor category names if asked: Hyro, Assort Health, Infinitus, Parlance, Syllable. None of them publish pricing. Do not quote any.

TCPA: an AI voice is an "artificial voice" under the FCC's February 2024 ruling (FCC 24-17), and that ruling expressly preserved the healthcare exemption. Inbound calls the patient initiates are outside the outbound autodialer and artificial-voice restrictions. Any outbound callback from the voice system falls back under them. Texas HB 149, effective 2026-01-01, extends an AI disclosure obligation to healthcare providers; scope not fully verified, so plan a disclosure at the start of the call.

The honest alternative: do not do voice at all in phase one. Let the front desk answer the phone while the prior auth agent takes that load off them.

What integration needs: a RIS scheduling API for the vendor to book against (a contract term from slide 3), a vendor BAA, an escalation path to a human on any symptom language, and a Spanish evaluation set built with Luis.

**BEAT**

Say the buy line plainly. Recommending a purchase here makes everything you do propose to build more believable.

---

### SLIDE 15 · Records: the clock and the fee rule both favor automation · 26:00 to 28:00

**SAY**

"Records requests. Two rules work in your favor here, and one problem works against you.

The first rule. The 30-day HIPAA clock runs from the day the request is received, not from the day it reaches the right desk. One extension of up to 30 more days, with written notice inside the first 30. Outer limit, 60 days. A request sitting in a pile is already burning the clock.

The second rule. The fee you can charge covers the labor to copy, supplies, postage, and a summary if the patient agreed to one. Search and retrieval labor is explicitly not chargeable. Finding the study is the expensive half of the work, and you cannot bill for it.

The problem. The harder side is outbound. A new center opens with zero priors on file. Every comparison study comes from somewhere else. RSNA is on record this year that DICOM exchange is still not a TEFCA requirement. Patients still carry their own discs. Nobody has solved that for a small center, and I am not going to tell you I have. The part I can build is the tracker: which facility accepts which kind of request, generate it, track it, and import what comes back."

**THEN SAY (the caveat)**

"Texas has its own records deadline that is shorter than the federal 30 days. I am not going to quote the day-count from memory. It goes in the specification after I verify it against the statute."

**DEPTH / IF ASKED**

The clock and the fee components: 45 CFR 164.524. The dividing line for billable labor, from the 2016 HHS guidance as quoted in Ciox: copying labor begins only once the responsive PHI "has been identified, retrieved or collected, compiled and/or collated, and is ready to be copied."

Ciox Health v. Azar, 435 F. Supp. 3d 30 (D.D.C. 2020), vacated the third-party-directive expansion but did not vacate the $6.50 flat-fee option. The court held the listing of fee methods was not reviewable agency action and never reached the merits. The option remains.

OCR's Right of Access Initiative has produced more than 50 enforcement actions. "More than 50" is supportable. Do not quote a settlement figure.

RSNA comment letter to ASTP/ONC, March 2026: names the prior-study retrieval gap directly, says patients still act as couriers for their own imaging, flags it for small community centers, and asks that DICOM exchange become a TEFCA requirement.

Recommendation: build, selectively. Inbound intake, deadline tracking, fee calculation, and status reporting are a small custom build with clear regulatory specifications and hard deadlines. Deadline tracking is the first feature, not the last, because the failure mode is a missed statutory deadline and an OCR complaint. Patient identity verification before release stays a human step in phase one. The retrieval itself is a DICOM query against the PACS, which is why the DICOM permission on slide 3 matters.

The local facility directory gets built by hand in the first months: the hospital systems and the independent groups. Do not name Southwest X-Ray or Akumin when you talk about where priors will come from.

Do not quote a cost per records request. The circulating "$50 to $200 per request" is a vendor figure and unverified.

**BEAT**

Do not say "from running two centers" or "two companies." He built one company with five centers. Let the fee rule land; it is the one most owners have never heard stated.

---

### SLIDE 16 · The fifth candidate: the numbers the owner actually looks at · 28:00 to 29:00

Cut this slide first if you are running long at 28:00.

Ask before or on the slide: "What do you want to see on one page every Monday morning?" Whatever he says is the specification.

**SAY**

"The fifth one is the numbers the owner actually looks at. Studies by modality, by reader, by referrer. Turnaround. Scheduled versus completed. Revenue per slot.

All of it already lives in the RIS and the billing system. The problem is that those are two systems, and RIS reporting is built for radiology operations, not for an owner.

I have no study to show you here. I have the fact that you will want a referrer-and-revenue view, and the RIS will not give it to you. It is the smallest compliance footprint of the five, and the cheapest to build. Luis's question, am I being paid correctly for what I read, is the same engine with a different view."

**DEPTH / IF ASKED**

There is no external evidence for this candidate, and the research says so plainly. No benchmark literature exists on what imaging center owners want from dashboards. Say "I have no study" rather than reaching for one.

The structural claim holds without a study: the owner's view requires joining RIS data to billing data, and those are usually different systems. Both exports are contract terms from slide 3.

Custom by nature, because it encodes one owner's definition of what matters. The reader-reconciliation view already has a customer in Luis. FDA: "business analytics" and "practice and inventory management" are named in the statute at slide 19. PHI is present, so the BAA and Texas residency still apply, but there is no patient-facing surface.

**BEAT**

Write down his Monday-morning answer. That sentence is worth more than the slide.

---

### SLIDE 17 · The scorecard · 29:00 to 30:00

**SAY, in one breath**

"Prior authorization and eligibility: build. Strongest evidence, no vendor fits a single site, and the federal APIs arrive January first.

Reminders and self-scheduling: buy. That is the RIS.

Cancellation backfill: build, small, on top of the RIS. That addresses the 22%, not the 2%.

Voice: buy. I integrate.

Records: build, selectively.

Owner reporting: build.

Two of the things you asked about, I am telling you to buy."

**DEPTH / IF ASKED**

Nothing new. Every line on this slide was defended on its own slide.

**BEAT**

Read it in one breath. The last line is the point of the slide.

---

### SLIDE 18 · Proof: RadAssist · 30:00 to 37:00

**SAY**

"Enough slides. This is RadAssist. Browser-based structured radiology reporting, with calcium score and thyroid modules. I built it. Luis uses it every day on real patients.

Luis, do not let me demo it. Tell him about a Tuesday. What broke, and how fast did it get fixed? What did you ask for that got built? What does it do that the vendor tools did not?"

Then stop talking.

**DEPTH / IF ASKED**

The only proof that matters is the artifact that already works, and the only witness who matters is the one using it. Seven minutes belong to Luis.

If Luis mentions something that broke, let him. The speed of the fix is the proof, not the absence of failures.

If Fernando connects this to the FDA slide coming up: the same discipline that keeps the agents administrative is what keeps RadAssist on the right side of the line. Keep that to one sentence.

Connectivity: the deck runs offline, RadAssist does not. Hotspot confirmed or screenshots ready, per the checklist.

**BEAT**

Open the live app. Hand the table to Luis. Do not demo features. Do not fill his pauses.

---

### SLIDE 19 · Boundaries: the FDA question, answered by the statute · 37:00 to 38:00

**SAY**

"The FDA question, answered by the statute and not by me. Federal law says software for administrative support of a health care facility is not a medical device, and it lists what that means by name. Claims or billing information. Appointment schedules. Business analytics. Determination of health benefit eligibility.

Every candidate on that scorecard is on the list by name.

And the agents stop at the clinical boundary. Nothing interprets an image, selects a protocol, or recommends a study."

**DEPTH / IF ASKED**

Source: 21 U.S.C. 360j(o)(1)(A), read verbatim at Cornell Legal Information Institute. The full list also includes financial records, information about patient populations, admissions, practice and inventory management, and laboratory workflow. Section 360j(o)(2) adds that FDA "shall not regulate" excluded administrative functions even when they coexist with device functions in one product.

Lead with the list, not with any engineering rule about orchestration. The list contains the words "appointment schedules" and "determination of health benefit eligibility." That is a complete answer and it invites no debate about how independently a clinician reviews anything.

The one real boundary: the moment an agent touches image data interpretively, or recommends which study to order, it leaves this exclusion and enters device territory under the clinical decision support criteria at 360j(o)(1)(E), whose guidance was revised 2026-01-06 and 2026-01-29. Protocol selection and clinical appropriateness are the live hazards in imaging. Say explicitly that the agents stop there.

Texas SB 1188 separately requires disclosure when AI is used for diagnostic purposes. None of these five are diagnostic. Another reason to keep the line clean.

If "won't regulators come for this" comes up: "The state that has legislated hardest on AI patient communication, California, expressly excludes appointment scheduling and billing from its disclosure law." (AB 3030, subsection (c)(7).)

**BEAT**

One minute. The list is the answer. Do not argue it.

---

### SLIDE 20 · Boundaries: what I will design around, stated before you ask · 38:00 to 39:00

**SAY**

"Four constraints I am going to design around, stated before you ask.

Texas SB 1188. Electronic health records with Texas patient data have to be physically stored in the United States as of January first this year. Every component, including the model provider, gets verified for US residency before anything is promised.

TCPA. The healthcare exemption allows one message per day and three per week per patient. No billing content. Provider name and opt-out in every message. Five hundred dollars per violation, up to fifteen hundred if willful. A reminder plus a backfill offer plus a results notice can collide with the three-per-week cap. The system needs a per-patient rate governor, not just a send queue. I have built that.

The AI vendor's business associate agreement. Anthropic's agreement now covers Skills, Web Search, Memory, and the Bash and Text Editor tools. It still excludes Computer Use and Web Fetch, which are exactly what you would reach for to drive a payer portal that has no API. So the prior auth design routes through APIs, EDI, or a human step. Not screen-driving.

Texas HB 300. Its definition of a covered entity is broad enough to reach me directly, not only through your BAA. I carry that obligation in my own right."

**THEN SAY (the caveat, on the BAA)**

"The coverage depends on which version of the agreement is signed and when. I will confirm the exact envelope in writing before anything with patient data is built."

**DEPTH / IF ASKED**

SB 1188, 89th Legislature, signed 2025-06-20, effective 2025-09-01, with the storage requirement effective 2026-01-01 and applying to all records stored on or after that date. Passage and dates verified at capitol.texas.gov. The provision wording comes from six or more converging law-firm analyses, not the enrolled text, so if pressed on exact wording say "as I read it."

TCPA: 47 CFR 64.1200(a)(9)(iv), the wireless healthcare exemption, all eight conditions: sent only to the number the patient provided; provider name and contact at the start; content limited to appointment confirmations and reminders, pre-registration instructions, lab results, and the other enumerated categories; no telemarketing and no accounting, billing, debt-collection, or other financial content; one minute or less for voice and 160 characters or less for text; one per day and three per week per patient, voice and text combined; opt-out in every message; opt-outs honored immediately. Damages under 47 U.S.C. 227: $500 per violation, trebled to up to $1,500 if willful or knowing. $1,500 is the ceiling, not a fixed amount. Balance-due and payment reminders cannot ride this exemption at all; they need their own consent basis, which is why they are declined for phase one.

BAA: Anthropic's BAA documentation at privacy.claude.com, accessed 2026-10-01. Also excluded: Files API, Skills API, Code Execution, Batch API, and third-party data flows through external MCP connectors. Enterprise coverage applies to agreements accepted after 2025-12-02; Messages API feature coverage after 2026-04-01. If he asks "can your AI vendor even handle patient data": "It covers the parts of the architecture I would use. It does not cover Computer Use or Web Fetch, so I will not promise screen-driving a portal with patient data, because I cannot do it inside the agreement today."

HB 300 is Texas Health and Safety Code Chapter 181. Do not quote a day-count or a training interval from it. Both get verified against the statute in the specification.

**BEAT**

Each constraint in a sentence or two, then move. Volunteering them is what separates you from twenty years of vendors.

---

### SLIDE 21 · The question you are going to ask · 39:00 to 40:00

Never cut this slide.

**SAY**

"The question you are going to ask is what happens when I get hit by a bus. Here is the answer, in order.

You own the specification. It is written for a competent engineer who has never met me, and it is the deliverable of the design engagement whether or not I build anything.

You own the code. It lives in a repository under your organization's account. You can revoke my access.

Runbooks, not memory. Every operational procedure is written down: how it runs, how it fails, who to call at each vendor.

No proprietary runtime. Standard interfaces, HL7 version 2, DICOM, payer APIs, and a named model vendor under its own business associate agreement. Any integrator can take it over.

Buy where buying is right. The RIS and the voice vendor are contracted in your name. Nothing routes through me that does not have to.

The design engagement exists so that this question has a boring answer. If I disappear in month four, you have a specification you can hand to anyone. If I disappear in year two, you have the code, the runbooks, and the vendor relationships in your name."

**DEPTH / IF ASKED**

Escrow: "Direct ownership is better than escrow. There is nothing to escrow if the repository is already yours."

A second person: "There is no second person. That is the honest answer, and it is why the engagement is structured so that the specification and the runbooks are the continuity plan, not me."

Why this slide may matter more than any number: his bar for AI may be low. His bar for vendors is high, and he has been left holding systems by vendors before. Compensate with verifiable structure, not warmth. The ninety-day gate on slide 23 is what makes this promise financial rather than reassuring: he can stop.

Ask here, and write the answer down: "We are two people. If you were in my chair pitching you, what would you want to see about continuity and about getting out, before you would put us anywhere near your schedule?" Whatever he names is your path to a yes.

**BEAT**

Five points, in order, no skipping. Then the "boring answer" line. Then the question. Then listen.

---

### SLIDE 22 · The most important slide · inside the close

Never cut this slide.

**SAY**

Say the first line slowly.

"What I recommend you do not buy from me.

A custom voice agent. Buy a vendor. I will specify, evaluate, and integrate it, and I will tell you when it is not good enough in Spanish.

Reminders, self-scheduling, and intake forms. Your RIS does this. Make sure the contract says so, then use it.

A product for other centers. I am not building something to sell to other centers. I am building for this one, and I will be the person who operates it.

Anything that touches the image clinically. Not from me, not from anyone, without an FDA pathway."

**DEPTH / IF ASKED**

The third bullet is printed on the slide as "A platform." The word is on the never-say strip. The spoken line above says "a product for other centers" instead, so you never say the word out loud even in the negative. He has heard "and then we expand it" from everyone who ever pitched him, and he knows it means the person is about to become unavailable to his center.

If he asks "is this going to be a product you sell to other centers": "No. I am building for this center and I will be the person who operates it. If it generalizes later, that is a conversation for when there is evidence. You know what that other sentence means for your service level, so I am not going to say it."

If he says "our last vendor promised the moon": "I know. That is why this slide exists. I am telling you to buy two of the things you asked about from someone else. The things I am proposing to build are the ones where the evidence is strongest and no vendor fits a single site."

**BEAT**

Recommending against yourself is the single most credible thing you can do in front of someone who has sat through twenty years of vendor decks. Slow down.

---

### SLIDE 23 · What I am proposing · inside the close

Never cut this slide. This is the single most rehearsed line in the deck.

**SAY, exactly this, once**

"Thirty thousand for the six months, in two phases. Twelve for the first ninety days: the contract language, the RIS and billing evaluation, the voice vendor shortlist. That is all the work that has to happen before you sign anything. Eighteen for the back half: the written specifications for prior auth, records, backfill, and reporting. At ninety days you decide whether the second phase goes. Build gets priced from the spec after you open."

Then stop talking.

**DEPTH / IF ASKED**

Do not break out hours. Do not name an hourly rate. Do not justify the number at length. Explaining a price invites negotiation on the explanation. Never, under any circumstances, mention what the total works out to per hour.

If he pushes on price: shorten the term, never cut the rate. "That is exactly what the ninety-day gate is for. Take Phase 1 and decide the back half when you have seen the work." You never discount, and your rate stays intact for the build conversation.

Why two phases: the decision in the room is twelve thousand, not thirty. Phase 1 is also the half with the real deadline, because it has to land before vendor signatures. If it slips, the advantage is gone. And the gate makes the continuity promise on slide 21 financial: he can stop.

Contract through RGF Global Ventures LLC, never personally. A greenfield center has no insurance history and no compliance program yet.

Do not discount because Luis is a friend. Luis's RadAssist license and retainer are separate and stay where they are. Fernando is a stranger who has closed more deals than you have.

If asked about the build: "Scoped and priced from the specification, after you open, with real volumes and real payer mix. I am not going to quote a build tonight because I would be guessing, and you would know."

If pressed for a build range: "I would rather give you the specification and a fixed price for each piece than a range tonight that we both have to pretend was meaningful."

Never give a date for the build. The build is decided after opening.

**BEAT**

Say it once. Stop. Let the silence sit. Whoever speaks next is not you.

---

### SLIDE 24 · If it were my money · inside the close

Cut this slide second if you are running long. Keep the closing question even if you cut the slide.

**SAY**

"If it were my money, I would do three things before signing another vendor contract.

Put the four access terms into every contract this month. It is free.

Decide now whether the prior authorization desk is a hire or a system. That decision expires the day you hire for it.

And tell me what front desk and prior authorization actually cost you last time, as a share of operating expense. Your number beats any benchmark I could bring.

One question for you. What would you do differently this time, knowing how the last one ended up?"

Then stop and listen.

**DEPTH / IF ASKED**

The third bullet is the most valuable question of the night. There is no defensible published benchmark for administrative labor as a share of imaging center operating cost. Everything circulating comes from content farms and financial-model templates. His P&L is the only number that matters, so ask for it and write it down.

Do not ask whether Southwest X-Ray was his. That is confirmed, and asking a question he has already answered reads as not listening.

The closing question is open on purpose. He is opening in direct competition with a company that owns what he built, and the buyer had financial trouble afterward. If his answer goes anywhere near the sale, the buyer, or how his time there ended: stop talking, listen, say little, ask nothing, move on. His answer tells you what he actually wants from this center, and it is probably control.

**BEAT**

Ask the closing question and then do not fill the silence. A man with his history has a long answer to it. Let him give it.

---

### SLIDE 25 · Thank you · the end

**SAY**

"Every one of these decisions is reversible today. None of them will be in six months.

Thank you both. Here is one page you can keep."

**DEPTH / IF ASKED**

Contact on the slide: Richard Finlay, RGF Global Ventures LLC, (480) 532-1367, rfinlay813@gmail.com.

**BEAT**

Put the leave-behind on the table, one per person. Then stop selling and have dinner.

---

# PART 3: REHEARSAL DRILLS

## Drill 1: the five headline numbers

Cover the right column. Say the number, then say its caveat, from memory. Then check.

| Slide | The number | The caveat you must say unprompted |
|---|---|---|
| 4 | 4.1 million denied. 11.5% appealed. 80.7% of appeals overturned. Four in five win, almost nobody files. | Medicare Advantage, all services. Not an imaging number, because CMS does not collect prior auth data by type of service. The only audited, payer-reported, national figure that exists. |
| 5 and 7 | 13 hours a week. About 40 requests per physician per week. 40% have staff working exclusively on it. You have not hired that person yet. | AMA 2025 survey, a thousand physicians. Self-reported. |
| 8 | At least 220 million hours and 16 billion dollars over ten years. Based on AMA data showing 14 hours per week. | CMS's projection in the rule. Not measured savings. Nobody has gone back and counted. |
| 13 | Mass General, about seven thousand MRI patients, text on top of a phone call. 5.1% to 3.8%. No change in punctuality. | 1.3 points absolute. Vendors say 25%. Same study. Only two thirds of the texting group reachable by text. Your RIS will do this. Let it. |
| 12 | UC Irvine, about nineteen thousand exams. 22.3% cancelled, 2.0% no-show. Seventy percent of cancellations patient-initiated. Backfill, not reminders. | One academic center, 2022 and early 2023. Your ratio will differ. The shape will not. |

Second pass: the sources, one line each, from memory.

| Slide | Source |
|---|---|
| 4 | KFF, 2026-01-28, from data insurers report to CMS |
| 5 and 7 | AMA 2025 Prior Authorization Physician Survey |
| 8 | CMS-0057-F, 89 FR 8758, Regulatory Impact Analysis |
| 13 | Liu et al., J Am Coll Radiol 2017, PMID 28583321 |
| 12 | Aijaz et al., Acad Radiol 2024, PMID 38705764 |

## Drill 2: the price answer

The single most rehearsed line in the deck. Say it out loud ten times. Then say it once more and stop talking for a full ten seconds afterward. The stopping is the part you are practicing.

"Thirty thousand for the six months, in two phases. Twelve for the first ninety days: the contract language, the RIS and billing evaluation, the voice vendor shortlist. That is all the work that has to happen before you sign anything. Eighteen for the back half: the written specifications for prior auth, records, backfill, and reporting. At ninety days you decide whether the second phase goes. Build gets priced from the spec after you open."

If pushed: "That is exactly what the ninety-day gate is for. Take Phase 1 and decide the back half when you have seen the work."

No hours. No rate. No justification. Shorten the term, never cut the rate.

## Drill 3: the bus answer, five points in order

1. You own the specification. Written for a competent engineer who has never met me. The deliverable whether or not I build anything.
2. You own the code. Repository under your organization's account. You can revoke my access.
3. Runbooks, not memory. How it runs, how it fails, who to call at each vendor.
4. No proprietary runtime. HL7 version 2, DICOM, payer APIs, a named model vendor under its own BAA. Any integrator can take it over.
5. Buy where buying is right. The RIS and the voice vendor are in your name. Nothing routes through me that does not have to.

Closer: "The design engagement exists so that this question has a boring answer."

Escrow: direct ownership beats escrow. Second person: there is no second person, and that is why the spec and the runbooks are the continuity plan.

## Drill 4: the questions you ask them, in the order you would ask them

Write every answer down at the table.

1. **At the open, before anything about his history:** "Luis told me you built and sold imaging here in El Paso before this, but I would rather hear it from you than secondhand. What did you build, and how many centers were you running at the end?"
2. **Slide 2, before the four contract terms:** "Which RIS and billing vendors are you looking at, and have you signed anything yet?"
3. **Slide 5, the 40% statistic:** "How many prior authorizations a day were you running at steady state, and who did them?"
4. **Slide 9, the federal dates:** "What is your payer mix going to look like?"
5. **Slide 12, before you lean on 22.3%:** "What was your cancellation rate, and what did you do with the empty slot?"
6. **Slide 14, before the voice recommendation:** "Who takes the phone call when a patient describes chest pain?"
7. **Slide 16, owner reporting:** "What do you want to see on one page every Monday morning?"
8. **Slide 19 or 20, the boundaries:** "You came up as an RPA, so you have been in the room with the patient. When you think about automating the front end, where is the line for you? What has to stay human?"
9. **Slide 21, the bus question:** "We are two people. If you were in my chair pitching you, what would you want to see about continuity and about getting out, before you would put us anywhere near your schedule?"
10. **Slide 24, the close:** "What did front desk and prior authorization actually cost you last time, as a share of operating expense?" Then: "What would you do differently this time, knowing how the last one ended up?"

The runbook numbers these 1 through 8 with two items each numbered 5 and 6. There are ten questions. Ask all ten.

## Drill 5: the 60-second version

If dinner collapses to one minute, this is what survives. Say it as one paragraph.

"Here is what I would tell you if I had one minute. You are in the only window where automation is a design choice and not a retrofit. Before you sign any vendor, put four terms in the contract: API access to your own data, HL7 interface fees fixed at signature, export rights at no charge, and DICOM query permissions. That is free today and hostage terms later. The biggest cost you have not planned for is prior authorization. In Medicare Advantage, four in five appeals win and almost nobody files one, because nobody has time. I would build that, and I would tell you to buy your reminders from the RIS and your phone system from a voice vendor, not from me. You own the spec, you own the code, and if I get hit by a bus you hand both to anyone. Thirty thousand for six months, in two phases, twelve then eighteen, with a gate at ninety days that you control."

## Drill 6: the 5-minute version

Cut slides 16 and 24 first. Never cut 21, 22, or 23. In five minutes you keep:

| Minute | Slides | What you say |
|---|---|---|
| 0:00 to 0:45 | 1, 3 | Framing line. The four contract terms, fast. "Whatever you decide about me, do this." |
| 0:45 to 1:45 | 4, 5 | Four in five, stop. Caveat. Forty percent, you have not hired that person yet. Caveat. |
| 1:45 to 2:30 | 6, 17 | "The thing you did not ask about." Then the scorecard in one breath: two of the things you asked about, I am telling you to buy. |
| 2:30 to 3:15 | 18 | RadAssist is open. "Luis, one Tuesday." Forty-five seconds of Luis. |
| 3:15 to 4:00 | 21 | The five bus points, in order. "A boring answer." |
| 4:00 to 4:30 | 22 | What I recommend you do not buy from me. Slowly. |
| 4:30 to 5:00 | 23 | The price, once. Stop. |

What is lost in the 5-minute version: every caveat except the two on slides 4 and 5, the federal dates, the records rules, the boundaries slides. If he asks about any of them, you have the full answer above.

---

# PART 4: PRE-DINNER CHECKLIST

## Today or tomorrow (2026-10-06 or 10-07)

- [ ] Send the confirmation text to Luis. The approved wording is Step 0 of the RUNBOOK. Paste it as-is. It asks for studies per day and modalities, front-end headcount, and the partner's name.

## Before you leave the house

- [x] **~~Replace `[PARTNER NAME]`~~ DONE 2026-10-06.** Fernando Escarzaga. Full name on the two client-facing surfaces (deck title slide, leave-behind title tag + header); first name only in the six deck presenter notes, the RUNBOOK, and AUTOMATION-CANDIDATES, where it reads naturally. Zero placeholders remain in any file. Deck and leave-behind PDFs reprinted from the corrected HTML and re-synced to OneDrive and Google Drive.
- [ ] **The fee is decided: $30,000, two phases, $12,000 then $18,000, gate at 90 days.** On slide 23 and on the leave-behind in writing. Say it once and stop.
- [ ] **Print the leave-behind.** Two copies. Verified to print on one US Letter page from Chrome.
- [ ] **Charge the laptop.** The deck runs with no wifi. RadAssist does not. Confirm radassist.app loads on your phone's hotspot before you sit down, or have screenshots ready.
- [ ] **Open the deck in a browser.** Press N once to confirm notes mode works, press N again to hide it. Set the browser to full screen.
- [ ] **Do not bring the Sherlock research document.** Everything you need from it is in this sheet, the deck notes, and the RUNBOOK.
- [ ] **Bring this sheet, folded.** Part 1 face up.

## Open items to decide before the dinner (found while building this sheet, not fixed)

- Slide 22 prints the word "platform" as its third bullet heading. The never-say strip says never say "platform." The spoken line in this sheet avoids the word. Decide whether to change the slide text or leave it on screen and simply not say it.
- The deck's clock gives slide 21 the last minute (39:00 to 40:00) and assigns no time to slides 22 through 25. The RUNBOOK's table puts slides 19 to 25 in 37:00 to 40:00, which is seven slides in three minutes. Slides 22 and 23 are never-cut slides and each needs a real minute. Plan on the close running to about 43 minutes, or trim a minute from slides 9 and 12.
- Slide 15's presenter note still says Fernando "will recognize this from running two centers." He ran one company with five centers. The spoken line in this sheet does not say it.
- Two of the RUNBOOK's objection answers quote the words "scale" and "platform" inside the negation ("I am not going to tell you 'and then we scale it'"). The versions in this sheet avoid both words.
