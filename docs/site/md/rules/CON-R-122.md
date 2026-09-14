# CON-R-122 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**Accruals are forecast: ForecastCapPercent/ForecastGrowthPercent/ForecastAdjustment and their Plan* twins grow the accrual independently of the contract's own escalation.**

Accruals are forecast: ForecastCapPercent/ForecastGrowthPercent/ForecastAdjustment and their Plan* twins grow the accrual independently of the contract's own escalation.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Accruals are forecast |
| Stated as | `ExpenseAccrualSchedule.ForecastCapPercent`, `.ForecastGrowthPercent`, `.ForecastAdjustment`, `.PlanCapPercent`, `.PlanGrowthPercent`, `.PlanAdjustment` |
| Stated as | Planning/forecast growth is independent of contractual escalation |
| Stated as | Forecast amounts |
| Stated as | Observed |

## What it constrains

[ExpenseAccrualSchedule](../entities/ExpenseAccrualSchedule.md)

Columns named: `ExpenseAccrualSchedule.ForecastCapPercent`

---

Source: `docs/modules/contracts/rules.md`
