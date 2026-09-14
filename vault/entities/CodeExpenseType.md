---
title: CodeExpenseType
tags: [entity, configuration, accounting]
evidence: Observed
---

**`TableType 3013` · 31 fields · [[code-table]] `Expense Type Code`** — 107 values, the third-largest
code table.

**The exemplar of a behaviour-bearing code table.** It carries `CodeSLScheduleID`,
`CodeASC842ScheduleID` and `CodeIFRS16ScheduleID`, which means **choosing an expense type is choosing
which accounting schedules the money flows into**. A row here is a routing decision, not a label.

That single fact is what sizes the Masters model for ASG Edge+'s MDM-01: the 3000-band cannot be
modelled as a simple `(code, label, active)` triple.

*(The band generalisation itself is refuted — this table supports it and others do not. See
[[code-table]].)*

Feeds [[ExpenseSetup]] and, through it, the whole [[setup-schedule-transaction]] chain.
