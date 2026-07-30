# Video Review Addendum — RadAssist
**2026-07-30 | Source: 2 of 3 workflow clips (phone-camera captures of Luis's live reading station)**

> **PHI note:** Clips are phone videos of live PACS screens and contain patient identifiers. Reviewed locally only; no patient data reproduced here or transmitted. Extracted analysis frames were deleted after review. Original clips remain in Rick's OneDrive.

## What the clips are
- **Clip 1** (`192718`, ~3.5 min): CT head study in Exa PACS — multi-pane hanging protocol, then single-pane slice navigation (soft-tissue + bone windows).
- **Clip 2** (`201136`, ~2.9 min): Chest/cardiac CT (contrast) — single-pane zoom/navigation.
- Both are **handheld phone recordings of the monitors**, not clean screen captures — so they validate the *workflow shape* but are too low-fidelity to read fine UI text, menu paths, or API hints.

## What they confirm/add to the SRS
1. **Two-monitor workflow is real and central:** ultrawide monitor for images (Exa PACS), separate right-hand monitor for the report/dictation column. Reinforces REQ-012 (non-intrusive companion) and the two-window UI expectation — any overlay must respect this dual-screen layout.
2. **Hanging-protocol pain is visually obvious (REQ-006):** he manually moves between the multi-pane thumbnail grid (left "Navigator" sidebar) and expanded single-pane reading, per study. This is exactly the repetitive screen-organization setup to persist/automate.
3. **Exa PACS is a browser-hosted UI** with a top toolbar of view controls + left series navigator — consistent with the "Chrome + Exa" environment. Supports the **browser-extension/overlay** approach as the phase-one integration hedge (vs. deep PACS API).
4. **Modalities match the money:** head CT and cardiac/chest CT on screen — the cardiovascular work he flagged as most lucrative, and the natural home for the calcium-score pilot.

## What they do NOT give us (still open)
- No readable view of the **report/template editor**, the **MESA calculator**, or the **dictation** interaction — the exact screens the Tier-1 pilot automates.
- No UI/DOM/API detail for building the extension (camera fidelity too low).

## Recommendation
The phone clips are good context but **not sufficient for integration specs.** For the build, request one of:
- A **native screen recording** (QuickTime/Windows screen capture on his workstation) of the specific loops we're automating — calcium-score entry, template pre-fill, and hanging-protocol setup — OR
- A **live screen-share** during the technical-discovery call.

That yields the readable UI/click-path detail the browser-extension prototype needs. The 3rd clip is still pending upload; I'll fold it in when it lands. None of this blocks the SRS or the pilot scope — it sharpens the build, not the requirements.
