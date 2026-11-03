# Demo scripts for the partner lunch

**Part A is NOT USED THURSDAY (overview only, per Luis; Rick, 2026-11-03).** Slide 19 is a one-minute spoken overview of RadAssist, and the table then goes to Luis; the walkthrough below is kept for reference and for any later working-day showing. **Part B**, the prior authorization agent (slide 11, the thing to be built), is unchanged and runs from a tab opened Thursday morning; it needs no login.

---

# Part A. RadAssist Spine MRI, live (about 3 minutes, slide 19). NOT USED THURSDAY: overview only, per Luis.

> Kept as written. Nothing below is set up or rehearsed for the 11-05 lunch. If Luis himself asks you to open it, this is the walkthrough; otherwise the spoken overview under slide 19 in the SPEAKING NOTES is the whole of slide 19.

**Live URL:** https://radassist.app/spine (sign in Thursday morning, before lunch; the session needs your password and your authenticator code).
**Works on:** the laptop. Keep the tab open from the moment you sign in; do not reload it at the table.
**What it is:** the production tool Luis uses every day. Everything you type at the table is synthetic. Nothing is sent to a server; the report is assembled in the browser and copied as plain text.
**Backups if the network fails:** `demo-assets/` in the pitch folder has eight screenshots of this exact case and a 27-second recording (`spine-demo-recording.mp4`), captured 2026-11-01 from the same build that is live.

## Before you switch tabs (10 seconds)

Slide 19 is up. Say the proof point once, then move to the tab:

> "Spine went live this week. Luis sent me his template and his rules. Every rule in it is his. Let me show you one case."

If the slide prompts it, one sentence on CT: "CT Spine followed two days later, live since Sunday, from his sample reports. Same tool, switched to CT." Then demo the MRI case only; do not switch modalities at the table.

## 1. Pick the study (15 seconds)

The page opens on **Spine MRI**. Region is already **Lumbosacral**, contrast **Without contrast**. If a previous draft is offered, click **New study**.

Set **Indications** to *Other / free text* and type: `Low back pain with right leg radiculopathy`.

> "One dropdown per sentence. The sentences are Luis's own template, not mine."

## 2. The severe level (45 seconds)

Scroll to **L4-L5**, click **Edit**, and enter the card values:

| Field | Value |
|---|---|
| Canal stenosis | Severe |
| Foraminal stenosis | Severe, Bilateral |
| Pfirrmann grade | IV |
| Bulge / protrusion / extrusion | Extrusion, 7 mm, Central |
| Nerve roots | Compression |
| Ligamentum flavum | Hypertrophy, 5 mm |
| AP diameter of the thecal sac (cm) | 0.5 |

Point at the note under the AP box: **"5 mm → suggests Severe canal stenosis, matches your canal grade."**

> "That flag suggests; it never decides. If Luis grades it differently, his grade prints and the flag just says it disagrees."

## 3. Two more levels, fast (40 seconds)

**L3-L4**, click **Edit**: Canal *Moderate*; Foraminal *Mild to moderate*, *Left*; Pfirrmann *IV*; *Protrusion*, 4 mm, *Central*; Nerve roots *Contact*; AP *0.7*.

**L5-S1**, click **Edit**: Foraminal *Moderate*, *Right*; Pfirrmann *III*; *Bulge*, 3 mm; Nerve roots *Contact*, *Foraminal*; AP *1.1*.

Then the summaries near the top of the form: **Conus** *L1*; **Discs** *Moderate to severe*; **Bones**: osteophytes *Moderate*, Modic *Type II*, levels `L4-L5`.

No narration beyond "same thing, two more levels." Let the preview on the right fill in while you type.

## 4. The impression writes itself, in Luis's order (30 seconds)

Scroll to **Impression**. Read the first lines aloud:

> "Line 1 is always the fracture sentence, because that is how Luis opens every report. Then the discopathy line names every level that matters. Then the stenosis, worst first: severe canal, moderate canal, severe foraminal, moderate foraminal. He set that order on October 31, and the software has followed it since that evening."

Then point at the **last line**:

> "**Segmental analysis incomplete: 2 disc levels not yet reviewed.** L1-L2 and L2-L3 are still blank. Look at the preview: they print as blank lines, not as normal. An unreviewed level never prints normal. That is the safety rule, and it was Luis's."

## 5. Finish the review (20 seconds)

Click **Mark the remaining 2 levels reviewed (normal)**, confirm, then open **L1-L2** and **L2-L3** and type `1.2` in each AP box. The red notice clears, the box reads **"Every level is reviewed,"** and the impression's last line disappears.

## 6. Copy, paste, done (30 seconds)

Click **Copy report**. Switch to the plain-text window you opened before lunch (TextEdit in plain-text mode, or Notes) and paste.

> "That is the whole report, plain text, in his words. It goes into whatever system the center buys. No integration needed on day one, nothing to install, nothing stored on a server."

Close the demo, back to the deck:

> "He drafts in it, he signs. It does not read an image, and it will not until there is a regulatory path for that."

**Optional close, only if you have cleared it with Luis:** his own line from the Friday call, that after he tweaks it, "it becomes sellable the next day." If you have not cleared it, let Luis say it himself or leave it out.

## Questions you will get, Part A

- **"Did you build all of that in a day?"** The spine module, yes, from his template; it was tested end to end against the two sample reports he sent, and reviewed by an independent code reviewer before release. The calcium and thyroid modules came first, over the summer.
- **"Where does the data go?"** Nowhere. The browser assembles the report; only a temporary draft lives on that computer for four hours. No patient data is stored on a server. Sign-ins are recorded.
- **"Is it FDA cleared?"** It is not a device and does not diagnose; it formats what the radiologist graded, from his own template, and he signs. Reading the images would be a different product with a regulatory path.
- **"Can it read the MRI for him?"** Not today, and not promised. That is diagnostic software. It is a future item with a regulatory path.
- **"What about Spanish?"** Click **Español** above the preview: the same report, drafted in Spanish, flagged as pending his review.
- **"Can other radiologists use it?"** Yes; the templates are per radiologist. Keep selling it to other centers out of this room (private conversation with Luis), and say nothing about terms.

## If the Wi-Fi dies, Part A

The tab you signed into Thursday morning keeps working without a network: the report is assembled in the browser. Do not reload. If the tab is gone, open `demo-assets/` and walk the screenshots in number order, or play `spine-demo-recording.mp4` (27 seconds): "The network is not cooperating, so here is the same case recorded this week from the live site."

---

# Part B. Prior Authorization Agent (about 3 minutes, slide 11)

**Live URL:** https://rfinlay.github.io/imaging-priorauth-demo/
**Works on:** laptop, iPad, phone. No login. Open it Thursday morning and leave the tab up.
**Source and the real-vs-simulated table:** https://github.com/rfinlay/imaging-priorauth-demo#readme

Before you start, glance at the top banner. It should read **"Payer sandbox: LIVE (HL7 Da Vinci PAS)"** in green.
If it is orange ("sandbox offline"), the demo still runs end to end; the submission just goes to the simulated payer and says so. Either way, say the line in step 4 that matches.

## Framing (10 seconds)

> "This is a working prototype, not slides. Everything you see is synthetic data, but the submission in the middle goes to a real payer test server that implements the national prior-auth standard. I want you to click it, not watch me."

Hand the laptop or phone to Fernando if he wants it.

## 1. Order arrives (20 seconds)

Click **Maria Delgado, MRI lumbar spine**. The HL7 message appears below.

> "This is literally what the RIS sends when a doctor orders a study. Nobody reads this today; a person re-types it into a payer portal. The agent reads it."

Click **Next: does this need prior auth?**

## 2. Is prior auth required? (15 seconds)

> "It knows the payer and the CPT code, so it knows the answer in under a second. For traditional Medicare it would say no and release the order to scheduling."

Click **Next: assemble the packet.**

## 3. Assemble packet (25 seconds)

Point at the checklist on the right.

> "This is the part that eats your staff's day: chasing the referral, the notes, proof of six weeks of therapy. The agent pulls it together and flags what is missing before anyone calls the payer."

Point at the purple **Human approves** box.

> "Nothing leaves the building without a person approving it. Your coordinator stays in charge; she just stops doing the typing."

Click **Approve packet and submit.**

## 4. Submit to payer (30 seconds)

Watch the log fill in. Wait for the line **"Payer sandbox accepted the request (HTTP 201). Tracking number …"**

> "That just went over the wire to HL7's prior-authorization test server, in the FHIR format CMS is requiring every Medicare Advantage and exchange plan to support by January 2027. That tracking number is real; the link opens the stored record on their server."

If Jesse wants proof, click **Show the FHIR request we sent** or the **Open the stored response** link. If the banner was orange, say instead: "Today the public test server is down, so this one went to our simulated payer, which is why it is labeled that way. The code path is the same."

Be straight about the boundary, because Fernando will ask: "The test server accepts and stores the request but has no medical-necessity rules for imaging, so the approve or deny you are about to see is simulated. Real payer decisions come when a real payer connects, which is the point of the 2027 rule."

Click **Next: track the clock.**

## 5. Track the clock (30 seconds)

> "Standard requests get a 7-day clock, expedited get 72 hours. Those are the CMS deadlines payers have to meet starting this year. The agent watches every one and escalates at 75 percent."

Click **Advance 3 days** at the top. Maria flips to **Approved** with an auth number.

> "Approved in two days. The order goes straight to scheduling."

Now go back to step 1, click **Robert Chen, MRI brain**, and run steps 2 to 4 quickly (about 20 seconds, no narration beyond "same thing"). Note the orange flag on the packet checklist: red-flag features not documented. Say: "The agent already warned us this one might get denied."

Return to the queue. Click **Advance 3 days** twice. Robert flips to **Appeal needs signature**.

## 6. Appeal a denial (30 seconds)

Click **Review appeal**.

> "Denied for insufficient documentation. Within a minute the agent has drafted the appeal: the denial reason, the patient's history, and the ACR Appropriateness Criteria citation that says a new headache after 50 is itself a red flag. Dr. Ortega reads it, edits it if he wants, and signs. The doctor owns the clinical argument; the agent owns the paperwork."

Click **Sign and submit**, then **Advance 3 days**. Robert flips to **Overturned, approved**.

## 7. Monday report (20 seconds)

Click **Owner's Monday report.**

> "Luis, this is your view. Turnaround, denial rate, appeal rate, overturn rate, and which payer is slow. One tile, Monday morning. In production you can ask it questions in plain English: which payer denies us most."

Say plainly: "These numbers are synthetic placeholders. Yours will come from your own volume."

## Questions you will get

- **"Is any of this connected to a real insurance company?"** No. It talks to HL7's public test server for the prior-auth standard. Connecting to Blue Cross or UHC means credentialing with each payer, which is Phase 4 work once the center has payer contracts.
- **"What about the clearinghouse / Availity?"** Same code path; the agent can submit through a clearinghouse where a payer is not yet on FHIR. Fax-and-portal payers get a human-assisted path with the agent preparing the packet.
- **"Exa says they are building this."** Good, use it if it ships and it is good. The agent sits above the PACS and RIS, so it works with Exa, Sectra, or whatever the center buys, and it covers the owner's reporting and the appeal drafting, which a PACS vendor will not.
- **"Can it get this wrong?"** Yes, which is why the two purple gates exist. It never submits or signs on its own.
- **"How long did this take to build?"** The prototype took an evening against a public test server. Production is the work on the build page: your RIS, your real payers, security and the BAAs, and your staff testing it before you open.

## If the Wi-Fi dies

The page is static and loads from a cache once opened; the only thing that needs the network is step 4. Open it on the phone over cellular before you sit down.
