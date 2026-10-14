# Plan: Full-Deck Walkthrough with Luis, **Thu 2026-10-15, 2:00 PM MT**

> **CONFIRMED by Rick 2026-10-12.** The date is 2026-10-15 at 2:00 PM MT, which is a **Thursday**;
> earlier drafts of this file labeled it Wednesday. The date was always right, the weekday was wrong.
> Decisions applied from Rick's internal review: `DECISIONS-APPLIED-2026-10-12.md`.

**Decided by Rick 2026-10-10 (voice).** Supersedes the "30-minute solo prep" framing in STATUS.md.

## The decision

Rick has **Thu 2026-10-15 at 2:00 PM MT, one hour, possibly two**, and walking the
**FULL 26-slide deck including the numbers** (24 of pitch plus the two-slide appendix that carries the engagement, as of 2026-10-14). Not the short version. Not a discovery session.

**Why this is the right call.** The STATUS.md open question was "solo prep or Fernando pitch?" Rick has
resolved it a third way: use the solo session as a **full dress rehearsal with the champion**, and get
Luis's reaction to the numbers *before* they are ever said in front of Fernando. That is strictly
better than burning the session on discovery, because the discovery questions get answered along the
way anyway.

## The explicit ask Rick wants answered in that room

> "I want to get his feedback on the numbers going in to see what he thinks so that I'm not way off
> base. Or maybe I shouldn't even show numbers at all — he'll be like, hey, don't even show numbers."

This is the single most valuable thing the session produces. **Luis is the only person who can tell
Rick how Fernando reacts to a price.** Three outcomes to be ready for:

1. **"$30k is right."** Proceed as built. Phase 1 / Phase 2 / 90-day gate stands.
2. **"$30k is high for him"** → the response is **shorten the term, never cut the rate**
   (`memory/imaging-center-engagement-pricing.md`). Offer Phase 1 alone at $12k with a hard stop.
3. **"Don't show a number at all."** → Deck runs without the appendix, slides 25 and 26; the engagement slide becomes a
   verbal "there's a scope and a price, and I'd rather earn the right to give it to you." The
   leave-behind goes home *without* the pricing panel. **Build this variant before the 15th.**

**Do not argue Luis out of #3.** He knows Fernando. Rick does not.

## ⚠️ This is still a RUNWAY problem, not just a rehearsal

Moving the walkthrough to 10-15 does **not** move the Fernando meeting, which Rick framed as "as early
as Oct 20." That leaves **five days** between Luis's feedback and the real room. Every change Luis asks
for has to be buildable in five days. Plan the session to produce *decisions*, not a wish list.

## Pre-session build (before Thu 10-15, 2:00 PM MT)

| # | Item | Why | Status |
|---|---|---|---|
| 1 | **FHIR/payer-side content** — new or revised slide | Rick's instinct was right: **the deck does not contain the word FHIR on a single slide.** It appears 33x in the HTML (notes/body text) and 51x in speaking notes, but no slide surfaces it. The 2027-01-01 payer API mandate is the single strongest "greenfield timing" argument available and it is currently invisible. | Awaiting Sherlock |
| 2 | **Add FHIR to the contract asks** | Existing deck language: *"FHIR on the RIS side is aspirational at a small center; the FHIR that matters is on the payer side."* That is defensible but it **declines a free ask**. A contract term costs nothing in October 2026. Revise to ask for it and explain why it is cheap insurance, not a requirement. | Awaiting Sherlock |
| 3 | **Agent-app / human-in-the-loop operating-model slide** | The 13 candidates have no architecture over them. Rick's words: *"human in the loop and agent API agent apps... almost automate the less expensive pieces."* Needs one slide: what the agent does, where the human signs, what the exception queue looks like. This is the answer to "what happens when I get hit by a bus" too. | **Built 2026-10-14 as slide 18** (report assistance: the agent drafts, the radiologist signs; one instance per center; the two-directions question). Architecture document page 6 carries the deployment point. |
| 4 | **Referring-physician channel** — likely the real "left on the table" | An imaging center's volume comes from referrers, and the 13-candidate inventory treats the referrer as an afterthought (#12, "Buy (RIS/PACS)", evidence: **None found**). If Sherlock finds evidence that referrer turnaround drives volume, this is a new pitch section. If he finds none, say so and drop it. | Awaiting Sherlock (Q3c) |
| 5 | **Owner-analytics depth from the DICOM feed** | Rick asked specifically about "all of the DICOM feed." Slide exists ("Studies by modality, by reader, by referrer...") but is thin. Sherlock Q2c is scoped at which DICOM tags / MPPS / RDSR fields are *reliably populated in practice* — scanner idle time and acquisition duration are the owner metrics nobody sells. | Awaiting Sherlock (Q2c) |
| 6 | **No-numbers deck variant** | Outcome #3 above. Cheap to build, and not having it means improvising in the room. | **Built 2026-10-12** (`?nonumbers`, one source). After the 2026-10-14 reorder it ends on the Thank You: 24 pages. |
| 7 | **Re-verify the deck PDF renders all 26 pages** | `pdfinfo \| grep Pages`: a JS deck prints to one page without `@media print`. Known trap: `memory/slide-deck-pdf-is-separate-artifact.md`. | **Verified 2026-10-14:** deck 26, no-numbers 24. |

## Dates: get these right, they are in the pitch

Rick said "July 1 or January 1." Neither is a single answer — **CMS-0057-F has two dates** and the one
that matters for the FHIR API is the later one:

- **2026-01-01** — payer prior-auth **decision timelines** bind (72 hrs expedited / 7 calendar days
  standard). *Already in the deck.* Live now.
- **2027-01-01** — the **payer FHIR Prior Authorization API** is required, along with Provider Access
  and Payer-to-Payer APIs. *This is the integration Rick is asking about.*

**Sherlock is verifying both against the Federal Register text (89 FR 8758) before either goes on a
slide.** Do not state a date in front of Fernando from this file alone.

**The strategic read, if the dates hold:** a center opening ~April 2027 opens *into* the mandate.
Incumbents will be retrofitting a 20-year-old stack; a greenfield center can specify it in the vendor
contract it has not signed yet. That is a sharper version of the deck's existing "six months of free
decisions" thesis — **the regulatory calendar is on their side exactly once**, and only if they ask for
it before signing.

Caveat to resolve before claiming it: the rule binds **payers, not providers**, and guarantees nothing
about data quality or ease of connection. Sherlock Q1d/Q1e is scoped on whether a small provider can
actually consume these APIs or whether clearinghouses re-intermediate them.

## Standing constraints that do not change

- **Fernando landmines:** actively suing Akumin (never mention). Did not found Desert Imaging. Never say
  **platform, roll-up, scale, synergies, density**. He is reclaiming operational control, not growing.
  → `memory/luis-partner-fernando-escarzaga.md`
- **Rick sends every client communication.** Gio never contacts Luis or Fernando directly, any channel.
  → `memory/rick-never-send-to-clients.md`
- Contract through **RGF Global Ventures LLC**, never personally.
- Only hard deadline: **Phase 1 must land before they sign vendor contracts.**
- Both artifacts go to **OneDrive Desktop AND Google Drive**, verified by Modified timestamp.
  → `memory/dual-sync-onedrive-and-drive.md`

## Open items for Rick

1. ~~Confirm 2:00 PM 10-15 with Luis.~~ **DONE, confirmed 2026-10-12: Thu 10-15, 2:00 PM MT.**
2. **Is Fernando in the 10-15 room or not?** Luis said "meet at my house." If Fernando is there, this is
   not a rehearsal and the whole plan changes.
3. **ASK 11 is still unanswered** — "access to three imaging centers," which three, are they running
   today. Live scope-and-price unknown, unverifiable from anything on disk.
4. **Is Oct 20 still the Fernando date?** Everything downstream of the 15th assumes five days.
