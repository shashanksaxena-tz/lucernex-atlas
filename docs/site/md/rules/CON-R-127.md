# CON-R-127 — 10. Suppression and gating

*Contracts & Leases · Observed*

**Forecast inclusion: only ExpenseSetup rows flagged IncludeInPlanForecast appear in VirtualExpenseForecastPeriod.**

Forecast inclusion: only ExpenseSetup rows flagged IncludeInPlanForecast appear in VirtualExpenseForecastPeriod.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Forecast inclusion |
| Stated as | `ExpenseSetup.IncludeInPlanForecast`, `CodePlanForecastBasedOnID`, `CodePlanForecastGroupID` |
| Stated as | Only flagged clauses appear in `VirtualExpenseForecastPeriod` |
| Stated as | Forecast scope |
| Stated as | Observed |

## What it constrains

[ExpenseSetup](../entities/ExpenseSetup.md), [VirtualExpenseForecastPeriod](../entities/VirtualExpenseForecastPeriod.md)

Columns named: `ExpenseSetup.IncludeInPlanForecast`

---

Source: `docs/modules/contracts/rules.md`
