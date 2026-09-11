# Capital Projects & Scheduling — data model

**Stated up front.** 23 objects, 376 fields. The module's own internal graph is small (11 edges) —
most of its outbound reach (62 edges) goes to `people-parties` (`Member`, `Employer`,
`EmployerSite` — assignees, vendors, contacts) and `platform-tenancy` (`ProjectEntity`,
`EntityTemplate`). Its inbound edges (8) come only from `portfolio-transactions` and `workflow`,
both consuming `TaskGroup` — see [`scheduling.md`](scheduling.md).

## 1. Every object

| Object | PG table | Fields | Role | One-line |
|---|---|---:|---|---|
| `Issue` | `issue` | 56 | `entity_scoped` | The generic unit-of-work record; 4 fields admin-exposed of 56 raw — see §4. |
| `Task` | `task` | 37 | `entity_scoped` | Schedule row. Byte-identical to `TaskGroup`/`TaskItem`; zero inbound FKs. |
| `TaskGroup` | `task_group` | 37 | `entity_scoped` | Schedule row. **The only one of the three ever targeted by an FK** — 18 inbound edges. |
| `TaskItem` | `task_item` | 37 | `entity_scoped` | Schedule row. Byte-identical to `Task`/`TaskGroup`; zero inbound FKs. |
| `ProcessTimeline` | `process_timeline` | 31 | `entity_scoped` | A flat milestone/phase timeline — no hierarchy, no dependency graph. |
| `TaskPredecessor` | `task_predecessor` | 15 | `entity_scoped` | The CPM dependency-network join between two `TaskGroup` rows. |
| `TaskTemplateAudit` | `task_template_audit` | 18 | `entity_scoped` | Records which template bundle (task/budget/folder) was applied and when. |
| `ChangeOrder` | `change_order` | 16 | `entity_scoped` | A cost change against an active capital project; links to `PurchaseOrder` (out of scope). |
| `LinkIssuePartOrder` | `link_issue_part_order` | 16 | `entity_scoped` | A parts order raised from an `Issue` (work order). |
| `CodeIssueType` | `code_issue_type` | 19 | `firm_global` (code table) | `TableType` 2035 — carries the same 11 `IsValidFor*` flags as every other template. |
| `LinkIssuePart` | `link_issue_part` | 13 | `entity_scoped` | A part consumed against an `Issue`, with cost/labor fields. |
| `HolidayDate` | `holiday_date` | 12 | `entity_scoped` | One calendar date within a `HolidaySchedule`. |
| `ProcessTimelineTemplate` | `process_timeline_template` | 10 | `firm_global` | Reusable milestone template — default task name, phase-status labels. |
| `IssueResponse` | `issue_response` | 11 | `entity_scoped` | A reply on an `Issue` (bidder Q&A, RFI response). |
| `LinkTaskByCodeMember` | `link_task_by_code_member` | 8 | `entity_scoped` | Assigns a task to a job-title/org-chart level rather than a named member. |
| `HolidaySchedule` | `holiday_schedule` | 8 | `firm_global` | Named calendar header over `HolidayDate`. |
| `CodeProblem` | `code_problem` | 4 | `firm_global` | Plain lookup — short/long name, remedy note. No observed inbound or outbound edge. |
| `CodeResponsibleParty` | `code_responsible_party` | 4 | `firm_global` | Plain lookup, links to a `Responsible Party System Code`. No observed inbound or outbound edge. |
| `LinkTaskMember` | `link_task_member` | 5 | `entity_scoped` | Assigns a named `Member` to a `TaskGroup`. |
| `VirtualTemplateSchedule` | `virtual_template_schedule` | 16 | `firm_global` (virtual/projection) | Read-only projection of schedule-template metadata + the 11 `IsValidFor*` flags. |
| `IssueSubmittal` | `issue_submittal` | 1 | `entity_scoped` | 1-field stub in this export — likely a join/submittal marker on an `Issue`. |
| `LinkTaskDocument` | `link_task_document` | 1 | `entity_scoped` | 1-field stub — attaches a document to a task. |
| `TaskTemplate` | `task_template` | 1 | `entity_scoped` | 1-field stub — the template a `TaskTemplateAudit` was applied from. |

Three objects (`IssueSubmittal`, `LinkTaskDocument`, `TaskTemplate`) show only 1 field
(`ProjectEntityID`) in the raw export — genuinely that sparse, or the export tool's column
enumeration under-captured them. Flagged, not resolved, in [`README.md`](README.md#open-questions).

## 2. `Task` / `TaskGroup` / `TaskItem` — the shared 37-field shape

See [`scheduling.md`](scheduling.md) §1 for the full field list and the FK-resolution evidence.
Summary: identical fields, `TaskGroup` is the sole resolution target of the `Task/Group ID` FK type
everywhere in the schema (18 occurrences, 3 modules), `Task` and `TaskItem` have zero inbound edges.

## 3. Internal FK edges (11)

| Source | Column | Target | Notes |
|---|---|---|---|
| `Task` / `TaskGroup` / `TaskItem` | `ParentTaskID` | `TaskGroup` | WBS hierarchy self-reference (all three physically resolve to `TaskGroup`). |
| `Task` / `TaskGroup` / `TaskItem` | `TskPredVal_PredecessorTaskID` | `TaskGroup` | Denormalised predecessor pointer, duplicating `TaskPredecessor`'s own edge. |
| `TaskPredecessor` | `PredecessorTaskID` | `TaskGroup` | The dependency-network join, source side. |
| `TaskPredecessor` | `SuccessorTaskID` | `TaskGroup` | The dependency-network join, target side. |
| `Issue` | `TaskIDList` | `TaskGroup` | An Issue can list the tasks it relates to. |
| `LinkTaskByCodeMember` | `TaskID` | `TaskGroup` | Job-title-based task assignment. |
| `LinkTaskMember` | `TaskID` | `TaskGroup` | Named-member task assignment. |

## 4. Cross-module edges

### 4.1 Outbound (62 columns, this module → elsewhere)

| Target module | Columns | What's referenced |
|---|---:|---|
| `people-parties` | 35 | `Member` (assignees, audit stamps — the large majority), `Employer`, `EmployerSite` |
| `platform-tenancy` | 21 | `ProjectEntity`, `EntityTemplate` (three separate template-type FKs on `TaskTemplateAudit` alone) |
| `assets-equipment` | 3 | `Asset` (`Issue.EquipmentID`/`EquipmentIDList` — work-order equipment) |
| `out-of-scope-cost-budget` | 2 | `BudgetColumnType` (`Issue.Budget`/`BudgetColumnTypeID`) |
| `accounting` | 1 | `PurchaseOrder` (`ChangeOrder.PurchaseOrderID`) — out of scope by decision; cited, not analysed |

### 4.2 Inbound (8 columns, elsewhere → this module)

| Source module | Source.Column | Target |
|---|---|---|
| `portfolio-transactions` | `RETransaction.ActiveDealStepTaskIDList`, `.DealSchedule`, `Scenario.ActiveDealStepTaskIDList`, `.DealSchedule` | `TaskGroup` |
| `portfolio-transactions` | `DevelopmentSlot.TaskTemplatePEID` | `TaskTemplate` |
| `workflow` | `WorkFlow.KickOffTaskID`, `WFStepFullImport.TaskID`, `WorkFlowStep.TaskID` | `TaskGroup` |

**Every inbound edge into this module targets `TaskGroup` or `TaskTemplate` — never `Task`,
`TaskItem`, `Issue`, or anything else.** This is the same pattern noted in
[`scheduling.md`](scheduling.md): the rest of the product treats `TaskGroup` as the one real
schedule-row table, and this module's generic scheduling engine is reused, unmodified, by both the
real-estate deal pipeline (`portfolio-transactions`) and workflow kickoff triggers (`workflow`).

## 5. `Issue`'s 56 fields vs. its 4 admin-exposed fields

`Issue` carries `AssignedToMemberIDs`, `ManagerMemberIDs`, `AttentionEmailTo`, `CodeChangeReasonID`,
`CodeDisciplineID`, `CodeLastActionStatusID`, `CodeMethodOfContactID`, `CodeOrderStatusID`,
`EquipmentID`/`EquipmentIDList`, `PartNumberIDList`, `VendorID`, `WorkFlowAdhocMemberID`, and more —
a genuinely rich record. The Manage Data Fields admin catalog exposes only 4 of its 56 raw fields
(`docs/data-fields/all-fields.csv`). **Observed**, same divergence pattern as `Prototype`
([`../facilities-locations/data-model.md`](../facilities-locations/data-model.md)) and
`PotentialProject`/`Project` (this module's sibling,
[`../portfolio-transactions/site-pipeline.md`](../portfolio-transactions/site-pipeline.md)) — a
recurring signal that the schema export and the tenant-admin-configurable surface are two
genuinely different views of the product, not one.

## Open questions

See [`README.md`](README.md#open-questions) and [`scheduling.md`](scheduling.md#open-questions).
