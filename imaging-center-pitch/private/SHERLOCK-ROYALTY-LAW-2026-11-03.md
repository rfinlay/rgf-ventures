# RadAssist royalty and referral fees: healthcare kickback law (federal + Texas)
Sherlock, 2026-11-03. Research memo for a lawyer conversation. This is not legal advice.

Facts assumed: RGF Global Ventures LLC licenses RadAssist (~$2,400/yr per center) to imaging centers. It drafts reports from radiologist-graded inputs and the radiologist signs. Proposed: Dr. Luis Ramos (radiologist, co-designer, future co-owner of a new El Paso center) gets free use at his center plus 30% of net license revenue from centers he helps sell to. Fernando Escarzaga and Jesse Martinez (co-owners of that center) get 10% for centers they introduce. One payout per sale.

## Options and risk level (plain English)

| # | Option | Risk | Why |
|---|---|---|---|
| A | As proposed: 30% sales-tied "royalty" to Luis + 10% finder fees to Fernando and Jesse | **Moderate to High** | Percentage of sales paid to healthcare providers for getting other providers to buy. That is the exact shape the kickback statutes describe. The only real defense is that the software is not paid for by Medicare/Medicaid, and that defense is arguable, not clean. Texas law adds a second, broader layer that does not need any federal payment. |
| B | Luis: true IP royalty on ALL RadAssist revenue (same % whether or not he made the sale), fixed in a written IP assignment; no sales commission at all | **Low to Moderate** | Paying an inventor for what he contributed is normal and defensible. Keeps working only if the rate is fair market value and does not go up because he sold something. |
| C | Luis: royalty (Option B) plus a separate, fixed, written consulting fee (hourly or flat, FMV) for demos, clinical advice, product work | **Low** | Mirrors the personal services safe harbor: written, at least 1 year, set in advance, FMV, not based on sales he generates. |
| D | Fernando and Jesse: no per-sale fee. If they help, pay a flat FMV consulting or advisory fee for documented work, or give equity in RadAssist (ownership, not per-deal) | **Low to Moderate** | Removes the "paid per referral" pattern. Equity still needs a lawyer to check the investment-interest rules, but it is not a commission. |
| E | Referral fees only to people who are not licensed providers, not owners of a provider, and not in a position to influence purchases (or to W-2 employees, who have a statutory exception) | **Low** | Employee exception is in the statute itself. Non-provider independent agents on commission are still scrutinized by OIG but far less exposed, especially for non-reimbursed software. |
| F | Any option plus guardrails: exclude centers Luis reads for or refers patients to; no payments tied to any center's Medicare/Medicaid volume; written disclosure to the buyer that the introducer is paid; log of hours/work | **Lowers whichever option you pick by about one level** | Texas 102.006 requires disclosure where a paid referral is otherwise allowed; carve-outs remove the obvious "swap" story. |
| G | Free license for Luis's own center | **Low** | Rick is a vendor, not a biller, and the center is a development/reference site. Paper it as a written beta/reference-site agreement with real obligations (feedback, case studies) so it reads as consideration, not a gift. |

Bottom line: the 30% and 10% per-sale numbers are the problem, not the people. Recast Luis as inventor (royalty on everything) plus paid consultant (fixed FMV fee), and drop per-sale fees for Fernando and Jesse. Confidence in that conclusion: **High** that a healthcare lawyer would push you there; **Medium** on exactly how risky Option A is, because no court or OIG opinion squarely addresses commissions on non-reimbursed radiology software.

---

## 1. Federal Anti-Kickback Statute (AKS), 42 U.S.C. 1320a-7b(b)

**What it says (verified from statute text, LII):** It is a felony (up to $100,000 and 10 years) to knowingly and willfully offer, pay, solicit, or receive "any remuneration ... directly or indirectly ... to induce such person ... (B) to purchase, lease, order, or arrange for or recommend purchasing, leasing, or ordering any good, facility, service, or item for which payment may be made in whole or in part under a Federal health care program." 42 U.S.C. 1320a-7b(b)(2)(B), (b)(1)(B). Confidence: **High**.

**Does paying providers to get other providers to buy software implicate it?** The "recommend purchasing ... any good ... or item" prong is not limited to patient referrals. Paying radiologists/center owners a percentage to recommend that other centers buy is textbook (b)(2)(B) conduct. The only open question is the federal-payment nexus. Confidence: **High**.

**When is software an item "for which payment may be made in whole or in part"?**
- Medicare does not pay separately for reporting software. Imaging centers are paid per study (technical component under the physician fee schedule / IDTF rules; hospital outpatient under OPPS). The software is overhead.
- OIG's longstanding position is that the statute reaches items paid indirectly, including costs that are folded into bundled or prospective payments or reported on cost reports. The phrase "in whole or in part" is the hook. OIG stated this in the original safe harbor rulemaking (56 Fed. Reg. 35952, July 29, 1991, preamble). Confidence that OIG takes this view: **Medium-High**; the exact preamble pinpoint should be pulled by counsel.
- Hospital buyers: software cost on a hospital Medicare cost report is a clearer federal nexus than a freestanding center paid on fee schedule. If any target customer is a hospital radiology department, risk rises. Confidence: **Medium-High**.
- "One purpose" test: if one purpose of a payment is to induce the purchase, the statute is violated even if other purposes are legitimate. United States v. Greber, 760 F.2d 68 (3d Cir. 1985); followed in several circuits. Intent standard: actual knowledge of the AKS is not required (42 U.S.C. 1320a-7b(h), added 2010). Confidence: **High**.
- Since 2010, an AKS-tainted claim is a false claim under the False Claims Act (42 U.S.C. 1320a-7b(g)). Confidence: **High**.

**OIG on percentage sales commissions to independent agents.** OIG has repeatedly said percentage-based compensation to independent (non-employee) sales agents is "suspect" and outside any safe harbor, with heightened concern when the agent is in a position to influence purchasers (e.g., a provider) rather than a pure salesperson. See OIG Advisory Opinions 98-1 and 98-4, and later opinions applying the same factors (compensation tied to volume, agent's relationship to buyers, whether items are federally reimbursed). Confidence: **Medium** (factors are well known; specific opinion numbers should be confirmed by counsel on oig.hhs.gov/compliance/advisory-opinions). I found no OIG opinion on commissions for non-separately-billed radiology reporting software.

**Safe harbors (42 C.F.R. 1001.952):**
- **Employees, (i)** and statutory exception 1320a-7b(b)(3)(B): bona fide W-2 employees may be paid commissions. Fernando/Jesse/Luis are not employees. **High**.
- **Personal services and management contracts, (d):** written, signed, at least 1 year, covers all services, compensation methodology set in advance, consistent with FMV, and **not determined in a manner that takes into account the volume or value of referrals or business otherwise generated** between the parties. The 2020 rule (85 Fed. Reg. 77684, Dec. 2, 2020) dropped the "aggregate compensation set in advance" requirement (methodology now suffices) and dropped the part-time schedule requirement. A percentage-of-sales commission still fails the volume/value condition. **High**.
- **Referral services, (f):** covers referral services (e.g., physician referral services), not vendor sales commissions. Does not fit. **High**.
- **EHR items and services, (y), and cybersecurity, (jj, added 2020):** protect donors who GIVE EHR/cybersecurity technology to referral sources. RadAssist is not donating to anyone, so these do not apply. Free use at Luis's center is not the right fit either (that is a vendor giving a customer a license). **High**.
- **Value-based safe harbors (ee)-(gg), 2020:** require a value-based enterprise; not applicable. **High**.
- **Royalties:** no dedicated safe harbor. Counsel analyze them under FMV and the volume/value principle. **High**.

## 2. Stark Law (physician self-referral), 42 U.S.C. 1395nn

Stark applies when a physician refers Medicare patients for "designated health services" (DHS) to an entity with which the physician has a financial relationship. Radiology and imaging ARE DHS (1395nn(h)(6)). But the relevant entity here is RGF/RadAssist, which does not furnish or bill DHS, and the payments are for software sales, not patient referrals to RGF. So the royalty/referral plan does not create a Stark issue. Confidence: **High**.

One caution: Luis's referrals of patients to his own imaging center are their own Stark question (ownership in a DHS entity; in-office ancillary and other exceptions). That is the center's lawyer's problem, separate from RadAssist. Also, do not let RadAssist payments flow through the imaging center entity, which would mix a DHS entity into the money trail. Confidence: **Medium-High**.

## 3. Texas

**Patient Solicitation Act, Tex. Occ. Code 102.001 (verified text):** "A person commits an offense if the person knowingly offers to pay or agrees to accept ... any remuneration in cash or in kind to or from another for securing or soliciting a patient or **patronage for or from** a person licensed, certified, or registered by a state health care regulatory agency." Class A misdemeanor; third-degree felony for repeat offenders or government employees. Confidence: **High** on text.
- **Key point: no federal-payment requirement.** It applies to all payers, including cash and commercial. **High**.
- **Does "patronage" reach B2B vendor sales?** The statute says patronage "for or from" a licensed person. Paying Luis (licensed) to secure the patronage of other radiologists/centers (purchases "from" licensed persons, i.e., licensed buyers) for RGF is within the literal text. I found no Texas appellate case or AG opinion applying it to a software vendor's sales commissions, and most enforcement involves patient steering. Treat as **unsettled; literal reading covers it**. Confidence: **Medium**.
- **Safe harbor import, Tex. Occ. Code 102.003 (verified):** 102.001 "permits any payment, business arrangement, or payment practice permitted by 42 U.S.C. Section 1320a-7b(b) or any regulation adopted under that law." So fitting a federal safe harbor (personal services, employee) also protects you in Texas. Merely "the AKS doesn't reach it because no federal payment" probably is NOT "permitted by" the AKS in the safe-harbor sense; counsel should confirm. Confidence: **Medium**.
- **Disclosure, Tex. Occ. Code 102.006 (verified):** where paid solicitation is otherwise allowed, the person paid must disclose, at first contact and at referral, their affiliation and that they will be paid. Written disclosure to buyers is cheap insurance. **High** on text; **Medium** on whether it applies to B2B buyers.

**Texas Medical Board fee-splitting / solicitation:** The correct cite is **Tex. Occ. Code 165.155** (verified), not 164.052(a)(8) (that subsection concerns buying/selling medical degrees). 165.155(a): a physician commits an offense if the physician pays or rewards anyone "for securing or soliciting a patient or patronage"; (c): a physician commits an offense if the physician "accepts or agrees to accept a payment or other thing of value for securing or soliciting patronage for another physician." Here Luis secures patronage for RGF (not a physician), so (c) is not a direct fit, but violations of 102 and fee-arrangement issues can also be disciplinary under 164.053 (unprofessional conduct) and TMB rules in 22 TAC ch. 190. Confidence: **Medium-High** on statute text; **Medium** on how TMB would treat it. Fernando and Jesse are not physicians; if either holds another license (e.g., radiologic technologist), that board's rules apply too.

**Texas Medicaid Fraud Prevention Act, Hum. Res. Code ch. 36:** 36.002 lists unlawful acts, including kickback conduct that violates Hum. Res. Code 32.039(b) (the state Medicaid kickback provision). Like the AKS, it needs a Medicaid payment nexus, so the same "indirect payment" analysis applies, with civil penalties and AG enforcement. Confidence: **Medium** (I could not pull the current section text live; counsel should confirm subsection numbering).

**TX AG guidance:** I found no AG opinion on vendor sales commissions to providers. Confidence that none is directly on point: **Medium**.

## 4. Royalty for IP vs. commission for selling: how lawyers tell them apart

Practitioners and OIG look at substance, not the label. A payment reads as a legitimate royalty when:
1. It is paid for a **real, documented contribution** (written IP assignment or license from Luis to RGF, describing what he contributed: workflow design, templates, grading schema).
2. It is calculated on **all** revenue from the product, regardless of who sold it or whether Luis touched the deal. A royalty that only pays on deals he brings in is a commission.
3. The rate is **fair market value** for that type of contribution (a third-party valuation helps; 30% is high for a contributing co-designer versus typical software/medical IP royalties, which often run low single digits to mid-teens, though this varies widely). Confidence on typical range: **Low-Medium**.
4. It is **set in advance**, in writing, and does not increase with sales Luis personally generates.
5. It **excludes or is neutral to** sales to entities Luis refers patients to or works with, and is not tied to federal program volume.
6. OIG has expressed concern with royalties paid to physicians who are in a position to generate business for the payer, especially on products they order or influence (e.g., the device-industry royalty concerns in OIG compliance guidance and the 2005 Compliance Program Guidance for Pharmaceutical Manufacturers, 68 Fed. Reg. 23731 (May 5, 2003)). Confidence: **Medium**.

Apply that to the proposal: "30% on centers he helps sell to" fails test 2 and probably 3. It is a commission.

## 5. Safer structures (detail behind the table)

- **Luis:** (a) written IP assignment + royalty on all net RadAssist revenue at a valuation-supported rate; (b) separate written consulting agreement, 1+ year, hourly or flat FMV fee for listed services (demos, clinical advisory, product reviews), with time logs. Optionally (c) equity in RadAssist instead of or alongside royalty.
- **Fernando and Jesse:** drop per-sale fees. If they contribute, flat FMV advisory fee for documented work, or equity. Do not route through the imaging center.
- **Commission sales** later: use W-2 sales staff (statutory exception) or non-provider independent reps with FMV, written terms; still keep it off any reimbursed-cost customers if possible.
- **Guardrails for any deal:** written agreements signed before any sale; exclude centers where payee reads, refers, or has ownership; no compensation tied to any customer's Medicare/Medicaid volume; written disclosure to buyers of any paid introducer (Tex. Occ. Code 102.006); price lists uniform so the license price itself is not discounted as a hidden kickback; keep RadAssist payments separate from the imaging center entity.
- **Free license for Luis's center:** written beta/reference-site agreement with concrete obligations; time-limited or tied to his development role.
- **If staying close to the original idea:** an OIG advisory opinion (42 C.F.R. part 1008) is available, but slow and costly; usually not worth it at $2,400/yr per center.

## Questions to bring to the lawyer

1. Is a freestanding imaging center's software overhead an item "for which payment may be made in whole or in part" under the AKS, given fee-schedule (not cost-report) payment? Does the answer change for hospital customers?
2. Does Tex. Occ. Code 102.001 "patronage for or from" a licensed person reach a software vendor paying licensed radiologists to recommend the software to other licensed providers?
3. Does 102.003 protect us if the AKS simply does not reach the arrangement (no federal nexus), or only if a federal safe harbor is met?
4. What royalty rate for Luis's contribution can be supported as FMV, and should we get a third-party valuation?
5. Can Luis's consulting fee meet the personal services safe harbor (1001.952(d)) as drafted? What services and rate?
6. Equity for Fernando/Jesse/Luis in RadAssist: any investment-interest safe harbor issues, given they are providers who may buy the product?
7. Does the free license at Luis's center need to be FMV-justified or documented as a beta site?
8. Are there TMB disciplinary risks for Luis (165.155, 164.053, 22 TAC 190) even if no crime applies?
9. Should we exclude centers Luis reads for, and centers where Fernando/Jesse have any interest?
10. Does Luis's current employer/group contract restrict outside IP, consulting, or royalty income?
11. Do we need 102.006-style disclosure language in sales materials when an introducer is paid?

## Sources (checked this session)
- 42 U.S.C. 1320a-7b(b), text via LII, verified 2026-11-03.
- Tex. Occ. Code 102.001, 102.003, 102.006, 165.155, 164.052, text via texas.public.law, verified 2026-11-03.
- Cited from knowledge, not re-fetched (confirm): 42 C.F.R. 1001.952 (d), (f), (i), (y), (jj), (ee)-(gg); 85 Fed. Reg. 77684 (Dec. 2, 2020); 56 Fed. Reg. 35952 (July 29, 1991); United States v. Greber, 760 F.2d 68 (3d Cir. 1985); 42 U.S.C. 1395nn(h)(6); OIG Adv. Ops. 98-1, 98-4; 68 Fed. Reg. 23731 (2003); Tex. Hum. Res. Code 36.002, 32.039.
