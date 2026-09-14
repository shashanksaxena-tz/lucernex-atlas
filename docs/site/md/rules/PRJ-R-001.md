# PRJ-R-001

*Capital Projects & Scheduling · Derived*

**Any object needs to reference a schedule row · `Task/Group ID` FK type · Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transactions`, and `workflow` points at `TaskGroup`. `Task` and `TaskItem` are never targeted, despite….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Any object needs to reference a schedule row |
| Stated as | `Task/Group ID` FK type |
| Stated as | Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transactions`, and `workflow` points at `TaskGroup`. `Task` and `TaskItem` are never targeted, despite sharing an identical 37-field shape. Read `TaskGroup` as the one real schedule-row table. |
| Stated as | Derived — see `scheduling.md` §1 |

## What it constrains

[TaskGroup](../entities/TaskGroup.md), [Task](../entities/Task.md), [TaskItem](../entities/TaskItem.md)

---

Source: `docs/modules/projects-capital/rules.md`
