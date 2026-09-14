---
title: ExpenseSchedule
tags: [entity, accounting, contracts]
evidence: Observed
---

**`expense_schedule` · 51 fields · [[module-accounting]]**

The generated billing schedule — the **schedule** layer of [[setup-schedule-transaction]], expanded
from [[ExpenseSetup]] by an operator-invoked generator, and discriminated by carrying a
`ProcessedFlag` the clause layer lacks.

The supported correction path is **delete and regenerate**, not edit in place ([[rule-CON-R-010]]).

Its rows define the accounting window — unless [[Asset]]`.AccountingBeginDate`/`EndDate` are
populated, in which case those **override** it ([[rule-AST-R-005]]).

`ASG Approval - Expense Schedules` (99146) is one of the two `ASG Approval - *` list layouts that make
up the [[atlas-ai-abstraction|abstraction pipeline]]'s own UI.
