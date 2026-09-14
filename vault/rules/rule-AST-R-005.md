---
title: "AST-R-005 — Asset dates override the schedule window"
tags: [rule, assets-equipment]
evidence: Observed
---

**`AST-R-005`** · [[module-assets-equipment]] · **Observed**

`Asset.AccountingBeginDate` / `EndDate`, **when populated, override** the window derived from
[[ExpenseSchedule]] rows. A silent precedence that a rebuild must reproduce or deliberately reject.

See [[rules-assets-equipment]] for the full register.
