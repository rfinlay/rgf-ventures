# Runbook: Corporate Email + Calendar for RGF Global Ventures

**Written:** 2026-10-10 · **Owner:** Rick · **Status:** ready to execute on Rick's go
**Goal:** a business email address on a domain RGF owns, with a **real calendar** that can
**originate** meeting invites, managed side-by-side with the personal calendar in the
**desktop Outlook app** on both the PC and the Mac mini.

**Nothing in this runbook is purchased or changed yet.** Rick executes; Gio does not buy on
his behalf.

---

## Decision summary (why this shape)

| Question | Answer | Why |
|---|---|---|
| New domain or reuse `rgf-ventures.com`? | **Buy `rgfglobalventures.com`** | Verified AVAILABLE 2026-10-10. No live mail stack to dismantle → removes the silent-SPF-failure class of bug entirely. Matches the LLC name exactly. |
| Which plan? | **M365 Business Standard, $14/user/mo annual** | Business Basic ($7) **excludes the installed desktop apps**, and desktop Outlook on two machines is the entire requirement. |
| Which registrar? | **Cloudflare Registrar** (~$10-12/yr at cost) | At-cost pricing, free WHOIS privacy, no upsell maze. Not Northwest (~$39/yr), not GoDaddy. |
| What about `rgf-ventures.com`? | **Leave it completely alone** | Working Northwest mail stack, paid through 2027-03-18. Untouched = free fallback. Later, add as an alias domain if wanted. |
| Use the new address for Luis? | **NO — use `rfinlay813@outlook.com`** | See "Luis exception" below. |

### ⚠️ The Luis exception — do NOT let this runbook gate the client work

The imaging-center dinner is **~2026-10-20**. Every existing Luis artifact carries
`rfinlay813@outlook.com`. **Use that address for all Luis communication through the dinner
and the follow-up.**

Reasons, in order of weight:
1. A **cold, brand-new domain** has no sending reputation and is materially more likely to be
   spam-filtered. The emails that must not vanish are the ones around a $30k proposal.
2. Switching addresses mid-engagement makes a prospect re-verify who you are.
3. Mail migrations inside a client window are how deliverability incidents happen.

Start using the new address on the **next** relationship, and let reputation build on
low-stakes mail first.

### One honest caveat on the liability rationale

Rick's stated driver is separation / liability protection. Straight answer: **an email address
is professionalism and hygiene, not a liability shield.** LLC protection comes from the entity,
the operating agreement, and not commingling funds — not from the From: header. Worth doing
anyway; just not load-bearing legally, and not a reason to rush it before 10-20.

---

## Prerequisites

- A payment method Rick controls (business card preferred, for clean books).
- ~45-60 minutes of uninterrupted time. **Do not start this the day of a client meeting.**
- Admin access to the Mac mini and the PC for the final client step.

---

## Phase 1 — Buy the domain (~10 min, ~$10-12/yr)

1. Go to `dash.cloudflare.com` → sign in or create an account.
2. **Domain Registration → Register Domain**. Search `rgfglobalventures.com`.
3. Register it. Registrant: **RGF Global Ventures LLC** (the entity, not Rick personally).
4. Immediately after purchase, set:
   - **Registrar Lock: ON**
   - **WHOIS privacy: ON** (free at Cloudflare)
   - **Auto-renew: ON**

**Verify before moving on:**
```bash
curl -s -o /dev/null -w "%{http_code}\n" -L \
  https://rdap.verisign.com/com/v1/domain/rgfglobalventures.com
# expect 200 (= now registered). 404 means the purchase did not complete.
dig +short NS rgfglobalventures.com    # expect cloudflare.com nameservers
```

> **Note on method:** a plain `whois` returns empty for many `.com` lookups, which *reads* like
> "available" and is not — the query simply failed. Always use RDAP, and always run a
> known-taken control (`rgf-ventures.com` → 200) in the same session to prove the check works.

---

## Phase 2 — Buy Microsoft 365 Business Standard (~15 min, $14/user/mo annual)

1. Go to `microsoft.com/microsoft-365/business` → **Microsoft 365 Business Standard**.
2. Choose **annual commitment** ($14/user/mo; monthly billing costs more per month).
3. Quantity: **1 user** for now.
4. When asked to create an account, choose **"I want to use a domain I already own"** and enter
   `rgfglobalventures.com`.
   - If the flow insists on an `onmicrosoft.com` tenant first, accept it — the custom domain
     gets added in Phase 3. The `onmicrosoft.com` name is permanent and invisible to
     recipients; pick something neutral like `rgfglobalventures`.
5. Create the admin account. **Store the password in Keychain, not in a file:**
   ```bash
   security add-generic-password -s m365-rgf-admin -a <admin-upn> -w
   # prompts for the password; never pass -w <value> inline (it lands in shell history)
   ```
6. Enable **MFA on the admin account** before anything else. This account controls company
   email; it is the single most valuable credential RGF will own.

> **⚠️ Tenant separation:** this is a **brand-new, independent tenant**. It does not touch and
> cannot be affected by UMGC's tenant. Confirmed: the Office apps on this Mac are licensed by
> UMGC (tenant `704ce3d6-a4bf-4e09-8516-d52840c9f7a9`), which is entirely separate.

---

## Phase 3 — Add the domain + DNS records (~20 min)

In **admin.microsoft.com → Settings → Domains → Add domain** → `rgfglobalventures.com`.

Because the domain is at Cloudflare, Microsoft may offer automated setup. **Decline it and add
records manually** — you want to see exactly what lands in the zone.

### 3a. Verify ownership

Microsoft shows a TXT value unique to the tenant:

| Type | Name | Value | TTL |
|---|---|---|---|
| TXT | `@` | `MS=msXXXXXXXX` (from the portal) | 3600 |

In Cloudflare DNS, add it with **Proxy status: DNS only** (TXT records are never proxied).
Then click **Verify** in the portal. Usually under 5 minutes.

### 3b. Mail + client autoconfiguration records

**Take every value from the Microsoft 365 admin portal, not from this table.** The portal's
`Settings → Domains → rgfglobalventures.com → DNS records` page is authoritative for *your*
tenant. The table below is the expected shape so you can sanity-check what the portal shows.

| Type | Name | Value | Priority | TTL |
|---|---|---|---|---|
| MX | `@` | `rgfglobalventures-com.mail.protection.outlook.com` | 0 | 3600 |
| CNAME | `autodiscover` | `autodiscover.outlook.com` | — | 3600 |
| TXT | `@` | `v=spf1 include:spf.protection.outlook.com -all` | — | 3600 |

Notes, each one a real failure mode:

- **MX hostname pattern:** domain with dots replaced by hyphens, so
  `rgfglobalventures.com` → `rgfglobalventures-com.mail.protection.outlook.com`. **Confirm the
  exact string in the portal** rather than hand-constructing it.
- **MX priority 0, and it must be the ONLY MX record.** Multiple MX records split mail
  between providers and produce intermittent, maddening delivery. (Not a concern on a fresh
  domain — just never add a second.)
- **Exactly ONE SPF record per domain.** Two TXT records starting `v=spf1` is a permanent
  SPF error, not a merge. Verified live 2026-10-10: `spf.protection.outlook.com` publishes
  Microsoft's sender ranges and ends in `-all`.
- **Start SPF at `~all`** (soft fail) for the first week, then move to `-all` once real mail is
  flowing and nothing legitimate is failing. Hard-failing on day one is how you discover a
  forgotten sender the expensive way.
- **Cloudflare proxy:** MX / TXT / SPF are **DNS only**. `autodiscover` is a CNAME to Microsoft
  and must also be **DNS only** — proxying it breaks Outlook autoconfiguration.
- **The `autodiscover` CNAME is the single most-forgotten record.** Its absence looks like
  "Outlook keeps asking me for server settings."

> **⚠️ Possible 2026 MX format change — verify, don't assume.** A third-party guide claims
> Microsoft is moving new domains to an `mx.microsoft` endpoint with DNSSEC/DANE support for
> domains provisioned after July 2026. **Microsoft's own reference doc (updated 2026-08-20)
> mentions `mx.microsoft`, DANE, and DNSSEC exactly zero times** and still documents
> `mail.protection.outlook.com`. So: **use whatever the admin portal gives you.** If the portal
> shows an `mx.microsoft` value, that is correct and current for your tenant; use it instead of
> the table above. Do not force the legacy value to match this runbook.

### 3c. DKIM (do this, it is not optional in 2026)

1. **admin.microsoft.com → Settings → Domains**, or Defender portal → **Email & collaboration
   → Policies & rules → Threat policies → Email authentication settings → DKIM**.
2. Select `rgfglobalventures.com`. The portal gives **two CNAMEs**:

| Type | Name | Value |
|---|---|---|
| CNAME | `selector1._domainkey` | `selector1-rgfglobalventures-com._domainkey.<tenant>.onmicrosoft.com` |
| CNAME | `selector2._domainkey` | `selector2-rgfglobalventures-com._domainkey.<tenant>.onmicrosoft.com` |

3. Add both at Cloudflare (**DNS only**), then return and **toggle DKIM signing ON**.
   Enabling before the CNAMEs resolve throws an error — add records first, then toggle.

### 3d. DMARC — start permissive, tighten after proof

| Type | Name | Value | TTL |
|---|---|---|---|
| TXT | `_dmarc` | `v=DMARC1; p=none; rua=mailto:<admin-upn>; fo=1` | 3600 |

**Start at `p=none`.** It reports without quarantining, so a misconfiguration shows up in
reports instead of silently eating mail. After Phase 5 passes and a week of clean reports,
move to `p=quarantine`.

> This is deliberately the *opposite* of the existing `rgf-ventures.com` setup, which sits at
> `p=quarantine`. On a domain with no sending history, hard policy plus an unnoticed SPF/DKIM
> gap equals invisible mail loss.

---

## Phase 4 — Create the mailbox (~5 min)

1. **admin.microsoft.com → Users → Active users → Add a user.**
2. Create `richard.finlay@rgfglobalventures.com` (keeps the naming convention already in use).
3. Assign the **Business Standard** license.
4. Set display name **Richard Finlay**.
5. **Enable MFA** on this account too.
6. Optional but recommended: add `rick@rgfglobalventures.com` as an **alias** on the same
   mailbox. Aliases are free and receive mail; this reserves the shorter form.

---

## Phase 5 — Prove it works BEFORE relying on it (~15 min)

Do not skip. Each check catches a specific, known failure.

### 5a. DNS propagated correctly

```bash
D=rgfglobalventures.com
echo "--- MX (expect ONE record, priority 0, *.mail.protection.outlook.com or portal value)"
dig +short MX $D
echo "--- SPF (expect EXACTLY ONE v=spf1 line)"
dig +short TXT $D | grep spf1
echo "--- autodiscover (expect CNAME to autodiscover.outlook.com)"
dig +short CNAME autodiscover.$D
echo "--- DKIM selectors (expect both to resolve)"
dig +short CNAME selector1._domainkey.$D
dig +short CNAME selector2._domainkey.$D
echo "--- DMARC (expect p=none for now)"
dig +short TXT _dmarc.$D
```

**Count the SPF lines.** More than one `v=spf1` is a hard failure, not a warning.

### 5b. Real mail, both directions

1. From `rfinlay813@outlook.com`, send **to** `richard.finlay@rgfglobalventures.com`. Confirm
   arrival at `outlook.office.com`.
2. **Reply from** the new mailbox back to `rfinlay813@outlook.com`.
3. In the received copy, open raw headers and confirm:
   - `spf=pass`
   - `dkim=pass`
   - `dmarc=pass`

   **All three must pass.** Anything else means stop and fix before using the address.
4. Send one test to a **Gmail** address (`rfinlay813@gmail.com`) and confirm it lands in
   **Inbox, not Spam**. Gmail is the strictest common receiver and the best early warning.

### 5c. The actual requirement — calendar invites

1. In the new mailbox, create a calendar event and **invite `rfinlay813@outlook.com`**.
2. Confirm the invite arrives **as an invitation with Accept/Decline buttons**, not as a plain
   attachment, and that the **organizer shows the `@rgfglobalventures.com` address**.
3. Accept it, and confirm it appears on the personal calendar.

This is the capability that does not exist today and the whole reason for the project.

---

## Phase 6 — Wire up the desktop clients (~10 min)

### Mac mini

1. Outlook → **Settings → Accounts → Add Account** → the new address.
2. It must detect **Microsoft 365 / Exchange automatically** via the autodiscover CNAME. If it
   prompts for server names, **stop** — autodiscover is wrong; recheck 5a.
3. Confirm the sidebar now shows, under **Calendar**, both `rfinlay813@outlook.com` **and**
   `richard.finlay@rgfglobalventures.com`.

> **This is the success criterion for the whole runbook.** Today the calendar sidebar contains
> only `rfinlay813@outlook.com`, because the `rgf-ventures.com` account is plain IMAP with no
> calendar. Two calendar entries = done.

4. Set the **default sending account** deliberately. If business mail should be the default,
   set it; otherwise leave personal as default to avoid sending personal mail from the business
   address by reflex.

### PC

Same flow. Both machines use the same Exchange mailbox, so calendar state syncs server-side —
no import/export, no .pst, no .olm.

### Graduation note (Spring 2027)

The **apps** on the Mac are licensed by UMGC and will drop to reduced-functionality mode at
graduation. Business Standard **includes desktop app rights**, so once this tenant is live and
the account is signed in, Outlook/Word/Excel stay fully licensed through RGF. This runbook
quietly removes the graduation cliff as a side effect.

---

## Phase 7 — Decommission and cleanup (do NOT rush this)

**Wait at least 30 days** of clean operation on the new domain first.

1. Tighten SPF `~all` → `-all` (after a week of clean mail).
2. Tighten DMARC `p=none` → `p=quarantine` (after clean DMARC reports).
3. **`rgf-ventures.com`:** flip **Registrar Lock ON** at Northwest — it is currently **OFF**,
   a standing finding from 2026-09-15 and still true.
4. Review the **8 Northwest Active Services** (5 never reviewed). Some bundles convert to paid
   at the **2027-03-18** renewal. Decide what to keep before that date.
5. Optional, only once the new domain is proven: add `rgf-ventures.com` to the tenant as an
   **alias domain** so `richard.finlay@rgf-ventures.com` delivers into the same mailbox. This
   **requires cutting its MX + SPF to Microsoft** — the exact silent-failure step this plan was
   designed to avoid, so do it as a deliberate, standalone task with its own verification, far
   from any client deadline. Not required for anything.
6. Remove the IMAP `richard.finlay@rgf-ventures.com` account from Outlook once it carries no
   unique mail.

---

## Rollback

Each phase is independently reversible, which is the point of the clean-domain approach:

| If this fails | Rollback |
|---|---|
| Phase 3-5 (DNS/mail broken) | Nothing to restore. `rgf-ventures.com` and the personal accounts were never touched. Fix the records and re-run Phase 5. |
| Phase 2 (wrong plan) | M365 subscriptions are cancellable; annual commitments are refundable within **7 days** of purchase. |
| Phase 1 (wrong domain) | Domain registrations are **not refundable**. This is the only irreversible ~$12. |

**The existing Northwest mail stack on `rgf-ventures.com` is never modified by Phases 1-6.** It
remains a working fallback throughout.

---

## Cost summary

| Item | Cost | Cadence |
|---|---|---|
| `rgfglobalventures.com` (Cloudflare) | ~$10-12 | per year |
| M365 Business Standard, 1 user | $14/mo = **$168** | per year, annual commitment |
| **Year 1 total** | **~$178-180** | |

For comparison: Business Basic would save $84/yr but does not license the desktop apps, which
is the requirement. Google Workspace Business Starter is $7/user/mo but moves calendaring off
Outlook-native.

---

## Verified facts behind this runbook (checked 2026-10-10)

- `rgfglobalventures.com` **AVAILABLE** — Verisign RDAP 404, with `rgf-ventures.com` → 200 as a
  working control.
- `spf.protection.outlook.com` resolves and publishes Microsoft's sender ranges, ending `-all`.
- `autodiscover.outlook.com` resolves (→ `autodiscover.outlook.cloud.microsoft`).
- M365 pricing **rose 2026-07-01**: Basic $6→**$7**, Standard $12.50→**$14**, Premium $22.
- Business Basic **excludes desktop apps** — confirmed on Microsoft Learn and microsoft.com.
- `richard.finlay@rgf-ventures.com` appears **nowhere** in RGF materials; Luis artifacts carry
  `rfinlay813@outlook.com` (×10) and `rfinlay813@gmail.com` (×7).
- Northwest mail on `rgf-ventures.com` = Dovecot IMAPS 993 + Postfix SMTPS 465, Roundcube
  webmail, **no CalDAV and no calendar plugin**.
- Office on this Mac is licensed by UMGC tenant `704ce3d6-a4bf-4e09-8516-d52840c9f7a9`; both
  `@outlook.com` addresses are consumer MSAs holding no tenant license.
