# Step actions — the full catalog and the action taxonomy

**Stated up front.** `WorkFlowTemplateStepAction` is where the engine's entire expressiveness
lives, and it is **narrower than it looks**. Of 38 fields, 11 are bookkeeping, 8 are dead or
finance-specific side effects, and the actual behavioural surface is **19 flags**. Those 19 express
exactly six kinds of effect: *decide* (approve / not-approve, with a quorum and an optional
signature), *move* (jump to a numbered step, restart this step, or close the workflow), *stamp a
status* (`CodeLastActionStatusID`), *lock* (`DisableEditAfterDecision`), *notify* (five fixed
audiences), and *spawn* (kick off another workflow template, optionally carrying the ad-hoc
assignee and priority across). It cannot write an arbitrary field, cannot evaluate a condition,
cannot call an external system, and cannot compute anything — except by executing a raw JavaScript
string held in `IsEnabledLxJSCode`.

**The engine has no conditional branching. The branch predicate is the human choosing which button
to press.** `MoveToStepNumber` is a plain integer on the action, not an expression, and there is no
condition column anywhere on the object. **Derived** — full field list below; exhaustive.

> ## ⚠ This object has not been seen in the live UI
>
> The live capture (`../layouts-and-forms/forms-vs-pages-vs-layouts.md`) reached the workflow list
> and the step grid, but **no action editor was opened and no `WorkFlowTemplateStepAction` row was
> rendered**. Everything in this document is read off the schema and the vendor's field help.
>
> That matters more here than anywhere else in this folder, because the step grid is strictly
> ordinal (steps 1..N, no branch construct visible) — so **the entire question of whether the engine
> can branch at all rests on this unobserved object**. The schema says it can, via
> `MoveToStepNumber`. Confirming that against a real action row is the highest-value screen left to
> open; see **OQ-43** below.
>
> The live grid surfaces six columns against `WorkFlowTemplateStep`'s 55 fields, and zero of
> `WorkFlowTemplateStepAction`'s 37. Roughly 90% of the step model and 100% of the action model
> remain schema-derived.

## Full field catalog

38 fields: 37 physical columns from `_lucernex_objects_summary.txt` line 223, plus
`bidAwdApCodeLastActionStatusID` which exists only in the Manage Data Fields catalog. Definitions
are **Observed** vendor help text from `_xlsx_lucernex_jcrew.txt`; empty definitions mean the vendor
ships no help for that field.

| Field | Schema type | UI label | Req | Definition (vendor help text) |
|---|---|---|---|---|
| `ActionComment` | Text | Action Comment |  | This field captures any comments left by the approver on the approver's action. |
| `AutoClearAmounts` | Boolean | Auto Clear Amounts |  |  |
| `AutoCopyAmounts` | Boolean | Auto Copy Amounts |  | This setting automatically copies budget-impacting values into a custom list in the next step of the work flow. This feature works together with the existing Copy To functionality for custom lists, and is recommended when using Budget Custom Lists in your work flow. |
| `bidAwdApCodeLastActionStatusID` *(catalog only)* | — | Bid Award Approval Status |  |  |
| `BOMapClientRecordID` | Text | Work Flow Template Step Action ClientID | Y | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". |
| `CloseWorkFlow` | Boolean | Action Should Close Work Flow? | Y | This setting will close the current work flow after this step has been completed. |
| `CodeLastActionStatusID` | Dropdown (Last Action Status Code) | Last Action Status |  |  |
| `CreatedByID` | Member ID | Created By |  | The Created By field is a system-populated field which captures the name of the member making changes to a record. |
| `CreatedDate` | Time | Created Date |  | The Created Date field is a system-populated field which captures the date that a record was created. |
| `Description` | Text | Description |  | Write a description of the record. |
| `DisableEditAfterDecision` | Boolean | Action Should Disable Edit? | Y | This setting prevents users from making any more changes after the step status is changed to Approved or Denied. |
| `FifoPayApp` | Boolean | Apply FIFO Pay App Validation |  |  |
| `GenPurchOrderLineSeqNum` | Boolean | Generate Purchase Order Line Sequence Number |  |  |
| `IsApprovalAction` | Boolean | Is Approval Action? | Y | Specifies whether the current action is an approval or not. If it is not, then the step is either restarted or denied. |
| `IsEnabledLxJSCode` | Text | Javascript Source Code |  | If you are creating a custom action using JavaScript, enter the JavaScript in this field. |
| `KickOffDescription` | Text | Kick Off Description |  | The description of the work flow kick off trigger. |
| `KickOffTargetWFTemplateID` | Number | Kick Off Work Flow Template Trigger |  | Returns the workflow template kickoff trigger value, a number associated with a workflow template. |
| `KickOffWorkFlowTemplateID` | Work Flow ID | Kick Off Work Flow Template |  | If you want to kick off another work flow with the completion of this action, select the work flow from this field. |
| `ModifiedByID` | Member ID | Modified By |  | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. |
| `ModifiedDate` | Time | Modified Date |  | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. |
| `MoveToStepNumber` | Number | Action Should Move to Next Step Number |  | If you want to move to a specific step number with the completion of this action, enter the step number in this field. |
| `NotifyInitiatorComplete` | Boolean | Notify Initiator on Complete? | Y | Select this check box if you want to send a notification to the initiator of this step once the step is complete. |
| `NotifyPriorApproversComplete` | Boolean | Notify Prior Approvers on Complete? | Y | Select this check box if you want to send a notification to all prior approvers of this step once this step is complete. |
| `NotifyPriorAssigneesComplete` | Boolean | Notify Prior Assignees on Complete? | Y | If set to true, prior assignees are notified by email when the workflow step is completed. |
| `NotifyStepApproversComplete` | Boolean | Notify Step Approvers on Complete? | Y | If set to true, step approvers are notified by email when the workflow step is completed. |
| `NotifyStepAssigneesComplete` | Boolean | Notify Step Assignees on Complete? | Y | If set to true, step assignees are notified by email when the workflow step is completed. |
| `PassAdhocToNewWF` | Boolean | Pass Adhoc Assignee To New Work Flow? | Y | This setting will assign the ad hoc member assigned to this task to the first task in the new work flow kicked off by this step. |
| `PassPriorityToNewWF` | Boolean | Pass Priority To New Work Flow? | Y | This setting will transfer the priority level of this work flow to a new work flow that is kicked off by this step. |
| `ProjectEntityID` | Entity ID | WF Step Action Entity |  | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. |
| `RequireAllApprovers` | Boolean | Require All Approvers? | Y | Select this check box if you want to require all qualified approvers on the entity to take the same action on the work flow step for the work flow to progress. |
| `RequireApproverSig` | Boolean | Require Approver Signature |  | Select this check box if you want to require an approver signature for an action on a work flow step. |
| `RestartStep` | Boolean | Action Should Restart the Step? | Y | Select this option button if this action should trigger the step to restart. |
| `RevNumber` | Number | Rev Number |  | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. |
| `SendPaymentInfo` | Boolean | Send Payment Info? | Y | This field is not implemented. |
| `WorkFlowTemplateKickOffID` | Number | Work Flow Template Kick Off |  | Specifies the action type and the WorkFlow that gets kicked off. |
| `WorkFlowTemplateStepActionID` | Number | Work Flow Template Step Action RecID |  | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. |
| `WorkFlowTemplateStepActionName` | Text | Action Name | Y | Enter the name of the action in this field. |
| `WorkFlowTemplateStepID` | Step ID | Work Flow Template Step |  | The ID of the work flow step that this action is associated with. |

## The action taxonomy

Eight categories. Category assignment is **Derived**; the evidence for each is the vendor
definition quoted in the catalog above.

### A. Identity and bookkeeping — 11 fields, no behaviour

`WorkFlowTemplateStepActionID`, `WorkFlowTemplateStepActionName`, `Description`,
`WorkFlowTemplateStepID`, `BOMapClientRecordID`, `ProjectEntityID`, `RevNumber`, `CreatedByID`,
`CreatedDate`, `ModifiedByID`, `ModifiedDate`.

`WorkFlowTemplateStepActionName` is what the approver sees on the button — *"Enter the name of the
action in this field."* The canonical set (Approve, Reject, Send Back) is **not** enumerated
anywhere in the schema; action names are free text per template. **Derived.** The engine has no
notion of a standard action vocabulary, which is why S4 line 353 reports *"There is no obvious,
standard Send Back to Previous Step or Request Rework action."*

### B. Decision semantics — 4 fields

| Field | Effect | Evidence |
|---|---|---|
| `IsApprovalAction` | *"Specifies whether the current action is an approval or not. **If it is not, then the step is either restarted or denied.**"* | **Observed** |
| `RequireAllApprovers` | *"…require all qualified approvers **on the entity** to take **the same action** on the work flow step for the work flow to progress."* | **Observed** |
| `RequireApproverSig` | *"…require an approver signature for an action on a work flow step."* Writes `WorkFlowStepApprover.SignatureDate`. | **Observed** |
| `ActionComment` | Prefilled/captured comment. *"This field captures any comments left by the approver on the approver's action."* Lands in `WorkFlowStepApprover.ActionComment`. | **Observed** |

`IsApprovalAction` is a **binary** — the engine knows approve vs not-approve and nothing else.
Denial and send-back are the same class; they differ only in what `RestartStep` /
`MoveToStepNumber` do afterwards. **Derived** from the quoted definition.

`RequireAllApprovers` is the quorum rule and it is **per action, not per step**. Two actions on the
same step may disagree about whether unanimity is required. Its definition says *"all qualified
approvers **on the entity**"* — not "all approvers on this step" — which suggests resolution
against the entity roster at decision time rather than against the frozen
`WorkFlowStep.ApproverMemberIDList`. **Open question OQ-14.** This wording is also the direct cause
of the reported "all-for-one" assignment overload (S4 line 360).

### C. Control flow — 3 fields

| Field | Effect | Evidence |
|---|---|---|
| `MoveToStepNumber` | *"If you want to move to a specific step number with the completion of this action, enter the step number in this field."* | **Observed** |
| `RestartStep` | *"Select this option button if this action should trigger the step to restart."* Sets `WorkFlowStep.IsReDo`. | **Observed** |
| `CloseWorkFlow` | *"This setting will close the current work flow after this step has been completed."* Sets `WorkFlow.IsCompleted`, `ClosedDate`, terminal `CodeWorkFlowStatusID`. | **Observed** |

This is the **entire** control-flow vocabulary. Consequences, all **Derived**:

- The workflow graph is a **state machine over integers**, where the transition function is
  `(StepNumber, ActionID) → StepNumber`. Edges are stored scattered across action rows; nothing
  materialises the graph. That is why no visualiser exists (S4 lines 330, 350).
- **Backward movement is possible but not distinguished.** Setting `MoveToStepNumber` to a lower
  number is a send-back. Nothing marks it as such, so no reporting can distinguish rework loops
  from forward progress.
- **`RestartStep` and `MoveToStepNumber` are independent Booleans/values with no stated
  precedence.** An action can set both. **Open question OQ-15.**
- **There is no fan-out, no fan-in, no join, no parallel branch.** One action moves the whole
  workflow to exactly one step.
- **There is no "next step" primitive.** Advancing to the following step requires the administrator
  to type its `StepNumber` into every relevant action, or to leave `MoveToStepNumber` null and rely
  on `WorkFlowTemplateStep.AutoLaunchNextStep`. The two mechanisms interact and their precedence is
  unstated. **Open question OQ-16.**
- Note that `AutoLaunchNextStep`'s definition adds a condition the action flags do not: *"…
  automatically launch the next step **if it is a form**."* Task steps apparently do not auto-launch.

### D. Record-state write — 3 fields

| Field | Effect | Evidence |
|---|---|---|
| `CodeLastActionStatusID` | Stamps a value from the `Last Action Status Code` firm dropdown. Lands on `Issue.CodeLastActionStatusID` and `Issue.LastActionStatusChangeDate`. | **Derived** — the same `sCODE_LAST_ACTION_STATUS` type appears on `Issue`, and `Issue` carries a paired change-date column. |
| `bidAwdApCodeLastActionStatusID` ⊘ | Same type, labelled "Bid Award Approval Status". Catalog-only. **⊘ out-of-scope-but-structural** — one of the object's 38 fields. | **Observed** label; effect **Inferred**. |
| `DisableEditAfterDecision` | *"This setting prevents users from making any more changes after the step status is changed to **Approved or Denied**."* Sets `WorkFlowStep.IsReadOnly`. | **Observed** |

**This is the only field-write capability the engine has, and it writes exactly one field.** There
is no generic "set field X to value Y" action. The definition of `DisableEditAfterDecision` is also
the only place in the whole corpus that names concrete step statuses — **Approved** and
**Denied**. Those two values are therefore **Observed** members of `Work Flow Status Code`.

### E. Notification fan-out — 5 fields

All five are Boolean, all fire *on completion of the action*, and together they enumerate the
engine's **complete** audience model.

| Field | Audience | Evidence |
|---|---|---|
| `NotifyStepAssigneesComplete` | Assignees of **this** step | *"If set to true, step assignees are notified by email when the workflow step is completed."* **Observed** |
| `NotifyStepApproversComplete` | Approvers of **this** step | **Observed** |
| `NotifyPriorAssigneesComplete` | Assignees of **all earlier** steps | *"…all prior approvers of this step…"* / *"prior assignees are notified by email…"* **Observed** |
| `NotifyPriorApproversComplete` | Approvers of **all earlier** steps | **Observed** |
| `NotifyInitiatorComplete` | `WorkFlow.InitiatedByMemberID` | *"…send a notification to the initiator of this step once the step is complete."* **Observed** |

Notice what is **absent**: notifiees (`NotifieeMemberIDList`) are **not** an audience for
action-completion notifications. The step's `Notifiee*` routing is used only for the
*step-completed* notification configured at step level — S2 says the notifiee lists select *"the
members that should receive a notification once this work flow task is completed"*. So there are
two overlapping completion-notification mechanisms, one on the step and one on each action, with no
stated interaction. **Open question OQ-17.**

Also absent: any per-audience message, subject, or template. All five flags share the step's single
`EMailMessage` body and the step's two channel switches. **Derived.**

### F. Sub-workflow spawn — 6 fields

| Field | Effect | Evidence |
|---|---|---|
| `KickOffWorkFlowTemplateID` | *"If you want to kick off another work flow with the completion of this action, select the work flow from this field."* | **Observed** |
| `KickOffTargetWFTemplateID` | *"Returns the workflow template kickoff trigger value, a number associated with a workflow template."* | **Observed**, meaning unclear |
| `WorkFlowTemplateKickOffID` | *"Specifies the action type and the WorkFlow that gets kicked off."* | **Observed**, meaning unclear |
| `KickOffDescription` | *"The description of the work flow kick off trigger."* | **Observed** |
| `PassAdhocToNewWF` | *"…assign the ad hoc member assigned to this task to the first task in the new work flow kicked off by this step."* | **Observed** |
| `PassPriorityToNewWF` | *"…transfer the priority level of this work flow to a new work flow that is kicked off by this step."* | **Observed** |

Three overlapping ID columns for one concept (`KickOffWorkFlowTemplateID`,
`KickOffTargetWFTemplateID`, `WorkFlowTemplateKickOffID`) mirror the same three-column redundancy on
`WorkFlowTemplate` (`KickOffID`, `StatusChangeID`, `StatusChangeType`). **Open question OQ-18.**

The GraphQL enum names this path explicitly: `KickOffMethod: [STEP_ACTION, PAGE_LAYOUT,
STATUS_CHANGE, TASK]` (**Observed**, `../../data-model/graphql-api.md`). `STEP_ACTION` **is** this
category — a workflow triggered by an action on a preceding workflow step. The enum also settles
something the vendor help got wrong: there are **four** kick-off methods, not the three the help
text lists. `STATUS_CHANGE` is the missing one, and it explains the otherwise-undocumented
`WorkFlowTemplate.StatusChangeID` / `StatusChangeType` pair. See
[`rules.md` WF-R-014](rules.md#b-kick-off-and-instantiation).

**Exactly two things cross the boundary into a spawned workflow: the ad-hoc assignee and the
priority.** No data, no context, no reference to the parent. Combined with the absence of a parent
pointer on `WorkFlow` (OQ-5), a spawned workflow is an orphan. **Derived.** For a rebuild in a
SOX/SOC-2 context this is a defect to fix, not a behaviour to replicate.

### G. Cost Management side effects — 6 fields, out of scope

> **⊘ Cost Management and Budgeting are out of scope** (2026-09-10, per the user via team-lead).
> These fields are retained, not deleted, because they are **columns on
> `WorkFlowTemplateStepAction`, an in-scope object**, and because they are load-bearing for the
> can/cannot-express matrix below: they are the *entire* set of business operations the engine can
> perform, so omitting them would make the engine look more general than it is. **Do not build Cost
> Management functionality off this table.** `bidAwdApCodeLastActionStatusID` (category D) carries
> the same marker, making six in total.

These are hard-coded operations against the capital-project cost and procurement modules — the
engine's only "business action" capability, and it is a closed set.

| Field | Effect | Evidence |
|---|---|---|
| `AutoCopyAmounts` | *"automatically copies budget-impacting values into a custom list in the next step of the work flow. This feature works together with the existing **Copy To** functionality for custom lists, and is recommended when using **Budget Custom Lists** in your work flow."* | **Observed** |
| `AutoClearAmounts` | No vendor help. Presumably the inverse. | **Inferred** |
| `FifoPayApp` | "Apply FIFO Pay App Validation" — no help text. Validates pay applications in first-in-first-out order against `PayApp`. | **Inferred** from the label + the `PayApp` object |
| `GenPurchOrderLineSeqNum` | "Generate Purchase Order Line Sequence Number" — no help text. Writes `PurchaseOrder.PurchaseOrderSequenceNumber`. | **Inferred** |
| `SendPaymentInfo` | *"**This field is not implemented.**"* | **Observed** — dead |

`AutoCopyAmounts` is the closest thing to data flow between steps that the engine has, and it works
only for Custom Lists on budget-impacting layouts. `PageLayout.IsBudgetImpacting` is the flag that
enables it. **Derived** (`../../data-fields/page-layout.md`).

**The structural point survives the scope cut, and it is the one worth keeping:** the engine has
**no general mechanism for passing data from one step to the next**. Its single exception is
hard-coded to an out-of-scope module. For ASG Edge+ that means step-to-step data flow must be
designed from scratch — there is nothing here to port.

### H. Escape hatch — 1 field

`IsEnabledLxJSCode` — *"If you are creating a custom action using JavaScript, enter the JavaScript
in this field."* **Observed.**

This is the engine's only general-purpose extension point, and it appears twice: here, and on
`WorkFlowTemplate` where its definition is *"custom JavaScript used to kick off conditional work
flows."* So **all conditional logic in Lucernex workflows is tenant JavaScript stored in a text
column.** No sandbox, no signature, no version, no test surface. **Derived.**

## What the engine can and cannot express

| Capability | Supported? | Mechanism | Confidence |
|---|---|---|---|
| Change the workflow/step status | Yes | `IsApprovalAction`, `CloseWorkFlow`, `RestartStep` → `CodeWorkFlowStatusID`, `IsReDo` | Derived |
| Stamp a business status on the form | Yes, one field only | `CodeLastActionStatusID` → `Issue.CodeLastActionStatusID` | Derived |
| Write an arbitrary field on the target record | **No** | — | Derived (exhaustive field list) |
| Lock the record from further edits | Yes | `DisableEditAfterDecision` → `WorkFlowStep.IsReadOnly` | Observed |
| Send a notification | Yes, five fixed audiences, one shared body | The five `Notify*Complete` flags | Observed |
| Branch on a condition | **No** | The human picks the button; only `IsEnabledLxJSCode` can compute | Derived |
| Jump to a specific step | Yes | `MoveToStepNumber` | Observed |
| Loop / rework | Yes | `RestartStep`, or `MoveToStepNumber` < current | Observed |
| Fan out to parallel branches | **No** | — | Derived |
| Join / merge branches | **No** | — | Derived |
| Spawn a sub-process | Yes, fire-and-forget | `KickOffWorkFlowTemplateID` | Observed |
| Return a result from a sub-process | **No** | No parent pointer, no callback | Derived |
| Call an external system | **No** | — | Derived |
| Run a scheduled job at step start/end | **No** — designed but never shipped | `runAt*ScheduledJob*` are catalog-only placeholders | Observed |
| Require a quorum | Yes, all-or-any only | `RequireAllApprovers` | Observed |
| Require a signature | Yes | `RequireApproverSig` → `WorkFlowStepApprover.SignatureDate` | Observed |
| Enforce an approval amount limit | **No, not from the action** | `Member.PaymentApprovalMin/MaxAmount`, `RecurringApprovalMin/MaxAmount`, `EquipPaymentApprovalMin/MaxAmount`, `EquipRecurringApprovalMin/MaxAmount` exist on `Member` but no action field references them | Derived |
| Time-based auto-escalation | Partial — notify only, never reassign or auto-decide | `DaysUntilWarn*` / `DaysUntilAlert*` on the step | Observed |
| Copy data between steps | **Effectively no** — the only mechanism is `AutoCopyAmounts`, hard-coded to budget amounts into a Custom List (⊘ out of scope). There is no general step-to-step data flow | `AutoCopyAmounts` | Observed |

The **approval-limit** row is significant. `Member` carries eight approval-threshold currency
columns (**Observed**, S1 line for `Member`), which is the classic shape of amount-banded approval
routing — but nothing on `WorkFlowTemplateStep` or `WorkFlowTemplateStepAction` reads them. Either
the routing is done outside the workflow engine (in the payment-approval module reached by the
`APPROVE_PAYMENTS` / `APPROVE_ASSET_PAYMENTS` submit buttons on `ProjectEntity`), or amount-banded
routing is done by hand-written `IsEnabledLxJSCode`. **Open question OQ-19** — and a first-class
requirement for ASG Edge+, where amount-banded lease approvals are a certainty.

## What the live configuration implies about actions

Nothing about `WorkFlowTemplateStepAction` was rendered, but the step grid constrains it indirectly.
All inferences here are **Derived** from `../layouts-and-forms/forms-vs-pages-vs-layouts.md`.

| Observation | What it implies about actions |
|---|---|
| All 19 steps are strictly ordinal 1..N; no branch, merge or parallel construct is rendered | Either no live action sets `MoveToStepNumber` to anything but *current + 1*, or the grid simply cannot render branches. The grid has no column that *could* show a jump target, so **absence of branching in the grid is not evidence of absence in the configuration.** |
| `Rent Payment Review/Approval` has three consecutive approval steps (ASG → LA → Client) | A denial at step 3 or 4 must go somewhere. Either an action carries `MoveToStepNumber` pointing back, or `RestartStep`, or the process has no rejection path at all. This is the cleanest live case to inspect for backward transitions. |
| `Lease Admin Request` step 6 is *Finalize* and step 7 is *Finalize … (Defaults)* | Two near-identical consecutive steps is the shape you get when an engine **cannot branch**: rather than one step with a conditional path, the administrator has laid out both outcomes in sequence. **Inferred**, but it is the sort of workaround that indicates a missing capability. |
| Every workflow ends in a terminal-sounding step — *Approve … (Client)*, *Complete Lease Admin Request*, *Final Rent Payment File*, *Submit Revisions* | Each of these final steps almost certainly carries an action with `CloseWorkFlow = true`. Confirming one closes **OQ-37** (what closes a workflow whose last step completes). |
| The `Form/Task` column shows the bound layout suffixed `(Approvers)` | Confirms `PageLayoutApproversID` is per-step and rendered; `PageLayoutAssigneesID` exists but is not on this grid. An action's `DisableEditAfterDecision` therefore locks a surface that differs by role. |

**The one thing the live data does establish about actions:** the `Approver` column is populated for
17 of 19 steps, so approvers are configured and therefore *actions must exist for them to press*.
The engine is in real use; the action rows are there, just not on this screen.

## Action buttons on page layouts

`sTYPE_SUBMITBUTTON` fields are *"Form action button that triggers a server-side process — not a
stored data value"* — 62 of them across the catalog (**Observed**,
`docs/data-fields/INDEX.md` line 44). They are placeable on page layouts alongside data fields:
*"Page layouts in Lucernex are not purely data-field surfaces — they also host placeable,
reorderable business-action buttons, wired to backend workflows"* (**Observed**,
`docs/admin/008-manage-page-layouts.md` lines 140-146, which captured `Approve Payments`,
`Generate Rent`, `Extend Contracts`, `Delete Payments`, `Alternate Rent Wizard`,
`Activate/Deactivate` on the ASG Contract Summary layout).

**These are a different mechanism from `WorkFlowTemplateStepAction` and must not be conflated.**
Submit buttons are platform-defined server procedures bound to a layout; step actions are
tenant-defined rows bound to a workflow step. The one that connects them is
`ProjectEntity.FormSubmitButton` (label **Submit**) — **Derived**: this is the button that writes
`WorkFlowStep.SubmitForApprovalByMemberID` / `SubmitForApprovalDate` and hands a form step from its
assignees to its approvers.

Workflow-relevant submit buttons observed in `all-fields.csv`:

| Button | Entity | Reading |
|---|---|---|
| `FormSubmitButton` (Submit) | `ProjectEntity` | Submits a form step for approval. **Derived.** |
| `APPROVE_PAYMENTS`, `APPROVE_ASSET_PAYMENTS` | `ProjectEntity` | Bulk payment approval — a separate approval path from the workflow engine. |
| `GenerateServiceRequest` | `Asset` | Creates an `Issue` of Service Request type. |
| `GenerateWorkOrder` | `ServiceRequest` | Creates a `WorkOrder` from a service request. |
| `InviteBidders`, `NotifyAllBidders`, `NotifyWinningBidder`, `NotifyLosingBidders`, `CanceledBidNotification` ⊘ | `BidPackage` | The bidding workflow's notification actions. **⊘ out-of-scope-but-structural** — retained only as evidence that notification can be a placeable layout button rather than a step-action flag. |

## Open questions

1. **OQ-43 — Open the action editor.** Nothing in this document is Observed in the running system.
   In **Manage Work Flows** → `Rent Payment Review/Approval` → step 2 or 3 (`Approve Rent Preview
   File`), open the step and then its actions. Capture: how many actions exist, their names, and
   every field rendered — in particular `Is Approval Action?`, `Action Should Move to Next Step
   Number`, `Action Should Restart the Step?`, `Action Should Close Work Flow?`, `Require All
   Approvers?` and `Last Action Status`. **This one screen converts the whole control-flow model
   from Derived to Observed** and answers OQ-14, OQ-15, OQ-16, OQ-20 and OQ-37 at the same time.
2. **OQ-44 — Does any live action set `MoveToStepNumber`?** Specifically: what happens when an
   approver denies at `Rent Payment Review/Approval` step 3 or 4? If a backward jump exists, the
   engine branches in production and the ordinal grid is simply hiding it. If it does not, ASG has
   no rejection path and that is a requirement gap for the rebuild, not a modelling detail.
3. **OQ-19 — How is amount-banded approval routing done?** `Member` carries eight approval-limit
   currency columns that no workflow field references. `Rent Payment Review/Approval` is the live
   process where amount banding would be expected — check its steps for any threshold; then open a
   `Member` record and check whether *Payment Approval Min/Max Amount* is populated. ASG Edge+ will
   certainly need amount-banded lease and payment approvals.
4. **OQ-16 — `MoveToStepNumber` vs `AutoLaunchNextStep`: which wins?** Configure a step with
   `AutoLaunchNextStep = true` and an action with `MoveToStepNumber = 5`, fire it, and observe which
   step becomes current.
5. **OQ-15 — `RestartStep` + `MoveToStepNumber` set together: what happens?** Configure both on one
   action and fire it.
6. **OQ-14 — Does `RequireAllApprovers` mean all *qualified approvers on the entity* or all
   *approvers on the step*?** The wording says the former, which would make the quorum re-resolve
   at decision time. Add a member to the entity with a matching job title *after* the step starts,
   then try to complete the step.
7. **OQ-17 — Step-level notifiees vs action-level `Notify*Complete`: do both fire?** Configure a
   step with a notifiee list *and* an action with `NotifyStepApproversComplete`, fire it, and check
   the **Email Log** (`/en/reports/EMailLogs.jsp`) for how many messages were sent.
8. **OQ-18 — What distinguishes `KickOffWorkFlowTemplateID`, `KickOffTargetWFTemplateID` and
   `WorkFlowTemplateKickOffID`?** Configure a kick-off action and read all three values back.
9. **OQ-20 — Is there a standard action vocabulary in the UI?** Open the action editor for a step
   and record whether *Action Name* is free text or a picklist, and what the seeded actions on a
   platform template are called.
10. **OQ-21 — What does `AutoClearAmounts` do?** No vendor documentation exists. Check the field's
   tooltip in the action editor.
