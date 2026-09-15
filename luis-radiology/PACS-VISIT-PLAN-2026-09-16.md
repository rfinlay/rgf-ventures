# PACS Visit Plan — Dr. Luis Ramos, Wed 2026-09-16, 2:00 PM

**Goal:** stand up remote access to Luis's reading workstation, then run a **read-only infrastructure
assessment** — no PHI — that answers three questions: **can DICOM data get out of Exa on this
instance, what does the Exa deployment actually look like, and which integration surface is real
here (DICOM / DICOMweb / HL7 / browser extension)?**

**Scope discipline, Rick's words 2026-09-15:** *"we want to avoid reading any HIPAA-protected PHI
data... we're just looking at the Exa PACS layout, to understand how we can integrate with it and
how we can pull DICOM data. It's just an infrastructure assessment."* That sentence is the scope of
work. Section 4A turns it into rules the scan is actually held to.

**Status of this doc:** planning. Supersedes nothing; executes `PACS-recon-plan.md` (2026-07-31) with
access mechanics, the authority question, the tier model, and the no-PHI scan doctrine added.

---

## 0. The thing to settle before anything is installed

**Luis is a 1099 independent contractor. The PACS is not his.** He reads for an imaging operation on
`exa.swxrayonline.com` (Exa Platform, Konica Minolta), operated by **Southwest X-Ray**. He has
**admin on his own workstation**; that is not the same as authority over the PACS.

Rick said "approved through his IT for full access." That needs one clarifying question before we
install, because the answer changes the whole shape of the engagement:

**Whose IT approved, and approved what exactly?**
- If **Luis's own** setup (his box, his home office, he owns it) → workstation access is his to grant.
  Proceed as planned.
- If **Southwest X-Ray's** IT approved → get it **in writing**, even one email. That email is the
  artifact that makes this a legitimate engagement rather than an independent contractor quietly
  letting a third party onto a clinical endpoint.

**This is not a compliance stall.** Per [[phi-raise-dont-gate]], raise and keep moving. The install and
the technical scan proceed tomorrow either way. What the answer changes is whether we touch anything
PHI-bearing, and whether the BAA gets signed this week or later.

**BAA status: being drafted against Southwest X-Ray** (`BAA-RGF-SouthwestXray-DRAFT-2026-09-16.md`,
2026-09-15). Supersedes `BAA-RGF-Ramos.md`, which named the wrong counterparty — **Luis cannot sign a
BAA for a PACS he does not own.** Bring it, don't force it. The companion analysis answers whether a
no-PHI infrastructure assessment triggers BA status at all.

---

## 0A. The tier model — what this assessment is actually deciding

Rick's framing, 2026-09-15: **a three-tier product, starting at the tier with no PHI whatsoever, or
PHI local-only.** The strategic goal is to **stay in Tier 1 as long as possible** and only accept a
PHI-bearing architecture when a feature genuinely cannot be delivered without it.

| Tier | PHI posture | How the agent gets data | BAA? |
|---|---|---|---|
| **1 — where we are, and where we want to stay** | **No PHI to RGF.** Anything patient-identifying stays in the browser on Luis's machine. | Radiologist-initiated: screen capture OCR, clipboard, manual entry. RadAssist is the workspace. | **Arguably not**, if no PHI ever reaches RGF systems. **Confirm, don't assume** — see the analysis doc. |
| **2 — the prize, if DICOM is reachable** | PHI transits a **local** path (workstation / on-prem agent). No PHI leaves the site. | Agent **pulls structured data** into RadAssist: DICOM Q/R, DICOMweb, or an HL7 ORU feed. Kills the OCR decimal problem outright. | **Yes.** Local-only is not the same as no-PHI. Rick said this himself. |
| **3 — the expensive one, avoid if possible** | Agent **acts inside PACS**. Broadest exposure. | Agent interacts with Exa directly: browser extension writing into the report editor, or a session-level agent. | **Yes, unambiguously**, plus a real security review and vendor/ToS questions with Konica Minolta. |

**The decision this visit informs:** Rick's stated preference is *"if we can pull the data, the agent
operates within RadAssist"* — Tier 2. **Tier 3 is the fallback for the surfaces where no data path
exists.** The scan's job is to tell us which surfaces fall into which tier, so Tier 3 is a deliberate,
scoped exception rather than the default architecture.

**Three things worth holding in view:**

**Tier 2 is the one that pays for itself.** The [[verify-behavior-not-diffs]] problem with the thyroid
prefill is that OCR has no arithmetic safety net for nodule measurements — a dropped decimal turns
1.8 cm into 18 cm and changes the recommendation. **Structured data has no decimal to lose.** If the
scan finds a real data path, it doesn't just save effort; it removes an entire class of clinical risk
that currently blocks shipping thyroid prefill.

**The tiers are per-feature, not per-product.** Calcium prefill might live at Tier 1 forever while
thyroid measurement ingestion needs Tier 2. Don't let one feature's requirement drag the whole
product into a higher tier.

**Exa Voice already sends PHI to a cloud.** Per Sherlock's research, Exa's native dictation is
**nVoq, cloud-based**. Southwest X-Ray has therefore already accepted a cloud PHI processor in this
workflow. That is useful context for a BAA conversation: RGF would not be introducing a novel risk
category. **Verify this is what his instance runs** — Q8 in section 3.

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
12. **TI-RADS guidelines per nodule after the impression.** **Verified in code 2026-09-15 — this is
    NOT an untested build awaiting deployment. It is shipped, live, and documented.** The "Justified"
    report detail level is on `main` (`0ea1587`, 2026-09-02), it prints every scored feature and the
    point total per nodule via `nodule-line.ts` / `describeTirads`, and the live guide at
    `radassist.app/new-features.html` (HTTP 200) walks him through it, including the physician-override
    case. **Default is Concise, which is why he has not seen it.**

    **So the ask of Luis is not "please test a new build." It is a disambiguation he owes us**, open
    since 2026-09-09 and re-asked in the Sep 9 email. He asked for "TI-RADS guidelines for the specific
    nodules after the impression," which could mean three different reports:
    - **(1) per-nodule management recommendation** — already prints for actionable nodules
    - **(2) how the category was reached** — **already exists, this is the Justified toggle**
    - **(3) the ACR guideline text itself** per category, printed verbatim for a nurse or referrer —
      **this one does not exist and is the only one that would be new work**

    **Ask him to flip the toggle in front of you.** Preview panel, Concise → Justified. Thirty seconds,
    and it either answers his request outright or proves it is option 3. **If it is option 3, get his
    exact wording** — it prints into a report he signs, so it should be his language, not ours. Also
    settle his **default** (Concise or Justified), which lives under the Thyroid template tab.

    *No deploy, no lower-environment test, and no new-features guide update is required for this item.*
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

Each finding maps to a tier (0A) so the output is an **architecture decision**, not a list of ports.

---

## 4A. No-PHI scan doctrine — how "avoid PHI" becomes a rule instead of an intention

Rick's instruction is to avoid reading PHI entirely. The risk is not that we go looking for it; it is
that **a PACS workstation has PHI on screen and in memory by default**, so avoidance has to be
designed rather than intended.

**The governing principle: characterize the pipe, never the water.** Every question this assessment
asks is about *structure* — does an endpoint exist, what does it speak, what does it return for an
empty or invalid query. None require a real patient.

**Rules the scan is held to:**

1. **Metadata and transport only.** Record endpoints, ports, protocols, HTTP status codes, response
   headers, auth mechanisms, TLS config, software versions, DOM structure. **Never response bodies
   that could carry patient data.**
2. **Probe with deliberately empty or invalid identifiers.** A DICOMweb QIDO endpoint answers "do you
   exist and do you speak this" with a malformed accession just as well as a real one. `C-ECHO`
   proves a DICOM listener without moving a single study. **A 401 or a 400 is a complete answer.**
3. **No C-MOVE, no C-GET, no WADO retrieve, no STOW.** Nothing that transfers a study. Q/R
   capability is established by `C-ECHO` plus configuration, not by pulling an image.
4. **If a real worklist is unavoidably on screen, photograph nothing and copy nothing.** Describe
   structure in prose: "worklist is an HTML table, roughly 9 columns, accession and MRN appear to be
   columns 2 and 3." That is the finding. The values are not.
5. **Browser DevTools: Network tab headers and request URLs only.** Do not save a HAR — **a HAR file
   captures response bodies and would persist PHI to disk.** This is the single most likely accidental
   capture of the entire visit, and it is the one to consciously avoid.
6. **Screenshots only of an empty state** — login screen, settings panel, an empty search, an About
   dialog. If Luis wants to show a real study, watch over his shoulder and capture nothing.
7. **Retain nothing patient-related.** Scan artifacts land in `luis-radiology/scan-2026-09-16/` and
   are reviewed before commit. **If a PHI-bearing artifact is created by accident, it is deleted
   immediately and the fact is logged** — logged, because an unlogged near-miss is one that repeats.
8. **Read-only throughout.** No configuration changes, no service installs beyond Tailscale and
   OpenSSH, nothing written to the PACS.

**The honest caveat, stated plainly:** doing this work at a clinical workstation means **incidental
exposure is possible even under perfect discipline**. Luis may open a study to demonstrate something.
That is a meaningful difference from a deliberate PHI access, and it is precisely why the
authorization question in section 0 gets asked before anything is installed rather than after. **The
scan can be designed to avoid PHI. It cannot be designed to guarantee zero incidental exposure at a
live reading station** — so the paperwork and the technique both have to do their share.

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

**And "no DICOM at his desk" does not mean Tier 2 is dead.** It means Tier 2 doesn't live on his
workstation. Sherlock verified that **HL7 v2 interfacing is a first-class, supported Exa integration
path** — provisioned by Konica Minolta per site, not self-serve. So the structured-data route may run
through **Southwest X-Ray and KM**, not through Luis's machine. That reframes the deliverable:
the highest-value thing Rick can leave with may be **the name and email of whoever owns the Exa
interface configuration at Southwest X-Ray.** A relationship with that person is worth more than any
port we find.

**The worst outcome is not "no path found." It is defaulting into Tier 3 by accident** — building a
browser extension because it's the only thing reachable without asking anyone, and quietly taking on
the broadest PHI exposure and a Konica Minolta ToS question along the way. **Tier 3 should be a
decision, made with the BAA signed and the vendor question answered. Not a path of least resistance.**

---

## References
- `PACS-recon-plan.md` — the scan procedure (2026-07-31)
- `sherlock-exa-integration-research.md` — Exa architecture + integration surface research
- `tailscale-acl-2026-09-16.hujson` + `tailscale-acl-README.md` — node isolation policy (2026-09-15)
- `BAA-RGF-SouthwestXray-DRAFT-2026-09-16.md` + `BAA-SouthwestXray-ANALYSIS.md` — current BAA (2026-09-15)
- `BAA-RGF-Ramos.md` — **superseded**, named the wrong counterparty
- `../../radassist-app/RESEARCH-phi-persistence.md` — PHI persistence analysis, informs the BAA
- [[phi-raise-dont-gate]] · [[radassist-pricing-decision]] · [[radassist-unified-platform-roadmap]]
