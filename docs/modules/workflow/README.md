# Workflow, Approval & Task Engine — module overview

**Stated up front.** Lucernex's workflow engine is a *step-numbered, template-instantiated approval
router*, not a general-purpose BPM engine. **The live tenant confirms the shape:** four workflows
exist, they carry 19 steps between them, every step is ordinal (1..N), and no branch, merge or
parallel construct is visible anywhere in the configuration
(**Observed**, `../layouts-and-forms/forms-vs-pages-vs-layouts.md`). A `WorkFlowTemplate` owns an
ordered list of `WorkFlowTemplateStep` rows keyed by an integer `StepNumber`; each step publishes a
menu of `WorkFlowTemplateStepAction` buttons; each action is a **declarative bundle of Boolean
flags** — approve or deny, jump to step *N*, restart this step, close the workflow, spawn another
workflow, notify these five audiences. **The branching predicate is the human's choice of button.**
The only condition language is a raw JavaScript blob (`IsEnabledLxJSCode`).

**The single most important live finding is layout-per-step-per-role.** A Form type has many page
layouts and their names are step names — `LAR Submit…`, `LAR Initial Review…`, `LAR Abstract Lease
Document`, `LAR ASG Review…`, `LAR Client Review…` and so on. The same underlying record shows a
**different field surface at every stage, to a different person**. That, not the control flow, is
what makes the engine expressive enough to run a real business process. See
[`template-vs-instance.md` §3a](template-vs-instance.md#3a-layout-per-step-per-role--the-real-source-of-expressiveness).

The three object families in scope are distinct and must not be conflated:

| Family | Root object | What it is | Admin screen |
|---|---|---|---|
| **Form** | `Issue` (56 cols) | **A Form *is* an Issue Type.** `TableType=2035` is `Issue Type Code` (**Observed**, `../../data-model/code-table-registry.md`), so the four "form types" are four rows in a code table and the record a Form produces is an `Issue`. `IssueInterface` is a declared GraphQL interface. Nine typed subtypes extend it by carrying `IssueID`. | Manage Forms — `/en/admin/FirmCodeEdit.jsp?…TableType=2035&tableName=Manage%20Forms` |
| **Schedule** | `Task` / `TaskGroup` / `TaskItem` (37 cols each, identical) | Gantt-style schedule rows with baseline/projected/actual triads, `TaskPredecessor` dependency edges, critical path, percent complete. | Manage Schedule Templates — `/en/admin/TaskTemplateEdit.jsp` |
| **Workflow** | `WorkFlowTemplate` → `WorkFlow` | The approval routing that runs *over* a Form or a Task. | Manage Work Flows — `/en/workflow/WorkFlowTemplateEdit.jsp` |

All three routes are **Observed** — `../../admin/004-company-administration.md` lines 57-66.

**Form and Work Flow are 1:1.** `Manage Forms` and `Manage Work Flows` list exactly the same four
names, and every Form type reports `WORK FLOW field set? = Yes` (**Observed**,
`../layouts-and-forms/forms-vs-pages-vs-layouts.md`). The Form is the record; the Work Flow is its
process. `CodeIssueType.IsWorkFlow` is the column behind that checkbox — a reading that was
Inferred before the live capture and is now **Observed**.

## The four live workflows

**Observed** — `../layouts-and-forms/forms-vs-pages-vs-layouts.md`. These are ASG's real, running
processes and they are the best available statement of what the rebuild must support.

| Workflow | Steps | Sequence prefix | Attachable to | Approval levels used |
|---|---:|---|---|---|
| ASC 842 Schedule Review/Approval | 3 | `ASR` | Portfolio, RE Contract | Member ×3 |
| Lease Admin Request | 8 | `LAR` | Portfolio, RE Contract | Member ×8 |
| Rent Payment Review/Approval | 6 | `RPR` | *(not captured)* | Member ×5, **Ad Hoc** ×1 |
| User Request | 2 | *(none shown)* | *(not captured)* | **Job Title** ×1, **Ad Hoc** ×1 |

19 steps total (3 + 8 + 6 + 2), **all of type `Form`; not one `Task` step is configured anywhere in
the tenant**. The source document states 22; the four per-workflow tables in it sum to 19.

Three of the four are lease-accounting processes and they say something the BRDs do not:

- **ASC 842 Schedule Review/Approval** — schedules are *not* auto-published. Produce → internal
  review → ASG approval → client approval. The accounting engine needs a review gate, not just a
  calculation.
- **Lease Admin Request** — the contract-setup process, in production configuration: initial review
  → abstract the lease document → ASG review → client review → import payment history/sales →
  finalize → finalize (defaults) → complete.
- **Rent Payment Review/Approval** — the payment run is preview → approve (×3) → **generate**, with
  file generation as its own workflow step rather than a side effect.

## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | Every object, every field, every FK edge, the ER diagram, and the GraphQL enums that pin down the rule vocabulary. |
| [`template-vs-instance.md`](template-vs-instance.md) | Field-level correspondence between `WorkFlowTemplate(Step)` and `WorkFlow(Step)`: 20 copied, 35 template-only, 30 instance-only, the hybrid snapshot/live-read hazard, and the layout-per-step-per-role mechanism. |
| [`step-actions.md`](step-actions.md) | The full 39-field `WorkFlowTemplateStepAction` catalog and the eight-category action taxonomy. **Still entirely unobserved in the live UI** — the highest-value screen left to open. |
| [`routing-and-approvals.md`](routing-and-approvals.md) | Approver vs assignee vs notifiee; the reconciliation of three competing routing vocabularies (UI `Approval Level`, vendor help, GraphQL enums); quorum, escalation, ad-hoc, reassignment. |
| [`issues-and-tasks.md`](issues-and-tasks.md) | The `Issue`/`Task` families, the nine Form subtypes, and the now-Observed attachability model. |
| [`state-machine.md`](state-machine.md) | The Observed linear baseline plus the schema-implied state model, as Mermaid diagrams with confidence labels. |
| [`rules.md`](rules.md) | `WF-R-001`…`WF-R-062` in rule-engine form: trigger, inputs, condition, effect, confidence. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What ASG Edge+ has, what must be built, what should deliberately differ, and the decisions blocking a build. |

## The eight facts a rebuild must not get wrong

1. **Steps are addressed by integer, not by edge.** `WorkFlowTemplateStep.StepNumber` and
   `WorkFlowTemplateStepAction.MoveToStepNumber` are plain numbers. No `WorkFlowStepPredecessor`
   exists in the 223-object schema — `TaskPredecessor` belongs to the *schedule*. **Derived**
   (exhaustive search), and **corroborated Observed**: all 19 live steps are strictly ordinal with
   no branch construct rendered.
2. **A workflow is triggered four ways, not three.** The GraphQL enum is
   `KickOffMethod: [STEP_ACTION, PAGE_LAYOUT, STATUS_CHANGE, TASK]` (**Observed**,
   `../../data-model/graphql-api.md`). The vendor help text names only three — *"by completion of an
   action in another work flow, by completion of a schedule task, or by completion of a form"* — and
   **omits `STATUS_CHANGE`**. That fourth method is why `WorkFlowTemplate` carries `StatusChangeID`
   and `StatusChangeType`, two columns the help text never explains. A record's status changing can
   start a workflow.
3. **Layout-per-step-per-role is the mechanism.** `WorkFlowTemplateStep` carries *two* layout FKs,
   `PageLayoutApproversID` and `PageLayoutAssigneesID`, and the live grid renders the bound layout
   suffixed `(Approvers)` — so the assignee layout exists and is simply not shown on that screen.
   Reproducing the engine without layout-per-step-per-role reproduces none of its expressiveness.
4. **Routing rules live only on the template; resolved people live only on the instance.**
   `ApproverType`, `ApproverJobTitleIDList`, `ApproverUserClassIDList` exist on
   `WorkFlowTemplateStep` and **not** on `WorkFlowStep`, which keeps only the flattened
   `ApproverMemberIDList`. Role→person resolution happens once, at instantiation. **Derived.**
5. **Some behaviour flags are *not* snapshotted and are therefore read live off the template.**
   `AutoLaunchNextStep`, `SetTaskInProcess`, `SetTaskCanceled`, `AutoAdjustTaskDates`,
   `NotifyStep*Started` and every routing column have no `WorkFlowStep` counterpart. Editing a live
   template changes running instances for those and not for the copied ones. **Derived.**
6. **Approvers decide; assignees do not.** `WorkFlowStepApprover` (20 cols) carries
   `ActionTakenName`, `WorkFlowTemplateStepActionID`, `HasApproved`, `HasTakenAction`,
   `SignatureDate` and a full `Prior*` mirror. `WorkFlowStepAssignee` (11 cols) carries **no action
   fields at all**. **Observed** (S1 lines 219-220).
7. **Attachability is declared on the Form Type, not on the workflow.** `WorkFlowTemplate` has no
   `IsValidFor*` columns; `CodeIssueType` has eleven plus `IsWorkFlow`. **Now Observed in the UI**:
   the Form Type editor renders a boolean per entity kind, and both lease-accounting form types are
   set to `Portfolio = Yes, RE Contract = Yes` with the other nine `No`.
8. **A Form *is* an Issue Type — `Issue` is the generic unit-of-work record for the whole
   product.** `Manage Forms` runs on `TableType=2035`, and the captured 207-table registry shows
   that is `Issue Type Code` (**Observed**, `../../data-model/code-table-registry.md`). The four
   form types are four code-table rows. Every vendor label says Form, and `IssueInterface` is a
   declared GraphQL interface. Treating `Issue` as a bug-tracker "issue" produces a fundamentally
   wrong data model.

   **Lucernex did not build a form builder.** It built one ticket type, made its subtype a
   code-table value, gave each subtype its own user-defined fields and one layout per workflow step,
   and got a form builder free. **Derived.** The warning that follows: **every request-shaped
   feature in this product is the same table.** A rebuild modelling Lease Admin Requests,
   rent-payment approvals, invoice disputes and bid questions as four aggregates will need four
   workflow engines. Lucernex needs one. Full argument in
   [`issues-and-tasks.md`](issues-and-tasks.md).

## What the live capture did *not* show

The `Manage Work Flows` grid surfaces **six columns** — `Step`, `Step Name`, `Form/Task`, `Type`,
`Approval Level`, `Approver` — against `WorkFlowTemplateStep`'s **55 physical fields**. Roughly 90%
of the step model is still unobserved, and `WorkFlowTemplateStepAction` (37 fields) has not been
seen at all. Specifically unobserved:

| Unobserved | Why it matters |
|---|---|
| The **step editor** behind `edit` on a step row | Holds SLA durations, warn/alert offsets, notification flags, assignee routing, `AutoLaunchNextStep`, the task-coupling flags, and `PageLayoutAssigneesID`. |
| The **action editor** — every field in [`step-actions.md`](step-actions.md) | This is where branching, quorum, signature, sub-workflow spawn and the Last Action Status write all live. Without it, the control-flow model stays schema-derived. |
| A **`Task` step** | Zero exist in the tenant. Half the step field set (`TaskName`, `TaskID`, `AutoAdjustTaskDates`, `SetTaskInProcess`, `SetTaskCanceled`) is exercised only by task steps. |
| The **`Work Flow Status Code` values** | The entire state model depends on them. **Not readable from Manage Firm Drop Downs — it is not one of the 207 platform code tables** (`../../data-model/code-table-registry.md`). Introspect `codeWorkFlowStatusID` via GraphQL instead; an earlier revision of this folder pointed at the wrong screen. |
| The **assignee side** | The grid shows only `Approver`. `Approval Level` is an approver concept; assignee routing was not rendered. |

## Known engine defects and gaps, as reported by ASG users

**Observed** from `_xlsx_feature_list.txt` — direct evidence about how the engine behaves in
production, and several are consequences of the schema described above.

| # | Reported behaviour | Line | Schema cause (Derived) |
|---|---|---|---|
| 1 | "When multiple approvers are required to vote on a single step and take conflicting actions (Approve vs Deny), the workflow can't move forward" — stalls indefinitely. | 362 | `RequireAllApprovers` is a single Boolean per *action*. No vote tally, no tie-break, no "first decisive action wins". |
| 2 | "The UI does not indicate if the approval process is sequential or parallel." | 352 | No sequence column on `WorkFlowStepApprover`. Approval is inherently parallel. |
| 3 | "There is no obvious, standard *Send Back to Previous Step* or *Request Rework* action." | 353 | Backward movement exists only as `MoveToStepNumber` < current or `RestartStep = true`, both configured per action. No built-in reverse transition. |
| 4 | "The vendor change workflow defaults to assigning tasks to all team members (*all-for-one* logic)." | 360 | Role routing resolves to **every** matching member; `RequireAllApprovers` then demands all of them act. Note the live tenant sidesteps this by routing 17 of 19 steps by **Member**. |
| 5 | "Workflows are presented as static text lists. There is no flowchart or diagram view." | 330, 350 | Consequence of fact 1 — the graph is implicit in scattered `MoveToStepNumber` integers. Confirmed by the live grid, which is exactly a static text list. |
| 6 | "For every step the administrator must manually select the correct Form Layouts for both Assignees and Approvers." | 351 | `PageLayoutApproversID` / `PageLayoutAssigneesID` are unconstrained selections; nothing ties them to the step's Form Type. The live layout naming convention (`LAR …`) is a manual discipline, not an enforced one. |
| 7 | "No proactive alerts for at-risk items beyond the basic duration triggers." | 354 | The only SLA machinery is `DaysUntilWarn*`/`DaysUntilAlert*`. |
| 8 | "*Checkout* allows users to lock records indefinitely; only a sysadmin can release." | 363 | `CheckedOutByMemberID`/`CheckedOutDate` on both `Issue` and `WorkFlowStep` have no expiry column. |
| 9 | "Need an out-of-office delegate feature so workflows do not stall when the admin is away." | 340 | No delegation object exists. Sharpened by the live data: `User Request` step 1 routes to a single Job Title, *System Administrator*. |
| 10 | "Ability to find a user and bulk replace them with another on all assigned entities and workflows." | 345 | Approver rows are per-instance; no bulk substitution primitive. Sharpened by the live data: 17 of 19 steps route by named **Member**. |

## Scope: Cost Management and Budgeting are out of scope

**Effective 2026-09-10**, per the user via team-lead. This folder follows the convention the
reporting-forms agent set: budget, bid, purchase-order, change-order, pay-app and cost-tracking
items that sit **on in-scope tables** are retained and marked
**⊘ out-of-scope-but-structural**, not deleted. They are columns, type discriminators and subtype
FKs on objects the workflow engine genuinely owns, and removing them would misrepresent those
records — a 38-field action object described as 33 fields is simply wrong.

What is marked in this folder:

| Location | Items | Why retained |
|---|---|---|
| [`step-actions.md` §G](step-actions.md#g-cost-management-side-effects--6-fields-out-of-scope) | `AutoCopyAmounts`, `AutoClearAmounts`, `FifoPayApp`, `GenPurchOrderLineSeqNum`, `SendPaymentInfo`, `bidAwdApCodeLastActionStatusID` | Six of `WorkFlowTemplateStepAction`'s 38 fields. They bound what the engine *can* express; omitting them would overstate its generality. |
| [`issues-and-tasks.md`](issues-and-tasks.md#the-nine-subtypes) | `PurchaseOrder`, `ChangeOrder`, `PayApp`, `InvoiceIssue`, `BidPackage`, `BidderIssue`, `Question` | The evidence for `Issue`-as-supertype, which is a core workflow finding. The subtypes prove the pattern; the modules behind them are out of scope. |
| [`data-model.md`](data-model.md) | `BudgetColumnType`, `CostTrackingTemplate`, `VirtualTemplateBudget*` in the `IsValidFor*` recurrence | Pattern evidence for the attachability idiom — the same retention team-lead approved for `BudgetColumnType`'s `IsValidFor*` family. |
| [`routing-and-approvals.md` §9](routing-and-approvals.md#9-vendor-collaboration) | The bidding module as the vendor-collaboration worked example | The only place that capability is exercised in the product. Doubly deferrable: the live tenant leaves `Collaborator Job Titles` empty on all four workflows. |

**Do not build Cost Management functionality off anything in this folder.**

### What is *not* out of scope, and must not be stripped by mistake

**`Rent Payment Review/Approval` is a lease-rent process, not Cost Management.** It is one of the
four live workflows, it runs over lease payment records, and it belongs with
`../contracts/payment-lifecycle.md`. Lucernex's Cost Management module is the *capital-project* cost
stack — Budget, BudgetColumn, PurchaseOrder, ChangeOrder, PayApp, BidPackage, CostTrackingTemplate.
The word "payment" appears in both; they are different modules. Likewise
[`asg-edgeplus-mapping.md` D10](asg-edgeplus-mapping.md#3-what-should-deliberately-differ)
(amount-banded approval routing) is about **lease and rent payment approvals** and stays in scope.

## Evidence discipline used in this folder

- **Observed** — read directly from an offline source file (see
  [`data-model.md`](data-model.md#source-files-and-how-to-read-them)) or from a live capture written
  by another agent, with the file cited.
- **Derived** — computed from Observed data (set differences over field lists, presence/absence
  arguments over the complete 223-object schema).
- **Inferred** — domain reasoning or naming-convention analogy. Never restated as fact downstream.

Live captures cited here were made by other agents and are **not owned by this folder**:
`../layouts-and-forms/forms-vs-pages-vs-layouts.md` (the workflow and form configuration) and
`../../data-model/graphql-api.md` (the API introspection). They are cited, never edited.
