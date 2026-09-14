---
title: Asset
tags: [entity, assets, accounting, core]
evidence: Observed
---

**`asset` · 122 fields · [[module-assets-equipment]]**

The fixed-asset / right-of-use-asset record. **605 assets** in the live tenant.

Its load-bearing property is that it carries **its own 13-field ASC 842 / IFRS 16 classification
overlay**, parallel to [[Contract]]'s ([[rule-AST-R-004]]) — and that
[[ContractFinancialTest]], [[SLSummary]] and [[SLPeriod]] each carry a **nullable `AssetID`**. Together
that is [[finding-accounting-runs-per-asset]]: the lease-accounting engine runs per equipment asset,
not only per lease. Which overlay wins when both are populated is **Inferred and unresolved**.

Other facts worth keeping:

- It attaches via a **soft `ProjectEntityID` only** — no hard `FacilityID` or `LocationID`
  ([[rule-AST-R-001]]).
- `Asset.AccountingBeginDate`/`EndDate`, when populated, **override** the window derived from
  [[ExpenseSchedule]] rows ([[rule-AST-R-005]]).
- `RemainingAssetBalance` is **magnitude-typed**: 0–100 reads as a percent, ≥100.01 as currency, and
  the user can override ([[rule-AST-R-006]]). That is a genuine landmine for a rebuild.
- `Asset.DiscountRateOverride` is one of the two candidate paths by which a rate could reach the
  engine at all — see [[finding-discount-rate-table-empty]].

The maintenance loop below it is **button-generated, never automatic** ([[rule-AST-R-011]]):
`ServiceRequest` → `WorkOrder`, each 1:1 with an underlying [[Issue]].

See [[equipment-contract]] · [[AssetHistory]]
