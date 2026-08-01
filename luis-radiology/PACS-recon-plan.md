# PACS Environment Recon Plan — Dr. Ramos (Exa)
**Purpose:** learn the system to architect the RadAssist suite. **Strictly technical + de-identified. No real patient studies. No PHI retained.** Executed over Tailscale (SSH to `luis-pacs`) once the node is up.

## Hard guardrails (non-negotiable, enforced by me)
- **No access to real patient records.** If a real study/report is on screen, I stop and note it — I do not read, capture, or store it. Real PHI waits for the signed BAA.
- **De-identified / test patient only** for any workflow walkthrough. Ideally Luis (or Rick) drives to a test/sample study, or we scrub identifiers first.
- **Retain nothing patient-related.** Any incidental capture is deleted immediately (same discipline used on all his layout screenshots to date).
- **Read-only.** No writes, config changes, or installs on his environment beyond what Rick sets up.
- **Node isolation.** `luis-pacs` is ACL-walled from our finance/personal nodes (I set this on our tailnet side).

## Access verification (first 5 min)
1. Confirm `luis-pacs` is reachable on our tailnet from the mini.
2. SSH in as the dedicated (non-admin) user Rick created.
3. Confirm Tailscale ACL isolation is active (node can't reach our other nodes).

## A. Machine & environment (no PHI)
- OS + version, hardware, monitor config (confirms the 3-screen layout).
- Installed software inventory: browser(s), any Exa/Konica local components, DICOM tools, dictation/voice software (e.g., PowerScribe/Fluency), the MESA calculator access, any local agents/services.
- How Exa is launched (URL, shortcut, any thick-client component vs. pure web).
- Admin rights / what the dedicated user can and can't see.

## B. Network & integration surface (the core question)
- What Exa talks to: hostnames/endpoints (`exa.swrxsyonline.com` + any API subdomains), TLS, auth flow (SSO? token?).
- Local listening ports / services — is there a **local DICOM listener** (SCP), a **DICOMweb** endpoint, or a local agent/relay Exa uses?
- Any local API, config files, or logs that reveal how the web app fetches studies/worklist and submits reports (all metadata/technical — no patient content).
- Outbound calls the app makes (network capture at the technical layer, no payload PHI).
- Cross-check against **Sherlock's Exa research** (does Exa expose REST/HL7/FHIR/DICOMweb; is there a partner/API path) — confirm which of those are actually reachable in *this* deployment.

## C. Workflow & report structure (de-identified/test only)
- Walk the read → report → sign-off flow on a **test/de-identified** study: how a template loads, how findings/impression are entered, how the report is saved/signed.
- Capture the **report template structure** (sections, boilerplate, macros) — this is template IP, not PHI.
- The **calcium-score / MESA** loop end-to-end (de-identified): where the Agatston scores come from, how the percentile is entered, where it lands in the report.
- Prior-study retrieval mechanism (how priors are found/opened) — the *mechanism*, not any patient's actual priors.
- Where the dictation/voice system fits.

## D. Companion-tool feasibility check
- Inspect the Exa web app's DOM/structure enough to judge a **browser-extension/overlay** approach (can we read the right fields, insert report text, detect exam type) — using a test/blank study.
- Feasibility of DICOMweb vs. extension vs. local-agent integration, given what's actually exposed here.
- Confirm the local footprint available for a **privacy-preserving local agent** (the AI-agent window Luis sketched) — compute, network egress control, where PHI would/wouldn't flow.

## Output
A **technical environment map + integration-options assessment** (no PHI) that feeds:
- **P3** — the PACS-integrated suite architecture (which integration path is real here)
- **P5** — the privacy-preserving agent design (local footprint, PHI boundaries)
Plus a short list of anything that genuinely requires real-PHI access — which we gate behind the signed BAA and do last, if at all.

## What Rick still needs to set up (relayed by Rick, not me → Luis)
- Tailscale on the workstation, joined to our tailnet, named `luis-pacs`.
- Windows **OpenSSH Server** enabled + a **dedicated non-admin login** for me.
- A **de-identified/test study** available for the workflow walkthrough (or Luis drives it).
