---
title: ExpenseSetup
tags: [entity, accounting, contracts]
evidence: Observed
---

**`expense_setup` · 96 fields · [[module-accounting]]**

The recurring-expense billing configuration — the **clause** layer, and the root of the schedule
chain: `ExpenseSetup → `[[ExpenseSchedule]]` → `[[PaymentTransaction]]. Referenced by 10 objects.

Step 5 of the [[screen-contract-wizard|contract wizard]] collects it in 22 fields: recurring rent and
expense with escalation. So a contract is created with its first recurring charge already configured.

`ASG Lease Abstract - Expense Setup` (102252) and `- Expense Schedule` (102251) are both part of the
[[atlas-ai-abstraction|abstraction]] layout family, and they match one-for-one the financial layers
stepped through by the `Implementation Workflow - Financial Abstraction` workflow.

Choosing the expense **type** is choosing which accounting schedules the money flows into —
`CodeExpenseType` carries `CodeSLScheduleID`, `CodeASC842ScheduleID` and `CodeIFRS16ScheduleID`. See
[[CodeExpenseType]].
