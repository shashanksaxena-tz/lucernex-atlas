# Scheduling — `Task`, `TaskGroup`, `TaskItem`, and the two graphs over them

**Stated up front.** The schema hands us one 37-column shape repeated across three object names,
and one FK-resolution pattern that points at exactly one of the three every time. **Best reading:
`Task`, `TaskGroup`, and `TaskItem` are the same underlying schedule row, exported three times by
the schema-dump tool** — most plausibly because the live application renders the same physical table
through three different JSPs/contexts (a single task, a task acting as a group header, and a task
row inside a list view) and the export tool's object-discovery step picked up each rendering as if
it were a distinct table. **This cannot be confirmed from the offline corpus** — it would take a
live query (`SELECT DISTINCT` against whatever the three PG tables actually resolve to, or a
`walkHierarchy.jsp` capture) to settle. Separately, and independently confirmed: **the WBS hierarchy
and the CPM dependency network are two different graphs over the same rows**, and whether the
dependency graph is acyclic is not something this schema enforces or this corpus can check.

## 1. The `Task`/`TaskGroup`/`TaskItem` identity question

### 1.1 The field lists are byte-identical

All three raw schema rows carry exactly the same 37 fields, in the same order, with the same types:

```
ActualDuration(Number) | ActualEndDate(Date) | ActualResourceUnits(Number) |
ActualStartDate(Date) | Assignee_MemberID(Member ID) | CodeTaskStatusID(Dropdown (Task Status Code)) |
DaysAheadOfSchedule(Number) | Description(Text) | EMailMessage(Text) | EnableForDashboard(Boolean) |
EnableForEMail(Boolean) | IsTaskGroup(Boolean) | ModifiedByID(Member ID) | ModifiedDate(Time) |
OnCriticalPath(Boolean) | OriginalDuration(Number) | OriginalEndDate(Date) |
OriginalResourceUnits(Number) | OriginalStartDate(Date) | ParentTaskID(Task/Group ID) |
PercentComplete(Number) | ProjectEntityID(Entity ID) | ProjectedDuration(Number) |
ProjectedEndDate(Date) | ProjectedResourceUnits(Number) | ProjectedStartDate(Date) |
TaskEndsCodeDayOfWeekID(Dropdown (Day Of Week Code)) | TaskID(Number) | TaskName(Text) |
TskBAndA_NoAccessorConversion(Text) | TskDone_ActualEndDate(Date) |
TskNotDoneCompleted_NoAccessorConversion(Text) | TskNotDone_ActualEndDate(Date) |
TskPredVal_ActualLeadLagDays(Number) | TskPredVal_OriginalLeadLagDays(Number) |
TskPredVal_PredecessorTaskID(Task/Group ID) | TskPredVal_ProjectedLeadLagDays(Number)
```

*(`_lucernex_objects_summary.txt` — **Observed**, byte-for-byte identical across `task`,
`task_group`, `task_item`.)*

`IsTaskGroup` is present on all three — a boolean that exists specifically to say "this row is
acting as a group header," which only makes sense as a **row-level discriminator inside one table**,
not as a column that would need to exist on a table that is *already* named `TaskGroup`.

### 1.2 Every FK of this shape's type resolves to `TaskGroup`, never to `Task` or `TaskItem`

The declared FK type `Task/Group ID` appears 18 times across the schema. Every single one resolves,
in `docs/mindmap/edges.json`, to `TaskGroup`:

| Source.Column | Source module |
|---|---|
| `Issue.TaskIDList` | `projects-capital` |
| `LinkTaskByCodeMember.TaskID` | `projects-capital` |
| `LinkTaskMember.TaskID` | `projects-capital` |
| `Task.ParentTaskID`, `TaskGroup.ParentTaskID`, `TaskItem.ParentTaskID` | `projects-capital` |
| `Task.TskPredVal_PredecessorTaskID`, `TaskGroup.…`, `TaskItem.…` | `projects-capital` |
| `TaskPredecessor.PredecessorTaskID`, `.SuccessorTaskID` | `projects-capital` |
| `RETransaction.ActiveDealStepTaskIDList`, `.DealSchedule` | `portfolio-transactions` |
| `Scenario.ActiveDealStepTaskIDList`, `.DealSchedule` | `portfolio-transactions` |
| `WorkFlow.KickOffTaskID`, `WFStepFullImport.TaskID`, `WorkFlowStep.TaskID` | `workflow` |

`Task` and `TaskItem` have **zero** inbound edges anywhere in the 972-edge graph. **Observed.** If
`Task` and `TaskItem` were genuinely separate, independently-populated tables, it would be very odd
for *nothing in the entire product* — not a deal step, not a workflow trigger, not even the other
two tables' own self-references — to ever point at them specifically. The simplest explanation
consistent with every observation is that there is one physical row type, and the graph-resolution
script (like a human reading the schema) picked `TaskGroup` as the canonical name because it is
alphabetically/contextually the one FK types most often name. **Derived**, and this is the module's
single most useful finding for a rebuild: **do not build three aggregates.**

### 1.3 What would settle it, and why this corpus cannot

A live read of the actual PostgreSQL tables behind `task`, `task_group`, `task_item` — row counts,
whether the same primary-key values appear in more than one, or whether two of the three are in
fact views over the third — would resolve this immediately. Nothing in the offline `_lucernex_objects_summary.txt`
dump distinguishes a real table from a view; the export tool that produced it treats both
identically. **Open question, ranked #1 in [`README.md`](README.md#open-questions).**

## 2. Two independent graphs over the schedule rows

### 2.1 The hierarchy: `ParentTaskID`

`ParentTaskID` is a self-reference on all three task tables — a work-breakdown-structure tree. A
"group" row (`IsTaskGroup = true`) is a phase; its children are the tasks or sub-phases under it.
This is a **tree**: every row has at most one parent.

### 2.2 The dependency network: `TaskPredecessor`

`TaskPredecessor` (15 fields) is a **separate object**, not a self-reference on the task tables
themselves: `PredecessorTaskID` and `SuccessorTaskID` (both `Task/Group ID`), plus
`ActualLeadLagDays`/`OriginalLeadLagDays`/`ProjectedLeadLagDays` and
`CodeTaskLeadLagTypeID` (`Task Lead Lag Type Code` — the FS/SS/FF/SF relationship type a CPM engine
needs). This is a **graph, not a tree**: a task can have multiple predecessors and multiple
successors, which is exactly why it needs its own join table rather than reusing `ParentTaskID`.
`Task.OnCriticalPath` and `Task.DaysAheadOfSchedule` are the plausible computed outputs of walking
this graph — the schedule engine's critical-path calculation surfacing back onto the row.
**Observed** structure; **Inferred** that these two computed fields are specifically the predecessor
graph's output (no formula or screen confirms it).

### 2.3 The two graphs are not required to agree

Nothing in the schema forces a task's `ParentTaskID` (its WBS parent) to also be a predecessor or
successor relationship in `TaskPredecessor`. A sub-task's schedule dependency may well be on a task
in a *different* branch of the WBS tree — the ordinary case in any real construction schedule (e.g.,
"pour foundation" predecessor-gates "frame walls" even though the two sit under different phase
headers). **Derived**, from the general shape of CPM scheduling and confirmed structurally by the
two relationships living in genuinely separate columns/tables rather than one.

### 2.4 Is the predecessor graph a DAG?

**Not confirmed, and not determinable from this corpus.** A CPM schedule *requires* the predecessor
graph to be acyclic for critical-path computation to terminate, but nothing in the schema — no
constraint, trigger, or captured validation message — shows the platform enforcing that. This is
almost certainly enforced in application code (the Gantt engine behind `TaskGantt2.jsp`,
[`screen-routing.md`](../../data-model/screen-routing.md)) rather than the database, which is
consistent with `TskPredVal_*` fields being pre-computed convenience columns rather than raw
graph edges recomputed on every read. **Open question, ranked #2.**

## 3. `ProcessTimeline` deliberately does not have either graph

`ProcessTimeline` (31 fields) shares `Task`'s date/duration/status vocabulary but has **no**
`ParentTaskID`, no corresponding predecessor table, no `IsTaskGroup`, and no resource-unit tracking.
It is a flat list of milestones — `RemainingDays` is its one genuinely distinct field, and its
`ProcessTimelineTemplateName` links back to a reusable `ProcessTimelineTemplate` (10 fields:
`DefaultTaskName`, phase-status labels, `CodeProjectPhaseID`). Per the Manage Data Fields catalog
(`docs/data-fields/INDEX.md`), `ProcessTimeline` spans both the site-selection and construction
phases — it is the mechanism behind `ProjectEntity.CurrentMilestone`/`NextMilestone`/
`PreviousMilestone` for *any* entity type, not a construction-specific schedule.

## 4. Confidence summary

| Claim | Label |
|---|---|
| `Task`, `TaskGroup`, `TaskItem` share an identical 37-field shape | **Observed** |
| All 18 `Task/Group ID`-typed FKs in the schema resolve to `TaskGroup`; `Task`/`TaskItem` have zero inbound edges | **Observed** |
| The three are one physical concept exported three times | **Derived** — the most economical explanation of the two facts above; not independently confirmed |
| `ParentTaskID` (hierarchy) and `TaskPredecessor` (dependency network) are two distinct graph structures | **Observed** (separate columns/tables) |
| The two graphs are not required to agree with each other | **Derived** |
| `Task.OnCriticalPath`/`DaysAheadOfSchedule` are computed from the predecessor graph | **Inferred** |
| The predecessor graph is acyclic | **Not determined** |
| `ProcessTimeline` is a deliberately simpler, non-networked milestone list | **Observed** (field-list diff) |

## Open questions

1. **Are `Task`, `TaskGroup`, and `TaskItem` one physical table or three?** Needs a live query;
   this corpus cannot settle it further. The single most valuable next capture for this module.
2. **Is the `TaskPredecessor` graph provably acyclic**, and if so, where is that enforced — database
   constraint, application code, or not at all until the Gantt engine chokes on it?
3. **What triggers `TskPredVal_*` recomputation** — is it recalculated on every read, or cached and
   updated only when a predecessor's dates change? The `TskBAndA_NoAccessorConversion` /
   `TskNotDoneCompleted_NoAccessorConversion` field names suggest some kind of legacy
   accessor-conversion shim, but their purpose is not otherwise documented anywhere in the corpus.
4. **Does `ProcessTimeline` ever reference a `Task`/`TaskGroup` row**, or are the two systems
   (milestone list vs. schedule network) entirely parallel with no cross-reference at all? No FK
   connects them in the schema, which argues for "entirely parallel," but this was not independently
   verified against a live screen.

## The working calendar — holidays and "crashing"

**Observed**, from the `Manage Holiday Calendar` screen's own on-screen help
(`/en/admin/ManageHolidayCalendar.jsp`,
`bbw-admin/32-manage-holiday-calendar.jpg`):

> *"Holiday days are used when determining task completion dates. If a schedule is not 'crashed' then
> weekends and holidays will not be used when determining task dates from lead/lag or duration
> values."*

**Derived.** The scheduling engine resolves a task's dates against a **working calendar**, and a
schedule carries a flag — "crashed" — that switches that off so durations run through weekends and
holidays. So `TaskPredecessor` lead/lag and task durations are in **working days by default, calendar
days when crashed**.

**Observed.** A holiday calendar is a named record scoped to `Portfolios / Programs` — columns
`Calendar Name` and `Portfolios / Programs`. **`(ASG)BBW` holds none**, so no working calendar is
configured in that tenant.

**Derived.** This is the only place in the product where holidays are used, and it is a *scheduling*
concern rather than an accounting one — the lease-accounting engine's periods come from the fiscal
calendar instead ([`../../features/reference-data/`](../../features/reference-data/)). Capital
projects are **out of scope** for ASG Edge+, so this behaviour is out of scope with them.

**Open.** Where the "crashed" flag lives is unobserved — it is not among the fields surfaced on
`Task`, `TaskGroup` or `TaskItem` in this corpus.
