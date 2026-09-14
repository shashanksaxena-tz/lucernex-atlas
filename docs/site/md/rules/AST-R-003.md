# AST-R-003 — An Asset's equipment lease is a hard, typed FK

*Assets, Equipment & Maintenance · Observed*

**Input: `Asset.FinancialContractID`, typed `Contract ID`. Effect: Ties the asset to the equipment-flavour `Contract` that finances it, independent of the entity it is physically scoped to.**

Input: `Asset.FinancialContractID`, typed `Contract ID`. Effect: Ties the asset to the equipment-flavour `Contract` that finances it, independent of the entity it is physically scoped to. Confidence: Observed (`../../data-fields/asset.md`).

## What it constrains

[Asset](../entities/Asset.md), [Contract](../entities/Contract.md)

Columns named: `Asset.FinancialContractID`

## Confidence

Observed (`../../data-fields/asset.md`)

---

Source: `docs/modules/assets-equipment/rules.md`
