# ACC-R-021 — New expense setup dirties the schedule that uses its expense type

*Lease Accounting & Payments · Observed*

**the accounting schedule associated with that expense type is dirtied.**

Creating an expense setup with a schedule flips Recalc? on whichever accounting schedule uses that expense type.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | an `ExpenseSetup` with an `ExpenseSchedule` is created |
| What it reads | `ExpenseSetup.CodeExpenseTypeID`; `SLSummary.AssociatedExpenseSetupIDs` |
| The test | the accounting schedule associated with that expense type is dirtied |
| What it writes | `SLSummary.NeedsRecalculation := true`; `AssociatedExpenseSetupIDs` extended |

## The wording it rests on

> If a new expense setup with an expense schedule is created, the accounting schedule associated with the expense type will have its Recalc? flag flipped to Yes.

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [ExpenseSchedule](../entities/ExpenseSchedule.md), [SLSummary](../entities/SLSummary.md)

Columns named: `ExpenseSetup.CodeExpenseTypeID`, `SLSummary.AssociatedExpenseSetupIDs`

## Confidence

Observed — "If a new expense setup with an expense schedule is created, the accounting schedule associated with the expense type will have its Recalc? flag flipped to Yes."

---

Source: `docs/modules/accounting/rules.md`
