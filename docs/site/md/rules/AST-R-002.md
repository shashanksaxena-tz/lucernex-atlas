# AST-R-002 — An Asset may carry a second, independent soft pointer

*Assets, Equipment & Maintenance · Inferred*

**Input: `Asset.AssociatedProjectEntityID`, typed the soft `Entity` type (not `Entity ID`). Effect: Distinct from the primary `ProjectEntityID` scope — allows an asset record to reference a second entity beyond the one it is scoped to.**

Input: `Asset.AssociatedProjectEntityID`, typed the soft `Entity` type (not `Entity ID`). Effect: Distinct from the primary `ProjectEntityID` scope — allows an asset record to reference a second entity beyond the one it is scoped to. Confidence: Inferred — the column's presence and type are Observed; what a populated value is used for at render time was not captured.

## What it constrains

[Asset](../entities/Asset.md)

Columns named: `Asset.AssociatedProjectEntityID`

## Confidence

Inferred — the column's presence and type are Observed; what a populated value is used for at render time was not captured

---

Source: `docs/modules/assets-equipment/rules.md`
