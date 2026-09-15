# Tailscale ACL — operator runbook (Luis Ramos PACS visit, 2026-09-16)

Companion to `tailscale-acl-2026-09-16.hujson`. Everything here was verified against current
Tailscale docs on 2026-09-15; doc URLs are cited inline and at the bottom.

**The one-sentence goal:** Luis's Windows radiology workstation joins the tailnet already tagged
`tag:pacs`, and `tag:pacs` cannot open a connection to anything — most importantly not the Mac mini.

**Current tailnet state, verified 2026-09-15** via `/Applications/Tailscale.app/Contents/MacOS/Tailscale status`:

| Tailscale IP | Hostname | Owner | OS |
|---|---|---|---|
| 100.67.156.31 | gios-mac-mini | rfinlay813@ | macOS |
| 100.107.118.42 | iphone-15-pro-max | rfinlay813@ | iOS (offline 112d) |
| 100.76.57.92 | iphone182 | rfinlay813@ | iOS |
| 100.125.123.33 | laptop-2tjvbjfj | rfinlay813@ | linux |

Four nodes, zero tags, flat default-allow. All four are **user-owned**, which is exactly why the
policy's rule 1 (`autogroup:member` → `autogroup:self:*`) keeps them all working unchanged.

---

## Do this the night before, not at Luis's kitchen table

Steps 1 and 2 happen at home on the Mac mini. Only step 3 happens at Luis's house. If the ACL is
already live and the key is already in your password manager, the on-site work is one command.

---

## Step 1 — Back up the current policy, then apply the new one

**Click path** (verified: `docs/features/tailnet-policy-file/manage-tailnet-policies`):

1. Go to **https://login.tailscale.com/admin/acls/file**
   (equivalently: admin console → **Access controls** in the top nav → **File** tab for raw HuJSON.
   The **Visual editor** tab is the point-and-click view; you want the file view for a paste.)
2. **Select all the existing text and copy it into a scratch file on the mini.** Do this even though
   you expect it to be the stock policy.

> **Saving replaces the ENTIRE policy file.** It is not a merge. Whatever sits in the editor when
> you hit Save becomes the whole policy for the tailnet. If the existing text is just the default
> starter rule (`src ["*"]`, `dst ["*:*"]`), replacing it wholesale is safe. If you ever added
> anything custom, merge it in by hand first.

3. Select all, paste in the full contents of `tailscale-acl-2026-09-16.hujson`.
4. Hit **Save**.

**What proves it worked:** the `tests` block runs automatically on every save, and *a failed
assertion causes Tailscale to reject the save with an error*
(verified: `kb/1337/policy-syntax`). So a clean save is itself the proof that
`tag:pacs` cannot reach `tag:rgf`. If it saves, the invariant held.

5. Optional extra confidence: the **Preview rules** tab lets you pick a user and list every
   destination they can reach.

**If something goes wrong:** admin console → **Configuration logs** → revert the policy file to a
previous date/time. Requires Owner/Admin/Network admin, which you are.

---

## Step 2 — Pre-generate the tagged auth key

The point: **never type Tailscale credentials into a client workstation**, and leave no window where
the node is joined but untagged. A key with the tag baked in means the node is `tag:pacs` from its
first packet.

**Click path** (verified: `kb/1085/auth-keys`):

1. **https://login.tailscale.com/admin/settings/keys**
   (admin console → **Settings** → **Keys**)
2. **Generate auth key…**
3. Set it up exactly like this:

| Option | Setting | Why |
|---|---|---|
| Description | `luis-pacs 2026-09-16 assessment` | So you recognize it later when revoking |
| **Reusable** | **OFF** (one-off) | One machine, one key. A leaked reusable key is a standing invitation |
| **Ephemeral** | **OFF** | Ephemeral nodes vanish when offline. You want this node to persist across reboots of Luis's box |
| **Pre-approved** | **ON** | Only matters if device approval is enabled; harmless otherwise, and avoids the node sitting unauthorized |
| **Expiry** | **1 day** (range is 1–90, default 90) | The key only needs to survive until the 2 PM install. Short expiry means a lost key is dead by Thursday |
| **Tags** | **ON** → select **`tag:pacs`** | The whole point. Without this the node joins user-owned and briefly unprotected |

> `tag:pacs` only appears in that Tags picker **after** step 1 is saved, because `tagOwners` is what
> defines the tag. Do step 1 first.

4. **Generate key**, then copy it into your password manager immediately. Tailscale shows it once.

**Side effect worth knowing:** applying a tag to a device for the first time **disables key expiry**
on that device (verified: `docs/features/tags`). The node will not silently drop off mid-assessment.
It also means you must explicitly remove the node when the engagement ends — see rollback.

---

## Step 3 — On Luis's Windows workstation

Install from https://tailscale.com/download/windows. Then, in an **Administrator** PowerShell or
Command Prompt:

```
tailscale up --auth-key=tskey-auth-XXXXXXXXXXXX --hostname=luis-pacs --accept-routes=false --shields-up
```

Flag by flag (verified: `kb/1080/cli`):

- `--auth-key=...` — authenticates as the tag, not as Rick. No browser login, no Microsoft account
  prompt, nothing of Rick's typed on Luis's keyboard.
- `--hostname=luis-pacs` — predictable name instead of whatever Windows calls itself.
- `--accept-routes=false` — the clinical box does not pull subnet routes from the tailnet.
- `--shields-up` — blocks *all* incoming connections at the client, independent of the ACL.

> **`--shields-up` is defense in depth, and it will also block your own SSH/RDP in.** It is the
> belt to the ACL's braces: even if the policy were wrong, nothing reaches this box. If you need
> RDP or SSH into it during the assessment, re-run without `--shields-up`:
> ```
> tailscale up --hostname=luis-pacs --accept-routes=false
> ```
> Decide deliberately. Starting shielded and dropping the shield only once you actually need a
> session is the safer order, and it means the first thing you do is prove the *outbound* block —
> which is the control that actually matters for protecting the mini.

**Do NOT** pass `--advertise-exit-node` or `--advertise-routes`. `autoApprovers` is empty, so such
an advertisement would sit pending anyway — but do not create the pending request. Do not approve
one if you see it.

`--advertise-tags` is **not** needed here; the tag rides in on the auth key.

---

## Step 4 — Prove the block. Behavior, not config.

A saved policy file is a claim. These four checks are the evidence. Run them in this order.

### 4a. FROM LUIS'S BOX — these MUST FAIL

This is the check that matters. Run it on the Windows workstation.

**The authoritative test is a real TCP connection**, not `tailscale ping`:

```
Test-NetConnection -ComputerName 100.67.156.31 -Port 22
```

**Expected: `TcpTestSucceeded : False`.** (PowerShell. It takes a few seconds to time out.)

Try a couple more ports so one closed service does not give you a false sense of security — these
must all fail:

```
Test-NetConnection -ComputerName 100.67.156.31 -Port 445
Test-NetConnection -ComputerName 100.67.156.31 -Port 5900
```

> **Do not use `tailscale ping` as your pass/fail here.** It sends a TSMP probe, which is
> deliberately *not* a normal data packet. Tailscale's own troubleshooting guidance is that
> "TSMP ping succeeds but ICMP ping fails" is the *signature of ACLs blocking traffic* — meaning
> a TSMP ping can come back fine while real connections are correctly blocked. If you run
> `tailscale ping gios-mac-mini` on the PACS box and it responds, that is **not** a failure of the
> control. Judge by `Test-NetConnection`.

> **If either of these SUCCEEDS, stop the engagement right there.** Do not proceed to the
> assessment. Run `tailscale logout` on Luis's box immediately and re-check the policy file. A
> success means the clinical workstation can reach your finance data and client work.

Also confirm it cannot see the tailnet at all:

```
tailscale status
```

**Expected:** the PACS box lists peers (peer listing is not gated by ACLs) but cannot connect to
any of them. Peer *visibility* is not peer *access* — do not misread a populated list as a failure
of the control. The `ping` and `Test-NetConnection` results are the authoritative evidence.

### 4b. FROM THE MAC MINI — this MUST SUCCEED

```
/Applications/Tailscale.app/Contents/MacOS/Tailscale ping luis-pacs
```

**Expected: success**, a pong with a latency figure. This confirms the node joined and the path is
up — but per the TSMP caveat above, treat it as a liveness check, not as proof of ACL permission.

The real proof is a TCP connection. Once OpenSSH Server is up on the Windows box (visit-plan
step 3) and you have dropped `--shields-up`:

```
nc -z -v luis-pacs 22
ssh <dedicated-nonadmin-user>@luis-pacs
```

**Expected: both succeed.** That is rule 2 (`tag:pacs:22,3389`) working. This is the direction that
is *supposed* to work, so a success here plus the failures in 4a together demonstrate the ACL is
enforcing direction rather than simply breaking all connectivity.

### 4c. Confirm the node is actually tagged

Admin console → **Machines** → `luis-pacs`. It should show **`tag:pacs`** and the owner column
should show the tag, **not** `rfinlay813@`. If it shows Rick as owner, the key's tag did not apply —
the node is user-owned, `autogroup:self` now covers it, and **rule 1 gives it full access to the
mini.** Remove the node and redo step 2.

This is the single highest-consequence failure mode in the whole procedure. Check it explicitly.

### 4d. Confirm least privilege

From the mini, an SMB probe that rule 2 does not permit:

```
nc -z -w 5 luis-pacs 445
```

**Expected: failure.** Only 22 and 3389 are open to you. If 445 answers, the ACL is wider than
intended.

---

## Rollback

**Kill the node (fastest, do this first if anything looks wrong):**

Admin console → **Machines** → `luis-pacs` → **…** menu → **Remove**. Instant; the device drops off
the tailnet regardless of what is running on Luis's box.

**Revoke the key:**

Admin console → **Settings** → **Keys** → find `luis-pacs 2026-09-16 assessment` → **Revoke**.
Revoking does not disconnect an already-joined node, so do the Remove above as well.

**On Luis's machine:**

```
tailscale logout
```

Then uninstall Tailscale via Settings → Apps if the engagement is over. Leaving a dormant VPN client
on a clinical workstation is not a good look and is not something you want to have to explain.

**Revert the whole policy:** admin console → **Configuration logs** → revert to the pre-visit
version. Your scratch-file copy from step 1 is the manual fallback.

---

## Things worth flagging

- **Tailscale SSH does not work against Windows.** Verified at `kb/1193/tailscale-ssh`: Tailscale
  SSH servers run on Linux and open-source (CLI `tailscaled`) macOS only. The `ssh` block in the
  policy is deliberately empty. Shell access to Luis's box is **Microsoft OpenSSH Server on TCP 22**,
  which rule 2 permits — ordinary SSH over the tailnet, authenticated by Windows credentials.
- **Do not tag the Mac mini.** Tagging a device *removes its user-based ownership*
  (`docs/features/tags`), which would drop it out of `autogroup:self` and break rule 1 for it.
  `tag:rgf` is defined for future use and is currently carried by no device. That is intentional.
- **The ACL protects the tailnet, not the PACS.** Nothing here restricts what Luis's workstation
  does over its own LAN or to `exa.swxrayonline.com`. ACLs govern tailnet traffic only and do not
  affect local network traffic. Scope discipline on PHI is a procedural control, not a network one.
- **`--shields-up` blocks your inbound access too.** Covered above; just do not be surprised by it.

---

## Docs verified against (fetched 2026-09-15)

- https://tailscale.com/kb/1337/policy-syntax — top-level keys, `tests`/`sshTests` syntax,
  `nodeAttrs`, `autoApprovers`, autogroup list, and the confirmation that failed tests reject the save
- https://tailscale.com/kb/1018/acls — `acls` action/src/dst format, default-allow for new tailnets
- https://tailscale.com/docs/reference/examples/acls — microsegmentation and `tests` patterns
- https://tailscale.com/docs/features/tags — tagging removes user ownership; tagging disables key expiry
- https://tailscale.com/kb/1193/tailscale-ssh — Tailscale SSH server platform support (no Windows)
- https://tailscale.com/kb/1085/auth-keys — tagged auth keys, reusable/ephemeral/pre-approved, 1–90 day expiry
- https://tailscale.com/kb/1080/cli — `tailscale up` flags, `logout`, `ping`, `status`
- https://tailscale.com/docs/features/tailnet-policy-file/manage-tailnet-policies — Preview rules tab,
  Configuration logs revert
