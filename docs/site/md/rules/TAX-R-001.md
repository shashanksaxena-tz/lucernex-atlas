# TAX-R-001 — A PropertyTaxAssessment must belong to exactly one PropertyTaxSummary

*Property Tax · Observed*

**Trigger: Assessment create/save. Input: `PropertyTaxAssessment.PropertyTaxSummaryID`.**

Trigger: Assessment create/save. Input: `PropertyTaxAssessment.PropertyTaxSummaryID`. Effect: Required FK; save is blocked without a parent Summary. Confidence: Observed (`Required = Yes`, `../../data-fields/property-tax-assessment.md`).

## What it constrains

[PropertyTaxAssessment](../entities/PropertyTaxAssessment.md)

Columns named: `PropertyTaxAssessment.PropertyTaxSummaryID`

## Confidence

Observed (`Required = Yes`, `../../data-fields/property-tax-assessment.md`)

---

Source: `docs/modules/property-tax/rules.md`
