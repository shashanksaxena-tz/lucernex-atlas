# WFStepFullImport

*47 fields · module: Workflow & Approvals · Postgres: `w_f_step_full_import`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 47 declared fields, filed under Workflow & Approvals, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 11 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApproverMemberIDList` |  | Member ID | — |  | [Member](Member.md) |
| `AssigneeMemberIDList` |  | Member ID | — |  | [Member](Member.md) |
| `CurrentStepMemberIDList` |  | Member ID | — |  | [Member](Member.md) |
| `NotifieeMemberIDList` |  | Member ID | — |  | [Member](Member.md) |
| `PageLayoutApproversID` |  | item ID | — |  | unresolved |
| `PageLayoutAssigneesID` |  | item ID | — |  | unresolved |
| `PriorSubmitByMemberID` |  | Member ID | — |  | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `SubmitForApprovalByMemberID` |  | Member ID | — |  | [Member](Member.md) |
| `TaskID` |  | Task/Group ID | — |  | [TaskGroup](TaskGroup.md) |
| `WorkFlowID` |  | Work Flow ID | — |  | [WorkFlow](WorkFlow.md) |
| `WorkFlowTemplateStepID` |  | Step ID | — |  | [WorkFlowStep](WorkFlowStep.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeWorkFlowStatusID` |  | Dropdown (Work Flow Status Code) | — |  | Work Flow Status Code |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DaysUntilAlertApprovers` |  | Number | — |  |  |
| `DaysUntilAlertAssignees` |  | Number | — |  |  |
| `DaysUntilWarnApprovers` |  | Number | — |  |  |
| `DaysUntilWarnAssignees` |  | Number | — |  |  |
| `DurationDaysApprovers` |  | Number | — |  |  |
| `DurationDaysAssignees` |  | Number | — |  |  |
| `Priority` |  | Number | — |  |  |
| `StepNumber` |  | Number | — |  |  |
| `WorkFlowStepID` |  | Number | — |  |  |

### Dates & timestamps (7)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CompleteDate` |  | Date | — |  |  |
| `DueDate` |  | Date | — |  |  |
| `DueDateApprovers` |  | Date | — |  |  |
| `DueDateAssignees` |  | Date | — |  |  |
| `PriorSubmitForApprovalDate` |  | Date | — |  |  |
| `StartDate` |  | Date | — |  |  |
| `SubmitForApprovalDate` |  | Date | — |  |  |

### Flags (9)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EMailAlertApprovers` |  | Boolean | — |  |  |
| `EMailAlertAssignees` |  | Boolean | — |  |  |
| `EnableForDashboard` |  | Boolean | — |  |  |
| `EnableForEMail` |  | Boolean | — |  |  |
| `IsCompleted` |  | Boolean | — |  |  |
| `IsFormStep` |  | Boolean | — |  |  |
| `IsNotifyClosed` |  | Boolean | — |  |  |
| `IsReDo` |  | Boolean | — |  |  |
| `IsReadOnly` |  | Boolean | — |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EMailMessage` |  | Text | — |  |  |
| `IssueID` |  | Text | — |  |  |
| `SubmitForApprovalByMemberName` |  | Text | — |  |  |
| `TaskName` |  | Text | — |  |  |
| `WFStepNotificationLink` |  | Text | — |  |  |
| `WorkFlowStepName` |  | Text | — |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` |  | Text | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
