# PRJ-R-006

*Capital Projects & Scheduling · Derived*

**A `TaskGroup` row's schedule position is computed · `ParentTaskID` (hierarchy) vs. `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID` (dependency network) · Two independent graphs.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A `TaskGroup` row's schedule position is computed |
| Stated as | `ParentTaskID` (hierarchy) vs. `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID` (dependency network) |
| Stated as | Two independent graphs. A task's WBS parent is not required to be, and generally is not, the same row as its schedule predecessor. |
| Stated as | Derived — see `scheduling.md` §2 |

## What it constrains

[TaskGroup](../entities/TaskGroup.md), [TaskPredecessor](../entities/TaskPredecessor.md)

Columns named: `TaskPredecessor.PredecessorTaskID`

---

Source: `docs/modules/projects-capital/rules.md`
