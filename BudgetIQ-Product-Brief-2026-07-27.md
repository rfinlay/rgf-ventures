# BudgetIQ — Product Brief

**For:** RGF Global Ventures · **Date:** 2026-07-27 · **Owner:** Rick · **Status:** Concept / roadmap (decision made 2026-07-27)

## One-liner
**BudgetIQ** is the budget-tracking module of the ProjectIQ suite: honest, reconciled **actuals-vs-budget** with forecasting and overrun alerts. Enterprise **OpEx/CapEx** focus; the personal finance instance ("Command Center"/Buffett) runs as the proof-of-concept and demo.

## Positioning
- **Completes the project financial lifecycle:** EstimateIQ (what will it cost) → ProcureIQ (buy it) → **BudgetIQ (track actuals vs budget, forecast overruns).**
- **Differentiator:** a fail-closed "honest numbers" engine, it never fabricates a figure, reconciles against source feeds, flags risk early (proven on Rick's own money).
- **Deliberately NOT** a consumer personal-finance app (crowded, low-margin). Enterprise/project budget tracking = higher ACV, stickier, rides RGF's PM/construction expertise.

## Suite fit
- EstimateIQ → ProcureIQ → **BudgetIQ** = coherent lifecycle.
- Shared customer: contractors / PMs / enterprises running capital + operating budgets.
- Personal **Command Center/Buffett** instance = dogfood + demo credibility + edge-case source.

## Reuse vs build
**Reusable now (~60-70%):** reconciliation engine (fail-closed), forecast/burn/runway, threshold guard → budget-variance/overrun alerts, dashboard shell + the data-source→JSON-summary→dashboard seam, balance-sheet + payoff modeling → CapEx/project P&L.
**Net-new for enterprise:** multi-tenant + auth (biggest lift), ERP/accounting connectors (QuickBooks/Xero/NetSuite/SAP), OpEx/CapEx/cost-center/project-code data model, RBAC, SOC2-flavored security.

## Naming
Product = **BudgetIQ** (fits *IQ convention, reads as SKU). Personal instance stays **Command Center**. No conflict.

## Phased roadmap
- **Phase 0 (now):** personal edition fully live — Plaid Phase B + debt APRs. Dogfood.
- **Phase 1:** OpEx/CapEx/cost-center domain model + first ERP connector (QuickBooks Online).
- **Phase 2:** multi-tenant + auth + RBAC; budget-vs-actual + variance/overrun alerts on real project data.
- **Phase 3:** suite integration (EstimateIQ budgets as baseline, ProcureIQ actuals as committed spend); pilot customer.
- **Phase 4:** security/compliance hardening for enterprise sales.

## Risks / honest notes
- Real product build, not a rename; multi-tenant + connectors + compliance is the bulk. Reusable engine = head start on the trust layer, not the whole job.
- Don't disrupt the working personal tool now. Avoid consumer personal finance as a revenue line.

## Recommendation
Fold in as **BudgetIQ**, enterprise OpEx/CapEx focus, personal edition as proof. Finish Plaid Phase B first; scope Phase 1 as a deliberate investment when ready.
