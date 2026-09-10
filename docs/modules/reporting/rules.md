# Reporting — rules

Rules the reporting subsystem enforces, numbered `RPT-R-NNN`. Each carries an evidence label.
**Observed** = seen in a capture or source artefact. **Derived** = computed from observed data.
**Inferred** = domain reasoning, not confirmed. **[BLOCKED]** = the most likely form, pending a
browser check that is named.

## A. What a report is

| # | Rule | Label | Source |
|---|---|---|---|
| RPT-R-001 | A report is not a distinct record type. It is a `PageLayout` row with `IsReport = true`. There is no `Report` table in the schema. | Derived (absence across 223 objects) + Observed (the column) | `_lucernex_objects_summary.txt`; `all-fields.csv` |
| RPT-R-002 | A report is **run**, not viewed: `PageLayout.LastRunBy` and `LastRunDate` record the most recent execution on the definition row itself. | Observed (columns) + Inferred (meaning) | `all-fields.csv` |
| RPT-R-003 | A report's output format is a required property of the definition (`OutputType`), not chosen at run time. | Observed | `all-fields.csv` |
| RPT-R-004 | A report declares which entities it may be run against (`EntitySelectionFilter`) and which filters the user is offered at run time (`RunModeFilters`). Both required. | Observed (columns) + Inferred (meaning) | `all-fields.csv` |
| RPT-R-005 | Reports are **Global** (platform standard, `IsGlobalReport = true`) or tenant/personal. `OwnedByMemberID` gives a report a personal owner. | Observed (columns) | `all-fields.csv` |
| RPT-R-006 | A **dashboard tile** is a `PageLayout` row with `IsDashboardReport = true`, administered by Manage Dashboard Reports (`/en/reports/ManageDashboardModules.jsp`). | Observed (column + route) + Inferred (the binding) | `all-fields.csv`; [004](../../admin/004-company-administration.md) |
| RPT-R-007 | A report can appear as its own navigation entry (`IsMenuLink`) and can be placed in the menu tree by `HierarchyName`, exactly like a page. | Observed (columns) | `all-fields.csv` |
| RPT-R-008 | A report can be redirected wholesale to a system URL (`PageLayout.URL`), discarding its configured columns. Same escape hatch as any layout (LAY-R-106). | Observed | [008](../../admin/008-manage-page-layouts.md#the-edit-dialog--full-metadata-surface) |
| RPT-R-009 | A layout can host **report-triggering action buttons**, a distinct button kind labelled "**(Run Report Action)**" — observed as `Expense Report` and `Check History` on the ASG Contract Payments edit layout. Reports are therefore invocable from inside an ordinary record page. | Observed | [008](../../admin/008-manage-page-layouts.md#a-list-type-record-can-carry-both-an-edit-layout-and-a-list-layout) |

## B. Report columns and the field registry

| # | Rule | Label | Source |
|---|---|---|---|
| RPT-R-010 | Report columns are drawn from **the same field registry as forms** — `ReportGroupAvailableField`, whose FK type Lucernex names `Report/Form Field ID`. There is no separate report-field catalog. | Observed | [report-field-registry.md](report-field-registry.md) |
| RPT-R-011 | A field carries **two** labels: `DefaultLabel` ("Label") and `UILabel` ("**Report Field Label**"). A field may therefore present differently on a form than as a report column header. | Observed (columns and their captions) + Inferred (which surface uses which) | `all-fields.csv` |
| RPT-R-012 | A report column is a `PageLayoutField` row; grid geometry uses the `View*` coordinate set (`ViewRowPosition`, `ViewColumnPosition`, `ViewFieldWidth`, `ViewFieldHeight`, `HeaderColumnPosition`). | Inferred (high) | `all-fields.csv` |
| RPT-R-013 | A column can be **searchable but hidden from the grid** — a third visibility state distinct from shown and removed. | Observed | [008](../../admin/008-manage-page-layouts.md#a-list-type-record-can-carry-both-an-edit-layout-and-a-list-layout) |
| RPT-R-014 | A report may include fields from **related** tables reached by declared FKs, disambiguated by `FieldContext`. | Observed (Related Fields) + Inferred (the column's role) | [009](../../admin/009-related-fields-and-data-model.md); `all-fields.csv` |
| RPT-R-015 | A report may include fields from a tenant's **Custom Lists**, which are ordinary registry leaves under the owning table's `Custom Lists` subgroup. | Observed | [008](../../admin/008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists) |
| RPT-R-016 | Every registry field carries a **Value Javascript** hook, so a report column's value can be scripted rather than read. | Observed | [005](../../admin/005-manage-data-fields.md#per-row-actions) |
| RPT-R-017 | The registry marks computed fields with `IsFunctional` and carries a `Definition` textarea for the computation. `View Object Model` exposes a `Functional Field?` column and `Math`/`Computed` filter radios. | Observed | `all-fields.csv`; [009](../../admin/009-related-fields-and-data-model.md#visible-layout-and-controls) |

## C. Filters, grouping and totals

| # | Rule | Label | Source |
|---|---|---|---|
| RPT-R-020 | Report and list filters are `PageLayoutFilter` rows: `ReportGroupAvailableFieldID` (required) + two `CriteriaType`/`CriteriaValue` pairs, discriminated by a required `IsListFilter` boolean. **This is not the conditional-field store** — conditional field rules are persisted as a JSON document per target, per live capture ([conditional-fields.md](../layouts-and-forms/conditional-fields.md#storage-format)). | Observed (columns) + Inferred (role) | `all-fields.csv` |
| RPT-R-021 | A filter row names **one** field (`ReportGroupAvailableFieldID`, required) and carries **two** operator/value pairs — a two-clause predicate on that field, e.g. a `between`. | Observed (columns) + Inferred (the pairing) | `all-fields.csv` |
| RPT-R-022 | Multiple filter rows chain through `ExtendedGroupFilterID` (self-FK). Whether the chain is AND, OR, or an explicit group is undetermined. | Observed (column) + Open (semantics) | `all-fields.csv` |
| RPT-R-023 | The same row that filters also **groups**: `RowOrderBy` and `ColumnOrderBy` give a field a position on each axis. Reporting in Lucernex is pivot-shaped, not flat-list-shaped. | Observed (columns) + Inferred (semantics) | `all-fields.csv` |
| RPT-R-024 | `ShowSubtotal` emits a subtotal at a grouping break; `ShowLabel` renders the grouping field's label there. | Observed (columns) + Inferred | `all-fields.csv` |
| RPT-R-025 | Report currency is a property of the definition (`PageLayout.CodeCurrencyTypeID`), not of the run. | Observed (column) | `all-fields.csv` |
| RPT-R-026 | **[BLOCKED]** The `CriteriaType` operator codebook is a small integer enum whose members are unobservable offline. *Check: distinct `CriteriaType1`/`CriteriaType2` values via GraphQL Explorer.* | Open | — |

## D. Purpose-built report types

**Scope note.** Budget View and the Bid/Cost report families are out of scope (Cost Management and
Budgeting excluded). Rules for them are removed; `RPT-R-034` and `RPT-R-035` are retired and not
reused.

| # | Rule | Label | Source |
|---|---|---|---|
| RPT-R-030 | A **Comparison Report** is a first-class record (`ComparisonReport`) that still delegates its rendering to a `PageLayout` (`PageLayoutID`, **required**). Even the bespoke report types run on the generic layout engine. | Observed | `_lucernex_objects_summary.txt`; `all-fields.csv` |
| RPT-R-031 | A Comparison Report's cells live in `ComparisonItem`, one row per scenario column, carrying `ScenarioName`, `ScenarioDate`, `ExpenseGroup`, `Assumptions`, `ComputedValue` and a serialised **`XmlData`** payload. | Observed | `_lucernex_objects_summary.txt` |
| RPT-R-032 | **Demographic Reports** are the only report family with an explicit asynchronous execution record: `DemographicResults` carries `TimeInitiated`, `TimeFinished`, a status code, a **third-party vendor** code, and a `DocumentID` for the produced artefact. | Observed | `_lucernex_objects_summary.txt` |
| RPT-R-033 | A Demographic Report's scope is a **trade area** defined by radius or drive time (`DemographicStudyArea.AreaRadius`, `.AreaDriveTimeInMinutes`, `.CodeRadiusUnitID`) — a site-selection feature, not a lease-accounting one. | Observed | `_lucernex_objects_summary.txt` |
| RPT-R-036 | `Virtual*` objects are **computed projections exposed as tables** — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForecastPeriod` (20) and others — so a report can select from a calculated period series with no materialisation step. | Derived (naming pattern, 12 objects) + Inferred (non-persistence) | `_lucernex_objects_summary.txt` |

## E. Audit reporting

| # | Rule | Label | Source |
|---|---|---|---|
| RPT-R-040 | Field-level change audit is stored in `AuditColumn`, with `EntityName`, `CodeSQLTableID`, `ObjectID`, `FieldName`, `AuditAction`, `OldValue`, `NewValue` and the actor/timestamp. | Observed | `all-fields.csv` |
| RPT-R-041 | Audit entries are **filed under the field registry's group tree** — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report. | Observed (columns) + Derived (11-for-11 match with the observed Audit Log dialog) | `all-fields.csv`; [007](../../admin/007-firm-and-client-drop-downs.md#value-level-editor--scoping-and-audit-log) |
| RPT-R-042 | Login, lockout and impersonation events are audited separately in `MemberAudit`, with `SrcIP` and `UserAgent`. | Observed | `_lucernex_objects_summary.txt` |
| RPT-R-043 | The Audit Log dialog is a **generic viewer** over `AuditColumn`, reachable from an individual record's editor — not only from a central Audit Reports screen. | Derived | [007](../../admin/007-firm-and-client-drop-downs.md#value-level-editor--scoping-and-audit-log) |

## F. Security

| # | Rule | Label | Source |
|---|---|---|---|
| RPT-R-050 | Report access is granted per **user class** through `UserClassSecurity.PageLayoutID`, alongside grants on fields (`ReportGroupAvailableFieldID`), field groups (`ReportGroupDataID`) and dashboard components. | Observed | `all-fields.csv` |
| RPT-R-051 | Dashboard tiles are secured **by title string** (`UserClassSecurity.DashboardComponentTitle`), not by record id. Renaming a tile therefore breaks its grants. | Observed (column) + Inferred (consequence) | `all-fields.csv` |
| RPT-R-052 | Granting on a registry **group** node means report-field permissions inherit down the catalog tree, not per-field only. | Inferred (high) | `all-fields.csv` |
| RPT-R-053 | **[BLOCKED]** Whether Portfolio/Capital-Program scoping filters report *rows* at the query level or only hides values in the UI is unresolved — the same question [007](../../admin/007-firm-and-client-drop-downs.md) raises for dropdown values. *Check: run a report as a portfolio-restricted user.* | Open | [007](../../admin/007-firm-and-client-drop-downs.md) |

## G. Bulk data movement

| # | Rule | Label | Source |
|---|---|---|---|
| RPT-R-060 | The field catalog itself is exportable and importable as a spreadsheet, scope-aware: `DocumentDownload?type=RGAFSpreadsheet&readOnly=true&isGlobal={true\|false}`. | Observed | [005](../../admin/005-manage-data-fields.md#page-level-controls-and-handlers) |
| RPT-R-061 | An exported catalog spreadsheet is **single-use**: "Once a spreadsheet is imported the same spreadsheet cannot be used again. You would have to create a new spreadsheet using 'Export Data Fields' button." This implies a nonce or version stamp inside the workbook. | Observed (instruction text) + Inferred (mechanism) | [005](../../admin/005-manage-data-fields.md#firm-only-instruction-block) |
| RPT-R-062 | The bulk-change instruction block is shown in **Firm** scope but not in **Global** scope. Reason unknown. | Observed | [005](../../admin/005-manage-data-fields.md#firm-only-instruction-block) |
| RPT-R-063 | ASG requires a **report-to-import** round trip (export a report to Excel, edit, re-import to update records), priority Critical. Lucernex's catalog export/import is field *metadata* only; no equivalent for report *data* was found. | Observed (requirement) + Derived (absence) | `_xlsx_feature_list.txt` line 244 |

## H. Requirements ASG has already stated

These are not Lucernex rules — they are ASG Edge+ obligations recorded in
`_xlsx_feature_list.txt`, listed here because they constrain the reporting design.

| # | Requirement | Priority | Line |
|---|---|---|---:|
| RPT-R-070 | Restrict edit access to standard reports (e.g. ASC 842) to prevent breakage, while allowing **runtime filters** to view specific data | **Blocker** | 242 |
| RPT-R-071 | "**Save As**" personal reports — a user copy that does not affect the global standard | **Critical** | 243 |
| RPT-R-072 | **Report-to-import** workflow — export to Excel, modify, re-import to update the system | **Critical** | 244 |
| RPT-R-073 | **Scheduled & external delivery** — email to recipients including non-users, or encrypted SFTP | Major | 245 |
| RPT-R-074 | **Multi-tenancy / global management** — a Global Admin view; today an admin logs into 21 instances separately | Critical | 246, 248 |
| RPT-R-075 | **Job log visibility** — an at-a-glance status board for scheduled jobs, not a click-away list; blank reports are being sent unnoticed | — | 247 |
| RPT-R-076 | **Readable audit logs** — "Audit tools are just raw links. User has to go look for logs manually in the table and infer on its own." ASG explicitly does **not** use Generate Enterprise Report File | — | 241 |
| RPT-R-077 | **Bulk action confirmation** — preview changes before executing a bulk import, with rollback visibility | Critical | 250 |

RPT-R-070 and RPT-R-071 map directly onto columns Lucernex already has
(`IsGlobalReport`, `RunModeFilters`, `OwnedByMemberID`), so the requirement is a UX and permission
gap rather than a data-model gap. RPT-R-073 has **no** Lucernex counterpart to migrate from.
