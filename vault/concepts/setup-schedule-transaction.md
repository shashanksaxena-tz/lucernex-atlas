---
title: Clause → Schedule → Transaction → Projection
tags: [concept, contracts, accounting, core]
evidence: Observed
---

Not five financial subsystems — **one architectural pattern applied five times**, plus one outlier.
This is the single most useful idea for reading the contracts module.

| Layer | Is | Discriminator |
|---|---|---|
| **Clause** | human-entered terms | `AmendmentID` + `Section` |
| **Schedule** | operator-invoked expansion into period rows | the above **+ `ProcessedFlag`** |
| **Transaction** | posted money with a GL account and a counterparty | `PostingDate` + GL + counterparty |
| **Projection** | forward calculation, never stored | a [[virtual-projection\|`Virtual*`]] object |

So `ExpenseSetup → ExpenseSchedule → PaymentTransaction` is the same shape as
`PercentageRent → VirtualPercentageRentPeriod`, and so on.

Three consequences that repeatedly bite:

- **Generation is user-invoked, not batch.** `Generate Rent` and `Calculate Schedule` are buttons on a
  record ([[finding-engine-is-button-driven]]).
- **The supported correction path is delete-then-regenerate**, not in-place editing of generated
  output ([[rule-CON-R-010]]).
- **Payable-versus-receivable direction is carried per clause and per transaction, not on the
  [[Contract]]** — one contract may be both ([[rule-CON-R-019]]).

**[[cam-waterfall|CAM does not follow the pattern]]**, and that is the module's stated centrepiece.

Source: [`modules/contracts/setup-schedule-transaction-pattern.md`](../../docs/modules/contracts/setup-schedule-transaction-pattern.md)
