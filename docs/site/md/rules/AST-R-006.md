# AST-R-006 — `RemainingAssetBalance` is magnitude-typed on Asset, exactly as on SLSummary

*Assets, Equipment & Maintenance · Observed*

**Input: `Asset.RemainingAssetBalance`, field type `sTYPE_PERCENT_OR_AMOUNT`. Effect: A value 0–100 is read as a percentage;.**

Input: `Asset.RemainingAssetBalance`, field type `sTYPE_PERCENT_OR_AMOUNT`. Effect: A value 0–100 is read as a percentage; ≥ 100.01 is read as currency; the user may override the platform's guess. Confidence: Observed (`../../data-fields/asset.md`), corroborating the identical hazard `../accounting/README.md` finding 4 documents for `SLSummary.SLRemainingAssetBalance`.

## What it constrains

[Asset](../entities/Asset.md), [SLSummary](../entities/SLSummary.md)

Columns named: `Asset.RemainingAssetBalance`, `SLSummary.SLRemainingAssetBalance`

## Confidence

Observed (`../../data-fields/asset.md`), corroborating the identical hazard `../accounting/README.md` finding 4 documents for `SLSummary.SLRemainingAssetBalance`

---

Source: `docs/modules/assets-equipment/rules.md`
