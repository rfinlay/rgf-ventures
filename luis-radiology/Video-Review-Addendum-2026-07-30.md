# Video Review Addendum — RadAssist
**2026-07-30 | Source: all 3 workflow clips (phone-camera captures of Luis's live reading station)**

> **PHI note:** Clips are phone videos of live PACS screens and contain patient identifiers (names, IDs, ordering providers, DOB/weight). Reviewed locally only; no patient data reproduced here or transmitted. All extracted analysis frames were deleted after review. Original clips remain in Rick's OneDrive.

## The clips
- **Clip 1** (`192718`, ~3.5 min): CT head — multi-pane hanging protocol → single-pane slice navigation (soft-tissue + bone windows).
- **Clip 2** (`201136`, ~2.9 min): Chest/cardiac CT (contrast) — single-pane zoom/navigation.
- **Clip 3** (`193059`, ~23.4 min): the comprehensive walkthrough across modalities — sinus/facial CT, brain MRI (pituitary), and **coronary CTA with calcium scoring**. This is the substantive one.
- All are **handheld phone recordings of the monitors**, not clean screen captures — they validate the *workflow shape* and *screen content* but are too low-fidelity to read fine UI text, menu paths, or API hints.

## What Clip 3 confirms (high value)
1. **The calcium-score pilot wedge is real and visible.** On a coronary CTA study, the screen simultaneously shows: the coronary CT panes, a **"Coronary Calcium Score" percentile chart** (the MESA-style X-Y percentile plot), and a **scoring worksheet/report** with physician signature. This is the exact Tier-1 loop (REQ-001/002/003) — extract data → percentile → into the report — now visually grounded. Build the pilot against this.
2. **Prior-report comparison workflow (REQ-007) confirmed.** On the brain-MRI (pituitary) case, the right monitor showed **multiple prior reports stacked side-by-side** for interval comparison — exactly the manual retrieval pain he described.
3. **Report generation target identified.** Final reports render on a **radiology-group letterhead ("Southwest …")** — that's the template the pre-fill feature (REQ-004) must populate. The report editor lives on the **right monitor**; images on the ultrawide left.
4. **Dictation hardware confirmed.** A boom/stand **microphone** is mounted at the workstation — the voice-recognition system behind the corruption pain (REQ-010).

## What all clips jointly establish
- **Two-monitor workflow is central:** ultrawide = Exa PACS images, right monitor = report/dictation. Any overlay must respect this dual-screen layout (REQ-012).
- **Hanging-protocol pain is visually obvious (REQ-006):** repeated manual moves between multi-pane thumbnail grids and expanded single-pane reading, per study, across modalities.
- **Exa PACS is a browser-hosted UI** (top toolbar of view controls + left series "Navigator"), consistent with "Chrome + Exa" — supports the **browser-extension/overlay** approach as the phase-one integration hedge vs. a deep PACS API.
- **Modalities match the money:** head/sinus CT, brain MRI, and **coronary CTA** — the cardiovascular work he flagged as most lucrative and the natural home for the calcium-score pilot.

## What the videos do NOT give us (still open)
- **Camera fidelity is too low** to read the report editor's fields, the exact MESA calculator inputs, dictation-command syntax, or any UI/DOM/API detail needed to *build* the extension.
- No capture of the *transitions* at usable resolution (how a template loads, how the calculator is invoked).

## Recommendation
The clips are strong **context and validation** — they lock the pilot target (calcium score on coronary CTA) and the integration surface (browser-hosted Exa, dual monitor). But for the **build**, request one of:
- A **native screen recording** (Windows/QuickTime screen capture on his workstation) of the three loops we're automating — calcium-score entry, template pre-fill, hanging-protocol setup — **OR**
- A **live screen-share** during the technical-discovery call.

That yields the readable click-path + field-level detail the prototype needs. **None of this blocks the SRS or pilot scope** — the requirements stand; this sharpens the build.
