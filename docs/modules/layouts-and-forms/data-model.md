# Layouts and Forms — data model

**Stated up front.** Three tables carry the whole subsystem: `PageLayout` (42 fields),
`PageLayoutField` (27), `PageLayoutFilter` (16). None of the three appears in
`_lucernex_objects_summary.txt` — Lucernex keeps presentation metadata outside its business object
model — so every column here comes from `docs/data-fields/all-fields.csv`, which is itself an
Observed capture of the Manage Data Fields catalog ([005](../../admin/005-manage-data-fields.md)).
All three live in the catalog's `Statics` top-level group, all Global scope.

**Scope note.** Cost Management and Budgeting are out of scope. Budget and Bid columns on
`PageLayout` / `PageLayoutField` are retained below because they are **type discriminators and FK
slots on tables that are in scope** — deleting them would misrepresent the layout record — but the
domains behind them are not analysed. `BudgetColumnType`'s `IsValidFor*` family is cited once, as
pattern evidence only.

**"Payment" is not a budget keyword.** Lease and rent payments are in scope — `PaymentTransaction`,
the `ASG Contract Payments` layout (96214) used below as the worked example for the Edit/List
duality, and the `Approve Payments` / `Generate Rent` action buttons all stay. Only the
*capital-project* cost stack is excluded.

## Table inventory

| Table | Fields | In `_lucernex_objects_summary.txt`? | Catalog group | Doc |
|---|---:|:---:|---|---|
| `PageLayout` | 42 | **No** | `Statics` | `docs/data-fields/page-layout.md` |
| `PageLayoutField` | 27 | **No** | `Statics` | `docs/data-fields/page-layout-field.md` |
| `PageLayoutFilter` | 16 | **No** | `Statics` | `docs/data-fields/page-layout-filter.md` |
| `ReportGroupAvailableField` | 27 | **Yes** | `Company Items` | see [reporting/data-model.md](../reporting/data-model.md) |
| `ReportGroupData` | 5 | **Yes** | `Company Items` | see [reporting/data-model.md](../reporting/data-model.md) |
| `CodeIssueType` | 19 | **Yes** | — | Form Types (Manage Forms) |
| `Issue` | 56 | **Yes** | `Specialized Forms` | Form instances |
| `ClientListRow` | 24 | **Yes** | — | Custom List rows |
| `UserClassSecurity` | 21 | **Yes** | — | Layout/field/group security grants |

The presence/absence split is architecturally load-bearing: `PageLayout*` are **platform
configuration**, `Issue`/`ClientListRow` are **tenant business data**. `ReportGroupAvailableField`
sits on the business-data side of that line, which is why the field registry is API-addressable and
the layout tables are not. **Derived** (membership checks against both artefacts).

## `PageLayout` — 42 fields

| Field | Type | Reqd | Role |
|---|---|:---:|---|
| `PageLayoutID` | `sTYPE_UNFORMATTED_NUMBER` | | PK |
| `PageLayoutName` | `sTYPE_TEXT` | **Y** | The **Page Layout Name\*** on the edit dialog |
| `Description` | `sTYPE_TEXTAREA` | | |
| `PageLayoutType` | `sTYPE_TEXT` | **Y** | Primary discriminator (`SEP`/`SUB`/`LIST`/… — see [forms-vs-pages-vs-layouts.md](forms-vs-pages-vs-layouts.md)) |
| `EquivalentPLTypes` | `sTYPE_TEXT` | | Which other types this layout may substitute for |
| `OutputType` | `sTYPE_TEXT` | **Y** | Render target |
| `PrimaryCodeSQLTableID` | `sCODE_SQLTABLE` | | **Primary Table\*** — the driving business object |
| `URL` | `sTYPE_TEXTAREA` | | Redirect to a system page instead of rendering (008 edit dialog) |
| `AllowEdit` | `sTYPE_BOOLEAN` | **Y** | **Allow Edit\*** Yes/No radio |
| `AllowUserCreate` | `sTYPE_BOOLEAN` | | End-user record creation through this layout |
| `IsSEPOrListLayout` | `sTYPE_BOOLEAN` | | Entity page or list, vs report/form |
| `IsReport` | `sTYPE_BOOLEAN` | | Layout is run, not viewed |
| `IsDashboardReport` | `sTYPE_BOOLEAN` | | Dashboard tile |
| `IsGlobalReport` | `sTYPE_BOOLEAN` | | Platform-shipped vs tenant-authored |
| `IsMenuLink` | `sTYPE_BOOLEAN` | | Own navigation entry |
| `IsBudgetImpacting` | `sTYPE_BOOLEAN` | | Marks a budget-domain layout — a type discriminator. The domain is out of scope, but this flag gates the workflow engine's *only* step-to-step data-flow mechanism; see below |
| `IsOrdered` | `sTYPE_BOOLEAN` | | Participates in the sibling chain |
| `HierarchyName` | `sTYPE_TEXT` | | Nav-tree path — the **Top Menu** breadcrumb (e.g. `Contract : Details : Summary`) |
| `ParentID` / `PreviousID` | `sTYPE_NUMBER` | | Generic ordered-tree columns |
| `ParentPageLayoutID` | `sTYPE_PAGE_LAYOUT` | | Layout-to-layout parent |
| `PreviousPageLayoutID` | `sTYPE_PAGE_LAYOUT` | | Sibling ordering |
| `ComputedSequenceNumber` | `sTYPE_NUMBER` | | Materialised order |
| `OrderRecordName` / `OrderRecordType` | `sTYPE_TEXT` | | Ordering context |
| `CodeIssueTypeID` | `sCODE_ISSUE_TYPE` | | **Binds the layout to a Form Type** |
| `ClientListRGDID` | `sTYPE_REPORT_GROUP_DATA` | | **Binds the layout to a Custom List** |
| `BudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | | Budget binding — out of scope |
| `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | | Currency for money columns |
| `EntitySelectionFilter` | `sTYPE_NUMBER` | **Y** | Which entities the layout may be run against |
| `RunModeFilters` | `sTYPE_NUMBER` | **Y** | Which filters are offered at run time |
| `LastRunBy` | `sTYPE_MEMBER` | | **Run tracking** |
| `LastRunDate` | `sTYPE_TIME` | | **Run tracking** |
| `OwnedByMemberID` | `sTYPE_MEMBER` | | Personal ownership (a "Save As my report") |
| `CreatedByMemberID` / `CreatedByID` | `sTYPE_MEMBER` | | Two creator columns — legacy overlap |
| `CreatedDate` / `ModifiedDate` / `ModifiedByID` | | | Lifecycle |
| `FirmID` | `sTYPE_FIRM` | | Tenant owner |
| `JSONConfigText` | `sTYPE_TEXTAREA` | | Overflow configuration |
| `BOMapClientRecordID` | `sTYPE_TEXT` | **Y** | Import/integration correlation id |

Not represented as a column anywhere in the capture: the **Available for the following
Portfolios/Capital Programs\*** chip control observed on the edit dialog
([008](../../admin/008-manage-page-layouts.md#the-edit-dialog--full-metadata-surface)). It is
almost certainly a link table absent from both artefacts. **Open question.**

### `IsBudgetImpacting` gates the only data-flow mechanism there is

Worth stating even though the budget domain is out of scope, because with that domain removed the
finding **inverts into something in scope**.

`WorkFlowTemplateStepAction.AutoCopyAmounts` is the workflow engine's only mechanism for carrying
data from one step to the next, and it is hard-coded to copy *budget amounts* into a Custom List on
a layout with `PageLayout.IsBudgetImpacting` set. Finding from
[modules/workflow/](../workflow/README.md); **verified independently here** by scanning all 37
declared fields of `WorkFlowTemplateStepAction` in `_lucernex_objects_summary.txt`:

| Field group | Fields | Carries form data between steps? |
|---|---|:---:|
| Amount handling | `AutoCopyAmounts`, `AutoClearAmounts`, `FifoPayApp`, `GenPurchOrderLineSeqNum`, `SendPaymentInfo` | Amounts only |
| Routing | `MoveToStepNumber`, `RestartStep`, `CloseWorkFlow`, `KickOffWorkFlowTemplateID`, `KickOffTargetWFTemplateID`, `WorkFlowTemplateKickOffID` | No |
| Notification | five `Notify*` booleans | No |
| Approval semantics | `IsApprovalAction`, `RequireAllApprovers`, `RequireApproverSig`, `DisableEditAfterDecision`, `CodeLastActionStatusID` | No |
| Cross-workflow hand-off | `PassAdhocToNewWF`, `PassPriorityToNewWF` | Routing metadata only — ad-hoc member and priority, **not field values** |
| Scripting | `IsEnabledLxJSCode` | Escape hatch, not a declared mechanism |

**Derived, from an exhaustive field scan: there is no general mechanism for passing field values
between workflow steps.** The two `Pass*ToNewWF` columns look like they might be one and are not —
they carry routing metadata into a *spawned* workflow, not data between steps of the same one.

**Consequence for ASG Edge+:** with Cost Management excluded there is nothing here to port. A
multi-step form that needs step 3 to see what step 1 entered requires a step-to-step data-flow
design built from scratch. That is a real gap in the PAGE-LAYOUTS-01 / workflow scope, not an
omission from this analysis. The layout-per-step model
([forms-vs-pages-vs-layouts.md](forms-vs-pages-vs-layouts.md#one-layout-per-workflow-step)) makes it
sharper: every step renders a *different* layout over the same `Issue`, so continuity depends
entirely on the record's own fields — there is no step-scoped state at all.

## `PageLayoutField` — 27 fields

One row = one placed item on one layout. "Item" is broader than "field": a row can be a registry
field, an embedded sub-layout, or literal text.

| Field | Type | Reqd | Role |
|---|---|:---:|---|
| `PageLayoutFieldID` | `sTYPE_UNFORMATTED_NUMBER` | | PK |
| `PageLayoutID` | `sTYPE_PAGE_LAYOUT` | **Y** | Owning layout |
| `ReportGroupAvailableFieldID` | `sTYPE_REPORT_GROUP_AVAILABLE_FIELD` | | **The placed registry field** (null when the row is a sub-layout or static text) |
| `SubPageLayoutID` | `sTYPE_PAGE_LAYOUT` | | **The embedded sub-page** — how a Summary Page composes a section |
| `StaticText` | `sTYPE_TEXTAREA` | | Literal copy with no field behind it |
| `DisplayLabel` | `sTYPE_TEXTAREA` | | **Per-placement caption override** — including a section's title when the row is a sub-layout |
| `AccessorName` | `sTYPE_TEXT` | | Denormalised field name |
| `FieldContext` | `sTYPE_TEXT` | | Join path, when the field came from a related table ([009](../../admin/009-related-fields-and-data-model.md)) |
| `IsInEditLayout` | `sTYPE_BOOLEAN` | | **The Edit-Layout / List-Layout facet flag** |
| `EditRowPosition`, `EditColumnPosition`, `EditFieldWidth`, `EditFieldHeight` | `sTYPE_NUMBER` | | Geometry on the **detail form** |
| `ViewRowPosition`, `ViewColumnPosition`, `ViewFieldWidth`, `ViewFieldHeight` | `sTYPE_NUMBER` | | Geometry in the **grid / view** |
| `HeaderColumnPosition` | `sTYPE_NUMBER` | | Grid header column |
| `MobileRowPosition` | `sTYPE_NUMBER` | | Responsive ordering |
| `DisplayOption1`, `DisplayOption2` | `sTYPE_NUMBER` | **Y** | Display bitmasks — alignment, wrap/fit, searchable-hidden (see below) |
| `DisplayOptionJSON` | `sTYPE_TEXTAREA` | | Newer overflow for the above |
| `LabelCSSStyle`, `ValueCSSStyle` | `sTYPE_TEXTAREA` | | Per-placement styling |
| `BudgetViewID` | `sTYPE_BUDGET_VIEW` | | Binds a placed budget grid — out of scope |
| `JSONConfigText` | `sTYPE_TEXTAREA` | | Overflow |
| `BOMapClientRecordID` | `sTYPE_TEXT` | **Y** | Correlation id |

**Two independent coordinate sets on one row** (`Edit*` and `View*`) plus `IsInEditLayout` is the
column-level explanation for 008's finding that `ASG Contract Payments` (`PageLayoutID=96214`)
carries *both* a sectioned detail form and a single-row column grid. One `PageLayout`, two
renderings, one set of placement rows. **Observed** columns; **Inferred** conclusion, high
confidence.

`DisplayOption1`/`DisplayOption2` being **required** on every row argues they are always-present
bitmasks rather than optional pointers. Corroborating: the sublist editor's handlers
`doAlign(fieldId,1,{0|8192|16384})` and `doWrap(fieldId,true|false)`
([006](../../admin/006-manage-custom-lists.md#visible-structure)) are exactly numeric display
flags, and the green `(Searchable, Hidden in grid)` state observed in
[008](../../admin/008-manage-page-layouts.md#a-list-type-record-can-carry-both-an-edit-layout-and-a-list-layout)
is a third such flag. **Inferred**, moderate-to-high confidence.

**No `IsRequired` and no `IsReadOnly` column exists on `PageLayoutField`** — despite the vendor
stating that required-ness is set from Manage Page Layouts or Manage Forms
(`_xlsx_feature_list.txt` line 938). Live capture partly explains this: the conditional rule action
`Show and Require` makes required-ness a *rule outcome* rather than a stored flag
([conditional-fields.md](conditional-fields.md#the-action--three-values-not-two)). That accounts for
conditional required-ness, not for the unconditional red-asterisk fields observed on layouts.
**Still open.**

`DisplayOptionJSON` is the most likely home for the conditional rule blob: it is an optional
per-placement JSON textarea, and a rule whose target is `subPage_<id>` maps exactly onto the
`PageLayoutField` row whose `SubPageLayoutID` holds that id. `JSONConfigText` on the same table, and
on `PageLayout`, are the alternatives. **Inferred**, moderate confidence.

## `PageLayoutFilter` — 16 fields

| Field | Type | Reqd | Role |
|---|---|:---:|---|
| `PageLayoutFilterID` | `sTYPE_UNFORMATTED_NUMBER` | | PK |
| `PageLayoutID` | `sTYPE_PAGE_LAYOUT` | **Y** | Owning layout |
| `ReportGroupAvailableFieldID` | `sTYPE_REPORT_GROUP_AVAILABLE_FIELD` | **Y** | The field being filtered or grouped |
| `AccessorName` | `sTYPE_TEXT` | | Denormalised field name |
| `FieldContext` | `sTYPE_TEXT` | | Join path when the field came from a related table |
| `CriteriaType1` / `CriteriaValue1` | `sTYPE_NUMBER` / `sTYPE_TEXTAREA` | | First clause: operator + value |
| `CriteriaType2` / `CriteriaValue2` | `sTYPE_NUMBER` / `sTYPE_TEXTAREA` | | Second clause on the same field — a `between` |
| `IsListFilter` | `sTYPE_BOOLEAN` | **Y** | Discriminator |
| `ExtendedGroupFilterID` | `sTYPE_PAGE_LAYOUT_FILTER` | | Self-FK — clause chaining |
| `RowOrderBy` / `ColumnOrderBy` | `sTYPE_NUMBER` | | Grouping position on each axis |
| `ShowLabel` / `ShowSubtotal` | `sTYPE_BOOLEAN` | | Render the label / emit a subtotal at a grouping break |
| `BOMapClientRecordID` | `sTYPE_TEXT` | **Y** | Correlation id |

**This is the row-filter and pivot table, not the conditional-field store.** An earlier reading of
the offline artefacts placed conditional field rules here, on the strength of the `Show Conditional
Field Associations` dialog's `Field / Rule / Criteria` columns lining up with
`ReportGroupAvailableFieldID` / `CriteriaType1` / `CriteriaValue1`, and of `IsListFilter` echoing
the dialog's own "*Conditions affect the edit layout and NOT the list layout*" heading. Live capture
([conditional-fields.md](conditional-fields.md#storage-format)) shows conditional rules are instead
posted as a JSON document (`json.conditionalFieldsConfig`), so that reading is **withdrawn**.

What remains is a coherent report/list filter table: `RowOrderBy` + `ColumnOrderBy` + `ShowSubtotal`
on the same row as the criteria is a **pivot** shape — one table saying both what to restrict and
how to break and total the result. **Inferred**, high confidence.

`IsListFilter` still needs an explanation. The layout builder passes `showInList=1` when
`layoutMode` is `list` or `budget` ([conditional-fields.md](conditional-fields.md#scope-of-evaluation--edit-layout-only)),
i.e. list-mode layouts have a *separate* conditional surface. If `IsListFilter` is that surface's
storage, then list-layout conditions are normalised rows while edit-layout conditions are an opaque
blob — an asymmetry worth confirming before copying either. **Open question.**

## Foreign-key edges

### Inbound to `PageLayout` (46 `sTYPE_PAGE_LAYOUT` + 3 `sTYPE_FORM_PAGE_LAYOUT` columns)

| From | Column(s) | Cardinality | Meaning |
|---|---|---|---|
| `Firm` | 11 × `*SetupPageLayoutID` | 1 per entity type | Tenant-default creation wizard per entity type |
| `Program` | 18 × `*SetupPageLayoutID` / `*MapSetupLayoutID` | 1 per entity type | **Portfolio-level override** of the same 11, plus 7 map-popup slots |
| `CodeIssueType` ← `PageLayout.CodeIssueTypeID` | reverse direction | 1 layout → 1 form type | Form-type binding |
| `WorkFlowTemplate` | `PageLayoutID` — `sTYPE_FORM_PAGE_LAYOUT` | 1 per workflow | The **kick-off (Submit) layout**. Vendor help: *"Select the form whose completion you want to have kick off this work flow."* |
| `WorkFlowTemplateStep` | `PageLayoutApproversID`, `PageLayoutAssigneesID` — both `sTYPE_FORM_PAGE_LAYOUT` | **2 per step** | The approver-facing and assignee-facing layouts for one step. Vendor help: *"Select which form layout approvers / assignees should see for this step."* |
| `WorkFlowStep` (instance) | `PageLayoutApproversID`, `PageLayoutAssigneesID` — plain `sTYPE_PAGE_LAYOUT` | 2 per step instance | The runtime snapshot of the two template-step layouts. The type **degrades** from `sTYPE_FORM_PAGE_LAYOUT` on the template to plain `sTYPE_PAGE_LAYOUT` here — what a snapshot looks like |
| Bid/Cost domain (`BidPackage`, `BidPackageTemplate`) | 8 layout slots | 8 | **Out of scope** — listed only so the 46-column arithmetic reconciles |
| `ComparisonReport` | `PageLayoutID` (**required**) | 1 | Comparison report rendering |
| `UserClassSecurity` | `PageLayoutID` | 1 | Per-user-class layout grant |
| `PageLayout` (self) | `ParentPageLayoutID`, `PreviousPageLayoutID` | tree + chain | Composition and ordering |
| `PageLayoutField` | `PageLayoutID` (**required**), `SubPageLayoutID` | many | Placement; sub-page inclusion |
| `PageLayoutFilter` | `PageLayoutID` (**required**) | many | Filters and conditions |

**Derived** by grepping `all-fields.csv` for `sTYPE_PAGE_LAYOUT` and `sTYPE_FORM_PAGE_LAYOUT`.

#### `sTYPE_FORM_PAGE_LAYOUT` is the schema's own proof of layout-per-step-per-role

Those **three** occurrences at `all-fields.csv` lines 691, 745 and 746 are the **only** three in the
entire 6,158-leaf catalog. **Derived.** All three are on the workflow *template* side, and their
distribution is the mechanism:

| Column | Holder | Cardinality |
|---|---|---|
| `PageLayoutID` ("Active Layout") | `WorkFlowTemplate` | **one per workflow** — the Submit/kick-off form |
| `PageLayoutApproversID` | `WorkFlowTemplateStep` | **one per step** |
| `PageLayoutAssigneesID` | `WorkFlowTemplateStep` | **one per step** |

A "Form Page Layout" is therefore *definitionally* a workflow-bound layout: the platform gives it a
separate type precisely because it binds to a **step** and a **role**, not to an entity. That is
independent structural evidence for the layout-per-step model observed live in
[forms-vs-pages-vs-layouts.md](forms-vs-pages-vs-layouts.md#one-layout-per-workflow-step), and the
arithmetic corroborates it: a workflow with N steps carries N+1 layouts, the extra being Submit —
matching the observed 4-layouts-for-3-steps and 9-for-8 counts.

An earlier revision of this document placed all three columns on `WorkFlowTemplate`. That was wrong
and it mattered: collapsing them loses the N×2 per-step role surfaces. Corrected against
`all-fields.csv` and the vendor Definition text; the correction came from the workflow analysis in
[modules/workflow/](../workflow/README.md).

### Outbound from the layout tables

| From | To | Column |
|---|---|---|
| `PageLayoutField` | `ReportGroupAvailableField` | `ReportGroupAvailableFieldID` |
| `PageLayoutFilter` | `ReportGroupAvailableField` | `ReportGroupAvailableFieldID` (**required**) |
| `PageLayoutFilter` | `PageLayoutFilter` | `ExtendedGroupFilterID` |
| `PageLayout` | `ReportGroupData` | `ClientListRGDID` |
| `PageLayout` | `CodeIssueType` | `CodeIssueTypeID` |
| `PageLayout` | code table | `PrimaryCodeSQLTableID` (`sCODE_SQLTABLE`) |
| `PageLayout` / `PageLayoutField` | budget domain | `BudgetColumnTypeID`, `BudgetViewID` — **out of scope** |

## The form side

| Table | Fields | Key columns |
|---|---:|---|
| `CodeIssueType` — **a Form Type** (code table `2035`, *Issue Type Code*) | 19 | `ShortName`, `ActualLongName`, `SequencePrefix`, `IsSequencePerFirm`, `AllowReply`, `AutoClose`, `IsWorkFlow`, `Inactive`, 11 × `IsValidFor<Entity>` |
| `Issue` — **a form instance** | 56 | `CodeIssueTypeID` (declared type **`Dropdown (Form Type)`**), `LastPageLayoutID` (see caveat below), `SequenceNumber`, `Subject`, `Body`, `AssignedToMemberIDs`, `IsClosed`, `IsPrivate`, `IsCritical`, `NumberOfResponses`, `ProjectEntityID`, `WorkFlowAdhocMemberID` |
| `IssueResponse` | 11 | Threaded replies — `IssueID`, `SequenceNumber`, `Subject`, `Body` |
| `Question` | 14 | Q&A on an issue — `AcceptedResponseID`, `IsPublished`, `IsShared`, `IsPrivateQandA` |

`CodeIssueType.IsValidFor*` — exactly 11 flags: `Portfolio`, `CapProgram`, `CapProject`,
`OpenProject`, `PotentialProject`, `Prototype`, `Parcel`, `Facility`, `Location`, `Contract`,
`EquipContract` — is a recurring Lucernex idiom: the identical eleven-way applicability vocabulary
appears on `BudgetColumnType` too, cited here purely as **pattern** evidence. **Observed.** It is how a
form type declares which entity types it may be raised against — the ASG Edge+ equivalent of
"which record types can this form attach to".

### `Issue.LastPageLayoutID` is depth-1 history, not an audit trail

Vendor Definition, **Observed** (`_xlsx_feature_list.txt`): *"The name of the last form layout used
to update the issue."*

It is **singular**. Because a Form shows a different layout at every step *and* a different one per
role (approver vs assignee), one pointer records only the surface the record was **last** edited
through — not the surface each approver actually saw. Reconstructing an eight-step Lease Admin
Request as each participant saw it requires the per-step `WorkFlowTemplateStep.PageLayoutApproversID`
/ `PageLayoutAssigneesID` rows, and only for as long as those rows survive unedited.

This corrects an earlier reading in this folder that treated `LastPageLayoutID` as what stops a
layout edit from reinterpreting historical form data. It does not. The ASG Edge+ consequence is in
[asg-edgeplus-mapping.md](asg-edgeplus-mapping.md#what-must-be-built): store the layout reference on
the **decision record**, not on the request. Analysis from [modules/workflow/](../workflow/README.md).

## Security overlay

`UserClassSecurity` (21 fields) grants against **four** different subjects from one table:

| Subject | Column |
|---|---|
| A layout | `PageLayoutID` |
| A registry field | `ReportGroupAvailableFieldID` |
| A registry group / subgroup | `ReportGroupDataID`, `RootReportGroupDataID`, `SubReportGroupDataID` |
| A dashboard component | `DashboardComponentTitle` |
| A budget column type | `BudgetColumnTypeID` — out of scope |

plus `CodeUserClassID`, `CodeSecurityPrivilegeID`, `SecurityLevelName`, `SecurityLevelByteValue`,
`SecurityType`, `SecurityObjectNameText`, `GroupHierarchy`, `GroupHierarchyNoPrefix`. **Observed.**

Two consequences for the rebuild. First, **field visibility is decided by at least three
independent systems** — security, layout placement, and conditional rules — and their precedence
must be stated. Second, granting on a **group** node (`ReportGroupDataID`) means security is
inherited down the registry tree, so an ASG Edge+ permission model that only grants per-field
will not reproduce Lucernex behaviour.

## Confidence

| Claim | Label |
|---|---|
| Column names, types and required flags for all three layout tables | Observed (`all-fields.csv`) |
| Layout tables absent from the business object model | Derived (membership check, two artefacts) |
| `IsInEditLayout` + dual coordinates explain the Edit/List duality | Inferred (high) |
| `SubPageLayoutID` + `DisplayLabel` explain sub-page inclusion and section titles | Inferred (high) |
| `DisplayOption1/2` are display bitmasks, not condition pointers | Inferred (moderate-high) |
| `Program` overrides `Firm` for setup pages | Inferred (moderate) — never observed in the UI |
| Portfolio scoping of a layout is a link table | Inferred (moderate) — no column found |
