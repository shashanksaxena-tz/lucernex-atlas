# TAX-R-011 — An appeal's outcome does not automatically adjust an already-issued bill

*Property Tax · Derived*

**Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills already issued or paid is not represented anywhere in this….**

Input: No FK from `PropertyTaxAppeal` or `PropertyTaxAppealAward` to `PropertyTaxBill` or `PropertyTaxDetail`. Effect: Reconciling a won appeal's computed reduction (`AssessmentReduction`/`TaxReduction`/`NetTaxReduction`) against bills already issued or paid is not represented anywhere in this object model. Confidence: Derived (absence of any such FK, exhaustive read); see `appeals.md`§3.

## What it constrains

[PropertyTaxAppeal](../entities/PropertyTaxAppeal.md), [PropertyTaxAppealAward](../entities/PropertyTaxAppealAward.md), [PropertyTaxBill](../entities/PropertyTaxBill.md), [PropertyTaxDetail](../entities/PropertyTaxDetail.md)

## Confidence

Derived (absence of any such FK, exhaustive read); see `appeals.md`§3

---

Source: `docs/modules/property-tax/rules.md`
