# Layouts and Forms

**Stated up front.** Lucernex presents Manage Page Layouts, Manage Forms, Manage Custom Lists and
Manage Data Fields as four distinct admin concepts. They run on shared machinery: **one field
registry** (`ReportGroupAvailableField`), **one layout record type** (`PageLayout`, 42 columns whose
booleans decide what kind of thing a layout is), **one placement table** (`PageLayoutField`, whose
`IsInEditLayout` flag and dual coordinate sets let a single layout be both a detail form and a
grid), and **one layout builder** driven by a `layoutMode` discriminator. What differs is *what you
point the engine at*: a **Page Layout** presents an entity the platform already defines; a **Form**
and a **Custom List** each define a new tenant record type and then get layouts for it.

## Contents

| Document | What it covers | Primary evidence |
|---|---|---|
| [forms-vs-pages-vs-layouts.md](forms-vs-pages-vs-layouts.md) | **The reconciliation.** What a Form, a Page, a Layout and a Custom List each are; Manage Forms running on the generic code-table editor; layout-per-workflow-step; the Form ⇄ Work Flow 1:1 relationship | Live browser capture |
| [conditional-fields.md](conditional-fields.md) | **The conditional-filtering rule engine, resolved.** `Show / Show and Require / Hide`, `all`/`any`, type-dependent operators, the 85-field cross-entity driver catalog, JSON storage | Live browser capture |
| [data-model.md](data-model.md) | `PageLayout` / `PageLayoutField` / `PageLayoutFilter` column by column, every FK edge, the form and security tables | Offline schema artefacts |
| [rules.md](rules.md) | The consolidated rule register — `LAY-R-001`…`018` from the two capture documents, then `LAY-R-100`+ derived from the schema | Both |
| [asg-edgeplus-mapping.md](asg-edgeplus-mapping.md) | Concept mapping, what to build, what to deliberately differ on, and what blocks a decision | Both |

## Related documents

| Document | Relationship |
|---|---|
| [admin/008 — Manage Page Layouts](../../admin/008-manage-page-layouts.md) | The primary layout-builder capture |
| [admin/006 — Manage Custom Lists](../../admin/006-manage-custom-lists.md) | The `layoutMode=sublist` editor and the "Add Report/Form Field" evidence |
| [admin/005 — Manage Data Fields](../../admin/005-manage-data-fields.md) | The field registry as a screen |
| [admin/009 — Related Fields](../../admin/009-related-fields-and-data-model.md) | The FK model the conditional driver catalog walks |
| [admin/007 — Firm and Client Drop Downs](../../admin/007-firm-and-client-drop-downs.md) | `FirmCodeEdit.jsp` — the same editor Manage Forms runs on |
| [data-model/graphql-api.md](../../data-model/graphql-api.md) | 490 types, 10 canonical field types, the `HasUDFs` / `ClientListRowInterface` / `IssueInterface` interfaces |
| [data-model/code-table-registry.md](../../data-model/code-table-registry.md) | All 207 `TableType` discriminators — the source identifying `2035` as `Issue Type Code` |
| [modules/reporting/](../reporting/README.md) | A report is a `PageLayout` with `IsReport = true` — same engine, different face |
| [modules/workflow/](../workflow/README.md) | A Form's process half |

## The six sentences that matter

1. `PageLayout` carries `IsReport`, `IsDashboardReport`, `IsGlobalReport`, `OutputType`,
   `RunModeFilters`, `LastRunBy` and `LastRunDate` — **a report is a layout that gets run**.
2. `PageLayoutField.IsInEditLayout` plus separate `Edit*Position` and `View*Position` coordinates —
   **one layout record renders both a form and a grid**.
3. `PageLayoutField.SubPageLayoutID` plus `DisplayLabel` — **a section is an embedded sub-layout,
   titled by the parent at the point of inclusion**. A conditional rule can target a whole section
   this way (`fieldKey = subPage_<id>`).
4. A **Form type is an Issue Type.** `Manage Forms` is `FirmCodeEdit.jsp?TableType=2035`, and
   `TableType=2035` is confirmed as `Issue Type Code` against the full 207-entry code-table
   registry. Corroborated from the schema side twice: `Issue.CodeIssueTypeID` is declared
   `Dropdown (Form Type)`, and `CodeIssueType`'s columns match the observed form-type properties one
   for one — `SequencePrefix`, `IsSequencePerFirm`, `AllowReply`, `AutoClose`, `IsWorkFlow`, plus 11
   `IsValidFor*` attachability booleans. **The record a Form produces is an `Issue`.**
5. A Form gets **one layout per workflow step**, so the same record shows a different surface at
   each stage of its lifecycle.
6. `PageLayoutFilter` — `ReportGroupAvailableFieldID` + `CriteriaType1/2` + `CriteriaValue1/2` +
   `IsListFilter` + `RowOrderBy`/`ColumnOrderBy`/`ShowSubtotal` — is the **row-filter and pivot**
   table for lists and reports. Conditional *field* rules are stored separately, as JSON.

## Open questions

Ranked by how much each blocks the ASG Edge+ rebuild. Questions already owned by
[conditional-fields.md](conditional-fields.md) and
[forms-vs-pages-vs-layouts.md](forms-vs-pages-vs-layouts.md) are not repeated here; these are the
schema-side gaps.

1. **Which column actually persists `json.conditionalFieldsConfig`?** The dialog posts it; the
   destination is not observed. `PageLayoutField.DisplayOptionJSON` is the strongest candidate — it
   is an optional per-placement JSON textarea, and a `subPage_<id>` target *is* a `PageLayoutField`
   row whose `SubPageLayoutID` holds that id. `PageLayoutField.JSONConfigText` and
   `PageLayout.JSONConfigText` are the alternatives. Settling this settles migration.
2. **Is `PageLayoutFilter` the `showInList=1` surface?** Its `IsListFilter` flag and the layout
   builder's `showInList=1` parameter for `layoutMode` `list`/`budget` describe the same
   distinction from two directions. If so, list-layout conditions are normalised rows while
   edit-layout conditions are a JSON blob — an odd asymmetry worth confirming before copying either.
3. **Where is per-placement required-ness stored?** `PageLayoutField` has no `IsRequired` column,
   yet the vendor states the flag is set "from the Manage Page Layouts section … or the Manage Forms
   page" and is read-only on the field catalog (`_xlsx_feature_list.txt` line 938). The
   `Show and Require` action makes *conditional* required-ness clear; *unconditional* per-placement
   required-ness is not accounted for.
4. **What is the complete `PageLayoutType` and `OutputType` vocabulary?** Five `mode` values and
   three `layoutMode` values are observed; the schema implies at least nine more layout kinds. This
   sets the scope of PAGE-LAYOUTS-01. `PageLayout.EquivalentPLTypes` would enumerate them.
5. **Does `Program`-level setup-page assignment override `Firm`-level?** 18 `sTYPE_PAGE_LAYOUT`
   columns on `Program` against 11 on `Firm`; only the Firm screen has been seen. Doubles the scope
   of layout assignment if true.
6. **How is a layout's Portfolio/Capital-Program scope stored?** The required chip control is
   observed on the layout edit dialog; no column in either offline artefact holds it. Presumed link
   table.
7. **How are action buttons stored on a layout?** No column declares one, yet Approve Payments,
   Generate Rent, Extend Contracts and the "(Run Report Action)" buttons are placed, reordered and
   deleted exactly like fields.
8. **What does Layout Changes (`ShowLayoutChanges.jsp`) record?** ASG has explicitly asked for an
   explanation of this tool (`_xlsx_feature_list.txt` line 44).
9. **Are layouts versioned at all?** `VersionAdded`/`VersionModified` exist on the *field* registry
   but not on `PageLayout`. Without layout versioning a historical form instance cannot be
   faithfully re-rendered, and Lucernex's only mitigation — `Issue.LastPageLayoutID` — is a single
   most-recent pointer, so it does not reconstruct what each approver saw at each step.
10. **Is there a Global/platform-wide Custom List concept?** None observed; only Firm scope.
