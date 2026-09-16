# PACS Remote Access — Technical Quick Reference

**Wednesday 2026-09-16** · Tailscale + OpenSSH setup on the reading workstation.

Commands are listed in the order they are run. Each one is on its own line and is copy-paste ready.

**Key facts**

| | |
|---|---|
| Mac mini tailnet IP | `100.67.156.31` |
| Hostname to assign | `luis-pacs` |
| Admin console | login.tailscale.com/admin/machines |

**Everything below runs in PowerShell as Administrator on the workstation**, except Step 3 (a browser) and Step 5c (run from the Mac mini).

---

## STEP 0 — Confirm admin rights and that the machine is standalone

Check for local administrator rights:

```
whoami /groups | findstr /i "Administrators"
```

`BUILTIN\Administrators` in the output means admin rights are present. Admin is required for every step below — the Tailscale installer writes a system service and a virtual network adapter, `tailscale up` needs an elevated shell, and OpenSSH Server installs at system level.

Check whether the machine is domain-joined:

```
systeminfo | findstr /i "Domain"
```

`Domain: WORKGROUP` means standalone. **If a real domain name appears, stop here** — remote-access software should not be installed on an organization-managed endpoint without approval from whoever administers it.

---

## STEP 1 — Install Tailscale

Download from **tailscale.com/download/windows** and run the installer.

**Do not sign in through the GUI.** The auth key in Step 2 replaces sign-in entirely.

---

## STEP 2 — Join the tailnet

Replace `PASTE_KEY_HERE` with the auth key.

```
tailscale up --authkey=PASTE_KEY_HERE --hostname=luis-pacs --shields-up --accept-routes=false
```

`--shields-up` blocks all inbound traffic to this machine, including SSH and RDP. **That is intentional** — the outbound block gets verified first, then the shield drops in Step 4b. It will look like a failure if you forget this. It is not.

---

## STEP 3 — Verify the node joined tagged (browser check)

Go to **login.tailscale.com/admin/machines**, find `luis-pacs`, and read the owner column.

| It reads | Meaning |
|---|---|
| `tag:pacs` | Correct. Proceed. |
| an email address | **Stop.** The tag did not apply. |

This is the check that matters most. A tagged node is fenced off by the access policy; a user-owned node is not.

**If it is wrong:** remove the node from the admin console, confirm the auth key had `tag:pacs` selected, generate a fresh key if needed, and rerun Step 2.

---

## STEP 4 — Verify the block, then drop the shield

### 4a. Confirm the workstation cannot reach the Mac mini

```
Test-NetConnection 100.67.156.31 -Port 22
```

**`TcpTestSucceeded : False` is the PASS.** Optionally repeat for the other ports:

```
Test-NetConnection 100.67.156.31 -Port 3389
```

```
Test-NetConnection 100.67.156.31 -Port 445
```

**Do not use `tailscale ping` for this test.** It sends a TSMP probe that Tailscale answers regardless of the access policy, so it succeeds even when real connections are correctly blocked.

### 4b. Drop the shield

Only after 4a returns `False`:

```
tailscale up --reset --authkey=PASTE_KEY_HERE --hostname=luis-pacs --accept-routes=false
```

---

## STEP 5 — Enable SSH

### 5a. Install and start OpenSSH Server

```
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

```
Start-Service sshd
```

```
Set-Service -Name sshd -StartupType Automatic
```

### 5b. Create a dedicated non-admin service account

Create a **standard (non-administrator)** local user named `rgfsvc`. A separate account keeps personal credentials out of it and lets access be revoked without touching the main profile.

```
New-LocalUser -Name rgfsvc -Description "RGF read-only service account"
```

Confirm it is NOT in the Administrators group:

```
Get-LocalGroupMember -Group "Administrators"
```

### 5c. Acceptance test — nothing to type at the workstation

**This step runs from the Mac mini, not from here.** Text Gio "run the acceptance test" and he runs it remotely while you are still in the room. If it passes, the setup is confirmed before you leave.

For reference, the test is:

```
ssh rgfsvc@luis-pacs "hostname && whoami"
```

**Real output means the setup succeeded** — the tailnet route, the SSH service, and the `rgfsvc` account all work end to end.

If it fails, the three things to check at the workstation are:

```
Get-Service sshd
```

```
tailscale status
```

```
Get-LocalUser rgfsvc
```

---

## STEP 6 — Clean up

The auth key is sitting in PowerShell history. Clear it:

```
Remove-Item (Get-PSReadlineOption).HistorySavePath
```

---

## STEP 7 — On-site browser observation (90 seconds)

This cannot be done later over SSH — SSH is a command line and cannot see a browser session.

1. In Chrome, open **DevTools** (`F12`) → **Network** tab
2. Load a study in Exa
3. Read the **Type** column on the requests carrying the image

| Type column shows | Meaning |
|---|---|
| `jpeg`, `png`, `webp`, or a websocket carrying frames | Server-side rendered pixels — no DICOM at the workstation |
| `application/dicom`, `.dcm`, or a WADO-RS URL | Real DICOM reaches the workstation |

**Screenshot the Type column only. Do NOT save a HAR file** — HAR export captures response bodies and would write patient data to disk.

---

## Optional — encryption status

```
manage-bde -status C:
```

Full-disk encryption present means a lost workstation is secured, not a reportable exposure.

---

## Reference — useful checks

Tailscale connection status:

```
tailscale status
```

This machine's tailnet IP:

```
tailscale ip -4
```

Is the SSH service running:

```
Get-Service sshd
```

---

## Teardown — when the assessment is complete

Remove `luis-pacs` from the tailnet at **login.tailscale.com/admin/machines**. The tagged key disables node key expiry, so the node persists until it is removed manually.

On the workstation, if fully backing out:

```
tailscale logout
```

```
Stop-Service sshd
```

```
Set-Service -Name sshd -StartupType Disabled
```

---

## One-line summary

Install Tailscale → join with the tagged key → confirm `tag:pacs` in the console → verify the block → drop the shield → install SSH → create `rgfsvc` → prove it from the Mac mini → clear the key from history.
