# Workflow & Approvals

*In scope for the rebuild*

Template-driven approval routing: workflow templates and their steps/actions, instantiated workflows, and per-step approvers and assignees.

> Correction, 2026-09-13. This document was written from (ASG)American Freight alone, where > there are 4 workflows and 4 form types. A second tenant, (ASG)BBW, has 13 workflow templates, > 62 steps and 6 form types (../../tenants/bbw-workflow-steps.json), > which refutes the 1:1 Form↔Workflow claim made below and in several sibling files. The > corrected model is in ../../features/workflows-forms/. The > shape findings — step-numbered, ordinal, no branch/merge, layout-per-step — survive the second > tenant unchanged; only the cardinality claims do not. Counts below are AF's, and are correct for AF.

|  | Count |
|---|---|
| Record types | 9 |
| Fields | 262 |
| Keys in | 0 |
| Keys out | 44 |
| Rules | 62 |

## What was found here

### Four workflows are live, one per form type

**Observed.** Lease Admin Request (8 steps), Rent Payment Review/Approval (6), ASC 842 Schedule Review/Approval (3), User Request (2). The Form is the record; the Work Flow is its process; they share a name.

### Lease Admin Request is BRD-24, already implemented

**Observed.** Initial Review, Abstract Lease Document, ASG Review, Client Review, Import Payment History/Sales, Finalize, Finalize (Defaults), Complete. The BRD says what the process should be; this shows what it is.

### A step shows a different screen to a different person

**Observed.** Each workflow step binds its own layout. The same request record presents a different field surface at Submit, at Review and at Approve. That is what makes the engine expressive enough to run a real business process.

### Routing is by position, not by name

**Observed.** Approval Level is Member, Job Title or Ad Hoc. The API's AssigneeType enum goes further: ALL, PARENT, REGION1, REGION2, MARKET, JOB_TITLE. Notifications walk the org chart to three explicit levels.

### Four ways to start a workflow

**Observed.** KickOffMethod: STEP_ACTION, PAGE_LAYOUT, STATUS_CHANGE, TASK. This is the trigger taxonomy any rebuilt rule engine has to reproduce.

### No Task step exists anywhere

**Observed.** All 19 configured steps are Form steps, though 'add task step' exists. WorkFlowTemplateStep has 55 fields and the admin grid surfaces six, so most of the step model is still unseen.

### Workflow status is not a Firm Drop Down

**Observed.** Work Flow Status Code is absent from the catalogue of 207. The nearest that exist are Approval Status Code, Last Action Status Code and Decision Status Code. Where status values actually live is unresolved.

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [WorkFlowTemplateStep](../entities/WorkFlowTemplateStep.md) | `work_flow_template_step` | 55 | 0 |
| [WFStepFullImport](../entities/WFStepFullImport.md) | `w_f_step_full_import` | 47 | 0 |
| [WorkFlowStep](../entities/WorkFlowStep.md) | `work_flow_step` | 47 | 7 |
| [WorkFlowTemplateStepAction](../entities/WorkFlowTemplateStepAction.md) | `work_flow_template_step_action` | 37 | 2 |
| [WorkFlowTemplate](../entities/WorkFlowTemplate.md) | `work_flow_template` | 25 | 0 |
| [WorkFlowStepApprover](../entities/WorkFlowStepApprover.md) | `work_flow_step_approver` | 20 | 1 |
| [WorkFlow](../entities/WorkFlow.md) | `work_flow` | 19 | 5 |
| [WorkFlowStepAssignee](../entities/WorkFlowStepAssignee.md) | `work_flow_step_assignee` | 11 | 0 |
| [CommitteePackage](../entities/CommitteePackage.md) | `committee_package` | 1 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [WF-R-001](../rules/WF-R-001.md) | A. Template definition and availability | WorkFlowTemplateName is required; every save increments RevNumber by one and stamps the modifying member and date. | Observed |
| [WF-R-002](../rules/WF-R-002.md) | A. Template definition and availability | DefaultWFCodePriorityID must be set from Priority Code; every workflow instance inherits it unless a spawning action overrides it. | Observed |
| [WF-R-003](../rules/WF-R-003.md) | A. Template definition and availability | A template restricted by LimitByEntity is offered only for its listed portfolios. The join table that would store which portfolios does not appear anywhere in the 223-object schema — where the restric | Observed |
| [WF-R-004](../rules/WF-R-004.md) | A. Template definition and availability | A user browses forms available on an entity of type T · `CodeIssueType.IsValidFor<T>` · Flag is true · A form of that type may be raised against that entity. Now Observed in the Form Type editor, whic | Observed |
| [WF-R-005](../rules/WF-R-005.md) | A. Template definition and availability | The workflow's own attachability is whatever its kick-off form's Form Type declares. WorkFlowTemplate carries no IsValidFor* columns of its own — the chain runs through PageLayoutID to the layout's Fo | Derived |
| [WF-R-006](../rules/WF-R-006.md) | A. Template definition and availability | A form type is marked as workflow-driving · `CodeIssueType.IsWorkFlow` · true · Forms of this type participate in the workflow engine rather than standing alone · Inferred — no vendor help text for th | Inferred |
| [WF-R-007](../rules/WF-R-007.md) | A. Template definition and availability | StepNumber and WorkFlowTemplateStepName are both required, and the step is ordered within its template by StepNumber. Uniqueness of StepNumber within one template is not enforced by any observed const | Observed |
| [WF-R-008](../rules/WF-R-008.md) | A. Template definition and availability | True selects a Form step, rendering a page layout and collecting a decision; false selects a Task step, working a schedule item with no form surface at all. | Observed |
| [WF-R-009](../rules/WF-R-009.md) | A. Template definition and availability | The principal selector (what kind of thing names the people) and the scope selector (where to search for them) are two independent dimensions, not two rival vocabularies for one idea. A rebuild should | Observed |
| [WF-R-010](../rules/WF-R-010.md) | A. Template definition and availability | Administrator configures a step · `WFTS.ApproverMemberIDList`, `ApproverJobTitleIDList`, `ApproverUserClassIDList`, `WorkFlowTemplateStepMember.OrgChartLevel` · — · `ComputedRequiresApprovers` is true | Observed |
| [WF-R-011](../rules/WF-R-011.md) | A. Template definition and availability | The name is required and free text. This is why ASG reports "there is no obvious, standard Send Back to Previous Step or Request Rework action" — the engine has no notion of a canonical set of actions | Observed |
| [WF-R-012](../rules/WF-R-012.md) | A. Template definition and availability | When present, this JavaScript executes — for conditional kick-off on the template, or as a custom action on a step action. There is no other conditional construct anywhere in the 223-object schema. | Observed |
| [WF-R-013](../rules/WF-R-013.md) | A. Template definition and availability | The 35 template-only fields — routing rules, AutoLaunchNextStep, SetTaskInProcess, SetTaskCanceled, AutoAdjustTaskDates, both NotifyStep*Started flags, and the three header-level Notify*Complete flags | Derived |
| [WF-R-014](../rules/WF-R-014.md) | B. Kick-off and instantiation | A workflow may be kicked off any of four ways per the GraphQL enum. This corrects the vendor help text, which names only three and omits STATUS_CHANGE. | Observed |
| [WF-R-015](../rules/WF-R-015.md) | B. Kick-off and instantiation | When a form matching the configured kick-off layout is completed, a WorkFlow row is created with KickOffIssueID pointing at that form. | Observed |
| [WF-R-016](../rules/WF-R-016.md) | B. Kick-off and instantiation | When the named schedule task completes, a WorkFlow row is created with KickOffTaskID pointing at it. | Observed |
| [WF-R-017](../rules/WF-R-017.md) | B. Kick-off and instantiation | An action with a non-null kick-off target creates a brand-new workflow instance from that template the moment the action fires. No column on the new instance records which parent workflow, step or act | Observed |
| [WF-R-018](../rules/WF-R-018.md) | B. Kick-off and instantiation | WorkFlow.TriggerCodeSQLTableID + TriggerObjectID together read "this workflow was triggered by row TriggerObjectID of table TriggerCodeSQLTableID" — a table-name-plus-primary-key polymorphic reference | Derived |
| [WF-R-019](../rules/WF-R-019.md) | B. Kick-off and instantiation | WorkFlow.WorkFlowCodePriorityID is seeded from the template's DefaultWFCodePriorityID, unless a spawning action overrides it per WF-R-020. | Derived |
| [WF-R-020](../rules/WF-R-020.md) | B. Kick-off and instantiation | If set, the parent workflow's priority overrides the spawned workflow's own template default (WF-R-019). | Observed |
| [WF-R-021](../rules/WF-R-021.md) | B. Kick-off and instantiation | When set, the workflow's initiator is written into WorkFlow.AdhocMemberID at instantiation and used for every later step that declares an ad-hoc assignee. | Observed |
| [WF-R-022](../rules/WF-R-022.md) | B. Kick-off and instantiation | If set, the parent workflow's ad-hoc assignee becomes the ad-hoc assignee of the first step of the newly spawned workflow. | Observed |
| [WF-R-023](../rules/WF-R-023.md) | B. Kick-off and instantiation | InitiatedByMemberID is set to whoever triggered the kick-off. | Observed |
| [WF-R-024](../rules/WF-R-024.md) | B. Kick-off and instantiation | Twenty fields are copied verbatim: StepNumber, TaskName, IsFormStep, Priority, both PageLayout* ids, both Approver/Assignee/Notifiee member lists, both duration pairs, all four warn/alert day-offsets, | Derived |
| [WF-R-025](../rules/WF-R-025.md) | C. Routing resolution | Step instantiation · `WFTS.ApproverType` = Member; `ApproverMemberIDList` · — · `WFS.ApproverMemberIDList` = the named members · Derived | Derived |
| [WF-R-026](../rules/WF-R-026.md) | C. Routing resolution | The step's ApproverJobTitleIDList is intersected against the roster of the entity the workflow is running on, filtered to members holding a matching job title, and the resulting flat member list is fr | Derived |
| [WF-R-027](../rules/WF-R-027.md) | C. Routing resolution | User Class routing resolves against Member.CodeUserClassID intersected with the entity roster; Org Chart Level routing walks Member.SupervisorID the configured number of hops from an anchor that is it | Derived |
| [WF-R-028](../rules/WF-R-028.md) | C. Routing resolution | Step instantiation · `WFTS.ApproverType` = Org Chart Level; `WorkFlowTemplateStepMember.OrgChartLevel`; | Derived |
| [WF-R-029](../rules/WF-R-029.md) | C. Routing resolution | Step instantiation · as WF-R-025…028 for assignees and notifiees · — · `WFS.AssigneeMemberIDList` and `WFS.NotifieeMemberIDList` populated by the same pipeline · Derived | Derived |
| [WF-R-030](../rules/WF-R-030.md) | C. Routing resolution | One WorkFlowStepApprover row per resolved approver, HasTakenAction starting false; one WorkFlowStepAssignee row per resolved assignee, carrying StepMemberResponsibility — described as "lists step memb | Derived |
| [WF-R-031](../rules/WF-R-031.md) | C. Routing resolution | Step instantiation · resolved assignee set · — · One `WFSAs` row per assignee: `MemberID`, `WorkFlowStepID`, `WorkFlowTemplateStepID`, `StepMemberResponsibility` · Derived; `StepMemberResponsibility`  | Derived |
| [WF-R-032](../rules/WF-R-032.md) | C. Routing resolution | Notifiees exist only as the flat WorkFlowStep.NotifieeMemberIDList. No WorkFlowStepNotifiee table exists anywhere in the 223-object schema, so no delivery or acknowledgement is ever tracked for them. | Derived |
| [WF-R-033](../rules/WF-R-033.md) | C. Routing resolution | Step becomes current · `WFS.ApproverMemberIDList`, `AssigneeMemberIDList` · — · `WFS.CurrentStepMemberIDList` = whoever the step is currently waiting on · Observed — "The members associated with the c | Observed |
| [WF-R-034](../rules/WF-R-034.md) | C. Routing resolution | Vendor definition: "When added to a form, this field allows users with appropriate permissions to reassign approvers by job title." Reassignment is a form field an administrator places on a layout, no | Observed |
| [WF-R-035](../rules/WF-R-035.md) | C. Routing resolution | Both this field and Member.IsUnassignedWorkFlowApprover are documented as unimplemented placeholders. | Observed |
| [WF-R-036](../rules/WF-R-036.md) | C. Routing resolution | All eight RunAtStart*/RunAtComplete*/runAt*ScheduledJob* fields are unimplemented; a rebuild should not implement them either, though the naming pattern is worth recording as a design intent that neve | Observed |
| [WF-R-037](../rules/WF-R-037.md) | D. Step execution and dates | Step becomes current · today · — · `WFS.StartDate` = today · Observed — "The date the work flow step started" | Observed |
| [WF-R-038](../rules/WF-R-038.md) | D. Step execution and dates | DueDateApprovers = StartDate + DurationDaysApprovers; DueDateAssignees is computed the same way for the assignee clock; | Observed |
| [WF-R-039](../rules/WF-R-039.md) | D. Step execution and dates | All five Computed*Date fields — warn and alert, for both roles, plus one notification due date — are calculated the moment the step becomes current, from the DaysUntilWarn*/DaysUntilAlert* offsets, an | Derived |
| [WF-R-040](../rules/WF-R-040.md) | D. Step execution and dates | Vendor definition: "set the work flow step status to 'In Process' when the step starts." Whether this writes Task.CodeTaskStatusID or WorkFlowStep.CodeWorkFlowStatusID is contradicted between the fiel | Observed |
| [WF-R-041](../rules/WF-R-041.md) | D. Step execution and dates | When AutoAdjustTaskDates is set, the linked schedule task's dates are rewritten to match the step's own start and due dates. | Observed |
| [WF-R-042](../rules/WF-R-042.md) | D. Step execution and dates | Step start · `WFTS.NotifyStepAssigneesStarted`, `WFS.EnableForEMail`, `EnableForDashboard`, `EMailMessage`, `WFStepNotificationLink` · true · Email/dashboard notification to every assignee; `WFSAs.EMa | Observed |
| [WF-R-043](../rules/WF-R-043.md) | D. Step execution and dates | Step start · `WFTS.NotifyStepApproversStarted` + same channel fields · true · Same, to every approver; `WFSAp.EMailSentStatus` written · Observed | Observed |
| [WF-R-044](../rules/WF-R-044.md) | D. Step execution and dates | Step start · `WFTS.EMailAlertAssignees` / `EMailAlertApprovers` · true · A dashboard alert is sent to the assignee/approver when the task starts · Observed — "send a dashboard alert to the assignee of | Observed |
| [WF-R-045](../rules/WF-R-045.md) | D. Step execution and dates | When an assignee completes the form and presses Submit, SubmitForApprovalByMemberID/Name/Date are set once for the whole step. This is the direct consequence of the approver/assignee asymmetry: assign | Derived |
| [WF-R-046](../rules/WF-R-046.md) | 3. What should deliberately differ | D7 · Policy-driven escalation: notify → reassign to a delegate → escalate to a supervisor → auto-decide, configurable per step. · Requested (feature list line 354). | Derived |
| [WF-R-047](../rules/WF-R-047.md) | D. Step execution and dates | A notification goes to a manager. That is the entire effect. | Observed |
| [WF-R-048](../rules/WF-R-048.md) | D. Step execution and dates | Only the same user or a system administrator can release the lock. This is a directly reported defect: "People check out by mistake all the time… I have to manually navigate to each item and check it  | Derived |
| [WF-R-049](../rules/WF-R-049.md) | E. Approval decisions | Vendor definition: "The approver should select the appropriate action for the work flow step from this field." Selecting an action stamps the button pressed, a comment, the date, and HasTakenAction =  | Observed |
| [WF-R-050](../rules/WF-R-050.md) | E. Approval decisions | Vendor definition of IsApprovalAction: "Specifies whether the current action is an approval or not. If it is not, then the step is either restarted or denied." The engine knows approve vs not-approve  | Observed |
| [WF-R-051](../rules/WF-R-051.md) | E. Approval decisions | Approver acts · `WFTSA.IsApprovalAction` · false · The step is either restarted or denied, per `RestartStep` · Observed — "If it is not, then the step is either restarted or denied" | Observed |
| [WF-R-052](../rules/WF-R-052.md) | E. Approval decisions | RequireApproverSig forces WorkFlowStepApprover.SignatureDate to be captured before the action counts as taken. | Observed |
| [WF-R-053](../rules/WF-R-053.md) | 3. What should deliberately differ | Vendor definition of RequireAllApprovers: "require all qualified approvers on the entity to take the same action on the work flow step for the work flow to progress." If qualified approvers choose dif | Derived |
| [WF-R-054](../rules/WF-R-054.md) | E. Approval decisions | When RequireAllApprovers is false, the first approver to act decides for the whole step. The vendor definition states only the true case, so this reading is Inferred, not confirmed. | Inferred |
| [WF-R-055](../rules/WF-R-055.md) | E. Approval decisions | CodeLastActionStatusID writes Issue.CodeLastActionStatusID and Issue.LastActionStatusChangeDate. This is the only field the engine can write on the record it is routing. | Derived |
| [WF-R-056](../rules/WF-R-056.md) | E. Approval decisions | Vendor definition of DisableEditAfterDecision: "prevents users from making any more changes after the step status is changed to Approved or Denied." This is also the only place in the whole corpus tha | Observed |
| [WF-R-057](../rules/WF-R-057.md) | E. Approval decisions | RestartStep sets WorkFlowStep.IsReDo = true and pushes the current submission round into the single Prior* slot. Only one prior round survives; | Observed |
| [WF-R-058](../rules/WF-R-058.md) | E. Approval decisions | MoveToStepNumber is a plain integer the administrator types in. A lower number is a send-back; | Observed |
| [WF-R-059](../rules/WF-R-059.md) | E. Approval decisions | Vendor definition: "automatically launch the next step if it is a form." Precedence against MoveToStepNumber and RestartStep is unstated (OQ-15, OQ-16). | Observed |
| [WF-R-060](../rules/WF-R-060.md) | E. Approval decisions | NotifyStepAssigneesComplete, NotifyStepApproversComplete, NotifyPriorAssigneesComplete, NotifyPriorApproversComplete and NotifyInitiatorComplete are the complete set. All five share the step's single  | Observed |
| [WF-R-061](../rules/WF-R-061.md) | E. Approval decisions | Action completes · `WFTSA.AutoCopyAmounts`, `PageLayout.IsBudgetImpacting` · true · Budget-impacting values are copied into a custom list on the next step, via the Custom Lists Copy To mechanism. ⊘ Co | Observed |
| [WF-R-062](../rules/WF-R-062.md) | E. Approval decisions | An action with CloseWorkFlow = true sets WorkFlow.IsCompleted, ClosedDate and a terminal CodeWorkFlowStatusID, and fires the three template-level completion notifications read live off WorkFlowTemplat | Observed |
