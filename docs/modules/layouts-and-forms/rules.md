# Layouts and Forms — rules

**Two sources, one register.** Rules `LAY-R-001`…`LAY-R-018` come from live browser capture and are
owned by the two capture documents in this folder. Rules `LAY-R-100` upward are derived from the
offline schema artefacts (`docs/data-fields/all-fields.csv`, `_lucernex_objects_summary.txt`,
`_xlsx_feature_list.txt`) and are listed here in full. Where the two disagree, **the capture wins**.

## LAY-R-001 … LAY-R-018 — from live capture

| Range | Subject | Owning document |
|---|---|---|
| `LAY-R-001` … `LAY-R-009` | Forms, form types, layout-per-workflow-step, the Form ⇄ Work Flow 1:1 relationship, step and approval vocabulary | [forms-vs-pages-vs-layouts.md](forms-vs-pages-vs-layouts.md#the-reconciliation-stated-as-rules) |
| `LAY-R-010` … `LAY-R-018` | Conditional field filtering — targets, the three actions, the `all`/`any` quantifier, type-dependent operators, the driver catalog, edit-layout scope | [conditional-fields.md](conditional-fields.md#rules-for-the-asg-edge-rule-engine) |

Two of those bear repeating here because everything below assumes them:

- **`LAY-R-011`** — a conditional rule set declares exactly one action: `SHOW`, `SHOW_AND_REQUIRE`
  or `HIDE`. Visibility and required-ness are **one** decision, not two.
- **`LAY-R-010`** — a rule's target is either a single placed field or an **entire sub-page
  section** (`fieldKey = subPage_<PageLayoutID>`).

## LAY-R-100 … — from the schema

Each carries an evidence label. **Observed** = seen in a capture or source artefact. **Derived** =
computed from observed data. **Inferred** = domain reasoning, not confirmed. **[BLOCKED]** = the
most likely form, pending a check that is named.

## A. Record identity and typing

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-101 | Summary Pages, Sub-pages, List Layouts, Forms, Wizards, Map Popups, Reports and Dashboard tiles are **all rows of one table, `PageLayout`**. They are distinguished by discriminator columns, not by separate record types. | Observed (schema) + Observed (008) | `all-fields.csv`; [008](../../admin/008-manage-page-layouts.md) |
| LAY-R-102 | Every layout has exactly one required `PageLayoutType`, one required `OutputType`, and one required `PageLayoutName`. | Observed | `all-fields.csv` |
| LAY-R-103 | A layout declares a single **Primary Table** (`PrimaryCodeSQLTableID`). Every field it may place is either a field of that table or a field reachable from it by a declared FK ("Related Fields"). | Observed (008, 009) | [008](../../admin/008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists), [009](../../admin/009-related-fields-and-data-model.md) |
| LAY-R-104 | A layout may be **Global** (platform-shipped, rendered with a `[Global Layout]` suffix) or **Firm** (tenant-authored). A tenant may keep the Global default per entity type or override it; the two coexist in one selector list. | Observed | [008 § Setup Pages](../../admin/008-manage-page-layouts.md#setup-pages-firmeditjspmodesetup) |
| LAY-R-105 | `AllowEdit = No` makes a layout read-only. `AllowUserCreate` separately controls whether end users may create records through it. | Observed (columns + 008 dialog) | `all-fields.csv`; [008](../../admin/008-manage-page-layouts.md#the-edit-dialog--full-metadata-surface) |
| LAY-R-106 | A layout with a non-blank `URL` **bypasses its own field configuration entirely** and redirects to that system page. Vendor help text: "*Leave blank for standard functionality. To use a system page enter the url here, related layout fields will be ignored.*" | Observed | [008](../../admin/008-manage-page-layouts.md#the-edit-dialog--full-metadata-surface) |
| LAY-R-107 | A layout can be scoped to specific **Portfolios/Capital Programs** via a required multi-select, defaulting to *All Portfolios/Capital Programs* — the same control used for dropdown values. | Observed (UI); storage **not found** in either artefact | [008](../../admin/008-manage-page-layouts.md#the-edit-dialog--full-metadata-surface), [007](../../admin/007-firm-and-client-drop-downs.md) |

## B. Composition

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-110 | A Summary Page is **composed of Sub-pages**, not authored monolithically. Each visible section corresponds to an independently-managed Sub-page layout. Proven directly for `ASG Contract Header` ⇄ the "Contract Information" section of `ASG Contract Summary`. | Observed | [008](../../admin/008-manage-page-layouts.md#manage-sub-pages-modesub) |
| LAY-R-111 | The inclusion mechanism is a `PageLayoutField` row whose `SubPageLayoutID` points at the child layout, positioned by the same coordinates as a field. | Inferred (high) | `all-fields.csv` |
| LAY-R-112 | A section's **title is supplied by the parent at the point of inclusion** (`PageLayoutField.DisplayLabel`), not by the sub-page. A sub-page opened on its own renders with no title bar. | Observed (no title bar) + Inferred (mechanism) | [008](../../admin/008-manage-page-layouts.md#manage-sub-pages-modesub); `all-fields.csv` |
| LAY-R-113 | A `PageLayoutField` row need not carry a field at all: it can be an embedded sub-layout (`SubPageLayoutID`) or literal copy (`StaticText`). | Observed (columns) | `all-fields.csv` |
| LAY-R-114 | A multi-step creation **Wizard** is a sequence of Sub-page layouts (`ASG Contract Wizard`, `Wizard Step 2`…`Step 5`), bound as an entity's creation flow via a Setup Page assignment. | Observed | [008](../../admin/008-manage-page-layouts.md#manage-sub-pages-modesub) |
| LAY-R-115 | Layout ordering among siblings uses a **previous-pointer chain** (`PreviousPageLayoutID`, `PreviousID`) with a materialised `ComputedSequenceNumber`, not a plain integer sort key. | Observed (columns) | `all-fields.csv` |
| LAY-R-116 | Layouts host **placeable, reorderable business-action buttons** (Approve Payments, Generate Rent, Extend Contracts, Alternate Rent Wizard, Copy Transaction, …) alongside fields, in the same grid with the same toolbars. A distinct button kind is labelled "**(Run Report Action)**". | Observed | [008](../../admin/008-manage-page-layouts.md#edit-layout--sections-field-grids-and-action-buttons) |
| LAY-R-117 | **[BLOCKED]** Action buttons are presumed to be `PageLayoutField` rows with no `ReportGroupAvailableFieldID`, identified by `DisplayOption`/`JSONConfigText`. No column declares a button. *Check: read `PageLayoutField` rows for `ASG Contract Summary` (96289) via GraphQL Explorer.* | Inferred (low) | — |

## C. The Edit / List duality

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-120 | A single `PageLayoutID` can carry **both** a detail Edit Layout and a grid List Layout, as two orthogonal facets of one record. Proven on `ASG Contract Payments` (96214, `PaymentTransaction`). | Observed | [008](../../admin/008-manage-page-layouts.md#a-list-type-record-can-carry-both-an-edit-layout-and-a-list-layout) |
| LAY-R-121 | The facet a placement belongs to is flagged by `PageLayoutField.IsInEditLayout`, and each facet has its **own coordinate set** — `EditRow/ColumnPosition`+`EditFieldWidth/Height` vs `ViewRow/ColumnPosition`+`ViewFieldWidth/Height`. | Inferred (high) | `all-fields.csv` |
| LAY-R-122 | A top-level parent entity with no natural "list of many inside one" view renders **"List Layout not applicable for current layout type."** This is a property of the target table, not a general one-facet-only rule. | Observed | [008](../../admin/008-manage-page-layouts.md#list-layout-tab--not-applicable-for-this-record) |
| LAY-R-123 | A field can be **searchable but hidden from the grid** — a distinct third visibility state, rendered in green as `(Searchable, Hidden in grid)`, present in both the Edit and List facets. | Observed | [008](../../admin/008-manage-page-layouts.md#a-list-type-record-can-carry-both-an-edit-layout-and-a-list-layout) |
| LAY-R-124 | A layout carries a separate **mobile ordering** (`MobileRowPosition`), i.e. responsive layout is configured, not derived. | Observed (column) | `all-fields.csv` |
| LAY-R-125 | Per-placement CSS is configurable independently for label and value (`LabelCSSStyle`, `ValueCSSStyle`). | Observed (columns) | `all-fields.csv` |

## D. Conditional field display — where the rules are stored

The rule *model* is settled by live capture and lives in
[conditional-fields.md](conditional-fields.md) as `LAY-R-010`…`LAY-R-018`. This section covers only
the **storage** question, which the capture left open, and corrects an earlier schema-side
inference.

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-130 | A conditional rule set is posted as a **single JSON document** per target — hidden form field `json.conditionalFieldsConfig` on form `ConditionFilter` — not as normalised rows. | Observed | [conditional-fields.md § Storage format](conditional-fields.md#storage-format) |
| LAY-R-131 | **Superseded.** An earlier reading of this corpus put conditional rules in `PageLayoutFilter` with `IsListFilter = false`. The live capture shows JSON-blob storage instead, so `PageLayoutFilter` is re-read as the **row-filter and pivot** table for lists and reports. See LAY-R-140. | Corrected | this document |
| LAY-R-132 | **[BLOCKED]** The destination column for that JSON is not observed. `PageLayoutField.DisplayOptionJSON` (optional per-placement textarea) is the strongest candidate: a `subPage_<id>` target *is* a `PageLayoutField` row whose `SubPageLayoutID` holds that id. Alternatives: `PageLayoutField.JSONConfigText`, `PageLayout.JSONConfigText`. *Check: read those three columns for a layout with rules.* | Inferred (moderate) | `all-fields.csv` |
| LAY-R-133 | Conditional rules are **invisible to the data API**. No type matching `condition`, `rule`, `criteria`, `visib`, `depend`, `trigger`, `expression` or `predicate` exists in the 490-type GraphQL schema, and `PageLayout*` tables are absent from the 223-object business model entirely. Rules are platform configuration, not tenant data. | Derived | [graphql-api.md](../../data-model/graphql-api.md); `_lucernex_objects_summary.txt` |
| LAY-R-134 | Because storage is an opaque blob, Lucernex **cannot answer "which layouts depend on this field or this dropdown value"**. Any Where-Used capability requires normalised predicate rows. | Derived | LAY-R-130 |

### D2. `PageLayoutFilter` — the row-filter and pivot table

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-140 | `PageLayoutFilter` holds **row filters**, not field-visibility rules: `ReportGroupAvailableFieldID` (required) + `CriteriaType1`/`CriteriaValue1` + `CriteriaType2`/`CriteriaValue2`, discriminated by a required `IsListFilter` boolean. | Observed (columns) + Inferred (role) | `all-fields.csv` |
| LAY-R-141 | The same row also carries **grouping and totalling**: `RowOrderBy`, `ColumnOrderBy`, `ShowLabel`, `ShowSubtotal`. Lucernex list/report output is pivot-shaped, not flat-list-shaped. | Observed (columns) + Inferred (semantics) | `all-fields.csv` |
| LAY-R-142 | Two `CriteriaType`/`CriteriaValue` pairs on one row express a two-clause predicate on one field — a `between`. Multiple rows chain through `ExtendedGroupFilterID` (self-FK); the combinator is undetermined. | Inferred (moderate-high) | `all-fields.csv` |
| LAY-R-143 | **[BLOCKED]** `IsListFilter` and the layout builder's `showInList=1` parameter (passed when `layoutMode` is `list` or `budget`) describe the same edit-vs-list split from two directions. Whether they are the same mechanism is unconfirmed — if they are, list-layout conditions are normalised rows while edit-layout conditions are a JSON blob. *Check: open the `showInList=1` surface and inspect what it posts.* | Open | [conditional-fields.md § Scope of evaluation](conditional-fields.md#scope-of-evaluation--edit-layout-only); `all-fields.csv` |
| LAY-R-144 | A filter may target a field reached through a relation, disambiguated by `FieldContext` — the same column `PageLayoutField` carries. | Inferred (moderate) | `all-fields.csv`; [009](../../admin/009-related-fields-and-data-model.md) |

## E. Fields, required-ness and read-only-ness

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-150 | Placeable fields come from the **shared field registry** (`ReportGroupAvailableField`), scoped to the layout's Primary Table, presented as the Available Fields tree. | Observed | [008](../../admin/008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists) |
| LAY-R-151 | Related-table fields are placeable through **Related Fields**, which for a true many-to-one FK target exposes that table's *complete* native catalog, not a curated subset. | Observed | [009](../../admin/009-related-fields-and-data-model.md#are-related-fields-a-full-catalog-or-a-curated-subset) |
| LAY-R-152 | The relationship is **asymmetric by cardinality**: from the many side, the one side appears under Related Fields; from the one side, the many side appears as an embedded `(One to Many List)` List Layout, never under Related Fields. | Observed | [009](../../admin/009-related-fields-and-data-model.md) |
| LAY-R-153 | A layout's Available Fields tree exposes each table's **Custom Lists** as a nested branch, drilling into that list's own fields. A custom list appears only under the table it belongs to. | Observed | [008](../../admin/008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists) |
| LAY-R-154 | Required fields render in red with a trailing `*`. | Observed | [008](../../admin/008-manage-page-layouts.md#edit-layout--sections-field-grids-and-action-buttons) |
| LAY-R-155 | Required-ness is intended to be set **from the layout editor (Manage Page Layouts) or from Manage Forms**, not from the field catalog — where the flag "defaults to No and is read-only". | Observed (vendor text) | `_xlsx_feature_list.txt` line 938 |
| LAY-R-156 | **[BLOCKED]** No `IsRequired`/`IsReadOnly` column exists on `PageLayoutField`, so LAY-R-155's storage is unknown — either packed into `DisplayOption1/2/JSON`, or written back to `RGAF.IsRequired`. *Check: change a field's required flag from the layout editor and re-read the catalog row.* | Open | `all-fields.csv` |
| LAY-R-157 | Some fields render as system-computed read-only placeholders (`xxxxx` on `Check Amount`, `Check Date`, `Check Number`, `AP Export Base#`) — populated by downstream processes, not by the form. | Observed | [008](../../admin/008-manage-page-layouts.md#a-list-type-record-can-carry-both-an-edit-layout-and-a-list-layout) |
| LAY-R-158 | Every registry field carries a **Value Javascript** hook, so a field can have scripted default/computed/visibility behaviour independent of the layout's declarative conditions. | Observed | [005](../../admin/005-manage-data-fields.md#per-row-actions) |

## F. Forms

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-160 | A **Form Type** is a `CodeIssueType` row. Lucernex's schema names the dropdown that selects one **`Dropdown (Form Type)`**. | Observed | `_lucernex_objects_summary.txt`, `Issue.CodeIssueTypeID` |
| LAY-R-161 | **Manage Forms** administers a firm code table (`FirmCodeEdit.jsp?TableType=2035`), i.e. the catalog of Form Types — not a layout builder. **`TableType=2035` is `Issue Type Code`**, confirmed against the full 207-entry registry. A Form is an Issue Type; the record it produces is an `Issue`. | Observed | [code-table-registry.md](../../data-model/code-table-registry.md); [004](../../admin/004-company-administration.md#company-administration) |
| LAY-R-162 | A Form Type declares which entity types it may be raised against, via eleven `IsValidFor<Entity>` flags (Portfolio, CapProgram, CapProject, OpenProject, PotentialProject, Prototype, Parcel, Facility, Location, Contract, EquipContract). | Observed | `_lucernex_objects_summary.txt`, `CodeIssueType` |
| LAY-R-163 | A Form Type carries its own numbering (`SequencePrefix`, `IsSequencePerFirm`) and lifecycle behaviour (`AllowReply`, `AutoClose`, `IsWorkFlow`). | Observed | `_lucernex_objects_summary.txt` |
| LAY-R-164 | A **form instance** is an `Issue` record. `Issue.LastPageLayoutID` records *"the name of the last form layout used to update the issue"* — **singular**, so it is depth-1 history, not a per-step audit trail. It does **not** make a multi-step form reproducible as each participant saw it. | Observed (vendor Definition text) | `_xlsx_feature_list.txt`; `_lucernex_objects_summary.txt` |
| LAY-R-165 | Forms are the workflow engine's rendering surface, bound at **two levels**: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesID` bind an approver-facing and an assignee-facing layout **per step**. A workflow with N steps therefore carries N+1 layouts. Different participants see a different form for the same record at the same step. | Observed (columns + vendor Definition text) | `all-fields.csv`; `_xlsx_feature_list.txt` |
| LAY-R-166a | `sTYPE_FORM_PAGE_LAYOUT` occurs **exactly three times** in the whole 6,158-leaf catalog (lines 691, 745, 746), all on the workflow template side. A "Form Page Layout" is definitionally a **workflow-and-role-bound** layout — the platform types it separately because it binds to a step and a role, not to an entity. | Derived (exhaustive count) | `all-fields.csv` |
| LAY-R-166b | On the *instance* side the same two columns degrade to plain `sTYPE_PAGE_LAYOUT` (`WorkFlowStep`, lines 5886-5887) — the shape of a snapshot rather than a binding. | Observed | `all-fields.csv` |
| LAY-R-166c | `WorkFlowTemplateStep.PageLayoutApproversID` / `.PageLayoutAssigneesID` are **unconstrained FKs**: nothing ties the chosen layout to the step's Form Type. The `LAR`/`ASR`/`RPR` layout-name prefixes are manual discipline, not a constraint. | Derived | `all-fields.csv` |
| LAY-R-166d | ASG has recorded the consequence as a pain point, in words that independently confirm the two-layouts-per-step model: *"For every step, the administrator must manually select the correct Form Layouts for both Assignees and Approvers. This creates a high cognitive load to keep forms and workflows perfectly synchronized."* | Observed | `_xlsx_feature_list.txt` line 351 |
| LAY-R-166e | The workflow engine has **no general mechanism for passing field values between steps**. `WorkFlowTemplateStepAction.AutoCopyAmounts` is the only data-flow affordance and is hard-coded to budget amounts into a Custom List on a layout with `PageLayout.IsBudgetImpacting` set; `PassAdhocToNewWF`/`PassPriorityToNewWF` carry routing metadata into a *spawned* workflow, not data between steps. With Cost Management out of scope there is nothing here to port — ASG Edge+ must design step-to-step data flow from scratch. | Derived (exhaustive scan of all 37 `WorkFlowTemplateStepAction` fields) | `_lucernex_objects_summary.txt`; [modules/workflow/](../workflow/README.md) |
| LAY-R-166 | The field registry's top-level group **`Specialized Forms`** is the only group applicable to Issue and not to Portfolio or Entity; its member entities are the Issue-derived transactional forms (Bid Package, Bidder Issue, Service Request, Work Order, Purchase Order, Change Order, Invoice Issue, Invoice Item, Bid Package Template). | Observed (applicability) + Derived (membership) | [005](../../admin/005-manage-data-fields.md#top-level-group-inventory); `docs/data-fields/INDEX.md` |

## G. Custom Lists

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-170 | A **Custom List** is a tenant-authored mini record type: its own field schema plus its own layout. It is not a picklist. | Observed | [006](../../admin/006-manage-custom-lists.md) |
| LAY-R-171 | The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves; its layout is a `PageLayout` whose `ClientListRGDID` points back at the node. The list itself is *also* an RGAF leaf of type `sTYPE_CLIENT_LISTS` on its owning entity. | Observed (6/6 name match) | `all-fields.csv`; [006](../../admin/006-manage-custom-lists.md) |
| LAY-R-172 | Each custom list gets its **own field-name namespace** derived from its initials (`CRL_*` for Client Request Log, `OpEx*` for Operating Expenses), plus shared system audit fields (`ModifiedByID`, `ModifiedDate`) with no prefix. | Observed | [006](../../admin/006-manage-custom-lists.md#field-schema--edit-fields-client-request-log-example), [008](../../admin/008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists) |
| LAY-R-173 | A custom-list field can be typed **Drop Down >>**, cascading into a Drop Down **Type** category and then a specific drop-down, binding it to Firm or Client Drop Downs. | Observed | [006](../../admin/006-manage-custom-lists.md#field-editor--edit-reportform-field-opened-via-edit-on-complete-date), [007](../../admin/007-firm-and-client-drop-downs.md) |
| LAY-R-174 | A custom list has a **Type** — `Standard` (2634) or `Part` (2635) — sharing machinery with the Parts and Inventory module. | Observed | [006](../../admin/006-manage-custom-lists.md#data-observed--full-list-inventory) |
| LAY-R-175 | Custom Lists are **Firm-scoped only**; no Global/platform custom list concept was observed. | Observed (absence) | [006](../../admin/006-manage-custom-lists.md#tenant-and-permission-implications) |

## H. Role binding and assignment

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-180 | A layout becomes an entity's **creation wizard** by assignment on Setup Pages, one slot per entity type. | Observed | [008](../../admin/008-manage-page-layouts.md#setup-pages-firmeditjspmodesetup) |
| LAY-R-181 | Setup-page assignment exists at **two levels**: `Firm` (11 slots, tenant default) and `Program` (18 slots — 11 setup pages + 7 map popups, per Portfolio/Capital Program). Only the Firm level was observed in the UI. | Observed (columns) + Inferred (override semantics) | `all-fields.csv` |
| LAY-R-182 | A setup-page selector lists **any** layout whose Primary Table matches the target — Summary Pages, Sub-pages and Wizards alike — not only Wizard-type records. | Observed (`ASG Client Request Log` offered as a Portfolio Layout) | [008](../../admin/008-manage-page-layouts.md#setup-pages-firmeditjspmodesetup) |
| LAY-R-183 | **Map Popup Layouts** are a third, minimal rendering context, distinct from Summary Page and Wizard. The seven `*MapSetupLayoutID` columns sit on `Program`, not `Firm`, implying portfolio scope. | Observed (UI + columns) + Inferred (scope) | [008](../../admin/008-manage-page-layouts.md#map-popup-layouts-firmeditjspmodemap); `all-fields.csv` |
| LAY-R-184 | A layout is placed in the **navigation menu** via a Parent Tab tree selection, materialised as `HierarchyName` (e.g. `Contract : Details : Summary`). Sub-pages have no such placement. | Observed | [008](../../admin/008-manage-page-layouts.md#the-edit-dialog--full-metadata-surface) |
| LAY-R-185 | A new layout may be seeded from an existing one via "**Initialize layout from existing layout**", available only on create, not on edit. Whether it is a full clone or a partial template is unknown. | Observed (control) + Open (behaviour) | [008](../../admin/008-manage-page-layouts.md#the-add-item-empty-state-manage-summary-pages) |

## I. Security

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-190 | Access is granted per **user class** against a layout, a field, a field *group*, or a dashboard component — all from one `UserClassSecurity` table with a `CodeSecurityPrivilegeID` and a `SecurityLevelByteValue`. (A fifth subject in the out-of-scope budget domain also exists.) | Observed | `all-fields.csv` |
| LAY-R-191 | Granting on a `ReportGroupDataID` (group or subgroup) means field permissions **inherit down the registry tree**, not per-field only. | Inferred (high) | `all-fields.csv` |
| LAY-R-192 | Field visibility is therefore decided by three independent systems: **security**, **layout placement**, and **conditional rules**. A stated precedence is required; none is documented by Lucernex. Recommended for ASG Edge+: security → placement → condition. | Derived + Inferred | this document |

## J. Change tracking

| # | Rule | Label | Source |
|---|---|---|---|
| LAY-R-200 | Layout changes are audited — the admin dashboard exposes a **Layout Changes** tool (`ShowLayoutChanges.jsp`). Its contents were never opened; ASG's own review note records "*Need further explanation as to what this is.*" | Observed (link + note) | [004](../../admin/004-company-administration.md#datapS-tools), `_xlsx_feature_list.txt` line 44 |
| LAY-R-201 | Field-level value changes are audited in `AuditColumn`, filed under the registry's group and subgroup — so an audit entry inherits the Data Fields taxonomy. | Derived (11-for-11 column match) | [007](../../admin/007-firm-and-client-drop-downs.md#value-level-editor--scoping-and-audit-log); `all-fields.csv` |
| LAY-R-202 | Layout records carry `VersionAdded`/`VersionModified` at the *field* level (`RGAF`) but not at the layout level — layout versioning, if any, is not visible in the schema. | Observed (absence) | `all-fields.csv` |
