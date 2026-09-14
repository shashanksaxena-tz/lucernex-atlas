# AST-R-007 — Two independent code-table lookups on Asset resolve to the same table, for different UI roles

*Assets, Equipment & Maintenance · Observed*

**Input: `Asset.CodeAssetCategoryID` (labelled Maintenance Category) and `Asset.CodeDesc_CodeAssetCategoryID` (labelled Account #), both FKs to `CodeAssetCategory`. Effect: The same code table serves a maintenance-classification role and a GL-account-lookup role from the same parent record, via two….**

Input: `Asset.CodeAssetCategoryID` (labelled Maintenance Category) and `Asset.CodeDesc_CodeAssetCategoryID` (labelled Account #), both FKs to `CodeAssetCategory`. Effect: The same code table serves a maintenance-classification role and a GL-account-lookup role from the same parent record, via two separate columns. Confidence: Observed (`../../data-fields/asset.md`).

## What it constrains

[Asset](../entities/Asset.md), [CodeAssetCategory](../entities/CodeAssetCategory.md)

Columns named: `Asset.CodeAssetCategoryID`, `Asset.CodeDesc_CodeAssetCategoryID`

## Confidence

Observed (`../../data-fields/asset.md`)

---

Source: `docs/modules/assets-equipment/rules.md`
