# Sherlock: Texas HB 300 (Health & Safety Code Ch. 181) verification
Date: 2026-11-03 · Analyst: Sherlock (read-only)

## Safe to say at lunch
1. Texas privacy law is broader than HIPAA: anyone who stores, processes or transmits patient data counts, including IT contractors like RGF.
2. Every employee who touches patient data must be trained within 90 days of hire and sign a record that is kept for 6 years.
3. Patients who ask in writing for their electronic record must get it electronically within 15 business days.
4. Patients must be told their data is shared electronically, and selling patient data is banned.
5. The Attorney General can fine up to $5k, $25k or $250k per violation, up to $1.5M a year for a pattern, and licensing boards can suspend or revoke.

**Correction to watch:** the statute does NOT require annual or every-2-years refresher training. Retraining is triggered only by a material change in law (within 1 year of it taking effect). Do not say "every two years."

## Sources
- Primary (official, current through the 2025 89th Leg. R.S.): https://tcss.legis.texas.gov/resources/hs/htm/hs.181.htm (Texas Legislative Council; fetched 2026-11-03). statutes.capitol.texas.gov now serves a JS app that would not render via fetch, so I used the Legislative Council's static copy of the same text.
- Cross-check mirror: texas.public.law section pages (verified May 26, 2025). Every quoted phrase below was string-matched against the official TCSS text.
- 2025 amendment: HB 4224 enrolled, https://capitol.texas.gov/tlodocs/89R/billtext/html/HB04224F.htm
- Amendment check: the only post-2015 amendment in the entire chapter's history notes is Acts 2025, 89th Leg., Ch. 650 (HB 4224), which ADDED 181.105. None of the five sections asked about changed after 2015.

## 1. Covered entity (181.001(b)(2)). Confidence: HIGH
> "Covered entity" means any person who: (A) for commercial, financial, or professional gain, monetary fees, or dues, or on a cooperative, nonprofit, or pro bono basis, engages, in whole or in part, and with real or constructive knowledge, in the practice of assembling, collecting, analyzing, using, evaluating, storing, or transmitting protected health information. The term includes a business associate, health care payer, governmental unit, information or computer management entity, school, health researcher, health care facility, clinic, health care provider, or person who maintains an Internet site; (B) comes into possession of protected health information; (C) obtains or stores protected health information under this chapter; or (D) is an employee, agent, or contractor of a person described by Paragraph (A), (B), or (C) insofar as the employee, agent, or contractor creates, receives, obtains, maintains, uses, or transmits protected health information.

Answer: yes. An IT contractor/developer that stores, transmits or processes PHI is covered three ways: (A) "storing, or transmitting" plus "information or computer management entity"; (B) mere possession; (D) contractor of a covered entity. Note 181.051 gives a partial exemption to HIPAA business associates/covered entities for some sections, but per 181.004(b) they still comply "subject to Section 181.051", and 181.101/154/153/201 still apply in practice (verify 181.051 text before stating exemptions in writing).

## 2. Training (181.101). Confidence: HIGH
> (a) Each covered entity shall provide training to employees of the covered entity regarding the state and federal law concerning protected health information as necessary and appropriate for the employees to carry out the employees' duties for the covered entity.
> (b) An employee of a covered entity must complete training described by Subsection (a) not later than the 90th day after the date the employee is hired by the covered entity.
> (c) If the duties of an employee of a covered entity are affected by a material change in state or federal law concerning protected health information, the employee shall receive training described by Subsection (a) within a reasonable period, but not later than the first anniversary of the date the material change in law takes effect.
> (d) A covered entity shall require an employee of the entity who receives training described by Subsection (a) to sign, electronically or in writing, a statement verifying the employee's completion of training. The covered entity shall maintain the signed statement until the sixth anniversary of the date the statement is signed.

- Who: all employees, scoped to their duties. Deadline: 90 days from hire.
- Interval: CHANGED. Original HB 300 (2011) required training at least every two years. SB 1609 (Acts 2013, 83rd Leg., Ch. 1367, eff. June 14, 2013) replaced that with the law-change trigger in (c). No change since.
- Documentation: signed statement (electronic or written), retained 6 years.

## 3. Electronic record access (181.102). Confidence: HIGH
> (a) Except as provided by Subsection (b), if a health care provider is using an electronic health records system that is capable of fulfilling the request, the health care provider, not later than the 15th business day after the date the health care provider receives a written request from a person for the person's electronic health record, shall provide the requested record to the person in electronic form unless the person agrees to accept the record in another form.

- 15 BUSINESS days, from a WRITTEN request. Applies to health care providers (not every covered entity) whose EHR can fulfill it. Format: electronic, unless the person accepts another form; (b) carves out 45 CFR 164.524 denials; (c) HHSC may recommend a standard format. Original HB 300 text was 15 business days too; the 2013 change was to 181.101, not here. Last amended 2015 (SB 219, agency renaming only).
- New and relevant (2025): 181.105, eff. Sept 1, 2025: "a covered entity shall prominently post on the entity's Internet website and at any entity facility detailed instructions for a consumer to: (1) request the consumer's health care records from the entity; (2) contact the disciplinary or licensing authority for the covered entity; and (3) file a consumer complaint". Exempts back-office processors (claims, data processing, billing) working for a provider. The imaging center itself must post this; RGF as a back-office vendor likely falls under the (b) exemption.

## 4. Notice of electronic disclosure (181.154) and sale ban (181.153). Confidence: HIGH
181.154(a):
> A covered entity shall provide notice to an individual for whom the covered entity creates or receives protected health information if the individual's protected health information is subject to electronic disclosure. A covered entity may provide general notice by: (1) posting a written notice in the covered entity's place of business; (2) posting a notice on the covered entity's Internet website; or (3) posting a notice in any other place where individuals whose protected health information is subject to electronic disclosure are likely to see the notice.

181.154(b)-(c): separate authorization per electronic disclosure is required, EXCEPT disclosures "to another covered entity ... for the purpose of: (A) treatment; (B) payment; (C) health care operations; or (D) performing an insurance or health maintenance organization function ... or (2) as otherwise authorized or required by state or federal law." (d) AG adopts a standard authorization form.

181.153(a):
> A covered entity may not disclose an individual's protected health information to any other person in exchange for direct or indirect remuneration, except [to another covered entity for treatment, payment, health care operations, or an insurance/HMO function] or (2) as otherwise authorized or required by state or federal law.

(b) remuneration for the insurance-function exception is capped at reasonable cost of preparing/transmitting.

## 5. Penalties (181.201, 181.202, 181.203). Confidence: HIGH
181.201(b):
> A civil penalty assessed under this section may not exceed: (1) $5,000 for each violation that occurs in one year, regardless of how long the violation continues during that year, committed negligently; (2) $25,000 for each violation that occurs in one year, regardless of how long the violation continues during that year, committed knowingly or intentionally; or (3) $250,000 for each violation in which the covered entity knowingly or intentionally used protected health information for financial gain.

- (a) AG may seek injunctive relief; (b) AG brings civil penalty actions.
- (b-1) 181.154 violations capped at $250,000/year if disclosure was only to another covered entity for a permitted purpose AND the court finds encryption, OR no further use/release by recipient, OR security policies including employee training were in place.
- (c) "pattern or practice": "a civil penalty not to exceed $1.5 million annually."
- (d) factors: "(1) the seriousness of the violation, including the nature, circumstances, extent, and gravity of the disclosure; (2) the covered entity's compliance history; (3) whether the violation poses a significant risk of financial, reputational, or other harm to an individual ...; (4) whether the covered entity was certified at the time of the violation as described by Section 182.108; (5) the amount necessary to deter a future violation; and (6) the covered entity's efforts to correct the violation."
- (e) For a LICENSED entity, the AG may sue for civil penalties only if the licensing agency refers it under 181.202(2).
- 181.202: licensed entities face "investigation and disciplinary proceedings, including probation or suspension by the licensing agency"; for egregious pattern or practice the agency may "(1) revoke the covered entity's license; or (2) refer the covered entity's case to the attorney general".
- 181.203: pattern or practice finding = exclusion from state-funded health care programs.
- 181.205: good-faith HIPAA/state compliance efforts are mitigating evidence.

## HIPAA preemption interaction. Confidence: MEDIUM-HIGH
- 181.001(a)/(b)(3): undefined terms take HIPAA meanings, frozen as of Sept 1, 2011 (later HIPAA rule changes are not auto-imported).
- 181.004: HIPAA covered entities must comply with HIPAA; Ch. 181 covered entities must comply with Ch. 181 (subject to 181.051 partial exemption).
- Under federal HIPAA preemption (45 CFR 160.203(b)), state law that is "more stringent" survives. Ch. 181's broader covered-entity definition, 90-day training, 15-business-day access (HIPAA allows 30 calendar days), and per-disclosure authorization are generally treated as more stringent and not preempted. That last point is analysis, not statute text; no court ruling was checked.
- 181.102(b) and 181.154(c)(2) expressly defer to HIPAA denials and "authorized or required by ... federal law" disclosures, which limits direct conflict.

## Gaps
- Did not pull 181.051 (partial exemption) text verbatim; read it before writing exemption claims into client deliverables.
- No Texas AG / HHSC enforcement guidance or case law reviewed.
