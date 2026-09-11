# Capital Projects & Scheduling — module overview

**Stated up front.** This module is the product's generic scheduling and issue-tracking engine,
reused across capital project delivery, real-estate deal steps, and workflow triggers. **23
objects, 376 fields.** Its central technical finding mirrors the accounting module's: **`Task`,
`TaskGroup`, and `TaskItem` are three byte-identical 37-field tables**, and every single FK of the
ambiguous type `Task/Group ID` anywhere in the 223-object schema — across this module,
`portfolio-transactions`, and `workflow` — resolves to **`TaskGroup` alone**. `Task` and `TaskItem`
receive zero inbound foreign keys anywhere in the product. Second: `Task.ParentTaskID` (a
hierarchy) and `TaskPredecessor` (a dependency network) are two **independent** graph structures
over the same row set — a WBS tree and a CPM predecessor network, not one thing. Third: the module
owns the generic `Issue` record — already established from the routing layer
([`code-table-registry.md`](../../data-model/code-table-registry.md),
[`screen-routing.md`](../../data-model/screen-routing.md)) as the record behind every "Form" — and
this module is where its non-form use (RFIs, change-order threads, bidder Q&A) lives.

**Note on `Project` itself:** the schema object that is a Capital Project or Opening Project
(`Project`, 111 fields) is **not** in this module's object list — [`modules.json`](../../mindmap/modules.json)
classifies it under `platform-tenancy`. This module is genuinely about *scheduling and issue
tracking*, which `Project` (and every other `ProjectEntity`) consumes via `ProjectEntityID`, not
about the Project record itself. See
[`../portfolio-transactions/site-pipeline.md`](../portfolio-transactions/site-pipeline.md) §3 for
`Project`'s own treatment.

*Evidence class for this paragraph: **Observed** field lists and FK edges from
`_lucernex_objects_summary.txt` and `docs/mindmap/edges.json`. Full citations in
[`data-model.md`](data-model.md) and [`scheduling.md`](scheduling.md).*

## The module at a glance

| Property | Value |
|---|---|
| Objects | 23 |
| Fields | 376 |
| Scheduling family | `Task`, `TaskGroup`, `TaskItem` (byte-identical, 37 fields each), `TaskPredecessor`, `TaskTemplate`, `TaskTemplateAudit`, `VirtualTemplateSchedule`, `LinkTaskMember`, `LinkTaskByCodeMember`, `LinkTaskDocument` |
| Milestone family | `ProcessTimeline`, `ProcessTimelineTemplate` — a simpler, non-networked timeline |
| Issue/RFI family | `Issue`, `IssueResponse`, `IssueSubmittal`, `CodeIssueType` |
| Change/parts family | `ChangeOrder`, `LinkIssuePart`, `LinkIssuePartOrder` |
| Calendar family | `HolidaySchedule`, `HolidayDate` |
| Small code tables | `CodeProblem`, `CodeResponsibleParty` |
| Internal FK edges | 11 |
| Inbound cross-module edges | 8 (from `portfolio-transactions` and `workflow`) |
| Outbound cross-module edges | 62 |
| Dashboard heading | Portfolio/Capital Program Administration |
| End-user screen | `Schedule`, rendered by `/en/reports/TaskGantt2.jsp` — a Gantt chart ([003](../../screens/003-main-navigation.md), [`screen-routing.md`](../../data-model/screen-routing.md)) |

## `Task`, `TaskGroup`, `TaskItem` — one shape, three names, one real target

All three objects carry the **identical 37-column field list** — `ActualDuration`,
`OriginalDuration`, `ProjectedDuration`, `PercentComplete`, `OnCriticalPath`, `IsTaskGroup`,
`ParentTaskID`, `Assignee_MemberID`, five `Tsk*` computed-conversion fields, and the rest.
Nothing in the field list distinguishes them structurally — same pattern the accounting module
found for its three schedule-type code tables
([`../accounting/README.md`](../accounting/README.md) finding 1). **The FK graph settles which one
is real:** every column anywhere in the schema typed `Task/Group ID` — 18 of them, across
`Issue.TaskIDList`, `LinkTaskByCodeMember.TaskID`, `LinkTaskMember.TaskID`,
`RETransaction.ActiveDealStepTaskIDList`/`DealSchedule`, `Scenario.ActiveDealStepTaskIDList`/
`DealSchedule`, `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID`, three objects'
`ParentTaskID`, three objects' `TskPredVal_PredecessorTaskID`, and `workflow`'s
`WorkFlow.KickOffTaskID`/`WFStepFullImport.TaskID`/`WorkFlowStep.TaskID` — resolves to **`TaskGroup`
and only `TaskGroup`.** `Task` and `TaskItem` have **zero** inbound edges anywhere in the 972-edge
graph. **Derived**, high confidence for the resolution pattern; the underlying cause (three
identically-shaped tables where only one is ever pointed at) is not explained by anything in this
corpus — most plausibly a UI-tier naming artefact (a task, a task group, and a task-list item
rendered from the same row via different JSPs) rather than three genuinely different record kinds.
**`PRJ-R-001`.**

`IsTaskGroup` (present on all three) is the field that would settle whether "Task" vs. "TaskGroup"
is a row-level flag rather than a table-level split — consistent with the FK-resolution finding: if
every schedule row physically lives in one table and `IsTaskGroup` distinguishes a summary row from
a leaf row, then `TaskGroup`, `Task`, and `TaskItem` may simply be the same physical table exported
three times under different names by the schema-dump tool. **Inferred** — no live query confirms
this, but it is the reading most consistent with the evidence. See [`scheduling.md`](scheduling.md)
§1.

## Two independent graphs over the same rows

`ParentTaskID` (a self-reference, present on all three task tables) builds a **hierarchy** — a
work-breakdown-structure tree, parent phase to child task. `TaskPredecessor`
(`PredecessorTaskID`/`SuccessorTaskID`, both `Task/Group ID`, plus lead/lag days and
`CodeTaskLeadLagTypeID`) builds a **separate dependency network** — the CPM predecessor graph a
Gantt chart needs to compute critical path and pushed dates. These are not the same structure: a
task's parent in the WBS tree is not necessarily its predecessor in the schedule network, and
nothing in the schema forces them to agree. `Task.OnCriticalPath` and `DaysAheadOfSchedule` are the
computed outputs of walking the predecessor graph. Full argument, including whether the predecessor
graph is provably acyclic, in [`scheduling.md`](scheduling.md).

## `ProcessTimeline` is a different, simpler thing from `Task`

`ProcessTimeline` (31 fields) shares most of `Task`'s date/duration vocabulary but **omits**
`ParentTaskID`, `TskPredVal_PredecessorTaskID`, `OnCriticalPath`, `IsTaskGroup`, and all three
resource-unit fields (`ActualResourceUnits` etc.) — no hierarchy, no dependency graph, no resource
tracking. It adds `RemainingDays` and a denormalised `ProcessTimelineTemplateName`. **This is a flat
milestone list, not a schedule network** — the mechanism behind `ProjectEntity`'s own
`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` columns
([`project-entity.md`](../../data-model/project-entity.md) §1.3), reused across both site-selection
phase tracking and construction phase tracking (per the Manage Data Fields catalog's own
description, `docs/data-fields/INDEX.md`). **`PRJ-R-002`.**

## The `Issue`/RFI family

This module's `Issue`-typed records are the **non-form** uses of the generic `Issue` table
([`code-table-registry.md`](../../data-model/code-table-registry.md) already established "a Form is
an Issue Type"): change-order threads (`ChangeOrder.IssueID`), part requests on a work order
(`LinkIssuePart`, `LinkIssuePartOrder`), and Q&A (`IssueResponse`, `IssueSubmittal`). `CodeIssueType`
(`TableType` 2035) carries the same eleven `IsValidFor*` entity-attachability flags found on
`VirtualTemplateSchedule` in this module and on the templates in every other module — one more
independent confirmation of the `ProjectEntity` subtype enumeration
([`project-entity.md`](../../data-model/project-entity.md) §1.4). **`PRJ-R-003`.**

`Issue` itself (56 raw schema fields) is drastically reduced in the Manage Data Fields admin catalog
(4 admin-exposed fields) — the same schema-vs-admin-catalog divergence
[`../facilities-locations/data-model.md`](../facilities-locations/data-model.md) documented for
`Prototype`. **`PRJ-R-004`.**

## The calendar

`HolidaySchedule` → `HolidayDate` is a firm-level named calendar; `Program.DefaultHolidayScheduleID`
(`portfolio-transactions`) sets the portfolio's default. `Task`/`TaskGroup`/`TaskItem`'s
`TaskEndsCodeDayOfWeekID` and `Program.DefaultWorkWeekends` are the other half of the working-day
calculation this calendar feeds. **`PRJ-R-005`.**

## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | Every object, field count, role, the 11-edge internal FK graph, and the cross-module inbound/outbound edges. |
| [`scheduling.md`](scheduling.md) | **The central technical question of this module** — the `Task`/`TaskGroup`/`TaskItem` identity, the hierarchy-vs-dependency-graph split, and whether the predecessor network is a DAG. |
| [`rules.md`](rules.md) | `PRJ-R-001`…`PRJ-R-014` — every rule in trigger/input/effect/confidence form. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What exists, what must be built, what should deliberately differ, and the open decisions blocking it. |

## What a rebuild must not get wrong

1. **`Task`, `TaskGroup`, and `TaskItem` are very likely one physical concept wearing three names**
   — do not build three separate aggregates. Build one `Task` aggregate with an `IsTaskGroup`-style
   discriminator (or confirm from a live query that they truly are three tables first). `PRJ-R-001`.
2. **A task's place in the WBS hierarchy and its place in the CPM dependency network are two
   different relationships** — do not collapse `ParentTaskID` and `TaskPredecessor` into one
   "depends on" concept. `PRJ-R-006` (see [`scheduling.md`](scheduling.md)).
3. **`ProcessTimeline` is not a lightweight `Task`** — it is deliberately simpler (no hierarchy, no
   dependency graph, no resource tracking) because it serves a different purpose: milestone-level
   phase tracking, not day-to-day schedule management. Do not merge the two models.
4. **Every FK typed `Task/Group ID`, across three separate modules, resolves to the same target.**
   This is the strongest evidence in the corpus that a "deal step" (`RETransaction`/`Scenario`), a
   workflow kickoff trigger (`WorkFlow.KickOffTaskID`), and a capital-project schedule row are the
   *same underlying record type*, wired together generically. Reuse that pattern rather than giving
   each caller its own task-like table.

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **Are `Task`, `TaskGroup`, and `TaskItem` genuinely three physical tables, or one table exported
   three times by the schema-dump tool?** The FK-resolution evidence strongly suggests the latter;
   nothing in this offline corpus can query the live database to confirm it. The single most
   valuable next step for this module.
2. **Is the `TaskPredecessor` graph provably acyclic?** Nothing in the schema enforces it; CPM
   scheduling assumes a DAG but the corpus cannot confirm the constraint is checked anywhere.
3. **What does the `Schedule` screen (`TaskGantt2.jsp`) actually render for a live Capital Project?**
   `projects` returns 0 rows in the live tenant
   ([`graphql-api.md`](../../data-model/graphql-api.md)), so no behavioural capture is possible
   without different tenant data.
4. **Are `LinkIssuePart`/`LinkIssuePartOrder` used for maintenance work orders, capital-project
   procurement, or both?** Both are plausible from the field names; no screen was opened.
5. **Does `CodeResponsibleParty` or `CodeProblem` actually attach to anything in this module**, or
   are they vestigial? Neither has any inbound or outbound FK in the 972-edge graph — though that
   may just mean their `Dropdown`-typed referencing columns are outside this corpus's edge-extraction
   method, not that they are unused. Not confirmed either way.
