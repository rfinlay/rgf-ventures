# Prior Authorization Agent: demo script for the Thursday briefing

**Slide 10, about 3 minutes.** Thursday 2026-11-05 at 3:30 PM, with Luis, Fernando and Jesse. This is the only live demo at the table; RadAssist on slide 33 is a spoken overview, not a demo.

**Live URL:** https://rfinlay.github.io/imaging-priorauth-demo/
**Runs on:** the phone and the laptop. No login. Open it on both Thursday morning, the phone over cellular, and leave both tabs up until the meeting is over.
**Source and the real-vs-simulated table:** https://github.com/rfinlay/imaging-priorauth-demo#readme

## Before the meeting: the banner

Glance at the top banner on both devices.

- **Green, "Payer sandbox: LIVE (HL7 Da Vinci PAS)":** the submission in step 4 goes to HL7's public test server. Say the green line in step 4.
- **Orange, "sandbox offline":** the demo still runs end to end; the submission goes to the simulated payer and says so on screen. Say the orange line in step 4.

Either way the demo works. Decide which line you are saying before you sit down, and check the banner again once at the table before you start.

## The link, the QR, and the pace (Rick, 2026-11-03)

- **Thursday morning:** text the link to Luis. He forwards it to Fernando and Jesse. Slide 10 and the leave-behind carry a QR code for the same URL with the caption "Scan to follow along."
- **At the table:** they scan the QR or open the text on their own phones and reload once for a fresh start. You run the same page on the laptop, split screen beside the deck, and set the pace.
- **Say each step before anyone clicks.** The one that matters is **Advance 3 days**: everyone waits for you, because whoever clicks it early is a step ahead of the room and the story stops matching.
- Pricing is not part of the demo; it comes later, on slide 23, after the close.

## Reset (Rick, 2026-11-03)

A **full page reload** (Cmd+R on the laptop, pull-to-refresh on the phone) resets Maria and Robert to new orders. The **"Start over with another order"** button does **not** reset state; after a rehearsal the queue still shows the old outcomes. Reload once before the meeting, and reload again before you hand the phone over, so the first click anyone sees is a fresh order. Reload on Wi-Fi or cellular before you need it, never mid-demo.

## Framing (10 seconds)

> "This is a working prototype, not slides. Everything you see is synthetic data, but the submission in the middle goes to a real payer test server that implements the national prior-auth standard. I want you to click it, not watch me."

They follow on their own phones (scanned QR or the forwarded text); keep the laptop as your own screen and lead from it. If someone has no phone out, hand them yours.

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

**Green banner line:**

> "That just went over the wire to HL7's prior-authorization test server, in the FHIR format CMS is requiring every Medicare Advantage and exchange plan to support by January 2027. That tracking number is real; the link opens the stored record on their server."

**Orange banner line:**

> "Today the public test server is down, so this one went to our simulated payer, which is why it is labeled that way. The code path is the same."

If Jesse wants proof, click **Show the FHIR request we sent** or the **Open the stored response** link.

**The boundary line.** Say it before anyone asks, because Fernando will:

> "The test server accepts and stores the request but has no medical-necessity rules for imaging, so the approve or deny you are about to see is simulated. Real payer decisions come when a real payer connects, which is the point of the 2027 rule."

Click **Next: track the clock.**

## 5. Track the clock, Maria first (30 seconds)

> "Standard requests get a 7-day clock, expedited get 72 hours. Those are the CMS deadlines payers have to meet starting this year. The agent watches every one and escalates at 75 percent."

Click **Advance 3 days** at the top. Maria flips to **Approved** with an auth number.

> "Approved in two days. The order goes straight to scheduling."

## 6. Robert, the denial (about 20 seconds, then 30)

Go back to step 1, click **Robert Chen, MRI brain**, and run steps 2 to 4 quickly, no narration beyond "same thing." Point at the orange flag on the packet checklist: red-flag features not documented.

> "The agent already warned us this one might get denied."

Return to the queue. Click **Advance 3 days** twice. Robert flips to **Appeal needs signature**. Click **Review appeal**.

> "Denied for insufficient documentation. Within a minute the agent has drafted the appeal: the denial reason, the patient's history, and the ACR Appropriateness Criteria citation that says a new headache after 50 is itself a red flag. Dr. Ortega reads it, edits it if he wants, and signs. The doctor owns the clinical argument; the agent owns the paperwork."

Click **Sign and submit**, then **Advance 3 days**. Robert flips to **Overturned, approved**.

## 7. Monday report (20 seconds)

Click **Owner's Monday report.**

> "Luis, this is your view. Turnaround, denial rate, appeal rate, overturn rate, and which payer is slow. One tile, Monday morning. In production you can ask it questions in plain English: which payer denies us most."

Say plainly: "These numbers are synthetic placeholders. Yours will come from your own volume."

Then back to the deck.

## Q&A you will get

- **"Is any of this connected to a real insurance company?"** No. It talks to HL7's public test server for the prior-auth standard. Connecting to Blue Cross or UHC means credentialing with each payer, which is Phase 4 work once the center has payer contracts.
- **"What about the clearinghouse / Availity?"** Same code path; the agent can submit through a clearinghouse where a payer is not yet on FHIR. Fax-and-portal payers get a human-assisted path with the agent preparing the packet.
- **"Exa says they are building this."** Good, use it if it ships and it is good. The agent sits above the PACS and RIS, so it works with Exa, Sectra, or whatever the center buys, and it covers the owner's reporting and the appeal drafting, which a PACS vendor will not.
- **"Can it get this wrong?"** Yes, which is why the two purple gates exist. It never submits or signs on its own.
- **"How long did this take to build?"** The prototype took an evening against a public test server. Production is the work on the build page: your RIS, your real payers, security and the BAAs, and your staff testing it before you open.

## If the Wi-Fi dies

The page is static and loads from a cache once opened; the only thing that needs the network is step 4. The phone is on cellular, so switch to it and keep going. If step 4 cannot reach the test server, the page falls back to the simulated payer on its own; say the orange banner line and carry on. Do not reload either tab.
