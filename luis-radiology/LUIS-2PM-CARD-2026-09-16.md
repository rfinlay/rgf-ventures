# LUIS — 2:00 PM CARD
**Wed 2026-09-16 · his house · 30 min on site · you have everything you need**

Mac mini tailnet IP: **100.67.156.31** (verified live 13:15 today)
Tailnet: **rfinlay813@outlook.com** — if the console shows *gmail*, you are in the dead one
Hostname to assign: **luis-pacs** · Console: login.tailscale.com/admin/machines

---

## BEFORE YOU DRIVE — 60 seconds
- [ ] **Auth key still alive?** It was made last night with a **1-day expiry**. Open the admin
      console → Settings → Keys. If it expired, generate a new one: **Reusable OFF,
      Ephemeral OFF, tag:pacs SELECTED.** The tag is the whole security control.
- [ ] Key photo on your phone, readable
- [ ] Plaud charged — but **ask before switching it on**

---

## STEP 0 — THE GATE (ask before anything)
> **"Is this your machine, or did Southwest X-Ray issue it?"**

| Answer | Do |
|---|---|
| His own laptop, he's local admin | **Proceed** — expected case |
| Issued / domain-joined | **STOP. Do not install.** |

Confirm in PowerShell:
> `whoami /groups | findstr /i "Administrators"`

> `systeminfo | findstr /i "Domain"`
`BUILTIN\Administrators` = admin. `Domain: WORKGROUP` = standalone, good.

**Why it's a hard stop:** you cannot put remote-access software on a clinical org's managed
endpoint on a 1099 contractor's say-so, no matter how much admin he has.

---

## THE COMMANDS (in order)

**2 — join, shields up**
> `tailscale up --authkey=KEY --hostname=luis-pacs --shields-up --accept-routes=false`
`--shields-up` blocks all inbound *including yours*. Looks like failure. It isn't.

**3 — THE CHECK THAT MATTERS MOST**
Admin console → Machines → `luis-pacs` → **owner column**

| Reads | Meaning |
|---|---|
| **tag:pacs** | Correct, proceed |
| **rfinlay813@** | **STOP** — remove node, fix key, rejoin |

If it's user-owned, `autogroup:self` gives that clinical box full access to your mini —
finance data, personal files, whole workspace. Wrong direction.

**4a — prove the block**
> `Test-NetConnection 100.67.156.31 -Port 22`
**`TcpTestSucceeded : False` is the PASS.**
**Do NOT use `tailscale ping`** — TSMP answers regardless of ACLs and will mislead you.

**4b — drop the shield**
> `tailscale up --reset --authkey=KEY --hostname=luis-pacs --accept-routes=false`

**5 — remote access**
> `Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0`

> `Start-Service sshd`

> `Set-Service -Name sshd -StartupType Automatic`
Create a **standard, non-admin** local user `rgfsvc`. Never use Luis's own login.

**5c — acceptance test, from your Mac**
> `ssh rgfsvc@luis-pacs "hostname && whoami"`
Real output = the visit succeeded.

**6 — clean up, the key is in his history**
> `Remove-Item (Get-PSReadlineOption).HistorySavePath`

---

## 7a — THE 90 SECONDS THAT ARE WORTH THE DRIVE
**Have Luis do it. Don't touch his authenticated session.**
Chrome → F12 → **Network** tab → load a study → read the **Type** column.

| You see | Means |
|---|---|
| jpeg / png / webp / websocket frames | **Server-rendered pixels — no DICOM at his desk.** Integration = browser extension, HL7 feed, or upstream DICOM |
| application/dicom / .dcm / WADO-RS | **Real DICOM arrives.** Tier 2 extraction is plausible |

**🔴 DO NOT SAVE A HAR FILE.** It captures response bodies = PHI written to disk. This is the
single most likely accidental PHI capture of the whole visit, and it happens right here.
Screenshot the **Type column only**.

SSH cannot see a browser. This is why it must happen on site.

---

## DON'T LEAVE WITHOUT — the volume numbers
Asked **twice in writing, never answered.** He'll say out loud what he won't email.
- **How many calcium studies per week?**
- **Minutes per case now, vs the old 20?**

This is the pricing blocker and the E&O timing decision. **Four numbers. Write them down.**

---

## MONEY — say this, not that

**1. FORGIVE THE PAST FIRST — before any number, unprompted**
> "Everything built so far is yours, free and clear. There is no invoice coming for any of it.
> I want to be clear about that before we talk about anything going forward."

Unconditional. Not a bargaining chip. The unspoken fear of a retroactive invoice is the single
biggest threat to this relationship — if you name a price first, he hears everything through it.

**2. Direction, not a total.** Commercial from **Oct 1**, because that's what pays for insurance,
a real agreement, and continued patching of a clinical tool he signs reports out of.
Frame as **durability, not money.** Ask for the **reference** as the exchange.

**3. The license — anchor on list, never say "$1,200" alone**

| Published list | **$1,490/yr** |
|---|---|
| Founding Clinician Credit | **-$290** (visible, dated, named on the invoice) |
| His price | **$1,200/yr, both modules** |
| Renewal | a **percentage** off then-current list, not a frozen dollar |
| Billing starts | **2026-10-01** |
| Licensor | **RGF Global Ventures LLC**, not you personally |

**4. 🔴 DO NOT PITCH THE RETAINER.** If he asks for a number:
> "Something like a thousand a month for a block of hours, and we'll size the block once we
> see the real pace."
Then move on. **Never say "80 hours"** — $1,000/80 = $12.50/hr.

**5. Bugs are always free, forever.** Say it out loud if it comes up.

**Not decided, do not promise:** E&O timing · new module pricing · any total, date, or signature.

---

## TWO THINGS HE DOESN'T KNOW
**TI-RADS — have him flip the toggle, 30 seconds.** "Justified" report detail already prints
every scored feature and the point total per nodule (shipped Sept 2). Default is **Concise**,
which is why he's never seen it. Toggle sits above the report preview.
Either it satisfies his 09-09 ask, or it proves he wants **verbatim ACR guideline text** — the
only genuinely new work. **Get his exact wording**, it prints into a report he signs.

**Paste behavior changed.** A second paste now **adds-or-flags** instead of overwriting.
He doesn't know. If you don't tell him, he files it as a bug.

---

## THE HONEST LIKELY OUTCOME
Exa is zero-footprint server-side rendering. His workstation probably receives **pixels, not
DICOM** — there may be nothing to extract at his desk.

**That is not a wasted trip, that is the answer.** It would mean the real paths are a browser
extension, an HL7 ORU feed, or DICOM obtained upstream. Worth the drive to know instead of
architecting against a guess.

---

## WHILE YOU'RE ON THE BOX — note, don't capture
- Local DICOM listener? dcm4che, Horos, any viewer installed?
- **Exa Voice running?** It's nVoq and cloud-based — if his instance uses it, Southwest X-Ray
  has **already accepted a cloud PHI processor.** Useful in a BAA talk: you're not introducing
  a new risk category.
- `manage-bde -status C:` — BitLocker on = a lost laptop is secured PHI, **not reportable**.
  Off = reportable, notice owed in 5 business days.

---

## NO-PHI DOCTRINE — characterize the pipe, never the water

| Do | Don't |
|---|---|
| Probe with invalid identifiers | Query with real patient IDs |
| C-ECHO to prove a listener answers | C-MOVE / WADO retrieve |
| Screenshot empty states | Screenshot a worklist or open study |
| Note a feature exists | Open a study to see how it renders |

**Plaud: ask first, pause whenever a real study is on screen.** Audio catching a spoken patient
name creates PHI in RGF's custody, outside any BAA. Highest-risk item of the visit.

---

## BEFORE YOU LEAVE
- [ ] `ssh rgfsvc@luis-pacs` returned real output
- [ ] PowerShell history cleared
- [ ] **Four volume numbers written down**
- [ ] Browser observation recorded (Type column, no HAR)
- [ ] Past work forgiven out loud
- [ ] TI-RADS toggle flipped in front of him
- [ ] Told him about the paste change
- [ ] **Text me the scope grant** when you want the scan to run:
      *"Scope approved: read-only enumeration on luis-pacs. No PHI-bearing paths,
      no browser profile, no DICOM retrieve."*
      Without that exact grant I run nothing.

**Not today:** no scanning on site · no RadAssist components · no PHI · no total quoted ·
no retainer · nothing signed.
