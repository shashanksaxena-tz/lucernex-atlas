---
title: TaskGroup
tags: [entity, projects]
evidence: Observed
---

**`task_group` · 37 fields · [[module-projects-capital]]**

The grouping node in the task tree — and **the only one of the three identical task tables anything
points at**: 11 objects, 18 columns, all the `Task/Group ID` traffic ([[rule-PRJ-R-001]]).

It carries **two separate graphs over the same rows** ([[rule-PRJ-R-006]]):

- `ParentTaskID` — the **WBS hierarchy** (what contains what)
- `TskPredVal_PredecessorTaskID` — the **CPM dependency network** (what must finish first)

Both are self-references on this one table. A rebuild that models "the task tree" as one graph cannot
express a schedule.

The deal pipeline reuses it directly — [[RETransaction]] and [[Scenario]] schedules are `TaskGroup`
rows, so **the deal pipeline has no scheduling engine of its own** ([[rule-PRJ-R-013]]).

`WorkFlow.KickOffTaskID` points here, corroborating the `KickOffMethod.TASK` enum
([[rule-PRJ-R-012]]).
