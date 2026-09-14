---
title: Assets and equipment
tags: [module, assets]
evidence: Observed
---

**8 objects · 230 fields · rules `AST-R-001`…`AST-R-016`**

Three unrelated concerns under one dashboard heading: the [[Asset]] record, the reactive-maintenance
ticket chain, and a parts catalog. **605 assets** in the live tenant.

Entities: [[Asset]] · [[AssetHistory]] · [[Issue]]

The module's most valuable file is `equipment-leases.md`, and its finding is
[[finding-accounting-runs-per-asset]]: [[ContractFinancialTest]], [[SLSummary]] and [[SLPeriod]] each
carry a nullable `AssetID`, so the ASC 842 / IFRS 16 engine runs per equipment asset.
[[tenant-bbw|BBW]]'s [[equipment-contract|Equipment Contract]] root is the same thing observed from
the front.

- `RemainingAssetBalance` is **magnitude-typed** — 0–100 is a percent, ≥100.01 is currency
  ([[rule-AST-R-006]]). A genuine landmine.
- The maintenance loop is **button-generated, never automatic** ([[rule-AST-R-011]]), and
  `ServiceRequest`/`WorkOrder` are undeclared [[Issue]] variants the FK graph misses entirely
  ([[soft-reference]]).
- **Parts are recorded against the Issue, not the WorkOrder** ([[rule-AST-R-014]]), and the catalog
  carries **no per-location stock** — one firm-wide count per part ([[rule-AST-R-015]]).

Rules: [[rules-assets-equipment]] ·
[`modules/assets-equipment/`](../../docs/modules/assets-equipment/README.md)
