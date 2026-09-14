# Projects & Construction

Out of scope - no approved BRD covers capital projects or construction. Kept in the corpus for graph completeness. The scheduling data is one of the strangest findings in the product - three byte-identical tables.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Project managers running a build-out against a schedule and a budget.

## Identical tables

*Observed · capability · source: `docs/modules/projects-capital/scheduling.md`*

Task, TaskGroup and TaskItem are byte-identical tables, and every foreign key of that shape in the entire schema resolves to TaskGroup alone. The work-breakdown hierarchy and the dependency network are two separate graphs drawn over the same rows.

## Issue / RFI loop

*Derived · capability · source: `docs/modules/projects-capital/README.md`*

Construction issues and RFIs run through the same request record that backs forms - the request machinery is shared across the product, not duplicated per module.

## Open questions (9)

*Inferred · group*

9 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Are Task TaskGroup and

*Inferred · question · source: `docs/modules/projects-capital/README.md`*

**Are Task, TaskGroup, and TaskItem genuinely three physical tables, or one table exported three times by the schema-dump tool?** The FK-resolution evidence strongly suggests the latter; nothing in this offline corpus can query the live database to confirm it. The single most valuable next step for this module. Nobody has confirmed this. Recorded in modules/projects-capital/README.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### Is the TaskPredecessor

*Inferred · question · source: `docs/modules/projects-capital/README.md`*

Is the TaskPredecessor graph provably acyclic? Nothing in the schema enforces it; CPM scheduling assumes a DAG but the corpus cannot confirm the constraint is checked anywhere. Nobody has confirmed this. Recorded in modules/projects-capital/README.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### What does the Schedule

*Inferred · question · source: `docs/modules/projects-capital/README.md`*

What does the Schedule screen (TaskGantt2.jsp) actually render for a live Capital Project? projects returns 0 rows in the live tenant (graphql-api.md), so no behavioural capture is possible without different tenant data. Nobody has confirmed this. Recorded in modules/projects-capital/README.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### Are LinkIssuePart

*Inferred · question · source: `docs/modules/projects-capital/README.md`*

**Are LinkIssuePart/LinkIssuePartOrder used for maintenance work orders, capital-project procurement, or both?** Both are plausible from the field names; no screen was opened. Nobody has confirmed this. Recorded in modules/projects-capital/README.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### Does

*Inferred · question · source: `docs/modules/projects-capital/README.md`*

Does CodeResponsibleParty or CodeProblem actually attach to anything in this module, or are they vestigial? Neither has any inbound or outbound FK in the 972-edge graph — though that may just mean their Dropdown-typed referencing columns are outside this corpus's edge-extraction method, not that they are unused. Not confirmed either way. Nobody has confirmed this. Recorded in modules/projects-capital/README.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### Are Task TaskGroup and

*Inferred · question · source: `docs/modules/projects-capital/scheduling.md`*

Are Task, TaskGroup, and TaskItem one physical table or three? Needs a live query; this corpus cannot settle it further. The single most valuable next capture for this module. Nobody has confirmed this. Recorded in modules/projects-capital/scheduling.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### Is the TaskPredecessor

*Inferred · question · source: `docs/modules/projects-capital/scheduling.md`*

Is the TaskPredecessor graph provably acyclic, and if so, where is that enforced — database constraint, application code, or not at all until the Gantt engine chokes on it?. Nobody has confirmed this. Recorded in modules/projects-capital/scheduling.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### What triggers

*Inferred · question · source: `docs/modules/projects-capital/scheduling.md`*

What triggers TskPredVal_* recomputation — is it recalculated on every read, or cached and updated only when a predecessor's dates change? The TskBAndA_NoAccessorConversion / TskNotDoneCompleted_NoAccessorConversion field names suggest some kind of legacy accessor-conversion shim, but their purpose is not otherwise documented anywhere in the corpus. Nobody has confirmed this. Recorded in modules/projects-capital/scheduling.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

### Does ProcessTimeline

*Inferred · question · source: `docs/modules/projects-capital/scheduling.md`*

Does ProcessTimeline ever reference a Task/TaskGroup row, or are the two systems (milestone list vs. schedule network) entirely parallel with no cross-reference at all? No FK connects them in the schema, which argues for "entirely parallel," but this was not independently verified against a live screen. Nobody has confirmed this. Recorded in modules/projects-capital/scheduling.md, under the Capital Projects & Scheduling area. Until it is settled, anything built on the assumption is a guess.

## Rules (14)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### PRJ-R-001 — [PRJ-R-001](../rules/PRJ-R-001.md)

*Derived · rule · source: `docs/modules/projects-capital/rules.md`*

**Any object needs to reference a schedule row · `Task/Group ID` FK type · Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transactions`, and `workflow` points at `TaskGroup`. `Task` and `TaskItem` are never targeted, despite….**

|  |  |
|---|---|
| Stated as | Any object needs to reference a schedule row |
| Stated as | `Task/Group ID` FK type |
| Stated as | Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transactions`, and `workflow` points at `TaskGroup`. `Task` and `TaskItem` are never targeted, despite sharing an identical 37-field shape. Read `TaskGroup` as the one real schedule-row table. |
| Stated as | Derived — see `scheduling.md` §1 |

### PRJ-R-002 — [PRJ-R-002](../rules/PRJ-R-002.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierarchy, no dependency graph, no resource tracking.….**

|  |  |
|---|---|
| Stated as | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) |
| Stated as | `ProcessTimeline` → `ProcessTimelineTemplate` |
| Stated as | Produces a flat, non-networked milestone list — no hierarchy, no dependency graph, no resource tracking. Deliberately simpler than `TaskGroup`. |
| Stated as | Observed (field-list diff) |

### PRJ-R-003 — [PRJ-R-003](../rules/PRJ-R-003.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**A tenant defines a new Form/Issue type · `CodeIssueType`, `TableType` 2035 · Carries the same 11 `IsValidFor*` entity-attachability flags as `VirtualTemplateSchedule` in this module and every template object in every other module. · Observed.**

|  |  |
|---|---|
| Stated as | A tenant defines a new Form/Issue type |
| Stated as | `CodeIssueType`, `TableType` 2035 |
| Stated as | Carries the same 11 `IsValidFor*` entity-attachability flags as `VirtualTemplateSchedule` in this module and every template object in every other module. |
| Stated as | Observed |

### PRJ-R-004 — [PRJ-R-004](../rules/PRJ-R-004.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**The Manage Data Fields admin screen renders `Issue`'s configurable surface · `Issue` (56 raw fields) vs. `docs/data-fields/all-fields.csv` (4 rows) · Only 4 of 56 fields are tenant-admin-configurable;.**

|  |  |
|---|---|
| Stated as | The Manage Data Fields admin screen renders `Issue`'s configurable surface |
| Stated as | `Issue` (56 raw fields) vs. `docs/data-fields/all-fields.csv` (4 rows) |
| Stated as | Only 4 of 56 fields are tenant-admin-configurable; the remaining 52 are schema-only. |
| Stated as | Observed |

### PRJ-R-005 — [PRJ-R-005](../rules/PRJ-R-005.md)

*Derived · rule · source: `docs/modules/projects-capital/rules.md`*

**A task's dates need working-day calculation · `HolidaySchedule` → `HolidayDate`, `Program.DefaultHolidayScheduleID` (`portfolio-transactions`), `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDayOfWeekID` · The portfolio's default calendar and weekend policy feed every task's duration math,….**

|  |  |
|---|---|
| Stated as | A task's dates need working-day calculation |
| Stated as | `HolidaySchedule` → `HolidayDate`, `Program.DefaultHolidayScheduleID` (`portfolio-transactions`), `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDayOfWeekID` |
| Stated as | The portfolio's default calendar and weekend policy feed every task's duration math, overridable per task via `TaskEndsCodeDayOfWeekID`. |
| Stated as | Derived |

### PRJ-R-006 — [PRJ-R-006](../rules/PRJ-R-006.md)

*Derived · rule · source: `docs/modules/projects-capital/rules.md`*

**A `TaskGroup` row's schedule position is computed · `ParentTaskID` (hierarchy) vs. `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID` (dependency network) · Two independent graphs.**

|  |  |
|---|---|
| Stated as | A `TaskGroup` row's schedule position is computed |
| Stated as | `ParentTaskID` (hierarchy) vs. `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID` (dependency network) |
| Stated as | Two independent graphs. A task's WBS parent is not required to be, and generally is not, the same row as its schedule predecessor. |
| Stated as | Derived — see `scheduling.md` §2 |

### PRJ-R-007 — [PRJ-R-007](../rules/PRJ-R-007.md)

*Inferred · rule · source: `docs/modules/projects-capital/rules.md`*

**The Gantt engine (`TaskGantt2.jsp`) needs a task's critical-path status · `TaskGroup.OnCriticalPath`, `DaysAheadOfSchedule` · Plausibly computed by walking the `TaskPredecessor` graph; no formula or screen confirms the exact computation.**

|  |  |
|---|---|
| Stated as | The Gantt engine (`TaskGantt2.jsp`) needs a task's critical-path status |
| Stated as | `TaskGroup.OnCriticalPath`, `DaysAheadOfSchedule` |
| Stated as | Plausibly computed by walking the `TaskPredecessor` graph; no formula or screen confirms the exact computation. |
| Stated as | Inferred |

### PRJ-R-008 — [PRJ-R-008](../rules/PRJ-R-008.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**A change is made against an active capital project's cost · `ChangeOrder.ApprovedChangeOrderAmount`, `OutstandingChangeOrderAmount`, `CostTrackingVariance`, `PurchaseOrderID` · Tracks approved vs. outstanding change amounts against a `PurchaseOrder` (out of scope by decision — cited, not analysed).**

|  |  |
|---|---|
| Stated as | A change is made against an active capital project's cost |
| Stated as | `ChangeOrder.ApprovedChangeOrderAmount`, `OutstandingChangeOrderAmount`, `CostTrackingVariance`, `PurchaseOrderID` |
| Stated as | Tracks approved vs. outstanding change amounts against a `PurchaseOrder` (out of scope by decision — cited, not analysed). |
| Stated as | Observed |

### PRJ-R-009 — [PRJ-R-009](../rules/PRJ-R-009.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**A part is consumed or ordered against a work-order `Issue` · `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) · Two distinct records — one for parts actually used, one for parts on order — both attached to the same….**

|  |  |
|---|---|
| Stated as | A part is consumed or ordered against a work-order `Issue` |
| Stated as | `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) |
| Stated as | Two distinct records — one for parts actually used, one for parts on order — both attached to the same `Issue` via `IssueID`. |
| Stated as | Observed |

### PRJ-R-010 — [PRJ-R-010](../rules/PRJ-R-010.md)

*Derived · rule · source: `docs/modules/projects-capital/rules.md`*

**A task needs an assignee, but not a named individual · `LinkTaskByCodeMember.CodeJobTitleID`, `OrgChartLevel` · Assigns by job title / org-chart level rather than by `Member`, matching the `AssigneeType` = `JOB_TITLE` routing option (`graphql-api.md`). · Derived.**

|  |  |
|---|---|
| Stated as | A task needs an assignee, but not a named individual |
| Stated as | `LinkTaskByCodeMember.CodeJobTitleID`, `OrgChartLevel` |
| Stated as | Assigns by job title / org-chart level rather than by `Member`, matching the `AssigneeType` = `JOB_TITLE` routing option (`graphql-api.md`). |
| Stated as | Derived |

### PRJ-R-011 — [PRJ-R-011](../rules/PRJ-R-011.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**A task needs a named assignee · `LinkTaskMember.MemberID` · Assigns a specific `Member`, alongside `TaskGroup.Assignee_MemberID`'s own direct field — two mechanisms for the same concept exist side by side. · Observed.**

|  |  |
|---|---|
| Stated as | A task needs a named assignee |
| Stated as | `LinkTaskMember.MemberID` |
| Stated as | Assigns a specific `Member`, alongside `TaskGroup.Assignee_MemberID`'s own direct field — two mechanisms for the same concept exist side by side. |
| Stated as | Observed |

### PRJ-R-012 — [PRJ-R-012](../rules/PRJ-R-012.md)

*Derived · rule · source: `docs/modules/projects-capital/rules.md`*

**A workflow needs to be triggered by a schedule event · `WorkFlow.KickOffTaskID` → `TaskGroup` · Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state can kick off a workflow. · Derived.**

|  |  |
|---|---|
| Stated as | A workflow needs to be triggered by a schedule event |
| Stated as | `WorkFlow.KickOffTaskID` → `TaskGroup` |
| Stated as | Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state can kick off a workflow. |
| Stated as | Derived |

### PRJ-R-013 — [PRJ-R-013](../rules/PRJ-R-013.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**A real-estate deal step needs its own schedule · `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) · Both reuse `TaskGroup` directly — the deal pipeline has no schedule engine of its own. · Observed.**

|  |  |
|---|---|
| Stated as | A real-estate deal step needs its own schedule |
| Stated as | `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) |
| Stated as | Both reuse `TaskGroup` directly — the deal pipeline has no schedule engine of its own. |
| Stated as | Observed |

### PRJ-R-014 — [PRJ-R-014](../rules/PRJ-R-014.md)

*Observed · rule · source: `docs/modules/projects-capital/rules.md`*

**`CodeProblem` or `CodeResponsibleParty` values are needed · (no confirmed attachment point) · Neither table shows an inbound or outbound edge in the 972-edge graph. May be referenced only via `Dropdown`-typed columns this corpus's edge-extraction does not model as graph edges — not confirmed either….**

|  |  |
|---|---|
| Stated as | `CodeProblem` or `CodeResponsibleParty` values are needed |
| Stated as | (no confirmed attachment point) |
| Stated as | Neither table shows an inbound or outbound edge in the 972-edge graph. May be referenced only via `Dropdown`-typed columns this corpus's edge-extraction does not model as graph edges — not confirmed either way. |
| Stated as | Observed (absence); cause not determined |
