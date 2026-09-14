# AST-R-016 — `AssetHistory` is entity-scoped in practice despite its mechanical `firm_global` label

*Assets, Equipment & Maintenance · Derived*

**Input: `AssetHistory.ProjectEntityID` and `.FromProjectEntityID`, both typed the soft `Entity` type rather than the hard `Entity ID` type. Effect: The object behaves as an entity-scoped snapshot of an `Asset`'s state, but escapes the mechanical role classifier that looks only for the hard FK type.**

Input: `AssetHistory.ProjectEntityID` and `.FromProjectEntityID`, both typed the soft `Entity` type rather than the hard `Entity ID` type. Effect: The object behaves as an entity-scoped snapshot of an `Asset`'s state, but escapes the mechanical role classifier that looks only for the hard FK type. Confidence: Derived, corroborating `../../data-model/project-entity.md` §2's own naming of this exact object as a false negative.

## What it constrains

[AssetHistory](../entities/AssetHistory.md), [Asset](../entities/Asset.md)

Columns named: `AssetHistory.ProjectEntityID`

## Confidence

Derived, corroborating `../../data-model/project-entity.md` §2's own naming of this exact object as a false negative

---

Source: `docs/modules/assets-equipment/rules.md`
