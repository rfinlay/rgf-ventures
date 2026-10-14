# SHERLOCK — Legal-name spelling verification: Luis's business partner
**Date:** 2026-10-14
**Analyst:** SHERLOCK (read-only; no contact made with any person or entity)
**Purpose:** Confirm spelling for pitch deck title page + printed leave-behind (handed to this person)

---

## 1. VERDICT

**`Fernando Escarzaga` — CONFIRMED. No accent mark. Safe to print on the leave-behind.**

The surname is **Escarzaga** (E-S-C-A-R-**Z**-A-G-A), unaccented. Confirmed by two independent
federal government records that are self-rendering (built from his own applications), plus a
federal court docket caption, plus his own professional web presence.

**SAFE TO PRINT.** Confidence: **CONFIRMED** (highest tier).

### One material refinement to Rick's brief
His **legal** first name is **Jesus Fernando Escarzaga** — a Spanish double given name, exactly the
possibility the brief flagged. "Fernando" is the name he uses in business and the one his own
company's press coverage and LinkedIn use.

> **Recommendation: print "Fernando Escarzaga".** Do NOT print "Jesus Fernando Escarzaga" on a
> pitch deck. The legal form belongs on a contract or engagement letter, not a title page.
> Using "Fernando" is correct, is his own business self-rendering, and is what he will expect.

### Second refinement — he holds BOTH credentials, and they are his
Rick's brief said "RDMS / RPA" and was right on both counts, but they appear in two different
federal records:
- **RDMS** — on the Southwest X-Ray, LP organizational NPI, as authorized official / **President**
- **RPA** (Radiology Practitioner Assistant) — on his individual provider NPI

Earlier in this research it looked like "Jesus Escarzaga, President" and "Fernando Escarzaga, CEO"
were two different people (a father/son or brother pair). **They are one man.** The org NPI record
resolves it: authorized official `JESUS FERNANDO ESCARZAGA, RDMS, president`. Do not refer to them
as two people.

---

## 2. If NOT safe to print

Not applicable — it is safe to print. No fallback needed.

For completeness, the fallback that is NOT required: omitting the surname / using "your partners" /
asking Luis in the room. **Do not do this** — hedging the name when the name is confirmed is a
needless credibility cost, and the brief correctly identified the title page as a first-three-seconds
moment.

---

## 3. Evidence table

| # | Source | What it says | Self-rendering? | URL | Accessed | Confidence |
|---|--------|--------------|-----------------|-----|----------|------------|
| 1 | **CMS NPI Registry — organizational record, SOUTHWEST X-RAY,LP** (NPI 1467524231) | Authorized official: `JESUS FERNANDO ESCARZAGA`, credential `RDMS`, title `president`. Org addr 10501 Gateway Blvd W, El Paso TX. Enumerated 2006-11-15. | **YES** — federal record populated from the entity's own NPI application, signed by the authorized official | `https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1467524231` | 2026-10-14 | **CONFIRMED** |
| 2 | **CMS NPI Registry — individual record** (NPI 1023261856) | `first_name: JESUS`, `middle_name: FERNANDO`, `last_name: ESCARZAGA`, `credential: rpa`, taxonomy `Radiology Practitioner Assistant` (243U00000X), El Paso TX 79922, sex M, status A, enumerated 2008-10-24 | **YES** — federal record from his own provider application | `https://npiregistry.cms.hhs.gov/api/?version=2.1&number=1023261856` | 2026-10-14 | **CONFIRMED** |
| 3 | **CourtListener / PACER — federal docket caption** | `Escarzaga v. Akumin Imaging Texas, LLC`, No. **3:25-cv-00291**, W.D. Tex. (El Paso div.), filed 2025-08-01. Correct surname, correct defendant entity, correct court. *(Spelling evidence only — see note below.)* | Party-of-record caption; authoritative legal-name spelling | `https://www.courtlistener.com/api/rest/v4/search/?q=%22Escarzaga%22+%22Akumin%22&type=r` | 2026-10-14 | **CONFIRMED** |
| 4 | **His own professional site** | Renders as `Jesus Escarzaga RPA`, El Paso TX, specialty Radiology. No accent. | **YES** — his own site | `https://jesusescarzaga.dr-leonardo.com/about-us.html` | 2026-10-14 | **CONFIRMED** |
| 5 | **LinkedIn public profiles (2)** | Both render `Fernando Escarzaga`; one headlined *Southwest X-Ray*, one *swxray*. Full pages blocked (HTTP 999) — read from search-result titles only. | **YES** (his own profiles) | `linkedin.com/in/fernando-escarzaga-90189017/`, `linkedin.com/in/fernando-escarzaga-54411715/` | 2026-10-14 | PROBABLE (titles only; body not retrievable) |
| 6 | **Doximity** | `Jesus Fernando Escarzaga`, Radiology, El Paso, same address/phone as NPI #2 | No (third-party directory) | `https://www.doximity.com/pub/jesus-escarzaga-pa` | 2026-10-14 | PROBABLE |
| 7 | **OpenNPI mirror** | `Jesus Fernando Escarzaga · 4930 Osborne, Suite H, El Paso, TX 79922 · Radiology Practitioner Assistant` | No (mirror of #2) | `https://opennpi.com/provider/1023261856` | 2026-10-14 | CONFIRMED (derivative) |
| 8 | ⚠️ **Akumin press release, 2019-08-19** | **"Fernando and Veronica Escargaza"** — *misspelled*, letters transposed (**-rgaza** instead of **-rzaga**) | No — third-party acquirer's PR | `https://akumin.com/newsroom/press-releases/akumin-expands-in-texas-with-five-diagnostic-centers-and-us13-million-revenues/` | 2026-10-14 | **ERROR — do not use** |
| 9 | ⚠️ **SEC EDGAR, Akumin 40FR12B EX-99.35** (filed 2020-08-28) | Same "Escargaza" string | No | `https://www.sec.gov/Archives/edgar/data/1776197/000119312520233781/d929223dex9935.htm` | 2026-10-14 | **ERROR — same PR re-filed, not independent** |

> **Litigation note (per engagement rules):** item #3 is cited **solely** as a spelling authority —
> a docket caption is an authoritative rendering of a legal name. The substance, merits, posture,
> and outcome of that matter are a **prohibited topic** in this engagement and were deliberately not
> retrieved, read, or summarized. Per standing memory, Akumin litigation must **never** be raised
> with him. **Do not mention Akumin, the sale, or any dispute at the 10-20 dinner.**

### Why the Akumin "Escargaza" spelling loses decisively
This was the one genuine scare in the research — a spelling nobody anticipated, in the acquirer's
own announcement. It is a typo, and the evidence is conclusive:
1. **It is a single source, not two.** The SEC filing (#9) is Akumin's identical press release
   re-filed verbatim as an exhibit. One error, propagated once — not independent corroboration.
2. **"Escargaza" has zero footprint in any records system.** CourtListener full-text: **0 results**.
   CMS NPI Registry: **0 results**. A real surname of a 20-year El Paso business owner and licensed
   provider cannot return zero in both.
3. **It is third-party PR about him**, written by the *buyer's* communications staff. Items #1, #2
   and #4 are **his own** renderings. Self-rendering beats third-party journalism — and two federal
   registry records beat a press release outright.
4. The error is a simple **letter transposition** (`rzaga` → `rgaza`), the single most common
   category of name typo in press copy.

---

## 4. Variants ruled out

| Variant | Ruled out by |
|---|---|
| **Escarsaga** | CMS NPI: **0** results (any state). CourtListener: **0** results. No footprint anywhere. |
| **Escarcega / Escárcega** ⬅ *the brief's flagged top risk* | **Addressed head-on and ruled out.** The brief was right that Escárcega is the far more common Mexican/Spanish surname — but it is **not this man's**. CMS NPI for `Escarcega` in TX returns 4 people, **none** of them him (Ana, Andrea RBT, Lydia LPC, Ricardo RDH — no radiology, no Southwest X-Ray). CourtListener returns 1,792 unrelated `Escarcega` parties nationwide, **none** connected to Akumin or El Paso imaging. Meanwhile *his own* federal records, his own site, and the Akumin docket caption all read **-zaga**. One aggregator (ZoomInfo-class) did list a stray "Veronica **Escarcega**" next to "Veronica Escarzaga" for the same company — that is exactly the aggregator contamination the brief predicted, and it is noise, not a record. |
| **Ezcarzaga** | CMS NPI: **0**. CourtListener: **0**. |
| **Escarzega** | CMS NPI: 1 hit — `ELIZABETH ESCARZEGA, OTR, San Francisco CA` — an occupational therapist in California, **not our man**. CourtListener: 22 unrelated parties, none El Paso/imaging/Akumin. |
| **Escárzaga** (accented) | **No accented form exists in any authoritative record.** CMS NPI for `Escárzaga`: no results. CMS NPI for `Escárcega`: no results. CourtListener for `Escárzaga`: 1 hit, which is *`Bartz v. Anthropic PBC`* (N.D. Cal.) — an incidental full-text match in an unrelated case, not a party name. All four of his own/government records render the surname **unaccented ASCII**. |
| **"Escargaza"** (Akumin's version) | CMS NPI: **0**. CourtListener: **0**. Appears only in one Akumin press release and that same release re-filed at SEC. See §3 above. |

**Accent flag, explicitly:** 🚩 **Print NO accent. `Escarzaga`, not `Escárzaga`.** Every
authoritative record is unaccented.

---

## 5. First-name finding

| Form | Status | Use it? |
|---|---|---|
| **Fernando** | His business/familiar name. Both LinkedIn profiles, Akumin PR, all trade directories. | ✅ **Use on the deck + leave-behind** |
| **Jesus Fernando** | His **legal** name. CMS NPI individual record (`first: JESUS`, `middle: FERNANDO`); Southwest X-Ray org NPI authorized official; Doximity. | Contracts / engagement letter only |
| Jesus (alone) | Used on his own professional site (`Jesus Escarzaga RPA`) and in some directory listings as "President". | Avoid on the deck — reads as a different person than Luis's "Fernando" |
| **Fernand** | ❌ **Ruled out.** Zero occurrences in any source. | No |

The brief's hypothesis of a Spanish double given name was **correct**.

**Final recommended rendering for the title page and leave-behind:**

```
Fernando Escarzaga
```

Optionally with credentials, both of which are verified federally: `Fernando Escarzaga, RDMS`.
(Use RDMS over RPA if listing one — RDMS is the credential attached to his *ownership/President*
role at Southwest X-Ray, which is the relevant capacity for this pitch.)

---

## 6. Negative results (explicit)

Every search that returned nothing, as required:

- **Texas Medical Board public license lookup** — NOT obtained. Guessed endpoint
  `public.tmb.state.tx.us/HCP_Search/...` returned HTTP 000 (does not exist) for all three
  surname variants. The real portal `https://profile.tmb.state.tx.us/` returns HTTP 200 but is an
  ASP.NET app behind a click-through disclaimer gate requiring `__VIEWSTATE`/`__EVENTVALIDATION`
  POST round-trips; not completed within the time box. **This is the one priority-1 source I did
  not land.** It is not needed for the verdict — CMS NPI is also a government record and is
  self-rendering — but it would have been a fourth confirmation.
- **Texas Comptroller Taxable Entity Search** — NOT obtained. `mycpa.cpa.state.tx.us/coa/` search
  endpoints returned HTTP 302 redirects to a session initializer; the franchise-tax search is
  session-gated and was not completed. No officer list retrieved from state entity filings.
- **Texas Secretary of State** — not attempted (SOSDirect is pay-walled and requires an account).
- **El Paso County DBA / assumed-name records** — not reached within the time box.
- **ARDMS credential verification** — blocked. `ardms.org/find-an-ardms-certified-professional/`
  returned **HTTP 403** (bot-blocked). RDMS not independently verified at the certifying body; it is
  verified on the CMS org NPI record instead.
- **LinkedIn full profiles** — blocked, **HTTP 999** (LinkedIn anti-scraping). Name spelling read
  from search-result titles only; profile bodies, credentials, and dates not retrievable.
- **ZoomInfo profile page** — blocked, **HTTP 403**. Read from search snippet only.
- **Southwest X-Ray current website** (`swxrayonline.com`) — fetched successfully but names **no**
  leadership, founder, or staff. Now footered "An AKUMIN Company."
- **Wayback Machine archived "About Us" pages** — fetched 4 snapshots
  (2008, 2011, 2015 ×2). **None name the owners.** The 2008 page's only personal name is an
  unrelated quoted figure (Roger J. Bulger, MD). No leadership/team page existed pre-acquisition.
- **SEC EDGAR full-text** — `Escarzaga`: 2 hits, both *Corporacion Durango S.A. de C.V.* (unrelated
  Mexican entity, 2005). `Escarcega`: 12 hits, all unrelated (Centennial Specialty Foods, Old Mutual
  Funds). `Escargaza`: 1 hit = the Akumin re-filed PR (#9). **No El Paso / Southwest X-Ray principal
  named in any other SEC filing.**
- **Birth year ~1956** — **NOT VERIFIED.** No authoritative source consulted carries a birth year.
  CMS NPI does not publish DOB. TMB online verification *does* publish birth year, but TMB was not
  landed (above). Radaris/people-aggregator results were deliberately **not** used — aggregator
  PII of unverified provenance, and irrelevant to the deliverable. **Treat ~1956 as UNVERIFIED.**
  It does not matter for the deck.
- **Veronica Escarzaga** — appears in the Akumin PR (as "Escargaza") and in one aggregator employee
  directory, where a competing "Veronica Escarcega" spelling also appears. **Her** spelling is
  therefore **UNVERIFIED**; she has no CMS NPI record found. **Do not print Veronica's name**
  without separate verification. The verdict in §1 covers Fernando only.
- **El Paso news archives** (El Paso Times / El Paso Inc. / El Paso Matters) — no substantive hits
  surfaced naming him; not separately paywall-penetrated.
- **Leroy Candelaria / Desert Imaging** — not re-derived. Brief's statement that Escarzaga did NOT
  found Desert Imaging was not contradicted by anything found.

---

## 7. Open questions only Luis can answer

1. **Does he go by "Fernando" in a business setting, or does anyone call him "Jesus"?** Records show
   both are legitimately his. The deck will say *Fernando* — low risk, since every business-facing
   source uses it, but Luis can confirm in one sentence.
2. **Is he the sole principal Rick should name, or should Veronica Escarzaga be on the deck too?**
   She appears to be a co-principal (named second in the Akumin PR). Her spelling is **not**
   verified and she has no NPI record found. If she should appear, get the spelling from Luis.
3. **Preferred professional rendering** — bare name, `Fernando Escarzaga, RDMS`, or with a title?
4. **Is he still the "RPA/RDMS practicing clinician" in Luis's framing, or purely the capital
   partner?** Affects whether to lead with his clinical credentials at all.
5. **Confirm the ~1956 birth year is irrelevant** — nothing in the deck should reference age.

---

## Standing-memory cross-checks performed
- ✅ Confirms memory note `luis-partner-fernando-escarzaga.md` spelling as correct.
- ➕ **New fact for that memory note:** legal name is **Jesus Fernando Escarzaga**; the "Jesus
  Escarzaga, President" and "Fernando Escarzaga, CEO" listings are **one person, not two**; the
  **RDMS sits on the Southwest X-Ray org NPI** and the **RPA on his individual NPI**.
- ➕ **New fact:** Akumin's own 2019 press release **misspells** him "Escargaza" — if Rick or anyone
  else ever sources the name from that PR or its SEC exhibit, they will get it wrong.
- 🔒 Litigation substance deliberately not researched or recorded, per prohibited-topic rule.
  Docket used for spelling only. **Never mention Akumin or the sale to him.**
- 🔒 No contact attempted with any person or entity. All observation read-only, public records.
