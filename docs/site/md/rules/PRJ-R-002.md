# PRJ-R-002

*Capital Projects & Scheduling · Observed*

**An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierarchy, no dependency graph, no resource tracking.….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) |
| Stated as | `ProcessTimeline` → `ProcessTimelineTemplate` |
| Stated as | Produces a flat, non-networked milestone list — no hierarchy, no dependency graph, no resource tracking. Deliberately simpler than `TaskGroup`. |
| Stated as | Observed (field-list diff) |

## What it constrains

[ProjectEntity](../entities/ProjectEntity.md), [ProcessTimeline](../entities/ProcessTimeline.md), [ProcessTimelineTemplate](../entities/ProcessTimelineTemplate.md), [TaskGroup](../entities/TaskGroup.md)

---

Source: `docs/modules/projects-capital/rules.md`
