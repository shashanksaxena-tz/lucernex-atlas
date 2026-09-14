# ACC-R-025 — Cash-flow routing by expense type

*Lease Accounting & Payments · Derived*

**each period cash flow is routed to the schedule type its expense type designates for the standard being generated.**

Each cash flow lands on the schedule its expense type designates for the standard being generated.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | schedule generation |
| What it reads | `ExpenseSchedule` rows → `ExpenseSetup.CodeExpenseTypeID` → `CodeExpenseType.CodeSLScheduleID` / `.CodeASC842ScheduleID` / `.CodeIFRS16ScheduleID` |
| What it computes | each period cash flow is routed to the schedule type its expense type designates for the standard being generated |
| What it writes | `SLPeriod.PeriodCashAmount` populated on the correct `SLSummary` |

## The wording it rests on

> Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts.

## What it constrains

[ExpenseSchedule](../entities/ExpenseSchedule.md), [ExpenseSetup](../entities/ExpenseSetup.md), [CodeExpenseType](../entities/CodeExpenseType.md), [SLPeriod](../entities/SLPeriod.md), [SLSummary](../entities/SLSummary.md)

Columns named: `ExpenseSetup.CodeExpenseTypeID`, `CodeExpenseType.CodeSLScheduleID`, `SLPeriod.PeriodCashAmount`

## Confidence

Derived from the three FK columns on `CodeExpenseType` plus the vendor statement "Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts." - Live state ↑ upgraded: in this tenant the routing has exactly one possible destination. `ASC 842 Schedule Type Code` (`TableType` 2162) holds one row, `842 Rent`; `Straight Line Schedule Type Code` (2161) and `IFRS 16 Schedule Type Code` (2163) are both empty. So `CodeExpenseType.CodeSLScheduleID` and `.CodeIFRS16ScheduleID` have no valid target and must be null everywhere, and every cash flow resolves to `842 Rent`. Observed, 2026-09-10, `docs/data-model/code-table-registry.md`

---

Source: `docs/modules/accounting/rules.md`
