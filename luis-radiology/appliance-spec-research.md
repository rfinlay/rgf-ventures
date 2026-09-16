# On-Prem HIPAA Appliance — Windows mini-PC vs. Apple Mac mini (RadAssist)

**Author:** Sherlock (research persona) → Gio → Rick + Steven
**Date:** 2026-08-04
**Status:** Research/report only. Read-only. No environment touched. No PHI involved.
**Purpose:** Decision-grade, sourced comparison of the physical appliance that will run RadAssist on-prem in Dr. Luis Ramos's office, integrate with Konica Minolta **Exa** PACS, and (later phase) run a **local** AI agent. Rick reviews this with a mentor (Steven), so every material claim is sourced + confidence-rated.

> **Confidence legend:** **High** = confirmed from primary/authoritative source this session. **Medium** = strong secondary source or stable domain fact, some site/price variance. **Low** = ballpark/estimate, verify before quoting.
>
> **Method + honesty note.** DuckDuckGo served bot/CAPTCHA challenges for most keyword searches this session, so hardware/price facts were pulled by **direct fetch** of primary pages (Apple, NVIDIA, EveryMac) plus one curated 2026 mini-PC roundup, and **OpenClaw platform facts from the authoritative local docs** (`/opt/homebrew/lib/node_modules/openclaw/docs`). Exa facts reuse our prior verified recon (`sherlock-exa-integration-research.md`, 2026-07-31). **Prices move and configurations change — treat every dollar figure as approximate + dated, and re-verify at purchase.** The single biggest driver of this decision is a question only Rick/Steven can answer (see §7): *does the agent have to run a capable LLM on PHI locally, or is the PHI-side processing deterministic?*

---

## 0. TL;DR / Lean

- **If PHI processing stays deterministic** (parse DICOM/HL7 + run RadAssist's own logic; any LLM reasoning runs on **de-identified** data in the cloud) → the appliance is light-duty. **Lean: Apple Mac mini M4 (16–24 GB)** as a clean, silent, low-power, FileVault-encrypted turnkey box — *or* a cheap Windows mini-PC if the practice's IT insists on a homogeneous Windows shop. Compute is not the deciding factor here; operational fit is.
- **If the agent must run a capable LLM on PHI locally** (the hard rule: PHI never leaves for a hosted LLM) → **memory capacity is the wall**, and the honest ranking flips by budget:
  - Biggest models for the least money → **Windows/x86 "Strix Halo" box (AMD Ryzen AI Max+ 395, 128 GB unified)**.
  - Fastest CUDA tooling + NVIDIA's own secured-OpenClaw stack (**NemoClaw**) for always-on agents → **NVIDIA DGX Spark (128 GB, GB10)** — but it's an Arm AI appliance, not a general office PC, and premium-priced.
  - Silent/low-power elegance at up to 64 GB, good enough for ~32B-class models → **Mac mini M4 Pro (48–64 GB)**.
- **PACS integration does NOT favor either OS.** Exa integrates over DICOM / HL7 / (maybe) DICOMweb — OS-agnostic TCP/IP protocols. (High)
- **OpenClaw runs well headless on macOS (LaunchAgent), native Windows (Scheduled Task), and Linux (systemd).** Windows-via-WSL2 is the *most Linux-compatible* runtime but has the *most moving parts* for unattended operation. (High)

---

## 1. Hardware options — current specs & prices (approximate, dated 2026-08-04)

### 1a. Apple Mac mini (M4 / M4 Pro, 2024)

| Config | Chip | CPU/GPU | Unified RAM | Mem. bandwidth | Storage | ~US price | Confidence |
|---|---|---|---|---|---|---|---|
| Base M4 | M4 | 10C CPU / 10C GPU | 16 GB (→24 GB) | **120 GB/s** | 256 GB (→512/1/2 TB) | **~$599** | Price: Medium; specs: High |
| M4 mid | M4 | 10C / 10C | 24 GB | 120 GB/s | 512 GB | ~$799–999 | Medium |
| M4 Pro base | M4 Pro | 12C CPU / 16C GPU | 24 GB (→48) | **273 GB/s** | 512 GB (→2 TB) | **~$1,399** | Price: Medium; specs: High |
| M4 Pro top | M4 Pro | 14C CPU / 20C GPU | 48 GB (→**64 GB**) | 273 GB/s | 512 GB (→8 TB) | ~$1,999–2,199 (64 GB) | Low–Medium |

- **Specs verified High** from Apple's tech-spec page: M4 = 120 GB/s bandwidth, 16-core Neural Engine, 16 GB default configurable to 24 GB; **M4 Pro = 273 GB/s bandwidth**, 12-core CPU / 16-core GPU configurable to 14C/20C, 24 GB configurable to 48 GB, top config to **64 GB unified**. Chassis 5×5×2 in, **max continuous power 155 W** (idles far lower), 100–240 V, Gigabit Ethernet (configurable 10 GbE), Thunderbolt 5 (M4 Pro). Source: apple.com/mac-mini/specs. RAM is **soldered/on-package — not upgradeable after purchase**; buy the tier you need. (EveryMac confirms 24 GB default on M4 Pro 14C/512 GB, RAM not upgradeable.)
- **64 GB is the Mac mini ceiling.** For 128 GB unified on Apple Silicon you must step up to a **Mac Studio** (larger, ~$2k+ more). (Medium — layer3labs roundup; consistent with Apple's lineup.)
- **Prices are Medium confidence** — Apple's storefront is JS-rendered and did not return live line-item pricing this session; the figures above combine Apple's known launch pricing (base M4 mini = $599; M4 Pro = $1,399) with standard ~$200/step memory & storage upgrades. **Verify exact BTO price at apple.com before quoting Steven.** (Wikipedia's infobox lists a $799 "introductory price" for the current release, which conflicts with the widely reported $599 base — another reason to confirm live.)

### 1b. Windows / x86 mini-PC & SFF options

Three sub-classes matter for an always-on appliance:

**(i) No-GPU thin client / SFF (deterministic workloads, CPU-only inference only):**
- Intel N100 / Core i5 / Ryzen mini-PCs (Beelink, Minisforum, GMKtec, Intel NUC-class), 16–32 GB DDR5, 512 GB–1 TB NVMe. **~$300–800.** (Low–Medium; broad market.) Fine for DICOM/HL7 parsing + RadAssist logic; **not** for real LLM inference (see §2).

**(ii) x86 "unified memory" boxes (the real Windows analog to the Mac mini for local LLM):**
| Model | APU | Unified/shared RAM | Ecosystem | ~US price | Confidence |
|---|---|---|---|---|---|
| **GMKtec EVO-X2** | AMD **Ryzen AI Max+ 395** (16 Zen5, Radeon 8060S iGPU, 40 CU) | **128 GB** LPDDR5X-8000, up to 96 GB assignable to GPU | ROCm / Vulkan | **~$1,800–2,000** | specs: High; price: Low–Medium |
| **Framework Desktop** | Ryzen AI Max+ 395 | up to 128 GB (soldered) | ROCm / Vulkan | ~$2,000+ configured | Medium |
| **Beelink GTR9 Pro** | Ryzen AI Max+ 395 | 128 GB LPDDR5X, **dual 10 GbE**, vapor chamber | ROCm / Vulkan | ~$1,900–2,200 | Medium |
- Source: layer3labs "Best Mini PCs for Local AI & LLMs (2026)." These run **70B-class quantized models** in a mini-PC form factor and **double as a normal x86 Windows desktop**. Caveat from the source: *"AMD ROCm tooling is less mature than CUDA; the biggest models load but run slowly."* (Medium)

**(iii) Windows + discrete NVIDIA GPU (fastest tokens/sec, VRAM-capped):**
- **Minisforum MS-01** — rare mini-PC with a **PCIe slot for a half-height GPU** (e.g., RTX 4000 SFF Ada 20 GB, RTX 2000 Ada 16 GB); dual 10 GbE, multi-NVMe. Box ~$700–900 + GPU. Real **CUDA VRAM**, but GPU choice constrained by half-height size, louder/warmer under load. (Medium)
- **Small tower / SFF + full GPU** — RTX 4060 Ti 16 GB build ~$1,200–1,600; RTX 4090 24 GB build ~$2,500–3,500; RTX 6000 Ada 48 GB (workstation) build $6k+. Bigger footprint than a "mini," but max tok/s. (Low–Medium, build-dependent.)

**(iv) Purpose-built local-agent appliance:**
- **NVIDIA DGX Spark** — **GB10 Grace Blackwell** superchip, **128 GB coherent unified memory**, full CUDA + NVIDIA AI stack, ConnectX networking. Runs models **up to ~200 B params** locally (405 B across two linked units). NVIDIA markets it explicitly as *"built to run always-on agent workloads right from the desktop."* **~$3,000–4,000** (NVIDIA/ASUS/partner variants). It is an **Arm** AI appliance, **not** a general Windows office PC. Source: nvidia.com DGX Spark page. (specs: High; price: Low–Medium)
  - **Notable for us:** the DGX Spark page announces **NemoClaw** — *"an open-source reference stack that adds security and privacy guardrails to **OpenClaw** using OpenShell,"* to *"run secure, always-on AI assistants on NVIDIA RTX PCs, DGX Station, and DGX Spark."* i.e., **NVIDIA has purpose-built a secured local-OpenClaw stack** for exactly the "always-on agent on-prem" pattern RadAssist's later phase envisions. (High — from NVIDIA's own page.)

---

## 2. Local LLM inference per platform — what actually fits & runs

**The governing rule:** on a small machine, **the model must *fit in memory* before speed matters** (layer3labs, High). Two levers: (1) capacity decides *which* model runs at all; (2) **memory bandwidth** decides *how fast* it runs (both Apple unified and x86 LPDDR5X unified are bandwidth-bound; discrete NVIDIA GPUs have ~3–8× the bandwidth).

**VRAM/RAM sizing — 4-bit (Q4) rule of thumb** (stable domain fact; ≈0.5–0.6 GB per 1B params for weights, **+15–30% for KV cache/context/runtime**). Confidence Medium (well-established; exact depends on quant + context length):

| Model size (Q4) | Weights ≈ | Practical footprint w/ context | Runs comfortably on |
|---|---|---|---|
| 7–8 B | ~4.5 GB | ~6–8 GB | 16 GB (any tier) |
| 13–14 B | ~8 GB | ~10–12 GB | 24 GB comfortably; 16 GB tight |
| 32–34 B | ~19 GB | ~22–28 GB | 32–48 GB unified, or 24 GB GPU tight (Q3/short ctx) |
| 70 B | ~40 GB | ~45–55 GB | 64 GB unified tight; **128 GB comfortably**; or 2× 24 GB GPU |
| 120–200 B (MoE) | varies | 90–128 GB+ | 128 GB unified (Strix Halo / DGX Spark) |

**Platform-specific notes:**
- **Apple Silicon (Metal / MLX):** unified memory is shared CPU/GPU. macOS caps GPU-wired memory to roughly **⅔–¾ of RAM by default** (raisable via `iogpu.wired_limit_mb`), so a 64 GB Mac mini yields ~**48 GB usable** for a model. → Mac mini M4 Pro/64 GB comfortably runs **32B-class**, and **70B Q4 only tightly**. M4 Pro bandwidth **273 GB/s** ⇒ ballpark **7–8 B Q4 ~20–40 tok/s; 32 B Q4 ~8–12 tok/s** (Low confidence — ballpark). Base M4 at **120 GB/s** is roughly half that and 16–24 GB caps it at **7–14 B**. MLX is Apple's optimized inference framework; ecosystem is good but smaller than CUDA. (Medium/Low)
- **x86 unified (Ryzen AI Max+ 395, 128 GB, ~256 GB/s LPDDR5X):** capacity to run **70B+ and large MoE** for the lowest price, but **ROCm/Vulkan tooling less mature than CUDA** and *"biggest models run slowly"* (layer3labs). Throughput ballpark similar to M4 Pro class, sometimes lower. (Medium)
- **Windows + discrete NVIDIA GPU (CUDA):** **fastest tok/s** and the **widest tooling support** (*"CUDA — almost every AI tool supports it out of the box"*), but **VRAM-capped** to the card: 16 GB → 7–14 B; 24 GB (4090) → up to 32 B Q4; 48 GB (RTX 6000 Ada) → 70 B Q4. 7B >100 tok/s, 32B ~30–40 tok/s on a 4090-class card. (Medium/Low)
- **NVIDIA DGX Spark (GB10, 128 GB, CUDA):** up to **~200 B** params; unified LPDDR5X so bandwidth-bound like the others (throughput modest for the largest models) but **full CUDA + NVIDIA NIM/AI stack** and the **NemoClaw** secured-OpenClaw path. Best "development-grade" local-agent box. (High capacity; Low on tok/s specifics.)
- **CPU-only (no-GPU mini-PC):** single-digit tok/s for 7B, impractical ≥13B. **Only viable if there is no LLM-on-PHI requirement.** (Medium)

**Bottom line on inference:** for local-LLM-on-PHI, **capacity ranking** = 128 GB x86/DGX (70–200 B) > Mac mini 64 GB (≤~70 B tight, 32B comfortable) > 24 GB NVIDIA GPU (≤32 B) > 16–24 GB anything (≤14 B) > CPU-only (≤7 B, slow). **Tooling maturity** = CUDA (NVIDIA) > MLX/Metal (Apple) > ROCm (AMD).

---

## 3. OpenClaw on Windows vs. macOS vs. Linux — headless/always-on fit

**Authoritative (High) — from local OpenClaw docs (`platforms/index.md`, `platforms/windows.md`):**
- **Runtime requirement:** OpenClaw core is TypeScript; **Node is the required runtime** (canonical state store uses `node:sqlite`). Task spec: Node **22.22.3+ / 24.15+ / 25.9+, Node 24 recommended.** (Doc confirms Node-required; exact minor from task brief.)
- **Service/always-on model per OS:**
  | OS | Always-on mechanism | Notes |
  |---|---|---|
  | **macOS** | **LaunchAgent** (`ai.openclaw.gateway`) + native menu-bar companion app | Cleanest turnkey; note a LaunchAgent runs in a user session (appliance should auto-login or use a daemon variant for true headless). |
  | **Native Windows** | **Scheduled Task** (`OpenClaw Gateway`), with Startup-folder login-item fallback | Supported & headless-capable. Launches via a generated `gateway.vbs` WScript wrapper so **no visible console window**. `openclaw gateway install`. |
  | **Windows + WSL2** | **systemd user service** *inside* WSL | *"Most Linux-compatible Gateway runtime,"* but **most moving parts** unattended (see gotchas). |
  | **Linux** | **systemd user service** (`openclaw-gateway.service`) | Most robust true-headless path. |
- **Windows Hub** is the native WinUI companion app (Win10 20H2+/Win11): tray status, launch-at-login, first-run setup for an **app-owned WSL Gateway**, Command Center diagnostics, Windows **node mode** (canvas/screen/camera/notify/`system.run`), and a **local MCP server** mode. Installs without admin. (High)

**WSL2 headless gotchas (High — documented in the OpenClaw Windows doc):**
- WSL ≥ 2.6.1.0 has a **regression (microsoft/WSL #13416)** that **idle-terminates the distro ~15–20 s after the last client exits**, even with linger enabled. Workaround: a scheduled `"WSL Boot"` task running `wsl.exe -d <distro> --exec dbus-launch true` at startup + `loginctl enable-linger`.
- Per-user WSL distros are **not visible to the SYSTEM account**, so a boot task must run as the **user** (`/ru "$env:USERNAME"`), not SYSTEM — otherwise "the task runs but the distro never starts."
- WSL has its **own virtual NIC**; exposing a Gateway/service to the office LAN needs `netsh interface portproxy` + a firewall rule, and **the WSL IP can change on restart** (refresh the rule). Extra fragility for an appliance that must reliably talk to the PACS on the LAN.

**Reliability read for an unattended appliance:** **Linux (systemd) ≈ macOS (LaunchAgent) ≈ native-Windows (Scheduled Task)** are all first-class and headless-capable; **Windows-via-WSL2 adds the most failure surface** (idle-termination workaround, SYSTEM-visibility caveat, changing WSL IP + port-proxy for LAN reach). Since the office is **Windows**, **native Windows** is a fully supported, lower-friction path than WSL2 — but if the box only exists to run OpenClaw + RadAssist, **macOS or Linux give the simplest always-on story**. (Medium-High synthesis; individual facts High.)

---

## 4. Konica Minolta **Exa** PACS integration — does it favor an OS?

**Short answer: No. Exa integrates over OS-agnostic network protocols; nothing favors Windows or macOS.** (High)

Reusing our verified 2026-07-31 recon (`sherlock-exa-integration-research.md`):
- **Exa** = Konica Minolta Healthcare "Exa Platform" (PACS+RIS+Billing), **browser-based, Zero-Footprint, server-side-rendered** — no client install, "any OS, any browser." (High)
- **DICOM** is inherent (it's a full PACS): **C-STORE (receive), C-FIND/C-MOVE (query/retrieve), Modality Worklist (MWL)** — standard DICOM over TCP/IP (typically port 104/11112). (High as a category; the specific AE-title/port exposed to a *new* third-party node is site-config → **recon**.)
- **HL7 v2** interfacing is a **first-class, KM-provisioned** integration path (ORM orders / ORU results / ADT), per KM's own Implementation Overview. HL7 over MLLP (TCP). (High that it exists; per-site provisioning → recon.)
- **DICOMweb (QIDO-RS / WADO-RS / STOW-RS)** — **Unknown / not publicly documented**; the ZFP viewer talks a private backend API, but whether a *documented, third-party-usable* DICOMweb endpoint is exposed on *his* instance is a **high-value recon probe**. (Unknown)
- **No public REST API, FHIR, webhooks, or partner SDK found** — assume none until proven on his instance. (Medium)

**Why this is OS-neutral:** DICOM (C-STORE/C-FIND/MWL), HL7-over-MLLP, and DICOMweb (HTTP/S) are **network protocols**; the appliance is a **DICOM AE / HL7 endpoint / HTTP client** regardless of Windows/macOS/Linux. The standard on-prem ingest/de-id hub (**Orthanc**, DICOMweb-capable, built-in anonymization) **runs on all three.** So PACS integration is **not** a tiebreaker. (High)

**Honest "depends on recon" flags (unchanged from PACS-recon-plan):** exact DICOM **Conformance Statement** for his Exa version, whether DICOMweb is reachable, whether KM will enable an outbound **ORU** feed, who controls the interface (group IT vs. reseller vs. KM), and network/VLAN reachability between appliance and PACS. These gate the *integration*, not the *OS choice*.

---

## 5. HIPAA on-prem appliance considerations

**Disk encryption at rest (both satisfy HIPAA's addressable encryption spec):**
| | macOS | Windows |
|---|---|---|
| Tech | **FileVault** — XTS-AES-128 (256-bit key), keyed to the **Secure Enclave**; on by default-eligible on all Macs | **BitLocker** — AES-128/256-XTS, backed by **TPM 2.0** |
| Edition gate | Available on **all** Macs | **Requires Windows 11 Pro/Enterprise** (not Home) — the appliance must run **Win 11 Pro** |
| Confidence | High | High |

**Platform-specific HIPAA landmines to disable (both have cloud-AI features that could exfiltrate PHI — turning them off is mandatory given the hard rule):**
- **Windows:** **Recall** (periodic screenshots of the screen, incl. PHI on the reading workstation) and **Copilot** — **must be disabled** on a PHI appliance. Recall in particular is a documented privacy hazard. (Medium — widely reported; verify current Windows build behavior.)
- **macOS:** **Apple Intelligence** (can offload to **Private Cloud Compute**) and Siri/analytics — **must be disabled** so no PHI-adjacent content leaves the box. (Medium)

**Broader posture (platform-agnostic, per HHS/HIPAA Security Rule):** physical security of the box, unique login + auto-lock, audit logging, patch cadence, least-privilege network placement (VLAN/firewall between appliance and PACS), and — the **hard architectural rule** — **PHI-bearing inference runs locally; only de-identified content may reach any cloud LLM, and only under a BAA.** DICOM de-identification standard = **PS3.15 Annex E**; tooling = RSNA **CTP** / Orthanc anonymizer; watch **burned-in pixel PHI** (ultrasound/secondary captures) not just header tags. (High as practices — from prior recon.)

**Which OS is a "cleaner" HIPAA fit?** Roughly a wash:
- **macOS** advantages: smaller malware target surface, FileVault on every unit, fewer bundled cloud-AI surfaces to police, silent/sealed appliance feel.
- **Windows** advantages: mature **enterprise management** (Group Policy, BitLocker + AD/Intune, Microsoft Defender, centralized patching) — better if the practice already has Windows IT governance; but you must run **Pro** and **explicitly disable Recall/Copilot**.
- Neither is inherently "more HIPAA-compliant"; **compliance is configuration + process, not brand.** (Medium synthesis.)

---

## 6. Comparison matrix — Windows appliance vs. Mac mini appliance

| Dimension | **Windows mini-PC appliance** | **Apple Mac mini appliance** | Edge |
|---|---|---|---|
| **Hardware $ (deterministic, no-GPU)** | ~$300–800 (N100/i5 SFF) | ~$599–799 (M4 16–24 GB) | Windows (cheaper floor) |
| **Hardware $ (local-LLM capable)** | Strix Halo 128 GB ~$1,800–2,000; DGX Spark ~$3–4k; 4090 build ~$2.5–3.5k | M4 Pro 48–64 GB ~$1,600–2,200 | Depends on model size needed |
| **Max memory for local models** | **128 GB** (Strix Halo / DGX Spark) | **64 GB** (Mac mini ceiling; 128 GB needs Mac Studio) | **Windows/x86** |
| **Local-LLM tooling maturity** | CUDA (best, NVIDIA) / ROCm (weakest, AMD) | MLX+Metal (good, mid) | Windows *if NVIDIA*; else ~tie |
| **Tok/s ceiling** | Highest w/ discrete NVIDIA GPU (~1 TB/s VRAM) | Bandwidth-bound (273 GB/s M4 Pro) | Windows+NVIDIA |
| **Power / noise / size** | Varies; GPU boxes hot/loud/bigger | ~155 W max, near-silent, 5×5×2 in | **Mac mini** |
| **OpenClaw always-on fit** | Native = Scheduled Task (good); WSL2 = most moving parts | LaunchAgent + native app (clean) | ~tie (Mac slightly cleaner; native-Win fine) |
| **Matches office (Windows) IT** | Homogeneous — easier for existing IT | Adds a macOS box to support | **Windows** |
| **PACS (Exa) integration** | DICOM/HL7/DICOMweb — OS-neutral | DICOM/HL7/DICOMweb — OS-neutral | **Tie** |
| **Disk encryption** | BitLocker (needs Win 11 **Pro**) | FileVault (all Macs) | Slight Mac |
| **Cloud-AI PHI landmines to disable** | Recall + Copilot (**must** disable) | Apple Intelligence/PCC (**must** disable) | Slight Mac (fewer) |
| **Enterprise mgmt (GPO/Intune/Defender)** | Mature | Lighter (MDM/Jamf) | **Windows** |
| **NVIDIA "secured OpenClaw" path (NemoClaw)** | Yes (RTX/DGX) | No | **Windows/NVIDIA** |

---

## 7. Recommendation framework — tie the choice to the deciding factor

**Everything hinges on one question Rick/Steven must answer:**
**→ Does RadAssist's on-prem agent need to run a *capable LLM on PHI locally*, or is the PHI-side processing *deterministic*?**

### Path A — PHI processing is **deterministic** (parse DICOM/HL7 + RadAssist's own logic; LLM reasoning, if any, runs on **de-identified** data in the cloud under a BAA)
- Compute demand is **light**; capacity/tok-s is irrelevant. Decide on **operational fit**.
- **Choose Mac mini (M4, 16–24 GB, ~$599–799) if** you want the cleanest turnkey appliance: silent, low-power, FileVault, mature macOS app + LaunchAgent, minimal surface to harden.
- **Choose a Windows mini-PC (~$300–800) if** the practice's IT wants a homogeneous Windows shop it already knows how to manage/patch (Win 11 **Pro** for BitLocker; disable Recall/Copilot).
- **Sherlock's lean:** **Mac mini M4** for a dedicated appliance you control end-to-end; **Windows mini-PC** if the existing IT relationship/support model dominates. Either is fine — this path is a wash on capability.

### Path B — agent must run a **capable LLM on PHI locally**
- **Memory capacity is the wall.** Sub-decide by *how big a model* and *budget*:
  - **Need 70B+ / large MoE, lowest cost →** **Windows/x86 AMD Ryzen AI Max+ 395, 128 GB** (GMKtec EVO-X2 / Beelink GTR9 Pro / Framework Desktop, ~$1.8–2.2k). Accept **ROCm** immaturity; big models "load but run slowly."
  - **Need CUDA tooling + NVIDIA's secured always-on agent stack →** **NVIDIA DGX Spark, 128 GB** (~$3–4k, Arm appliance) — up to ~200B, **NemoClaw** = purpose-built secured OpenClaw for on-prem agents. Best "serious local-agent" box; not a general office PC.
  - **Need max tok/s on ≤32B and already Windows →** small tower + **NVIDIA RTX 4090 24 GB** (~$2.5–3.5k) — fastest responses, VRAM-capped at ~32B Q4.
  - **32B-class is enough + want silent/low-power elegance →** **Mac mini M4 Pro, 48–64 GB** (~$1.6–2.2k). Runs 32B comfortably, 70B only tightly; caps at 64 GB.
- **Sherlock's lean:** if the local model is genuinely large (≥32–70B) and this is the product's differentiator, **Windows/x86 128 GB (Strix Halo) for value** or **DGX Spark for the CUDA + NemoClaw path** beat the Mac mini, whose **64 GB ceiling** and bandwidth cap it below the 128 GB x86 boxes. If ~32B suffices, the **Mac mini M4 Pro 64 GB** is the elegant, silent middle.

### "Choose Windows if… / choose Mac mini if…" quick matrix
- **Choose Windows appliance if:** you need **>64 GB** for local models (only x86/DGX reach 128 GB) **OR** you want **CUDA + NemoClaw** (fastest tooling, NVIDIA's secured OpenClaw) **OR** the practice's IT mandates a homogeneous, centrally-managed Windows fleet.
- **Choose Mac mini appliance if:** PHI processing is **deterministic** (Path A) **OR** a **≤32B-class** local model is enough **AND** you value a **silent, low-power, small, FileVault-sealed, low-maintenance** turnkey box you fully control — accepting the **64 GB ceiling** and MLX (non-CUDA) ecosystem.

---

## 8. Open items that flip or refine this decision (recon / decisions owed)

1. **Local-LLM-on-PHI: yes or no, and what size?** (Path A vs. B — the whole decision.) — **Rick/Steven decision.**
2. **Exact Exa integration surface** on his instance (DICOM AE/port, DICOMweb reachable?, HL7 ORU enabled?, who controls the interface). — **Hands-on recon** (already in `PACS-recon-plan.md`). OS-neutral, but gates the build.
3. **Current pricing** — re-verify Apple BTO and mini-PC prices at purchase; figures here are approximate + dated 2026-08-04.
4. **Practice IT preference** — Windows homogeneity vs. accepting a Mac/Linux appliance; who patches/monitors it.
5. **Network placement** — VLAN/firewall path between appliance and the PACS/reading workstation; whether the operator permits an on-prem agent + (if used) browser extension.
6. **Tok/s ballparks** in §2 are **Low confidence** — if throughput is a hard requirement, benchmark the finalist box on the actual target model before committing.

---

## References
- **Apple** — Mac mini Technical Specifications (M4: 120 GB/s, 16→24 GB; M4 Pro: 273 GB/s, 24→48→64 GB; 155 W max; TB5; dimensions): https://www.apple.com/mac-mini/specs/ — *High (specs)*
- **Apple Support** — Mac mini (2024) Tech Specs (tested configs M4 16 GB / M4 Pro 24 GB): https://support.apple.com/en-us/121555 — *High*
- **EveryMac** — Mac mini "M4 Pro" 14C/20C 2024 (default 24 GB/512 GB, RAM not upgradeable, TB5, dimensions): https://everymac.com/systems/apple/mac_mini/specs/mac-mini-m4-pro-14-core-cpu-20-core-gpu-2024-specs.html — *High*
- **Wikipedia** — Mac Mini (release Nov 8 2024; pricing note — conflicts w/ known $599 base, verify): https://en.wikipedia.org/wiki/Mac_Mini — *Medium*
- **Layer3Labs** — Best Mini PCs for Local AI & LLMs (2026) (Ryzen AI Max+ 395 128 GB boxes, DGX Spark, Mac mini 64 GB cap, MS-01 PCIe GPU, ecosystem table): https://www.layer3labs.io/gear/best-mini-pcs-for-local-ai — *Medium*
- **NVIDIA** — DGX Spark (GB10, 128 GB unified, up to 200B params, always-on agents; **NemoClaw** secured OpenClaw reference stack): https://www.nvidia.com/en-us/products/workstations/dgx-spark/ — *High (specs), Medium (price)*
- **OpenClaw docs** — Platforms overview (Node required; macOS LaunchAgent / Linux+WSL2 systemd / native-Windows Scheduled Task): `/opt/homebrew/lib/node_modules/openclaw/docs/platforms/index.md` — *High*
- **OpenClaw docs** — Windows (Windows Hub, native CLI+Gateway via Scheduled Task + `gateway.vbs`, WSL2 setup + idle-termination regression #13416 + linger + port-proxy for LAN): `/opt/homebrew/lib/node_modules/openclaw/docs/platforms/windows.md` — *High*
- **Prior Sherlock recon** — Exa PACS/RIS integration (DICOM inherent; HL7 v2 KM-provisioned; DICOMweb unknown; no public API/SDK; OS-neutral protocols; on-prem de-id via Orthanc/CTP; PS3.15 Annex E): `projects/rgf-ventures/luis-radiology/sherlock-exa-integration-research.md` — *High (internal, sourced)*
- **VRAM/quant sizing** — Q4 ≈ 0.5–0.6 GB/1B params + 15–30% KV/context overhead (established llama.cpp/GGUF community rule of thumb; DuckDuckGo blocked live re-fetch this session) — *Medium*

**Search-tooling caveat:** DuckDuckGo returned bot/CAPTCHA challenges for keyword searches throughout this session; hardware/OpenClaw facts were obtained by direct primary-source fetch and authoritative local docs, and price/tok-s figures are conservatively rated and flagged for verification at purchase.
