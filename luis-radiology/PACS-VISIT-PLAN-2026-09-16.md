# PACS Visit Plan — Dr. Luis Ramos, Wed 2026-09-16, 2:00 PM

**Goal:** stand up remote access to Luis's reading workstation, then scan the environment to answer
one question: **how does DICOM data get out of Exa PACS, and what integration path is actually real
on this instance?**

**Status of this doc:** planning. Supersedes nothing; executes `PACS-recon-plan.md` (2026-07-31) with
the access mechanics and the authority question added.

---

## 0. The thing to settle before anything is installed

**Luis is a 1099 independent contractor. The PACS is not his.** He reads for an imaging operation on
`exa.swxrayonline.com` (Exa Platform, Konica Minolta). He has **admin on his own workstation**; that is
not the same as authority over the PACS.

Rick said "approved through his IT for full access." That needs one clarifying question before we
install, because the answer changes the whole shape of the engagement:

**Whose IT approved, and approved what exactly?**
- If **Luis's own** setup (his box, his home office, he owns it) → workstation access is his to grant.
  Proceed as planned.
- If the **imaging group / Akumin / the PACS operator's** IT approved → get it **in writing**, even one
  email. That email is the artifact that makes this a legitimate engagement rather than an
  independent contractor quietly letting a third party onto a clinical endpoint.

**This is not a compliance stall.** Per [[phi-raise-dont-gate]], raise and keep moving. The install and
the technical scan proceed tomorrow either way. What the answer changes is whether we touch anything
PHI-bearing, and whether the BAA gets signed this week or later.

**BAA status: unsigned template** with blank Covered Entity name, address, and effective date
(`BAA-RGF-Ramos.md`). PACS integration is the exact trigger the phi-raise-dont-gate rule names as
where formal work starts. **Bring it. Don't force it.**

---

## 1. What Rick needs before 2:00 PM Wednesday

### On Gio's side (I do these — say go and they're done today)

| Item | Status | Note |
|---|---|---|
| Tailnet live | ✅ `rfinlay813@outlook.com` / `taila9a1b3.ts.net`, 4 nodes | verified live |
| Mac mini node | ✅ `gios-mac-mini` 100.67.156.31 | this machine |
| **ACL isolation for `luis-pacs`** | ❌ **NOT SET — no node has tags** | **must do before the node joins** |
| Auth key for the install | ❌ not generated | pre-generate so no Tailscale login happens on his box |

**The ACL gap is the real prep item.** Right now the tailnet is a flat default-allow network. If
`luis-pacs` joins as-is, that clinical workstation can reach the Mac mini — which holds finance data,
Rick's personal files, and the whole workspace. **That is the wrong direction of exposure and it is
the one that matters.** A clinical endpoint should not be able to route into personal infrastructure.

Fix is a tagged ACL: tag the node `tag:pacs`, allow `gios-mac-mini → luis-pacs:22` only, deny
everything from `tag:pacs` outbound to the rest of the tailnet.

### On Rick's side (physical, at the house)

1. **Laptop or just your phone** — the install is on *his* machine, not yours. You mostly need hands
   on his keyboard and a browser.
2. **A pre-generated Tailscale auth key** (I'll produce it) so you never type Rick's Tailscale
   credentials into a client workstation. Pre-auth key, reusable=false, ephemeral=false,
   tagged `tag:pacs`, short expiry.
3. **The BAA**, printed or on a tablet. Offered, not pushed.
4. **Plaud recorder** — yes, same as the discovery session. **Ask before switching it on**, and per
   the standing rule keep PHI off it. If a real study is on screen, pause the recorder.
5. **The onboarding card / nothing else to install** — this visit is access + recon, not a build.

### On Luis's side (what Rick asks him to have ready)

- Workstation powered on and logged in, with his normal Exa session available.
- **A de-identified or test study** he can drive, or willingness to drive a real one while we look
  only at mechanism and never capture. Ideally the former.
- Fifteen quiet minutes where he's not mid-read.

---

## 2. Install sequence at the house (~30 min)

Do these in order. Stop at any step that doesn't come back clean.

**Step 1 — Tailscale (10 min).**
Install from tailscale.com/download on his Windows box. Join with the **pre-generated auth key**, not
by signing into Rick's account on that machine. Set hostname `luis-pacs`. Verify from the Mac mini:
`tailscale status` shows `luis-pacs` online.

**Step 2 — Confirm the ACL actually bit (5 min).** This is the step people skip.
From `luis-pacs`, try to reach `gios-mac-mini`. **It should fail.** If it succeeds, the ACL isn't
applied and we stop until it is. Verifying isolation means proving the block, not trusting the config.

**Step 3 — OpenSSH Server + a dedicated non-admin account (10 min).**
Windows Settings → Optional Features → OpenSSH Server → start the service, set to Automatic. Create a
**dedicated non-admin local user** for remote access — not Luis's account, not an admin. Key-based
auth, no password login. Verify SSH from the mini.

**Step 4 — Prove it end to end, then leave.**
One command from the Mac mini that returns real output from his box. That's the deliverable for the
visit. Everything else is bonus.

**What NOT to do tomorrow:** no scanning while you're standing there, no installing RadAssist
components, no config changes to Exa or the browser. Get access, prove it works, ask the questions
below, leave. The scan is the follow-up and it's better done unhurried.

---

## 3. Questions for Luis (the real payload of this visit)

Ordered so it reads as a conversation, not an interrogation. The top three are the ones that change
the architecture.

### Authority and scope
1. **Who approved this, and would they put it in an email?** Framed helpfully: *"so I've got something
   on file showing this was sanctioned, which protects you more than me."*
2. **Is the workstation yours, or does the imaging group own it?**
3. **Who do you actually read for** — Akumin, a teleradiology group, several? Who operates
   `swxrayonline.com`?

### The DICOM question (the stated goal)
4. **Does the Exa viewer ever let you export or download a study?** Any "export", "burn CD",
   "download DICOM", "send to" option. *This is the single highest-value answer of the visit.*
5. **Are the images rendered server-side, or does anything land on the machine?** Sherlock's research
   says Exa is Zero Footprint with server-side rendering — meaning **pixels come down as rendered
   images, not DICOM**. If that holds, there may be **no DICOM on his workstation at all**, and the
   integration path is not a local agent. Confirm rather than assume.
6. **Is there a second path to images** — a CD burner, a share drive, a modality he can reach, an
   old-fashioned Q/R tool?
7. **Who would we ask for a DICOM node / AE title?** Even if the answer is "no idea," the name of the
   person is the deliverable.

### The report side
8. **Voice: Exa Voice (nVoq) or PowerScribe/Fluency?** Changes the whole report-automation surface.
9. **The report editor** — plain text box or a structured widget? (Rick can just look.)
10. **Can you export a worklist?** Any CSV/report export. Feeds the reconciliation idea.

### The one that's been asked twice in writing and never answered
11. **Volume numbers.** *"How many calcium studies in a typical week, and how long does one take you
    now versus the twenty minutes before?"*

    **Ask this in person. It is the pricing blocker.** Per [[radassist-pricing-decision]] the $1,200/yr
    against $1,490 list can't be defended without it, and the E&O timing decision depends on it too.
    He answers questions out loud that he doesn't answer by email. **Do not leave the house without a
    number, even a rough one.**

### Also worth surfacing while you're there
12. **TI-RADS guidelines per nodule after the impression** — open since 2026-09-09, re-asked, no answer.
    It prints into a report he signs, so don't guess at it.
13. **The second-paste behavior change** — he was emailed before the merge fix landed, so he doesn't
    know a second capture now adds-or-flags instead of overwriting. Tell him or he files it as a bug.

---

## 4. What the scan produces (the follow-up, not tomorrow)

Executes `PACS-recon-plan.md` sections A–D over SSH. Output is a **technical environment map +
integration-options assessment, no PHI**, answering:

- Is there DICOMweb (QIDO/WADO/STOW) reachable on this instance?
- Is there any DICOM listener, or is the endpoint purely a browser?
- What does the Exa web app actually call? (network layer, metadata only, no payloads)
- Is a browser extension viable against the report editor DOM?
- What's the local footprint for a future on-prem agent?

**Standing guardrails, unchanged from the recon plan:** no real patient records, de-identified/test
only, retain nothing patient-related, read-only, node ACL-isolated.

---

## 5. The honest read

**Rick pushed for Tailscale→PACS on 2026-08-06 and I pushed back — right endgame, wrong sequence.
The sequence has now earned it.** Luis went live in production, validated three real patients clean,
shipped thyroid, and *he* volunteered the workstation. That's a different situation than August.

**But the likeliest technical outcome of this scan is "there is no DICOM here."** Exa is a
zero-footprint, server-side-rendered web PACS. If the architecture is what Konica Minolta advertises,
his workstation never receives DICOM — it receives rendered pixels. **That is not a failure of the
visit; it's the answer, and it's worth the trip to know for certain.** It would mean the real
integration paths are (a) a browser extension against the live Exa session, (b) an HL7 ORU feed
arranged with whoever operates the PACS, or (c) DICOM obtained upstream at the source rather than at
his desk.

**The most valuable thing that happens tomorrow is probably not technical.** It's getting the volume
numbers, the authority answer, and the name of the person who controls the PACS interfaces.

---

## References
- `PACS-recon-plan.md` — the scan procedure (2026-07-31)
- `sherlock-exa-integration-research.md` — Exa architecture + integration surface research
- `BAA-RGF-Ramos.md` — unsigned template
- [[phi-raise-dont-gate]] · [[radassist-pricing-decision]] · [[radassist-unified-platform-roadmap]]
