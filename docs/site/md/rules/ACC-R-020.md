# ACC-R-020 — Schedule-type change dirties the schedule

*Lease Accounting & Payments · Observed*

**`SLSummary.NeedsRecalculation := true`.**

Changing the ASC 842 or IFRS 16 schedule type on the Accounting Assumptions, Covenants or Recurring Expenses page sets Recalc? to Yes.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | `CodeASC842ScheduleID` or `CodeIFRS16ScheduleID` is changed on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page |
| What it writes | `SLSummary.NeedsRecalculation := true` |

## The wording it rests on

> This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES.

## What it constrains

[SLSummary](../entities/SLSummary.md), [ContractFinancialTest](../entities/ContractFinancialTest.md), [AcctingAssumptionAdjust](../entities/AcctingAssumptionAdjust.md), [Covenant](../entities/Covenant.md), [CodeExpenseType](../entities/CodeExpenseType.md)

## Confidence

Observed — the definition is repeated verbatim on `SLSummary`, `ContractFinancialTest`, `AcctingAssumptionAdjust`, `Covenant` and `CodeExpenseType`: "This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES."

---

Source: `docs/modules/accounting/rules.md`
