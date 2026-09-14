# POR-R-016

*Portfolio & Real-Estate Transactions · Derived*

**`Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, `TaskGroup`, and `TaskItem` are byte-identical 37-field….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read |
| Stated as | `Task/Group ID` FK type |
| Stated as | The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, `TaskGroup`, and `TaskItem` are byte-identical 37-field tables — treat the resolution as "one of the three," not as proof a deal step is never a plain `Task`. |
| Stated as | Derived, low confidence on the specific target |

## What it constrains

[Task](../entities/Task.md), [TaskGroup](../entities/TaskGroup.md), [RETransaction](../entities/RETransaction.md), [Scenario](../entities/Scenario.md), [TaskItem](../entities/TaskItem.md)

---

Source: `docs/modules/portfolio-transactions/rules.md`
