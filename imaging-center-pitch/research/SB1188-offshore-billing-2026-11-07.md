# Research Brief: Texas SB 1188 and an Offshore (India) Billing Vendor
**Prepared by:** Sherlock (Gio research) for Rick / El Paso imaging center · **Date:** 2026-11-07
**Status:** Research brief for counsel. NOT legal advice.

Confidence key: **HIGH** = primary text read verbatim · **MED** = reputable secondary source or a reasoned reading · **LOW** = inference or not verified.

---

## Bottom line
**SB 1188 itself very likely allows** US-hosted EHRs with offshore remote access by billing staff. Its localization duty covers where records are *physically maintained*. It does not ban access from abroad. **(MED-HIGH)**

**The gray area is the Texas Medicaid / managed care contract layer, not SB 1188.** HHSC's Uniform Managed Care Contract (UMCC) bars MCOs and their "subcontractors, vendors, agents, and service providers" from offshore work and offshore remote access. Medicaid is in the client's payer mix, so counsel must review the MCO provider agreements before any Medicaid claims touch India. **(MED)**

---

## 1. SB 1188: enrolled text (primary source)
Source: https://capitol.texas.gov/tlodocs/89R/billtext/html/SB01188F.htm (enrolled version, read in full 2026-11-07) **(HIGH)**

- **Codified at:** new Tex. Health & Safety Code **Chapter 183**, §§183.001–183.012. **(HIGH)**
- **Data-localization provision, §183.002(a), verbatim:**
  > "A covered entity shall ensure that electronic health records under the control of the entity that contain patient information are **physically maintained in the United States or a territory of the United States**. This subsection applies to: (1) electronic health records that are stored by a third-party or subcontracted computing facility or an entity that provides cloud computing services; and (2) electronic health records that are stored using a technology through which patient information may be electronically retrieved, accessed, or transmitted."
- **Access provision, §183.002(b), verbatim:**
  > "A covered entity shall ensure that the electronic health record information of this state's residents, other than open data, is accessible only to individuals who require the information to perform duties within the scope of the individual's employment related to treatment, payment, or health care operations."
- **§183.002(c):** "reasonable and appropriate administrative, physical, and technical safeguards to protect the confidentiality, integrity, and availability of electronic health record information." **(HIGH)**
- **Who is covered (§183.001(2)):** "Covered entity" has the meaning in **§181.001** (the HB 300 definition), and "includes a health care practitioner." The §181.001 definition is very broad. It includes business associates, information or computer management entities, and "an employee, agent, or contractor" who handles PHI, as quoted by BakerHostetler. **That means the billing vendor itself is likely a covered entity.** The listed exclusions are home health, nursing, assisted living, ICF, day activity, and HCS/TxHmL providers. Imaging centers are not excluded. **(HIGH on text; MED on vendor coverage)**
- **Effective dates:** the Act takes effect **Sept. 1, 2025** and applies to EHRs prepared on or after that date. §183.002 storage applies "to the storage of an electronic health record on or after **January 1, 2026**, regardless of the date on which the electronic health record was prepared." **(HIGH)**
- **Exceptions:** there is no exception for storage location. The only carve-outs are the facility types listed above. §183.002(b) excludes "open data." **(HIGH)**
- **Enforcement:**
  - The HHSC ("commission") or the appropriate regulatory agency investigates credible allegations (§183.009).
  - A licensing agency may discipline after **three or more** violations, up to suspension or revocation (§183.010).
  - The **Attorney General** may seek injunctive relief and civil penalties (§183.011): up to **$5,000** per negligent violation per year, **$25,000** per knowing or intentional violation, and **$250,000** where PHI was knowingly or intentionally used for financial gain.
  - Agencies must enter an MOU and may adopt rules (§183.012). **(HIGH)**

## 2. Storage vs. access: what the text regulates
- The operative verb is "**physically maintained**." The chapter does not define "electronic health record," "maintain," or "store." **(HIGH)** I did not check whether rules adopted under §183.012 since then supply definitions. **(LOW)**
- Subdivision (a)(2) extends the storage duty to records "stored using a technology through which patient information may be electronically retrieved, accessed, or transmitted." Read plainly, that clause covers *systems that permit remote access*. It requires those systems to be physically in the US. It does not bar who may access them, or from where. **(MED)**
- The only access rule is **§183.002(b)**, which is role-based (TPO need). **Billing is "payment,"** so properly scoped billing staff qualify. The provision contains no geographic limit. **(HIGH on text; MED on application)**
- **Risk point:** a remote session can download files, cache them locally, export them, print them, or sync them to a device in India. That arguably creates records "physically maintained" outside the US. Controls must prevent offshore persistence. **(MED)**

## 3. Commentary
- **BakerHostetler, Data Counsel blog (2025-08-19)**, https://www.bakerdatacounsel.com/blogs/texas-passes-new-law-regulating-electronic-health-records-and-the-use-of-ai-by-healthcare-professionals/ : "Notably, the law does not restrict access to electronic health records from outside of the U.S. … Covered entities can thus continue to use offshore vendors that need access to U.S.-based electronic health records. However, covered entities should ensure that controls are in place so that those offshore vendors are unable to save and store the electronic health records they access." **(HIGH that they say this; it directly supports the bottom line)**
- **Weaver Johnston**, https://weaverjohnston.com/legislative-regulatory-updates/texas-sb-1188-what-healthcare-providers-need-to-know-about-new-ai-and-ehr-rules/ : "offshore storage (i.e. physically outside the U.S.) prohibited." This is framed as storage only. (Search snippet only; the full page was not read.) **(MED)**
- **Shumaker, Loop & Kendrick (2025-12-12)**, https://www.shumaker.com/insight/offshoring-patient-data-what-health-care-providers-need-to-know-now/ : "HIPAA does not prohibit PHI from being accessed or stored outside the United States." It also says Texas's UMCC "prohibits performance of work or maintenance of information outside the United States and bars remote offshore access to Texas Health and Human Services systems or data." **(HIGH that they say this)**
- **TMA / TMB / AG:** I found **no** FAQ, rule, or AG statement addressing offshore access. One targeted search returned nothing. This is **unverified absence, not proof of absence.** Counsel should check the Texas Register for §183.012 rules and the TMA's SB 1188 resources. **(LOW)**
- **Conflicts between sources:** none on SB 1188. The sources are consistent that it is a storage rule, not an access rule.

## 4. Other law affecting the offshore piece
- **HIPAA:** HIPAA has no offshore ban. It requires a **BAA** with the billing vendor and any subcontractor BAAs (45 CFR 164.502(e), 164.504(e), 164.308(b)), plus minimum necessary access, a risk analysis covering offshore access, and breach terms. Enforcement against an Indian entity is practically weak, so the risk stays with the client. **(HIGH on rule; MED on practical point, per Shumaker)**
- **Texas HB 300 (H&S Code ch. 181):**
  - The vendor is a covered entity under §181.001.
  - Workforce training is required (§181.101).
  - The **ban on sale of PHI** (§181.153) applies.
  - Electronic disclosure requires notice (§181.154).
  - AG penalties apply (§181.201).
  These obligations travel with the vendor's staff. I did not reread ch. 181 verbatim this session. **(MED)**
- **Federal Medicaid, ACA §6505 (42 USC 1396a(a)(80); 42 CFR 431.53/ 455):** states may not pay for items or services from entities outside the US. Per Shumaker, CMS has said this does not target administrative support. **(MED)**
- **Texas Medicaid UMCC v2.45 §4.11** (HHSC PDF read 2026-11-07, https://www.hhs.texas.gov/sites/default/files/documents/services/health/medicaid-chip/programs/contracts/uniform-managed-care-contract.pdf) **(HIGH on text)**:
  > "MCO and all subcontractors, vendors, agents, and service providers of or for MCO must not permit any person to have remote access to HHSC information, systems, or Deliverables from a location outside the United States."
  > "HHSC forbids the performance of any work or the maintenance of any information relating or obtained pursuant to this Agreement to occur outside of the United States."

  Revision 2.33 (June 1, 2021) removed the prior-approval option, so no waiver path remains. §11.08 requires the MCO's security program to prohibit offshore work. **(HIGH)**
  **Open question:** does a *network provider's* own billing vendor fall within "service providers of or for MCO"? Literally, the provider bills *the MCO*. It does not perform the MCO's work. MCO provider agreements, however, commonly flow these clauses down. **(MED; counsel must read the actual Superior / El Paso Health / other MCO provider contracts)**
- **Medicare Advantage / Part D:** offshore subcontractors that "receive, process, transfer, handle, store, or access" PHI require plan attestations (per Shumaker), which can flow down to providers. Traditional Medicare FFS has no offshore ban for provider billing vendors. **(MED)**

## 5. Practical safeguards if they proceed
1. **No data at rest offshore.** Use VDI or browser-only access (for example Citrix, AVD, or the PM/EHR's hosted portal) with copy/paste, download, print, local drives, and screenshots disabled, and no sync clients. Keep all backups, logs, and scans US-hosted. Put this in the contract. (This is the BakerHostetler-recommended control.)
2. **Segregate Medicaid / Medicaid-managed-care work** to US staff until counsel clears the MCO contracts. Wall off traditional Medicare / commercial work if offshore staff are used.
3. Get a **BAA** plus a subcontractor BAA chain. Require the vendor to contractually acknowledge it is a ch. 181 / ch. 183 covered entity. Require HB 300 training attestations, a ban on PHI sale, and US-law governing / venue terms, with indemnity and cyber insurance.
4. **Role-based least privilege** (§183.002(b)): limit access to billing fields and scope out images and full charts where possible. Use MFA, IP allow-listing, session logging, and quarterly access reviews.
5. Get a SOC 2 Type II or HITRUST report, conduct an annual audit, and include breach notice ≤ 72h (Texas requires notice within 60 days under Bus. & Com. Code §521.053; confirm).
6. Document a **risk analysis** that specifically covers offshore access.

## 6. What counsel must confirm
1. Whether any §183.012 rules or MOU since 2025 define "maintain" or "store" or address remote access.
2. Whether the **client's MCO provider agreements** (Texas Medicaid / CHIP / STAR) flow down UMCC §4.11 to network providers' billing vendors.
3. Any Medicare Advantage plan offshore attestation requirements in their contracts.
4. Whether a VDI no-persistence architecture satisfies "physically maintained in the United States" for cached or temporary data.
5. HIPAA BAA and ch. 181 compliance of the specific Indian vendor, and contract enforceability in India.
6. Any AG enforcement activity under ch. 183 to date (none found).
