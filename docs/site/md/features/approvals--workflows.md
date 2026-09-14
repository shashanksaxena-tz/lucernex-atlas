# Approvals & Workflows

The approval machinery. Four workflows are live in this tenant, one per form type: Lease Admin Request (8 steps), Rent Payment Review/Approval (6), ASC 842 Schedule Review/Approval (3), and User Request (2). The request is the record; the workflow is its process; they share a name.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Everyone who submits a request and everyone who approves one. Routing is by position — a member, a job title, or ad hoc — not by named person.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

A different page layout per workflow step, so the same request presents a different screen to the submitter and to each approver.

## BRD-24, already live

*Observed · capability · source: `docs/modules/workflow/README.md`*

Lease Admin Request is BRD-24, already implemented: Initial Review, Abstract Lease Document, ASG Review, Client Review, Import Payment History/Sales, Finalize, Finalize (Defaults), Complete. The BRD describes what the process should be; this shows what it actually is.

## Per-step layouts

*Observed · capability · source: `Live capture, Manage Work Flows`*

Each step shows a different screen: a workflow step binds its own page layout, so the same request presents a different field surface at Submit, at Review and at Approve. That per-step binding is what makes the engine expressive enough to run a real business process.

## Position-based routing

*Observed · capability · source: `docs/modules/workflow/`*

Routing is by position, not by person: approval level is a member, a job title, or ad hoc - and the API's assignee enum goes further (all, parent, region 1, region 2, market, job title). Notifications walk the org chart to three explicit levels, and routing resolves through the geographic region hierarchy, not the supervisor chain.

## Four kick-off triggers

*Observed · capability · source: `docs/modules/workflow/`*

A workflow can start four ways: from a step action, from a page layout, on a status change, or from a task. This is the trigger taxonomy any rebuilt rule engine has to reproduce.

## Nested state machines

*Derived · capability · source: `docs/modules/workflow/README.md`*

The module documents three nested state machines: template lifecycle, instance lifecycle, and per-step transitions, split cleanly into template versus instance.

## No Task steps exist

*Observed · fact*

No task step exists anywhere in this tenant: all 19 configured steps are form steps, though 'add task step' exists in the product. The step record has 55 fields and the admin grid surfaces six - most of the step model is still unseen.

## Status home unknown

*Observed · fact*

Where workflow status lives is unresolved: 'Work Flow Status Code' is absent from the catalogue of 207 firm-wide value lists. The nearest that exist are approval, last-action and decision status codes.

## Workflows Forms

*Observed · fact · source: `docs/features/workflows-forms/README.md`*

What the workflows forms manual settles: Corrects the 1:1 Form↔Workflow claim — true in AF, false in BBW (4 of 13 match). Versioning is by name suffix. Two JavaScript escape hatches. Biggest open question: Which Lease Admin Request variant is live.

## Manual contents

*Observed · fact · source: `docs/features/workflows-forms/README.md`*

The workflows forms manual is organised as: The 13 BBW workflow templates; Workflows are tenant-authored — they do not fork from a published set; Versioning by name suffix; What the second tenant does not change; Two mechanisms only BBW shows; Routing — a correction carried forward; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Evidence

*Observed · fact · source: `features/workflows-forms/README.md`*

Written up in features/workflows-forms/README.md. 4 screen captures on disk, under docs/assets/screenshots/workflow, docs/assets/screenshots/forms — the screens themselves, not a description of them. 4 of them are cited by name in the documentation, which is what ties a capture to the screen it shows. Admin tools documented here, each with the capture named after it: Manage Forms, Manage Work Flows.

![Manage Work Flow expanded — every step of every workflow](../../assets/screenshots/workflow/manage-workflow-expanded-all-steps.jpg)
![Manage Work Flow — the same four names as Manage Forms](../../assets/screenshots/workflow/manage-workflow-index.jpg)
![Manage Forms expanded — every form type's layouts](../../assets/screenshots/forms/manage-forms-expanded-all-layouts.jpg)
![Manage Forms — four form types, each with edit fields and add layout](../../assets/screenshots/forms/manage-forms-index.jpg)

## Open questions (67)

*Inferred · group*

67 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Everything in rules md

*Inferred · question · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

Everything in rules.md — in particular OQ-43 (open the action editor), OQ-7 (the status code values), OQ-44 (is the linearity real) and OQ-19 (amount-banded routing). OQ-43 is now the single highest-value screen: WorkFlowTemplateStepAction has never been rendered, and it holds the entire control-flow model. Nobody has confirmed this. Recorded in modules/workflow/asg-edgeplus-mapping.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### Does the ASC 842

*Inferred · question · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

Does the ASC 842 review gate exist in the accounting module's spec? The live workflow proves schedules are reviewed and double-approved before publication. If ../accounting/ and its BRD assume auto-publish, that is a requirements gap to raise now. Nobody has confirmed this. Recorded in modules/workflow/asg-edgeplus-mapping.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### Does the payments spec

*Inferred · question · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

Does the payments spec treat file generation as a workflow step? `Rent Payment Review/Approval` step 5 is *Generate Final Rent Payment File* — a step, not a side effect of approval. Check ../contracts/payment-lifecycle.md against it. Nobody has confirmed this. Recorded in modules/workflow/asg-edgeplus-mapping.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### Is BRD 17 Workflows

*Inferred · question · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

Is BRD 17 ("Workflows & Approvals Module") consistent with what this analysis found? It is Submitted and ASG-approved (Observed, feature list line 307) but was not available offline for this pass. Read it against rules.md and record every contradiction — per the estate's source-of-truth order, an approved BRD outranks this document. Nobody has confirmed this. Recorded in modules/workflow/asg-edgeplus-mapping.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### Does BRD 15 Modern

*Inferred · question · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

Does BRD 15 ("Modern Document Workflow") overlap? Also Submitted (Observed, line 304). Two BRDs with "workflow" in the title need reconciling before either is specced. Nobody has confirmed this. Recorded in modules/workflow/asg-edgeplus-mapping.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### What does the existing

*Inferred · question · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

**What does the existing feature/909-page-layouts-backend-poc branch in the monorepo assume about workflow?** It is stranded and must be ported or abandoned before the monorepo is dismantled; if it made workflow assumptions they should be captured now. Nobody has confirmed this. Recorded in modules/workflow/asg-edgeplus-mapping.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### Which ADR 004 governs

*Inferred · question · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

Which ADR-004 governs? The KnowledgeFolder database-per-tenant one or the Configuration-Service shared-database one. Workflow instance placement (§5) depends on it. Nobody has confirmed this. Recorded in modules/workflow/asg-edgeplus-mapping.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 1 Are

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-1 — Are TriggerCodeSQLTableID / TriggerObjectID real stored columns? They are the only edge from a running workflow to the business record it governs, yet they are absent from the physical extract. In Manage Work Flows open any template, then find a *running* workflow on a Contract's Work Flow tab and check whether the list shows the source record. If the pair is not stored, attachment must be reconstructed via KickOffIssueID → Issue.ProjectEntityID and the model changes materially. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 2 Does

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-2 — Does WorkFlowTemplateStepMember exist as a real table? It is the only place Org Chart Level routing can live. In Manage Work Flows → any step → the Approver/Assignee picker, check whether *Org Chart Level* is offered as a selectable Approver Type and, if so, what value it takes (an integer depth? a relative "my supervisor"?). Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 3 Where is

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-3 — Where is LimitByEntity's portfolio list stored? No join table exists in the schema. In Manage Work Flows tick *Limit By Entity* on a template and observe what control appears and what it is bound to. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 5 Can a spawned

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-5 — Can a spawned workflow be traced to its parent? With an action configured to KickOffWorkFlowTemplateID, fire it and inspect the new WorkFlow record for any parent pointer. If none exists, the audit chain is broken by design and ASG Edge+ must add one. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 4 What is

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-4 — What is StepMemberResponsibility? A fifth routing dimension or a display label? Check whether Manage Work Flows offers a *Responsibility* field on a step's member configuration, and whether its values come from a code list or free text. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 6 What does

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-6 — What does IsNotifyClosed actually mean? The column name says "notification closed"; the vendor definition says "has notifications configured". One of them is wrong. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 7 re routed What

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-7 (re-routed) — What are the values of Work Flow Status Code? **Work Flow Status Code is not one of the 207 platform code tables (Observed**, ../../data-model/code-table-registry.md) — an earlier revision of this folder wrongly asserted that it was. The table exists (S1 declares the type on WorkFlow and WorkFlowStep) but is not tenant-editable. Read it instead by introspecting codeWorkFlowStatusID through the GraphQL API, which expands code tables to { shortName longName }. Full instructions in state-machine.md. Last Action Status Code (2082) is in the catalogue and can be read from Manage . Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 8 What are the

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-8 — What are the integer values of ApproverType / AssigneeType / NotifieeType? S2 names four categories but not their encoding. Read the option order in the Manage Work Flows step editor. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 45 What polarity is

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-45 — What polarity is Global Sequence Numbers? / IsSequencePerFirm? The UI label and the column name are near-inverses. On a Form Type with a known prefix, toggle nothing but read the checkbox state, then create a request on two different entities and compare the numbers. Gets sequence numbering right in migration. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 46 Which entity

*Inferred · question · source: `docs/modules/workflow/data-model.md`*

OQ-46 — Which entity types are the other two live Form Types attachable to? Rent Payment Review/Approval and User Request were not captured. Expands OQ-32. Nobody has confirmed this. Recorded in modules/workflow/data-model.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 29 do

*Inferred · question · source: `docs/modules/workflow/issues-and-tasks.md`*

OQ-29 — do SetTaskInProcess / SetTaskCanceled write the Task's status or the Step's? Label and definition contradict each other. Configure a task step with both flags, start it, and read Task.CodeTaskStatusID on the linked schedule task. Nobody has confirmed this. Recorded in modules/workflow/issues-and-tasks.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 30 is a Form

*Inferred · question · source: `docs/modules/workflow/issues-and-tasks.md`*

OQ-30 — is a Form created by the workflow, or does the workflow attach to an existing Form? WorkFlowStep.IssueID exists but nothing says who creates the row. Kick off a workflow and check whether a new row appears on the entity's Forms tab at step start. Nobody has confirmed this. Recorded in modules/workflow/issues-and-tasks.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 31 how does a Task

*Inferred · question · source: `docs/modules/workflow/issues-and-tasks.md`*

OQ-31 — how does a Task step differ from a Form step in the UI? IsFormStep = false steps have PageLayoutAssigneesID too, which implies they still render a layout. Configure one of each and compare. Nobody has confirmed this. Recorded in modules/workflow/issues-and-tasks.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 32 which of the

*Inferred · question · source: `docs/modules/workflow/issues-and-tasks.md`*

OQ-32 — which of the eleven IsValidFor* entity types does ASG actually use? Five are confirmed by the feature list (Portfolio, Location, Facility, Contract, Equipment). Open Manage Forms and record the flags on every Form Type in the tenant. Nobody has confirmed this. Recorded in modules/workflow/issues-and-tasks.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 28 are Finish to

*Inferred · question · source: `docs/modules/workflow/issues-and-tasks.md`*

OQ-28 — are Finish-to-Finish and Start-to-Finish predecessor types available? Open Manage Firm Drop Downs → Task Lead Lag Type Code and read the values. Nobody has confirmed this. Recorded in modules/workflow/issues-and-tasks.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 33 do WorkOrder

*Inferred · question · source: `docs/modules/workflow/issues-and-tasks.md`*

**OQ-33 — do WorkOrder.ApproverMemberID and ServiceRequest.ApproverPartyID bypass the workflow engine entirely?** If they do, there are two approval systems and a rebuild must consolidate them. Nobody has confirmed this. Recorded in modules/workflow/issues-and-tasks.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 19 repeated from

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

**OQ-19 (repeated from step-actions.md) — how is amount-banded approval routing done?** Member carries PaymentApprovalMinAmount/MaxAmount, RecurringApprovalMinAmount/MaxAmount and the two Equip* pairs, and no workflow field reads them. Open Manage Work Flows → a payment-approval step and look for any threshold control; then open Member Administration → a member and check whether those four pairs are populated. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 8 sharpened which

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-8 (sharpened) — which vocabulary does the legacy ApproverType integer encode? Three competing vocabularies are now Observed (§2) and the reconciliation offered there is Derived, not proven. Open a step's approver configuration in Manage Work Flows, record the exact option list offered for *Approval Level*, then read the same saved step through the GraphQL Explorer and compare the returned enum value against the integer. This single comparison settles §2. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 40 is AssigneeType

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-40 — is AssigneeType a scope selector, as §2 concludes? If REGION1 / REGION2 / MARKET / PARENT really are ProjectEntity hierarchy scopes, a step must have *both* a principal category and a scope. Check whether the step editor offers two controls or one. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 2 does

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-2 — does WorkFlowTemplateStepMember exist, and is Org Chart Level selectable? Record what control appears when an org-chart option is chosen, and whether the depth is a free integer or a picklist of 1/2/3/All/Market matching MemberNotifyType. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 22 Org Chart Level

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-22 — Org Chart Level is relative to whom? Configure a step with a level and observe who resolves. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 24

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-24 — CodeJobTitleIDList vs AssignedCodeJobTitleIDList on LinkMemberProjectEntity. On a Contract's Members/Contacts tab, check whether a member's titles there differ from their global title in Member Administration. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 14 the exact

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-14 — the exact meaning of "all qualified approvers on the entity". See step-actions.md. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 26 does form level

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-26 — does form-level reassignment write back to the template? Place ReassignApproversJobTitleIDList on an approver layout, use it on a running step, then re-open the template step and see whether its ApproverJobTitleIDList changed. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 25 do workflow SLA

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-25 — do workflow SLA days honour HolidaySchedule and working days? Set DurationDaysApprovers = 5 on a step started on a Thursday and read back DueDateApprovers. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 23 which manager

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-23 — which manager receives the DaysUntilAlert* notification? LinkMemberProjectEntity.IsManager, ProjectEntity.ManagerIDList, or Member.SupervisorID? The ORGCHART_LEV1 enum value suggests SupervisorID walked one hop. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 41 how is assignee

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-41 — how is assignee routing configured? The live grid shows only Approval Level and Approver, both approver concepts. WorkFlowTemplateStep carries a full parallel set of assignee routing columns and a PageLayoutAssigneesID, none of which was rendered. Open the step editor and capture the assignee half. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 42 why does the

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-42 — why does the live tenant route 17 of 19 steps by named Member? Deliberate policy, or role-based routing being unusable in practice (the "all-for-one" overload, feature list line 360)? Ask ASG. The answer decides how much of the routing engine ASG Edge+ actually needs on day one. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 27 what happens to

*Inferred · question · source: `docs/modules/workflow/routing-and-approvals.md`*

OQ-27 — what happens to a running workflow when a member is deactivated? ASG states (S4 line 332) that deactivated users lose all access but *"Anything created or assigned to the deactivated user must stay in the system with user's details."* Confirm whether a step routed solely to a deactivated member deadlocks. Nobody has confirmed this. Recorded in modules/workflow/routing-and-approvals.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 7 re routed the

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-7 (re-routed) — the full value set of Work Flow Status Code. **Do not look in Manage Firm Drop Downs; it is not there.** Two routes remain, both cheap: (a) The GraphQL API — preferred. The API expands code tables to a pair, codeContractStatusID { shortName longName } (Observed, ../../data-model/graphql-api.md). Query live WorkFlow and WorkFlowStep records selecting codeWorkFlowStatusID { shortName longName } and collect the distinct values; or introspect the field's type directly, which returns the whole enumeration whether or not any record uses it. Introspection is strictly better — it ca. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 44 is the linear

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-44 — is the linear reading real, or an artefact of the grid? Open the actions on Rent Payment Review/Approval steps 3-4 and on Lease Admin Request steps 6-7 and record every MoveToStepNumber value. If all are *current + 1* or null, linearity is confirmed in production. If any points backward or skips, the engine branches and the grid was simply hiding it. See step-actions.md OQ-43, which is the same screen. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 34 how is a step

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-34 — how is a step cancelled? SetTaskCanceled's definition says *"when the user cancels the step"*, but no WorkFlowTemplateStepAction field expresses cancel. Is it a separate UI control, a sTYPE_SUBMITBUTTON, or an action named "Cancel" whose behaviour is conventional?. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 36 does the

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-36 — does the workflow status differ from the step status? Both bind the same dropdown. Start a workflow and compare the value shown on the Work Flows list against the value on the current step. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 16 OQ 15 T12

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-16 / OQ-15 — T12 precedence between MoveToStepNumber, AutoLaunchNextStep and RestartStep. See step-actions.md. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 37 what closes a

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-37 — what closes a workflow whose last step completes without a CloseWorkFlow action? Cheaper than building a template: open the action on the terminal step of each live workflow — *Approve ASC 842 Schedules (Client)*, *Complete Lease Admin Request*, *Final Rent Payment File*, *Submit Revisions* — and check whether Action Should Close Work Flow? is ticked. If it is on all four, closure is explicit and a rebuild must require it. If not, there is an implicit end-of-sequence close. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 35 the value sets

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-35 — the value sets of EMailSentStatus and NotifyAcknowledgedStatus. Both are free text on both WorkFlowStepApprover and WorkFlowStepAssignee. Read the Email Log (/en/reports/EMailLogs.jsp) alongside a live step. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 38 is there a step

*Inferred · question · source: `docs/modules/workflow/state-machine.md`*

OQ-38 — is there a step-level audit trail beyond the single Prior* slot? Check Audit Reports (/en/reports/…) and the per-record Audit Log popup on a running workflow step. TaskTemplateAudit and the audit-history-tables family exist; whether workflow transitions are written there is unknown, and it decides whether ASG Edge+ can migrate history at all. Nobody has confirmed this. Recorded in modules/workflow/state-machine.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 43 Open the action

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-43 — Open the action editor. Nothing in this document is Observed in the running system. In Manage Work Flows → Rent Payment Review/Approval → step 2 or 3 (`Approve Rent Preview File`), open the step and then its actions. Capture: how many actions exist, their names, and every field rendered — in particular Is Approval Action?, `Action Should Move to Next Step Number, Action Should Restart the Step?, Action Should Close Work Flow?, Require All Approvers? and Last Action Status`. **This one screen converts the whole control-flow model from Derived to Observed** and answers OQ-14, OQ-15, OQ-1. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 44 Does any live

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-44 — Does any live action set MoveToStepNumber? Specifically: what happens when an approver denies at Rent Payment Review/Approval step 3 or 4? If a backward jump exists, the engine branches in production and the ordinal grid is simply hiding it. If it does not, ASG has no rejection path and that is a requirement gap for the rebuild, not a modelling detail. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 19 How is amount

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-19 — How is amount-banded approval routing done? Member carries eight approval-limit currency columns that no workflow field references. Rent Payment Review/Approval is the live process where amount banding would be expected — check its steps for any threshold; then open a Member record and check whether *Payment Approval Min/Max Amount* is populated. ASG Edge+ will certainly need amount-banded lease and payment approvals. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 16 MoveToStepNumber

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-16 — MoveToStepNumber vs AutoLaunchNextStep: which wins? Configure a step with AutoLaunchNextStep = true and an action with MoveToStepNumber = 5, fire it, and observe which step becomes current. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 15 RestartStep

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-15 — RestartStep + MoveToStepNumber set together: what happens? Configure both on one action and fire it. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 14 Does

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

**OQ-14 — Does RequireAllApprovers mean all *qualified approvers on the entity* or all *approvers on the step*?** The wording says the former, which would make the quorum re-resolve at decision time. Add a member to the entity with a matching job title *after* the step starts, then try to complete the step. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 17 Step level

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-17 — Step-level notifiees vs action-level Notify*Complete: do both fire? Configure a step with a notifiee list *and* an action with NotifyStepApproversComplete, fire it, and check the Email Log (/en/reports/EMailLogs.jsp) for how many messages were sent. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 18 What

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

**OQ-18 — What distinguishes KickOffWorkFlowTemplateID, KickOffTargetWFTemplateID and WorkFlowTemplateKickOffID?** Configure a kick-off action and read all three values back. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 20 Is there a

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-20 — Is there a standard action vocabulary in the UI? Open the action editor for a step and record whether *Action Name* is free text or a picklist, and what the seeded actions on a platform template are called. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 21 What does

*Inferred · question · source: `docs/modules/workflow/step-actions.md`*

OQ-21 — What does AutoClearAmounts do? No vendor documentation exists. Check the field's tooltip in the action editor. Nobody has confirmed this. Recorded in modules/workflow/step-actions.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 9 What seeds

*Inferred · question · source: `docs/modules/workflow/template-vs-instance.md`*

OQ-9 — What seeds WorkFlow.WorkFlowName? Template name, kick-off form Subject, or user input? Kick off any workflow from a Contract's Work Flow tab and compare the resulting name against the template name and the form title. This is a one-line answer that changes the create path. Nobody has confirmed this. Recorded in modules/workflow/template-vs-instance.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 10 Are all

*Inferred · question · source: `docs/modules/workflow/template-vs-instance.md`*

OQ-10 — Are all WorkFlowStep rows created up front, or one at a time? Start a three-step workflow and look at the step list on step 1: if steps 2 and 3 are listed with dates, materialisation is eager. Determines whether MoveToStepNumber jumps to an existing row or creates one. Nobody has confirmed this. Recorded in modules/workflow/template-vs-instance.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 11 Does editing a

*Inferred · question · source: `docs/modules/workflow/template-vs-instance.md`*

OQ-11 — Does editing a live template change running instances? Start a workflow, then change AutoLaunchNextStep and EMailMessage on its template's current step, then advance the workflow. If the new AutoLaunchNextStep takes effect but the old EMailMessage is still sent, the hybrid model described here is confirmed exactly as stated. Nobody has confirmed this. Recorded in modules/workflow/template-vs-instance.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 12 Is

*Inferred · question · source: `docs/modules/workflow/template-vs-instance.md`*

OQ-12 — Is WorkFlowStepAssignee created for every resolved assignee, or only on demand? Compare the row count against WorkFlowStep.AssigneeMemberIDList length on a live step. Nobody has confirmed this. Recorded in modules/workflow/template-vs-instance.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 13 What does the

*Inferred · question · source: `docs/modules/workflow/template-vs-instance.md`*

OQ-13 — What does the engine do when a resolved member set is empty? Configure a step routed to a job title nobody on the entity holds and observe: does it block, auto-complete, or fall through to UnassignedApproverID?. Nobody has confirmed this. Recorded in modules/workflow/template-vs-instance.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

### OQ 47 Are layouts

*Inferred · question · source: `docs/modules/workflow/template-vs-instance.md`*

OQ-47 — Are layouts shared across steps, or is the second layout per step the assignee one? §3a offers two readings for LAR Review Financial Abstract and the missing Approve … (LA) layout. Open Lease Admin Request step 3 and Rent Payment Review/Approval step 3 in the step editor and read both Layout To Use With Approvers and `Layout To Use With Assignees`. This also answers OQ-41 (how assignee routing is configured) from the same screen. This cannot be settled offline, and one observation will not settle it either. The layout↔step binding lives in WorkFlowTemplateStep *rows*; all-fields.csv su. Nobody has confirmed this. Recorded in modules/workflow/template-vs-instance.md, under the Workflow & Approvals area. Until it is settled, anything built on the assumption is a guess.

## Rules (62)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### A Template — [WF-R-001](../rules/WF-R-001.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**WorkFlowTemplateName is required; every save increments RevNumber by one and stamps the modifying member and date.**

|  |  |
|---|---|
| Stated as | Administrator saves a workflow template |
| Stated as | `WFT.WorkFlowTemplateName` |
| Stated as | Name is non-empty |
| Stated as | Template is saved; `RevNumber` += 1; `ModifiedByID`/`ModifiedDate` stamped |
| Stated as | Observed — `WorkFlowTemplateName` is Required; `RevNumber` "increases by 1 each time the record is modified" |

### A Template — [WF-R-002](../rules/WF-R-002.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**DefaultWFCodePriorityID must be set from Priority Code; every workflow instance inherits it unless a spawning action overrides it.**

|  |  |
|---|---|
| Stated as | Administrator saves a template |
| Stated as | `WFT.DefaultWFCodePriorityID` |
| Stated as | Required |
| Stated as | A priority must be chosen from `Priority Code` |
| Stated as | Observed — field is Required |

### A Template — [WF-R-003](../rules/WF-R-003.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**A template restricted by LimitByEntity is offered only for its listed portfolios. The join table that would store which portfolios does not appear anywhere in the 223-object schema — where the restriction list actually lives is unresolved (OQ-3).**

|  |  |
|---|---|
| Stated as | A user browses available workflows on an entity |
| Stated as | `WFT.LimitByEntity`, the (unlocated) portfolio restriction list |
| Stated as | `LimitByEntity = 1` |
| Stated as | The template is offered only for the listed portfolios; if `0`, for all portfolios |
| Stated as | Observed — "If this value is 1, the work flow template is only available for certain portfolios. If this value is 0, the work flow template is available for all portfolios." Storage location unknown (OQ-3) |

### A Template — [WF-R-004](../rules/WF-R-004.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**A user browses forms available on an entity of type T · `CodeIssueType.IsValidFor<T>` · Flag is true · A form of that type may be raised against that entity. Now Observed in the Form Type editor, which renders a boolean per entity kind: Portfolio, Capital Program, Prototype, Location, Parcel, Site,….**

|  |  |
|---|---|
| Stated as | A user browses forms available on an entity of type T |
| Stated as | `CodeIssueType.IsValidFor<T>` |
| Stated as | Flag is true |
| Stated as | A form of that type may be raised against that entity. Now Observed in the Form Type editor, which renders a boolean per entity kind: Portfolio, Capital Program, Prototype, Location, Parcel, Site, Project, Facility, Capital Project, RE Contract, Equipment Contract. Both lease-accounting form types are set `Portfolio = Yes, RE Contract = Yes`, the other nine `No` |
| Stated as | Observed — `../layouts-and-forms/forms-vs-pages-vs-layouts.md`; the UI-label→column mapping is Derived (see `issues-and-tasks.md`) |

### A Template — [WF-R-005](../rules/WF-R-005.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**The workflow's own attachability is whatever its kick-off form's Form Type declares. WorkFlowTemplate carries no IsValidFor* columns of its own — the chain runs through PageLayoutID to the layout's Form Type.**

|  |  |
|---|---|
| Stated as | A workflow template is bound to a kick-off form |
| Stated as | `WFT.PageLayoutID` → `PageLayout.CodeIssueTypeID` → `CodeIssueType.IsValidFor*` |
| Stated as | — |
| Stated as | The workflow's attachability is that of its kick-off form's type. `WorkFlowTemplate` itself carries no `IsValidFor*` columns |
| Stated as | Derived |

### A Template — [WF-R-006](../rules/WF-R-006.md)

*Inferred · rule · source: `docs/modules/workflow/rules.md`*

**A form type is marked as workflow-driving · `CodeIssueType.IsWorkFlow` · true · Forms of this type participate in the workflow engine rather than standing alone · Inferred — no vendor help text for this column.**

|  |  |
|---|---|
| Stated as | A form type is marked as workflow-driving |
| Stated as | `CodeIssueType.IsWorkFlow` |
| Stated as | true |
| Stated as | Forms of this type participate in the workflow engine rather than standing alone |
| Stated as | Inferred — no vendor help text for this column |

### A Template — [WF-R-007](../rules/WF-R-007.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**StepNumber and WorkFlowTemplateStepName are both required, and the step is ordered within its template by StepNumber. Uniqueness of StepNumber within one template is not enforced by any observed constraint.**

|  |  |
|---|---|
| Stated as | Administrator adds a step |
| Stated as | `WFTS.StepNumber`, `WFTS.WorkFlowTemplateStepName` |
| Stated as | Both Required |
| Stated as | Step is ordered within the template by `StepNumber`. Uniqueness of `StepNumber` within a template is not enforced by any observed constraint |
| Stated as | Observed (Required flags); uniqueness Inferred |

### A Template — [WF-R-008](../rules/WF-R-008.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**True selects a Form step, rendering a page layout and collecting a decision; false selects a Task step, working a schedule item with no form surface at all.**

|  |  |
|---|---|
| Stated as | Administrator configures a step |
| Stated as | `WFTS.IsFormStep` |
| Stated as | — |
| Stated as | The step is a Form step (true) or a Task step (false) |
| Stated as | Observed — "This field has one of two values: Form Step or Task Step." |

### A Template — [WF-R-009](../rules/WF-R-009.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**The principal selector (what kind of thing names the people) and the scope selector (where to search for them) are two independent dimensions, not two rival vocabularies for one idea. A rebuild should model routing as one reusable principal selector crossed with an orthogonal scope selector, and….**

|  |  |
|---|---|
| Stated as | Administrator configures a step |
| Stated as | `WFTS.ApproverType`/`AssigneeType`/`NotifieeType` |
| Stated as | — |
| Stated as | Selects the routing category. Authoritative form is the GraphQL enum `MemberNotifyType: [ORGCHART_ALL, ORGCHART_LEV1, ORGCHART_LEV2, ORGCHART_LEV3, ORGCHART_MKT, USERCLASS, JOBTITLE, MEMBERID]` — the vendor help's four categories, with org-chart depth bounded at three explicit levels. The live UI renders the column as Approval Level and adds a fifth value the schema does not name: Ad Hoc |
| Stated as | Observed (both enums and the UI); the mapping between them is Derived — see `routing-and-approvals.md` §2 and OQ-8 |

### A Template — [WF-R-010](../rules/WF-R-010.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Administrator configures a step · `WFTS.ApproverMemberIDList`, `ApproverJobTitleIDList`, `ApproverUserClassIDList`, `WorkFlowTemplateStepMember.OrgChartLevel` · — · `ComputedRequiresApprovers` is true iff the step requires approvers; `ComputedRequiresAssignees` likewise · Observed — "The value of….**

|  |  |
|---|---|
| Stated as | Administrator configures a step |
| Stated as | `WFTS.ApproverMemberIDList`, `ApproverJobTitleIDList`, `ApproverUserClassIDList`, `WorkFlowTemplateStepMember.OrgChartLevel` |
| Stated as | — |
| Stated as | `ComputedRequiresApprovers` is true iff the step requires approvers; `ComputedRequiresAssignees` likewise |
| Stated as | Observed — "The value of this field is true if the work flow step requires approvers." Derivation rule itself unstated |

### A Template — [WF-R-011](../rules/WF-R-011.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**The name is required and free text. This is why ASG reports "there is no obvious, standard Send Back to Previous Step or Request Rework action" — the engine has no notion of a canonical set of actions at all.**

|  |  |
|---|---|
| Stated as | Administrator saves an action |
| Stated as | `WFTSA.WorkFlowTemplateStepActionName` |
| Stated as | Required |
| Stated as | The name is the button label shown to approvers. There is no controlled vocabulary — no code table constrains it |
| Stated as | Observed (Required) + Derived (no FK) |

### A Template — [WF-R-012](../rules/WF-R-012.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**When present, this JavaScript executes — for conditional kick-off on the template, or as a custom action on a step action. There is no other conditional construct anywhere in the 223-object schema.**

|  |  |
|---|---|
| Stated as | Template or action is saved with JavaScript |
| Stated as | `WFT.IsEnabledLxJSCode`, `WFTSA.IsEnabledLxJSCode` |
| Stated as | Non-empty |
| Stated as | Custom JavaScript executes — for conditional kick-off (template) or as a custom action (action). This is the engine's only conditional-logic mechanism |
| Stated as | Observed — "custom JavaScript used to kick off conditional work flows" / "If you are creating a custom action using JavaScript, enter the JavaScript in this field." |

### A Template — [WF-R-013](../rules/WF-R-013.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**The 35 template-only fields — routing rules, AutoLaunchNextStep, SetTaskInProcess, SetTaskCanceled, AutoAdjustTaskDates, both NotifyStep*Started flags, and the three header-level Notify*Complete flags — are read through WorkFlowStep.WorkFlowTemplateStepID and therefore change behaviour on every….**

|  |  |
|---|---|
| Stated as | Template is edited while instances are running |
| Stated as | `WFS.WorkFlowTemplateStepID` |
| Stated as | — |
| Stated as | The 35 template-only fields (routing rules, `AutoLaunchNextStep`, `SetTaskInProcess`, `SetTaskCanceled`, `AutoAdjustTaskDates`, `NotifyStep*Started`, the three `WFT.Notify*Complete` flags) are read live and therefore change running instances. The 20 snapshotted fields do not |
| Stated as | Derived — set difference; confirm via OQ-11 |

### B Kick off and — [WF-R-014](../rules/WF-R-014.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**A workflow may be kicked off any of four ways per the GraphQL enum. This corrects the vendor help text, which names only three and omits STATUS_CHANGE.**

|  |  |
|---|---|
| Stated as | Any of four events |
| Stated as | `WFT.KickOffMethod` |
| Stated as | — |
| Stated as | A workflow may be kicked off four ways, per the GraphQL enum `KickOffMethod: [STEP_ACTION, PAGE_LAYOUT, STATUS_CHANGE, TASK]`: (a) `STEP_ACTION` — an action on a preceding workflow step; (b) `PAGE_LAYOUT` — completion of a form / a button on a layout; (c) `STATUS_CHANGE` — a record's status changing; (d) `TASK` — completion of a schedule task |
| Stated as | Observed — `../../data-model/graphql-api.md`. Corrects the vendor help text, which names only three and omits `STATUS_CHANGE`: "There are three ways a work flow can be kicked off: by completion of an action in another work flow, by completion of a schedule task, or by completion of a form." |

### B Kick off and — [WF-R-015](../rules/WF-R-015.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**When a form matching the configured kick-off layout is completed, a WorkFlow row is created with KickOffIssueID pointing at that form.**

|  |  |
|---|---|
| Stated as | A form of the configured layout is completed |
| Stated as | `WFT.PageLayoutID`, the completed `Issue` |
| Stated as | Layout matches |
| Stated as | A `WF` row is created with `KickOffIssueID` = the form |
| Stated as | Observed — "Select the form whose completion you want to have kick off this work flow" / "The ID of the form that kicked off the work flow" |

### B Kick off and — [WF-R-016](../rules/WF-R-016.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**When the named schedule task completes, a WorkFlow row is created with KickOffTaskID pointing at it.**

|  |  |
|---|---|
| Stated as | A schedule task is completed |
| Stated as | `WFT.TaskName`, the completed `Task` |
| Stated as | Name matches |
| Stated as | A `WF` row is created with `KickOffTaskID` = the task |
| Stated as | Observed — "Select the schedule task whose completion you want to have kick off this work flow" / "The ID of the schedule task that kicked off the work flow" |

### B Kick off and — [WF-R-017](../rules/WF-R-017.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**An action with a non-null kick-off target creates a brand-new workflow instance from that template the moment the action fires. No column on the new instance records which parent workflow, step or action spawned it — a spawned workflow is an orphan from the moment it is born.**

|  |  |
|---|---|
| Stated as | An action with a kick-off target completes |
| Stated as | `WFTSA.KickOffWorkFlowTemplateID` |
| Stated as | Non-null |
| Stated as | A new `WF` is created from that template. No column on the new instance records the parent workflow, step or action |
| Stated as | Observed (the kick-off) + Derived (the missing parent pointer — OQ-5) |

### B Kick off and — [WF-R-018](../rules/WF-R-018.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**WorkFlow.TriggerCodeSQLTableID + TriggerObjectID together read "this workflow was triggered by row TriggerObjectID of table TriggerCodeSQLTableID" — a table-name-plus-primary-key polymorphic reference. Both columns are catalog-only, absent from the physical database extract, which is either an….**

|  |  |
|---|---|
| Stated as | Workflow instantiation |
| Stated as | `WF.TriggerCodeSQLTableID`, `WF.TriggerObjectID` |
| Stated as | — |
| Stated as | The instance is bound polymorphically to the triggering record: table name + primary key |
| Stated as | Derived — `sCODE_SQLTABLE` is the platform table registry; catalog-only columns (OQ-1) |

### B Kick off and — [WF-R-019](../rules/WF-R-019.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**WorkFlow.WorkFlowCodePriorityID is seeded from the template's DefaultWFCodePriorityID, unless a spawning action overrides it per WF-R-020.**

|  |  |
|---|---|
| Stated as | Workflow instantiation |
| Stated as | `WFT.DefaultWFCodePriorityID` |
| Stated as | — |
| Stated as | `WF.WorkFlowCodePriorityID` is seeded from the template default |
| Stated as | Derived — identical `sCODE_PRIORITY` type, "Default" prefix |

### B Kick off and — [WF-R-020](../rules/WF-R-020.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**If set, the parent workflow's priority overrides the spawned workflow's own template default (WF-R-019).**

|  |  |
|---|---|
| Stated as | Workflow instantiation by a spawning action |
| Stated as | `WFTSA.PassPriorityToNewWF` |
| Stated as | true |
| Stated as | The parent workflow's `WorkFlowCodePriorityID` overrides WF-R-019 |
| Stated as | Observed — "transfer the priority level of this work flow to a new work flow that is kicked off by this step" |

### B Kick off and — [WF-R-021](../rules/WF-R-021.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**When set, the workflow's initiator is written into WorkFlow.AdhocMemberID at instantiation and used for every later step that declares an ad-hoc assignee.**

|  |  |
|---|---|
| Stated as | Workflow instantiation |
| Stated as | `WFT.AutoAssignInitiator`, current user |
| Stated as | true |
| Stated as | `WF.AdhocMemberID` = the initiator, applied to the kick-off step/form and to every later step that requires an ad-hoc assignee |
| Stated as | Observed — full quote in `routing-and-approvals.md` §5 |

### B Kick off and — [WF-R-022](../rules/WF-R-022.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**If set, the parent workflow's ad-hoc assignee becomes the ad-hoc assignee of the first step of the newly spawned workflow.**

|  |  |
|---|---|
| Stated as | Workflow instantiation by a spawning action |
| Stated as | `WFTSA.PassAdhocToNewWF` |
| Stated as | true |
| Stated as | The parent's `AdhocMemberID` is assigned to the first step of the new workflow |
| Stated as | Observed — "assign the ad hoc member assigned to this task to the first task in the new work flow kicked off by this step" |

### B Kick off and — [WF-R-023](../rules/WF-R-023.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**InitiatedByMemberID is set to whoever triggered the kick-off.**

|  |  |
|---|---|
| Stated as | Workflow instantiation |
| Stated as | `WF.InitiatedByMemberID` |
| Stated as | — |
| Stated as | Set to the member who triggered the kick-off |
| Stated as | Observed — "The member ID of the user who initiated the work flow" |

### B Kick off and — [WF-R-024](../rules/WF-R-024.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**Twenty fields are copied verbatim: StepNumber, TaskName, IsFormStep, Priority, both PageLayout* ids, both Approver/Assignee/Notifiee member lists, both duration pairs, all four warn/alert day-offsets, both EMailAlert flags, both channel switches, and EMailMessage.**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | `WFTS` → `WFS` |
| Stated as | — |
| Stated as | Exactly 20 configuration fields are copied: `StepNumber`, `TaskName`, `IsFormStep`, `Priority`, `PageLayoutApproversID`, `PageLayoutAssigneesID`, `ApproverMemberIDList`, `AssigneeMemberIDList`, `NotifieeMemberIDList`, `DurationDaysApprovers`, `DurationDaysAssignees`, `DaysUntilWarnApprovers`, `DaysUntilWarnAssignees`, `DaysUntilAlertApprovers`, `DaysUntilAlertAssignees`, `EMailAlertApprovers`, `EMailAlertAssignees`, `EnableForEMail`, `EnableForDashboard`, `EMailMessage`. `WFS.WorkFlowStepName` ← `WFTS.WorkFlowTemplateStepName` under a renamed column |
| Stated as | Derived (set intersection) + Observed ("The name of the work flow step from the work flow template") |

### C Routing resolution — [WF-R-025](../rules/WF-R-025.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**Step instantiation · `WFTS.ApproverType` = Member; `ApproverMemberIDList` · — · `WFS.ApproverMemberIDList` = the named members · Derived.**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | `WFTS.ApproverType` = Member; `ApproverMemberIDList` |
| Stated as | — |
| Stated as | `WFS.ApproverMemberIDList` = the named members |
| Stated as | Derived |

### C Routing resolution — [WF-R-026](../rules/WF-R-026.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**The step's ApproverJobTitleIDList is intersected against the roster of the entity the workflow is running on, filtered to members holding a matching job title, and the resulting flat member list is frozen onto the running step as WorkFlowStep.ApproverMemberIDList.**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | `WFTS.ApproverType` = Job Title; `ApproverJobTitleIDList`; `LinkMemberProjectEntity` for `WF.ProjectEntityID`; `Member.CodeJobTitleID`/`CodeJobTitleIDList` |
| Stated as | — |
| Stated as | `WFS.ApproverMemberIDList` = every member on the entity holding one of the listed titles |
| Stated as | Derived; corroborated by Observed "The Job Title is used when auto-assigning things like tasks, work flow steps, and notifications" |

### C Routing resolution — [WF-R-027](../rules/WF-R-027.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**User Class routing resolves against Member.CodeUserClassID intersected with the entity roster; Org Chart Level routing walks Member.SupervisorID the configured number of hops from an anchor that is itself unstated (OQ-22);.**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | `WFTS.ApproverType` = User Class; `ApproverUserClassIDList`; `Member.CodeUserClassID` |
| Stated as | — |
| Stated as | `WFS.ApproverMemberIDList` = every member on the entity in one of the listed classes |
| Stated as | Derived |

### C Routing resolution — [WF-R-028](../rules/WF-R-028.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**Step instantiation · `WFTS.ApproverType` = Org Chart Level; `WorkFlowTemplateStepMember.OrgChartLevel`;.**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | `WFTS.ApproverType` = Org Chart Level; `WorkFlowTemplateStepMember.OrgChartLevel`; `Member.SupervisorID` |
| Stated as | — |
| Stated as | `WFS.ApproverMemberIDList` = members n supervisor-hops from an anchor. The anchor is unspecified |
| Stated as | Derived + OQ-22 |

### C Routing resolution — [WF-R-029](../rules/WF-R-029.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**Step instantiation · as WF-R-025…028 for assignees and notifiees · — · `WFS.AssigneeMemberIDList` and `WFS.NotifieeMemberIDList` populated by the same pipeline · Derived.**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | as WF-R-025…028 for assignees and notifiees |
| Stated as | — |
| Stated as | `WFS.AssigneeMemberIDList` and `WFS.NotifieeMemberIDList` populated by the same pipeline |
| Stated as | Derived |

### C Routing resolution — [WF-R-030](../rules/WF-R-030.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**One WorkFlowStepApprover row per resolved approver, HasTakenAction starting false; one WorkFlowStepAssignee row per resolved assignee, carrying StepMemberResponsibility — described as "lists step members whose responsibility matches the responsibility for the workflow template step," a fifth,….**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | resolved approver set |
| Stated as | — |
| Stated as | One `WFSAp` row per approver: `MemberID`, `WorkFlowStepID`, `WorkFlowTemplateStepID`, `HasTakenAction = false` |
| Stated as | Derived |

### C Routing resolution — [WF-R-031](../rules/WF-R-031.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**Step instantiation · resolved assignee set · — · One `WFSAs` row per assignee: `MemberID`, `WorkFlowStepID`, `WorkFlowTemplateStepID`, `StepMemberResponsibility` · Derived; `StepMemberResponsibility` "lists step members whose responsibility matches the responsibility for the workflow template step"….**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | resolved assignee set |
| Stated as | — |
| Stated as | One `WFSAs` row per assignee: `MemberID`, `WorkFlowStepID`, `WorkFlowTemplateStepID`, `StepMemberResponsibility` |
| Stated as | Derived; `StepMemberResponsibility` "lists step members whose responsibility matches the responsibility for the workflow template step" (Observed) |

### C Routing resolution — [WF-R-032](../rules/WF-R-032.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**Notifiees exist only as the flat WorkFlowStep.NotifieeMemberIDList. No WorkFlowStepNotifiee table exists anywhere in the 223-object schema, so no delivery or acknowledgement is ever tracked for them.**

|  |  |
|---|---|
| Stated as | Step instantiation |
| Stated as | resolved notifiee set |
| Stated as | — |
| Stated as | No per-person row is created. Notifiees exist only as `WFS.NotifieeMemberIDList`; no delivery or acknowledgement is tracked for them |
| Stated as | Derived — no `WorkFlowStepNotifiee` object exists |

### C Routing resolution — [WF-R-033](../rules/WF-R-033.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Step becomes current · `WFS.ApproverMemberIDList`, `AssigneeMemberIDList` · — · `WFS.CurrentStepMemberIDList` = whoever the step is currently waiting on · Observed — "The members associated with the current workflow step"; the exact derivation is unstated.**

|  |  |
|---|---|
| Stated as | Step becomes current |
| Stated as | `WFS.ApproverMemberIDList`, `AssigneeMemberIDList` |
| Stated as | — |
| Stated as | `WFS.CurrentStepMemberIDList` = whoever the step is currently waiting on |
| Stated as | Observed — "The members associated with the current workflow step"; the exact derivation is unstated |

### C Routing resolution — [WF-R-034](../rules/WF-R-034.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Vendor definition: "When added to a form, this field allows users with appropriate permissions to reassign approvers by job title." Reassignment is a form field an administrator places on a layout, not a workflow operation, and it can only redirect to a job title, never to a named person. Whether….**

|  |  |
|---|---|
| Stated as | A user with permission edits a reassignment field on a form |
| Stated as | `WFTS.ReassignApproversJobTitleIDList` / `ReassignAssigneesJobTitleIDList` |
| Stated as | The field is present on the layout and the user has the permission |
| Stated as | Approvers/assignees are reassigned by job title only. Whether the change persists to the template or only to the running step is unresolved |
| Stated as | Observed — "When added to a form, this field allows users with appropriate permissions to reassign approvers by job title"; persistence per OQ-26 |

### C Routing resolution — [WF-R-035](../rules/WF-R-035.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Both this field and Member.IsUnassignedWorkFlowApprover are documented as unimplemented placeholders.**

|  |  |
|---|---|
| Stated as | — |
| Stated as | `WFTS.UnassignedApproverID`, `Member.IsUnassignedWorkFlowApprover` |
| Stated as | — |
| Stated as | No effect. Both are documented as "a placeholder for an upcoming feature" |
| Stated as | Observed |

### C Routing resolution — [WF-R-036](../rules/WF-R-036.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**All eight RunAtStart*/RunAtComplete*/runAt*ScheduledJob* fields are unimplemented; a rebuild should not implement them either, though the naming pattern is worth recording as a design intent that never shipped.**

|  |  |
|---|---|
| Stated as | — |
| Stated as | `WFTS.RunAtStartApprover1ID`, `RunAtStartApprover2ID`, `RunAtCompleteApprover1ID`, `RunAtCompleteApprover2ID`, and the four catalog-only `runAt*ScheduledJob*` fields |
| Stated as | — |
| Stated as | No effect. All eight are unimplemented placeholders |
| Stated as | Observed (four of them explicitly); Derived (the four with no physical column) |

### D Step execution and — [WF-R-037](../rules/WF-R-037.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Step becomes current · today · — · `WFS.StartDate` = today · Observed — "The date the work flow step started".**

|  |  |
|---|---|
| Stated as | Step becomes current |
| Stated as | today |
| Stated as | — |
| Stated as | `WFS.StartDate` = today |
| Stated as | Observed — "The date the work flow step started" |

### D Step execution and — [WF-R-038](../rules/WF-R-038.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**DueDateApprovers = StartDate + DurationDaysApprovers; DueDateAssignees is computed the same way for the assignee clock;.**

|  |  |
|---|---|
| Stated as | Step start |
| Stated as | `WFS.StartDate`, `DurationDaysApprovers`, `DurationDaysAssignees` |
| Stated as | — |
| Stated as | `WFS.DueDateApprovers` = start + approver duration; `DueDateAssignees` = start + assignee duration; `DueDate` = the governing one |
| Stated as | Observed — all three are "Calculates the due date of the work flow step…"; the arithmetic and which one governs are Derived |

### D Step execution and — [WF-R-039](../rules/WF-R-039.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**All five Computed*Date fields — warn and alert, for both roles, plus one notification due date — are calculated the moment the step becomes current, from the DaysUntilWarn*/DaysUntilAlert* offsets, and then simply sit there until the system clock reaches them.**

|  |  |
|---|---|
| Stated as | Step start |
| Stated as | `WFS.DaysUntilWarnApprovers`/`Assignees`, `DaysUntilAlertApprovers`/`Assignees`, `WFTS.DaysUntilNotification` |
| Stated as | — |
| Stated as | The five hidden dates are materialised: `ComputedWarnDateApprovers`, `ComputedWarnDateAssignees`, `ComputedAlertDateApprovers`, `ComputedAlertDateAssignees`, `ComputedDueDateNotification` |
| Stated as | Derived — matching name pairs |

### D Step execution and — [WF-R-040](../rules/WF-R-040.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Vendor definition: "set the work flow step status to 'In Process' when the step starts." Whether this writes Task.CodeTaskStatusID or WorkFlowStep.CodeWorkFlowStatusID is contradicted between the field label and its own definition (OQ-29).**

|  |  |
|---|---|
| Stated as | Step start |
| Stated as | `WFTS.SetTaskInProcess`, `WFS.TaskID` |
| Stated as | true |
| Stated as | Status set to "In Process". Whether this writes `Task.CodeTaskStatusID` or `WFS.CodeWorkFlowStatusID` is contradicted between the field label and its definition |
| Stated as | Observed (the value and the flag); target per OQ-29 |

### D Step execution and — [WF-R-041](../rules/WF-R-041.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**When AutoAdjustTaskDates is set, the linked schedule task's dates are rewritten to match the step's own start and due dates.**

|  |  |
|---|---|
| Stated as | Step start |
| Stated as | `WFTS.AutoAdjustTaskDates`, `WFS.StartDate`/`DueDate`, `WFS.TaskID` |
| Stated as | true |
| Stated as | The linked task's dates are adjusted to match the step's |
| Stated as | Observed — "automatically adjust the task dates to match the step durations" |

### D Step execution and — [WF-R-042](../rules/WF-R-042.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Step start · `WFTS.NotifyStepAssigneesStarted`, `WFS.EnableForEMail`, `EnableForDashboard`, `EMailMessage`, `WFStepNotificationLink` · true · Email/dashboard notification to every assignee; `WFSAs.EMailSentStatus` written · Observed.**

|  |  |
|---|---|
| Stated as | Step start |
| Stated as | `WFTS.NotifyStepAssigneesStarted`, `WFS.EnableForEMail`, `EnableForDashboard`, `EMailMessage`, `WFStepNotificationLink` |
| Stated as | true |
| Stated as | Email/dashboard notification to every assignee; `WFSAs.EMailSentStatus` written |
| Stated as | Observed |

### D Step execution and — [WF-R-043](../rules/WF-R-043.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Step start · `WFTS.NotifyStepApproversStarted` + same channel fields · true · Same, to every approver; `WFSAp.EMailSentStatus` written · Observed.**

|  |  |
|---|---|
| Stated as | Step start |
| Stated as | `WFTS.NotifyStepApproversStarted` + same channel fields |
| Stated as | true |
| Stated as | Same, to every approver; `WFSAp.EMailSentStatus` written |
| Stated as | Observed |

### D Step execution and — [WF-R-044](../rules/WF-R-044.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Step start · `WFTS.EMailAlertAssignees` / `EMailAlertApprovers` · true · A dashboard alert is sent to the assignee/approver when the task starts · Observed — "send a dashboard alert to the assignee of this task when the task starts".**

|  |  |
|---|---|
| Stated as | Step start |
| Stated as | `WFTS.EMailAlertAssignees` / `EMailAlertApprovers` |
| Stated as | true |
| Stated as | A dashboard alert is sent to the assignee/approver when the task starts |
| Stated as | Observed — "send a dashboard alert to the assignee of this task when the task starts" |

### D Step execution and — [WF-R-045](../rules/WF-R-045.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**When an assignee completes the form and presses Submit, SubmitForApprovalByMemberID/Name/Date are set once for the whole step. This is the direct consequence of the approver/assignee asymmetry: assignees do the work, one stamp records that it happened.**

|  |  |
|---|---|
| Stated as | Assignee completes and submits the form |
| Stated as | `ProjectEntity.FormSubmitButton`, current user, today |
| Stated as | — |
| Stated as | `WFS.SubmitForApprovalByMemberID`, `SubmitForApprovalByMemberName`, `SubmitForApprovalDate` set. One stamp per step, not per assignee |
| Stated as | Derived — the three columns exist and `WFSAs` has no submission columns |

### 3 What should — [WF-R-046](../rules/WF-R-046.md)

*Derived · rule · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

**D7 · Policy-driven escalation: notify → reassign to a delegate → escalate to a supervisor → auto-decide, configurable per step. · Requested (feature list line 354).**

|  |  |
|---|---|
| Stated as | D7 |
| Stated as | Policy-driven escalation: notify → reassign to a delegate → escalate to a supervisor → auto-decide, configurable per step. |
| Stated as | Requested (feature list line 354). Lease critical dates make missed approvals expensive. |
| Stated as | New scheduler component. |

### D Step execution and — [WF-R-047](../rules/WF-R-047.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**A notification goes to a manager. That is the entire effect.**

|  |  |
|---|---|
| Stated as | System date reaches `ComputedAlertDate*` |
| Stated as | — |
| Stated as | Step not complete |
| Stated as | Notification to a manager. No state change, no reassignment, no auto-decision |
| Stated as | Observed — "before a manager is notified that this step has not been completed" |

### D Step execution and — [WF-R-048](../rules/WF-R-048.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**Only the same user or a system administrator can release the lock. This is a directly reported defect: "People check out by mistake all the time… I have to manually navigate to each item and check it in." ASG's own proposed fix is recorded verbatim: rename to Lock/Unlock, grant managers the unlock….**

|  |  |
|---|---|
| Stated as | User presses Checkout on a step or form |
| Stated as | current user, today |
| Stated as | — |
| Stated as | `CheckedOutByMemberID`, `CheckedOutDate` set. No expiry exists; only the same user or a sysadmin can release it |
| Stated as | Derived (columns) + Observed (behaviour, feature list line 363) |

### E Approval decisions — [WF-R-049](../rules/WF-R-049.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Vendor definition: "The approver should select the appropriate action for the work flow step from this field." Selecting an action stamps the button pressed, a comment, the date, and HasTakenAction = true onto the approver's own row.**

|  |  |
|---|---|
| Stated as | Approver selects an action |
| Stated as | `WFTSA.WorkFlowTemplateStepActionID`, comment, today |
| Stated as | The member has a `WFSAp` row for this step |
| Stated as | `WFSAp.WorkFlowTemplateStepActionID`, `ActionTakenName`, `ActionTakenDate`, `ActionComment`, `HasTakenAction = true` |
| Stated as | Observed — "The approver should select the appropriate action for the work flow step from this field" |

### E Approval decisions — [WF-R-050](../rules/WF-R-050.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Vendor definition of IsApprovalAction: "Specifies whether the current action is an approval or not. If it is not, then the step is either restarted or denied." The engine knows approve vs not-approve and nothing finer;.**

|  |  |
|---|---|
| Stated as | Approver acts |
| Stated as | `WFTSA.IsApprovalAction` |
| Stated as | true |
| Stated as | `WFSAp.HasApproved = true` |
| Stated as | Observed — "Specifies whether the current action is an approval or not" |

### E Approval decisions — [WF-R-051](../rules/WF-R-051.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Approver acts · `WFTSA.IsApprovalAction` · false · The step is either restarted or denied, per `RestartStep` · Observed — "If it is not, then the step is either restarted or denied".**

|  |  |
|---|---|
| Stated as | Approver acts |
| Stated as | `WFTSA.IsApprovalAction` |
| Stated as | false |
| Stated as | The step is either restarted or denied, per `RestartStep` |
| Stated as | Observed — "If it is not, then the step is either restarted or denied" |

### E Approval decisions — [WF-R-052](../rules/WF-R-052.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**RequireApproverSig forces WorkFlowStepApprover.SignatureDate to be captured before the action counts as taken.**

|  |  |
|---|---|
| Stated as | Approver acts |
| Stated as | `WFTSA.RequireApproverSig` |
| Stated as | true |
| Stated as | `WFSAp.SignatureDate` must be captured |
| Stated as | Observed — "require an approver signature for an action on a work flow step" |

### 3 What should — [WF-R-053](../rules/WF-R-053.md)

*Derived · rule · source: `docs/modules/workflow/asg-edgeplus-mapping.md`*

**Vendor definition of RequireAllApprovers: "require all qualified approvers on the entity to take the same action on the work flow step for the work flow to progress." If qualified approvers choose different actions, the unanimity condition can never be satisfied. This is ASG's loudest reported….**

|  |  |
|---|---|
| Stated as | D2 |
| Stated as | Explicit quorum policy per step: unanimous / first-decisive / N-of-M / weighted; plus an explicit conflict outcome (deny wins, or escalate to a named resolver). |
| Stated as | This is ASG's single loudest complaint about the current system. |
| Stated as | None — it is strictly more capable. Migration maps `RequireAllApprovers = true` → unanimous, `false` → first-decisive. |

### E Approval decisions — [WF-R-054](../rules/WF-R-054.md)

*Inferred · rule · source: `docs/modules/workflow/rules.md`*

**When RequireAllApprovers is false, the first approver to act decides for the whole step. The vendor definition states only the true case, so this reading is Inferred, not confirmed.**

|  |  |
|---|---|
| Stated as | Approver acts |
| Stated as | `WFTSA.RequireAllApprovers` |
| Stated as | false |
| Stated as | The first approver to act decides |
| Stated as | Inferred — the definition states only the true case |

### E Approval decisions — [WF-R-055](../rules/WF-R-055.md)

*Derived · rule · source: `docs/modules/workflow/rules.md`*

**CodeLastActionStatusID writes Issue.CodeLastActionStatusID and Issue.LastActionStatusChangeDate. This is the only field the engine can write on the record it is routing.**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTSA.CodeLastActionStatusID` |
| Stated as | Non-null |
| Stated as | `Issue.CodeLastActionStatusID` = the value; `Issue.LastActionStatusChangeDate` = today. This is the engine's only field-write capability |
| Stated as | Derived — matching type on `Issue` plus its paired change-date column |

### E Approval decisions — [WF-R-056](../rules/WF-R-056.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Vendor definition of DisableEditAfterDecision: "prevents users from making any more changes after the step status is changed to Approved or Denied." This is also the only place in the whole corpus that names two concrete step-status values.**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTSA.DisableEditAfterDecision` |
| Stated as | true |
| Stated as | `WFS.IsReadOnly = true`; no further edits after the status becomes Approved or Denied |
| Stated as | Observed |

### E Approval decisions — [WF-R-057](../rules/WF-R-057.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**RestartStep sets WorkFlowStep.IsReDo = true and pushes the current submission round into the single Prior* slot. Only one prior round survives;.**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTSA.RestartStep` |
| Stated as | true |
| Stated as | `WFS.IsReDo = true`; the current round is pushed to `WFS.PriorSubmitByMemberID`/`PriorSubmitForApprovalDate` and `WFSAp.PriorActionComment`/`PriorActionTakenDate`/`PriorWFTemplateStepActionID`. Only one prior round is retained; a third round overwrites the second |
| Stated as | Observed (the flag and `IsReDo`) + Derived (the single `Prior*` slot) |

### E Approval decisions — [WF-R-058](../rules/WF-R-058.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**MoveToStepNumber is a plain integer the administrator types in. A lower number is a send-back;.**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTSA.MoveToStepNumber` |
| Stated as | Non-null |
| Stated as | The workflow moves to the step with that `StepNumber`. A lower number is a send-back; nothing distinguishes it from forward movement |
| Stated as | Observed |

### E Approval decisions — [WF-R-059](../rules/WF-R-059.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Vendor definition: "automatically launch the next step if it is a form." Precedence against MoveToStepNumber and RestartStep is unstated (OQ-15, OQ-16).**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTS.AutoLaunchNextStep` |
| Stated as | true and the next step is a Form step |
| Stated as | The next step launches automatically. Precedence against `MoveToStepNumber` is unstated |
| Stated as | Observed — "automatically launch the next step if it is a form"; precedence per OQ-16 |

### E Approval decisions — [WF-R-060](../rules/WF-R-060.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**NotifyStepAssigneesComplete, NotifyStepApproversComplete, NotifyPriorAssigneesComplete, NotifyPriorApproversComplete and NotifyInitiatorComplete are the complete set. All five share the step's single EMailMessage body and its two channel switches;.**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTSA.NotifyStepAssigneesComplete`, `NotifyStepApproversComplete`, `NotifyPriorAssigneesComplete`, `NotifyPriorApproversComplete`, `NotifyInitiatorComplete` |
| Stated as | each true |
| Stated as | Email to that audience, using the step's single `EMailMessage` body and its two channel switches. These five are the complete audience model; notifiees are not among them |
| Stated as | Observed (all five) + Derived (the absence of notifiees) |

### E Approval decisions — [WF-R-061](../rules/WF-R-061.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**Action completes · `WFTSA.AutoCopyAmounts`, `PageLayout.IsBudgetImpacting` · true · Budget-impacting values are copied into a custom list on the next step, via the Custom Lists Copy To mechanism. ⊘ Cost Management is out of scope — do not implement.**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTSA.AutoCopyAmounts`, `PageLayout.IsBudgetImpacting` |
| Stated as | true |
| Stated as | Budget-impacting values are copied into a custom list on the next step, via the Custom Lists Copy To mechanism. ⊘ Cost Management is out of scope — do not implement. Retained because it is the engine's only step-to-step data-flow mechanism, so its narrowness is the finding: ASG Edge+ must design step-to-step data flow from scratch |
| Stated as | Observed |

### E Approval decisions — [WF-R-062](../rules/WF-R-062.md)

*Observed · rule · source: `docs/modules/workflow/rules.md`*

**An action with CloseWorkFlow = true sets WorkFlow.IsCompleted, ClosedDate and a terminal CodeWorkFlowStatusID, and fires the three template-level completion notifications read live off WorkFlowTemplate.**

|  |  |
|---|---|
| Stated as | Action completes |
| Stated as | `WFTSA.CloseWorkFlow` |
| Stated as | true |
| Stated as | `WF.IsCompleted = true`, `WF.ClosedDate` = today, terminal `WF.CodeWorkFlowStatusID`; `WFT.NotifyInitiatorComplete`, `NotifyAllApproversComplete`, `NotifyAllAssigneesComplete` fire (read live off the template) |
| Stated as | Observed |
