# PRJ-R-007

*Capital Projects & Scheduling · Inferred*

**The Gantt engine (`TaskGantt2.jsp`) needs a task's critical-path status · `TaskGroup.OnCriticalPath`, `DaysAheadOfSchedule` · Plausibly computed by walking the `TaskPredecessor` graph; no formula or screen confirms the exact computation.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | The Gantt engine (`TaskGantt2.jsp`) needs a task's critical-path status |
| Stated as | `TaskGroup.OnCriticalPath`, `DaysAheadOfSchedule` |
| Stated as | Plausibly computed by walking the `TaskPredecessor` graph; no formula or screen confirms the exact computation. |
| Stated as | Inferred |

## What it constrains

[TaskGroup](../entities/TaskGroup.md), [TaskPredecessor](../entities/TaskPredecessor.md)

Columns named: `TaskGroup.OnCriticalPath`

---

Source: `docs/modules/projects-capital/rules.md`
