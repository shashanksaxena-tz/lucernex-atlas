---
title: "CON-R-001 — The four-layer classifier"
tags: [rule, contracts]
evidence: Observed
---

**`CON-R-001`** · [[module-contracts]] · **Observed**

Every financial record in the module resolves to exactly one layer, by discriminator:

| Layer | Discriminator |
|---|---|
| CLAUSE | `AmendmentID` + `Section` |
| SCHEDULE | the above **+ `ProcessedFlag`** |
| TRANSACTION | `PostingDate` + GL + counterparty |
| PROJECTION | it is a [[virtual-projection\|`Virtual*`]] object |

This is the test that makes [[setup-schedule-transaction]] usable rather than descriptive.

See [[rules-contracts]] for the full register.
