# Demo script: Prior Authorization Agent (about 3 minutes)

**Live URL:** https://rfinlay.github.io/imaging-priorauth-demo/
**Works on:** laptop, iPad, phone. No login. Open it before dinner and leave the tab up.
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

If Jesse wants proof, click **Show the FHIR request we sent** or the **Open the stored response** link. If the banner was orange, say instead: "Tonight the public test server is down, so this one went to our simulated payer, which is why it is labeled that way. The code path is the same."

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

- **"Is any of this connected to a real insurance company?"** No. It talks to HL7's public test server for the prior-auth standard. Connecting to Blue Cross or UHC means credentialing with each payer, which is build work (milestone B2 onward) once the center has payer contracts.
- **"What about the clearinghouse / Availity?"** Same code path; the agent can submit through a clearinghouse where a payer is not yet on FHIR. Fax-and-portal payers get a human-assisted path with the agent preparing the packet.
- **"Exa says they are building this."** Good, use it if it ships and it is good. The agent sits above the PACS and RIS, so it works with Exa, Sectra, or whatever the center buys, and it covers the owner's reporting and the appeal drafting, which a PACS vendor will not.
- **"Can it get this wrong?"** Yes, which is why the two purple gates exist. It never submits or signs on its own.
- **"How long did this take to build?"** The prototype took an evening against a public test server. Production is the work on the build page: your RIS, your real payers, security and the BAAs, and your staff testing it before you open.

## If the Wi-Fi dies

The page is static and loads from a cache once opened; the only thing that needs the network is step 4. Open it on the phone over cellular before you sit down.
