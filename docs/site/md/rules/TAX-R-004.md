# TAX-R-004 — A PropertyTaxAppeal must belong to exactly one PropertyTaxAssessment

*Property Tax · Observed*

**Input: `PropertyTaxAppeal.PropertyTaxAssessmentID`. Effect: An appeal always contests one specific dated assessed value, never the ongoing Summary as a whole.**

Input: `PropertyTaxAppeal.PropertyTaxAssessmentID`. Effect: An appeal always contests one specific dated assessed value, never the ongoing Summary as a whole. Confidence: Observed (`../../data-fields/property-tax-appeal.md`).

## What it constrains

[PropertyTaxAppeal](../entities/PropertyTaxAppeal.md)

Columns named: `PropertyTaxAppeal.PropertyTaxAssessmentID`

## Confidence

Observed (`../../data-fields/property-tax-appeal.md`)

---

Source: `docs/modules/property-tax/rules.md`
