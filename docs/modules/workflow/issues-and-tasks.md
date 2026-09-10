# Issues, Forms and Tasks — the three work-object families

**Stated up front — and this is now proven, not inferred.** **A Form *is* an Issue Type, and the
record a Form produces is an `Issue`.** `Manage Forms` opens
`FirmCodeEdit.jsp?includeType=Manage&TableType=2035&tableName=Manage Forms`, and the captured
registry of all 207 platform code tables shows **`TableType=2035` is `Issue Type Code`**
(**Observed**, `../../data-model/code-table-registry.md`). The four "form types" in this tenant are
four **rows in the Issue Type code table**. `CodeIssueType` (19 fields) is the object behind that
table; `Issue` (56 fields) is the record.

This is the answer to *"what is an Issue, versus a Task, versus a WorkFlow?"*, and it is stronger
than anything derivable from the schema dump alone.

**`Issue` is the generic unit-of-work record for the whole product.** Nine other tables extend it by
carrying an `IssueID`. `Task` is a completely separate family — Gantt schedule rows with baselines,
predecessors and a critical path. A **workflow step is either a Form step or a Task step**
(`IsFormStep`), and that Boolean is the fork between the two families.

### Everything else lines up behind that one fact

Each row below was a loose observation before; each is now explained. **Observed** except where
noted.

| Observation | Explained by |
|---|---|
| Every vendor label on the object says **Form** — `Form ClientID`, `Form RecID`, *"Enter the title of the form in this field"* | The UI name for an `Issue` is "Form" |
| Form types carry a `Sequence Prefix` (`ASR`, `LAR`, `RPR`) and `Global Sequence Numbers?` | `Issue.SequenceNumber` — issues are numbered tickets |
| Form types declare attachability per entity kind | `Issue` hangs off `ProjectEntity`, the universal entity spine |
| Every form type reports `WORK FLOW field set? = Yes` | `Issue` is what a workflow routes |
| `Auto close`, `Allow Reply` | Ticket lifecycle properties |
| GraphQL declares an `IssueInterface` | `Issue` is a supertype with variants |
| `InvoiceIssue` (23 fields) and `BidderIssue` (21 fields) exist as their own objects | Two more Issue variants — for invoicing and bidding |
| `CodeIssueType` exists as a 19-field object | The object behind `TableType=2035` |
| `Issue` has 56 fields | It is the generic unit-of-work record for the whole product |

### The design insight, and the warning that follows

**Lucernex did not build a form builder.** It built **one ticket type**, made its subtype a
**code-table value**, gave each subtype its own user-defined fields and **one layout per workflow
step**, and got a form builder for free. **Derived.** That is an economical design and ASG Edge+
should consider copying it rather than modelling each request type as its own aggregate.

The corollary is a warning. **Every request-shaped feature in this product is the same table.** A
rebuild that models Lease Admin Requests, rent-payment approvals, invoice disputes and bid questions
as four separate aggregates will need **four separate workflow engines**. Lucernex needs one. This
is recorded as decision **D13** in
[`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md#3-what-should-deliberately-differ) and argued
from the layouts side in `../layouts-and-forms/forms-vs-pages-vs-layouts.md`.

```
                       ┌──────────────────────────────────────────┐
   CodeIssueType ─────▶│  Issue  ("Form")           56 columns     │◀──── 9 subtype tables
   (Form Type,         │  Subject / Body / DueDate / AssignedTo…   │      each carrying IssueID
    11 IsValidFor*)    └──────────────────────────────────────────┘
                                        ▲                    ▲
                       WorkFlow.KickOffIssueID    WorkFlowStep.IssueID
                                        │                    │
                       ┌────────────────┴────────────────────┴──────────┐
                       │  WorkFlow → WorkFlowStep  (IsFormStep = true)  │
                       └────────────────┬────────────────────┬──────────┘
                                        │                    │
                        WorkFlow.KickOffTaskID     WorkFlowStep.TaskID
                                        ▼                    ▼
                       ┌──────────────────────────────────────────┐
                       │  Task / TaskGroup / TaskItem  37 columns  │◀─── TaskPredecessor
                       │  baseline / projected / actual triads     │     (dependency edges)
                       └──────────────────────────────────────────┘
```

## 1. `Issue` — the Form supertype

56 columns, S1 line 101. Only **4** of them appear in the Manage Data Fields catalog, so the
catalog is useless here and S1 + S2 are the sources.

| Field | Schema type | UI label | Req | Definition (vendor help text) |
|---|---|---|---|---|
| `ActionComment` | Text | Action Comment |  | This field captures any comments left by the approver on the approver's action. |
| `AssignedToMemberIDs` | Member ID | Assignee(s) |  | The assignees of this form. |
| `AttentionEmailTo` | Member ID | Attention Email To: |  | This field is not implemented. |
| `BidderBudget` | Text | Submit Bid |  | Click this button to submit your bid. |
| `BidLevelerBudget` | Text | Condition Bids |  | Click this button to condition bids. |
| `Body` | Text | Description |  | Enter a description of the issue in this field. |
| `BOMapClientRecordID` | Text | Form ClientID | Y |  |
| `Budget` | Budget Type ID | Budget |  | This field is not implemented. |
| `BudgetColumnTypeID` | Budget Type ID | Bid Type |  | Select the budget type from this field. |
| `BudgetStatus` | Text | Budget Status Button |  | Click this button to set the budget status. |
| `CheckedOutByMemberID` | Member ID | Checked Out By |  | The name of the person who checked out the form. |
| `CheckedOutDate` | Date | Checked Out Date |  | The date the form was checked out. |
| `ClosedDate` | Date | Closed Date |  | The date the form was closed. |
| `CodeChangeReasonID` | Dropdown (Change Reason Code) | Cause |  | This field allows you to select a change reason. The values in this field are defined by your system administrator. |
| `CodeDisciplineID` | Dropdown (Discipline Code) | Discipline |  | This field allows you to select a discipline. The values in this field are defined by your system administrator. |
| `CodeIssueTypeID` | Dropdown (Form Type) | Type | Y | This field displays the name of the form layout. |
| `CodeLastActionStatusID` | Dropdown (Last Action Status Code) | Last Action Status |  |  |
| `CodeLocationID` | Dropdown (Location Code) | Location |  | This field allows you to select a location. The values in this field are defined by your system administrator. |
| `CodeMethodOfContactID` | Dropdown (Method Of Contact Code) | Method Of Contact |  | This field allows you to select a method of contact. The values in this field are defined by your system administrator. |
| `CodeOrderStatusID` | Dropdown (Part Order Status Code) | Order Status |  | Select the part order status from this field. |
| `CreatedDate` | Time | Created Date |  | The Created Date field is a system-populated field which captures the date that a record was created. |
| `DocumentIDList` | Number | Documents |  | This is a generic field that allows you to add documents to the form from the Documents page. This field also allows you to upload new documents to the entity and attach them to the form. |
| `DueDate` | Date | Due Date |  | Enter the form due date in this field. |
| `DueDateConv` | Date | Followup |  | Select this check box to indicate that a follow-up is required for this form. When the check box is selected, a Due Date field will appear. Select the date by which the follow-up must be completed. You must also select the members who need to be assigned to the follow-up. |
| `EmployerSiteID` | Vendor Site ID | Vendor Site |  |  |
| `EquipmentID` | Equipment ID | Equipment |  | This field allows you to select a piece of equipment associated with the entity. |
| `EquipmentIDList` | Equipment ID | Equipment List |  | This field is required if you want to use Lucernex's work orders functionality. This field allows you to select one or more pieces of equipment associated with the entity. |
| `ImportedCreatedDate` *(catalog only)* | — | ImportedCreatedDate |  |  |
| `InitiatedByMemberID` | Member ID | Creator |  | The member ID of the person who added the form. |
| `IsClosed` | Boolean | Is Closed? |  | If this field is set to true, it means that the form is closed. If it is set to false, it means that the form is open. |
| `IsCritical` | Boolean | Is Critical? | Y | If this field is set to true, it means that the form is critical. If it is set to false, it means that the form is not critical. Issues with this flag set to true will appear in the Critical Issues widget on the Dashboard, and will have a flag next to their title on the Forms page. |
| `IsPrivate` | Boolean | Private Issue? | Y | If this field is set to true, it means that the form is private. If it is set to false, it means that the form is public. Only certain members will have access to private issues. |
| `IssueDateRange` | Dropdown | Issue Date Range |  | This field is not implemented. |
| `IssueDateType` | Dropdown | Issue Date Type |  | This field is not implemented. |
| `IssueID` | Number | Form RecID |  | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. |
| `LastActionStatusChangeDate` | Date | Last Action Status Change Date |  |  |
| `LastPageLayoutID` | item ID | Last Layout Used | Y | The name of the last form layout used to update the issue. |
| `LastResponseDate` | Date | Last Reply |  | The date of the last reply to this form on the Forms page. |
| `ManagerMemberIDs` | Member ID | Assignee(s) / Manager(s) |  | When added to a form, this field adds a series of fields that allow you to select managers, members, assignees, and approvers. |
| `ModifiedByID` | Member ID | Modified By |  | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. |
| `ModifiedDate` | Time | Modified Date |  | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. |
| `NumberOfResponses` | Number | # Replies |  | The number of replies to a form on the Forms page. |
| `PartNumberIDList` | Number | Part List |  | This field is a custom list. It allows you to select pieces of equipment associated with the entity, select parts for the equipment, enter a quantity of parts, cost, and total. |
| `PartOrderList` | Text | Part Order List |  | This field is a custom list. It allows you to select maintenance categories, vendors, and parts. Then, you must enter the number of parts needed, and the date they are needed by. There are also fields for the status, quantity received, the receipt date, and comments. |
| `PersonContactedID` | Contact | Contacted Contact |  | Select the person who was contacted from this field. |
| `Photos` | Text | Photos |  | This field allows you to upload a photo to the form. You cannot add the photo in Add mode, only in Edit mode. |
| `PONumber` | Text | Invoice Number |  | This field generates an automatic invoice number based on the currently selected entity and form type. This field is typically used for invoices, but can be used for any forms that need to be auto-numbered. This number starts at 0 and is unique within the firm. This field will not display in Add view, but will appear in View and Edit mode after the form has been saved the first time. |
| `PriorIssueID` | Number | Prior Issue |  | If you use the follow-up functionality, this field displays the parent issue that is being followed up on. |
| `ProjectEntityID` | Entity ID | ProjectEntityID |  |  |
| `RelatedIssueID` | Text | Related Issue |  | This field points to a related issue. |
| `SearchField` | Text | Search Field |  | This field determines search criteria for the issue list. |
| `SequenceNumber` | Text | Number | Y | This field generates a sequence number for the record. The next record created receives the next number in the sequence. |
| `Subject` | Text | Title |  | Enter the title of the form in this field. This title is used in the Dashboard and in form and workflow lists. |
| `TaskIDList` | Task/Group ID | Associated Task |  | This field allows you to associate the form with a task in your schedule. |
| `VendorID` | Employer ID | Vendor |  |  |
| `VendorSiteID` | Text | Vendor Site ID |  |  |
| `WorkFlowAdhocMemberID` | Member | Ad Hoc WF Assignee |  | This field lists the members of the entity who can be selected as an ad hoc assignee. |

### What a Form is, functionally

Grouping the 56 columns (**Derived**):

| Group | Columns | Reading |
|---|---|---|
| **Ticket core** | `IssueID`, `SequenceNumber`, `Subject` (label **Title**), `Body` (label **Description**), `CodeIssueTypeID` (label **Type**), `CreatedDate`, `InitiatedByMemberID` (label **Creator**) | A titled, numbered, typed, authored document. |
| **Assignment** | `AssignedToMemberIDs`, `ManagerMemberIDs`, `WorkFlowAdhocMemberID`, `AttentionEmailTo` *(not implemented)* | `ManagerMemberIDs` is documented as *"adds a series of fields that allow you to select managers, members, assignees, and approvers"* — i.e. one catalog field renders a whole people-picker block. |
| **Lifecycle** | `IsClosed`, `ClosedDate`, `DueDate`, `DueDateConv` (label **Followup**), `CodeLastActionStatusID`, `LastActionStatusChangeDate`, `LastResponseDate`, `NumberOfResponses` | Open/closed plus a workflow-written *last action status*. |
| **Triage** | `IsCritical`, `IsPrivate`, `CodeChangeReasonID` (Cause), `CodeDisciplineID`, `CodeMethodOfContactID`, `CodeLocationID`, `PersonContactedID` | `IsCritical` drives the **Critical Issues** dashboard widget (**Observed**, S2 + `docs/screens/001-dashboard-home.md` line 74). |
| **Threading** | `PriorIssueID`, `RelatedIssueID`, `IssueResponse` children, `Question` children | `PriorIssueID` is the follow-up parent: *"If you use the follow-up functionality, this field displays the parent issue that is being followed up on."* |
| **Attachment** | `ProjectEntityID`, `DocumentIDList`, `Photos`, `TaskIDList`, `EquipmentID`, `EquipmentIDList`, `VendorID`, `EmployerSiteID`, `VendorSiteID` | `EquipmentIDList` is *"required if you want to use Lucernex's work orders functionality."* |
| **Locking** | `CheckedOutByMemberID`, `CheckedOutDate` | No expiry — see the reported defect. |
| **Layout** | `LastPageLayoutID` (*"the last form layout used to update the issue"*) | A Form renders through a `PageLayout` and remembers which — but only the **last** one. Since a Form shows a different layout at every step (layout-per-step-per-role), this single pointer cannot reconstruct what each approver saw. See [`template-vs-instance.md` §3a](template-vs-instance.md#historical-reconstruction-is-lossy). |
| **Bidding** ⊘ | `BidderBudget` (button *"Click this button to submit your bid"*), `BidLevelerBudget` (*"Click this button to condition bids"*), `BudgetColumnTypeID` (Bid Type), `BudgetStatus`, `Budget` *(not implemented)* | **⊘ out of scope.** Retained for one structural reason: the bidding workflow's action buttons live **on the Form**, not on the workflow step — evidence that Lucernex has two competing action mechanisms. |
| **Procurement** ⊘ | `PONumber` (label **Invoice Number**), `PartNumberIDList`, `PartOrderList`, `CodeOrderStatusID` | **⊘ out of scope**, except `PONumber`, whose behaviour is in scope as sequence-numbering evidence: *"generates an automatic invoice number based on the currently selected entity and form type… unique within the firm."* That is `CodeIssueType.SequencePrefix` / `IsSequencePerFirm` in action. |
| **Misc** | `ActionComment`, `SearchField`, `IssueDateRange` *(not implemented)*, `IssueDateType` *(not implemented)*, `BOMapClientRecordID`, `ModifiedByID`, `ModifiedDate` | `ActionComment` shares its definition verbatim with `WorkFlowTemplateStepAction.ActionComment` and `WorkFlowStepApprover.ActionComment` — the approver's comment is surfaced on the Form. |

Five columns are explicitly *"This field is not implemented"* (**Observed**): `AttentionEmailTo`,
`Budget`, `IssueDateRange`, `IssueDateType`. A rebuild should drop them.

### The nine subtypes

> **⊘ Cost Management and Budgeting are out of scope** (2026-09-10). Seven of the nine subtypes
> below — `PurchaseOrder`, `ChangeOrder`, `PayApp`, `InvoiceIssue`, `BidPackage`, `BidderIssue`,
> `Question` — belong to those modules. They are **retained as structural evidence, not as
> requirements.** The finding they support is a core workflow one: `Issue` is a supertype, and the
> proof is that nine tables extend it while carrying no title, description, due date, assignee or
> status of their own. Listing three subtypes instead of nine would weaken an argument the rebuild
> depends on. **Do not build any of these modules from this table.**
>
> `ServiceRequest` and `WorkOrder` are facilities maintenance, not Cost Management, and are not
> marked.

Every one of these tables carries a column `IssueID(Text)` and **none of them carries a title,
description, due date, assignee, status, or attachment** — those live only on `Issue`. **Derived**,
S1, exhaustive.

| Subtype | S1 line | Own columns | What it adds |
|---|---:|---:|---|
| `PurchaseOrder` | — | 20 | `PurchaseOrderAmount`, `EstimateAmount`, `RetainagePercent`, `VendorPONumber`, roll-ups `NumberChangeOrders`, `NumberPayApps`, `ApprovedChangeOrderAmount`, `OutstandingChangeOrderAmount`, `PayAppAmount` |
| `ChangeOrder` | — | 16 | `ApprovedChangeOrderAmount`, `OutstandingChangeOrderAmount`, `CostTrackingVariance`, `VendorCONumber`, FK `PurchaseOrderID` |
| `PayApp` | — | 15 | `PayAppAmount`, `RetainagePercent`, `CostTrackingVariance`, FK `PurchaseOrderID` |
| `InvoiceIssue` | 99 | 23 | `InvoiceNumber`, `InvoiceAmount`, `TaxAmount1/2`, `TotalAmount`, `BatchNumber`/`BatchDate`, `ReceivedDate`, `PaidDate`, `CodeInvoiceStatusID` |
| `WorkOrder` | 224 | 30 | Estimated/actual cost, labour hours and dates; `PrimaryVendorID`/`SecondaryVendorID`/`AlternateVendorID`; `ApproverMemberID` + `ApprovalDate`; `CodeEvaluationRatingID`; FK `ServiceRequestID` |
| `ServiceRequest` | — | 30 | `CodeSRQStatusID`/`TypeID`/`SourceID`, `CodeProblemID`, `RequestorPartyID`/`RequestedForPartyID`, `ApproverPartyID` + `ApprovalDate`, `DNEAmount`, `GLNumber`, `RequestedCompletionDate` |
| `BidderIssue` | 17 | 21 | `SubmittedBidAmount`, `ConditionedBidAmount`, `IsWinningBid`, `IsBidInviteAccepted`, `ExtendedBidCloseDate`, `UniqueVendorID` |
| `BidPackage` | — | 53 | The solicitation header; also carries `WinningBidderIssueID` |
| `Question` | — | 14 | `IsPrivateQandA`, `IsPublished`, `IsShared`, `AcceptedResponseID` — bid Q&A |

Plus three child tables hanging off `Issue` directly: `IssueResponse` (11, the reply thread),
`LinkIssuePart` (13, parts consumed), `LinkIssuePartOrder` (16, parts ordered).

**`WorkOrder` and `ServiceRequest` each carry their own `ApproverMemberID` + `ApprovalDate` pair.**
That is a *second*, single-approver approval mechanism entirely outside the workflow engine.
**Derived** — a rebuild must decide whether to unify them, and Lucernex evidently did not.

### `CodeIssueType` — the Form Type registry and the attachability model

The **only** place attachability is declared. `WorkFlowTemplate` has no `IsValidFor*` columns at
all. **Observed**, S1 lines 41 and 221 — and **now Observed in the UI**: the Form Type editor
renders exactly this as *"a boolean per entity type, controlling what a request of this type can be
raised against"* (`../layouts-and-forms/forms-vs-pages-vs-layouts.md`).

The UI labels and the schema columns are both elevens, and they line up — with one uncertain pair.

| Schema flag (S1) | UI label (live) | Confidence of the mapping |
|---|---|---|
| `IsValidForPortfolio` | Portfolio | Observed both sides |
| `IsValidForCapProgram` | Capital Program | Observed both sides |
| `IsValidForPrototype` | Prototype | Observed both sides |
| `IsValidForLocation` | Location | Observed both sides |
| `IsValidForParcel` | Parcel | Observed both sides |
| `IsValidForPotentialProject` | **Site** | **Derived — the one uncertain pair.** "Site" and "Potential Project" are the two names left over after the other ten match. A site under consideration is plausibly a potential project, but this is not proven |
| `IsValidForOpenProject` | Project | Derived |
| `IsValidForFacility` | Facility | Observed both sides |
| `IsValidForCapProject` | Capital Project | Observed both sides |
| `IsValidForContract` | **RE Contract** | Derived — "RE" = real estate, distinguishing it from Equipment Contract |
| `IsValidForEquipContract` | Equipment Contract | Observed both sides |

**Live values.** Both `ASC 842 Schedule Review/Approval` and `Lease Admin Request` are set
`Portfolio = Yes`, `RE Contract = Yes`, and the other nine `No` (**Observed**). Those two request
types can only be raised against a portfolio or a real-estate contract — exactly right for lease
accounting, and a useful sanity check for the rebuild's scope. The attachability of
`Rent Payment Review/Approval` and `User Request` was not captured (**OQ-32**).

### The Form Type's other live properties

The Form Type editor also renders a behaviour group, which **confirms four readings this document
previously had to Infer** (**Observed**, `../layouts-and-forms/forms-vs-pages-vs-layouts.md`):

| UI property | Schema column | Live values | Status change |
|---|---|---|---|
| `WORK FLOW field set?` | `IsWorkFlow` | **Yes for all four** | Inferred → **Observed**. Every Form Type here drives a workflow, and `Manage Forms` / `Manage Work Flows` list the same four names — the relationship is **1:1**. |
| `Auto close` | `AutoClose` | not transcribed | Inferred → **Observed (the control exists)**; *"Close the request automatically on completion"* |
| `Allow Reply` | `AllowReply` | not transcribed | Inferred → **Observed**; *"Whether responses are permitted"* — gates `IssueResponse` threading, as predicted |
| `Sequence Prefix` | `SequencePrefix` | `ASR`, `LAR`, `RPR`; none shown for User Request | Inferred → **Observed** |
| `Global Sequence Numbers?` | `IsSequencePerFirm` | not transcribed | **Caution.** The UI label says *Global* ("platform-wide or per-scope") and the column says *PerFirm*. These are near-inverses; do **not** assume they carry the same polarity. **OQ-45.** |

The identical eleven-flag family appears on seven other objects —
`BidPackageTemplate`, `BudgetColumnType`, `CostTrackingTemplate`, `VirtualTemplateBudget`,
`VirtualTemplateBudgetOption`, `VirtualTemplateFolder`, `VirtualTemplateSchedule` (**Observed**,
S1, exhaustive search for `IsValidFor`) — so this is the platform's standard **template
attachability** pattern.

The chain that gives a workflow its attachability is therefore indirect (**Derived**):

```
WorkFlowTemplate.PageLayoutID  ──▶  PageLayout.CodeIssueTypeID  ──▶  CodeIssueType.IsValidFor*
   ("the form whose completion         (which Form Type this          (which entity types that
    kicks off this work flow")          layout renders)                Form Type may attach to)
```

`CodeIssueType.IsWorkFlow` marks a Form Type as workflow-driving — **Observed** in the UI as
`WORK FLOW field set?`, Yes for all four live types (no vendor help text exists for the column). Combined with `WorkFlowTemplate.LimitByEntity` (*"only available for certain portfolios"*),
a workflow's availability is gated in two independent places, neither of them on the workflow.

The **Forms** and **Work Flow** tabs are confirmed on five entity types in ASG's own feature
inventory (**Observed**, `_xlsx_feature_list.txt`): Portfolio (lines 42-43), Location (476-477),
Facility (488-489), Contract (504-505), Equipment (239-240). That is a subset of the eleven; the
tenant simply does not use the others.

`IssuesAndAlerts` is a text roll-up column that appears on **eleven** entities — `Contract`,
`Facility`, `Location`, `Parcel`, `Program`, `Project`, `ProjectEntity`, `Prototype`,
`PotentialProject`, `BudgetOptionTemplate` — and its definition is the best single statement of how
Forms and Workflows surface on an entity: *"In View mode, this field will display a table with form
and workflow data, such as the **work flow / form type, critical issue count, non-critical issue
count, escalated count, and past due notification count**."* **Observed**, S2. It names four
countable states — critical, non-critical, escalated, past due — which is corroborating evidence
for the escalation model in [`routing-and-approvals.md`](routing-and-approvals.md).

## 2. `Task` — the schedule family

`Task`, `TaskGroup` and `TaskItem` have **byte-identical 37-column shapes** (S1 lines 189-191,
verified field by field — **Derived**). They are three projections of one model discriminated by
`IsTaskGroup`.

> **The live tenant configures zero Task steps.** All 19 workflow steps across all four workflows
> are of type `Form` (**Observed**, `../layouts-and-forms/forms-vs-pages-vs-layouts.md`). The
> `add task step` action exists on the workflow grid, so the capability is present and unused. Two
> consequences: **(a)** the Task step's field set — `TaskName`, `TaskID`, `AutoAdjustTaskDates`,
> `SetTaskInProcess`, `SetTaskCanceled`, and whatever a Task step's editor renders — is entirely
> unobserved; **(b)** ASG Edge+ may be able to drop Task steps from scope, which removes roughly
> half the step model. That is decision **B1** in
> [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md#6-decisions-asg-must-make-before-this-can-be-built),
> and the live evidence now points hard at "not needed".

| Field | Schema type | UI label | Req | Definition (vendor help text) |
|---|---|---|---|---|
| `ActualDuration` | Number | Forecast/Actual Duration |  | Enter the number of days this task is predicted to take. Entering a value in this field automatically changes the value in the Forecast / Actual End date field. A Duration of 1 day means that the task ends on the same day that it was started. Duration refers to working days only, and tasks cannot have a duration of 0. |
| `ActualEndDate` | Date | Forecast/Actual End Date |  | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. |
| `ActualResourceUnits` | Number | Actual Resource Units |  | The actual resource units of the task or task group. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. The value of this field is used to calculate a task item's Remaining Resource Units, using this formula: Actual Resource Units * (1 - Computed Percent Complete). |
| `ActualStartDate` | Date | Forecast/Actual Start Date |  | Enter the actual start date in this field. |
| `Assignee_MemberID` | Member ID | Resources |  | The member ID of the task assignee. |
| `AssigneeMemberIDList` *(catalog only)* | — | Members Assigned to Task |  |  |
| `CodeTaskStatusID` | Dropdown (Task Status Code) | Task Status |  | Select the task status from this field. By default, this value is set to Not Begun. If you select Canceled, the duration is set to 0. If you select Completed, the Percent Complete changes to 100%. If you select In-Process, the Percent Complete is set to 99%, but can be changed if necessary. |
| `DaysAheadOfSchedule` | Number | Days Ahead of Schedule |  | The value of this field equals the original / baseline end date - the actual end date. |
| `Description` | Text | Description |  | The associated email message with the given task. |
| `EMailMessage` | Text | Email Message |  | The email message associated with the given task. |
| `EnableForDashboard` | Boolean | Alert when task Completes |  | This flag is used to determine if the dashboard will receive an alert when the task is completed. |
| `EnableForEMail` | Boolean | Email when task Completes |  | This flag is used to determine if an email will be sent when the task is completed. |
| `IsTaskGroup` | Boolean | Is Task Group | Y | Flag for whether the task is on a critical path or not. (not much insight in the code about this one) |
| `ModifiedByID` | Member ID | Modified By |  | The original duration of the task. It cannot be negative. |
| `ModifiedDate` | Time | Modified Date |  | The original resource units of the task. Task groups aggregate their tasks' original resource units to obtain their own. |
| `OnCriticalPath` | Boolean | On Critical Path? |  | This flag indicates whether the task is on a critical path or not. |
| `OriginalDuration` | Number | Baseline Duration |  | The original or baseline duration of the task. This field's value cannot be negative. |
| `OriginalEndDate` | Date | Baseline End Date |  | The baseline end date of a schedule task on the entity. |
| `OriginalResourceUnits` | Number | Original Resource Units |  | The original resource units of the task or task group. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. |
| `OriginalStartDate` | Date | Baseline Start Date |  | The baseline start date of a schedule task on the entity. |
| `ParentTaskID` | Task/Group ID | Parent Task |  | The ID of the parent task of the given task. |
| `PercentComplete` | Number | Percent Complete |  | The percentage of the task completed. |
| `ProjectedDuration` | Number | Projected Duration |  | Calculates the projected duration of the task. |
| `ProjectedEndDate` | Date | Projected End Date |  | Enter the end date you are aiming for in this field. You can think of your projected dates as your goal dates. |
| `ProjectedResourceUnits` | Number | Projected Resource Units |  | The projected resource units of the task or task group. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. |
| `ProjectedStartDate` | Date | Projected Start Date |  | Enter the start date you are aiming for in this field. You can think of your projected dates as your goal dates. |
| `ProjectEntityID` | Entity ID | ProjectEntityID |  |  |
| `TaskEndsCodeDayOfWeekID` | Dropdown (Day Of Week Code) | Task Ends On Day |  | If the task should end on a particular weekday, select the weekday from this field. If you use this field, the Forecast / Actual End date field will not be editable. The system will automatically calculate the value for the Forecast / Actual End date using the Forecast / Actual Start and End Weekday. |
| `TaskID` | Number | Task RecID |  | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. |
| `TaskName` | Text | Name | Y | Enter the task name in this field. |
| `TskBAndA_NoAccessorConversion` | Text | Baseline with Forecast/Actual End Date |  | Displays both the baseline and forecast /actual end dates. The baseline date is indicated with a (b), the forecast date is indicated with a (f), and the actual date is indicated with an (a). |
| `TskDone_ActualEndDate` | Date | Actual End Date |  | The task end date. If a task is canceled, this field will either be blank or will contain the word "canceled". |
| `TskNotDone_ActualEndDate` | Date | Forecast End Date |  | The forecasted end date of the task. This field only displays for non-complete tasks. |
| `TskNotDoneCompleted_NoAccessorConversion` | Text | Forecast End Date/Complete |  | If the task is complete, this field displays "complete". If the task is canceled, the field displays "canceled". Otherwise, the field displays the forecasted end date. |
| `TskPredVal_ActualLeadLagDays` | Number | Forecast/Actual Lead/Lag Days |  | This field computes the actual lead / lag days of this task's predecessor. This value is used when a task checks if all of its predecessors have completed (where all of their lead days are < 0). |
| `TskPredVal_OriginalLeadLagDays` | Number | Baseline Lead/Lag Days |  | The original lead / lag days of the task predecessor. |
| `TskPredVal_PredecessorTaskID` | Task/Group ID | Predecessor Task(s) |  | The ID of the predecessor task of a given task. |
| `TskPredVal_ProjectedLeadLagDays` | Number | Projected Lead/Lag Days |  | The number of lead or lag days of the predecessor task. |

Every date and duration comes as a **triad** — Baseline (`Original*`), Projected, Forecast/Actual —
plus the four presentation-only `Tsk*_NoAccessorConversion` / `TskDone_*` / `TskNotDone_*` columns
that format them for a Gantt grid. **Observed**, S2 labels.

Status semantics are **Observed** verbatim from `Task.CodeTaskStatusID`: *"By default, this value is
set to **Not Begun**. If you select **Canceled**, the duration is set to 0. If you select
**Completed**, the Percent Complete changes to 100%. If you select **In-Process**, the Percent
Complete is set to 99%, but can be changed."* That gives four **Observed** values of
`Task Status Code`: Not Begun, In-Process, Completed, Canceled.

### `TaskPredecessor` — dependency edges, for the schedule only

| Field | Schema type | UI label | Req | Definition (vendor help text) |
|---|---|---|---|---|
| `ActualLeadLagDays` | Number | Actual Lead Lag Days | Y | The actual lead / lag days of the task predecessor. This value is used when a task checks if all of its predecessors have completed (where all of their lead days are < 0). |
| `BOMapClientRecordID` | Text | Task Predecessor ClientID | Y | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". |
| `CodeTaskLeadLagTypeID` | Dropdown (Task Lead Lag Type Code) | Task Lead Lag Type | Y | Select the relationship type of the two tasks from this field. If this value is Start-to-Start, the start date of the successor task is dependent upon the start date of the predecessor task. If this value is Finish-to-Start, the start date of the successor task is dependent upon the finish date of the predecessor task. |
| `CreatedByID` | Member ID | Created By |  | The Created By field is a system-populated field which captures the name of the member making changes to a record. |
| `CreatedDate` | Time | Created Date |  | The Created Date field is a system-populated field which captures the date that a record was created. |
| `ModifiedByID` | Member ID | Modified By |  | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. |
| `ModifiedDate` | Time | Modified Date |  | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. |
| `OriginalLeadLagDays` | Number | Original Lead Lag Days | Y | The original lead / lag days of the task predecessor. |
| `PredecessorTaskID` | Task/Group ID | Predecessor Task |  | Select the predecessor task from this field. |
| `PredecessorTemplateTaskName` | Text | Predecessor Task Name |  | This field displays the name of the predecessor task. |
| `ProjectedLeadLagDays` | Number | Projected Lead/Lag Days | Y | Enter the number of lead or lag days in this field. |
| `ProjectEntityID` | Entity ID | ProjectEntityID |  |  |
| `RevNumber` | Number | Rev Number |  | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. |
| `SuccessorTaskID` | Task/Group ID | Successor Task | Y | Select the successor task from this field. |
| `TaskPredecessorID` | Number | Task Predecessor RecID |  | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. |

**Observed**, `CodeTaskLeadLagTypeID`: *"If this value is **Start-to-Start**, the start date of the
successor task is dependent upon the start date of the predecessor task. If this value is
**Finish-to-Start**, the start date of the successor task is dependent upon the finish date of the
predecessor task."* Two named types; whether Finish-to-Finish and Start-to-Finish also exist is
unstated. **Open question OQ-28.**

**Observed**, `Task.TskPredVal_ActualLeadLagDays`: *"This value is used when a task checks if **all
of its predecessors have completed** (where all of their lead days are < 0)."* — the completion
predicate is a conjunction over all predecessors, i.e. a genuine **AND-join**.

**Critical distinction for the rebuild.** The schedule has what the workflow lacks:

| | Schedule (`Task`) | Workflow (`WorkFlowStep`) |
|---|---|---|
| Dependency edges | `TaskPredecessor` — a real DAG | **None** — integer `StepNumber` only |
| Join semantics | AND-join over all predecessors | **None** |
| Lead/lag | Three lead/lag columns + a type code | **None** |
| Hierarchy | `ParentTaskID`, `IsTaskGroup` | **None** — flat list |
| Critical path | `OnCriticalPath` | **None** |
| Percent complete | `PercentComplete` | **None** — Boolean `IsCompleted` |
| Baseline vs actual | Full triads | Single `StartDate`/`CompleteDate` |

**Derived, and load-bearing: `TaskPredecessor` is a schedule concept and does *not* apply to
workflow steps.** There is no `WorkFlowStepPredecessor` in the 223-object schema. A rebuild that
assumes workflow steps form a DAG because `TaskPredecessor` exists would be modelling the wrong
family.

### Task assignment

Three separate mechanisms, all **Observed** from S1/S2:

| Mechanism | Object | Targets |
|---|---|---|
| Single resource | `Task.Assignee_MemberID` (label **Resources**) | one member |
| Named members | `LinkTaskMember` (5 cols) | many members |
| Role-based | `LinkTaskByCodeMember` (8 cols) — `CodeJobTitleID` + `OrgChartLevel`, labelled *"Template Auto-Assignment"* | job title / org chart level |

`LinkTaskByCodeMember`'s vendor labels are *"The job title that should be **automatically
assigned** to a task"* and *"The org chart level that should be automatically assigned to a task"*.
This is the **same four-way principal-selector pattern** as workflow routing, minus User Class.
**Derived.**

`Task.AssigneeMemberIDList` appears in the catalog (label *Members Assigned to Task*) but not in
the physical schema — it is the read-through projection of `LinkTaskMember`. **Derived.**

### Schedule templates

`TaskTemplate` is a one-column stub. The real template machinery is `TaskTemplateAudit` (18 cols,
S1 line 194), which records a **template application event**: `EntityTemplateID`,
`TaskEntityTemplateID`, `BudgetEntityTemplateID`, `FolderEntityTemplateID`,
`CodeFolderActionIDList`, `CopyFolderStructure`, `ScheduleStartDate`, `ScheduleEndDate`,
`AppliedDate`, `EntityTemplateTypeName`. **Derived:** applying a schedule template to an entity
stamps schedule, budget and folder structure together in one audited operation. Admin screen:
**Manage Schedule Templates**, `/en/admin/TaskTemplateEdit.jsp?includeType=Manage&BOType=TaskTemplate`
(**Observed**, `docs/admin/004` line 58).

## 3. Milestones — the third timeline

`ProcessTimelineTemplate` (10) → `ProcessTimeline` (31). Admin screen **Manage Milestone Timeline**,
`/en/admin/ProcessTimelineEdit.jsp` (**Observed**, `docs/admin/004` line 59).

| Field | Schema type | UI label | Req | Definition (vendor help text) |
|---|---|---|---|---|
| `AlwaysShowInSummary` | Boolean | Always Show in Summary? | Y | If this milestone is a summary item, select this check box. Milestones that have this check box selected will appear in the default view of the Milestone Timeline section of your Summary page, even if the milestone has been completed. |
| `CodeProjectPhaseID` | Dropdown (Project Phase Code) | Project Phase | Y | Select the project phase that this milestone belongs to from this field. The project phase corresponds with key dates on your project. You may have multiple milestones that share the same phase. |
| `CompletedPhaseStatus` | Text | Completed Phase Status | Y | Enter the status the entity should have after the milestone is completed in this field. |
| `DefaultTaskName` | Text | Default Task Name |  | Select the schedule task whose completion triggers this milestone from this field. |
| `InProcessPhaseStatus` | Text | In Process Phase Status | Y | Enter the status the entity should have prior to the milestone being completed in this field. |
| `ModifiedByID` | Member ID | Milestone Template Modified By |  | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. |
| `ModifiedDate` | Time | Milestone Template Modified Date |  | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. |
| `PreviousProcessTimelineID` | Text | Previous Milestone Template |  | The ID of the milestone that precedes this milestone. |
| `ProcessTimelineTemplateID` | Number | Milestone Template RecID |  | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. |
| `ProcessTimelineTemplateName` | Text | Milestone Template Name | Y | Enter the name of the milestone in this field. |

`ProcessTimeline` is a 31-column subset of the `Task` shape (no `IsTaskGroup`, `ParentTaskID`,
`OnCriticalPath`, `TaskID`, or resource-unit columns; plus `RemainingDays` and
`ProcessTimelineTemplateName`). **Derived.**

The mechanism, **Observed** from S2:

- `DefaultTaskName` — *"Select the schedule task whose completion **triggers this milestone**."*
- `InProcessPhaseStatus` / `CompletedPhaseStatus` — *"Enter the status **the entity** should have
  prior to / after the milestone being completed."*
- `PreviousProcessTimelineID` — the milestone chain (a linked list, not a DAG).
- `CodeProjectPhaseID` — *"The project phase corresponds with key dates on your project. You may
  have multiple milestones that share the same phase."*
- `AlwaysShowInSummary` — pins the milestone to the entity Summary page.

So the milestone timeline is a **task-completion → entity-phase-status projection**. It writes
`ProjectEntity.CurrentPhaseStatus`, `CurrentMilestone`, `NextMilestone`, `PreviousMilestone`,
`MilestoneTimeline` and the five `*PhaseStatus` columns (`RealEstatePhaseStatus`,
`DesignPhaseStatus`, `ConstructionPhaseStatus`, `PossessionPhaseStatus`, `OperationsPhaseStatus`)
— all **Observed** on `ProjectEntity`, S1.

**`ProcessTimeline` has no link to `WorkFlow` whatsoever.** **Derived**, exhaustive. Milestones
track schedule progress; workflows route approvals; the two meet only through `Task`.

## 4. How the three families connect to a workflow

| Edge | Column | Direction | Evidence |
|---|---|---|---|
| Form kicks off a workflow | `WorkFlow.KickOffIssueID` | Form → Workflow | **Observed**, S2 |
| Task kicks off a workflow | `WorkFlow.KickOffTaskID` | Task → Workflow | **Observed**, S2 |
| Step works a Form | `WorkFlowStep.IssueID` + `IsFormStep = true` | Workflow → Form | **Observed**, S2 |
| Step works a Task | `WorkFlowStep.TaskID` + `IsFormStep = false` | Workflow → Task | **Observed**, S1/S2 |
| Step names its task at design time | `WorkFlowTemplateStep.TaskName` | Template → Task | **Observed**, S2 |
| Template names its kick-off task | `WorkFlowTemplate.TaskName` | Template → Task | **Observed**, S2 |
| Step drives task status | `SetTaskInProcess`, `SetTaskCanceled` | Workflow → Task | **Observed**, S2 |
| Step drives task dates | `AutoAdjustTaskDates` | Workflow → Task | **Observed**, S2 |
| Action stamps the Form's status | `CodeLastActionStatusID` → `Issue.CodeLastActionStatusID` | Workflow → Form | **Derived** |
| Form lists its tasks | `Issue.TaskIDList` | Form → Task | **Observed**, S2 |
| Form carries the ad-hoc assignee picker | `Issue.WorkFlowAdhocMemberID` | Form → Workflow | **Observed**, S2 |

Note the asymmetry in `SetTaskInProcess` / `SetTaskCanceled`: their **labels** say *task*
(*"Mark Task In Progress When Step Starts"*, *"Cancel Task When Step is Canceled"*) but their
**definitions** say *step* (*"set the **work flow step** status to 'In Process' when the step
starts"*). One of the two is wrong. **Open question OQ-29** — and it decides whether these flags
write `Task.CodeTaskStatusID` or `WorkFlowStep.CodeWorkFlowStatusID`.

## Open questions

1. **OQ-29 — do `SetTaskInProcess` / `SetTaskCanceled` write the Task's status or the Step's?**
   Label and definition contradict each other. Configure a task step with both flags, start it, and
   read `Task.CodeTaskStatusID` on the linked schedule task.
2. **OQ-30 — is a Form created by the workflow, or does the workflow attach to an existing Form?**
   `WorkFlowStep.IssueID` exists but nothing says who creates the row. Kick off a workflow and
   check whether a new row appears on the entity's **Forms** tab at step start.
3. **OQ-31 — how does a Task step differ from a Form step in the UI?** `IsFormStep = false` steps
   have `PageLayoutAssigneesID` too, which implies they still render a layout. Configure one of
   each and compare.
4. **OQ-32 — which of the eleven `IsValidFor*` entity types does ASG actually use?** Five are
   confirmed by the feature list (Portfolio, Location, Facility, Contract, Equipment). Open
   **Manage Forms** and record the flags on every Form Type in the tenant.
5. **OQ-28 — are Finish-to-Finish and Start-to-Finish predecessor types available?** Open
   **Manage Firm Drop Downs** → `Task Lead Lag Type Code` and read the values.
6. **OQ-33 — do `WorkOrder.ApproverMemberID` and `ServiceRequest.ApproverPartyID` bypass the
   workflow engine entirely?** If they do, there are two approval systems and a rebuild must
   consolidate them.
