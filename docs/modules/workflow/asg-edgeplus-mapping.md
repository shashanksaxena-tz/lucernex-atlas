# Mapping the workflow engine onto ASG Edge+

**Stated up front.** Nothing in ASG Edge+ implements workflow today, and we now know exactly what
it has to replace: **four workflows, 19 steps, three of them lease-accounting processes ASG runs
today** (**Observed**, `../layouts-and-forms/forms-vs-pages-vs-layouts.md`). That is a far smaller
and far more concrete target than the 223-object schema suggested. The estate index
(`../../../../CLAUDE.md`) lists six running services — Platform, Configuration-Service,
User-Service, Api-Gateway, Documents-Service, Audit-Service — and the live thread is Masters
(MDM-01) and Page Layouts (PAGE-LAYOUTS-01). **Workflow & Approval Management is BRD 17
("Workflows & Approvals Module BRD.docx", Submitted, ASG-approved)** — **Observed**,
`_xlsx_feature_list.txt` line 307. So this is a from-scratch build with an approved BRD and a
seven-year-old reference implementation whose defects are documented by its own users.

The recommendation that follows from this analysis is blunt: **rebuild the Lucernex *capabilities*,
not the Lucernex *model*.** Six of the model's characteristics are not conservative design choices
but structural defects that ASG users are already complaining about — no conflict resolution, no
sequencing, depth-1 history, no template versioning, no parent pointer on spawned workflows, and
JavaScript-in-a-text-column as the only conditional logic. Reproducing them would import ten
documented pain points on day one.

Everything below labelled about Lucernex inherits the confidence label of the document it cites.
Everything about ASG Edge+ is stated from the estate index and is **Observed** only to the extent
that index is current — none of the ASG repos were opened for this analysis.

## 1. What ASG Edge+ already has that workflow needs

| Need | ASG Edge+ asset | Fit | Note |
|---|---|---|---|
| Tenant isolation | Hub/Spoke, database-per-tenant (`ADR-004`, accepted 2026-05-22) | Good | A `WorkFlow` instance is unambiguously Spoke data (it hangs off a Contract/Portfolio). A `WorkFlowTemplate` is arguably Hub. See §5. |
| Identity, roles, job titles | `ASG-Edgeplus-User-Service`; `asg-edgeplus-starter-identity`; gateway forwards `X-User-Id`, `X-Tenant-Id`, `X-Roles` | Good | The four-way principal selector (Member / Job Title / User Class / Org Chart Level) needs an org chart. Confirm `SupervisorID`-equivalent exists in User-Service before designing level routing. |
| Form layouts per step | PAGE-LAYOUTS-01 in Configuration-Service | **Direct dependency** | `PageLayoutApproversID` / `PageLayoutAssigneesID` mean a workflow step *renders a layout*. Workflow cannot ship before layouts do. |
| Form types and their attachability | Masters (MDM-01) | **Direct dependency** | `CodeIssueType` with its eleven `IsValidFor*` flags is a Master. |
| Priority, status and action-status code lists | Masters (MDM-01) | Direct dependency, **but not uniformly** | `Last Action Status Code` (2082), `Priority Code`, `Task Status Code` and `Task Lead Lag Type Code` are tenant-editable platform code tables and are straightforward Masters. **`Work Flow Status Code` is not among the 207** (**Observed**, `../../data-model/code-table-registry.md`) — it is a platform-internal enumeration that governs engine behaviour, not presentation. **Do not model it as a Master.** A tenant able to rename or deactivate *Approved* would break the engine. Values still uncaptured — OQ-7. |
| Immutable audit | `ASG-Edgeplus-Audit-Service`; ADR-0012 outbox; ADR-0020 in-transaction audit | **Critical, and blocked** | The workflow decision log is exactly the kind of record ADR-0020 governs. Configuration-Service is currently standing on a `LoggingMasterAuditAdapter` marked PROVISIONAL, with `NoOpOutboxPublisher` behind ADR-0012. Workflow must not ship on a provisional audit adapter. |
| Documents on a form | `ASG-Edgeplus-Documents-Service` | Good | `Issue.DocumentIDList`, `Issue.Photos`, `LinkTaskDocument`. |
| Notification delivery | **None** | **Gap** | No notification service exists in the estate. User-Service has SES SMTP credentials (in plaintext in `application.yml` — a known defect; do not extend that pattern). |

## 1a. The four processes the rebuild must actually support

**Observed**, `../layouts-and-forms/forms-vs-pages-vs-layouts.md`. This is the highest-value input
in this document: the BRDs say what the processes *should* be; this is what they *are*, in
production configuration. **Any gap between the two is a requirements question, not a documentation
gap.**

| Workflow | Steps | Prefix | Attachable to | What it tells the rebuild |
|---|---:|---|---|---|
| **Lease Admin Request** | 8 | `LAR` | Portfolio, RE Contract | The contract-setup process, already implemented. Maps onto BRD-24 / the PJ-01…PJ-13 phases in `../../contracts-explained.html`: submit → initial review → abstract the lease document → ASG review → client review → import payment history/sales → finalize → finalize (defaults) → complete. |
| **ASC 842 Schedule Review/Approval** | 3 | `ASR` | Portfolio, RE Contract | **The accounting engine's output is not auto-published.** Produce → internal review → ASG approval → client approval. ASG Edge+'s accounting engine needs a review/approval gate, not just a calculation. This is a direct obligation on the accounting module. |
| **Rent Payment Review/Approval** | 6 | `RPR` | not captured | The payment run is **preview → approve ×3 → generate**, with *Generate Final Rent Payment File* as its own workflow step. File generation is a workflow step, not a side effect of approval. Direct obligation on the payments module. |
| **User Request** | 2 | none shown | not captured | Routes by **Job Title → System Administrator**, then an **Ad Hoc** revision step. This is the process behind the reported single-point-of-failure and no-delegation pain points (feature list lines 340, 349). |

Three structural facts about all four:

- **Every step is a `Form` step. Not one `Task` step exists.** See B1 below — this may remove half
  the step model from scope.
- **17 of 19 steps route to a named Member**, one to a Job Title, one Ad Hoc. The elaborate
  role-based routing the schema supports is essentially unused in production. Ask ASG whether that
  is policy or workaround (**OQ-42**) before sizing the routing engine.
- **Every workflow is strictly linear.** No branch is visible — though the grid could not render one
  if it existed (**OQ-44**).

## 2. What must be built

Ordered by dependency. Sizes are relative, not estimates.

| # | Component | Lucernex source | Notes |
|---:|---|---|---|
| 1 | **Form (`Issue`) aggregate + Form Type master** | `Issue` (56 cols), `CodeIssueType` (19) | The unit of work. Must land before workflow. Nine subtypes in Lucernex — decide per §4 whether ASG Edge+ keeps a supertype or models each independently. |
| 2 | **Principal selector** — a reusable value object resolving {named user, job title, user class, org-chart level} against an entity roster | `ApproverType` + three `*IDList` columns; `WorkFlowTemplateStepMember`; `NotifyTemplateMember`; `LinkTaskByCodeMember` | Lucernex uses this shape in **three** subsystems. Model it once. |
| 3 | **Workflow definition aggregate** — template, ordered steps, per-step actions | `WFT`/`WFTS`/`WFTSA` | Add versioning (§3). |
| 3a | **Layout-per-step-per-role binding** | `WFTS.PageLayoutApproversID` / `PageLayoutAssigneesID`; `WFT.PageLayoutID` for the kick-off Submit layout | **The engine's real source of expressiveness** (**Observed**). One record, a different field surface at every stage and per role. Constrain the layout picker to layouts whose Form Type matches the step's — that alone removes ASG's reported sync burden (feature list line 351). |
| 4 | **Workflow instance aggregate** — instance, steps, participants, decision log | `WF`/`WFS`/`WFSAp`/`WFSAs` | Append-only decision log, not a depth-1 `Prior*` slot. |
| 5 | **Resolution service** — routing rule → resolved principals at step entry | WF-R-025…029 | Decide whether to store the rule, the resolved set, or both. |
| 6 | **SLA / escalation scheduler** — warn, alert, and whatever ASG adds beyond that | `DaysUntilWarn*` / `DaysUntilAlert*` / `Computed*Date*` | Lucernex only notifies. ASG's own pain point (feature list line 354) asks for more. |
| 7 | **Notification service** — templated, multi-channel, per-recipient delivery records | `EMailMessage` + two channel flags; `NotifyTemplate` family | Lucernex has no subject line and no merge fields for workflow email. This is a real gap, not a simplification. |
| 8 | **Task / schedule module** | `Task`/`TaskGroup`/`TaskItem`/`TaskPredecessor` | Only needed if ASG Edge+ ships Task steps. **Decide early** — see §6. |
| 9 | **Workflow visualiser** | none — Lucernex has none | Explicitly requested twice (feature list lines 330, 350). A designed graph model makes this nearly free; scattered `MoveToStepNumber` integers make it nearly impossible. |
| 10 | **Task inbox / My Approvals** | Dashboard widgets *My Activities / Alerts / Approvals / Assignments*, *Critical Issues*, *My Work Queue* | **Observed**, `docs/screens/001-dashboard-home.md` lines 74-85. |

## 3. What should deliberately differ

Each row is a **recommendation with a stated reason and a stated cost**. These are the decisions to
put in front of ASG, not choices to make silently.

| # | Lucernex behaviour | Recommended ASG Edge+ behaviour | Why | Cost of diverging |
|---:|---|---|---|---|
| D1 | Templates are mutable in place; running instances read 35 fields live off the template and 20 from a snapshot ([`template-vs-instance.md`](template-vs-instance.md)) | **Version templates. Pin every instance to a version. Never read through to a mutable definition.** | Non-deterministic instance behaviour is unauditable; SOX/SOC-2 will not accept "the rule changed under the running approval". | Migrated Lucernex instances carry no version. They must be pinned to a synthetic "as imported" version. |
| D2 | Conflicting approver actions under `RequireAllApprovers` deadlock with no recovery (WF-R-053; feature list line 362) | **Explicit quorum policy per step: unanimous / first-decisive / N-of-M / weighted; plus an explicit conflict outcome (deny wins, or escalate to a named resolver).** | This is ASG's single loudest complaint about the current system. | None — it is strictly more capable. Migration maps `RequireAllApprovers = true` → unanimous, `false` → first-decisive. |
| D3 | Approval is structurally parallel; no ordering column exists (feature list line 352) | **Support both parallel and sequential approval, and show which is in force.** | Second-loudest complaint. Lease approvals routinely need "analyst then manager then director". | Migration defaults everything to parallel, which matches today. |
| D4 | One prior round of history (`Prior*` slots), and a single `Issue.LastPageLayoutID` that records only the most recent layout (`LAY-R-164`) | **Append-only decision log; every action by every participant in every round, immutable — and store the layout reference on each decision record, not just on the request.** Concrete schema drafted as `workflow_decision` in `../layouts-and-forms/asg-edgeplus-mapping.md`; see D4a for the one caveat. | Audit requirement, not a feature. Because a Form shows a different surface at every step, an auditor asking "what did this approver actually see?" cannot be answered from `LastPageLayoutID` alone. Route it through Audit-Service. | More storage. Blocked on the ADR-0020 successor. |
| D4a | Lucernex records **one submission stamp per step** (`WorkFlowStep.SubmitForApprovalByMemberID` / `…Date`) and **one decision row per approver** (`WorkFlowStepApprover`). Assignees get no decision row at all — `WorkFlowStepAssignee` has 11 columns and not one action field | The layouts module proposes a single `workflow_decision` table keyed by `(request_id, step_id, actor_id, role)` with `role ∈ {APPROVER, ASSIGNEE}` and `layout_id` + `layout_version` frozen per row (`../layouts-and-forms/asg-edgeplus-mapping.md`). **Endorsed, with one caveat recorded below.** | Merging the two roles into one decision log is a deliberate improvement — it captures *who submitted*, which Lucernex loses. But it must be labelled a divergence, not a port: a per-assignee decision row is **new data with no Lucernex source**. | **Migration consequence:** for imported requests, `role = ASSIGNEE` rows can only ever be reconstructed as a single synthetic row per step, from the one `SubmitForApprovalByMemberID` stamp. Do not model assignee rows as if historical per-person data exists. |
| D5 | Branching is a bare integer `MoveToStepNumber`; conditional logic is JavaScript in a text column | **A declarative transition model: explicit typed edges, plus a sandboxed, versioned, testable condition expression over form fields.** | Makes visualisation (§2 #9) possible and removes an unsandboxed code-execution surface. | Real design work. Migration converts each `(step, action)` pair to an edge — mechanical. |
| D6 | Spawned workflows have no parent pointer (OQ-5) | **Every instance records its origin: parent instance, parent step, parent action, or the kick-off form/task.** | Without it the chain of custody breaks at every kick-off. | Trivial — two columns. |
| D7 | Escalation only notifies; never reassigns, escalates or auto-decides (WF-R-046/047) | **Policy-driven escalation: notify → reassign to a delegate → escalate to a supervisor → auto-decide, configurable per step.** | Requested (feature list line 354). Lease critical dates make missed approvals expensive. | New scheduler component. |
| D8 | No delegation / out-of-office (feature list line 340) | **First-class delegation with a date range and an audit trail.** | Explicitly requested by the sysadmin persona. | New concept; no Lucernex data to migrate. |
| D9 | Checkout lock has no expiry (feature list line 363) | **Lock with a TTL, manager override, and pre-expiry warning.** ASG's own proposal: rename to Lock/Unlock, grant managers unlock, expire at 48 hours. | Named as Critical by ASG. | None. |
| D10 | Amount-banded approval routing is absent from the workflow engine; `Member` carries eight unreferenced approval-limit columns (OQ-19). **In scope** — lease and rent payment approvals, not capital-project Cost Management | **First-class amount bands on the routing rule, reading the form's monetary value.** | Lease and payment approvals in ASG Edge+ will require it. Constitution §4.4 forbids `double`; use `BigDecimal` throughout, and store JSON monetary attributes as strings. | Depends on resolving OQ-19 — Lucernex may do this in the payment module rather than the workflow. |
| D11 | Notification body is one free-text field per step; no subject, no merge fields, no per-recipient delivery record | **Templated notifications with subject, merge fields, channel routing, and a delivery record per recipient.** | Lucernex's `EMailSentStatus` is free text on the participant row; notifiees get nothing at all. | New service (§2 #7). |
| D12 | Role-based routing resolves to *everyone* matching, producing the "all-for-one" overload (feature list line 360) | **Distinguish "any one of this role" from "all of this role" at rule level.** | Third-loudest complaint. | Migration defaults to "all", matching today. |
| D12a | Layout-per-step-per-role is bound by naming convention only (`LAR …`, `ASR …`); nothing ties a layout to the step's Form Type | **Keep layout-per-step-per-role; enforce the binding.** The picker should offer only layouts whose Form Type matches. | The mechanism is right; the lack of a constraint is what generates the reported cognitive load. | None. Migration reads the existing FKs unchanged. |
| D13 | Nine `Issue` subtypes share one 56-column supertype carrying bidding, procurement, equipment and Q&A columns together — most of them **⊘ out of scope** | **Keep exactly ONE Form/request aggregate. Thin its core; move type-specific *columns* to the owning module.** This is a column-placement change, **not** a decomposition into separate aggregates. | 56 columns of which perhaps 20 are universal; five are explicitly *"not implemented"*. **The one-aggregate half is now proven, not preferred:** `TableType=2035` is `Issue Type Code` (**Observed**, `../../data-model/code-table-registry.md`), so a Form type is a *code-table row*, not a type. Lucernex built one ticket table, made its subtype a code value, and got a form builder free. | Cross-module coordination on the columns. Follows the estate rule "no shared domain library across services" — share via events, not Java types. **The failure mode to avoid is the opposite one:** modelling Lease Admin Request, rent-payment approval, invoice dispute and bid question as four aggregates means four workflow engines. Lucernex needs one. Argued from the layouts side in `../layouts-and-forms/forms-vs-pages-vs-layouts.md`. |
| D14 | `WorkOrder.ApproverMemberID` and `ServiceRequest.ApproverPartyID` are a second, single-approver approval path outside the engine (OQ-33) | **One approval mechanism.** | Two approval systems means two audit trails and two sets of rules. | Verify OQ-33 first. |

## 4. What should deliberately stay the same

Equally important. These are good decisions in the Lucernex model and copying them is the right call.

| Lucernex behaviour | Why keep it |
|---|---|
| **Template/instance split with an explicit snapshot** | Correct. Only the *partial* snapshot is wrong (D1). |
| **Approver ≠ assignee ≠ notifiee, with different runtime records per role** | The asymmetry is deliberate and right: decisions need per-person audit, work assignment does not, and notification needs neither. |
| **Actions as first-class configurable rows rather than a hard-coded Approve/Reject enum** | Tenants genuinely need "Approve with conditions", "Return to Analyst", "Escalate to Legal". Keep it. |
| **Attachability declared on the Form Type, not on the workflow** | Decoupling *what kind of thing this is* from *how it gets approved* is correct and lets one workflow serve many entity types. |
| **A step renders a configured page layout, with different layouts for approvers and assignees** | **Now Observed in production and the most important thing to copy.** Powerful and unusual. Keep it — and fix the sync burden (feature list line 351) by constraining the layout picker to layouts valid for the step's Form Type. |
| **The layout id is snapshotted onto the running step** | Correct: an administrator editing layouts cannot change what a half-completed approval shows. Lucernex freezes the presentation and floats the behaviour; ASG Edge+ should freeze both (D1). |
| **Form Type is 1:1 with Work Flow** | Observed for all four live types. One record type, one process. Resist the temptation to allow many workflows per form type until ASG asks for it. |
| **Ad Hoc as a declared routing category** | Observed on 2 of 19 steps. An honest, design-time declaration that the principal is chosen at runtime — better than an off-model override. Give it an audit trail. |
| **The step is the unit of SLA, with separate approver and assignee clocks** | Correct granularity. |
| **`IsFormStep` — form step vs task step** | A clean two-mode model, if ASG Edge+ ships schedules at all (§6). |
| **Sequence numbers with a per-firm/per-entity prefix** (`CodeIssueType.IsSequencePerFirm`, `SequencePrefix`, `Issue.PONumber`) | Human-readable business identifiers matter to lease administrators. |
| **Ad-hoc assignee as an explicit, named slot** | An honest escape hatch, better than off-model overrides. Give it an audit trail. |
| **Private forms** (`Issue.IsPrivate` + `Member.IsViewPrivateIssueAllowed`) | Needed for legal and HR-adjacent lease matters. |

## 5. Hub/Spoke placement

The estate's target shape puts global configuration in the **Hub** and per-firm operational data in
a per-firm **Spoke** database. Applying that to workflow:

| Object | Placement | Reasoning | Confidence |
|---|---|---|---|
| `CodeIssueType` (Form Type master), `Last Action Status Code`, `Priority Code`, `Task Status Code` | **Hub**, with the publish/accept/fork mechanism | They are tenant-editable Masters, and MDM-01 already owns Masters. | Derived from the estate index |
| `Work Flow Status Code` | **Neither — engine-internal.** Ship it as a code enum in the workflow service, not as tenant-configurable master data | Not in the 207-table platform catalogue; it governs transitions rather than presentation. | Observed (its absence) + Derived (the reading) |
| `WorkFlowTemplate` / `Step` / `StepAction` | **Hub-defined, Spoke-forkable** | Lucernex's `WorkFlowTemplate` is Global scope with no Firm-scope fields at all (**Observed** — `docs/data-fields/work-flow-template.md`: 25 Global, 0 Firm; same for all six workflow objects). But ASG's own pain point (feature list line 349) is that *"The administrator is the only one who creates and manages all workflows… a significant bottleneck"*. A Hub-published, Spoke-forkable template answers both. | Recommendation |
| `WorkFlow`, `WorkFlowStep`, `WorkFlowStepApprover`, `WorkFlowStepAssignee` | **Spoke** | Instance data hanging off a Contract/Portfolio. | Derived |
| `Issue` and its subtypes | **Spoke** | Operational records on an entity. | Derived |
| Member/job-title/user-class/org-chart routing data | **Hub** (shared entities per the estate index), read by the Spoke at resolution time | The index places User management among the shared Hub entities. | Derived from the estate index |

**The unresolved item this exposes:** the Hub→Spoke publish/accept/fork mechanism and the "never
more than one version behind" rule are, per the estate index, *not written down anywhere yet*. A
forkable workflow template is a harder case than a forkable Master, because a fork must not break
running instances — which is exactly D1 (version pinning) again. **Confirm before building.**

Note also the unreconciled ADR conflict flagged in the estate index: `ADR-004` in
`KnowledgeFolder` specifies database-per-tenant, while a *different* document also numbered
ADR-004 in Configuration-Service specifies one shared platform database. Workflow instance data
placement depends on which one governs.

## 6. Decisions ASG must make before this can be built

| # | Decision | Why it blocks | Depends on |
|---:|---|---|---|
| B1 | **Does ASG Edge+ ship a schedule/Task module at all?** **Live evidence now points hard at "no".** All 19 configured steps are `Form` steps; **not one `Task` step exists in the tenant** (**Observed**). If Tasks are out, `IsFormStep` collapses, and `TaskName`, `TaskID`, `AutoAdjustTaskDates`, `SetTaskInProcess`, `SetTaskCanceled` plus the whole `Task`/`TaskGroup`/`TaskItem`/`TaskPredecessor` family leave scope. The feature list also shows Forms and Work Flow tabs on five entities but no Schedule tab. **Recommend: confirm with ASG and drop it.** | ASG scope — now answerable |
| B2 | **Which of the eleven `IsValidFor*` entity types are in scope?** **Narrowed sharply.** Both lease-accounting form types are attachable to **Portfolio and RE Contract only**, with the other nine `No` (**Observed**). The feature list separately shows Forms/Work Flow tabs on five entities. Two of four form types were not captured (**OQ-46**). | Determines the attachability matrix and how much of `ProjectEntity`'s polymorphism must be rebuilt. If it really is Portfolio + RE Contract, this is a much smaller build. | OQ-32, OQ-46 |
| B3 | **Is the audit ADR resolved?** The successor to ADR-0020 (in-transaction audit vs. the ADR-0012 outbox) is an open blocker on Configuration-Service, and the workflow decision log is a harder case than the Masters audit. | D4 cannot be built on a `LoggingMasterAuditAdapter` marked PROVISIONAL. | Estate blocker |
| B4 | **Is the Hub→Spoke publish/accept/fork mechanism specified?** | Determines whether workflow templates are Hub-only, Spoke-only, or forkable — §5. | Estate blocker |
| B5 | **Migration fidelity: do running Lucernex workflows migrate, or only completed ones?** | Depth-1 history (D4) means in-flight instances carry almost no context. Migrating them into a versioned, append-only model requires inventing history that does not exist. | ASG scope + OQ-38 |
| B6 | **Do amount bands belong in the workflow engine?** | D10. If Lucernex does amount-banded approval in the payment module instead (OQ-19), ASG must decide whether to consolidate. | OQ-19 |
| B7 | **One approval mechanism or two?** `WorkOrder` and `ServiceRequest` have their own approver fields. | D14. | OQ-33 |
| B8 | **What replaces `IsEnabledLxJSCode`?** A sandboxed expression language, a rules service, or nothing? | D5. Some tenants will have real JavaScript in production that must be reimplemented. | OQ + a Lucernex data extract |

## 7. Cross-module obligations

The estate rule *"Never spec a module from its own BRD alone"* applies with force here — the
workflow engine touches nearly everything.

| Module | Obligation |
|---|---|
| **Masters (MDM-01)** | Owns `CodeIssueType` and four code lists. `CodeIssueType` is unusual for a Master: it carries eleven behavioural Boolean flags, not just a name and description. Confirm the Masters model can hold that. |
| **Page Layouts (PAGE-LAYOUTS-01)** | `PageLayout.CodeIssueTypeID`, `IsBudgetImpacting`, `AllowUserCreate`, `AllowEdit` are all read by the workflow engine. `sTYPE_SUBMITBUTTON` action buttons on layouts are a *second* action mechanism — see [`step-actions.md`](step-actions.md#action-buttons-on-page-layouts). D18 (does MCT-028 forbid central layout push?) is already an open decision and it touches this. |
| **Contract** | The primary attachment target. Contract has 147 Firm-scope fields, and Lucernex surfaces `IssuesAndAlerts` on it — a roll-up of *"work flow / form type, critical issue count, non-critical issue count, escalated count, past due notification count"* (**Observed**, S2). That roll-up is a workflow read model. |
| **Documents** | `Issue.DocumentIDList` and `Issue.Photos`. Feature list line 348 marks *"attach documentation directly to a workflow and ensure it stays linked to that specific request for auditors"* as **Critical**. |
| **User / identity** | Job titles, user classes, the org chart (`SupervisorID`), per-entity rosters (`LinkMemberProjectEntity`), approval limits, `IsViewPrivateIssueAllowed`. Feature list line 332 states deactivated users must retain their historical attribution. |
| **Audit** | The decision log. |
| **Notification** | Does not exist yet. |

## 8. Open questions blocking a decision

1. **Everything in [`rules.md`](rules.md#open-questions)** — in particular OQ-43 (open the action
   editor), OQ-7 (the status code values), OQ-44 (is the linearity real) and OQ-19 (amount-banded
   routing). OQ-43 is now the single highest-value screen: `WorkFlowTemplateStepAction` has never
   been rendered, and it holds the entire control-flow model.
2. **Does the ASC 842 review gate exist in the accounting module's spec?** The live workflow proves
   schedules are reviewed and double-approved before publication. If
   `../accounting/` and its BRD assume auto-publish, that is a requirements gap to raise now.
3. **Does the payments spec treat file generation as a workflow step?** `Rent Payment
   Review/Approval` step 5 is *Generate Final Rent Payment File* — a step, not a side effect of
   approval. Check `../contracts/payment-lifecycle.md` against it.
4. **Is BRD 17 ("Workflows & Approvals Module") consistent with what this analysis found?** It is
   Submitted and ASG-approved (**Observed**, feature list line 307) but was not available offline
   for this pass. Read it against [`rules.md`](rules.md) and record every contradiction — per the
   estate's source-of-truth order, an approved BRD outranks this document.
5. **Does BRD 15 ("Modern Document Workflow") overlap?** Also Submitted (**Observed**, line 304).
   Two BRDs with "workflow" in the title need reconciling before either is specced.
6. **What does the existing `feature/909-page-layouts-backend-poc` branch in the monorepo assume
   about workflow?** It is stranded and must be ported or abandoned before the monorepo is
   dismantled; if it made workflow assumptions they should be captured now.
7. **Which ADR-004 governs?** The `KnowledgeFolder` database-per-tenant one or the
   Configuration-Service shared-database one. Workflow instance placement (§5) depends on it.
