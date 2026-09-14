# PRJ-R-013

*Capital Projects & Scheduling · Observed*

**A real-estate deal step needs its own schedule · `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) · Both reuse `TaskGroup` directly — the deal pipeline has no schedule engine of its own. · Observed.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A real-estate deal step needs its own schedule |
| Stated as | `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) |
| Stated as | Both reuse `TaskGroup` directly — the deal pipeline has no schedule engine of its own. |
| Stated as | Observed |

## What it constrains

[RETransaction](../entities/RETransaction.md), [Scenario](../entities/Scenario.md), [TaskGroup](../entities/TaskGroup.md)

Columns named: `RETransaction.DealSchedule`, `Scenario.DealSchedule`

---

Source: `docs/modules/projects-capital/rules.md`
