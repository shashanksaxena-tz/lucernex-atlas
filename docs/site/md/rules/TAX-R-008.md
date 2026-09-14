# TAX-R-008 — Property tax expenses route through the same Expense Type/Group mechanism as any other recoverable expense

*Property Tax · Observed*

**Input: `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`, `PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. Effect: Selecting an expense type/group on a property-tax record is a GL-routing decision, identical in mechanism to `CodeExpenseType`'s role documented in….**

Input: `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`, `PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. Effect: Selecting an expense type/group on a property-tax record is a GL-routing decision, identical in mechanism to `CodeExpenseType`'s role documented in `../../data-model/code-table-registry.md`. Confidence: Observed (field presence).

## What it constrains

[PropertyTaxSummary](../entities/PropertyTaxSummary.md), [PropertyTaxAppeal](../entities/PropertyTaxAppeal.md), [CodeExpenseType](../entities/CodeExpenseType.md)

Columns named: `PropertyTaxSummary.CodeExpenseGroupID`, `PropertyTaxAppeal.CodeExpenseGroupID`

## Confidence

Observed (field presence)

---

Source: `docs/modules/property-tax/rules.md`
