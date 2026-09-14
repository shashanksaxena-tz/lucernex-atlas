---
title: ExpenseEscalation
tags: [entity, accounting, contracts]
evidence: Observed
---

**`expense_escalation` · 28 fields · [[module-accounting]]**

The automatic escalation clause on a recoverable expense: fixed percentage, or indexed to an
[[EscalationIndex]] series.

The cap machinery stacks: cap, floor and a lifetime collar, configured through `Cap Type Code`
(`2164`) and the escalation code-table family. See
[`escalations.md`](../../docs/modules/contracts/escalations.md).

Changing a schedule type on the recurring-expense side sets [[SLSummary]]`.NeedsRecalculation`
([[rule-ACC-R-020]]) — escalation changes propagate into the accounting engine.
