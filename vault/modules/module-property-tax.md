---
title: Property tax
tags: [module, property-tax]
evidence: Derived
---

**6 objects · 163 fields · rules `TAX-R-001`…`TAX-R-012`** — all six entity-scoped. **No live screen
was ever captured**, so confidence tops out at Derived except where noted.

A five-level roll-up under a single [[Parcel]] — never a [[Facility]], never a [[Contract]]:

```
PropertyTaxSummary → PropertyTaxAssessment → { PropertyTaxBill → Detail
                                              PropertyTaxAppeal → Award }
```

Entities: [[PropertyTaxSummary]] · [[PropertyTaxAssessment]] · [[PropertyTaxBill]] ·
[[PropertyTaxAppeal]]

Two facts shape everything:

- **Property tax is a recoverable [[cam-waterfall|CAM]] expense**, not a landlord bill —
  `CodeRecoveryGroupID` / `CodeRecoveryTypeID` on the summary ([[rule-TAX-R-009]]).
- **A won appeal is reconciled nowhere.** No FK connects the appeal branch back to the bill
  ([[rule-TAX-R-011]]).

[[PropertyTaxBill]] is the only member reachable from the payment engine ([[rule-TAX-R-010]]).

Seven code tables, `2184`–`2190`, four of them easily confused, **none opened**.

Rules: [[rules-property-tax]] ·
[`modules/property-tax/`](../../docs/modules/property-tax/README.md)
