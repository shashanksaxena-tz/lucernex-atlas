---
title: PropertyTaxAppeal
tags: [entity, property-tax]
evidence: Derived
---

**`property_tax_appeal` · 41 fields · [[module-property-tax]]** — the largest object in its module.

Contests one dated [[PropertyTaxAssessment]], carrying filing details, fees and the resulting
reduction.

**The gap is the finding: no foreign key connects `PropertyTaxAppeal` or `PropertyTaxAppealAward` back
to [[PropertyTaxBill]] or `PropertyTaxDetail`** ([[rule-TAX-R-011]]). A won appeal's reduction is
**reconciled nowhere**. If a bill has already been issued and the appeal then succeeds, the product
has no modelled path from the award to the bill.

Four of the seven property-tax code tables (`2186` Tax Appeal Result, `2187` Tax Appeal Status,
`2184` Property Tax Status, `2185` Property Tax Type) are easily confused with one another and **none
was opened**.
