# AST-R-005 — `Asset.AccountingBeginDate`/`AccountingEndDate` override the derived accounting window

*Assets, Equipment & Maintenance · Derived*

**Input: The two override fields. Effect: When populated, replace the accounting window that would otherwise be derived from the asset's `ExpenseSchedule` rows.**

Input: The two override fields. Effect: When populated, replace the accounting window that would otherwise be derived from the asset's `ExpenseSchedule` rows. Confidence: Observed — vendor field-definition text quoted in `equipment-leases.md`.

## What it constrains

[ExpenseSchedule](../entities/ExpenseSchedule.md)

## Confidence

Observed — vendor field-definition text quoted in `equipment-leases.md`

---

Source: `docs/modules/assets-equipment/rules.md`
