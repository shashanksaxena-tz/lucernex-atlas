# AST-R-008 — An Asset Category code-table row is a GL routing decision, not a plain label

*Assets, Equipment & Maintenance · Observed*

**Input: `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/ `ActualLongName`/`Inactive`. Effect: Selecting an asset category also selects a GL account, a sub-account, and a per-category spending ceiling (`DNEAmount`, "Do Not Exceed").**

Input: `CodeAssetCategory.GLNumber`, `.SubAccount`, `.DNEAmount`, alongside `ShortName`/ `ActualLongName`/`Inactive`. Effect: Selecting an asset category also selects a GL account, a sub-account, and a per-category spending ceiling (`DNEAmount`, "Do Not Exceed"). Confidence: Observed (field list), corroborating the same pattern `../../data-model/code-table-registry.md` documents for `CodeExpenseType`.

## What it constrains

[CodeAssetCategory](../entities/CodeAssetCategory.md), [CodeExpenseType](../entities/CodeExpenseType.md)

Columns named: `CodeAssetCategory.GLNumber`

## Confidence

Observed (field list), corroborating the same pattern `../../data-model/code-table-registry.md` documents for `CodeExpenseType`

---

Source: `docs/modules/assets-equipment/rules.md`
