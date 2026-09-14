# Capital Projects & Scheduling

*In scope for the rebuild*

Project delivery: task/schedule networks with predecessors and holiday calendars, process timelines, change orders, and the issue/RFI loop.

Stated up front. This module is the product's generic scheduling and issue-tracking engine, reused across capital project delivery, real-estate deal steps, and workflow triggers. 23 objects, 376 fields. Its central technical finding mirrors the accounting module's: Task, TaskGroup, and TaskItem are three byte-identical 37-field tables, and every single FK of the ambiguous type Task/Group ID anywhere in the 223-object schema — across this module, portfolio-transactions, and workflow — resolves to TaskGroup alone. Task and TaskItem receive zero inbound foreign keys anywhere in the product. Second: Task.ParentTaskID (a hierarchy) and TaskPredecessor (a dependency network) are two independent graph structures over the same row set — a WBS tree and a CPM predecessor network, not one thing. Third: the module owns the generic Issue record — already established from the routing layer (code-table-registry.md, screen-routing.md) as the record behind every "Form" — and this module is where its non-form use (RFIs, change-order threads, bidder Q&A) lives.

|  | Count |
|---|---|
| Record types | 23 |
| Fields | 376 |
| Keys in | 8 |
| Keys out | 62 |
| Rules | 14 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Issue](../entities/Issue.md) | `issue` | 56 | 0 |
| [Task](../entities/Task.md) | `task` | 37 | 0 |
| [TaskGroup](../entities/TaskGroup.md) | `task_group` | 37 | 18 |
| [TaskItem](../entities/TaskItem.md) | `task_item` | 37 | 0 |
| [ProcessTimeline](../entities/ProcessTimeline.md) | `process_timeline` | 31 | 0 |
| [CodeIssueType](../entities/CodeIssueType.md) | `code_issue_type` | 19 | 0 |
| [TaskTemplateAudit](../entities/TaskTemplateAudit.md) | `task_template_audit` | 18 | 0 |
| [ChangeOrder](../entities/ChangeOrder.md) | `change_order` | 16 | 0 |
| [LinkIssuePartOrder](../entities/LinkIssuePartOrder.md) | `link_issue_part_order` | 16 | 0 |
| [VirtualTemplateSchedule](../entities/VirtualTemplateSchedule.md) | `virtual_template_schedule` | 16 | 0 |
| [TaskPredecessor](../entities/TaskPredecessor.md) | `task_predecessor` | 15 | 0 |
| [LinkIssuePart](../entities/LinkIssuePart.md) | `link_issue_part` | 13 | 0 |
| [HolidayDate](../entities/HolidayDate.md) | `holiday_date` | 12 | 0 |
| [IssueResponse](../entities/IssueResponse.md) | `issue_response` | 11 | 0 |
| [ProcessTimelineTemplate](../entities/ProcessTimelineTemplate.md) | `process_timeline_template` | 10 | 0 |
| [HolidaySchedule](../entities/HolidaySchedule.md) | `holiday_schedule` | 8 | 0 |
| [LinkTaskByCodeMember](../entities/LinkTaskByCodeMember.md) | `link_task_by_code_member` | 8 | 0 |
| [LinkTaskMember](../entities/LinkTaskMember.md) | `link_task_member` | 5 | 0 |
| [CodeProblem](../entities/CodeProblem.md) | `code_problem` | 4 | 0 |
| [CodeResponsibleParty](../entities/CodeResponsibleParty.md) | `code_responsible_party` | 4 | 0 |
| [IssueSubmittal](../entities/IssueSubmittal.md) | `issue_submittal` | 1 | 0 |
| [LinkTaskDocument](../entities/LinkTaskDocument.md) | `link_task_document` | 1 | 0 |
| [TaskTemplate](../entities/TaskTemplate.md) | `task_template` | 1 | 1 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [PRJ-R-001](../rules/PRJ-R-001.md) |  | Any object needs to reference a schedule row · `Task/Group ID` FK type · Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transa | Derived |
| [PRJ-R-002](../rules/PRJ-R-002.md) |  | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat,  | Observed |
| [PRJ-R-003](../rules/PRJ-R-003.md) |  | A tenant defines a new Form/Issue type · `CodeIssueType`, `TableType` 2035 · Carries the same 11 `IsValidFor*` entity-attachability flags as `VirtualTemplateSchedule` in this module and every template | Observed |
| [PRJ-R-004](../rules/PRJ-R-004.md) |  | The Manage Data Fields admin screen renders `Issue`'s configurable surface · `Issue` (56 raw fields) vs. `docs/data-fields/all-fields.csv` (4 rows) · Only 4 of 56 fields are tenant-admin-configurable; | Observed |
| [PRJ-R-005](../rules/PRJ-R-005.md) |  | A task's dates need working-day calculation · `HolidaySchedule` → `HolidayDate`, `Program.DefaultHolidayScheduleID` (`portfolio-transactions`), `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDa | Derived |
| [PRJ-R-006](../rules/PRJ-R-006.md) |  | A `TaskGroup` row's schedule position is computed · `ParentTaskID` (hierarchy) vs. `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID` (dependency network) · Two independent graphs. | Derived |
| [PRJ-R-007](../rules/PRJ-R-007.md) |  | The Gantt engine (`TaskGantt2.jsp`) needs a task's critical-path status · `TaskGroup.OnCriticalPath`, `DaysAheadOfSchedule` · Plausibly computed by walking the `TaskPredecessor` graph; no formula or s | Inferred |
| [PRJ-R-008](../rules/PRJ-R-008.md) |  | A change is made against an active capital project's cost · `ChangeOrder.ApprovedChangeOrderAmount`, `OutstandingChangeOrderAmount`, `CostTrackingVariance`, `PurchaseOrderID` · Tracks approved vs. out | Observed |
| [PRJ-R-009](../rules/PRJ-R-009.md) |  | A part is consumed or ordered against a work-order `Issue` · `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) · Two dist | Observed |
| [PRJ-R-010](../rules/PRJ-R-010.md) |  | A task needs an assignee, but not a named individual · `LinkTaskByCodeMember.CodeJobTitleID`, `OrgChartLevel` · Assigns by job title / org-chart level rather than by `Member`, matching the `AssigneeTy | Derived |
| [PRJ-R-011](../rules/PRJ-R-011.md) |  | A task needs a named assignee · `LinkTaskMember.MemberID` · Assigns a specific `Member`, alongside `TaskGroup.Assignee_MemberID`'s own direct field — two mechanisms for the same concept exist side by  | Observed |
| [PRJ-R-012](../rules/PRJ-R-012.md) |  | A workflow needs to be triggered by a schedule event · `WorkFlow.KickOffTaskID` → `TaskGroup` · Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state | Derived |
| [PRJ-R-013](../rules/PRJ-R-013.md) |  | A real-estate deal step needs its own schedule · `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) · Both reuse `Ta | Observed |
| [PRJ-R-014](../rules/PRJ-R-014.md) |  | `CodeProblem` or `CodeResponsibleParty` values are needed · (no confirmed attachment point) · Neither table shows an inbound or outbound edge in the 972-edge graph. May be referenced only via `Dropdow | Observed |
