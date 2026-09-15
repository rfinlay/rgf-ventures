# BAA Analysis — RGF Global Ventures <> Southwest X-Ray

**Prepared by:** Sherlock (research agent)
**Date:** 2026-09-15
**For:** Rick Finlay, ahead of the PACS visit on 2026-09-16, 2:00 PM
**Companion document:** `BAA-RGF-SouthwestXray-DRAFT-2026-09-16.md`
**All sources retrieved:** 2026-09-15

> **This is not legal advice.** I am a research agent, not an attorney. This document is an evidenced analysis of primary regulatory text and public corporate information, written so that a lawyer's review can be short and targeted rather than exploratory. **A Texas healthcare attorney should review the BAA before signature.** Note that healthcare regulatory work is a distinct competency from general litigation or business law — a firm that handles an unrelated matter well is not thereby the right firm for a HIPAA instrument. Ask specifically for HIPAA and health information privacy experience.

---

## The 90-second version

1. **You almost certainly do not need a signed BAA to do tomorrow's visit as scoped** — installing Tailscale, standing up SSH, and asking questions. **Confidence: Medium-High.** But that conclusion rests entirely on you actually holding the line on scope, and the line is thinner than it sounds.
2. **The riskier exposure tomorrow is not HIPAA. It is authorization.** Getting onto a clinical endpoint you were let onto by a 1099 contractor who does not own it is the thing that looks bad in hindsight. Get an email. **Confidence: High.**
3. **Southwest X-Ray is an Akumin company.** This materially changes who signs and how long it will take. **Confidence: High** on the affiliation, **Low** on the correct contracting entity.
4. **Do not send this BAA to Luis to "pass along."** It goes to a named Akumin privacy or contracting officer, or it goes nowhere.

---

## 1. Who actually signs

### What I established

| Finding | Evidence | Confidence |
|---|---|---|
| Southwest X-Ray operates five outpatient imaging centers in El Paso | swxrayonline.com locations page; corroborating directory listings | **High** |
| The PACS at `exa.swxrayonline.com` is Southwest X-Ray's patient/physician portal | swxrayonline.com links its Patient Portal to `https://exa.swxrayonline.com/p/SWXR/login` and its Physician Portal to `https://exa.swxrayonline.com/phy/SWXR/login`; both resolve (HTTP 200) | **High** |
| Southwest X-Ray is **an Akumin company** | swxrayonline.com footer: "Southwest X-Ray — An AKUMIN Company. © 2026 Akumin Inc. All rights reserved." Careers link points to `akumin.com/careers` | **High** |
| Akumin acquired Southwest X-Ray on 2019-08-16 | PitchBook company profile (secondary source, not verified against a primary filing) | **Medium** |
| Southwest X-Ray's HIPAA Notice of Privacy Practices **is Akumin's corporate notice** | swxrayonline.com footer links directly to `akumin.com/wp-content/uploads/Akumin_NoticeOfPrivacyPolicy_Apr032020-1.pdf` (HTTP 200) | **High** |
| Akumin's privacy contact is `privacy@akumin.com`, and Akumin designates a Privacy Officer | akumin.com/policies-notices/protected-health-information/ | **High** |

### Covered Entity or Business Associate?

**Southwest X-Ray is a Covered Entity, and specifically a health care provider that transmits health information electronically in connection with covered transactions. Confidence: High.**

The reasoning is direct. A "covered entity" includes "a health care provider who transmits any health information in electronic form in connection with a transaction covered by this subchapter" ([45 CFR 160.103](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103)). Southwest X-Ray performs and bills for diagnostic imaging, offers an insurance-coverage page, and runs an online patient billing portal. It publishes a HIPAA Notice of Privacy Practices, which is an obligation of covered entities under 45 CFR 164.520 — not of business associates. Entities do not publish an NPP unless they think they are a covered entity.

**So the instrument is a BAA, not a subcontractor BAA. Confidence: Medium-High** — high on the substance, discounted because of the entity question below, and because Akumin also sells "Managed Services" and "Joint Ventures" to other providers, meaning some Akumin entities are business associates in some relationships. The BAA draft handles this with a capacity clause that works either way, since 45 CFR 164.504(e) and 45 CFR 164.308(b)(2) impose materially identical requirements on a BA and on a subcontractor.

### What I could NOT determine, and will not guess at

**The correct contracting legal entity. Confidence in any specific answer: Low. I am not naming one.**

"Southwest X-Ray" is a trade name. What I do not know:

- Whether it is an assumed name of an Akumin subsidiary, a surviving Texas legal entity under Akumin ownership, or a d/b/a of a management company.
- Whether the radiology professional services are delivered through a separate physician-owned professional association — the "friendly PA" structure that Texas corporate-practice-of-medicine doctrine commonly produces. If so, there may be **two** entities in play: the imaging facility (technical component) and a physician entity (professional component), and Luis may read for the latter while the PACS is operated by the former.
- Whether Akumin centralizes BAA execution corporately. Akumin's corporate addresses appear on its site as Plantation, FL and Tampa, FL, and its Privacy Officer contact is corporate — which suggests centralization.

I did not search state corporate registries or SEC filings to resolve this. It is resolvable, but it is a question for counsel or for Akumin itself, and guessing wrong puts the wrong name on a signed contract. **Do not fill the entity name from a website footer.**

**Practical read:** a corporate privacy function at a multi-state imaging operator will have a standard vendor BAA and a vendor-onboarding process. Realistically **they will hand you their paper, not sign yours.** That is fine and normal. The value of the drafted BAA is then (a) it proves you are credible, and (b) Sections 3.3 and 3.4 are the architecture-specific terms you should insist are carried into their template, because their template will not have them.

---

## 2. Is a BAA required for tomorrow's no-PHI infrastructure assessment?

**This is the decision-relevant question. Here is the direct answer.**

### Short answer

**No — a signed BAA is not legally required to perform a genuinely read-only infrastructure assessment in which you do not create, receive, maintain, or transmit PHI. Confidence: Medium-High.**

**But the practical answer is different from the theoretical one, and the gap is where the risk lives. Confidence: High.**

### The theoretical analysis

BA status is triggered by function, not by proximity. Under [45 CFR 160.103](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103), a business associate is a person who, on behalf of a covered entity, "creates, receives, maintains, or transmits protected health information for a function or activity regulated by this subchapter," or who provides enumerated services "where the provision of the service involves the disclosure of protected health information." Those four verbs are the whole test. Standing in a room where PHI is visible is none of them.

HHS makes the carve-out explicit. Its Business Associates guidance lists, under **"Other Situations in Which a Business Associate Agreement Is NOT Required,"** that a BAA is not required:

> "With a person (e.g., janitorial service, electrician) whose functions or services do not involve the use or disclosure of PHI, provided that access to PHI by such persons would be only **incidental**, if at all, and that **reasonable safeguards** are in place."
> — [HHS OCR, *Business Associates*](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html)

That is the exception you would be relying on. **Note both conditions.** It is not enough that exposure is incidental; reasonable safeguards must also be in place. The safeguard obligation at 45 CFR 164.530(c) is the covered entity's, but your conduct is what makes it satisfiable.

### Why the conduit exception is the wrong thing to reach for

The conduit exception gets cited constantly and almost always wrongly. HHS is unambiguous that it is narrow:

> "The conduit exception is limited to entities that only provide transmission services for PHI (whether in electronic or paper form), including any temporary storage of PHI. **Entities that access PHI on a regular or frequent basis to perform a service on behalf of a covered entity are not conduits.**"
> — [HHS OCR, *Business Associates*](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html)

And in the cloud computing guidance, asked directly whether a cloud provider can be a conduit:

> "**Generally, no.** ... the conduit exception is limited to transmission-only services for PHI... **Any access to PHI by a conduit is only transient in nature.** In contrast, a CSP that maintains ePHI for the purpose of storing it will qualify as a business associate, and not a conduit."
> — [HHS OCR, *Guidance on HIPAA & Cloud Computing*](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html)

**RadAssist is not a conduit and never will be.** Do not build any argument on that exception. The incidental-access carve-out is the right one, and it is a different doctrine. **Confidence: High.**

### Why the theoretical answer is fragile — read this part twice

Three things make tomorrow's "no PHI" scope harder to hold than it sounds.

**(a) The line between "assessment" and "support services" is thin, and HHS has drawn it against you.** The same HHS guidance lists as an example of a business associate:

> "**IT contractor or vendor** (e.g., EHR vendor, Managed Services Provider) **that provides maintenance and/or support services (either in person or remotely) for information systems that require the contractor or vendor to create, receive, maintain, or transmit ePHI.**"

Read that carefully. The operative qualifier is still "that require... ePHI." A one-time feasibility assessment that touches no ePHI is not that. But **persistent remote SSH access to a clinical workstation, established for ongoing technical work, walks straight toward it.** Tomorrow's plan does not stop at looking — it stands up durable remote access. The assessment is arguably pre-contractual due diligence; the standing access channel is the thing that starts to look like ongoing IT support. **Confidence: Medium** that a regulator would see the standing access as the pivot point, but it is the honest reading.

**(b) A PACS workstation has PHI on screen, and the plan contemplates Luis driving a real study.** The visit plan asks for "a de-identified or test study he can drive, or willingness to drive a real one while we look only at mechanism and never capture." If it is a real study, you will see patient names. That is incidental exposure — permitted — right up until you record it.

**(c) The Plaud recorder is the single highest-risk item on the checklist.** An audio recording that captures a spoken patient name converts incidental exposure into **creation of PHI in RGF's custody**, on RGF's device, outside any BAA. That is not a gray area. The visit plan already flags this ("Ask before switching it on... If a real study is on screen, pause the recorder"), and that instruction is correct and load-bearing. **Confidence: High.**

### So what do you actually do tomorrow?

**Proceed. Do not gate the visit on a signature.** A no-PHI infrastructure assessment with incidental exposure does not require a BAA, and waiting for a multi-state imaging operator's legal department would cost weeks for a benefit you do not yet need.

**But treat the incidental-access exception as a scope commitment you have to actually honor,** not as a label you apply afterward. Its protection evaporates the moment you record, export, or retain anything.

---

## 3. The 1099 problem

### Does Luis have authority to grant RGF access to the PACS?

**Almost certainly not, as to the PACS itself. Confidence: High.**

Luis is an independent contractor who reads studies. Two distinct things get conflated here and should not be:

| Asset | Who likely controls it | Can Luis grant RGF access? |
|---|---|---|
| His own workstation, if he owns it | Luis | **Probably yes** — it is his device |
| His Exa PACS **credentials and session** | Southwest X-Ray / Akumin | **No.** Credentials are issued to him personally and are near-universally non-transferable by their terms of use |
| The PACS environment, DICOM nodes, HL7 interfaces | Southwest X-Ray / Akumin IT | **No** |
| A workstation owned by the imaging group | Southwest X-Ray / Akumin | **No** |

Akumin's own website says the quiet part out loud: "The medical professionals listed on this website **may include independently contracted radiologists**... and other medical professionals **who are not affiliated with Akumin Inc.**" ([akumin.com](https://akumin.com/policies-notices/protected-health-information/)). Akumin is publicly disclaiming an affiliation relationship with contracted radiologists. A person whose affiliation the company disclaims is not a person who can bind the company. **Confidence: High.**

This is why Section 3.7(b) of the draft BAA says so expressly, and why Section 3.7(c) forbids RGF from operating under any physician's credentials. If tomorrow's access path is "Luis logs in and Rick looks at his session," that is a credential-sharing posture that will be hard to defend later, no matter how benign the intent.

### "Approved through his IT" — the precise question that needs answering

The phrase is ambiguous in exactly the way that matters. **Whose IT?** Decompose it into four questions, ordered by how much they change the engagement:

1. **Who owns the workstation — you, or the imaging group?**
   *If Luis: his to grant. If the group: nothing gets installed until the group says so, in writing.*

2. **Who said yes, by name and title, and what did they think they were approving?**
   *"IT approved" could mean a helpdesk tech unblocked a software install. That is not authorization for a third-party company to establish persistent remote access to a clinical endpoint. These are different approvals with different signatories.*

3. **Who operates `swxrayonline.com` and the Exa instance — Southwest X-Ray locally, or Akumin corporate IT?**
   *This determines whether the person who can actually say yes is in El Paso or in Florida, and it determines your timeline.*

4. **Who is the privacy or compliance contact?**
   *Akumin publishes `privacy@akumin.com` and references a Privacy Officer. For a BAA you need a named human, not a shared inbox.*

### What written authorization should look like

It does not need to be a contract. One email is enough, and it should contain five things:

1. **Who is authorizing** — name, title, entity, and a statement that they have authority to authorize third-party access on behalf of that entity.
2. **Who is being authorized** — Richard Finlay, RGF Global Ventures LLC.
3. **What, specifically** — e.g. "install Tailscale and OpenSSH on the workstation at [location] and connect remotely for read-only technical assessment of the imaging environment."
4. **What is excluded** — no access to PHI, no export of studies, no configuration changes to the PACS, no use of physician credentials.
5. **Duration**, and who to notify when it ends.

**Framing for Luis, from the visit plan and worth keeping verbatim:** *"so I've got something on file showing this was sanctioned — which protects you more than me."* That is true, not a technique. If this goes sideways, the contractor who let a vendor onto a clinical endpoint without written approval is in a worse position than the vendor.

**Confidence: High** that written authorization is the right ask. **Medium** on whether Luis can produce it quickly — he may not know who to ask, in which case **the name of the person who can say yes is itself a successful outcome of tomorrow.**

---

## 4. What Rick should NOT do tomorrow, pending signature

Ordered by how badly each one goes wrong.

| Do not | Why |
|---|---|
| **Record audio while a real study is on screen** | Converts incidental exposure into PHI created and held by RGF, on RGF's device, outside any BAA. Ask before the recorder goes on; pause it for anything clinical. **This is the number one item.** |
| **Screenshot, photograph, or export anything from Exa** | Same conversion, plus it creates a retained artifact you would have to account for. No "just one screenshot of the layout" with a study open. |
| **Log into Exa using Luis's credentials, or watch over his shoulder while he navigates real studies to demonstrate features** | Credential sharing. Ask for a de-identified or test study. If none exists, look at the *mechanism* — menus, export options, settings — not at study content. |
| **Copy, download, or open any DICOM file or study export** | Directly triggers "receives." This is the bright line. |
| **Install RadAssist components, browser extensions, or agents** | The visit plan already says access + recon only. An installed component that touches the Exa DOM is a product deployment, and that is where BA status becomes unarguable. |
| **Change any Exa, PACS, or browser configuration** | You do not have authority, and a change on a clinical system is the one thing that generates an incident report. |
| **Run network scans while standing there** | The visit plan already defers this. Unannounced scanning of a clinical network without written authorization is a security-incident trigger independent of HIPAA. |
| **Leave persistent access in place without written authorization following within days** | Standing remote access is the fact pattern that most resembles "IT support services" in HHS's BA examples. Time-box it or get it papered. |
| **Hand the BAA to Luis to "pass to legal"** | A contractor is not a channel for contract execution and it puts him in an awkward position. Get the name of a privacy or contracting officer and send it to them. |
| **Enable the RadAssist local-draft feature against real studies** | Unresolved BitLocker status. See below. |

### The BitLocker item — resolve it tomorrow, it is nearly free

It is unresolved whether Luis's workstation has BitLocker full-disk encryption enabled. It intersects the BAA at **Section 5.4**, and the consequence is concrete:

- With FDE enabled and meeting the Secretary's guidance, PHI on a lost or stolen device is **secured** PHI and its loss is **not a reportable Breach** ([45 CFR 164.402](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D/section-164.402)).
- Without it, the same loss is a **reportable breach of Unsecured PHI**, and Section 4 of the BAA would obligate RGF to report it within five business days.

The check is one command: `manage-bde -status C:`. **Put it on tomorrow's list.** Note that the encrypted-at-rest safe harbor turns on device state at the time of loss — a machine lost while powered on and logged in with the volume unlocked does not get the benefit. **Confidence: High** on the mechanism, **Medium** on real-world application, since it is a fact question.

This also has a product consequence beyond compliance: `RESEARCH-phi-persistence.md` recommends browser-local draft persistence and independently identifies FDE status as "the single most important input to option (b)'s risk profile." Same fact, two decisions.

---

## 5. Confidence summary

| Conclusion | Confidence | What would change it |
|---|---|---|
| Southwest X-Ray is an Akumin company | **High** | Nothing; it is on their own site |
| Southwest X-Ray is a Covered Entity (health care provider) | **High** | Discovery of a split professional/technical entity structure where the PACS sits in a non-provider entity |
| The instrument is a BAA, not a subcontractor BAA | **Medium-High** | Learning the PACS is operated by an Akumin managed-services entity acting as a BA for other providers |
| The correct contracting legal entity | **Low — not determined, not guessed** | A corporate registry search, or asking Akumin |
| A signed BAA is **not required** for a genuinely no-PHI infrastructure assessment | **Medium-High** | Any recording, export, or retention of PHI; or the assessment becoming ongoing IT support |
| Incidental on-screen exposure does not itself create BA status | **High** | Nothing in current guidance |
| The conduit exception does **not** apply to RadAssist | **High** | Nothing; HHS is explicit |
| Luis cannot authorize PACS access | **High** | Evidence he holds a formal administrative role at the entity, not just reading privileges |
| Luis can authorize access to a workstation **he personally owns** | **Medium** | Learning the group owns the device |
| Written authorization is the correct ask | **High** | — |
| An AI Service receiving PHI is a subcontractor requiring its own BAA | **High** | A regulatory change; none pending that I found |
| Texas ch. 181 adds obligations if RGF ever stores PHI | **Medium-High** | Verification against the primary statute, which I did not obtain |

---

## 6. What I could not verify

Stated plainly.

1. **Southwest X-Ray's exact legal entity name, state of organization, EIN, registered agent, and authorized officers.** Not researched in corporate registries, not guessed. All left as `[FILL]`.
2. **Whether Akumin executes BAAs corporately or at the facility level**, and who the named Privacy Officer is. Only the shared address `privacy@akumin.com` is published.
3. **Whether a separate physician professional entity exists** between Luis and the facility. This is common in Texas because of corporate-practice-of-medicine doctrine, but I found no evidence either way.
4. **The 2019 Akumin acquisition date** rests on a PitchBook profile — a secondary source. The *current* affiliation is solid because it is on Southwest X-Ray's own site; the acquisition date is not independently confirmed.
5. **Who owns Luis's workstation.** Question 2 in the visit plan. Unanswered.
6. **What "approved through his IT" meant** — whose IT, what scope, by whom. The central open question.
7. **BitLocker status on the workstation.** Unresolved.
8. **Whether Akumin's vendor BAA template exists and what it contains.** Almost certainly it does. Not obtainable publicly.
9. **Texas Health & Safety Code ch. 181** could not be retrieved from the official state server in prior research (`statutes.capitol.texas.gov` returns a JavaScript shell); the text relied on came from `texas.public.law`. Flagged in `RESEARCH-phi-persistence.md` and not re-verified here. **Verify against the primary source before relying on the Texas analysis.**
10. **The Akumin Notice of Privacy Practices PDF** resolves (HTTP 200) but I did not read its contents; I relied on the HTML privacy page and the site's own framing.
11. **Whether Exa/Konica Minolta imposes contractual terms** on third-party integration or credential use. Not researched. Could independently constrain what RadAssist may do against the Exa session even if HIPAA permits it.

---

## 7. URL status log

Every URL cited, with the HTTP status observed on 2026-09-15.

| URL | Status | Notes |
|---|---|---|
| https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html | **200** / 403 | 200 via MCP fetcher; 403 to curl and WebFetch. **Page is live.** Published Jan. 25, 2013; content last reviewed June 16, 2017 |
| https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html | **200** / 403 | Same split; 200 via MCP fetcher |
| https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html | **200** | Via MCP fetcher |
| https://www.hhs.gov/hipaa/for-professionals/faq/3006/does-a-covered-entity-need-a-business-associate-agreement-with-a-cloud-service-provider/index.html | **403** | Not relied upon; superseded by the cloud computing guidance above |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103 | **200** | |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504 | **200** | |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502 | **200** | |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D/section-164.410 | **200** | |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D/section-164.402 | **200** | |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306 | **200** | |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308 | **200** | |
| https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514 | **200** | |
| https://swxrayonline.com/ | **200** | Footer: "An AKUMIN Company. © 2026 Akumin Inc." |
| https://swxrayonline.com/for-patients/protected-health-information/ | **200** | |
| https://akumin.com/policies-notices/protected-health-information/ | **200** | Privacy Officer contact: privacy@akumin.com |
| https://akumin.com/wp-content/uploads/Akumin_NoticeOfPrivacyPolicy_Apr032020-1.pdf | **200** | Resolves; contents not read |
| https://exa.swxrayonline.com/p/SWXR/login | **200** | Patient portal; login page only, not accessed further |

Regulatory text was retrieved from the eCFR versioner API at the **2026-09-01** point-in-time snapshot of Title 45.

---

## 8. Recommended sequence after tomorrow

1. **Get the authorization email** — or the name of the person who can send it. Highest-value non-technical outcome of the visit.
2. **Confirm workstation ownership and BitLocker status.** Both are one question each.
3. **Identify the Akumin privacy or vendor-contracting contact.** Start from `privacy@akumin.com` only if no named person emerges.
4. **Have a Texas healthcare attorney review the draft BAA** before it goes to any counterparty. Expect Akumin to counter with their own paper — the review is still worth it, because it tells you which of your Sections 3.3 and 3.4 terms to insist on in theirs.
5. **Keep Tier 1 the product boundary** until a BAA is executed. The strongest position remains the one `RESEARCH-phi-persistence.md` already argues for: RGF never creates, receives, maintains, or transmits PHI, so the obligation set never attaches. The BAA is insurance against that posture changing, not permission to change it.
