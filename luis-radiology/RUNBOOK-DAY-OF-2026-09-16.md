# PACS Visit Runbook — Wednesday 2026-09-16, 2:00 PM

**VERSION 3** — adds the money conversation (license, forgiveness, retainer-hold).

**Location:** Luis's house · **Duration target:** 30 minutes on site
**Goal:** get durable remote access to the PACS workstation, answer the open questions, leave.
**Not today:** no scanning while standing there, no RadAssist components, no PHI.
**Not today, money:** no total quoted, no retainer pitched, nothing signed.

---

## STATUS: prep is complete

All of this was verified on the evening of 2026-09-15. Nothing below is assumed.

| Item | State |
|---|---|
| Tailscale ACL policy | **APPLIED** to tailnet `rfinlay813@outlook.com` |
| `tag:pacs` exists and is selectable | **YES** |
| `tag:pacs` as an ACL source | **ABSENT** — this is the security control |
| Policy tests (4 assertions) | **PASSED** — a failing test blocks the save |
| Your existing SSH rule | **PRESERVED** |
| Your existing Funnel grant | **PRESERVED** |
| Your 4 nodes | correctly **untagged** (do not tag them) |
| Auth key `luis-pacs 2026-09-16` | **GENERATED**, tagged `tag:pacs`, 1-day expiry, single-use |
| Key in your possession | **YES** — photo on your phone |

**There is nothing left to configure before you leave.**

**The one thing still unconfirmed is on his end, not yours: that the workstation is his own hardware and he is local admin. Step 0 settles it in under a minute.**

---

## Key facts to have in front of you

| | |
|---|---|
| Your Mac mini tailnet IP | **100.67.156.31** |
| Tailnet | `rfinlay813@outlook.com` (NOT the Gmail one) |
| Hostname to assign | `luis-pacs` |
| Admin console | login.tailscale.com/admin/machines |

**Account warning:** if the Tailscale admin console shows `rfinlay813@gmail...` in the corner, you are in the dead ghost tailnet. Switch to the Outlook account. The right one shows 4 machines.

---

## STEP 0 — WHOSE MACHINE IS THIS? (do this first, it is a gate)

**The single question that resolves both ownership and authority at once:**

> **"Is this your machine, or did Southwest X-Ray issue it?"**

**Expected answer: it is his own laptop, he is local admin, and he reaches PACS through a browser session at `exa.swxrayonline.com`.** That is the configuration this entire runbook assumes.

| Answer | What you do |
|---|---|
| **His own hardware, he is local admin** | **Proceed.** This is the expected case. |
| **Southwest X-Ray issued it / domain-joined** | **STOP.** Do not install. |

**Why the second case stops the visit:** installing remote-access software on a clinical organization's managed endpoint is not something a 1099 contractor can authorize, no matter how much admin he happens to have. That is not "Luis approved it." Get written approval from whoever actually runs that machine, or do not install.

**This also makes the BAA question concrete.** On his own hardware, a no-PHI infrastructure assessment does not trigger business-associate status. On their hardware, that analysis does not apply.

### Verify admin rights before touching the installer

Open **PowerShell** and run:

```
whoami /groups | findstr /i "Administrators"
```

**`BUILTIN\Administrators` in the output = he has it.** Five seconds, removes the guesswork.

**Admin is required for every step that follows** — the Tailscale installer writes a system service and a virtual network adapter, `tailscale up` needs an elevated shell, `Add-WindowsCapability` installs OpenSSH Server at system level, creating the `rgfsvc` account is administrator-only, and `manage-bde -status` needs elevation. **There is no non-admin path through this runbook.**

**Also confirm it is domain-free** while you are there:

```
systeminfo | findstr /i "Domain"
```

`Domain: WORKGROUP` means standalone, his own machine. A real domain name means it is managed by an organization — see the STOP row above.

---

## BEFORE YOU INSTALL ANYTHING — ask these

### 1. Whose IT approved this?

Luis is a 1099 contractor. The PACS at `exa.swxrayonline.com` belongs to **Southwest X-Ray, which is an Akumin company**. Admin rights on his own laptop is not authority over someone else's clinical system.

**This raises a question, it does not gate the install** — provided Step 0 confirmed the hardware is his. What the answer changes is whether you touch anything PHI-bearing and when a BAA gets signed. If the imaging group approved, ask for one email confirming it — framed as protecting Luis more than you.

### 2. May I record?

**Ask before switching the Plaud on.** Per the BAA analysis this is the single highest-risk item of the visit: audio catching a spoken patient name converts incidental exposure into PHI created and held by RGF, outside any BAA.

**Pause it whenever a real study is on screen.**

### 3. Is the workstation ready?

Powered on, Exa session available, and fifteen minutes when he is not mid-read.

---

## STEP 1 — Install Tailscale on the workstation

Download from **tailscale.com/download/windows** and run the installer.

**Do not sign in through the GUI.** Do not type your Tailscale credentials into his machine. The auth key replaces that entirely.

---

## STEP 2 — Join the tailnet with the tagged key

Open **PowerShell as Administrator**, then:

```
tailscale up --authkey=PASTE_KEY_HERE --hostname=luis-pacs --shields-up --accept-routes=false
```

**`--shields-up` blocks ALL inbound to his box, including your own SSH and RDP.** That is intentional. You prove the outbound block first, then drop the shield in Step 4. **It will look like a failure if you forget this.** It is not.

---

## STEP 3 — THE CHECK THAT MATTERS MOST

On your phone or laptop: **login.tailscale.com/admin/machines** → find `luis-pacs` → look at the owner column.

| It reads | Meaning |
|---|---|
| **`tag:pacs`** | Correct. Proceed. |
| **`rfinlay813@`** | **STOP.** The tag did not apply. |

**Why this is the one failure mode that matters:** if the node is user-owned instead of tagged, `autogroup:self` covers it, and ACL rule 1 gives that clinical workstation full access to your Mac mini — finance data, personal files, the whole workspace.

**Recovery:** remove the node from the admin console, verify the auth key had `tag:pacs` selected, generate a fresh key if needed, and rejoin.

---

## STEP 4 — Prove the block, then drop the shield

### 4a. Prove the workstation CANNOT reach your Mac

On his machine, in PowerShell:

```
Test-NetConnection 100.67.156.31 -Port 22
```

**`TcpTestSucceeded : False` is the PASS.** Repeat for `-Port 3389` and `-Port 445` if you want more confidence.

**Do NOT use `tailscale ping` to test this.** It sends a TSMP probe that Tailscale answers regardless of ACLs. TSMP succeeding while real connections fail is the *signature of the ACL working correctly*, not a failure. Using it here will mislead you.

### 4b. Drop the shield

Once 4a returns False:

```
tailscale up --reset --authkey=PASTE_KEY_HERE --hostname=luis-pacs --accept-routes=false
```

---

## STEP 5 — Enable remote access

### 5a. Install OpenSSH Server

In the Administrator PowerShell:

```
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
```

### 5b. Create a dedicated non-admin account

**Do not use Luis's own login.** A separate account means his credentials are never yours, and access can be revoked without touching his profile.

Create a standard (non-administrator) local user. Name it something obvious like `rgfsvc`.

### 5c. Prove it end to end from YOUR Mac

This is the acceptance test. From the Mac mini:

```
ssh rgfsvc@luis-pacs "hostname && whoami"
```

**It must return real output.** If it does, you have durable access and the visit succeeded.

---

## STEP 6 — Clean up before you leave

**Clear the key from his PowerShell history** — the auth key is in it:

```
Remove-Item (Get-PSReadlineOption).HistorySavePath
```

**Then leave.** Do not start scanning. The assessment is better done unhurried from your own desk — see Step 7 for how that actually works.

---

## STEP 7 — HANDOFF TO GIO (how the assessment actually gets done)

**The access exists so Gio can run the assessment remotely, later, from the Mac mini. This section is the contract for that.**

### What Gio CAN do over SSH

Enumerate what is installed and running on that workstation: processes, listening ports, installed software, services, filesystem layout, network configuration, whether a DICOM listener exists, BitLocker status. That is a real picture of the machine and it is most of the infrastructure question.

### What Gio CANNOT do — read this before planning around it

**Gio cannot see his screen.** SSH is a command line on a Windows box. **Exa PACS is a browser session** — server-side rendered pixels in Chrome, authenticated as Luis.

**So the single most important question of this engagement — what does the Exa client actually deliver to that workstation, pixels or DICOM — is NOT answerable over SSH.** It requires a human looking at the browser.

**That is why the browser observation below is an on-site task and not something to leave for later.** Nobody should plan around a capability that does not exist.

### 7a. ON-SITE TASK: the browser observation (90 seconds, highest value of the visit)

**Have Luis do this, or watch him do it. Do not do it yourself in his authenticated session.**

1. In Chrome, open **DevTools** (F12) → **Network** tab
2. Load a study in Exa
3. Look at the **Type** column on the requests that carry the image

| What you see | What it means |
|---|---|
| `jpeg`, `png`, `webp`, or a websocket carrying frames | **Server-side rendered pixels.** There is no DICOM at his desk. Integration is a browser extension, an HL7 feed, or upstream DICOM. |
| `application/dicom`, `.dcm`, or a WADO-RS URL | **Real DICOM reaches the workstation.** Tier 2 structured extraction becomes plausible. |

**Write down what you see, or photograph the DevTools panel with no patient data visible.**

**DO NOT save a HAR file.** DevTools' "save all as HAR" captures response bodies, which would persist PHI to disk. This is the single most likely accidental PHI capture of the entire visit, and it happens right here, in this step. **Screenshot the Type column only.**

### 7b. What Rick owes Gio before any remote scan runs

**Gio will not run anything on that box without an explicit scope grant from you.** Text or say:

> *"Scope approved: read-only enumeration on luis-pacs. No PHI-bearing paths, no browser profile, no DICOM retrieve."*

**Gio's default without that grant is to run nothing.**

### 7c. What Gio will run, and what Gio will not touch

| Will run | Will not touch |
|---|---|
| Installed programs, services, running processes | Anything under the Chrome/Edge user profile |
| Listening ports, network config, firewall rules | Any file in a study, cache, or image directory |
| Whether a DICOM listener answers `C-ECHO` | `C-MOVE`, WADO retrieve, or any study transfer |
| BitLocker status, OS build, patch level | Any path containing patient identifiers |
| Whether Exa Voice (nVoq) is present | The Exa session or any authenticated state |

**Timing:** evenings, when Luis is not logged into a study. Lowest PHI exposure surface, and an unhurried scan is a better scan.

### 7d. After the assessment

**Remove `luis-pacs` from the tailnet.** The tagged key disables node key expiry, so the node persists until removed manually. Standing remote access to a clinical endpoint is what walks RGF toward business-associate status — the BAA analysis flags this specifically. Time-box it or paper it.

---

## THE QUESTIONS — do not leave without these

### Volume numbers (asked twice in writing, never answered)

- **How many calcium studies per week?**
- **Minutes per case now, versus the old twenty?**

This is the pricing blocker on $1,200/yr against $1,490 list, and the E&O timing decision rides on it. **He answers out loud what he will not answer by email.**

---

## THE MONEY CONVERSATION — what to say, and what NOT to say

**Goal today: forgive the past, name the direction, get the numbers. Do NOT close, quote a total, or propose the retainer.** Full terms: [[radassist-pricing-decision]].

### 1. Forgive the past work FIRST — explicitly, out loud, before any number

Roughly **$12,000-$18,000** of work is already done and unbilled. Per the market analysis Section 8.4, **the unspoken fear that a retroactive invoice is coming is the single biggest threat to this relationship.** If you name a price before closing that door, he hears the whole conversation through it.

Say it plainly, in your own words, something like:

> "Everything built so far is yours, free and clear. There is no invoice coming for any of it. I want to be clear about that before we talk about anything going forward."

**Do not soften it, do not make it conditional, and do not attach it to the ask.** It is a statement, not a negotiating chip.

### 2. Name the direction, do NOT quote a total

**What to say:** the tool goes commercial starting **October 1**, because that is what pays for the insurance, the real agreement, and a commitment to keep patching a clinical tool he signs reports out of.

**Frame it as durability, not money.** He is not buying software, he is buying the assurance that it will still be maintained in two years.

**Ask for the reference as the exchange.** That is what the founding rate is actually purchasing.

### 3. The license — $1,200/yr, presented as a credit off list

| | |
|---|---|
| Published list | **$1,490/yr** |
| `Founding Clinician Credit` | **-$290** (visible, dated, named on the invoice) |
| **His price** | **$1,200/yr**, both modules |
| Renewal | **a percentage off then-current list**, NOT a frozen dollar figure |
| Billing starts | **2026-10-01**, not immediately |
| Licensor | **RGF Global Ventures LLC**, not Rick personally |

**Never present it as "$1,200."** The list price is the anchor and the credit is a named favor to him.

### 4. The retainer — DO NOT PITCH IT TODAY

Decided shape: **flat $1,000/month for a block of 8-10 hours** ($100-$125/hr effective against the $150 anchor). **It is recorded, not ready.**

**Two reasons to hold it:**

1. **The demand rate is unknown.** His four asks in one email came the week a module shipped. That is not proven steady state, and sizing a block against a spike is how you end up resenting the work in November.
2. **$1,000/mo is $12,000/yr — ten times the license.** Moving Luis from **$0 to $13,200/yr in one conversation** is a categorically bigger ask than $1,200/yr. It can sink the license too.

**If he asks for a number in the room, say exactly this and move on:**

> "Something like a thousand a month for a block of hours, and we'll size the block once we see the real pace."

**⚠️ Do not say "80 hours."** The instinct was $1,000 for 80 hours = **$12.50/hr**, a 92% discount and half a full-time job. Run the division before naming any block size.

### 5. Never bill him for a defect

A clinician who hesitates to report a bug in a clinical tool is a liability, not a customer. **Bugs are always free, forever.** Say it out loud if it comes up.

### What is NOT decided and must not be promised

- **Insurance (E&O) timing** — decide after one real Texas quote, not before. Current contract liability cap is fees paid in the prior 12 months = **$1,200**, which is close to no cap at all against a clinical claim.
- **New module pricing** (Lung/Fleischner, DICOM Agatston) — priced per module as built. **Do not quote.**
- **Any total, any contract date, any signature.**

### TI-RADS per nodule — have him flip the toggle

His 09-09 request was ambiguous. **The "Justified" report detail level already exists and already prints every scored feature and the point total per nodule** (shipped `0ea1587`, Sept 2; the live new-features guide documents it). The default is **Concise**, which is why he has never seen it. The toggle sits above the report preview.

**Have him flip it in front of you.** Thirty seconds. It either satisfies his request outright, or it proves he wants option 3:

1. Per-nodule management recommendation — **already prints**
2. How the category was reached — **this is the Justified toggle, it exists**
3. The ACR guideline text printed verbatim — **does not exist, this is the only new work**

If it is option 3, **get his exact wording.** It prints into a report he signs.

### Tell him about the paste behavior

A second paste now **adds-or-flags** instead of overwriting. He does not know this. If you do not tell him, he will file it as a bug.

---

## THE ASSESSMENT QUESTIONS — what you are actually there to learn

**Do not run scans today — Gio runs them remotely per Step 7.** These are the questions that access exists to answer. **The exception is the browser observation in 7a, which must happen on site because SSH cannot see a browser session.**

### The likeliest outcome, stated honestly

**Exa is zero-footprint with server-side rendering.** If Konica Minolta's architecture is what they advertise, his workstation receives **rendered pixels, not DICOM at all** — there may be nothing to extract at his desk.

**That is not a wasted trip. That is the answer.** It would mean the real integration paths are:

- a browser extension operating against the live session
- an HL7 ORU feed from whoever operates the PACS
- DICOM obtained upstream, not at the workstation

Worth the drive to know for certain instead of architecting against a guess.

### While you are on the machine, note (do not capture)

- Is there a local DICOM listener? Is `dcm4che`, Horos, or any viewer installed?
- Is **Exa Voice** running? It is nVoq, and **cloud-based**. If his instance uses it, Southwest X-Ray has *already* accepted a cloud PHI processor in this workflow — useful in a BAA conversation, because you would not be introducing a new risk category.
- **BitLocker status:** `manage-bde -status C:` — with full-disk encryption a lost workstation is secured PHI and **not reportable**; without it, reportable with notice owed in 5 business days.

---

## NO-PHI DOCTRINE — the rules that make this defensible

**The principle: characterize the pipe, never the water.**

| Do | Do not |
|---|---|
| Probe with **invalid** identifiers — a malformed accession proves an endpoint exists as well as a real one | Query with real patient identifiers |
| `C-ECHO` to prove a DICOM listener responds | `C-MOVE` or WADO retrieve — these move studies |
| Screenshot **empty states** only | Screenshot anything with a worklist or study open |
| Note that a feature exists | Open a study to see how it renders |

**The single most likely accidental capture of the whole visit: saving a HAR file.** DevTools' "save all as HAR" captures response bodies, which would persist PHI to disk. **Do not save a HAR.**

**Honest caveat:** the scan can be designed to avoid PHI. It cannot guarantee zero incidental exposure at a live reading station, since Luis may open a study to show you something. That is exactly why the authorization question gets settled before anything installs.

---

## AFTER THE VISIT

**Remove `luis-pacs` from the tailnet when the assessment is done.** The tagged key disables node key expiry, so the node persists until you remove it manually. Standing access to a clinical endpoint is the thing that walks you toward business-associate status — the BAA analysis flags this specifically.

**Delete the photo of the auth key from your phone**, including Recently Deleted.

---

## ROLLBACK — if you need to undo the ACL

Your previous policy was wide-open. To restore it, paste this into the JSON editor:

```
{
	"grants": [
		{"src": ["*"], "dst": ["*"], "ip": ["*"]},
	],
	"ssh": [
		{
			"action": "accept",
			"src":    ["autogroup:member"],
			"dst":    ["autogroup:self"],
			"users":  ["autogroup:nonroot"],
		},
	],
	"nodeAttrs": [
		{
			"target": ["autogroup:member"],
			"attr":   ["funnel"],
		},
	],
}
```

Tailscale's Configuration logs also support point-in-time revert.

---

## Known cosmetic issue

`laptop-2tjvbjfj` advertises subnet routes. Those approvals live on the machine, not in `autoApprovers`, so they should survive the policy change. **If a subnet route stops working**, re-approve at Machines → laptop-2tjvbjfj → Route settings. Not a failure, just a thing not to chase.

---

## One-line summary of the visit

**Get access. Do the 90-second browser check. Forgive the past work. Ask the questions. Leave. Gio scans later from the Mac mini.**

**The one thing that cannot be done later is the browser observation — Gio cannot see his screen over SSH.**

**The one thing that must be said out loud today is that the past work is free and clear.** No number lands right until that door is closed.
