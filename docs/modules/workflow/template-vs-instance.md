# Template vs. instance — field-level correspondence

**Stated up front.** Instantiation is **not** a copy. At the header level `WorkFlowTemplate` and
`WorkFlow` share nothing but the FK and four audit columns — not even the name. At the step level
exactly **20 configuration fields are snapshotted** from `WorkFlowTemplateStep` onto `WorkFlowStep`,
**35 stay behind on the template**, and **30 exist only on the instance**. The consequence is a
**hybrid model**: a running step reads *some* of its behaviour from its own frozen copy and *the
rest* live from `WorkFlowTemplateStep` via `WorkFlowStep.WorkFlowTemplateStepID`. Editing a live
template therefore changes running instances for the un-snapshotted half and not for the
snapshotted half. Any rebuild that picks one discipline — pure snapshot or pure live-read — will
diverge from Lucernex on migrated data.

One thing Lucernex freezes correctly: **the page layout**. §3a below shows that layout-per-step-
per-role is the engine's real source of expressiveness, and that the layout id is snapshotted onto
the instance while the behaviour flags are not.

All correspondence tables below are **Derived** by set operations over the union of S1
(`_lucernex_objects_summary.txt`) and S3 (`docs/data-fields/all-fields.csv`) field lists. Vendor
help text quoted in the Reading column is **Observed** from S2 (`_xlsx_lucernex_jcrew.txt`).

## 1. Header level — `WorkFlowTemplate` (25) vs `WorkFlow` (21)

### Shared

| Field | On template | On instance | Reading |
|---|---|---|---|
| `WorkFlowTemplateID` | PK | FK | The only real link. |
| `BOMapClientRecordID` | own | own | Import key; independent values. |
| `CreatedDate` | own | own | Independent timestamps. |
| `ModifiedByID`, `ModifiedDate` | own | own | Independent. |

Five columns, four of them bookkeeping. **Nothing configurational is copied at header level.**

### Template-only (20) — never appears on the instance

| Field | Category | Reading |
|---|---|---|
| `WorkFlowTemplateName` | Identity | Not copied. The instance gets its own `WorkFlowName` — **Open question OQ-9: is `WorkFlowName` seeded from the template name, from the kick-off form's `Subject`, or typed by the initiator?** |
| `Description` | Identity | Not carried to the instance. |
| `KickOffMethod`, `KickOffID`, `KickOffDescription`, `StatusChangeID`, `StatusChangeType` | Kick-off config | The instance records *which* form/task fired it (`KickOffIssueID`/`KickOffTaskID`) but not *how* it was configured to fire. |
| `PageLayoutID` | Kick-off config | The kick-off form layout. Per-step layouts *are* copied; this one is not. |
| `TaskName` | Kick-off config | The kick-off schedule task. |
| `DefaultWFCodePriorityID` | Runtime seed | **Renamed on the instance to `WorkFlowCodePriorityID`.** The "Default" prefix and the identical `sCODE_PRIORITY` type make this the one genuine header-level seed. **Derived, high confidence.** |
| `AutoAssignInitiator` | Runtime behaviour | Read live. Governs whether `WorkFlow.AdhocMemberID` is auto-populated. |
| `LimitByEntity` | Availability | Design-time gate only; irrelevant once running. |
| `EnableVendorCollaboration`, `CollaboratorJobTitleIDList` | Access | Read live. |
| `NotifyAllApproversComplete`, `NotifyAllAssigneesComplete`, `NotifyInitiatorComplete` | Closure notification | **Read live at close time.** Changing these on a template changes what a running workflow does when it finishes. |
| `IsEnabledLxJSCode` | Escape hatch | Read live. |
| `CreatedByID` | Audit | The instance instead has `InitiatedByMemberID`. |
| `RevNumber` | Audit | Template modification counter. |

### Instance-only (16)

| Field | Category | Reading |
|---|---|---|
| `WorkFlowID` | Identity | PK. |
| `WorkFlowName` | Identity | See OQ-9. |
| `ProjectEntityID` | Attachment | Owning entity. Physical column, not in the catalog. |
| `TriggerCodeSQLTableID`, `TriggerObjectID` | Attachment | Polymorphic pointer to the triggering record. Catalog-only. |
| `KickOffIssueID` | Provenance | *"The ID of the form that kicked off the work flow."* |
| `KickOffTaskID` | Provenance | *"The ID of the schedule task that kicked off the work flow."* |
| `InitiatedByMemberID` | Provenance | *"The member ID of the user who initiated the work flow."* |
| `AdhocMemberID` | Routing | *"Select an ad hoc assignee from this field."* One slot per instance. |
| `WorkFlowCodePriorityID` | Runtime | Seeded from `DefaultWFCodePriorityID`; overridable. |
| `CodeWorkFlowStatusID` | State | *"This field displays the status of the work flow on the Work Flows page."* |
| `IsCompleted` | State | *"If true, this work flow has been completed."* |
| `ClosedDate` | State | *"The date that the work flow was closed."* |
| `Inactive` | State | *"If true, this work flow has been deactivated on the Work Flow page."* |
| `NumberOfDaysOpen` | Derived metric | Stored, not computed at read time. |
| `WFApproverList` | Roll-up | Denormalised list of `WorkFlowStepApprover` rows. |

**Provenance is captured for two of the three kick-off methods and lost for the third.** No column
records the parent workflow or the parent action when a workflow is spawned by
`WorkFlowTemplateStepAction.KickOffWorkFlowTemplateID`. **Derived** — see OQ-5 in
[`data-model.md`](data-model.md#open-questions).

## 2. Step level — `WorkFlowTemplateStep` (59) vs `WorkFlowStep` (54)

### 2a. Snapshotted at instantiation — 20 configuration fields

Same internal name on both objects, same semantics, independent storage.

| # | Field | Type | What changes between template and instance |
|---:|---|---|---|
| 1 | `StepNumber` | Number | Identical. The step's address in the sequence. |
| 2 | `TaskName` | Text | Template: *"Select the schedule task that this work flow step should be associated with."* Instance: *"The name of the schedule task this work flow step is associated with."* Resolved; the instance additionally gains the FK `TaskID`. |
| 3 | `IsFormStep` | Boolean | Template: *"This field has one of two values: Form Step or Task Step."* Instance: *"If this step is a form step, this value is true. If this step is a task step, false."* Identical. |
| 4 | `Priority` | Number | Template label "Relative Priority"; instance label "Priority". |
| 5 | `PageLayoutApproversID` | `sTYPE_FORM_PAGE_LAYOUT` → `sTYPE_PAGE_LAYOUT` | **Type changes.** Template selects a *form* layout; the instance stores the resolved layout id. |
| 6 | `PageLayoutAssigneesID` | same | same |
| 7 | `ApproverMemberIDList` | Member ID | **The critical one.** Template: *"Select the members that should approve this work flow task."* Instance: *"This field **gets** a list of the approvers that **can be assigned** to this work flow step."* The instance value is the **resolved** set, computed from `ApproverType` + the three template lists. See §3. |
| 8 | `AssigneeMemberIDList` | Member ID | Same resolution, for assignees. |
| 9 | `NotifieeMemberIDList` | Member ID | Same resolution, for notifiees. Instance label "WF Notify List". |
| 10 | `DurationDaysApprovers` | Number | Template: *"Enter how long in days an approver has to complete a step."* Instance: *"Calculates the duration of this work flow step for approvers."* — the instance value drives `DueDateApprovers`. |
| 11 | `DurationDaysAssignees` | Number | Same, for assignees. |
| 12 | `DaysUntilWarnApprovers` | Number | Days before the **approver** is warned. |
| 13 | `DaysUntilWarnAssignees` | Number | Days before the **assignee** is warned. |
| 14 | `DaysUntilAlertApprovers` | Number | Days before a **manager** is alerted. |
| 15 | `DaysUntilAlertAssignees` | Number | Days before a **manager** is alerted. |
| 16 | `EMailAlertApprovers` | Boolean | Dashboard alert to approver at step start. |
| 17 | `EMailAlertAssignees` | Boolean | Dashboard alert to assignee at step start. |
| 18 | `EnableForEMail` | Boolean | Email channel on. |
| 19 | `EnableForDashboard` | Boolean | Dashboard channel on. |
| 20 | `EMailMessage` | Textarea | The message body, frozen at instantiation. |

Plus four bookkeeping columns present on both with independent values: `BOMapClientRecordID`,
`ModifiedByID`, `ModifiedDate`, and the back-pointer `WorkFlowTemplateStepID`.

**The SLA configuration is frozen; the routing *rules* are not copied at all; the notification
*decisions* are split between the two.** That split is the source of the hybrid-read hazard.

### 2b. Template-only — 35 fields never reaching the instance

| Field | Category | Consequence at runtime |
|---|---|---|
| `WorkFlowTemplateStepID` | PK | The instance holds it as an FK, so live read-through is always possible. |
| `WorkFlowTemplateID` | FK | — |
| `WorkFlowTemplateStepName` | Identity | Instance has `WorkFlowStepName`, documented as *"The name of the work flow step **from the work flow template**"* — so it **is** copied in substance under a different column name. **Derived.** |
| `Description` | Identity | Lost at runtime. |
| `ApproverType`, `ApproverJobTitleIDList`, `ApproverUserClassIDList` | Approver routing | **Not on the instance.** Re-resolution requires reading the template. |
| `AssigneeType`, `AssigneeJobTitleIDList`, `AssigneeUserClassIDList` | Assignee routing | Same. |
| `NotifieeType`, `NotifieeJobTitleIDList`, `NotifieeUserClassIDList` | Notifiee routing | Same. |
| `ComputedRequiresApprovers`, `ComputedRequiresAssignees` | Routing | Derived template predicates. |
| `ReassignApproversJobTitleIDList`, `ReassignAssigneesJobTitleIDList` | Reassignment | *"When added to a form, this field allows users with appropriate permissions to reassign approvers/assignees by job title."* These are **form fields**, surfaced on a layout, not step state. |
| `UnassignedApproverID` | Routing | Placeholder; unimplemented. |
| `AutoLaunchNextStep` | Control flow | **Read live.** *"Select this check box if you want Lucernex to automatically launch the next step **if it is a form**."* |
| `AutoAdjustTaskDates` | Task coupling | **Read live.** Adjusts the linked `Task`'s dates to the step's. |
| `SetTaskInProcess` | Task coupling | **Read live.** *"…set the work flow step status to 'In Process' when the step starts."* |
| `SetTaskCanceled` | Task coupling | **Read live.** *"…set the work flow step status to 'Canceled' when the user cancels the step."* |
| `NotifyStepApproversStarted`, `NotifyStepAssigneesStarted` | Notification | **Read live at step start.** |
| `DaysUntilNotification` | Notification | *"the number of days **after the form completion date** a notification should be sent."* Its instance counterpart is the hidden `ComputedDueDateNotification`. |
| `RunAtStartApprover1ID`, `RunAtStartApprover2ID`, `RunAtCompleteApprover1ID`, `RunAtCompleteApprover2ID` | Dead | *"placeholder for an upcoming feature."* |
| `runAtStartScheduledJob1ID`, `runAtStartScheduledJob2ID`, `runAtCompleteScheduledJob1ID`, `runAtCompleteScheduledJob2ID` | Dead | Catalog-only; no physical column. |
| `CreatedByID`, `CreatedDate`, `RevNumber` | Audit | — |

### 2c. Instance-only — 30 fields

| Field | Category | Reading |
|---|---|---|
| `WorkFlowStepID` | Identity | PK. |
| `WorkFlowStepName` | Identity | Copy of `WorkFlowTemplateStepName` under a new name. |
| `WorkFlowID` | Structure | Parent instance. |
| `ProjectEntityID` | Attachment | Physical only. |
| `IssueID` | Work object | *"The ID of the form associated with this work flow step."* |
| `TaskID` | Work object | The resolved schedule task. |
| `CodeWorkFlowStatusID` | State | *"The status of the work flow step."* |
| `IsCompleted` | State | Boolean duplicate of the status. |
| `IsReDo` | State | *"If true, the step must be completed again… related to the action the approver takes."* |
| `IsReadOnly` | State | Set by an action's `DisableEditAfterDecision`. |
| `IsNotifyClosed` | State | See OQ-6. |
| `StartDate`, `CompleteDate` | Dates | Actuals. |
| `DueDate`, `DueDateApprovers`, `DueDateAssignees` | Dates | *"Calculates the due date…"* — computed from `StartDate` + `DurationDays*`. |
| `ComputedWarnDateApprovers`, `ComputedWarnDateAssignees`, `ComputedAlertDateApprovers`, `ComputedAlertDateAssignees`, `ComputedDueDateNotification` | Dates | Hidden materialised escalation calendar. |
| `SubmitForApprovalByMemberID`, `SubmitForApprovalByMemberName`, `SubmitForApprovalDate` | Submission | Current round. |
| `PriorSubmitByMemberID`, `PriorSubmitForApprovalDate` | Submission | Exactly one previous round. |
| `CurrentStepMemberIDList` | Routing | *"The members associated with the current workflow step."* |
| `CheckedOutByMemberID`, `CheckedOutDate` | Lock | Pessimistic checkout, no expiry. |
| `WFStepNotificationLink` | Notification | Deep link for emails. |

## 3. What "resolution" means, concretely

The template says *who should act* in role terms. The instance says *which named people may act*.
The transformation happens once, at step instantiation. **Derived** from the field split plus S2's
two definitions of `ApproverMemberIDList` (template: "Select the members that **should** approve";
instance: "**gets** a list of the approvers that **can be assigned**").

```
WorkFlowTemplateStep.ApproverType            ─┐
WorkFlowTemplateStep.ApproverMemberIDList     │
WorkFlowTemplateStep.ApproverJobTitleIDList   ├─► resolve against the entity's roster ─►
WorkFlowTemplateStep.ApproverUserClassIDList  │   (LinkMemberProjectEntity, Member.CodeJobTitleID,
WorkFlowTemplateStepMember.OrgChartLevel     ─┘    Member.CodeUserClassID, Member.SupervisorID)

                                              ─► WorkFlowStep.ApproverMemberIDList  (the flat set)
                                              ─► one WorkFlowStepApprover row per resolved member
```

The same pipeline runs three times per step — approvers, assignees, notifiees — but only the first
two materialise per-person rows. Notifiees get the flat list and nothing else. Full detail in
[`routing-and-approvals.md`](routing-and-approvals.md).

## 3a. Layout-per-step-per-role — the real source of expressiveness

**Observed**, `../layouts-and-forms/forms-vs-pages-vs-layouts.md`. This is the finding that most
changes how the template/instance split should be read.

A Form type owns **many** page layouts and their names are step names:

| Form type | Steps | Layouts | Layout names |
|---|---:|---:|---|
| ASC 842 Schedule Review/Approval | 3 | 4 | `ASR Submit ASC 842 Schedules` · `ASR Initial Review of ASC 842 Schedule` · `ASR Approve ASC 842 Schedules (ASG)` · `ASR Approve ASC 842 Schedules (Client)` |
| Lease Admin Request | 8 | 9 | `LAR Submit…` · `LAR Initial Review…` · `LAR Abstract Lease Document` · `LAR Review Financial Abstract` · `LAR ASG Review…` · `LAR Client Review…` · `LAR Import Payment History/Sales` · `LAR Finalize…` · `LAR Complete…` |
| Rent Payment Review/Approval | 6 | 6 | `RPR Submit…` · `RPR Initial Review…` · `RPR Approve … (ASG)` · `RPR Approve … (Client)` · `RPR Generate Final Rent Payment File` · `RPR Final Rent Payment File` |

**The N + 1 pattern.** ASC 842: 3 steps, 4 layouts. Lease Admin Request: 8 steps, 9 layouts. In both
cases the extra layout is the one named **Submit** — and that is exactly
`WorkFlowTemplate.PageLayoutID`, whose vendor definition is *"Select the form whose completion you
want to have kick off this work flow"* (**Observed**, S2). **Derived, and it confirms the kick-off
model independently:** the Submit layout is the kick-off form; the remaining N layouts are the step
layouts.

**But the correspondence is not clean, and the gaps are informative.** Matching live layout names
against live step names:

| Form type | Layouts with a matching step | Layouts with no step | Steps with no matching layout |
|---|---|---|---|
| ASC 842 | 3 of 3 | `Submit` (kick-off) | — |
| Lease Admin Request | 7 of 8 | `Submit` (kick-off), **`LAR Review Financial Abstract`** | **step 7 `Finalize Lease Admin Requests (Defaults)`** |
| Rent Payment | 5 of 6 | `Submit` (kick-off) | **step 3 `Approve Rent Preview File (LA)`** |

Two readings account for the mismatches, and they are not exclusive (**Derived**):

1. **Layouts are shared across steps.** `Approve … (ASG)` and `Approve … (LA)` plausibly render the
   same layout; `Finalize` and `Finalize (Defaults)` likewise. `PageLayoutApproversID` is a plain FK
   with no uniqueness constraint, so sharing is permitted.
2. **There are two layouts per step, and the grid shows only one.** `WorkFlowTemplateStep` carries
   **both** `PageLayoutApproversID` and `PageLayoutAssigneesID`, and the live `Form/Task` column
   renders its value **suffixed `(Approvers)`** (**Observed**). So the grid is showing the approver
   layout only. `LAR Review Financial Abstract` — a layout with no step of that name — is exactly
   the shape of an *assignee* layout for one of the review steps.

**The correct statement of the mechanism is therefore layout-per-step-per-role.** The same record
shows a different field surface at each stage *and* a different surface to the approver than to the
assignee at the same stage. Submit shows entry fields; Review shows read-mostly fields plus a
decision; Approve shows the approval surface.

### `sTYPE_FORM_PAGE_LAYOUT` exists only to serve the workflow engine

**Observed, and decisive.** The field type `sTYPE_FORM_PAGE_LAYOUT` appears on exactly **three**
fields in the entire 6,158-leaf Manage Data Fields catalog, and all three belong to the workflow
definition:

| Field | Object | Role |
|---|---|---|
| `PageLayoutID` | `WorkFlowTemplate` | the kick-off **Submit** layout |
| `PageLayoutApproversID` | **`WorkFlowTemplateStep`** | the step's **approver** layout |
| `PageLayoutAssigneesID` | **`WorkFlowTemplateStep`** | the step's **assignee** layout |

Source: `../../data-fields/all-fields.csv`, exhaustive grep — three hits, no others. Written up from
the layouts side as `LAY-R-166a`, with the instance-side degradation as `LAY-R-166b` and the
unconstrained-FK consequence as `LAY-R-166c`/`166d`
(`../layouts-and-forms/rules.md`). **Derived:** a "Form Page Layout" is *definitionally* a
workflow-bound layout. The platform distinguishes it as a
type precisely because it is bound to a step and a role, which is independent structural
confirmation of the layout-per-step-per-role reading above.

Note that the two per-role layouts are on **`WorkFlowTemplateStep`**, not `WorkFlowTemplate`. That
distinction is the whole finding: one kick-off layout per *workflow*, two layouts per *step*. A
reading that puts all three on the template collapses N×2 step surfaces into one and loses the
mechanism.

On the instance the same two fields are typed plain `sTYPE_PAGE_LAYOUT`
(`WorkFlowStep.PageLayoutApproversID` / `PageLayoutAssigneesID`, `all-fields.csv` lines 5886-5887) —
**Observed**. The type narrows from "a layout bound to a workflow step" at design time to "a layout
id" at run time, which is exactly what a snapshot looks like.

### Historical reconstruction is lossy

`Issue.LastPageLayoutID` (label **Last Layout Used**, type `item ID`) records *"the name of the last
form layout used to update the issue"* — **Observed**, S2. It is the only pointer from a completed
request back to a layout.

**Derived: it is singular, so it is lossy.** It preserves which surface the record was *last* edited
through, not which surface each step used. The layouts module reached the same conclusion
independently and records it as `LAY-R-164` in
`../layouts-and-forms/rules.md`. Re-rendering a finished eight-step Lease Admin Request as
each approver actually saw it requires joining back through `WorkFlowStep.PageLayoutApproversID` per
step — which works only while those `WorkFlowStep` rows survive. For ASG Edge+ this is the same
depth-1 history problem as the `Prior*` slots (D4 in
[`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md)): **if you want to show an auditor what a
decision looked like at the moment it was taken, store the layout reference on the decision record,
not just on the request.**

### What this means for the template/instance split

`PageLayoutApproversID` and `PageLayoutAssigneesID` are **among the 20 snapshotted fields** (§2a rows
5-6), and their type changes across the boundary — `sTYPE_FORM_PAGE_LAYOUT` on the template,
`sTYPE_PAGE_LAYOUT` on the instance. **Derived: the instance freezes the layout id at step entry.**

That is the right design and a rebuild should keep it. If a running approval snapshots its layout,
an administrator editing layouts cannot change what a half-completed approval shows — which is the
opposite of the hazard in §5, where 35 *behaviour* fields are read live. **Lucernex freezes the
presentation and floats the behaviour. Both should be frozen.**

Two consequences for ASG Edge+:

- Layout-per-step-per-role must be a first-class concept, not conditional sections on one form.
  Note that conditional field rules can *also* vary a single layout
  (`../layouts-and-forms/conditional-fields.md`), so the two mechanisms overlap and a deliberate
  choice is needed — see [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md).
- The naming convention (`LAR …`, `ASR …`, `RPR …`) is **manual discipline, not an enforced
  constraint**. Nothing ties a layout to its Form Type at the picker. This is precisely ASG's
  reported pain point: *"For every step the administrator must manually select the correct Form
  Layouts for both Assignees and Approvers… high cognitive load to keep forms and workflows
  perfectly synchronized"* (feature list line 351). Constrain the picker to layouts whose
  `CodeIssueTypeID` matches the step's Form Type and the pain point disappears.

## 4. The instantiation sequence

**Inferred** from the field split, the FK graph, and S2's per-field definitions. Every numbered
step names the columns it writes so it can be checked against a live capture.

1. A kick-off fires: a form completes, a schedule task completes, or another workflow's action sets
   `KickOffWorkFlowTemplateID`. (**Observed** — `WorkFlowTemplate.KickOffMethod`, S2 line 7292.)
2. Create `WorkFlow`: `WorkFlowTemplateID`, `ProjectEntityID`, `TriggerCodeSQLTableID` +
   `TriggerObjectID`, `KickOffIssueID` *or* `KickOffTaskID`, `InitiatedByMemberID` = current user,
   `WorkFlowCodePriorityID` ← template `DefaultWFCodePriorityID` (or ← parent workflow's priority
   when the spawning action set `PassPriorityToNewWF`), `CreatedDate`, `CodeWorkFlowStatusID` ←
   initial value, `IsCompleted` = false.
3. If `WorkFlowTemplate.AutoAssignInitiator`, set `WorkFlow.AdhocMemberID` = initiator. If the
   spawning action set `PassAdhocToNewWF`, set it from the parent instead.
4. For the template step with the lowest `StepNumber`, create a `WorkFlowStep`: copy the 20 fields
   of §2a, set `WorkFlowTemplateStepID`, `WorkFlowStepName` ← `WorkFlowTemplateStepName`,
   `StartDate` = today, compute `DueDateApprovers` = `StartDate` + `DurationDaysApprovers`,
   `DueDateAssignees` likewise, `DueDate` = the governing one, and the five `Computed*` escalation
   dates from the `DaysUntilWarn*`/`DaysUntilAlert*` offsets.
5. Bind the work object: if `IsFormStep`, create or link the `Issue` and set `IssueID`; else resolve
   `TaskName` to a `Task` on the entity and set `TaskID`. If `SetTaskInProcess`, set that task's
   `CodeTaskStatusID` to In Process. If `AutoAdjustTaskDates`, write the step's dates onto the task.
6. Resolve the three roles (§3); write `ApproverMemberIDList`, `AssigneeMemberIDList`,
   `NotifieeMemberIDList`, `CurrentStepMemberIDList`; create one `WorkFlowStepApprover` and one
   `WorkFlowStepAssignee` row per resolved member with `EMailSentStatus` and
   `NotifyAcknowledgedStatus` unset.
7. If `NotifyStepAssigneesStarted` / `NotifyStepApproversStarted`, send on the channels enabled by
   `EnableForEMail` / `EnableForDashboard`, body `EMailMessage`, link `WFStepNotificationLink`;
   record delivery in each row's `EMailSentStatus`.
8. Steps 4-7 repeat per step as the workflow advances. **Whether later steps are materialised
   eagerly at instantiation or lazily on entry is not determinable from the schema** — this is
   **Open question OQ-10**, and it decides whether `WorkFlowStep` rows exist for steps never
   reached.

## 5. Consequences a rebuild must decide on

| Consequence | Why it follows | Decision needed |
|---|---|---|
| **Live templates are mutable and partially bleed into running instances.** | 35 template-only fields are read through the `WorkFlowTemplateStepID` FK; 20 are frozen. | ASG Edge+ should version templates and pin each `WorkFlow` to a version. That is a deliberate divergence and must be recorded as such, because migrated Lucernex data will not carry a version. |
| **Re-resolution of approvers after a template edit is impossible without re-running resolution.** | The instance keeps only the flat member list. | Decide whether ASG Edge+ stores the resolved set, the rule, or both. |
| **Only one prior round survives.** | Single `Prior*` slot on both `WorkFlowStep` and `WorkFlowStepApprover`. | ASG Edge+ needs an append-only decision log; this is an audit requirement, not a feature request. |
| **The template name is not the instance name.** | No copy path. | Resolve OQ-9 before writing the create path. |
| **Header-level priority is the only true seed.** | `DefaultWFCodePriorityID` → `WorkFlowCodePriorityID`. | Confirm the rename in the UI. |

## Open questions

1. **OQ-9 — What seeds `WorkFlow.WorkFlowName`?** Template name, kick-off form `Subject`, or user
   input? Kick off any workflow from a Contract's **Work Flow** tab and compare the resulting name
   against the template name and the form title. This is a one-line answer that changes the create
   path.
2. **OQ-10 — Are all `WorkFlowStep` rows created up front, or one at a time?** Start a
   three-step workflow and look at the step list on step 1: if steps 2 and 3 are listed with dates,
   materialisation is eager. Determines whether `MoveToStepNumber` jumps to an existing row or
   creates one.
3. **OQ-11 — Does editing a live template change running instances?** Start a workflow, then change
   `AutoLaunchNextStep` and `EMailMessage` on its template's current step, then advance the
   workflow. If the new `AutoLaunchNextStep` takes effect but the old `EMailMessage` is still sent,
   the hybrid model described here is confirmed exactly as stated.
4. **OQ-12 — Is `WorkFlowStepAssignee` created for every resolved assignee, or only on demand?**
   Compare the row count against `WorkFlowStep.AssigneeMemberIDList` length on a live step.
5. **OQ-13 — What does the engine do when a resolved member set is empty?** Configure a step routed
   to a job title nobody on the entity holds and observe: does it block, auto-complete, or fall
   through to `UnassignedApproverID`?
6. **OQ-47 — Are layouts shared across steps, or is the second layout per step the assignee one?**
   §3a offers two readings for `LAR Review Financial Abstract` and the missing
   `Approve … (LA)` layout. Open `Lease Admin Request` step 3 and `Rent Payment Review/Approval`
   step 3 in the step editor and read **both** `Layout To Use With Approvers` and `Layout To Use
   With Assignees`. This also answers **OQ-41** (how assignee routing is configured) from the same
   screen.

   **This cannot be settled offline, and one observation will not settle it either.** The
   layout↔step binding lives in `WorkFlowTemplateStep` *rows*; `all-fields.csv` supplies columns and
   never rows, and neither offline artefact carries instance data — established by the
   reporting-forms agent, who reached the same wall from the layouts side. Worse, because both
   columns are **unconstrained FKs** (`LAY-R-166c`), a layout being shared across steps is
   structurally *permitted* — so seeing sharing once would show it is possible, not that it is the
   rule. **Read both FKs across several steps in at least two workflows** before concluding
   anything about the intended pattern.
