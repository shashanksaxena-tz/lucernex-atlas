# TAX-R-002 — A PropertyTaxBill must belong to exactly one PropertyTaxAssessment

*Property Tax · Observed*

**Input: `PropertyTaxBill.PropertyTaxAssessmentID`. Effect: A bill is always issued against a specific assessed value, never against the summary directly.**

Input: `PropertyTaxBill.PropertyTaxAssessmentID`. Effect: A bill is always issued against a specific assessed value, never against the summary directly. Confidence: Observed (`../../data-fields/property-tax-bill.md`).

## What it constrains

[PropertyTaxBill](../entities/PropertyTaxBill.md)

Columns named: `PropertyTaxBill.PropertyTaxAssessmentID`

## Confidence

Observed (`../../data-fields/property-tax-bill.md`)

---

Source: `docs/modules/property-tax/rules.md`
