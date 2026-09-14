# PRJ-R-012

*Capital Projects & Scheduling · Derived*

**A workflow needs to be triggered by a schedule event · `WorkFlow.KickOffTaskID` → `TaskGroup` · Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state can kick off a workflow. · Derived.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A workflow needs to be triggered by a schedule event |
| Stated as | `WorkFlow.KickOffTaskID` → `TaskGroup` |
| Stated as | Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state can kick off a workflow. |
| Stated as | Derived |

## What it constrains

[WorkFlow](../entities/WorkFlow.md), [TaskGroup](../entities/TaskGroup.md)

Columns named: `WorkFlow.KickOffTaskID`

---

Source: `docs/modules/projects-capital/rules.md`
