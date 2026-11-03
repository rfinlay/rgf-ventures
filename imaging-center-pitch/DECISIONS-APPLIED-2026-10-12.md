# Decision Record: Rick's internal review, closed 2026-10-12

> **Slide numbers in this record are the 24-slide deck of 2026-10-12.** On 2026-10-14 the deck became
> 26 slides: report assistance is new at 18, and the engagement slide ("slide 22" below) is now slide 26
> in a two-slide appendix after the Thank You. The current map is in `RUNBOOK-2026-11-05.md`. This record
> is history and was not renumbered.

**Supersedes `CHANGE-LOG-PENDING-RICK-REVIEW.md`.** The review freeze is LIFTED. Rick approved the
final pass on 2026-10-12 and these edits are **applied, not proposed.** The documents are now frozen
for rehearsal, not for review.

**Rick's instruction, verbatim intent:** one final update pass so he can rehearse against stable
documents. No further content changes unless a rehearsal with Luis produces one, or Sherlock's payer
mix research comes back with something that must be said differently.

---

## ⚠️ CANONICAL SOURCE WARNING, found during this pass

There are **two divergent copies** of this document set:

| Location | Status |
|---|---|
| `~/OneDrive/Desktop/Imaging-Center-Pitch-2026-10-20/` | **CANONICAL.** Matched the verified 2026-10-10 revert backup byte for byte before this pass. All 10-12 edits are here. |
| `~/.openclaw/workspace/projects/rgf-ventures/imaging-center-pitch/` | **STALE.** Older (Oct 6-8) and smaller on every file. Diverged before the 10-10 revert. |

The workspace copy was never updated after the 10-06 pass. **Edit only the OneDrive set.** The
workspace copy should be either deleted or replaced with a copy of the OneDrive set; leaving a second
plausible-looking source directory in place is how a correct edit lands in a document nobody reads.

Pre-edit backup of this pass: `.bak-20261012-pre-final-pass/`

---

## The seven review items and what happened to each

### 1. Owner reporting / agent: do not promise anything live by a date ✅ APPLIED

**Rick's call (2026-10-10), reaffirmed 10-12.** Keep the deck as-is, promise nothing live by a date,
and if the partners later want something live before a date, scope and price it then. The ground Gio
had missed: **the infrastructure was never priced.** A reporting agent needs a host, a database, an
LLM API bill that scales with use, auth, backups, and monitoring, which is a recurring line in the
*client's* operating budget forever. Promising it live without that number is the same error as
quoting a prior auth agent against an unchosen RIS.

**Applied:**
- `RUNBOOK-2026-11-05.md`: new objection section **"We want something of yours live before a specific
  date"** with the scoping-question answer, the neutral-not-defensive framing instruction, and the
  stated cost of the position.
- `SPEAKING-NOTES-2026-11-05.md`: same content in SLIDE 22 depth.
- Deck presenter notes on the engagement slide: condensed version.
- One line added to the Phase 2 description in the runbook and the notes: **each specification carries
  its own fixed build price.**
- **Slide 22 visible content and the leave-behind pricing panel: UNCHANGED.** $12k + $18k, 90-day
  gate, $30k, said once.

**The position to hold:** *"If you want something live before a specific date, tell me which piece and
we'll scope it."* Not a no, not a yes-with-a-date.

**Known cost, written down so it is not a surprise at the table:** Rick has no day-one deliverable of
his own. If Fernando asks what he has on opening day, the honest answer is a contracted vendor stack
that works plus a set of priced specifications.

### 2. Automation's effect on their hiring ✅ APPLIED, VERBAL ONLY

**Rick's concern (2026-10-10):** do not let automation recommendations cause them to hire prior-auth
staff they later have to let go. **Rick's call on the open question (10-12): verbal, per Gio's
recommendation.** It is NOT a named deliverable on slide 22. Decide with Luis on 10-15.

**Why verbal.** Luis is the only person who can say how Fernando thinks about payroll. Adding a
deliverable to slide 22 before testing it on Luis is exactly the mistake the minimalist position was
adopted to avoid.

**Applied:**
- `RUNBOOK-2026-11-05.md`: new objection section **"Should we hire for prior auth, or will your
  automation cover it?"** with the spoken answer, the both-ways failure analysis, and the framing rule.
- `SPEAKING-NOTES-2026-11-05.md`: SLIDE 23 depth now carries a ⚠️ instruction to volunteer the
  guardrail immediately after the "a hire or a system" bullet, because that bullet as written invites
  exactly the wrong conclusion.
- Deck presenter notes on the engagement slide: one-line reminder to volunteer it.
- **Not on any slide and not in the leave-behind.**

**FRAMING, NON-NEGOTIABLE.** Never *automation reduces headcount.* Always **automation changes what
your people do.** For a greenfield center scaling from zero that is also the truer claim: no existing
job is eliminated, they are avoiding hires otherwise needed around month eighteen. Growth absorption,
not reduction.

### 3. El Paso payer mix is all four channels 🔄 SHERLOCK DISPATCHED 2026-10-12

**Rick's call: send Sherlock.** Research dispatched 2026-10-12. Output will land at
`projects/rgf-ventures/imaging-center-pitch/SHERLOCK-RESEARCH-2026-10-12-elpaso-payer-mix.md`.

Five questions: channel shares for an El Paso center; VA community care referral and authorization
mechanics including the current CCN regional administrator; TRICARE West prior-auth and referral rules
for advanced imaging by Prime vs Select and beneficiary category; whether either military channel is
reachable by the FHIR/API story or is a separate manual track; and reimbursement reality across all
four.

**NOTHING about TRICARE, VA, or Medicare enters any document until it is verified.** No document was
edited for item 3 in this pass.

**Interim safe answer if it comes up before the research lands:** the El Paso mix is distinctive, the
automation design has to handle the military and Medicare channels on their own terms rather than as
commercial variants, and pinning those mechanics down is exactly what Phase 1 does before a vendor is
signed. That converts a gap into scope without inventing a fact. **Do not quote shares, rules, or
rates.**

### 4. Slide 22 pricing structure: confirmed correct ✅ APPLIED (notes only)

Rick confirmed the structure on 10-12: everything is a written spec before opening, build priced from
the spec after opening, and $30k holds whether it is one center or three. The logic is consistent, the
design engagement is flat because the spec is written once and deployed three times, and the four
access terms are negotiated once across all three contracts.

**Applied:** the "does that change at three centers?" answer now sits next to the price in the runbook
"How much?" section, in SLIDE 22 depth in the speaking notes, and in the deck's presenter notes.
Previously it lived only on slide 9, thirteen slides earlier, which meant page-flipping mid-objection.
A buyer starts counting centers the moment he hears a price, so it belongs in the same breath.

### 5. Billing vendor gap ✅ APPLIED, OPTION B (seventh scorecard row)

**Rick's call: add the row,** per Gio's recommendation. The gap Rick caught: the scorecard had six
rows and two buys, billing was not a row at all, yet billing is charged for in Phase 1 on slide 22 and
in the spoken price line. The deck charged for a billing evaluation it never justified, and Fernando
has reconciled real remittances for twenty years.

**Applied:**
- Deck scorecard slide: seventh row, **"Billing, claims, and the eligibility feed / Buy / Commodity
  clearinghouse function. I evaluate reachability and contract terms, not the claims work. Row 1 reads
  the feed; it does not replace the vendor."** Speaker note updated to **"three of the seven, I am
  telling you to buy."**
- Leave-behind: row 8 added with the same content, "Declined" renumbered to row 9.
- Speaking notes SLIDE 16: spoken line updated to three-of-seven, plus the full prepared answer.

**A contradiction was caught and resolved while applying this.** `AUTOMATION-CANDIDATES.md` #2 rates
*eligibility verification* as **BUILD** (the first stage of the prior auth pipeline), while the new
scorecard row rates billing/eligibility as **BUY**. A careful listener hears eligibility on both sides
of the buy/build line, and Fernando is a careful listener. The row was reworded to name the **feed**
rather than the function, and all three documents now carry the disambiguating sentence:

> "I am not building an eligibility system. Your billing vendor already has that transaction; the EDI
> 270/271 eligibility check is the oldest standardized surface in this business and every clearinghouse
> exposes it. What I build is the thing that reads it and acts on it, which is the part nobody sells
> you. That is also why the access terms in that billing contract matter to me."

**This is the seam to rehearse.** Fumbled, the slide stops being a credibility move and becomes
something Fernando has to untangle.

### 6. Desert Imaging ✅ NO CHANGE NEEDED, already prohibited

**Rick's call: never say it,** per Gio's recommendation. Drop it rather than resolve it; Southwest
X-Ray is confirmed and is the only credential worth referencing.

**Verified across all documents 2026-10-12: it was already fully handled and no edit was required.**
Desert Imaging appears nowhere as an assertion. It appears only as a **prohibition** in runbook
landmine #2, row 2 of the speaking-notes landmine strip, and a do-not-name line in
`AUTOMATION-CANDIDATES.md`, plus the source research file. The founder is **Leroy Candelaria**, a
radiopharmacist, not Fernando.

### 7. Freeze violation of 2026-10-10 ✅ CLOSED, no action

Six files were edited mid-freeze on 10-10 and the PDFs re-rendered. Rick caught it, the revert
completed at 18:18 the same day, every file verified byte-identical to its backup, and all four PDFs
scanned clean for the promise language. On the record, not reopened. The lesson is recorded in
`memory/freeze-blocks-file-writes-not-just-sends.md`.

---

## Meeting dates, corrected 2026-10-12

**Two events, not one, and only one of them is confirmed.**

1. **Full-deck rehearsal with Luis: CONFIRMED Thursday 2026-10-15, 2:00 PM MT.** Luis only. Walk the
   full deck including the numbers. *(The prior plan file labeled 10-15 a Wednesday; 2026-10-15 is a
   Thursday. The date is right, the weekday label was wrong.)*
2. **The Fernando dinner: approximately 2026-10-20, NOT confirmed.** Every document in this set is
   written for that room.

A header block flagging both was added to the top of the runbook and the speaking notes.

### Still open, to settle with Luis on 10-15

1. **The price reaction.** Does $30k land, is it high for Fernando, or should no number be shown at
   all? If Luis says no number: run without slides 22-24 and hand over a leave-behind with no pricing
   panel. **Do not argue him out of it.** The no-numbers deck variant is still unbuilt.
2. **The staffing plan**: named Phase 1 deliverable on slide 22, or stay verbal? Verbal as written.
3. **ASK 11**: "access to three imaging centers," which three, operating today? Unanswered since
   2026-10-01 and it is a scope-and-price question.
4. **Is 10-20 still the Fernando date?**
5. ⚠️ **The real opening target.** Every timeline claim, including the CMS-0057-F / FHIR argument,
   is anchored on "six months from the call with Luis," and that call's date was never pinned down.
   **~April 2027 is an assumption, not a fact, throughout these documents.** Confirm it with Luis
   before any date is said in front of Fernando.

---

## Verification performed on this pass

- Zero hits across all four documents for the reverted promise language: `running the day you open`,
  `specified and built`, `built and live for opening`, `live for opening day`.
- Zero em dashes in the runbook, speaking notes, and deck (standing style rule). 13 were introduced
  during drafting and all 13 were removed.
- No headcount-reduction language anywhere except the landmine prohibition itself.
- Pre-edit backup taken before any write: `.bak-20261012-pre-final-pass/`
- PDF re-render, page-count verification, and the Google Drive dual-sync were run as a separate
  verified step; see the journal entry for 2026-10-12.
