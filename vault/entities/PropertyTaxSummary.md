---
title: PropertyTaxSummary
tags: [entity, property-tax]
evidence: Observed
---

**`property_tax_summary` · 32 fields · [[module-property-tax]]**

The top of the property-tax roll-up: assessment amount, percent and billing frequency, per
[[Parcel]].

It carries `CodeRecoveryGroupID` and `CodeRecoveryTypeID`, which makes **property tax explicitly a
recoverable [[cam-waterfall|CAM]] expense**, not a simple landlord bill ([[rule-TAX-R-009]]). That is
the module's most consequential single fact.

The chain below it: `PropertyTaxSummary → `[[PropertyTaxAssessment]]` → {`[[PropertyTaxBill]]` → Detail,
`[[PropertyTaxAppeal]]` → Award}`.

All six objects carry a **direct required `ParcelID`** as well as their chain parent, and nothing
enforces agreement between the two ([[rule-TAX-R-006]]).
