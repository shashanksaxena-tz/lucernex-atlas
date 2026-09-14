# TAX-R-003 — A PropertyTaxDetail must belong to exactly one PropertyTaxBill

*Property Tax · Observed*

**Input: `PropertyTaxDetail.PropertyTaxBillID`. Effect: Each tax-type breakdown line is scoped to one billing cycle.**

Input: `PropertyTaxDetail.PropertyTaxBillID`. Effect: Each tax-type breakdown line is scoped to one billing cycle. Confidence: Observed (`../../data-fields/property-tax-bill.md` references; `PropertyTaxDetail`'s own field list, `_lucernex_objects_summary.txt`).

## What it constrains

[PropertyTaxDetail](../entities/PropertyTaxDetail.md)

Columns named: `PropertyTaxDetail.PropertyTaxBillID`

## Confidence

Observed (`../../data-fields/property-tax-bill.md` references; `PropertyTaxDetail`'s own field list, `_lucernex_objects_summary.txt`)

---

Source: `docs/modules/property-tax/rules.md`
