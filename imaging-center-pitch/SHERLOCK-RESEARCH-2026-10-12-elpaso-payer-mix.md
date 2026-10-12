# SHERLOCK RESEARCH — El Paso Payer-Mix Mechanics for a Greenfield Outpatient Imaging Center

**Prepared for:** Rick Finlay / RGF Global Ventures LLC
**Date:** 2026-10-12
**Mission:** Arm Rick for the room on the four-channel payer-mix objection (VA community care / TRICARE / commercial / Medicare) against the CMS-0057-F-anchored deck.
**Method:** Primary regulatory text (eCFR, Federal Register full text, CMS RVU files, Census API), agency manuals, live API capability probes. Every finding rated.
**Standing note:** This file is the only document created. The deck, speaking notes, runbook, leave-behind, and candidates doc were not touched (edit freeze respected).

---

## 1. BOTTOM LINE

1. **The four-channel objection is factually wrong on magnitude, and I can prove it with Census data.** In El Paso County, TRICARE/military-only coverage is **33,795 people (4.0%)** and VA-Health-Care-only is **5,037 (0.6%)** — combined **4.6%** of the 844,384-person insured-universe. Employer-based + direct-purchase is **320,020 (37.9% minimum)**. The military channels are a rounding error against commercial. **CONFIRMED** (ACS 2024 5-year, table B27010, El Paso County).
2. **Rick's working belief about VA community care is CORRECT** — it is referral-and-authorization driven, not approve/deny, and scope/expiry is the real operational risk. VA's own words: *"VA reimburses only for services explicitly authorized in the VA-approved referral."* **CONFIRMED**.
3. **But there is a brand-new VA fact Rick does not have, and it is 5 weeks old.** Effective **September 8, 2026**, VA **eliminated precertification entirely** and took the VA Precertification Portal (VAPP) offline. If Rick says "VA precertification" in that room, the partner who ran five imaging centers may or may not know this yet — but it is a live, checkable fact and saying it wrong is a credibility hit. **CONFIRMED** (VA Community Care, accessed 2026-10-12).
4. **TRICARE is even less of a prior-auth story than Rick assumed — and this is the finding most likely to be raised against him.** For **TRICARE Select, TRICARE For Life, Reserve Select, Retired Reserve, and Young Adult-Select**, advanced imaging (MRI/CT/PET) requires **no referral and no pre-authorization**. The pre-auth list is adjunctive dental, ABA, home health, hospice, transplants, ECHO, and some provisional-coverage services. Imaging is not on it. **CONFIRMED** (TRICARE.mil Referrals and Pre-Authorizations).
5. **CMS-0057-F does not touch TRICARE or VA — and I have the verbatim proof plus a quotable CMS admission.** The word "TRICARE" appears **zero times** in the entire 1.6 MB final rule. On VA/DoD, CMS wrote: *"These are independent agencies over which HHS has no authority."* **CONFIRMED** (89 FR 8758 full text).
6. **A bigger exposure than the military channels: CMS-0057-F does not cover commercial employer-sponsored plans either.** The impacted-payer list is MA, Medicaid FFS, CHIP FFS, Medicaid managed care, CHIP managed care, and QHP issuers **on the FFEs**. Commenters raised the "150 million Americans in employer-sponsored coverage" gap and CMS declined, citing lack of authority. **This is the real soft spot in the deck's central argument — not Fort Bliss.** **CONFIRMED**.
7. **Reimbursement falls the way Rick hoped, decisively.** VA pays Medicare rates (38 CFR 17.4035(a)); TRICARE's CMAC is Medicare-anchored and capped at Medicare; commercial runs **~254% of Medicare** nationally and **259% in Texas** (RAND 5.1). Commercial carries both the margin and the prior-auth burden. **The economics strengthen the deck's commercial focus.** **CONFIRMED/LIKELY as noted below.**
8. **Medicare FFS does not prior-auth outpatient diagnostic imaging — verified exhaustively, including the new 2026 program that applies to Texas.** The complete 42 CFR 419.83 list is 8 surgical/cosmetic categories. The new WISeR model *does* run in Texas from 2026-01-01, but its prior-auth list is skin substitutes, nerve stimulators, knee arthroscopy and similar — **no diagnostic imaging CPT**. **CONFIRMED**.

---

## 2. DOES THIS BREAK THE DECK?

### Verdict: **No. It strengthens the deck's commercial focus — but it exposes a different and more serious gap that Rick must pre-empt.**

**The four-channel objection collapses on its own numbers.** Rick framed the risk as "a meaningful share of volume may sit OUTSIDE the mechanism my argument depends on." The Census data says that share is **4.6%** for the two military channels. That is not meaningful. The deck's commercial focus is correct and the data defends it.

**However, I found a real problem that is NOT the one Rick was worried about.** CMS-0057-F's payer FHIR Prior Authorization API binding 2027-01-01 applies to MA, Medicaid, CHIP, and FFE QHPs — **not to employer-sponsored commercial plans**, which are the single largest block of El Paso's insured population (268,142 employer-based-only, 31.8%). So the rule does not automate prior auth for the majority of the commercial book that carries the margin. Fernando ran five imaging centers for twenty years; if he or a consultant pressure-tests the regulatory claim, **this** is where it breaks, not Fort Bliss.

**The good news: this does not damage the engagement thesis, only a too-strong version of the regulatory claim.** The burden is real, the margin is in commercial, and the operational fix (intake, documentation, benefit verification, referral/authorization tracking) pays for itself regardless of which payers are API-mandated. CMS-0057-F is a **tailwind and a direction-of-travel argument**, not the load-bearing wall. Rick should demote it from "the reason" to "the reason the window is now."

### Recommended qualifying sentences (use both; they are short and they inoculate)

> "CMS-0057-F binds Medicare Advantage, Medicaid, CHIP and exchange plans on January 1, 2027 — it does not reach employer-sponsored plans, TRICARE, or VA. So I'm not selling you a compliance deadline. I'm pointing out that the payers who move first set the standard the rest follow, and your build window lands exactly on that transition."

And if the four-channel objection is raised directly:

> "I looked that up, because you'd know better than I would. In El Paso County, TRICARE-only and VA-only coverage together are under five percent of the insured population — about thirty-nine thousand people out of eight hundred forty-four thousand. Commercial and Medicare are where the volume and the margin are. The military channels matter for front-office workflow, not for the business case."

---

## 3. WHAT RICK CAN SAY OUT LOUD

Every sentence below is CONFIRMED against a primary source cited in §9.

**On payer mix:**
- "El Paso County has about 870,000 residents. Of the 844,000 in the insurance-coverage universe, employer-based-only is about 268,000, direct-purchase-only about 52,000, Medicaid-only about 134,000, Medicare-only about 48,000, TRICARE-or-military-only about 34,000, and VA-only about 5,000."
- "TRICARE-only and VA-only together are 4.6 percent of covered residents."
- "El Paso County's uninsured rate is 21.6 percent — about 183,000 people. That's a bigger operational factor for a new center than the military channels are." *(This is a genuinely useful, non-obvious number for a greenfield pro forma — self-pay policy and point-of-service collection matter more here than in most markets.)*
- "Age 65-plus is 114,171 people, 13.1 percent of the county."
- "There are 47,646 veterans in El Paso County — 7.6 percent of the adult population."
- "Fort Bliss has 41,527 direct employees including 30,288 active-duty, and the Texas Comptroller counts 185,499 military retirees with installation access." *(Say "with installation access," not "living in El Paso" — see §4.)*

**On VA community care:**
- "VA community care is referral-and-authorization driven, not an approve-deny gate like commercial prior auth."
- "Texas is VA Community Care Network Region 4, and TriWest is the third-party administrator for Region 4."
- "VA pays community providers at the Medicare rate unless there's a contract-negotiated rate — that's in the regulation at 38 CFR 17.4035."
- "A VA episode of care is defined in regulation as lasting no longer than one calendar year, including follow-up and ancillary services."
- "VA's standing rule is that it reimburses only for services explicitly authorized in the referral. Anything outside the Standardized Episode of Care scope needs a Request for Service — VA Form 10-10172 — approved before you deliver the care."
- "Requests missing supporting documentation or a provider signature are denied. VA says so on the page."
- "VA processes a Request for Service in three business days."
- "As of September 8, 2026, VA no longer requires precertification, and the precertification portal is offline. The referral and the SEOC are what govern now."

**On TRICARE:**
- "El Paso is TRICARE West. TriWest Healthcare Alliance has been the West Region contractor since January 1, 2025."
- "For TRICARE Select and TRICARE For Life, MRI, CT and PET need no referral and no pre-authorization."
- "For TRICARE Prime, non-active-duty, specialty care and some diagnostic services need a PCM referral, and the regional contractor issues the referral and pre-authorization together."
- "For active duty on Prime, it's a referral for anything the PCM doesn't provide, plus pre-authorization for all specialty care."
- "If a Prime enrollee self-refers or goes out of network without a referral, they're on the point-of-service option and their out-of-pocket cost goes up. That becomes a front-desk conversation, which is a staffing and scripting problem, not a payer problem."
- "The TriWest transition in 2025 was rough enough that DHA waived referral approval for West Region Prime enrollees from January 25, 2025. That waiver expired June 30, 2025, and patients using it had to get new referrals before October 1, 2025. Standard rules apply now."

**On CMS-0057-F:**
- "The rule's impacted payers are Medicare Advantage organizations, state Medicaid fee-for-service, state CHIP fee-for-service, Medicaid managed care plans, CHIP managed care entities, and QHP issuers on the federally-facilitated exchanges."
- "The Prior Authorization API compliance date is January 1, 2027 for MA and state Medicaid and CHIP FFS."
- "The prior-authorization *process* requirements — decision notices with a specific denial reason, response timeframes, public metrics reporting — were already due January 1, 2026."
- "TRICARE is not mentioned once in the final rule. On VA and DoD, CMS wrote that these are independent agencies over which HHS has no authority."
- "The rule does not reach employer-sponsored or other commercial plans. CMS said it lacks the authority and encouraged voluntary adoption."

**On reimbursement (El Paso-specific, computed from the CMS October 2026 RVU file):**
- "Medicare in El Paso — that's the Rest of Texas locality — pays about $188 global for an MRI brain without contrast, $184 for MRI lumbar, $128 for a CT chest, and $121 for a screening mammogram with CAD."
- "On the technical component alone, which is what the center earns if the read is separate: about $121 MRI brain, $117 MRI lumbar, $79 CT chest, $87 screening mammo."
- "The CY2026 Medicare conversion factor is $33.4009, and Rest of Texas GPCIs are work 1.000, practice expense 0.949, malpractice 0.903."
- "TRICARE's allowable is the CMAC, and the regulation anchors it to Medicare — overpriced codes get ratcheted down toward the Medicare fee, and CMS may raise the national CMAC only to a level not greater than the Medicare rate. Localities use the same geographic adjustment factors as Medicare."
- "RAND's latest price transparency study puts commercial at 254 percent of Medicare nationally for hospital inpatient and outpatient combined, and Texas employers at 259 percent."
- "Medicare fee-for-service does not require prior authorization for outpatient diagnostic imaging. The regulation's full list is blepharoplasty, botulinum toxin, panniculectomy, rhinoplasty, vein ablation, cervical fusion with disc removal, implanted spinal neurostimulators, and facet joint interventions — and it applies to hospital outpatient departments, not freestanding centers."
- "There's a new CMS model called WISeR that started January 1, 2026 and does run in Texas — but its prior-auth list is skin substitutes, nerve stimulators, knee arthroscopy and similar. No diagnostic imaging."

---

## 4. WHAT RICK MUST NOT SAY

These are UNVERIFIED or subtly wrong. Do not reach for them under pressure.

| Do NOT say | Why | Say instead |
|---|---|---|
| Any **percentage of the imaging center's volume** by channel | I could not establish payer mix for imaging *volume*. Census measures **coverage of residents**, not utilization. Imaging utilization skews heavily older and sicker, so Medicare's volume share will exceed its 5.7% coverage share by a wide margin. No defensible conversion factor exists. | "Coverage shares in the county are X. Volume will skew older than coverage does — you'd know the conversion better than I would." *(Hands the expertise to Fernando. Good room dynamics.)* |
| "185,499 military retirees **live in El Paso**" | The Texas Comptroller says retirees "accessing the installation, camp facilities and resources" — a catchment that extends well beyond the county, and the same series said "over 80,000" in 2023, a jump that signals a definitional change, not population growth. | "The Comptroller counts 185,499 military retirees with Fort Bliss installation access." |
| A **Fort Bliss dependent/beneficiary count** | Not established. The Fort Bliss CDP figure (11,419 residents, of whom 2,206 under 18) counts only on-post residents and is not the assigned population or the TRICARE beneficiary count. DMDC's report endpoints 404'd. | Cite active duty (30,288) and direct employees (41,527) only. |
| An **El Paso VA enrollee count** | Not published on any VA page I could reach; data.va.gov's package_search 404'd. | "El Paso has a VA Health Care System; I don't have the enrollee count." |
| **Medicare Advantage penetration in El Paso** | Not established — CMS's MA state/county penetration file is not in the data.cms.gov catalog API and the landing page 404'd. **This one actually matters**: MA *is* covered by CMS-0057-F, so MA penetration determines how much Medicare volume the rule reaches. Flag it as a diligence item, don't guess it. | "MA penetration is the number that decides how much of your Medicare book the new rule touches. I'd pull that before we price Phase 2." |
| "Commercial pays **2.5x Medicare for imaging**" | RAND's 254% is hospital inpatient+outpatient facility+professional. For a **freestanding** center the relevant comparators are lower: associated professional services **184%**, ASCs **171%**. Hospital outpatient facility was 279%. Quoting 254% for a freestanding imaging center overstates it. | "RAND puts commercial at 254 percent of Medicare for hospital services and 171 percent for ambulatory surgery centers. A freestanding imaging center sits in that lower band, and your actual number is whatever you negotiate." |
| A **VA referral expiry in days** (e.g. "90 days," "180 days") | The regulation defines the **episode of care** as ≤1 calendar year (38 CFR 17.4005). Specific SEOC durations and referral validity windows are set per-SEOC and in TPA handbooks I could not retrieve as primary text. Do not invent a day count. | "A VA episode of care is capped at one calendar year by regulation, and the specific SEOC sets the scope. The expiry discipline is what protects the claim." |
| "VA requires **precertification**" | **False as of September 8, 2026.** | "VA dropped precertification in September 2026; the referral and SEOC govern." |
| "TRICARE requires **prior auth for MRI/CT/PET**" | False for Select / For Life / Reserve Select / Retired Reserve / Young Adult-Select. Only Prime involves referral, and the pre-auth list excludes imaging. | Use the plan-by-plan language in §3. |
| "CMS-0057-F **requires providers** to use the FHIR APIs" | It does not. It obligates **payers** to build and maintain them. Provider-side measures are MIPS/Promoting Interoperability reporting for eligible clinicians and hospitals. | "The rule makes the payers build the APIs. Whether you can use them depends on your software vendor, which is exactly the integration question." |
| "VA/DHA have a **FHIR prior-auth API** you can integrate with" | **Verified false today.** VA's production FHIR R4 API exposes 19 resources — none are authorization/referral transaction resources. | See §7-Q4 for the exact resource list and what automation actually looks like. |
| Any **Texas-imaging-specific commercial multiple** | RAND Texas 259% is all hospital services, not imaging-specific. No imaging-specific Texas multiple established. | — |

---

## 5. Q1 — PAYER MIX SHARES

### Verdict: A defensible **coverage-share** estimate exists and I computed it. A defensible **imaging-volume-share** estimate does **not** exist. I give the bounding facts and refuse the conversion.

### El Paso County coverage shares — CONFIRMED

Source: Census ACS 2024 5-year, table **B27010** (Types of Health Insurance Coverage by Age), geography `050XX00US48141` (El Paso County, TX), retrieved via `data.census.gov` access API 2026-10-12. Universe: civilian noninstitutionalized population = **844,384**.

| Channel (single-type coverage) | Count | Share of 844,384 |
|---|---|---|
| Employer-based only | 268,142 | 31.8% |
| **Uninsured** | **182,797** | **21.6%** |
| Medicaid / means-tested only | 133,674 | 15.8% |
| Direct-purchase only | 51,878 | 6.1% |
| Medicare only | 48,366 | 5.7% |
| **TRICARE / military only** | **33,795** | **4.0%** |
| **VA Health Care only** | **5,037** | **0.6%** |
| *Commercial floor (employer + direct, single-type)* | *320,020* | *37.9%* |
| *Military channels combined* | *38,832* | *4.6%* |

Multi-type combinations (e.g. 10,906 employer+Medicare and 7,504 direct+Medicare at 65+, and 18,480 "other combinations" at 65+) are excluded from the single-type rows, so commercial and Medicare are both **understated** — which only widens the gap versus the military channels.

**Age 65+ detail (B27010, universe 112,140):** Medicare-only 42,089; Medicare+Medicaid 23,801; employer+Medicare 10,906; direct+Medicare 7,504; other combinations 18,480; **TRICARE-only at 65+ just 52** and **VA-only just 84** — because at 65 retirees move to TRICARE For Life with Medicare primary. **This is an important mechanical point: the large retiree population does not present as a TRICARE prior-auth problem; it presents as Medicare-primary.**

### Supporting demographics — CONFIRMED

- Total population **870,779**; under 18 **226,840 (26.1%)**; 18+ **643,939 (73.9%)**; **65+ 114,171 (13.1%)**; 85+ 13,366 (1.5%). *(ACS 2024 5-yr DP05)*
- **Veterans 47,646 — 7.6%** of the 624,740 civilian population 18+. *(ACS 2024 5-yr S2101)*
- Insured 661,587 (78.4%); **uninsured 182,797 (21.6%)**. *(ACS 2024 5-yr S2701)*
- Fort Bliss: **41,527 direct employees**, **30,288 active-duty** (Army 28,040; Navy 1,227; Air Force 937; plus Marines), **185,499 military retirees with installation access**; total direct+indirect employment 121,220. *(Texas Comptroller, Texas Military Installations 2025)*
- Fort Bliss CDP (on-post residents only): 11,419 total; 2,206 under 18; 9,213 adults. *(ACS 2024 5-yr DP05, place 4827348)* — **do not use as the assigned or beneficiary population.**

### Why I will not give a volume percentage — UNVERIFIED by design

Three unbridgeable gaps:
1. **Coverage ≠ utilization.** Imaging utilization rises steeply with age and comorbidity. Medicare's 5.7% coverage share will substantially understate its volume share; the 21.6% uninsured will substantially overstate theirs (they under-utilize elective imaging).
2. **Active duty are largely outside B27010's universe and outside the center's likely book.** On-post/barracks populations are institutional; and active-duty Prime care is directed to William Beaumont Army Medical Center first. Direct-care capture suppresses community referral.
3. **No El Paso imaging-specific utilization data exists in any source I could reach.** Any percentage I produced would be a fabrication dressed as analysis — and Fernando, who ran five El Paso centers for twenty years, has the real number in his head. **That asymmetry is an asset: ask him.**

---

## 6. Q2 — VA COMMUNITY CARE REFERRAL AND AUTHORIZATION MECHANICS

### Rick's belief: CONFIRMED, with one material update he does not have.

> **Rick's working belief:** "referral-and-authorization driven rather than approve/deny, with referral expiry and scope limits as the real operational risk."
>
> **Verdict: CORRECT on all three points.** And as of 2026-09-08 it is *more* correct than it was, because VA deleted the one approve/deny-style gate it had (precertification).

### Who authorizes — CONFIRMED

**VA authorizes, not the TPA.** 38 CFR 17.4020(a): a covered veteran may *"have **VA** authorize the veteran to receive an episode of care... when **VA** determines such care or services are clinically necessary."* The TPA administers the network, processes claims, and pays on VA's behalf. The referral originates in VA.

- Eligibility gates are in **38 CFR 17.4010** — the drive-time/wait-time standards at **17.4040** are the operative ones for imaging: **specialty care = cannot schedule within 60 minutes average drive time AND within 28 days.** (Primary/mental health: 30 minutes / 20 days.)
- **17.4010(d):** eligibility decisions go to VA's clinical appeals process and **may not** be appealed to the Board of Veterans' Appeals.

### TPA for El Paso — CONFIRMED, and this is the currency check Rick asked for

**Texas is CCN Region 4. TriWest Healthcare Alliance is the TPA for Regions 4 and 5. Optum holds Regions 1–3.**

> *"CCN is made up of five regional networks of community providers that are managed by third-party administrators (TPAs) on behalf of VA. Optum serves as TPA for regions 1-3, while TriWest serves as the TPA for regions 4 and 5."*
> — VA Community Care Network page, accessed 2026-10-12

Region 4 = American Samoa, Arizona, California, Colorado, Guam, Hawaii, Idaho, Montana, New Mexico, Nevada, Northern Mariana Islands, Oregon, **Texas**, Utah, Washington, Wyoming.
Provider enrollment: `joinournetwork.triwest.com` (preferred), ProviderServices@TriWest.com, 877-CCN-TRIW (877-226-8749).

**Note the symmetry Rick can use:** TriWest is the TPA for **both** VA Region 4 **and** TRICARE West. One counterparty, two programs, two entirely separate rule sets and portals. That is a real operational insight and it is the kind of thing that lands with an operator.

### ⚠️ PRECERTIFICATION ELIMINATED 2026-09-08 — CONFIRMED, 5 weeks old

> *"**Precertification no longer required.** Effective September 8, 2026, VA no longer requires precertification before providing authorized care for Veterans. The VA Precertification Portal (VAPP) is now offline. Continue delivering care as authorized under the Veteran's referral and SEOC. This change has no impact on claims processing or payment. Follow the Request for Service (RFS) process to request care the authorization or SEOC doesn't cover."*
> — VA Community Care, Precertification requirements, accessed 2026-10-12

**Implication for the deck:** the VA channel just got *simpler*, and the entire remaining risk concentrated into exactly the two things Rick already identified — **scope** and **expiry**. His thesis survived a regulatory change that invalidated the alternative framing.

### Scope limits — CONFIRMED, with the operative language

This is the heart of the VA risk and VA states it plainly:

> *"**Authorized services only.** VA reimburses only for services explicitly authorized in the VA-approved referral. Providers should confirm that all care delivered falls within the scope of the referral."*
> — VA fee schedules page, accessed 2026-10-12

SEOC mechanics:
> *"SEOCs provide a high-level summary of the typical scope of care and commonly associated billing codes for a referral. The billing codes listed on a SEOC are not intended to represent every service that may be provided. If a billing code is not listed on a SEOC, determine whether the service is within the scope and intent of the authorized referral... **Services within scope** may be billed using appropriate codes, even if the specific code is not listed. **Services outside scope** of the authorized referral require additional VA approval before care is provided."*
> — VA Standardized Episodes of Care, accessed 2026-10-12

**Does an authorization for one modality cover a follow-up?** Answer: **only if it is within the scope and intent of the referring provider's order, and within the episode-of-care window.** It is a judgment call the provider makes and bears the risk on — which is precisely why a documented scope-check at intake is worth paying for. If outside scope: RFS before delivering care.

### Expiry — CONFIRMED at the regulatory level; specific day-counts UNVERIFIED

**38 CFR 17.4005:** *"**Episode of care** means a necessary course of treatment, including follow-up appointments and ancillary and specialty services, which lasts **no longer than 1 calendar year**."*

RFS is explicitly the expiry remedy: an RFS is required when requesting *"Additional visits or time beyond what is authorized in an active referral (**for example, when an authorization is expiring**)."*

**UNVERIFIED:** per-SEOC durations and referral validity windows shorter than one year. These live in SEOC definitions and TPA handbooks I could not retrieve as primary text (the SEOC Billing Code List sits behind an AMA CPT license click-through). **Do not state a day count.**

### Documented operational failure modes → unpaid or rejected claims — CONFIRMED

Directly from VA's own pages. This list is the engagement's VA-channel value proposition:

1. **Care delivered outside referral scope** → not reimbursed. *"VA reimburses only for services explicitly authorized in the VA-approved referral."*
2. **RFS missing documentation or signature** → *"Requests that are missing supporting documentation or provider signature **will be denied**."* Required: provider notes, care plans, lab results and/or radiology reports, with wet or electronic signature, **one form per service request**.
3. **Care delivered before RFS approval** → *"Services outside scope of the authorized referral require additional VA approval **before care is provided**."*
4. **Authorization expiry with no RFS in flight** → RFS must be submitted *in advance*; the DME-rental analogue is explicit: *"Rentals beyond the initial 30 days require an RFS submitted in advance to avoid disruption in service."*
5. **Non-reimbursable codes** → VA maintains a Non-Reimbursable Codes List of procedure codes deemed ineligible for payment.
6. **Rate-basis confusion** → *"Reimbursement rates do not imply coverage. A published rate, whether from CMS or VAFS, does not imply that a service is covered."*
7. **Billing above contract** → *"Depending on the contract, VA may pay whichever is less: the agreed-upon rate or the amount the provider bills."*
8. **Referral-type variance** → *"Reimbursement rates may differ depending on how care was approved."*

**RFS turnaround:** 3 business days. **Submission channels:** HSRM, secure email, direct messaging, fax (electronic or traditional), mail if the facility permits. **Form:** VA Form 10-10172.
**Urgent care comparator (shows VA's documentation clock discipline):** medical documentation within **30 calendar days**; claim within **180 calendar days** to the regional TPA.

---

## 7. Q3 — TRICARE WEST PRIOR-AUTH AND REFERRAL RULES FOR ADVANCED IMAGING

### Contractor currency check — CONFIRMED

**TRICARE West Region contractor = TriWest Healthcare Alliance, health care delivery began January 1, 2025.** East = Humana Military. TRICARE For Life = WPS Government Services. Pharmacy = Express Scripts.

- TRICARE.mil Regions page, **Last Updated 9/29/2026**, lists TriWest as West contractor; beneficiary portal `tricare-bene.triwest.com`.
- Six states moved from East to West effective 2025-01-01. Humana-era provider agreements in transitioning states *"will be assigned to TriWest with an effective date of January 1, 2025."* (TriWest provider contracting Q&A — **LIKELY**, contractor-published.)

### Transition issues — CONFIRMED, and fully resolved on paper

DHA acknowledged, verbatim: payment set-up, call center wait times, network provider availability, **processing of referrals and authorizations**, and TriWest beneficiary portal access.

Timeline:
- **2025-01-25** — DHA waives the requirement to obtain approval for referrals to outpatient specialty care for West Region Prime enrollees. Specialty providers need not wait for TriWest approval of a PCM-issued referral.
- Extended (payment deadline and waiver extensions to April 30 per the DHA article's March 26 update).
- **2025-06-30** — waiver **expired**. (CMA: *"Providers must now follow standard TRICARE requirements for all new outpatient services."* — **LIKELY**, credible secondary, corroborated by TriWest and DHA.)
- **2025-10-01** — patients who used the waiver between Jan 1 and Jun 30, 2025 needed a **new referral to a network specialist** to continue care.
- TriWest hired 400+ additional CSRs and added call-back. *"Over 97% of West Region beneficiaries have access to all provider specialties."* Network includes *"almost all of Humana Military's network in the six transition states"* and *"over 80% of the providers that were in HNFS' network."*

**Residual as of 2026-10-12:** no active waiver; standard rules apply. A **DEERS outage Oct 9–11, 2026** was banner-posted on tricare.mil during this research — beneficiaries *"may be unable to update contact information, verify eligibility, or complete enrollment actions."* **Relevant operational color: eligibility verification for this channel has a real downtime mode, which argues for same-day eligibility capture and a documented fallback.**

### Referral and pre-auth requirements by plan — CONFIRMED

Source: TRICARE.mil, *Referrals and Pre-Authorizations*, accessed 2026-10-12.

| Plan / category | Referral? | Pre-authorization? |
|---|---|---|
| **Prime — active duty (ADSM)** | **Yes**, for any care the PCM doesn't provide — urgent, routine, preventive, specialty. Without one, *"you'll pay out of pocket."* | **Yes, for all specialty care.** Plus a **fitness-for-duty review** for certain care. |
| **Prime — all others (ADFM, retiree, retiree family)** | **Yes**, for *"specialty care and some diagnostic services."* PCM works with the regional contractor. Without one → **point-of-service option**. | **Yes, for all specialty care.** *"Your PCM gets your referral and pre-authorization at the same time."* |
| **Select, Select Overseas, Reserve Select, Retired Reserve, Young Adult-Select, TRICARE For Life** | **No** — *"Only applied behavior analysis requires a referral."* | **Only** for: adjunctive dental, ABA, home health, hospice, transplants (all solid organ and stem cell), all ECHO services, some Provisional Coverage Program services. **MRI / CT / PET are NOT on this list.** |

**Beneficiary-category mapping for El Paso:** active duty → Prime (strictest, and directed to William Beaumont first). ADFM → usually Prime, sometimes Select. Working-age retirees and their families → Prime or Select. **Retirees 65+ → TRICARE For Life with Medicare primary → no referral, no pre-auth, Medicare rules govern.** Given B27010 shows only 52 TRICARE-only people at 65+ in the county, the retiree population is overwhelmingly a **Medicare-primary** book.

**Services exempt from PCM referral under Prime (network providers, in-region):** preventive care; outpatient mental health visits.

### Patient-financial exposure — the front-office conversation — CONFIRMED

> *"If you get care from a non-network provider (or a network provider outside of your region) without a referral from your PCM, you're using the point-of-service option. You'll have higher out-of-pocket costs."*

Non-network provider protections under TRICARE — **network providers cannot**:
- Ask a beneficiary to sign a document making them pay for **authorized** services;
- Ask them to sign a document making them pay for any part of a service TRICARE doesn't cover;
- Refuse to see them for declining to sign.

**Operational translation for the pitch:** if the center is in-network, it **cannot** paper over a coverage gap with a patient waiver. The only defense is getting the referral and authorization right before the scan. That is an intake-process problem — i.e., exactly what Rick is selling. **This is a strong, concrete, non-speculative argument.**

**Balance billing:** non-participating providers may not balance bill above the limit, which is *"the same percentage as the Medicare limiting charge percentage for nonparticipating physicians"* (32 CFR 199.14(j)(1)(i)(C)).
**Prime + non-participating provider:** allowable = CMAC **plus** balance-billing amount up to the limit (199.14(j)(1)(i)(D)).

**Authorization expiry — CONFIRMED, quotable:**
> *"Get care before the authorization expires. Otherwise, you'll need to get the care reapproved."* Patients must *"Book your appointment with the provider listed in the authorization letter."*

**Portal:** West Region referrals/auths live only in the TriWest portal. *"Referral and authorization information isn't available on the MHS GENESIS Patient Portal."* — **a concrete, citable fragmentation fact.**

---

## 8. Q4 — IS EITHER MILITARY CHANNEL REACHABLE BY THE FHIR/API AUTOMATION STORY?

### Short answer: **No. Neither. And the exclusion also extends to commercial employer plans, which is the bigger finding.**

### CMS-0057-F regulated entities — CONFIRMED verbatim

From the SUMMARY of 89 FR 8758 (CMS-0057-F, published 2024-02-08, effective 2024-04-08):

> *"This final rule will improve the electronic exchange of health care data and streamline processes related to prior authorization through new requirements for **Medicare Advantage (MA) organizations, state Medicaid fee-for-service (FFS) programs, state Children's Health Insurance Program (CHIP) FFS programs, Medicaid managed care plans, CHIP managed care entities, and Qualified Health Plan (QHP) issuers on the Federally-facilitated Exchanges (FFEs)**. This final rule will also add new measures for eligible hospitals and critical access hospitals (CAHs) to report under the Medicare Promoting Interoperability Program and for MIPS eligible clinicians..."*

§II.D.4 "Impacted Payers" confirms the same six categories.

**Compliance dates — CONFIRMED:**
- **Prior Authorization API:** *"by January 1, 2027, for MA organizations and state Medicaid and CHIP FFS programs; by the rating period beginning on or after January 1, 2027, for Medicaid managed care plans and CHIP managed care entities; and for plan years beginning on or after January 1, 2027, for QHP issuers on the FFEs."*
- **Prior authorization *process* requirements** (decision notices with specific denial reason; response timeframes; public metrics) — **January 1, 2026**. *(Already in force. Rick can say the first wave has already landed.)*
- Patient Access API PA-data inclusion: 2027. Payer metrics reporting to CMS: from 2026-01-01.
- Name change: the proposed "PARDD API" was finalized simply as the **"Prior Authorization API"** — *"This name change alone does not indicate any changes to the requirements or standards."*

### TRICARE: not covered — CONFIRMED by exhaustive text search

**The string "TRICARE" occurs ZERO times in the full text of 89 FR 8758** (1,608,552 characters, searched 2026-10-12). "Veterans Affairs" also zero. The only VA/DoD references are two commenter requests and CMS's responses.

### VA: not covered — CONFIRMED, with the quote Rick should memorize

> *"Comment: Multiple commenters recommended that CMS work with ONC and other Federal agencies, such as the Veterans Administration (VA), the U.S. Department of Defense (DoD), and other government payers, to bring additional data into the interoperability universe.*
> *Response: We continue to work with ONC and agencies across the Federal Government to move toward a fully interoperable health care system. We are committed to sharing any insights and best practices from our experience working with impacted payers with other agencies that provide health care coverage to inform their own interoperability goals. **These are independent agencies over which HHS has no authority.**"*

A second commenter specifically *"recommended that CMS work with the DoD and the VA to implement Payer-to-Payer APIs."* CMS gave a non-committal response.

### ⚠️ Commercial employer-sponsored plans: ALSO not covered — CONFIRMED. This is the deck's real exposure.

> *"Comment: ... Multiple commenters expressed their concern that **private payers, commercial plans, and employer-sponsored plans would not be subject to the rule requirements**. A commenter expressed concern regarding the **150 million Americans who are in employer-sponsored coverage**, who may not have access to the benefits of the proposed rule.*
> *Response: We appreciate commenters supporting implementation of the policies by private payers, commercial plans, and employer-sponsored plans. **However, we proposed to impose these requirements under our authority to regulate issuers in the Exchanges that CMS operates, which does not apply to health insurance issuers and group health plans outside the FFEs.** There is nothing prohibiting those payers from implementing the provisions in this final rule voluntarily..."*

Also excluded: stand-alone dental plans (SADPs) on the FFEs; FF-SHOP-only QHP issuers; public-sector COBRA group health plans (*"we did not make any proposals regarding public sector COBRA plans, so they are not included as impacted payers"*).

**Why this matters more than the military channels:** El Paso County has **268,142 employer-based-only** covered lives (31.8%) versus **38,832** in both military channels combined (4.6%). The rule misses a block **seven times larger** than the one Rick was worried about. Pre-empt it (see §2).

### Medicare FFS: not directly covered — CONFIRMED

> *"**Although these requirements do not directly pertain to Medicare FFS**, we want to ensure that people with Medicare can benefit from the policies in this final rule... **We intend for the Medicare FFS program to be a market leader on data exchange**, including through the Provider Access, Payer-to-Payer, and Prior Authorization APIs, and therefore we solicited comments on how these proposals could apply to Medicare FFS... We did not make any policy proposals regarding this effort, but we are considering comments as we plan our roadmap for implementation."*

**Usable framing:** Medicare FFS is a stated intention without a binding date. That is a legitimate "direction of travel" argument and it is honest.

### Does VA have its own FHIR/API referral or authorization interface? — CONFIRMED NO (probed live)

I queried VA's production FHIR capability statement directly on 2026-10-12.

**`https://api.va.gov/services/fhir/v0/r4/metadata`** → HTTP 200. `fhirVersion: 4.0.1`, publisher **Department of Veterans Affairs**, `version: 14.0.98`, `date: 2026-10-12T21:25:46Z`, SMART-on-FHIR, OAuth2 at `api.va.gov/oauth2/*`.

**All 19 supported resources:**
`AllergyIntolerance, Appointment, Binary, Condition, Device, DeviceRequest, DiagnosticReport, DocumentReference, Encounter, Immunization, Location, Medication, MedicationRequest, Observation, Organization, Patient, Practitioner, PractitionerRole, Procedure`

**What is absent is the finding:** no `ServiceRequest` (the FHIR resource for a referral), no `CoverageEligibilityRequest`/`Response`, no `Claim`/`ClaimResponse`, no `Task`, no `Coverage`, no `Contract`. **VA's FHIR API is a clinical-data read API. It cannot carry a referral or an authorization transaction.**

Also probed: `sandbox-api.va.gov/services/community-care/v0/eligibility/search` → **HTTP 401** (exists, gated). This is a VA **community-care-eligibility** lookup — i.e. "is this veteran eligible for community care," **not** an authorization or referral API, and not a claim-safety mechanism. `api.va.gov/services/community-care/v1/eligibility` → 404. `provider-directory/v0/r4/metadata` → 404.

### What VA actually offers a small community provider in 2026 — CONFIRMED

Per VA's Care Coordination Tools page (accessed 2026-10-12):

| Tool | What it is | Automation reality |
|---|---|---|
| **HSRM** (HealthShare Referral Manager) | *"secure, **web-based system**"* to receive referrals/auths, submit RFS online, view clinical summary | **Portal.** No API. Gated behind a CCN/VCA agreement, NPI listed in the agreement, and **mandatory training** (2-hour live webinar, 2-part extended, or self-paced eLearning via VHA TRAIN) before access. |
| **EPS** (External Provider Scheduling) | VA books directly into the provider's scheduling system; *"includes the referral authorization number"* | **The one genuine integration.** *"EPS works with over 150 EHR and scheduling systems."* **Optional** and free. Provider controls which blocks VA sees. **Explicitly cannot retrieve records.** |
| **VHIE** | Bi-directional clinical information sharing | Document exchange, not authorization. |
| **Azure RMS** | *"securely exchange information with community providers using **encrypted email**"* | Email. |

And the tell, verbatim: *"Records and medical history are delivered through your preferred method — **fax, secure email**, Veterans Health Information Exchange or HealthShare Referral Manager."*

**Fax is still a first-class VA channel in 2026.** RFS submission channels are *"HSRM, Secure email, Direct messaging, Fax (electronic or traditional), Mail."*

### Does DHA/TRICARE have a provider-facing FHIR auth API? — UNVERIFIED (leaning no)

I found **no** DHA or TriWest provider-facing FHIR prior-authorization or referral API. TRICARE's referral/authorization surface is the **region-specific contractor portal** (`tricare-bene.triwest.com` for West beneficiaries), and TRICARE.mil states referral/auth data *"isn't available on the MHS GENESIS Patient Portal."* MHS GENESIS is DoD's Oracle Health EHR and has patient-facing FHIR, but I could not establish a provider-facing authorization API. **Rated UNVERIFIED rather than CONFIRMED-absent**, because I could not retrieve the TriWest provider handbook as primary text (`tricare-west.com` returned a connection failure). **If this matters to the engagement scope, it is a one-phone-call diligence item: ask TriWest provider services whether an X12 278 or API submission path exists.**

### Do clearinghouses re-intermediate these channels? — PARTIALLY VERIFIED

- **Standards exist.** CMS-0057-F notes HIPAA administrative-simplification transaction standards and the ASETT complaint portal; **X12 278** is the HIPAA standard for referral certification and authorization. A clearinghouse route is therefore *structurally* plausible for TRICARE, which is a HIPAA-covered payer.
- **VA community care is different in kind.** VA is not operating as a HIPAA-standard commercial payer for authorization purposes; authorization is a VA clinical referral + SEOC, issued through HSRM. **No clearinghouse 278 path to VA authorization was found.** Eligibility/claim-status for VA runs through the TPA.
- **UNVERIFIED:** which specific clearinghouses carry TRICARE West 278 transactions today, and at what fill rate. Do not name a vendor in the room.

### So what does realistic automation look like for the military channels? — my assessment, flagged as such

This is **ASSESSMENT built on CONFIRMED facts above**, not a cited finding. Present it as judgment, which is what Rick is being paid for.

1. **VA — EPS integration is the only real API play, and it is worth doing.** It is free, optional, works with 150+ scheduling systems, and delivers the **referral authorization number** into the center's system automatically. That single field is the hinge for scope-and-expiry control. **Recommend EPS enrollment as a named Phase 1 deliverable** — it is concrete, cheap, verifiable, and it is the opposite of vapor.
2. **VA — everything else is document-generation plus human submission.** RFS is a signed PDF (VA Form 10-10172) with mandatory attachments, one per service, submitted via HSRM/secure email/fax, 3-business-day turnaround. Automate the **assembly and the tracking**, not the submission: pre-fill the form from the order, auto-attach the radiology report and notes, enforce the signature check (because unsigned = denied), and run a tickler against the episode-of-care window. The human presses send.
3. **VA — scope-check at intake is the highest-value, lowest-tech control.** Compare the ordered CPT against the SEOC scope before scanning. A rules table, not AI. This directly prevents failure mode #1, which is the one that produces unpaid claims.
4. **TRICARE — eligibility is the automatable piece; authorization is portal/270-271 + 278 if available.** Verify eligibility same-day (DEERS has outages — see §7), capture plan type, and branch: Select/TFL → proceed, no referral needed; Prime → require the referral and authorization letter, and confirm the center is the provider named in the letter, because the patient *"must book with the provider listed in the authorization letter."*
5. **RPA against portals: possible, but I would not scope it in Phase 1.** HSRM and the TriWest portal are both credentialed web apps with training gates and ToS considerations; screen-scraping a federal health portal carries compliance and brittleness risk disproportionate to 4.6% of covered lives. **Say this out loud if asked — declining to over-automate a small channel is a credibility signal to an operator, not a weakness.**
6. **Rick's honest position: the military channels are a workflow-discipline problem, not an API problem.** That framing is defensible, it matches the regulation, and it is what Fernando will already believe.

---

## 9. Q5 — REIMBURSEMENT REALITY: IS THIS VOLUME WORTH OPTIMIZING?

### Verdict: **The evidence falls Rick's way, clearly. Commercial carries the margin AND the prior-auth burden. The deck's focus is correct.**

### El Paso Medicare rates — CONFIRMED, computed from primary CMS files

**Method (fully reproducible):** CMS **RVU26D** (Physician Fee Schedule, October 2026 release, file `rvu26d-updated-08-26-2026.zip`), `PPRRVU2026_Oct_nonQPP.csv` for RVUs; `GPCI2026.csv` for geographic indices. Formula: `(wRVU × PW_GPCI + peRVU × PE_GPCI + mpRVU × MP_GPCI) × CF`.

- **CY2026 conversion factor: $33.4009** (non-QP). **QP conversion factor: $33.5675.** *(New for CY2026: a differential CF applies to Qualifying APM Participants — per the RVU26D notes, *"Beginning January 1, 2026 a differential conversion factor applies when services are furnished by an eligible clinician who is a Qualifying Alternative Payment Model (APM) Participant (QP) for the year."*)*
- **El Paso = Medicare locality 99, "REST OF TEXAS," carrier 04412.** GPCIs: **PW 1.000, PE 0.949, MP 0.903.**
- No OPPS cap applies to these four codes in this locality (checked `OPPSCAP_Oct.csv`), so PFS amounts stand.

| CPT | Description | wRVU | peRVU (non-fac) | mpRVU | **Global** | **TC (-TC)** | **Prof (-26)** |
|---|---|---|---|---|---|---|---|
| **70551** | MRI brain stem w/o dye | 1.44 | 4.31 | 0.10 | **$187.73** | **$121.05** | $66.68 |
| **72148** | MRI lumbar spine w/o dye | 1.44 | 4.20 | 0.10 | **$184.24** | **$116.93** | $67.31 |
| **71250** | CT thorax dx, w/o contrast | 1.05 | 2.85 | 0.07 | **$127.52** | **$78.91** | $48.61 |
| **77067** | Screening mammo, bilateral, incl CAD | 0.74 | 2.99 | 0.05 | **$121.00** | **$86.52** | $34.48 |

*Facility and non-facility rates are identical for these codes in this locality (PE RVUs equal, PC/TC indicator reflects the split).* **The TC column is the operationally relevant one for a freestanding center whose reads are billed separately.**

### Rate basis by channel — CONFIRMED

| Channel | Rate basis | Relative to Medicare | Confidence |
|---|---|---|---|
| **Medicare FFS** | PFS: `(RVUs × GPCIs) × CF`; CY2026 CF $33.4009 / $33.5675 (QP). OPPS where applicable. | **1.00× (definitional)** | **CONFIRMED** — computed from CMS RVU26D + GPCI2026 |
| **VA community care** | 38 CFR 17.4035(a): *"payment rates **will not exceed the applicable Medicare fee schedule**... or prospective payment system amount."* Published hierarchy: **contract-negotiated → Medicare → VAFS → % of billed charges.** | **≈1.00×, capped at Medicare** | **CONFIRMED** |
| **TRICARE** | 32 CFR 199.14(j)(1): allowable = *"the **lower of** the billed charge or the local CHAMPUS Maximum Allowable Charge (CMAC)."* CMAC is Medicare-anchored (below). | **≈1.00×, effectively capped at Medicare** | **CONFIRMED** |
| **Commercial (TX)** | Negotiated. RAND 5.1 (2022 claims): **254%** of Medicare nationally, all hospital IP+OP incl. professional; **Texas 259%**; hospital **outpatient facility 279%**; **associated professional 184%**; **ASC 171%**. | **~1.7×–2.8× depending on setting** | **CONFIRMED** (RAND primary) / **LIKELY** for the TX 259% figure (secondary citing RAND) |

### The VA = Medicare proof, done empirically — CONFIRMED (this is a nice piece of evidence)

I downloaded the **CY26 VA Fee Schedule — All Payers** (28 MB, 559,877 rows, effective 2026-01-01) and searched all four target codes against every Texas locality.

**Result: 70551, 72148, 71250, and 77067 are ABSENT from the VA Fee Schedule entirely.** Meanwhile adjacent niche imaging codes *are* present — 70555/70557/70558/70559 (fMRI), 72159, 77013, 77022, 77061/77062 (breast tomosynthesis).

**That absence is the proof.** VAFS exists only *"in the absence of a contract-negotiated rate or Medicare rate."* Routine imaging codes have Medicare rates, so VA never needs a VAFS line for them — and doesn't publish one. **Conclusion: VA pays El Paso Medicare rates for these studies.** The only Texas locality in the file is **"REST OF TEXAS"** (carrier 04412), matching the PFS locality.

And note row 3 of the VAFS: *"Rates in this schedule will be used by **VA, TriWest and Optum**."* — the TPA does not set its own rates.

### The TRICARE = Medicare proof, from the regulation — CONFIRMED

32 CFR 199.14(j)(1)(iii)–(iv) ratchets CMAC toward Medicare from both directions:
- Overpriced procedures: appropriate charge = prior-year CMAC *"reduced by the lesser of: the percentage by which it exceeds the Medicare fee or fifteen percent."*
- Underpriced: increased by *"the lesser of: the percentage by which it is exceeded by the Medicare fee or the Medicare Economic Index."*
- Where national CMAC < Medicare, the Director *"may increase the national CMAC to a level **not greater than the Medicare rate**."*
- Localities: *"adjusted for localities using the same (or similar) geographical areas and **the same geographic adjustment factors as are used for determining allowable charges under Medicare**."*
- Hospital outpatient radiology: *"TRICARE payments for hospital outpatient radiology services are based on the allowable charge method under paragraph (j)(1)."*

**Rick's "TRICARE generally follows Medicare rates" — VERIFIED CORRECT, with a sharpening: Medicare is the ceiling, not just the benchmark.**

### Medicare FFS prior auth for outpatient imaging — CONFIRMED ABSENT (checked three programs)

1. **42 CFR 419.83** — the complete OPD prior-auth list: blepharoplasty, botulinum toxin injections, panniculectomy, rhinoplasty, vein ablation (from 2020-07-01); cervical fusion with disc removal, implanted spinal neurostimulators (2021-07-01); facet joint interventions (2023-07-01). **No diagnostic imaging.** And the program is scoped to **hospital outpatient department** services — a freestanding imaging center is not an HOPD. (42 CFR 419.82: prior auth is *"a condition of Medicare payment"* for listed services, with claim denial absent a provisional affirmation.)
2. **WISeR Model** — **runs in Texas**, 2026-01-01 to 2031-12-31, six states (NJ, OH, OK, TX, AZ, WA); Texas participant **Cohere Health** under MAC **Novitas (JH)**. Prior auth / pre-payment review applies to Appendix A: knee arthroscopy for OA, induced lesions of nerve tracts, vagus/phrenic nerve stimulation, electrical nerve stimulators, incontinence control devices, skin and tissue substitutes, and similar. **I read Appendix A directly: it contains no diagnostic imaging CPT.** Imaging codes (70360, 70450, 71045/71046, 72020/72040/72220, 74420/74430, 76000, 77002) appear only in **Appendix C "Associated Codes"** — codes bundled with the reviewed procedures, not independently prior-authorized. CMS: *"WISeR does not change Medicare coverage or payment policy"* and *"does not apply to people with Medicare Advantage."*
3. **Medicare Advantage** — **this is where Medicare-channel prior auth actually lives**, and MA **is** a CMS-0057-F impacted payer. So MA imaging prior auth is both a real burden and squarely inside the rule's reach. **The missing number is El Paso MA penetration** (UNVERIFIED — see §4).

### The uncomfortable question, answered

**Rick asked: does commercial carrying both the margin and the prior-auth burden strengthen the deck's focus?**

**Yes — and the evidence is unusually clean.**

- **Margin:** VA ≈ Medicare (capped). TRICARE ≈ Medicare (capped). Medicare = Medicare. **Commercial is the only channel that pays a multiple** — 171%–279% of Medicare depending on setting. For 70551, the spread between a Medicare-rate payer and a commercial payer at even 1.7× is roughly **$188 vs ~$319 global**; at 2.5× it is ~$469. Three of four channels are rate-takers at the same anchor.
- **Burden:** Medicare FFS does **not** prior-auth outpatient imaging (three programs checked). VA is referral/SEOC-scope, and VA just **removed** precertification. TRICARE requires **nothing** for Select/TFL imaging and is PCM-referral-driven for Prime. **Commercial — and MA — are where utilization-management-style prior auth for advanced imaging actually concentrates.**
- **Therefore:** burden and margin are **co-located in commercial**. Optimizing the commercial prior-auth pathway is the highest-value automation target by both measures simultaneously. **The deck's focus is not just defensible; it is the correct answer.**

**The one honest qualification:** the *regulatory* lever (CMS-0057-F) reaches MA, Medicaid, CHIP and FFE QHPs — **not** employer-sponsored commercial, which is the largest commercial block. So the **business case** for focusing on commercial is strong and independent; the **regulatory tailwind** is narrower than the deck likely implies. Fix the claim, keep the focus. See §2 for the exact sentence.

---

## 10. FLAGGED: ANYTHING THAT CONTRADICTS THE DECK'S PREMISE

Ordered by severity. Items 1–2 need action before 2026-10-20.

| # | Finding | Severity | Action |
|---|---|---|---|
| **1** | **CMS-0057-F does not cover commercial employer-sponsored plans.** Impacted payers are MA, Medicaid FFS, CHIP FFS, Medicaid MCO, CHIP MCE, FFE QHPs only. CMS explicitly declined to extend to employer plans for lack of authority, in response to a comment citing 150M Americans. El Paso employer-based-only = 268,142 lives (31.8%) vs 38,832 (4.6%) in both military channels. | **HIGH — this is the real vulnerability, and it is not the one Rick was worried about.** | **Demote CMS-0057-F from load-bearing claim to timing argument. Use the §2 sentence proactively, before anyone asks.** |
| **2** | **VA eliminated precertification effective 2026-09-08**; VAPP is offline. Any deck/notes language about VA precertification is now wrong. | **HIGH — 5-week-old fact, trivially checkable, in front of a 20-year operator.** | **Verify no frozen document says "VA precertification." If one does, flag it for the post-freeze pass. Reframe VA risk as scope + expiry — which is what Rick already believed.** |
| **3** | **TRICARE Select / For Life / Reserve Select / Retired Reserve / YA-Select require NO referral and NO pre-auth for MRI/CT/PET.** TRICARE is a much weaker prior-auth story than a four-channel-burden framing implies. | **MEDIUM — undercuts a burden argument if Rick leans on TRICARE.** | Don't claim TRICARE imaging prior-auth burden. Use Prime-only, and reframe TRICARE as a front-office/POS-penalty issue. |
| **4** | **Medicare FFS does not prior-auth outpatient diagnostic imaging** — verified across 42 CFR 419.83, WISeR, and OPD program scope. | **MEDIUM — but this CONFIRMS Rick's own stated assumption.** | Safe to state affirmatively. Mention WISeR proactively: it runs in Texas, it does not touch imaging. Knowing it exists *and* that it doesn't apply is a credibility win. |
| **5** | **The military channels are 4.6% of covered lives, not a "heavy mix."** The premise behind the whole worry is quantitatively wrong. | **LOW — resolves in Rick's favor.** | Lead with the number if challenged. It retires the objection in one sentence. |
| **6** | **RAND 254% is hospital-based, not freestanding-imaging.** Professional-only is 184%, ASC 171%. | **LOW — precision risk.** | Quote the band (171%–279%) and name the setting. Never quote 254% bare for a freestanding center. |
| **7** | **Retirees 65+ present as Medicare-primary, not TRICARE.** Only 52 people in El Paso County have TRICARE-only coverage at 65+. | **LOW — refines the story.** | The "large military retiree population" is, operationally, a **Medicare** population. Useful, non-obvious, and it will land with Fernando. |
| **8** | **El Paso's 21.6% uninsured rate (182,797 people)** is a larger operational factor for a greenfield center than either military channel. | **LOW — opportunity, not contradiction.** | Consider raising it. Self-pay policy, pre-service estimation and point-of-service collection are real automation targets and it shows Rick studied *this* market rather than a generic one. |

---

## 11. SOURCES

All accessed **2026-10-12** unless noted. Primary regulatory and agency sources preferred throughout.

### Regulatory — primary text
1. **38 CFR 17.4000–17.4040** (Veterans Community Care Program) — eCFR API, title-38 as of 2026-10-01. `https://www.ecfr.gov/api/versioner/v1/full/2026-10-01/title-38.xml?part=17&section=17.4005` (and .4000/.4010/.4020/.4030/.4035/.4040). Note 17.4020 amended **91 FR 42671, July 10, 2026**.
2. **32 CFR 199.14** (TRICARE/CHAMPUS provider reimbursement; CMAC; balance billing) — eCFR API, title-32 as of 2026-10-01.
3. **42 CFR 419.82, 419.83** (Medicare prior auth for certain hospital OPD services) — eCFR API, title-42 as of 2026-10-01. 419.83 amended through 87 FR 72292 (2022-11-23).
4. **89 FR 8758** — CMS-0057-F, *Advancing Interoperability and Improving Prior Authorization Processes*, published 2024-02-08, effective 2024-04-08. Full text (1,608,552 chars): `https://www.federalregister.gov/documents/full_text/text/2024/02/08/2024-00895.txt`. HTML: `https://www.federalregister.gov/documents/2024/02/08/2024-00895/...`
5. **89 FR 85070** — CMS-0057-F Correcting Amendment, 2024-10-25 (doc 2024-24801), noted for completeness.
6. **89 FR 23498 / 2024-06431** — VA, *Methodology for Reimbursing Medical Services... Not on Medicare Fee Schedules*, 2024-03-27 (VAFS rate-setting basis). `https://www.federalregister.gov/documents/2024/03/27/2024-06431/...`

### VA — agency pages and data
7. VA Community Care, **Precertification requirements** (precert eliminated 2026-09-08; VAPP offline) — `https://department.va.gov/vha/community-care/care-coordination/precertification-requirements/`
8. VA Community Care, **Community Care Network** (Region 4 = TX; TriWest TPA Regions 4–5; Optum 1–3) — `https://department.va.gov/vha/community-care/community-care-network/`
9. VA Community Care, **VA fee schedules** (rate hierarchy; "authorized services only"; CY26 file link) — `https://department.va.gov/vha/community-care/va-fee-schedules/`
10. VA Community Care, **Standardized Episodes of Care** (SEOC scope/intent; in-scope vs out-of-scope) — `https://department.va.gov/vha/community-care/care-coordination/standardized-episodes-of-care/`
11. VA Community Care, **Request for Service requirements** (VA Form 10-10172; denial conditions; 3-business-day; channels) — `https://department.va.gov/vha/community-care/care-coordination/request-for-service-requirements/`
12. VA Community Care, **Care coordination tools** (HSRM portal + training gate; EPS 150+ systems; VHIE; Azure RMS; "fax, secure email") — `https://department.va.gov/vha/community-care/care-coordination/care-coordination-tools/`
13. VA Community Care, **Veteran care / urgent care** (30-day documentation, 180-day claim) — `https://department.va.gov/vha/community-care/types-of-veteran-care/`
14. **CY26 VA Fee Schedule — All Payers**, effective 2026-01-01, v1 (28 MB XLSX, 559,877 rows; "Rates in this schedule will be used by VA, TriWest and Optum") — `https://department.va.gov/vha/community-care/wp-content/uploads/sites/60/2026/05/CY26-Fee-Schedule.xlsx`
15. **VA FHIR R4 capability statement**, live probe — `https://api.va.gov/services/fhir/v0/r4/metadata` → 200, fhirVersion 4.0.1, version 14.0.98, date 2026-10-12T21:25:46Z, 19 resources (no ServiceRequest / CoverageEligibility* / Claim / Task).
16. **VA Community Care Eligibility API (sandbox)**, live probe — `https://sandbox-api.va.gov/services/community-care/v0/eligibility/search` → **401** (exists, gated). Production `v1/eligibility` → 404; `provider-directory/v0/r4/metadata` → 404.
17. VA El Paso Healthcare System — `https://www.va.gov/el-paso-health-care/` (5001 North Piedras Street, El Paso, TX 79930-4210). *No enrollee count published.*

### TRICARE / DHA
18. TRICARE, **Referrals and Pre-Authorizations** (plan-by-plan table; POS option; authorization expiry; network-provider protections; MHS GENESIS exclusion) — `https://www.tricare.mil/GettingCare/ReferralsPreAuth`
19. TRICARE, **Regions** — Last Updated 9/29/2026 (TriWest = West; Humana Military = East; WPS = TFL) — `https://www.tricare.mil/About/Regions`
20. TRICARE, **West Region** — `https://www.tricare.mil/west` (beneficiary portal `tricare-bene.triwest.com`; DEERS outage banner Oct 9–11, 2026)
21. DHA, **TRICARE West Region Contractor Transition** (Feb 6 2025, updated Mar 26; acknowledged challenges incl. referral/auth processing; Jan 25 2025 waiver; 97% specialty access; network retention) — `https://www.dha.mil/News/2025/02/07/13/36/TRICARE-West-Region-Contractor-Transition`
22. DHA, **TRICARE West Region Referral Approval Waiver** announcement, 2025-01-25 — via `https://myarmybenefits.us.army.mil/News/Defense-Health-Agency-Announces-TRICARE-West-Region-Referral-Approval-Waiver`
23. TRICARE Newsroom, **Live in the West Region? ... Referrals Before Oct 1** (2025-09-09; waiver users need new referrals) — `https://newsroom.tricare.mil/News/TRICARE-News/Article/4297998/...`
24. TriWest, **TRICARE Prime Beneficiaries: Specialty Care Referral Extension Ends Sept. 30** — `https://triwest.com/en/news/news-archive/2025/tricare-prime-beneficiaries-specialty-care-referral-extension-ends-sept.-30/` — **LIKELY** (contractor-published)
25. California Medical Association, **TRICARE referral and authorization waiver expired June 30** — `https://www.cmadocs.org/newsroom/news/view/reminder-tricare-referral-and-authorization-waiver-expired-june-30` — **LIKELY** (credible secondary, corroborated)
26. TriWest, **TRICARE Provider Contracting Q&A** (Humana agreements assigned to TriWest eff. 2025-01-01) — `https://tricare-qa.triwest.com/en/home-page/provider/join-the-triwest-provider-network/tricare-provider-contracting-qa/` — **LIKELY**
27. TriWest, **Letter to TRICARE West Region Providers** ("navigating several challenges... due to the size and scale of this transition") — `https://www.triwest.com/globalassets/tricare/provider/letter-to-tricare-west-region-providers.pdf` — **LIKELY**
28. *Attempted and failed:* `tricare-west.com` provider handbook — connection failure. **TriWest provider-side X12 278 / API path remains UNVERIFIED.**

### CMS — fee schedules and prior-auth programs
29. **CMS RVU26D** — PFS Relative Value Files, October 2026 release: `https://www.cms.gov/files/zip/rvu26d-updated-08-26-2026.zip` (landing: `/medicare/payment/fee-schedules/physician/pfs-relative-value-files/rvu26d`). Used: `PPRRVU2026_Oct_nonQPP.csv`, `PPRRVU2026_Oct_QPP.csv`, `GPCI2026.csv` (Addendum E, Final CY2026 GPCIs), `OPPSCAP_Oct.csv`, `26LOCCO.csv`. CF non-QP **$33.4009**; CF QP **$33.5675**; Rest of Texas (04412, loc 99) PW 1.000 / PE 0.949 / MP 0.903.
30. **CMS WISeR Model** (Jan 1 2026 – Dec 31 2031; NJ, OH, OK, **TX**, AZ, WA; Cohere Health = TX / Novitas JH; voluntary; "does not change Medicare coverage or payment policy"; excludes MA) — `https://www.cms.gov/priorities/innovation/innovation-models/wiser`
31. **WISeR Model Provider and Supplier Operational Guide** v5.0+ (Appendix A select items/services as of 2026-07-24 — no diagnostic imaging; Appendix C associated codes; dates of service on/after 2026-01-15) — `https://www.cms.gov/priorities/innovation/files/wiser-provider-supplier-guide.pdf`
32. CMS **data.json** catalog (3,438 datasets; searched for PFS/OPPS/MA-penetration) — `https://data.cms.gov/data.json`. **MA state/county penetration file not present in catalog API; landing page 404.** → MA penetration UNVERIFIED.

### Census — demographics
33. **ACS 2024 5-year, B27010** (Types of Health Insurance Coverage by Age), El Paso County TX — `https://data.census.gov/api/access/data/table?id=ACSDT5Y2024.B27010&g=050XX00US48141` (+ metadata endpoint for labels). Universe 844,384.
34. **ACS 2024 5-year, DP05**, El Paso County — total 870,779; 65+ 114,171 (13.1%); under 18 226,840; 18+ 643,939; 85+ 13,366.
35. **ACS 2024 5-year, S2701**, El Paso County — insured 661,587 (78.4%); uninsured 182,797 (21.6%).
36. **ACS 2024 5-year, S2101** (Veteran Status), El Paso County — veterans 47,646 (7.6% of 624,740 civilian pop 18+).
37. **ACS 2024 5-year, DP05**, Fort Bliss CDP (`1600000US4827348`) — 11,419 residents; under 18 2,206; 18+ 9,213. *On-post residents only.*
38. *Note:* `api.census.gov` requires a key ("Missing Key") and QuickFacts returned 403; all figures above were retrieved keyless via the `data.census.gov` access API.

### Other
39. **Texas Comptroller of Public Accounts**, *Texas Military Installations 2025 — Fort Bliss* (41,527 direct employees; 30,288 active duty — Army 28,040 / Navy 1,227 / AF 937; 185,499 military retirees **accessing the installation**; 121,220 total direct+indirect) — `https://comptroller.texas.gov/economy/economic-data/military/2025/fort-bliss.php`. *2023 edition said "over 80,000" retirees — definitional discontinuity, see §4.*
40. **RAND**, *Hospital Price Transparency Study Round 5 Results* (2022 claims; $77.4B / 4,000+ hospitals / 12 APCDs; **254%** all IP+OP incl. professional; IP facility 254%; **OP facility 279%**; **professional 184%**; round-over-round 254/246/253%) — `https://www.rand.org/health/projects/hospital-pricing/round5.html`; report RRA1144-2-v2.
41. **Employer Price Transparency / RAND 5.1** (released 2024-12-10; **ASC 171%** of Medicare; physician-administered meds 205% of ASP; AR lowest 162%, FL highest 346%; median 253%) — `https://employerptp.org/studies/pt5/`
42. **Texas Employers Against Health Care Costs**, *Texas Employers Paid Hospitals 259% of What Medicare Would Pay per RAND* (TX 259%; Houston 227% / 354% OP facility) — `https://txeahc.org/texas-employers-paid-hospitals-259-of-what-medicare-would-pay-per-rand-price-transparency-study/` — **LIKELY** (secondary citing RAND; the 259% TX figure is not independently verified against the RAND annex)

---

## 12. CONFIDENCE SUMMARY

| Question | Verdict | Confidence |
|---|---|---|
| **Q1** Coverage shares by channel, El Paso County | Military channels 4.6%; commercial floor 37.9%; uninsured 21.6% | **CONFIRMED** (Census primary) |
| **Q1** Imaging **volume** share by channel | **Not establishable** — bounding facts given instead | **UNVERIFIED, by design** |
| **Q2** VA authorizer, TPA (TriWest/Region 4), rate basis, scope limits, failure modes, precert elimination | Rick's belief **confirmed**; precert elimination is new | **CONFIRMED** |
| **Q2** Specific referral expiry in days | Episode of care ≤1 calendar year (reg); per-SEOC windows not retrieved | **Partly UNVERIFIED** |
| **Q3** TriWest = West contractor since 2025-01-01; plan-by-plan referral/pre-auth; POS penalties; waiver timeline | Imaging **not** on Select/TFL pre-auth list | **CONFIRMED** (waiver-expiry date **LIKELY**) |
| **Q4** CMS-0057-F excludes TRICARE, VA, Medicare FFS, **and commercial employer plans** | Verbatim confirmed; "TRICARE" appears 0× in rule | **CONFIRMED** |
| **Q4** VA has no FHIR referral/auth API; HSRM portal + EPS scheduling + fax | Live capability-statement probe | **CONFIRMED** |
| **Q4** DHA/TRICARE provider-facing FHIR auth API | None found; handbook unreachable | **UNVERIFIED (leaning no)** |
| **Q4** Clearinghouse re-intermediation | X12 278 structurally plausible for TRICARE; none found for VA auth | **PARTIALLY VERIFIED** |
| **Q5** Medicare El Paso rates (4 CPTs, global/TC/26) | Computed from CMS RVU26D + GPCI2026 | **CONFIRMED** |
| **Q5** VA ≈ Medicare (empirically: target CPTs absent from VAFS) | 38 CFR 17.4035(a) + 559,877-row file search | **CONFIRMED** |
| **Q5** TRICARE CMAC Medicare-anchored and capped | 32 CFR 199.14(j)(1) operative text | **CONFIRMED** |
| **Q5** Commercial 171%–279% of Medicare; TX 259% | RAND 5.1 primary; TX figure secondary | **CONFIRMED / LIKELY** |
| **Q5** Medicare FFS does not prior-auth outpatient imaging | 42 CFR 419.83 + WISeR Appendix A + HOPD scope | **CONFIRMED** |
| **Q5** Verdict: commercial carries margin AND burden | Deck's focus is correct | **CONFIRMED** |
| El Paso **MA penetration** | Not retrievable from primary CMS API | **UNVERIFIED — flagged as diligence item** |
| El Paso **VA enrollee count** | Not published / data.va.gov 404 | **UNVERIFIED** |
| Fort Bliss **dependent / TRICARE beneficiary count** | DMDC endpoints 404; CDP ≠ assigned population | **UNVERIFIED** |

---

*Sherlock. Read-only. No document outside this file was created or modified.*
