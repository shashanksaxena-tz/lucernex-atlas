# Layouts and Forms → ASG Edge+

**Stated up front.** ASG Edge+ already has an epic for this — **PAGE-LAYOUTS-01** in
`ASG-Edgeplus-Configuration-Service` — but the epic as currently framed is scoped to *page
layouts*, and the Lucernex evidence says page layouts, forms, list layouts, wizards, map popups,
dashboard tiles and reports are **one record type**. Scoping the rebuild to "page layouts" alone
will produce a second, incompatible mechanism for each of the other faces later. The single most
consequential recommendation in this document is: **model one `Layout` aggregate with a type
discriminator, from day one.**

## What already exists in ASG Edge+

| ASG Edge+ artefact | Relevance |
|---|---|
| **PAGE-LAYOUTS-01** epic (`ASG-Edgeplus-Configuration-Service`) | The target epic. Domain + application + REST exist for Masters; layouts not yet built. |
| **D-01** (OPEN-DECISIONS.md) | Chose a **central layout-push** model — the platform pushes layouts to tenants |
| **D-18** | Open: does MCT-028 forbid the central layout-push model? Blocks PAGE-LAYOUTS-01 phase 3 only |
| `CROSS-BRD-FINDINGS.md` | 14 inbound obligations, 9 contradictions across 28 BRDs touching Masters and Layouts |
| Hub/Spoke target architecture | Global Page/Sub-Page Layouts live in the **Hub**; per-firm layouts in the **Spoke** |
| Workbook module plan (`_xlsx_feature_list.txt`) | Work area 7 **UI & Structural Configuration (Client Level)** contains *Manage Page Layouts*, *Manage Forms*, *Manage Top Menu*, *Manage Folder Templates*, *Layout Changes*. ASG marked Manage Forms and Manage Page Layouts **Required = Yes**, Layout Changes **"Need further explanation as to what this is"** |
| Migration plan | The workbook lists **Layout Migration** and **Field Migration** as distinct migration work areas |

Note the Global-vs-Firm layout duality observed in Lucernex
([008 § Setup Pages](../../admin/008-manage-page-layouts.md#setup-pages-firmeditjspmodesetup)) is
exactly the Hub→Spoke publish/accept/fork mechanism that the workspace `CLAUDE.md` records as *not
yet written down anywhere*. Lucernex's answer is the simplest possible one: a tenant either points
at the `[Global Layout]` or points at its own `ASG *` copy, per entity type, with no partial
inheritance and no version relationship between the two. That is a real design data point for the
"never more than one version behind" rule that still needs confirming.

## Concept mapping

| Lucernex | ASG Edge+ | Gap |
|---|---|---|
| `PageLayout` (one table, many types) | `Layout` aggregate with `LayoutType` | **Must be built.** Do not build one type at a time. |
| `PageLayoutType` = `SEP` | Summary/Detail page | To build |
| `PageLayoutType` = `SUB` | Section fragment, reusable across pages | To build — and it is what makes the whole thing composable |
| `PageLayoutType` = `LIST` | Grid/column layout | To build |
| `layoutMode=sublist` | Custom-list column layout | Same mechanism as LIST; do not fork it |
| `CodeIssueType` (code table `2035`, *Issue Type Code*) + `PageLayout.CodeIssueTypeID` | Form Type + its form layout | To build |
| `Issue` | Form instance | To build (or map onto an existing request/ticket concept) |
| Wizard sub-page sequence | Multi-step creation flow | To build |
| Map Popup Layout | Map-pin popup | Deliberately differ — defer unless GIS is in scope |
| Budget-grid layouts, Bid/Cost layout slots | — | **Out of scope.** Cost Management and Budgeting are excluded |
| `PageLayout.IsDashboardReport` | Dashboard tile | See [reporting mapping](../reporting/asg-edgeplus-mapping.md) |
| `PageLayoutField` | `LayoutField` placement | To build |
| `PageLayoutField.SubPageLayoutID` | Section inclusion | To build |
| `json.conditionalFieldsConfig` (a JSON blob per rule target) | Conditional field rule | To build — **as normalised rows**, see §3 |
| `PageLayoutFilter` | List/report row filter + pivot grouping | To build, as a table separate from conditions |
| `ReportGroupAvailableField` | ASG Edge+ **Data Fields** (Global + Firm) | Partially exists as a concept; the registry itself is the Masters/Data Fields work |
| `Firm.*SetupPageLayoutID` / `Program.*SetupPageLayoutID` | Layout role assignment, tenant + portfolio level | To build — **two levels, not one** |
| `UserClassSecurity` | Role-based layout/field/group permissions | To build; note group-level inheritance |
| `AuditColumn` | Field-change audit | Blocked on the ADR superseding **ADR-0020** (in-transaction audit vs. the ADR-0012 outbox) |
| `ShowLayoutChanges.jsp` ("Layout Changes") | Layout configuration audit | **Unknown** — ASG has flagged it as needing explanation |

## What must be built

### 1. One `Layout` aggregate, typed

```
Layout
  id, tenant_id (null = Hub/global)
  name, description
  layout_type          enum(SUMMARY, SECTION, LIST, FORM, WIZARD, WIZARD_STEP,
                            REPORT, DASHBOARD_TILE, MAP_POPUP)
                       -- Lucernex also has a budget-grid kind; out of scope
  primary_entity_type                                   -- Lucernex PrimaryCodeSQLTableID
  output_type          enum(SCREEN, PDF, XLSX, CSV)
  allow_edit           bool
  allow_user_create    bool
  redirect_url         text                             -- LAY-R-106 escape hatch
  nav_path             text                             -- HierarchyName
  parent_layout_id, sort_key
  form_type_id         FK -> form_type                  -- when layout_type = FORM
  custom_list_id       FK -> field_group                -- when the layout serves a custom list
  owned_by_user_id                                      -- personal "Save As" copies
  source_global_layout_id, source_version               -- Hub→Spoke fork lineage (new; Lucernex has none)
```

The last line is the deliberate difference. Lucernex has **no** lineage between a `[Global Layout]`
and a tenant's copy of it — the tenant simply selects one or the other. ASG Edge+'s Hub/Spoke plan
needs to know which Global layout a firm layout was forked from and at what version, so record it.

### 2. Placement rows that can carry three kinds of thing

```
layout_field
  id, layout_id
  kind                 enum(FIELD, SECTION, STATIC_TEXT, ACTION_BUTTON)
  field_id             FK -> field_registry   -- kind=FIELD
  field_context        text                   -- relation path when placed via a related entity
  child_layout_id      FK -> layout           -- kind=SECTION
  static_text          text                   -- kind=STATIC_TEXT
  action_key           text                   -- kind=ACTION_BUTTON
  display_label        text                   -- per-placement caption / section title
  facet                enum(EDIT, LIST)       -- replaces IsInEditLayout
  row, col, width, height
  mobile_row
  is_required_override bool null              -- explicit; Lucernex leaves this unresolved
  is_readonly_override bool null
  is_searchable_hidden bool                   -- the green "(Searchable, Hidden in grid)" state
  label_style, value_style
```

Three explicit improvements over Lucernex: `kind` instead of inferring from which FK is non-null;
`facet` as an enum with one coordinate set per facet row instead of two coordinate sets on one row;
and **`is_required_override` / `is_readonly_override` as real columns**, which resolves the
contradiction Lucernex leaves open (LAY-R-155 vs LAY-R-156).

`ACTION_BUTTON` is not optional. [008](../../admin/008-manage-page-layouts.md#edit-layout--sections-field-grids-and-action-buttons)
observed Approve Payments, Generate Rent, Extend Contracts, Delete Payments, Alternate Rent Wizard,
Activate/Deactivate, Copy Transaction, Generate Pass-through Payments, and two "(Run Report Action)"
buttons placed *inside* layouts. A layout engine that only places fields will not render an ASG
Contract Summary page.

### 3. Conditions and row filters, separately

The rule model is settled by live capture — see
[conditional-fields.md](conditional-fields.md#rules-for-the-asg-edge-rule-engine) for `LAY-R-010`…
`LAY-R-018` and its design notes. Three points to carry into the schema:

- **One action enum, not two booleans.** Lucernex's `Show / Show and Require / Hide` makes
  visibility and required-ness a single decision. Model `effect enum(SHOW, SHOW_AND_REQUIRE, HIDE)`.
- **Keep the flat `all`/`any` quantifier.** One level, no nesting. It is why the feature is usable.
- **Store predicates as rows, not as a JSON blob.** Lucernex persists
  `json.conditionalFieldsConfig` per target, which is cheap to write and impossible to query.
  Given ASG Edge+ already has an unresolved Where-Used problem (`D-07`, which forced
  `DeactivationPolicy` to default to `WARN_AND_BLOCK`), normalised predicates would let Where-Used
  answer "this dropdown value drives 14 layout rules" — something Lucernex cannot answer about
  itself.

```
layout_rule
  id, layout_id
  target_kind      enum(FIELD, SECTION)
  target_id        FK -> layout_field
  effect           enum(SHOW, SHOW_AND_REQUIRE, HIDE)
  quantifier       enum(ALL, ANY)

layout_rule_predicate
  id, layout_rule_id
  driver_field_id  FK -> field_registry
  driver_context   text                     -- the FK path, when the driver is on a related entity
  operator         enum(IN, NOT_IN, EQ, NEQ, GT, GTE, LT, LTE,
                        SELECTED, NOT_SELECTED, IS_SPECIFIED, IS_NOT_SPECIFIED)
  value_json       jsonb
```

Row filters for lists and reports are a **separate** table with the same predicate shape but
`WHERE`-clause semantics plus grouping — see [data-model.md](data-model.md#pagelayoutfilter--16-fields)
for what Lucernex packs into `PageLayoutFilter`.

Two things Lucernex does not do, that ASG Edge+ should:

- **Re-evaluate server-side on submit.** A conditionally hidden field's value must never be trusted
  from the client, and a `SHOW_AND_REQUIRE` that the client chose not to enforce must still fail
  validation. Evaluation timing is an open question for Lucernex; for ASG Edge+ it is a decision:
  client-side on change for responsiveness, server-side on write for correctness.
- **State the precedence.** See §6.

### 4. Forms as a first-class type

```
form_type
  id, tenant_id
  short_name, long_name
  sequence_prefix, sequence_per_tenant   -- e.g. RFI-0001
  allow_reply, auto_close, is_workflow
  active
  valid_for_entity_types  -- set; Lucernex's 11 IsValidFor* booleans, normalised

workflow_step_layout
  step_id
  role            enum(APPROVER, ASSIGNEE)
  layout_id       FK -> layout
  CONSTRAINT layout.form_type_id = step.workflow.form_type_id   -- see below
```

**Layout-per-step-per-role is the mechanism, and it must be constrained.** Lucernex binds one
kick-off layout on `WorkFlowTemplate` and **two per step** on `WorkFlowTemplateStep` (approver-facing
and assignee-facing), so a workflow with N steps carries N+1 layouts. Both step columns are
**unconstrained FKs** — nothing ties the chosen layout to the step's Form Type, and the `LAR`/`ASR`/
`RPR` naming convention is manual discipline. ASG has already recorded exactly this as a pain point,
in words that independently confirm the two-per-step model:

> "For every step, the administrator must manually select the correct Form Layouts for both
> Assignees and Approvers. This creates a high cognitive load to keep forms and workflows perfectly
> synchronized."
> — `_xlsx_feature_list.txt` line 351, *SysAdmin / Workflow Administration & Configuration / Form
> Integration*. **Observed.** Constraining the layout picker to layouts whose `form_type_id`
matches the step's workflow makes the pain point disappear. Analysis from
[modules/workflow/](../workflow/README.md).

**Record the layout on the decision, not on the request.** Lucernex has only
`Issue.LastPageLayoutID` — *"the name of the last form layout used to update the issue"*, singular
(LAY-R-164). Since a Form shows a different layout at every step and a different one per role, one
pointer cannot reconstruct what each approver actually saw; it is depth-1 history. For SOC 2/SOX an
approval record has to be reproducible as the approver saw it, so:

```
workflow_decision
  id, request_id, step_id
  actor_id, role          enum(APPROVER, ASSIGNEE)
  decision, decided_at, comment
  layout_id, layout_version   -- the surface THIS actor saw, frozen at decision time
  -- role=ASSIGNEE rows have NO Lucernex source. Migrated requests get one synthetic
  -- row per step, from WorkFlowStep.SubmitForApprovalByMemberID/Date. See below.
```

**A uniform decision log is a deliberate divergence, not a port.** Lucernex records the two roles
asymmetrically, and the asymmetry is total:

| | `WorkFlowStepApprover` | `WorkFlowStepAssignee` |
|---|---:|---:|
| Columns | 20 | 11 |
| Action/decision fields | 9 — `HasApproved`, `HasTakenAction`, `ActionTakenName`, `ActionTakenDate`, `ActionComment`, `SignatureDate`, `WorkFlowTemplateStepActionID`, plus `PriorActionComment` / `PriorActionTakenDate` / `PriorWFTemplateStepActionID` | **0** |
| What it does carry | the decision, per approver | `MemberID`, `StepMemberResponsibility`, and two notification-status columns |

**Observed** (`_lucernex_objects_summary.txt`, verified field-by-field). Approvers decide and every
decision is individually recorded; assignees do the work and **none of it is recorded per person**.
Submission is stamped **once per step**, on `WorkFlowStep.SubmitForApprovalByMemberID` /
`SubmitForApprovalDate` (with a single `PriorSubmitByMemberID` / `PriorSubmitForApprovalDate` behind
it — the same depth-1 history limit as everywhere else in this engine).

Merging both roles into one log is still the right call: it captures "who submitted", which
Lucernex genuinely loses, and one uniform audit table is easier to reason about and to prove to an
auditor. But the migration consequence has to be stated, because it is invisible until it bites —
**for imported requests there is no historical per-assignee data to backfill.** A migration spec
that assumes per-person assignee rows exist in the source will produce either empty history or
fabricated history, and fabricated approval history is worse than none. Caveat and analysis from
[modules/workflow/](../workflow/README.md).

That also removes the dependency on the template rows surviving unedited, which is what Lucernex's
model quietly relies on.

### 5. Two-level role assignment

```
layout_assignment
  scope_type    enum(TENANT, PORTFOLIO)   -- Lucernex: Firm vs Program
  scope_id
  entity_type
  role          enum(SETUP_WIZARD, MAP_POPUP, SUMMARY, LIST)
  layout_id
```

Lucernex has this as 29 dedicated columns spread over two tables (11 on `Firm`, 18 on `Program`).
Normalise it. Resolution order: portfolio assignment → tenant assignment → Hub default.

### 6. Precedence, stated

Nobody at Lucernex wrote this down and it is the kind of gap that produces production bugs:

> **security → placement → condition.** A user class denial cannot be overridden by placing the
> field on a layout. A field not placed on a layout cannot be shown by a condition. A condition can
> only hide, never reveal, what the first two allow.

## What should deliberately differ

| Lucernex behaviour | ASG Edge+ | Why |
|---|---|---|
| `PageLayoutFilter` serves both row filters and field conditions, split by a boolean | Two tables | The boolean exists only because of a legacy merge; it forces every consumer to remember to filter on it |
| `DisplayOption1`/`DisplayOption2` numeric bitmasks | Named boolean/enum columns | Bitmask semantics are undocumented even inside Lucernex (see [006 open question 5](../../admin/006-manage-custom-lists.md)) |
| `URL` override that discards the whole layout (LAY-R-106) | **Do not build**, or gate behind a platform-admin role | An escape hatch that silently ignores every configured field is a support nightmare and an audit hole |
| Per-placement raw CSS (`LabelCSSStyle`, `ValueCSSStyle`) | Named style tokens from a design system | Raw CSS in configuration data cannot be themed, tested, or migrated |
| Per-field **Value Javascript** (LAY-R-158) | A declarative expression language, or nothing | Arbitrary stored JavaScript per field is unreviewable and a supply-chain surface. If computed fields are needed, make them declarative |
| No lineage between Global and Firm layouts | `source_global_layout_id` + `source_version` | Required by the Hub/Spoke publish/accept/fork plan |
| Layouts not versioned (`VersionAdded`/`VersionModified` exist on fields only, LAY-R-202) | Version layouts | Form instances reference a layout; without versioning, historical forms cannot be faithfully re-rendered |
| Two creator columns (`CreatedByID` and `CreatedByMemberID`) on one table | One | Legacy duplication |

## Open questions blocking a decision

Ranked by how much each blocks the rebuild.

| # | Question | Blocks | Who can answer |
|---:|---|---|---|
| 1 | Does the `Field / Rule / Criteria` triple name the hidden field or the tested field? | The entire conditional-field model | Browser: GraphQL Explorer against a layout that has conditions |
| 2 | ~~Is code table **2035** really the Issue Type table?~~ **Answered: yes** — `TableType=2035` is `Issue Type Code` per the full 207-entry registry ([code-table-registry.md](../../data-model/code-table-registry.md)). A Form is an Issue Type and produces an `Issue`. | — | Settled |
| 3 | Where is per-placement required-ness stored? | Validation semantics and the migration of every existing required flag | Browser: layout editor + catalog re-read |
| 4 | What is the full `PageLayoutType` and `OutputType` vocabulary? | The `layout_type` enum, and the scope of PAGE-LAYOUTS-01 | Browser: GraphQL/REST schema, or `EquivalentPLTypes` values |
| 5 | Does `Program`-level setup-page assignment actually override `Firm`-level? | Whether layout assignment is one level or two | Browser: Manage Portfolios → a portfolio's setup pages |
| 6 | How is a layout's Portfolio/Capital-Program scope stored? | Multi-tenant layout visibility | Browser or schema export |
| 7 | What does **Layout Changes** (`ShowLayoutChanges.jsp`) record? | Whether layout config audit is a separate mechanism from `AuditColumn` | Browser — and ASG has explicitly asked for this |
| 8 | Does `D-18` (MCT-028 vs central layout push) survive the finding that Forms are layouts too? | PAGE-LAYOUTS-01 phase 3 scope | ASG decision, not a browser check |
