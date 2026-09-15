# BUSINESS ASSOCIATE AGREEMENT

**DRAFT — NOT FOR SIGNATURE WITHOUT COUNSEL REVIEW.**
Prepared 2026-09-15 by Sherlock (research agent) for RGF Global Ventures LLC.
Companion analysis: `BAA-SouthwestXray-ANALYSIS.md` — read it before sending this to anyone.

<!--
=====================================================================================
DRAFTING NOTES — DELETE THIS ENTIRE COMMENT BLOCK BEFORE SENDING TO THE COUNTERPARTY.
These notes are internal. They are not part of the contract and must not be.
=====================================================================================

SOURCE OF THE MODEL TEXT
This instrument is built on the HHS "Sample Business Associate Agreement Provisions,"
published January 25, 2013, page content last reviewed June 16, 2017, retrieved
2026-09-15 from:
  https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html
  HTTP status: 200 via the MCP fetcher; 403 to curl and to the WebFetch tool
  (hhs.gov bot-filters those user agents). The page IS live. The 403 is a client
  fingerprinting artifact, not a dead link.
HHS states plainly that the sample provisions "address only concepts and requirements
set forth in the HIPAA Privacy, Security, Breach Notification, and Enforcement Rules,
and alone may not be sufficient to result in a binding contract under State law."
Contract formalities (governing law, counterparts, entire agreement, notice, signature
blocks) have been added and are NOT from HHS.

WHICH TIERS THIS BAA COVERS
  Tier 1 (no PHI at all, or PHI local-only in the clinician's browser):
      COVERED, and deliberately over-covered. Under the architecture described in
      Section 3.3, RGF arguably never becomes a business associate at all, because it
      never creates, receives, maintains, or transmits PHI (45 CFR 160.103). This
      agreement is executed as a belt-and-suspenders measure. Signing a BAA does not
      make RGF a business associate if it otherwise is not one; it allocates risk.
  Tier 2 (RGF personnel with credentialed or remote access to the PACS environment,
      read-only technical work, support and maintenance):
      COVERED. This is the tier that most plainly triggers BA status. HHS's Business
      Associates guidance names "IT contractor or vendor (e.g., EHR vendor, Managed
      Services Provider) that provides maintenance and/or support services (either in
      person or remotely) for information systems that require the contractor or vendor
      to create, receive, maintain, or transmit ePHI" as a business associate example.
      https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html
  Tier 3 (an autonomous or semi-autonomous AI agent that interacts with the PACS
      directly, retrieves studies, or drafts reports from PHI):
      NOT ADEQUATELY COVERED BY THIS DOCUMENT AS DRAFTED. Section 3.4 is a deliberate
      prohibition, not an authorization. Tier 3 needs its own negotiated amendment
      covering, at minimum: which model providers may process PHI, on what legal basis,
      whether outputs are retained or used for training, human-in-the-loop review of
      AI-generated clinical text, and the CE's audit rights over the model pipeline.
      Do not attempt to draft Tier 3 terms without counsel.

WHY SECTION 3.4 (AI/LLM) EXISTS AND IS WRITTEN AS A PROHIBITION
This is currently material and is the clause a generic template will not contain.
If RadAssist transmits any PHI to a third-party model API (OpenAI, Anthropic, Google,
or any hosted inference provider), that provider is creating, receiving, maintaining,
or transmitting ePHI on RGF's behalf and is therefore a SUBCONTRACTOR business associate
under 45 CFR 160.103(3)(iii), requiring its own BAA before any PHI is disclosed to it.
HHS's cloud computing guidance forecloses the two most common escape hatches:
  - Encryption does not help. "An entity that maintains ePHI on behalf of a covered
    entity (or another business associate) is a business associate, even if the entity
    cannot actually view the ePHI... even if it does not hold a decryption key."
  - The conduit exception does not apply. "Generally, no... the conduit exception is
    limited to transmission-only services for PHI... Any access to PHI by a conduit is
    only transient in nature."
  https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html
HHS also now lists a "Third-party vendor Artificial Intelligence (AI) chatbot on a
provider's patient portal" as a business associate example, so OCR is treating AI
vendors as squarely inside the BA framework.
Drafting choice: prohibit by default, permit only by written amendment naming the
provider. That converts an open-ended liability into a controlled one, and it is
honest about the current architecture, in which the only ML component (tesseract.js
OCR) runs in-page on the clinician's own workstation and calls no external API.

THE BITLOCKER GAP — SEE SECTION 5.4
Section 5.4 is drafted as an affirmative allocation of responsibility, not a warranty,
because RGF cannot warrant the state of a workstation it does not own or control.
As of 2026-09-15 it is UNRESOLVED whether Dr. Ramos's reading workstation has BitLocker
full-disk encryption enabled. This matters concretely and not theoretically:
  - Section 3.3 authorizes a browser-local draft store on that workstation.
  - Under 45 CFR 164.402, PHI encrypted to HHS-specified standards is "secured" PHI,
    and its loss falls within the breach safe harbor and is not reportable.
  - If BitLocker is OFF, a lost or stolen workstation is a reportable breach of
    UNSECURED PHI. RGF's marginal contribution would be small next to the PACS caches
    and dictation drafts already on that machine, but it would be non-zero, and
    Section 2(c) of this agreement would then require RGF to report it.
DO NOT enable the local draft feature against real studies until this is confirmed.
Confirming it is a one-line check (`manage-bde -status C:`) and it belongs on the
2026-09-16 visit checklist. See RESEARCH-phi-persistence.md, which reaches the same
conclusion independently and rates it "the single most important input to option (b)'s
risk profile."

WHO SIGNS — UNRESOLVED, SEE THE ANALYSIS DOCUMENT
Southwest X-Ray is branded on its own website as "An AKUMIN Company" with a footer
reading "© 2026 Akumin Inc." Its patient and physician portals resolve to
exa.swxrayonline.com and its HIPAA Notice of Privacy Practices is Akumin's corporate
notice. It is therefore NOT established that "Southwest X-Ray" is the correct
contracting legal entity, or that a Southwest X-Ray site manager has authority to bind
it. The signature block is left deliberately open. Do not fill in an entity name,
address, EIN, or officer from a website footer.
=====================================================================================
-->

---

This Business Associate Agreement (this "Agreement") is entered into by and between:

- **Covered Entity:** `[FILL: exact legal entity name — see drafting note. Do not use the trade name "Southwest X-Ray" unless counsel confirms it is the contracting legal entity and not an assumed name of an Akumin subsidiary]`, a `[FILL: state]` `[FILL: entity type]` with its principal place of business at `[FILL: street address, city, state, ZIP]` ("Covered Entity"); and

- **Business Associate:** **RGF Global Ventures, LLC**, a Texas limited liability company located in El Paso, Texas ("Business Associate").

Covered Entity and Business Associate are each a "Party" and together the "Parties."

**Effective Date:** `[FILL: effective date]`

> **Note on the Parties' respective capacities.** If Covered Entity is itself a business associate of one or more other covered entities with respect to some or all of the Protected Health Information covered by this Agreement, then this Agreement shall operate as a subcontractor business associate agreement as to that Protected Health Information, Business Associate shall be a subcontractor within the meaning of 45 CFR 160.103, and every obligation imposed on Business Associate herein shall apply with equal force. 45 CFR 164.504(e) and 45 CFR 164.308(b)(2) impose materially identical requirements in either configuration, and the Parties intend this Agreement to satisfy both. `[FILL: confirm which capacity applies before execution]`

---

## Recitals

**A.** Covered Entity operates, or contracts for the operation of, a picture archiving and communication system (the "PACS") and related clinical information systems used in the provision of diagnostic imaging services.

**B.** Business Associate develops and supports RadAssist, a radiology reporting and workflow-assistance application (the "Software"), and provides related software development, integration, assessment, testing, and support services (together with the Software, the "Services").

**C.** Performance of the Services may involve Business Associate creating, receiving, maintaining, or transmitting Protected Health Information, or may afford Business Associate access to systems or environments in which Protected Health Information resides.

**D.** The Parties enter into this Agreement to comply with the HIPAA Rules and to permit Business Associate's performance of the Services in a manner that safeguards Protected Health Information.

---

## 1. Definitions

Capitalized terms used but not otherwise defined in this Agreement shall have the same meaning as those terms in the HIPAA Rules.

**(a) "Business Associate"** shall generally have the same meaning as the term "business associate" at 45 CFR 160.103, and in reference to the party to this Agreement shall mean RGF Global Ventures, LLC.

**(b) "Covered Entity"** shall generally have the same meaning as the term "covered entity" at 45 CFR 160.103, and in reference to the party to this Agreement shall mean the entity identified above. Where that entity acts in the capacity of a business associate of another covered entity, "Covered Entity" as used herein shall be construed to mean that entity in its capacity as a business associate, consistent with the Note on the Parties' respective capacities above.

**(c) "HIPAA Rules"** shall mean the Privacy, Security, Breach Notification, and Enforcement Rules at 45 CFR Part 160 and Part 164.

**(d) "Clinical Workstation"** shall mean any computing device owned, controlled, or designated by Covered Entity, or by a physician providing services to or on behalf of Covered Entity, from which the Software is accessed and on which Protected Health Information resides or is displayed.

**(e) "Local Draft Data"** shall have the meaning given in Section 3.3.

**(f) "AI Service"** shall mean any artificial intelligence, machine learning, large language model, or similar inference service operated by a third party and accessed over a network, including any hosted model application programming interface.

**(g)** The following terms shall have the same meaning as in the HIPAA Rules: Breach, Data Aggregation, Designated Record Set, Disclosure, Health Care Operations, Individual, Minimum Necessary, Notice of Privacy Practices, Protected Health Information ("PHI"), Required By Law, Secretary, Security Incident, Subcontractor, Unsecured Protected Health Information, and Use.

---

## 2. Obligations and Activities of Business Associate

Business Associate agrees to:

**(a)** Not use or disclose PHI other than as permitted or required by this Agreement or as Required By Law;

**(b)** Use appropriate safeguards, and comply with Subpart C of 45 CFR Part 164 with respect to electronic PHI, to prevent use or disclosure of PHI other than as provided for by this Agreement;

**(c)** Report to Covered Entity any use or disclosure of PHI not provided for by this Agreement of which it becomes aware, including Breaches of Unsecured PHI as required by 45 CFR 164.410, and any Security Incident of which it becomes aware, in accordance with the timelines in Section 4;

**(d)** In accordance with 45 CFR 164.502(e)(1)(ii) and 45 CFR 164.308(b)(2), ensure that any Subcontractors that create, receive, maintain, or transmit PHI on behalf of Business Associate agree in writing, before any PHI is disclosed to them, to the same restrictions, conditions, and requirements that apply to Business Associate with respect to such PHI;

**(e)** Make available PHI in a Designated Record Set to Covered Entity as necessary to satisfy Covered Entity's obligations under 45 CFR 164.524. Business Associate shall provide such PHI within ten (10) business days of a written request. Where Business Associate receives a request for access directly from an Individual, Business Associate shall not respond substantively and shall forward the request to Covered Entity within five (5) business days;

**(f)** Make any amendment(s) to PHI in a Designated Record Set as directed or agreed to by Covered Entity pursuant to 45 CFR 164.526, or take other measures as necessary to satisfy Covered Entity's obligations under 45 CFR 164.526, within ten (10) business days of a written request. Business Associate shall forward any amendment request received directly from an Individual to Covered Entity within five (5) business days;

**(g)** Maintain and make available the information required to provide an accounting of disclosures to Covered Entity as necessary to satisfy Covered Entity's obligations under 45 CFR 164.528, within ten (10) business days of a written request, and retain such information for six (6) years;

**(h)** To the extent Business Associate is to carry out one or more of Covered Entity's obligations under Subpart E of 45 CFR Part 164, comply with the requirements of Subpart E that apply to Covered Entity in the performance of such obligation(s);

**(i)** Make its internal practices, books, and records relating to the use and disclosure of PHI received from, or created or received by Business Associate on behalf of, Covered Entity available to the Secretary of the U.S. Department of Health and Human Services for purposes of determining compliance with the HIPAA Rules; and

**(j)** Acknowledge that, pursuant to Section 13404 of the HITECH Act (42 U.S.C. 17934) and 45 CFR 164.104(b), Business Associate is directly liable under the HIPAA Rules and subject to civil and, in some cases, criminal penalties for uses and disclosures of PHI not authorized by this Agreement or Required By Law, and for failing to safeguard electronic PHI in accordance with the Security Rule.

---

## 3. Permitted and Required Uses and Disclosures by Business Associate

### 3.1 General limitation

**(a)** Business Associate may use or disclose PHI only as necessary to perform the Services for Covered Entity, and as otherwise expressly permitted by this Agreement.

**(b)** Business Associate may use or disclose PHI as Required By Law.

**(c)** Business Associate shall make uses and disclosures of, and requests for, PHI consistent with Covered Entity's Minimum Necessary policies and procedures.

**(d)** Business Associate shall not use or disclose PHI in a manner that would violate Subpart E of 45 CFR Part 164 if done by Covered Entity, except for the specific uses and disclosures set forth in Sections 3.5 and 3.6.

**(e)** Business Associate shall access PHI on a **read-only** basis and only to the minimum extent necessary to perform the Services, except where the Services expressly require the creation, modification, or transmission of PHI as directed by Covered Entity.

### 3.2 Technical assessment activities

**(a)** Business Associate may access Covered Entity's PACS environment and Clinical Workstations solely to conduct technical assessment, configuration review, and integration-feasibility work, and only pursuant to written authorization from Covered Entity under Section 3.7.

**(b)** In conducting such work, Business Associate shall:

  1. Use de-identified or test data wherever the assessment objective can be met with such data;
  2. Collect and record **system and configuration metadata only** — including network endpoints, service versions, protocol availability, and application behavior — and **not** study content, patient identifiers, or image payloads;
  3. Not capture, screenshot, photograph, record, export, download, or transcribe any PHI, whether by audio recording device, screen capture, or otherwise;
  4. Not copy, move, or transmit any PHI outside Covered Entity's environment; and
  5. Treat any PHI incidentally observed on screen as confidential, not record it, and not further use or disclose it.

**(c)** The Parties acknowledge that incidental exposure to PHI displayed on a Clinical Workstation during such work is foreseeable. Such incidental exposure is permitted under this Agreement, is subject to the reasonable safeguards required by 45 CFR 164.530(c), and does not constitute a use or disclosure not provided for by this Agreement for purposes of Section 2(c), provided Business Associate complies with Section 3.2(b).

### 3.3 Local-only processing and the browser draft store

**(a) Architecture representation.** Business Associate represents that, in the configuration of the Software in effect as of the Effective Date:

  1. Clinical study data entered into or derived by the Software is processed **in the web browser on the Clinical Workstation**;
  2. Such data is **not transmitted to, received by, maintained by, or stored on** any server, database, or cloud service operated by or for Business Associate;
  3. Optical character recognition of any image pasted into the Software is performed **entirely in-page on the Clinical Workstation**, with no transmission of the image or of recognized text to any server or external service; and
  4. Business Associate's servers and databases contain no patient study data, patient identifiers, or clinical measurements.

**(b) Local Draft Data.** The Software may persist in-progress work to browser-local storage on the Clinical Workstation, for the purpose of preventing loss of clinical work on reload or crash ("Local Draft Data"). The Parties acknowledge and agree that:

  1. Local Draft Data resides **solely on the Clinical Workstation**, which is within Covered Entity's own security boundary and is not within Business Associate's custody or control;
  2. Local Draft Data is **not transmitted to** Business Associate and is **not maintained by** Business Associate within the meaning of 45 CFR 164.306(a)(1);
  3. Business Associate shall configure the Software so that Local Draft Data is limited to the active study, is cleared on report completion, on logout, and on the commencement of a new study, and expires automatically no later than `[FILL: TTL, e.g. eight (8) hours]` after last modification;
  4. Business Associate shall **not** persist to Local Draft Data any source image, any raw optical-character-recognition output, or any direct patient identifier, and shall persist only extracted structured clinical fields; and
  5. Business Associate shall not enable any feature that synchronizes, backs up, or replicates Local Draft Data off the Clinical Workstation without prior written amendment to this Agreement.

**(c) Change of architecture.** Business Associate shall notify Covered Entity in writing **not less than thirty (30) days before** implementing any change to the Software that would cause Business Associate or any Subcontractor to create, receive, maintain, or transmit PHI outside the Clinical Workstation, including any server-side persistence of study data, any cloud storage, or any transmission of PHI to a third party. Such a change is material and may require amendment of this Agreement before it is implemented.

### 3.4 Artificial intelligence and third-party model services

**(a) Prohibition.** Business Associate shall **not** disclose, transmit, submit, or otherwise make available any PHI to any AI Service, and shall not use PHI as input to any AI Service, **except** pursuant to a written amendment to this Agreement executed by both Parties that expressly identifies the AI Service provider by name and the categories of PHI involved.

**(b) Subcontractor status.** The Parties acknowledge that any AI Service provider that creates, receives, maintains, or transmits PHI on behalf of Business Associate is a Subcontractor and a business associate within the meaning of 45 CFR 160.103, and that Business Associate must execute a business associate agreement with that provider **before** any PHI is disclosed to it, as required by 45 CFR 164.502(e)(1)(ii) and 45 CFR 164.308(b)(2). Neither encryption of the PHI in transit or at rest, nor the provider's inability to view the PHI, nor a characterization of the provider as a mere conduit, relieves Business Associate of this obligation.

**(c) No training on PHI.** Business Associate shall not permit any AI Service provider, or any other Subcontractor, to use PHI to train, fine-tune, evaluate, or improve any model, or to retain PHI beyond the period necessary to return the requested output, except as expressly permitted by written amendment under Section 3.4(a).

**(d) Local models.** Artificial intelligence or machine learning components that execute entirely on the Clinical Workstation and transmit no data off that workstation are not AI Services for purposes of this Section, and are governed by Section 3.3.

**(e) Human review.** Where the Software generates draft clinical text, Business Associate shall design the Software so that no such text is finalized, signed, or entered into a clinical record without review by a qualified clinician.

### 3.5 De-identification

Business Associate may use PHI to create de-identified information in accordance with 45 CFR 164.514(a)-(c) for purposes of software development, testing, and product improvement, provided that de-identification is performed on the Clinical Workstation or otherwise within Covered Entity's environment where technically feasible. De-identified information created in accordance with the HIPAA Rules is not PHI and is not subject to the return-or-destroy obligation in Section 7(c). Business Associate shall not attempt to re-identify such information.

### 3.6 Management and administration

Business Associate may use PHI for the proper management and administration of Business Associate or to carry out its legal responsibilities. Business Associate may disclose PHI for such purposes only where the disclosure is Required By Law, or where Business Associate obtains reasonable assurances from the recipient that the information will remain confidential, will be used or further disclosed only as Required By Law or for the purpose for which it was disclosed, and that the recipient will notify Business Associate of any breach of confidentiality.

### 3.7 Authorization and scope of access

**(a)** Business Associate shall access Covered Entity's PACS, networks, or Clinical Workstations only pursuant to **written authorization from Covered Entity** identifying the authorized personnel, the systems in scope, the permitted activities, and the duration of the authorization.

**(b)** The Parties acknowledge that a physician who provides services to Covered Entity as an independent contractor, and who does not own or operate the PACS, **does not thereby have authority to grant Business Associate access** to Covered Entity's systems. Authorization under this Section must come from a person with authority to bind Covered Entity. `[FILL: name and title of Covered Entity's authorizing official, and the designated privacy or security contact]`

**(c)** Business Associate shall use only credentials issued to it by Covered Entity and shall not use, share, or operate under credentials issued to any physician or other individual.

---

## 4. Breach and Security Incident Reporting

**(a) Breaches of Unsecured PHI.** Business Associate shall report to Covered Entity any Breach of Unsecured PHI without unreasonable delay and in no event later than **five (5) business days** after Discovery. This period is shorter than the sixty (60) calendar day outer limit permitted by 45 CFR 164.410(b), and the Parties adopt it deliberately so that Covered Entity retains adequate time to meet its own obligations under 45 CFR 164.404 and 45 CFR 164.408.

**(b) Content.** The report shall include, to the extent known, the identification of each Individual whose Unsecured PHI has been, or is reasonably believed to have been, accessed, acquired, used, or disclosed, together with the other information Covered Entity requires under 45 CFR 164.404(c). Business Associate shall supplement the report promptly as further information becomes available.

**(c) Discovery.** A Breach shall be treated as discovered as of the first day on which it is known to Business Associate or, by exercising reasonable diligence, would have been known to Business Associate, consistent with 45 CFR 164.410(a)(2).

**(d) Other unauthorized uses or disclosures.** Business Associate shall report any other use or disclosure of PHI not provided for by this Agreement without unreasonable delay and in no event later than **five (5) business days** after becoming aware of it.

**(e) Security Incidents.** Business Associate shall report Security Incidents that result in unauthorized access to, or acquisition, use, disclosure, modification, or destruction of, electronic PHI without unreasonable delay and in no event later than **five (5) business days** after becoming aware of them. Unsuccessful Security Incidents that do not result in such access — including routine port scans, pings, and unsuccessful login attempts — shall be reported in aggregate `[FILL: quarterly, or on request]`, and this paragraph constitutes notice of their ongoing occurrence.

**(f) Cooperation.** Business Associate shall cooperate with Covered Entity's investigation, risk assessment under 45 CFR 164.402, and any notification obligations, and shall mitigate to the extent practicable any harmful effect known to it of a use or disclosure in violation of this Agreement, as required by 45 CFR 164.530(f).

**(g) Notice contact.** Reports under this Section shall be delivered to `[FILL: Covered Entity privacy/security officer name, title, email, phone]`.

---

## 5. Security Rule Obligations

**5.1 Direct applicability.** Business Associate acknowledges that Subpart C of 45 CFR Part 164 (the Security Rule) applies to it directly, and not merely by contract, with respect to electronic PHI it creates, receives, maintains, or transmits on behalf of Covered Entity.

**5.2 Safeguards.** Business Associate shall implement administrative, physical, and technical safeguards that reasonably and appropriately protect the confidentiality, integrity, and availability of such electronic PHI, including:

  **(a)** a risk analysis and risk management process under 45 CFR 164.308(a)(1)(ii)(A)-(B);
  **(b)** workforce security, access authorization, and termination procedures under 45 CFR 164.308(a)(3)-(4);
  **(c)** a security awareness and training program, and a sanction policy, under 45 CFR 164.308(a)(1)(ii)(C) and (a)(5);
  **(d)** unique user identification, audit controls, integrity controls, and person-or-entity authentication under 45 CFR 164.312(a)-(d);
  **(e)** encryption of electronic PHI in transit and at rest to standards not less protective than those specified in the Secretary's guidance under 45 CFR 164.402; and
  **(f)** retention of required documentation for six (6) years under 45 CFR 164.316(b)(2)(i).

**5.3 Scope-proportionate application.** The Parties acknowledge that, under the architecture described in Section 3.3, Business Associate does not maintain electronic PHI on its own systems, and that the obligations in Section 5.2 attach with respect to electronic PHI Business Associate actually creates, receives, maintains, or transmits. Nothing in this Section relieves Business Associate of any obligation that attaches upon a change of architecture under Section 3.3(c).

**5.4 Clinical Workstation encryption.**

  **(a)** Covered Entity shall be responsible for implementing and maintaining device and media controls and workstation security on Clinical Workstations under 45 CFR 164.310(b)-(d), including full-disk encryption.

  **(b)** Business Associate shall not enable any feature that writes Local Draft Data to a Clinical Workstation until Covered Entity has **confirmed in writing** that full-disk encryption is enabled and active on that workstation. `[FILL: confirmation of full-disk encryption status — UNRESOLVED as of the date of this draft]`

  **(c)** The Parties acknowledge the consequence of this allocation: where full-disk encryption meeting the Secretary's guidance is enabled, PHI on a lost or stolen Clinical Workstation is secured PHI and its loss is not a Breach of Unsecured PHI under 45 CFR 164.402; where it is not, such a loss is reportable.

**5.5 Subcontractor flow-down.** Business Associate shall obtain satisfactory assurances, in the form of a written business associate agreement meeting 45 CFR 164.314(a) and 45 CFR 164.504(e), from each Subcontractor before disclosing PHI to it, and shall remain responsible for its Subcontractors' performance. Business Associate shall provide Covered Entity, on request, a current list of Subcontractors that create, receive, maintain, or transmit PHI on Business Associate's behalf. `[FILL: initial Subcontractor list — state "None" if accurate]`

**5.6 Pattern of violation.** Consistent with 45 CFR 164.504(e)(1)(iii), if Business Associate knows of a pattern of activity or practice of a Subcontractor that constitutes a material breach of the Subcontractor's obligations, Business Associate shall take reasonable steps to cure the breach or end the violation and, if such steps are unsuccessful, terminate the arrangement if feasible.

---

## 6. Obligations of Covered Entity

**(a)** Covered Entity shall notify Business Associate of any limitation(s) in its Notice of Privacy Practices under 45 CFR 164.520, of any changes in or revocation of permission by an Individual to use or disclose PHI, and of any restriction on the use or disclosure of PHI that Covered Entity has agreed to or is required to abide by under 45 CFR 164.522, to the extent any of the foregoing may affect Business Associate's use or disclosure of PHI.

**(b)** Covered Entity shall not request Business Associate to use or disclose PHI in any manner that would not be permissible under Subpart E of 45 CFR Part 164 if done by Covered Entity, except as otherwise permitted by Sections 3.5 and 3.6.

**(c)** Covered Entity shall provide written authorization under Section 3.7 before Business Associate accesses any Covered Entity system, and shall issue and manage credentials for Business Associate personnel.

**(d)** Covered Entity shall be responsible for the security of its own PACS, networks, and Clinical Workstations, including the encryption confirmation contemplated by Section 5.4(b).

---

## 7. Term and Termination

**(a) Term.** This Agreement is effective as of the Effective Date and shall continue until terminated as provided herein, and thereafter until all PHI provided by Covered Entity to Business Associate, or created or received by Business Associate on behalf of Covered Entity, is destroyed or returned, or, if return or destruction is infeasible, protections are extended to such PHI in accordance with this Section.

**(b) Termination for cause.** Covered Entity may terminate this Agreement if it determines that Business Associate has violated a material term of this Agreement and Business Associate has not cured the violation within thirty (30) days of written notice. Covered Entity may terminate immediately where cure is not possible.

**(c) Termination for convenience.** Either Party may terminate this Agreement upon `[FILL: number]` days' prior written notice.

**(d) Obligations upon termination.** Upon termination for any reason, Business Associate shall return to Covered Entity or, if agreed to by Covered Entity, destroy all PHI received from Covered Entity, or created, maintained, or received by Business Associate on behalf of Covered Entity, that Business Associate still maintains in any form, and shall retain no copies. Business Associate shall additionally:

  1. instruct any Subcontractor holding such PHI to do the same, and obtain written confirmation;
  2. cause any Local Draft Data remaining on a Clinical Workstation to be cleared, or provide Covered Entity written instructions sufficient for Covered Entity to clear it; and
  3. certify completion in writing within thirty (30) days.

**(e) Infeasibility.** If return or destruction is infeasible, Business Associate shall notify Covered Entity in writing of the conditions making it infeasible, shall extend the protections of this Agreement to such PHI, and shall limit further uses and disclosures to those purposes that make return or destruction infeasible, for so long as Business Associate maintains the PHI.

**(f) Survival.** The obligations of Business Associate under this Section, and under Sections 2, 4, and 5, shall survive termination of this Agreement.

---

## 8. Miscellaneous

**(a) Regulatory references.** A reference in this Agreement to a section in the HIPAA Rules means the section as in effect or as amended.

**(b) Amendment.** The Parties agree to take such action as is necessary to amend this Agreement from time to time as is necessary for compliance with the HIPAA Rules and any other applicable law. No amendment is effective unless in writing and signed by both Parties.

**(c) Interpretation.** Any ambiguity in this Agreement shall be interpreted to permit compliance with the HIPAA Rules. In the event of a conflict between this Agreement and any underlying services agreement, this Agreement controls as to PHI.

**(d) No third-party beneficiaries.** Nothing in this Agreement shall confer upon any person other than the Parties any rights, remedies, obligations, or liabilities.

**(e) State law.** The Parties acknowledge that Texas law, including the Texas Medical Records Privacy Act (Tex. Health & Safety Code ch. 181), may impose obligations in addition to the HIPAA Rules, and that nothing in this Agreement limits either Party's obligations under applicable state law. `[FILL: confirm with counsel whether ch. 181 training and recordkeeping obligations attach to Business Associate under the architecture in Section 3.3]`

**(f) Governing law.** This Agreement shall be governed by the laws of the State of Texas and applicable federal law, without regard to conflict-of-laws principles. `[FILL: confirm — Covered Entity may require the law of its state of organization]`

**(g) Notices.** Notices shall be in writing and delivered to the addresses in the signature blocks, or to such other address as a Party designates in writing.

**(h) Entire agreement; counterparts.** This Agreement constitutes the entire agreement between the Parties regarding its subject matter and may be executed in counterparts, including by electronic signature, each of which shall be deemed an original.

**(i) Severability.** If any provision is held invalid, the remainder shall continue in effect.

---

## Signatures

**COVERED ENTITY**

`[FILL: exact legal entity name]`

By: ______________________________
Name: `[FILL]`
Title: `[FILL]`
Date: ____________________________
Address: `[FILL]`

**BUSINESS ASSOCIATE**

RGF Global Ventures, LLC

By: ______________________________
Name: **Richard Finlay**
Title: **Founder / Managing Member**
Date: ____________________________
Address: `[FILL: RGF business address]`

---

## Sources

All URLs retrieved **2026-09-15**. HTTP status recorded per source.

| Source | URL | Status |
|---|---|---|
| HHS, *Sample Business Associate Agreement Provisions* (published Jan. 25, 2013; page last reviewed June 16, 2017) | https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html | **200** via MCP fetcher; **403** to curl and WebFetch (bot filtering, not a dead link) |
| HHS OCR, *Business Associates* guidance | https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html | **200** via MCP fetcher; **403** to curl |
| HHS OCR, *Guidance on HIPAA & Cloud Computing* | https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html | **200** via MCP fetcher |
| 45 CFR 160.103 (definitions: business associate, covered entity) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103 | **200** |
| 45 CFR 164.504(e) (business associate contract requirements) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504 | **200** |
| 45 CFR 164.502 (uses and disclosures; 164.502(e) BA standard) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502 | **200** |
| 45 CFR 164.410 (breach notification by a business associate) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D/section-164.410 | **200** |
| 45 CFR 164.402 (definition of breach; secured/unsecured PHI) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D/section-164.402 | **200** |
| 45 CFR 164.306 (Security Rule general requirements) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306 | **200** |
| 45 CFR 164.308 (administrative safeguards; 164.308(b) BA contracts) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.308 | **200** |
| 45 CFR 164.514 (de-identification) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514 | **200** |

Regulatory text was retrieved from the eCFR versioner API at the 2026-09-01 point-in-time snapshot of Title 45, which is the authoritative current text.

**HHS's own caveat, reproduced because it governs this document:** the sample provisions "address only concepts and requirements set forth in the HIPAA Privacy, Security, Breach Notification, and Enforcement Rules, and alone may not be sufficient to result in a binding contract under State law... Reliance on this sample may not be sufficient for compliance with State law, and does not replace consultation with a lawyer or negotiations between the parties to the contract."

**This document is not legal advice.** It was prepared by a research agent, not an attorney. A Texas healthcare attorney should review it before signature.
