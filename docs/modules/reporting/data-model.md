# Reporting — data model

**Stated up front.** Lucernex has no `Report` table. A report **is** a `PageLayout` row with
`IsReport = true`, run-tracked by `LastRunBy` / `LastRunDate`, its output format set by
`OutputType`, its runtime parameters declared by `RunModeFilters` and `EntitySelectionFilter`, its
columns held as `PageLayoutField` rows, and its filters and groupings held as `PageLayoutFilter`
rows with `IsListFilter = true`. Alongside that generic engine sit two in-scope **purpose-built
report types** with their own tables — Comparison Report and the `Virtual*` computed-projection
family — one **audit reporting** table, `AuditColumn`, and one family documented only to be ruled
out, Demographics.

**Scope note.** Cost Management and Budgeting are out of scope for ASG Edge+. `BudgetView`,
`BudgetOptionTemplate`, `ProFormaBudget`, `BudgetTemplateAudit`, `VirtualTemplateBudget(Option)`
and the Bid/Cost families are therefore **not analysed here**. Two budget-adjacent citations are
retained deliberately, and only as evidence about something else: `BudgetColumnType.ReportGroupAvailableFieldID`
(evidence for the shared field registry — see [report-field-registry.md](report-field-registry.md))
and `BudgetColumnType`'s `IsValidFor*` boolean family (evidence for the general
"what entities can this attach to" pattern).

**Boundary warning — "payment" spans both sides of the scope line.** Cost Management is the
*capital-project* cost stack (Budget, BudgetColumn, PurchaseOrder, ChangeOrder, PayApp, BidPackage,
CostTrackingTemplate). **Lease and rent payments are a different module and are in scope**:
`PaymentTransaction`, `PaymentReceipt`, `Percentage Rent`, the `ASG Contract Payments` layout
(`PageLayoutID=96214`), the `Approve Payments` / `Generate Rent` action buttons, and the
`Rent Payment Review/Approval` workflow all stay. A keyword sweep for "payment" or "budget" across
this corpus **will strip live, ASG-critical, in-scope material**. Boundary established in
[modules/workflow/](../workflow/README.md).

## The generic engine

| Table | Role | Fields | Detail |
|---|---|---:|---|
| `PageLayout` | The report definition | 42 | [layouts-and-forms/data-model.md](../layouts-and-forms/data-model.md#pagelayout--42-fields) |
| `PageLayoutField` | Report columns and their geometry | 27 | same |
| `PageLayoutFilter` | Filters, groupings, subtotals | 16 | same |
| `ReportGroupAvailableField` | The field catalog the columns draw from | 27 | [report-field-registry.md](report-field-registry.md) |
| `ReportGroupData` | The catalog's group tree | 5 | same |

### The columns that make a `PageLayout` a report

| Column | Type | Reqd | Reporting role |
|---|---|:---:|---|
| `IsReport` | boolean | | This layout is run, not viewed |
| `IsDashboardReport` | boolean | | Renders as a dashboard tile (Manage Dashboard Reports) |
| `IsGlobalReport` | boolean | | Platform-shipped standard report vs tenant-authored |
| `OutputType` | text | **Y** | Render target — screen, PDF, XLSX, CSV (value set unobserved) |
| `RunModeFilters` | number | **Y** | Which filters the user is offered at run time |
| `EntitySelectionFilter` | number | **Y** | Which entities the report may be run against |
| `LastRunBy` | `sTYPE_MEMBER` | | Who last ran it |
| `LastRunDate` | `sTYPE_TIME` | | When |
| `OwnedByMemberID` | `sTYPE_MEMBER` | | Personal ownership — the storage for a "Save As my report" copy |
| `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | | Reporting currency |
| `URL` | textarea | | Redirect to a system report page instead of rendering the configured one |
| `IsMenuLink` | boolean | | Report appears as its own navigation entry |

**Observed** columns (`docs/data-fields/all-fields.csv`). The *reporting* interpretation of
`LastRunBy`/`LastRunDate` is **Inferred**, but it is hard to read them any other way: a screen
layout is not run.

`OwnedByMemberID` deserves a note because it maps directly onto an ASG requirement. The feature
workbook records the pain point "**'Save As' Personal Reports** — Users should be able to 'Save As'
a standard report to create a personal version without affecting the global standard", priority
**Critical** (`_xlsx_feature_list.txt` line 243). `PageLayout` already has both halves of that:
`IsGlobalReport` for the standard and `OwnedByMemberID` for the personal copy. **Observed** columns,
**Inferred** that this is what Lucernex uses them for.

### Report filters — `PageLayoutFilter` with `IsListFilter = true`

| Column | Reporting meaning |
|---|---|
| `ReportGroupAvailableFieldID` (**required**) | The field being filtered or grouped |
| `CriteriaType1` / `CriteriaValue1` | First clause: operator + value |
| `CriteriaType2` / `CriteriaValue2` | Second clause — a `between` on the same field |
| `ExtendedGroupFilterID` (self-FK) | Chains rows into a compound predicate |
| `RowOrderBy` | Row-axis grouping/sort position |
| `ColumnOrderBy` | Column-axis grouping/sort position |
| `ShowLabel` | Render this field's label at the grouping break |
| `ShowSubtotal` | Emit a subtotal at this grouping break |
| `FieldContext` | Which join path the field arrived by |
| `AccessorName` | Denormalised field name |

`RowOrderBy` + `ColumnOrderBy` + `ShowSubtotal` on the same row as the filter criteria is a
**pivot-table shape**: one table describing both what to restrict and how to break and total the
result. **Observed** columns; **Inferred** semantics, high confidence.

`IsListFilter` remains unexplained. It is **not** the conditional-field discriminator — live
capture shows conditional field rules are persisted as a JSON document per target
([conditional-fields.md](../layouts-and-forms/conditional-fields.md#storage-format)), not as rows
here. The likelier reading is that it separates *list-layout* filters from *report run-mode*
filters, which would pair it with the layout builder's `showInList=1` parameter. **Open question**,
tracked in [layouts-and-forms/rules.md](../layouts-and-forms/rules.md) as `LAY-R-143`.

### How list and report data is served

**Observed** ([conditional-fields.md](../layouts-and-forms/conditional-fields.md#the-driver-field-catalog--rules-cross-entity-boundaries)):
the layout builder's driver grid is populated from
`/servlet/BOList?…&BOType=ConditionFilterList` — a **generic list servlet with a `BOType`
discriminator**, not a purpose-built endpoint.

That pattern matters for reporting because it is the same shape the whole product uses: one servlet,
one discriminator, many list payloads — matching the `getLayoutNames` and `JSONDataRequest?reqType=…`
servlets already observed in [005](../../admin/005-manage-data-fields.md#network-evidence) and
[004](../../admin/004-company-administration.md#network-evidence). **Inferred**, moderate
confidence: report and list rendering very likely go through the same `BOList`-style servlet with a
different `BOType`, which would make it the natural place to look for how a report actually
executes — something no table in the schema records.

## Purpose-built report types

### `ComparisonReport` — 4 fields

| Field | Type |
|---|---|
| `ComparisonReportID` | Number (PK) |
| `PageLayoutID` | `sTYPE_PAGE_LAYOUT` (**required**) |
| `ProjectEntityID` | Entity ID |
| `BOMapClientRecordID` | Text |

A four-column table that is almost entirely a pointer: one entity, one layout. The report's actual
*content* lives in `ComparisonItem`.

### `ComparisonItem` — 9 fields

| Field | Type | Note |
|---|---|---|
| `ComparisonItemID` | Number | PK |
| `ProjectEntityID` | Entity ID | |
| `ScenarioName`, `ScenarioDate` | Text, Date | One column of the comparison = one scenario |
| `ExpenseGroup` | Text | Row grouping |
| `Assumptions` | Text | |
| `ComputedValue` | Text | The computed cell value |
| `XmlData` | Text | **Serialised payload** — the comparison's working data |
| `BOMapClientRecordID` | Text | |

`XmlData` is the interesting column: this report type stores a serialised blob rather than
normalised rows. **Observed.** Anyone migrating comparison reports will have to parse it.

Cross-reference: the field registry's `Summary Information` group contains a `Comparison Report`
subgroup ([009](../../admin/009-related-fields-and-data-model.md#data-displayed--the-related-fields-inventory-for-contract)),
so comparison-report fields are placeable on ordinary layouts too. **Observed.**

### Demographics — four tables

| Table | Fields | Role |
|---|---:|---|
| `DemographicReport` | 10 | The report definition: `DemographicReportName`, `CodeMarketAreaID`, `CodeMarketTypeID`, `TradeArea`, `PrototypeID`, `RegionID` |
| `DemographicStudyArea` | 6 | The geographic scope: `AreaRadius`, `AreaDriveTimeInMinutes`, `CodeRadiusUnitID` — radius-or-drive-time trade areas |
| `DemographicFact` | 10 | The measures: `CodeMarketDemographicsID`, `Weighting`, ordered via `ParentID`/`PreviousID`/`ComputedSequenceNumber` |
| `DemographicResults` | 12 | An **execution**: `TimeInitiated`, `TimeFinished`, `CodeResultsStatusID`, `CodeThirdPartyVendorID`, `DocumentID`, `TempLocation` |

**Observed** (`_lucernex_objects_summary.txt`). This is the only reporting family in the schema with
an explicit **asynchronous execution record**: initiated/finished timestamps, a status code, a
third-party vendor code, and a `DocumentID` holding the produced artefact. It is a site-selection
feature (drive-time trade areas, market demographics from an external data vendor) and is **almost
certainly out of scope for ASG Edge+**, which is lease accounting and contract management. Noted
for completeness, and because its shape is the right pattern to copy for *scheduled* reporting.

### `Virtual*` — computed projections exposed as tables

**The most reusable idea in Lucernex's reporting model.** The `Virtual*` prefix marks
**computed, non-persisted projections** that the object model presents *as if they were tables*, so
a report can select from a calculated period series with no materialisation step.

| Object | Fields | What it projects |
|---|---:|---|
| `VirtualSalesPeriod` | 66 | Sales periods for percentage-rent calculation |
| `VirtualUsagePeriod` | 66 | Usage periods for use-based rent |
| `VirtualPercentageRentPeriod` | 38 | Percentage-rent period expansion |
| `VirtualUseBasedRentPeriod` | 23 | Use-based rent period expansion |
| `VirtualPRAccrualPeriod` | 20 | Percentage-rent accrual periods |
| `VirtualExpenseForecastPeriod` | 20 | Expense forecast periods |
| `VirtualPRPAggregate` | 16 | Percentage-rent aggregation |
| `VirtualUBRPAggregate` | 14 | Use-based rent aggregation |
| `VirtualExpAccrualForecastPeriod` | 13 | Expense accrual forecast periods |

**Observed** names and counts; **Derived** that the prefix marks a family (12 `Virtual*` objects
in total); **Inferred** that they are non-persisted.

Four further `VirtualTemplate*` objects exist and are **out of scope** — two of them are budget
projections. Noted only so the family count reconciles.

Why this matters for a lease-accounting rebuild: a report over an ASC 842 or IFRS 16 schedule
should read the *calculated* series, not a stale snapshot. Lucernex achieves that by making the
calculation queryable. See [asg-edgeplus-mapping.md](asg-edgeplus-mapping.md#what-must-be-built).

## Audit reporting — `AuditColumn`

| Field | Type | Audit Log dialog column ([007](../../admin/007-firm-and-client-drop-downs.md#value-level-editor--scoping-and-audit-log)) |
|---|---|---|
| `CreatedByID` | Member ID | Member Name |
| `CreatedDate` | Time | Date/Time |
| `GroupID` | `sTYPE_REPORT_GROUP_DATA` | Group Name |
| `SubGroupID` | `sTYPE_REPORT_GROUP_DATA` | Sub-Group |
| `EntityName` | Text | Entity |
| `CodeSQLTableID` | Dropdown (SQL Table Code) | Table |
| `ObjectID` | Number | Item ID |
| `FieldName` | Text | Field |
| `AuditAction` | Text | Action |
| `OldValue` | Text | Old Value |
| `NewValue` | Text | New Value |
| `AccessorName`, `ScriptName`, `ProjectEntityID` | Text, Text, Entity ID | (not surfaced in the dialog) |

An **11-for-11 match** between the schema and the observed dialog. **Derived.** Two things follow:
the Audit Log dialog seen on a Custom Drop Down value is a generic viewer over `AuditColumn`, and
audit entries are **filed under the Data Fields catalog's own group tree** (`GroupID`,
`SubGroupID` both point at `ReportGroupData`), which makes the field registry the organising
taxonomy for audit as well as for forms and reports.

Sibling audit tables, all **Observed**: `MemberAudit` (12 — logins, lockouts, impersonation,
`SrcIP`, `UserAgent`), `TemplateAudit` (18 — template *application* events, not layout changes),
`FolderTemplateAudit` and `TaskTemplateAudit` (18 each), and `AuditTable` (1 field exposed —
effectively empty in the object model). A fourth sibling of the same shape exists in the budget
domain and is out of scope.

## Reporting-adjacent tables

| Table | Fields | Relevance |
|---|---:|---|
| `Document` | 23 | Report output artefacts (`DemographicResults.DocumentID`) |
| `EMailSentLog` / `EMailReceivedLog` | 1 / 15 | Email Log admin tool; scheduled-report delivery evidence would live here |
| `GlobalProperty` | 4 | Feature flags — the "Manage Features / Global Properties" tool |
| `ScratchPad` | 1 | "Manage Scratch Pads" tool |
| `Security` / `UserClassSecurity` | 21 / 21 | Report and dashboard-tile access grants |

`UserClassSecurity.DashboardComponentTitle` (text) is the only schema evidence of how dashboard
tiles are secured — by **title string**, not by id. **Observed**, and worth not copying.

## What is missing from the schema

| Expected | Present? | Consequence |
|---|:---:|---|
| A report **schedule** table | **No** | ASG's "Scheduled & External Delivery" requirement (`_xlsx_feature_list.txt` line 245) has no Lucernex counterpart to migrate from. Scheduling is presumably in the job subsystem behind `JobLogEdit.jsp` |
| A report **run history** table | **No** | Only `PageLayout.LastRunBy`/`LastRunDate` — a single most-recent stamp, not a history. The **Report Log** admin tool (`JobLogEdit.jsp?type=reportlog`) is a *job log* view, not a report-execution table |
| A report **subscription / recipient** table | **No** | Same gap |
| A **chart / visualisation** definition | **No** | No chart, series, or axis table anywhere in the 223 objects. Dashboard tiles are `PageLayout` rows; how a tile renders a chart is undetermined |
| A **saved query / ad-hoc query** table | **No** | Reporting is layout-driven only; there is no free-form query object |
| Layout tables (`PageLayout*`) in the business object model | **No** | Presentation metadata is deliberately outside the 223-object BO model — see [conditional-fields.md § 2.1](../layouts-and-forms/data-model.md#table-inventory) |

The chart gap is the most notable. `_lucernex_objects_summary.txt` contains no object matching
`chart`, `graph`, `series`, `axis`, `widget`, `tile` or `visual`. **Derived.** Either dashboard
tiles are text/grid only, or chart configuration lives in `PageLayout.JSONConfigText`. **Open
question**, and one the lead can settle by opening Manage Dashboard Reports.

Independently corroborated from the API side: the GraphQL schema has **490 types, 433 of them
objects, and none of them is a `PageLayout`, a report, a chart, or a rule**
([graphql-api.md](../../data-model/graphql-api.md), **Observed**). 617 queries against 3 mutations,
all over business objects. Presentation and reporting metadata is not exposed over the data API at
all — which answers, negatively, the question of whether a Lucernex→ASG Edge+ report migration can
be driven through GraphQL. It cannot; Export Configuration is the route.
