# CON-R-121 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**An accrual schedule is generated: period-by-period accrual amounts are produced from AccrualRate/DailyAccrualRate, with the same daily-rate support as recurring expense.**

An accrual schedule is generated: period-by-period accrual amounts are produced from AccrualRate/DailyAccrualRate, with the same daily-rate support as recurring expense.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An accrual schedule is generated |
| Stated as | `ExpenseAccrualSchedule.AccrualRate`, `.DailyAccrualRate`, `.PeriodAmount`, `.AnnualAmount`, `.BeginPeriod/Year`, `.EndPeriod/Year` |
| Stated as | Period-by-period accrual amounts, with daily-rate support |
| Stated as | L1 accrual rows |
| Stated as | Observed |

## What it constrains

[ExpenseAccrualSchedule](../entities/ExpenseAccrualSchedule.md)

Columns named: `ExpenseAccrualSchedule.AccrualRate`

---

Source: `docs/modules/contracts/rules.md`
