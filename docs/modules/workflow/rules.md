# Workflow engine — business rules

**Stated up front.** 67 rules, `WF-R-001`…`WF-R-062` plus five live-evidence additions
(`WF-R-004a/b`, `WF-R-009a/b`, `WF-R-014a`), each stated so a rule engine could consume it:
**trigger** (the event), **inputs** (the exact columns read), **condition**, **effect** (the exact
columns written), **confidence**. Rules are grouped by lifecycle phase. Where a rule is Inferred it
is because the schema implies it but no vendor text states it; those rules must not be implemented
without confirming the corresponding open question.

**Two rules changed when live evidence arrived.** `WF-R-014` (kick-off) had **three** methods from
the vendor help text and has **four** from the GraphQL enum — `STATUS_CHANGE` was missing.
`WF-R-009` (routing category) had four categories and now has a reconciled two-dimensional model
plus an `Ad Hoc` escape hatch. Both corrections come from captures written by other agents:
`../layouts-and-forms/forms-vs-pages-vs-layouts.md` and `../../data-model/graphql-api.md`.

**⊘ Scope.** Cost Management and Budgeting are out of scope as of 2026-09-10. One rule
(`WF-R-061`) is marked ⊘ and retained for the structural point it carries; it must not be
implemented. **`Rent Payment Review/Approval` is not affected** — it is a lease-rent process, not
capital-project cost management. Convention explained in [`README.md`](README.md#scope-cost-management-and-budgeting-are-out-of-scope).

**Confidence legend.** **Observed** — the vendor's own field help text in `_xlsx_lucernex_jcrew.txt`
states this, and the quote is given. **Derived** — computed from Observed data, usually a
presence/absence argument over the complete field list. **Inferred** — domain reasoning or naming
convention; not confirmed.

Column references use `Object.Field`. Abbreviations: **WFT** = `WorkFlowTemplate`, **WFTS** =
`WorkFlowTemplateStep`, **WFTSA** = `WorkFlowTemplateStepAction`, **WF** = `WorkFlow`, **WFS** =
`WorkFlowStep`, **WFSAp** = `WorkFlowStepApprover`, **WFSAs** = `WorkFlowStepAssignee`.

---

## A. Template definition and availability

| ID | Trigger | Inputs | Condition | Effect | Confidence |
|---|---|---|---|---|---|
| **WF-R-001** | Administrator saves a workflow template | `WFT.WorkFlowTemplateName` | Name is non-empty | Template is saved; `RevNumber` += 1; `ModifiedByID`/`ModifiedDate` stamped | Observed — `WorkFlowTemplateName` is Required; `RevNumber` *"increases by 1 each time the record is modified"* |
| **WF-R-002** | Administrator saves a template | `WFT.DefaultWFCodePriorityID` | Required | A priority must be chosen from `Priority Code` | Observed — field is Required |
| **WF-R-003** | A user browses available workflows on an entity | `WFT.LimitByEntity`, the (unlocated) portfolio restriction list | `LimitByEntity = 1` | The template is offered only for the listed portfolios; if `0`, for all portfolios | Observed — *"If this value is 1, the work flow template is only available for certain portfolios. If this value is 0, the work flow template is available for all portfolios."* Storage location unknown (OQ-3) |
| **WF-R-004** | A user browses forms available on an entity of type *T* | `CodeIssueType.IsValidFor<T>` | Flag is true | A form of that type may be raised against that entity. **Now Observed in the Form Type editor**, which renders a boolean per entity kind: Portfolio, Capital Program, Prototype, Location, Parcel, Site, Project, Facility, Capital Project, RE Contract, Equipment Contract. Both lease-accounting form types are set `Portfolio = Yes, RE Contract = Yes`, the other nine `No` | Observed — `../layouts-and-forms/forms-vs-pages-vs-layouts.md`; the UI-label→column mapping is Derived (see [`issues-and-tasks.md`](issues-and-tasks.md#codeissuetype--the-form-type-registry-and-the-attachability-model)) |
| **WF-R-004a** | Administrator saves a Form Type | `CodeIssueType.IsWorkFlow` | — | Rendered as **`WORK FLOW field set?`** and set to **Yes for all four live form types**. Every Form Type in this tenant participates in a workflow, and `Manage Forms` and `Manage Work Flows` list exactly the same four names — the relationship is **1:1** | Observed |
| **WF-R-004b** | A request record is created | `CodeIssueType.SequencePrefix`, `IsSequencePerFirm` | — | The record number carries a human-readable prefix — live values `ASR`, `LAR`, `RPR` — and `Global Sequence Numbers?` controls whether numbering is platform-wide or per-scope. **Caution:** the UI label *Global* and the column name *PerFirm* are near-inverses; do not assume they carry the same polarity | Observed (the UI properties and the three prefixes); the column mapping is Derived |
| **WF-R-005** | A workflow template is bound to a kick-off form | `WFT.PageLayoutID` → `PageLayout.CodeIssueTypeID` → `CodeIssueType.IsValidFor*` | — | The workflow's attachability is that of its kick-off form's type. `WorkFlowTemplate` itself carries no `IsValidFor*` columns | Derived |
| **WF-R-006** | A form type is marked as workflow-driving | `CodeIssueType.IsWorkFlow` | true | Forms of this type participate in the workflow engine rather than standing alone | Inferred — no vendor help text for this column |
| **WF-R-007** | Administrator adds a step | `WFTS.StepNumber`, `WFTS.WorkFlowTemplateStepName` | Both Required | Step is ordered within the template by `StepNumber`. **Uniqueness of `StepNumber` within a template is not enforced by any observed constraint** | Observed (Required flags); uniqueness Inferred |
| **WF-R-008** | Administrator configures a step | `WFTS.IsFormStep` | — | The step is a **Form step** (true) or a **Task step** (false) | Observed — *"This field has one of two values: Form Step or Task Step."* |
| **WF-R-009** | Administrator configures a step | `WFTS.ApproverType`/`AssigneeType`/`NotifieeType` | — | Selects the routing category. Authoritative form is the GraphQL enum `MemberNotifyType: [ORGCHART_ALL, ORGCHART_LEV1, ORGCHART_LEV2, ORGCHART_LEV3, ORGCHART_MKT, USERCLASS, JOBTITLE, MEMBERID]` — the vendor help's four categories, with org-chart depth bounded at three explicit levels. The live UI renders the column as **Approval Level** and adds a fifth value the schema does not name: **Ad Hoc** | Observed (both enums and the UI); the mapping between them is Derived — see [`routing-and-approvals.md` §2](routing-and-approvals.md#2-three-competing-routing-vocabularies-reconciled) and OQ-8 |
| **WF-R-009a** | Administrator configures a step | GraphQL `AssigneeType: [ALL, PARENT, REGION1, REGION2, MARKET, JOB_TITLE]` | — | Selects the **scope** to search for the principal — all entities, the parent entity, region level 1 or 2, or market. This is a second, orthogonal dimension to WF-R-009, not a rival vocabulary: `PARENT`/`REGION1`/`REGION2`/`MARKET` are all `ProjectEntity` hierarchy concepts (`RegionID`, `RootRegionID`, `SubRegionID`, `CodeMarketAreaID`) | Observed (the enum); the scope reading is Derived (OQ-40) |
| **WF-R-009b** | Administrator configures a step | `WorkFlowTemplateStepMember.IsAdhoc` | Approval Level = **Ad Hoc** | The step names no principal at design time; one is chosen at runtime from `WorkFlow.AdhocMemberID` / `Issue.WorkFlowAdhocMemberID`. The live grid shows an **empty `Approver` column** for both Ad Hoc steps, which is the observable signature | Observed (the category and the empty column) + Derived (the columns) |
| **WF-R-010** | Administrator configures a step | `WFTS.ApproverMemberIDList`, `ApproverJobTitleIDList`, `ApproverUserClassIDList`, `WorkFlowTemplateStepMember.OrgChartLevel` | — | `ComputedRequiresApprovers` is true iff the step requires approvers; `ComputedRequiresAssignees` likewise | Observed — *"The value of this field is true if the work flow step requires approvers."* Derivation rule itself unstated |
| **WF-R-010a** | Administrator binds a layout to a step | `WFTS.PageLayoutApproversID`, `WFTS.PageLayoutAssigneesID`, `PageLayout.CodeIssueTypeID` | — | The step renders **one layout per role**. A Form type therefore owns many layouts, one per step per role, named after the step (`LAR Initial Review of Lease Admin Request`, `LAR Abstract Lease Document`, …). The same record shows a different field surface at each stage to each audience. The live grid renders the bound layout suffixed **`(Approvers)`**, confirming the approver layout is per-step; the assignee layout exists but is not on that screen | Observed — `../layouts-and-forms/forms-vs-pages-vs-layouts.md` |
| **WF-R-010b** | Administrator binds the kick-off layout | `WFT.PageLayoutID` | — | The template's own layout is the **Submit** form. Live: `ASR Submit ASC 842 Schedules`, `LAR Submit Lease Admin Request`, `RPR Submit Rent Preview File` — one per workflow, matching the vendor definition *"Select the form whose completion you want to have kick off this work flow"*. ASC 842 has 4 layouts for 3 steps and Lease Admin Request 9 for 8, i.e. **N + 1**, the extra being Submit | Observed (the layout names) + Derived (the N+1 arithmetic) |
| **WF-R-011** | Administrator saves an action | `WFTSA.WorkFlowTemplateStepActionName` | Required | The name is the button label shown to approvers. **There is no controlled vocabulary** — no code table constrains it | Observed (Required) + Derived (no FK) |
| **WF-R-012** | Template or action is saved with JavaScript | `WFT.IsEnabledLxJSCode`, `WFTSA.IsEnabledLxJSCode` | Non-empty | Custom JavaScript executes — for conditional kick-off (template) or as a custom action (action). **This is the engine's only conditional-logic mechanism** | Observed — *"custom JavaScript used to kick off conditional work flows"* / *"If you are creating a custom action using JavaScript, enter the JavaScript in this field."* |
| **WF-R-013** | Template is edited while instances are running | `WFS.WorkFlowTemplateStepID` | — | The 35 template-only fields (routing rules, `AutoLaunchNextStep`, `SetTaskInProcess`, `SetTaskCanceled`, `AutoAdjustTaskDates`, `NotifyStep*Started`, the three `WFT.Notify*Complete` flags) are **read live** and therefore change running instances. The 20 snapshotted fields do not | Derived — set difference; confirm via OQ-11 |

## B. Kick-off and instantiation

| ID | Trigger | Inputs | Condition | Effect | Confidence |
|---|---|---|---|---|---|
| **WF-R-014** | Any of **four** events | `WFT.KickOffMethod` | — | A workflow may be kicked off four ways, per the GraphQL enum `KickOffMethod: [STEP_ACTION, PAGE_LAYOUT, STATUS_CHANGE, TASK]`: **(a)** `STEP_ACTION` — an action on a preceding workflow step; **(b)** `PAGE_LAYOUT` — completion of a form / a button on a layout; **(c)** `STATUS_CHANGE` — a record's status changing; **(d)** `TASK` — completion of a schedule task | **Observed** — `../../data-model/graphql-api.md`. **Corrects** the vendor help text, which names only three and omits `STATUS_CHANGE`: *"There are three ways a work flow can be kicked off: by completion of an action in another work flow, by completion of a schedule task, or by completion of a form."* |
| **WF-R-014a** | A watched record's status changes | `WFT.StatusChangeID`, `WFT.StatusChangeType` | `KickOffMethod = STATUS_CHANGE` | A `WF` row is created. These two columns are the configuration for the fourth kick-off method — the only reading that explains them, since no vendor help text does | Derived, from the `KickOffMethod` enum plus the two otherwise-unexplained columns |
| **WF-R-015** | A form of the configured layout is completed | `WFT.PageLayoutID`, the completed `Issue` | Layout matches | A `WF` row is created with `KickOffIssueID` = the form | Observed — *"Select the form whose completion you want to have kick off this work flow"* / *"The ID of the form that kicked off the work flow"* |
| **WF-R-016** | A schedule task is completed | `WFT.TaskName`, the completed `Task` | Name matches | A `WF` row is created with `KickOffTaskID` = the task | Observed — *"Select the schedule task whose completion you want to have kick off this work flow"* / *"The ID of the schedule task that kicked off the work flow"* |
| **WF-R-017** | An action with a kick-off target completes | `WFTSA.KickOffWorkFlowTemplateID` | Non-null | A new `WF` is created from that template. **No column on the new instance records the parent workflow, step or action** | Observed (the kick-off) + Derived (the missing parent pointer — OQ-5) |
| **WF-R-018** | Workflow instantiation | `WF.TriggerCodeSQLTableID`, `WF.TriggerObjectID` | — | The instance is bound polymorphically to the triggering record: table name + primary key | Derived — `sCODE_SQLTABLE` is the platform table registry; catalog-only columns (OQ-1) |
| **WF-R-019** | Workflow instantiation | `WFT.DefaultWFCodePriorityID` | — | `WF.WorkFlowCodePriorityID` is seeded from the template default | Derived — identical `sCODE_PRIORITY` type, "Default" prefix |
| **WF-R-020** | Workflow instantiation by a spawning action | `WFTSA.PassPriorityToNewWF` | true | The **parent** workflow's `WorkFlowCodePriorityID` overrides WF-R-019 | Observed — *"transfer the priority level of this work flow to a new work flow that is kicked off by this step"* |
| **WF-R-021** | Workflow instantiation | `WFT.AutoAssignInitiator`, current user | true | `WF.AdhocMemberID` = the initiator, applied to the kick-off step/form **and to every later step that requires an ad-hoc assignee** | Observed — full quote in `routing-and-approvals.md` §5 |
| **WF-R-022** | Workflow instantiation by a spawning action | `WFTSA.PassAdhocToNewWF` | true | The parent's `AdhocMemberID` is assigned to the **first** step of the new workflow | Observed — *"assign the ad hoc member assigned to this task to the first task in the new work flow kicked off by this step"* |
| **WF-R-023** | Workflow instantiation | `WF.InitiatedByMemberID` | — | Set to the member who triggered the kick-off | Observed — *"The member ID of the user who initiated the work flow"* |
| **WF-R-024** | Step instantiation | `WFTS` → `WFS` | — | Exactly 20 configuration fields are copied: `StepNumber`, `TaskName`, `IsFormStep`, `Priority`, `PageLayoutApproversID`, `PageLayoutAssigneesID`, `ApproverMemberIDList`, `AssigneeMemberIDList`, `NotifieeMemberIDList`, `DurationDaysApprovers`, `DurationDaysAssignees`, `DaysUntilWarnApprovers`, `DaysUntilWarnAssignees`, `DaysUntilAlertApprovers`, `DaysUntilAlertAssignees`, `EMailAlertApprovers`, `EMailAlertAssignees`, `EnableForEMail`, `EnableForDashboard`, `EMailMessage`. `WFS.WorkFlowStepName` ← `WFTS.WorkFlowTemplateStepName` under a renamed column | Derived (set intersection) + Observed (*"The name of the work flow step from the work flow template"*) |

## C. Routing resolution

| ID | Trigger | Inputs | Condition | Effect | Confidence |
|---|---|---|---|---|---|
| **WF-R-025** | Step instantiation | `WFTS.ApproverType` = Member; `ApproverMemberIDList` | — | `WFS.ApproverMemberIDList` = the named members | Derived |
| **WF-R-026** | Step instantiation | `WFTS.ApproverType` = Job Title; `ApproverJobTitleIDList`; `LinkMemberProjectEntity` for `WF.ProjectEntityID`; `Member.CodeJobTitleID`/`CodeJobTitleIDList` | — | `WFS.ApproverMemberIDList` = every member on the entity holding one of the listed titles | Derived; corroborated by Observed *"The Job Title is used when auto-assigning things like tasks, work flow steps, and notifications"* |
| **WF-R-027** | Step instantiation | `WFTS.ApproverType` = User Class; `ApproverUserClassIDList`; `Member.CodeUserClassID` | — | `WFS.ApproverMemberIDList` = every member on the entity in one of the listed classes | Derived |
| **WF-R-028** | Step instantiation | `WFTS.ApproverType` = Org Chart Level; `WorkFlowTemplateStepMember.OrgChartLevel`; `Member.SupervisorID` | — | `WFS.ApproverMemberIDList` = members *n* supervisor-hops from an anchor. **The anchor is unspecified** | Derived + OQ-22 |
| **WF-R-029** | Step instantiation | as WF-R-025…028 for assignees and notifiees | — | `WFS.AssigneeMemberIDList` and `WFS.NotifieeMemberIDList` populated by the same pipeline | Derived |
| **WF-R-030** | Step instantiation | resolved approver set | — | One `WFSAp` row per approver: `MemberID`, `WorkFlowStepID`, `WorkFlowTemplateStepID`, `HasTakenAction = false` | Derived |
| **WF-R-031** | Step instantiation | resolved assignee set | — | One `WFSAs` row per assignee: `MemberID`, `WorkFlowStepID`, `WorkFlowTemplateStepID`, `StepMemberResponsibility` | Derived; `StepMemberResponsibility` *"lists step members whose responsibility matches the responsibility for the workflow template step"* (Observed) |
| **WF-R-032** | Step instantiation | resolved notifiee set | — | **No per-person row is created.** Notifiees exist only as `WFS.NotifieeMemberIDList`; no delivery or acknowledgement is tracked for them | Derived — no `WorkFlowStepNotifiee` object exists |
| **WF-R-033** | Step becomes current | `WFS.ApproverMemberIDList`, `AssigneeMemberIDList` | — | `WFS.CurrentStepMemberIDList` = whoever the step is currently waiting on | Observed — *"The members associated with the current workflow step"*; the exact derivation is unstated |
| **WF-R-034** | A user with permission edits a reassignment field on a form | `WFTS.ReassignApproversJobTitleIDList` / `ReassignAssigneesJobTitleIDList` | The field is present on the layout **and** the user has the permission | Approvers/assignees are reassigned **by job title only**. Whether the change persists to the template or only to the running step is unresolved | Observed — *"When added to a form, this field allows users with appropriate permissions to reassign approvers by job title"*; persistence per OQ-26 |
| **WF-R-035** | — | `WFTS.UnassignedApproverID`, `Member.IsUnassignedWorkFlowApprover` | — | **No effect.** Both are documented as *"a placeholder for an upcoming feature"* | Observed |
| **WF-R-036** | — | `WFTS.RunAtStartApprover1ID`, `RunAtStartApprover2ID`, `RunAtCompleteApprover1ID`, `RunAtCompleteApprover2ID`, and the four catalog-only `runAt*ScheduledJob*` fields | — | **No effect.** All eight are unimplemented placeholders | Observed (four of them explicitly); Derived (the four with no physical column) |

## D. Step execution and dates

| ID | Trigger | Inputs | Condition | Effect | Confidence |
|---|---|---|---|---|---|
| **WF-R-037** | Step becomes current | today | — | `WFS.StartDate` = today | Observed — *"The date the work flow step started"* |
| **WF-R-038** | Step start | `WFS.StartDate`, `DurationDaysApprovers`, `DurationDaysAssignees` | — | `WFS.DueDateApprovers` = start + approver duration; `DueDateAssignees` = start + assignee duration; `DueDate` = the governing one | Observed — all three are *"Calculates the due date of the work flow step…"*; the arithmetic and which one governs are Derived |
| **WF-R-039** | Step start | `WFS.DaysUntilWarnApprovers`/`Assignees`, `DaysUntilAlertApprovers`/`Assignees`, `WFTS.DaysUntilNotification` | — | The five hidden dates are materialised: `ComputedWarnDateApprovers`, `ComputedWarnDateAssignees`, `ComputedAlertDateApprovers`, `ComputedAlertDateAssignees`, `ComputedDueDateNotification` | Derived — matching name pairs |
| **WF-R-040** | Step start | `WFTS.SetTaskInProcess`, `WFS.TaskID` | true | Status set to **"In Process"**. Whether this writes `Task.CodeTaskStatusID` or `WFS.CodeWorkFlowStatusID` is contradicted between the field label and its definition | Observed (the value and the flag); target per OQ-29 |
| **WF-R-041** | Step start | `WFTS.AutoAdjustTaskDates`, `WFS.StartDate`/`DueDate`, `WFS.TaskID` | true | The linked task's dates are adjusted to match the step's | Observed — *"automatically adjust the task dates to match the step durations"* |
| **WF-R-042** | Step start | `WFTS.NotifyStepAssigneesStarted`, `WFS.EnableForEMail`, `EnableForDashboard`, `EMailMessage`, `WFStepNotificationLink` | true | Email/dashboard notification to every assignee; `WFSAs.EMailSentStatus` written | Observed |
| **WF-R-043** | Step start | `WFTS.NotifyStepApproversStarted` + same channel fields | true | Same, to every approver; `WFSAp.EMailSentStatus` written | Observed |
| **WF-R-044** | Step start | `WFTS.EMailAlertAssignees` / `EMailAlertApprovers` | true | A **dashboard alert** is sent to the assignee/approver when the task starts | Observed — *"send a dashboard alert to the assignee of this task when the task starts"* |
| **WF-R-045** | Assignee completes and submits the form | `ProjectEntity.FormSubmitButton`, current user, today | — | `WFS.SubmitForApprovalByMemberID`, `SubmitForApprovalByMemberName`, `SubmitForApprovalDate` set. **One stamp per step, not per assignee** | Derived — the three columns exist and `WFSAs` has no submission columns |
| **WF-R-046** | System date reaches `ComputedWarnDate*` | — | Step not complete | Notification to the **actor** (approver or assignee). **No state change** | Observed — *"before an approver receives a notification that this step has not been completed"* |
| **WF-R-047** | System date reaches `ComputedAlertDate*` | — | Step not complete | Notification to a **manager**. **No state change, no reassignment, no auto-decision** | Observed — *"before a manager is notified that this step has not been completed"* |
| **WF-R-048** | User presses Checkout on a step or form | current user, today | — | `CheckedOutByMemberID`, `CheckedOutDate` set. **No expiry exists**; only the same user or a sysadmin can release it | Derived (columns) + Observed (behaviour, feature list line 363) |

## E. Approval decisions

| ID | Trigger | Inputs | Condition | Effect | Confidence |
|---|---|---|---|---|---|
| **WF-R-049** | Approver selects an action | `WFTSA.WorkFlowTemplateStepActionID`, comment, today | The member has a `WFSAp` row for this step | `WFSAp.WorkFlowTemplateStepActionID`, `ActionTakenName`, `ActionTakenDate`, `ActionComment`, `HasTakenAction = true` | Observed — *"The approver should select the appropriate action for the work flow step from this field"* |
| **WF-R-050** | Approver acts | `WFTSA.IsApprovalAction` | true | `WFSAp.HasApproved = true` | Observed — *"Specifies whether the current action is an approval or not"* |
| **WF-R-051** | Approver acts | `WFTSA.IsApprovalAction` | false | The step is **either restarted or denied**, per `RestartStep` | Observed — *"If it is not, then the step is either restarted or denied"* |
| **WF-R-052** | Approver acts | `WFTSA.RequireApproverSig` | true | `WFSAp.SignatureDate` must be captured | Observed — *"require an approver signature for an action on a work flow step"* |
| **WF-R-053** | Approver acts | `WFTSA.RequireAllApprovers`, all `WFSAp` rows | true | The workflow advances only when **all qualified approvers on the entity have taken the same action**. If they choose different actions the condition is unsatisfiable and the step **deadlocks with no recovery path** | Observed (the rule) + Observed (the failure, feature list line 362) |
| **WF-R-054** | Approver acts | `WFTSA.RequireAllApprovers` | false | The first approver to act decides | Inferred — the definition states only the true case |
| **WF-R-055** | Action completes | `WFTSA.CodeLastActionStatusID` | Non-null | `Issue.CodeLastActionStatusID` = the value; `Issue.LastActionStatusChangeDate` = today. **This is the engine's only field-write capability** | Derived — matching type on `Issue` plus its paired change-date column |
| **WF-R-056** | Action completes | `WFTSA.DisableEditAfterDecision` | true | `WFS.IsReadOnly = true`; no further edits after the status becomes **Approved** or **Denied** | Observed |
| **WF-R-057** | Action completes | `WFTSA.RestartStep` | true | `WFS.IsReDo = true`; the current round is pushed to `WFS.PriorSubmitByMemberID`/`PriorSubmitForApprovalDate` and `WFSAp.PriorActionComment`/`PriorActionTakenDate`/`PriorWFTemplateStepActionID`. **Only one prior round is retained; a third round overwrites the second** | Observed (the flag and `IsReDo`) + Derived (the single `Prior*` slot) |
| **WF-R-058** | Action completes | `WFTSA.MoveToStepNumber` | Non-null | The workflow moves to the step with that `StepNumber`. A lower number is a send-back; nothing distinguishes it from forward movement | Observed |
| **WF-R-059** | Action completes | `WFTS.AutoLaunchNextStep` | true **and** the next step is a Form step | The next step launches automatically. Precedence against `MoveToStepNumber` is unstated | Observed — *"automatically launch the next step **if it is a form**"*; precedence per OQ-16 |
| **WF-R-060** | Action completes | `WFTSA.NotifyStepAssigneesComplete`, `NotifyStepApproversComplete`, `NotifyPriorAssigneesComplete`, `NotifyPriorApproversComplete`, `NotifyInitiatorComplete` | each true | Email to that audience, using the step's single `EMailMessage` body and its two channel switches. **These five are the complete audience model; notifiees are not among them** | Observed (all five) + Derived (the absence of notifiees) |
| **WF-R-061** ⊘ | Action completes | `WFTSA.AutoCopyAmounts`, `PageLayout.IsBudgetImpacting` | true | Budget-impacting values are copied into a custom list on the **next** step, via the Custom Lists **Copy To** mechanism. **⊘ Cost Management is out of scope — do not implement.** Retained because it is the engine's *only* step-to-step data-flow mechanism, so its narrowness is the finding: ASG Edge+ must design step-to-step data flow from scratch | Observed |
| **WF-R-062** | Action completes | `WFTSA.CloseWorkFlow` | true | `WF.IsCompleted = true`, `WF.ClosedDate` = today, terminal `WF.CodeWorkFlowStatusID`; `WFT.NotifyInitiatorComplete`, `NotifyAllApproversComplete`, `NotifyAllAssigneesComplete` fire (read live off the template) | Observed |

---

## Rules that do **not** exist

Stating the absences is as important as stating the rules, because a rebuild will otherwise
"helpfully" add them and diverge. Every row is **Derived** by exhaustive inspection of the complete
field lists for `WFT`, `WFTS`, `WFTSA`, `WF`, `WFS`, `WFSAp` and `WFSAs`.

| Absent rule | Evidence of absence |
|---|---|
| Conditional branching on data | No condition, expression, predicate or criteria column on any of the seven objects. Only `IsEnabledLxJSCode`. |
| Amount-banded approval routing | `Member.PaymentApprovalMinAmount`/`MaxAmount`, `RecurringApprovalMinAmount`/`MaxAmount` and the two `Equip*` pairs exist, and **no workflow column references them** (OQ-19). **In scope** — this is about lease and rent payment approvals, not capital-project Cost Management. |
| Sequential / tiered approval | No order, sequence, tier or level column on `WFSAp`. |
| Partial quorum ("2 of 3") | `RequireAllApprovers` is Boolean. No threshold or count column. |
| Tie-break on conflicting approver actions | None. Directly produces the observed deadlock. |
| Delegation / out-of-office | No delegate, proxy or substitute column anywhere. |
| Timer-driven state change | `DaysUntilWarn*`/`DaysUntilAlert*` only send notifications; no auto-approve, auto-deny, auto-advance or auto-reassign. |
| Auto-escalation by reassignment | Reassignment is a manual form field (`Reassign*JobTitleIDList`). |
| Parallel branches, fork or join | One `WorkFlow` has one current step. No branch, fork, join or gateway object. |
| Workflow-step predecessors | `TaskPredecessor` exists for the schedule; no equivalent for workflow steps. |
| Parent pointer on a spawned workflow | No `ParentWorkFlowID` on `WorkFlow`. |
| Return value from a spawned workflow | No callback, result or completion pointer. |
| More than one round of approval history | Single `Prior*` slot on both `WFS` and `WFSAp`. |
| External / API call from a step | No endpoint, URL, webhook or integration column. |
| Scheduled job at step start or end | The four `runAt*ScheduledJob*` fields are catalog-only placeholders. |
| Arbitrary field write | Only `CodeLastActionStatusID`. |
| Suspend / resume / hold | `Inactive` is a soft delete of the instance, not a pause. |
| Withdraw by the initiator | Closing requires an approver to press an action with `CloseWorkFlow`. |
| Template versioning | `RevNumber` is a modification counter. No version, draft/published state or effective date. |
| Notification templating | One free-text `EMailMessage` per step. No subject, no merge fields, no per-audience body. |
| Per-notifiee delivery tracking | No `WorkFlowStepNotifiee` table. |
| Checkout expiry | No expiry column on either `CheckedOut*` pair. |
| Terminal-state consistency constraint | `IsCompleted`, `ClosedDate` and `CodeWorkFlowStatusID` are three independent columns. |

---

## Open questions

Consolidated from every document in this folder, ranked by how much a wrong answer costs the
rebuild. Each names exactly what to check in the live UI.

| Rank | ID | Question | Where to look |
|---:|---|---|---|
| 1 | **OQ-7** (re-routed) | What are the values of `Work Flow Status Code`? **It is not one of the 207 platform code tables** — introspect `codeWorkFlowStatusID` via GraphQL instead. `Last Action Status Code`, `Task Status Code`, `Priority Code` and `Task Lead Lag Type Code` **are** in the catalogue. | GraphQL Explorer for workflow status; **Manage Firm Drop Downs** `/en/admin/FirmCodeList.jsp` for the other four |
| 2 | **OQ-43** | **Open the action editor.** `WorkFlowTemplateStepAction` has never been rendered in any capture, and it holds the entire control-flow, quorum, signature, sub-workflow and status-write model. One screen converts [`step-actions.md`](step-actions.md) from Derived to Observed and answers OQ-14, OQ-15, OQ-16, OQ-20 and OQ-37 at once. | **Manage Work Flows** → `Rent Payment Review/Approval` → step 2 or 3 → its actions |
| 3 | **OQ-44** | Is the observed linearity real, or an artefact of a grid with no column for a jump target? Record every `MoveToStepNumber` on the live actions. | Same screen; also `Lease Admin Request` steps 6-7 |
| 4 | **OQ-19** | How is amount-banded approval routing done? `Member` has eight approval-limit currency columns that no workflow field reads. `Rent Payment Review/Approval` is where banding would be expected. | **Manage Work Flows** → a payment-approval step; then **Member Administration** → a member's approval limits |
| 5 | **OQ-1** | Are `WorkFlow.TriggerCodeSQLTableID` / `TriggerObjectID` real stored columns? They are the only edge from a running workflow to its business record. | A Contract's **Work Flow** tab, on a live instance |
| 6 | **OQ-2 / OQ-8** | Does `WorkFlowTemplateStepMember` exist? Is *Org Chart Level* selectable as an Approver Type, and what integers do the four categories take? | **Manage Work Flows** → a step → approver configuration |
| 7 | **OQ-16 / OQ-15** | Precedence between `MoveToStepNumber`, `AutoLaunchNextStep` and `RestartStep`. | Configure conflicting values on one action and fire it |
| 8 | **OQ-14** | Does `RequireAllApprovers` mean all qualified approvers **on the entity** (re-resolved at decision time) or all approvers **on the step** (frozen)? | Add a matching-title member to the entity after the step starts, then try to complete it |
| 9 | **OQ-11** | Does editing a live template change running instances? | Change `AutoLaunchNextStep` and `EMailMessage` mid-flight and advance the workflow |
| 10 | **OQ-5** | Can a spawned workflow be traced to its parent? | Fire a `KickOffWorkFlowTemplateID` action and inspect the new instance |
| 11 | **OQ-29** | Do `SetTaskInProcess` / `SetTaskCanceled` write `Task.CodeTaskStatusID` or `WorkFlowStep.CodeWorkFlowStatusID`? Label and definition contradict. | A task step with both flags; read the linked task's status |
| 12 | **OQ-10** | Are all `WorkFlowStep` rows created eagerly at instantiation, or lazily on entry? | The step list on step 1 of a three-step workflow |
| 13 | **OQ-34** | How is a step cancelled? No action field expresses cancel. | The step UI on a running workflow |
| 14 | **OQ-9** | What seeds `WorkFlow.WorkFlowName`? | Compare a new instance's name against the template name and the kick-off form title |
| 15 | **OQ-26** | Does form-level reassignment write back to the template or only to the running step? | Reassign on a live step, then re-open the template step |
| 16 | **OQ-25** | Do workflow SLA days honour working days and `HolidaySchedule`? | Set a 5-day duration on a Thursday and read `DueDateApprovers` |
| 17 | **OQ-17** | Do step-level notifiees and action-level `Notify*Complete` both fire? | **Email Log** `/en/reports/EMailLogs.jsp` after firing an action |
| 18 | **OQ-3** | Where is `LimitByEntity`'s portfolio list stored? | Tick *Limit By Entity* and observe the control that appears |
| 19 | **OQ-37** | What closes a workflow whose last step completes without a `CloseWorkFlow` action? | Run a two-step template with no closing action to the end |
| 20 | **OQ-22 / OQ-23** | Org Chart Level is relative to whom, and which manager receives the alert — `LinkMemberProjectEntity.IsManager`, `ProjectEntity.ManagerIDList`, or `Member.SupervisorID`? | Configure a level and observe who resolves; let a step breach its alert date |
| 21 | **OQ-38** | Is there a step-level audit trail beyond the single `Prior*` slot? Decides whether history can be migrated at all. | **Audit Reports**; the per-record **Audit Log** popup on a workflow step |
| 22 | **OQ-24** | `CodeJobTitleIDList` vs `AssignedCodeJobTitleIDList` on `LinkMemberProjectEntity` — which does job-title routing use? | A Contract's **Members/Contacts** tab vs Member Administration |
| 23 | **OQ-30 / OQ-31** | Does the workflow create the `Issue` or attach to an existing one, and how does a Task step differ from a Form step in the UI? | Kick off a workflow; watch the entity's **Forms** tab |
| 24 | **OQ-33** | Do `WorkOrder.ApproverMemberID` and `ServiceRequest.ApproverPartyID` bypass the workflow engine entirely? If so there are two approval systems. | A Work Order and a Service Request record |
| 25 | **OQ-27** | What happens to a running workflow when a routed member is deactivated? | Deactivate a member who is the sole approver on a live step |
| 26 | **OQ-18 / OQ-21 / OQ-35 / OQ-36 / OQ-39 / OQ-6 / OQ-4 / OQ-20 / OQ-28 / OQ-32 / OQ-12 / OQ-13** | The remaining lower-cost ambiguities — the three kick-off ID columns, `AutoClearAmounts`, the two free-text status columns, workflow-vs-step status, whether **Manage Forms** writes `CodeIssueType`, `IsWorkFlow`, `StepMemberResponsibility`, the action-name vocabulary, the lead/lag types, which `IsValidFor*` flags ASG uses, `IsNotifyClosed`, and the empty-resolved-set behaviour. | Detailed in the `## Open questions` section of each document in this folder |
