# Reporting → ASG Edge+

**Stated up front.** ASG Edge+ has five reporting work areas already planned — **27 Reporting
Engine, 28 Report Management, 29 Report Creation, 30 Report Modification, 31 Report Integrations**
(`_xlsx_feature_list.txt`, `ASG Edge Plus Modules` sheet, rows 126-130, all marked *"Correct"* by
ASG on 01.06.26), plus **Reports Migration** as a distinct migration work area and **BRD 19
Reporting Capability** as an approved, submitted BRD. The Lucernex finding that reshapes all of
this: **a report is a layout**. If ASG Edge+ builds a reporting engine separate from its layout
engine, it will build the same field-placement, filtering and permission machinery twice and then
have to keep the two in sync.

The recommendation is not "build reports as layouts because Lucernex did". It is: build **one
field registry** and **one placement + filter model**, then let a report be a layout whose type is
`REPORT` and whose output is a file rather than a screen. That is the smallest design that satisfies
both PAGE-LAYOUTS-01 and work areas 27-31.

## What exists in ASG Edge+ today

| Artefact | Status |
|---|---|
| Work areas 27-31 (Reporting Engine / Management / Creation / Modification / Integrations) | Planned, ASG-confirmed, not built |
| **BRD 19 — Reporting Capability** | Submitted, approved (`19 Reporting Capability BRD.docx`) |
| **BRD 8 — Dashboards & Home Experience** | Submitted, approved |
| Reports Migration | Named as a migration work area |
| Reporting & Analytics pain points | Eight recorded, one **Blocker** and four **Critical** — see [rules.md § H](rules.md#h-requirements-asg-has-already-stated) |
| Data Fields / Masters (MDM-01) | The live thread; the field registry this depends on |
| PAGE-LAYOUTS-01 | The layout engine this depends on |

**Read this before designing anything:** the reporting engine cannot be specified before the field
registry is settled, because a report column *is* a registry field. MDM-01 and PAGE-LAYOUTS-01 are
upstream of work areas 27-31, not parallel to them.

## Concept mapping

| Lucernex | ASG Edge+ | Gap |
|---|---|---|
| `PageLayout` with `IsReport = true` | `Layout` with `layout_type = REPORT` | Build once, share with PAGE-LAYOUTS-01 |
| `PageLayout.IsDashboardReport` | Dashboard tile | BRD 8 |
| `PageLayout.IsGlobalReport` | Platform standard report | Maps onto the Hub/Spoke split |
| `PageLayout.OwnedByMemberID` | Personal "Save As" copy | **RPT-R-071, Critical** — the column already exists in Lucernex; the gap is UX and permissions |
| `PageLayout.RunModeFilters` | Runtime filters on a locked standard report | **RPT-R-070, Blocker** |
| `PageLayout.OutputType` | Output format | Build |
| `PageLayout.LastRunBy` / `LastRunDate` | Run tracking | **Insufficient** — build a real run-history table |
| `PageLayoutField` (`View*` coordinates) | Report column definition | Shared with layouts |
| `PageLayoutFilter` (`IsListFilter = true`) | Report filter + grouping + subtotal | Build as its own table, separate from field conditions |
| `ReportGroupAvailableField` / `ReportGroupData` | The Data Fields registry | MDM-01 |
| `ComparisonReport` + `ComparisonItem` | Scenario comparison | Likely in scope — lease scenario comparison is core |
| `DemographicReport` family (4 tables) | — | **Deliberately out of scope.** Site-selection/trade-area analytics with a third-party data vendor; not lease accounting |
| Budget/Bid/Cost report families | — | **Out of scope.** Cost Management and Budgeting are excluded |
| `Virtual*` computed projections | Calculated period series exposed as queryable | **Worth copying as a pattern** — see below |
| `AuditColumn` | Field-change audit | Blocked on the ADR superseding **ADR-0020** |
| `UserClassSecurity` | Report and tile permissions | Build; note group-level inheritance |
| Report Log (`JobLogEdit.jsp?type=reportlog`) | Job/report execution monitor | **RPT-R-075** — ASG wants a status board, not a list |
| — (no schedule table exists) | Scheduled + SFTP delivery | **RPT-R-073** — nothing to migrate from; greenfield |
| — (no chart table exists) | Charts and visualisations | **Unknown whether Lucernex has any** |

## What must be built

### 1. Report = Layout, with a run

Reuse the `Layout` / `layout_field` model in
[layouts-and-forms/asg-edgeplus-mapping.md](../layouts-and-forms/asg-edgeplus-mapping.md#what-must-be-built).
A report adds three things Lucernex handles poorly or not at all:

```
report_definition                      -- extends layout where layout_type = REPORT
  layout_id            FK -> layout
  output_formats       set(SCREEN, PDF, XLSX, CSV)   -- Lucernex has one required OutputType
  runtime_filter_ids   FK[] -> report_filter          -- which filters the user may set at run time
  locked               bool                            -- RPT-R-070: standard reports are not editable
  is_standard          bool                            -- IsGlobalReport
  forked_from_id, forked_from_version                  -- "Save As" lineage; Lucernex has none

report_run                             -- Lucernex has NO equivalent; it has one timestamp
  id, report_definition_id, layout_version
  requested_by, requested_at, started_at, finished_at
  status               enum(QUEUED, RUNNING, SUCCEEDED, FAILED, EMPTY)
  parameter_values     jsonb
  row_count                                            -- RPT-R-075: "blank reports still sent"
  output_document_id
  error

report_schedule                        -- Lucernex has NO equivalent
  id, report_definition_id
  cron, timezone, active
  parameter_values     jsonb
  delivery             enum(EMAIL, SFTP)
  recipients           jsonb                           -- including non-users, per RPT-R-073
  suppress_if_empty    bool                            -- directly answers "blank reports still sent"
```

`row_count` and `suppress_if_empty` are small columns that resolve a named ASG operational
complaint. `layout_version` on `report_run` is what makes a historical run reproducible — Lucernex
does not version layouts at all (LAY-R-202), so a Lucernex report run cannot be faithfully
re-rendered after its definition changes.

### 2. Filters and grouping, separate from field conditions

Lucernex packs both into `PageLayoutFilter` and distinguishes them with `IsListFilter`. Split them.
The report side needs:

```
report_filter
  id, report_definition_id
  predicate_id         FK -> layout_predicate   -- the shared boolean tree
  is_runtime           bool                      -- user may override at run time
  runtime_label
report_grouping
  id, report_definition_id
  field_id             FK -> field_registry
  axis                 enum(ROW, COLUMN)         -- RowOrderBy / ColumnOrderBy
  sort_order, direction
  show_label, show_subtotal
  aggregate            enum(SUM, COUNT, AVG, MIN, MAX, NONE)
```

Lucernex's `ShowSubtotal` is a boolean with no aggregate selector, which means the aggregate is
implied by the field's type. Make it explicit. And note `axis` — Lucernex reporting is pivot-shaped
(`RowOrderBy` **and** `ColumnOrderBy` on the same row); a flat-list report engine will not reproduce
existing ASG reports.

### 3. Financial correctness in the report layer

Constitution §4.4 forbids `double` in financial code. That applies to the reporting engine too, and
it is easy to lose: aggregation, subtotalling and currency conversion all sit in the report path.

| Requirement | Why |
|---|---|
| `BigDecimal` throughout aggregation and subtotalling | Constitution §4.4 |
| Report currency is a property of the definition (`PageLayout.CodeCurrencyTypeID`, RPT-R-025), and conversion must record the rate and rate date used | A report re-run months later must not silently re-convert at today's rate |
| Rounding policy stated per report, applied once at presentation, never mid-aggregation | Subtotals that do not sum to the total are the classic finance bug |

Lucernex gives no evidence of recording the exchange rate used in a report run — `ExchangeRate` is a
separate table and `PageLayout` stores only a currency type. **Derived** (absence). Do better.

### 4. Charts — decide, do not inherit

There is **no chart, series, axis, widget or visualisation table anywhere in the 223-object
schema** (**Derived**, exhaustive grep of `_lucernex_objects_summary.txt`). Either Lucernex
dashboard tiles are grid/text only, or chart configuration hides in `PageLayout.JSONConfigText`.

This is a decision ASG Edge+ has to make from BRD 8 rather than from Lucernex parity. If charts are
in scope, model them explicitly — chart type, series bindings to registry fields, axis scales — and
do not follow Lucernex's precedent of securing dashboard components **by title string**
(RPT-R-051), which breaks every grant on a rename.

### 5. Copy the `Virtual*` idea

Lucernex exposes computed period series — `VirtualSalesPeriod` (66 fields),
`VirtualPercentageRentPeriod` (38), `VirtualUsagePeriod` (66), `VirtualExpenseForecastPeriod` (20),
`VirtualPRAccrualPeriod` (20) and seven more — **as if they were tables**, so a report can select a
calculated rent or sales schedule without a materialisation step. **Derived** from the naming
pattern; **Inferred** that they are non-persisted.

For a lease-accounting product this is the right shape: a report over an IFRS 16 / ASC 842 schedule
should read the calculated series, not a stale snapshot. In ASG Edge+ terms, the accounting engine
should expose its computed schedules as queryable projections that the reporting engine can treat as
sources. Coordinate with the accounting-engine work.

## What should deliberately differ

| Lucernex | ASG Edge+ | Why |
|---|---|---|
| One `OutputType`, required, on the definition | A set of formats, chosen per run | A report is the same report as a PDF or an XLSX |
| `LastRunBy` / `LastRunDate` only | A `report_run` history table | ASG cannot currently answer "did last night's job run, and was it empty" |
| Dashboard tiles secured by **title string** | Secured by id | A rename silently revokes access |
| No layout versioning | Version layouts; stamp the version on each run | Historical runs must be reproducible for audit |
| No lineage between a Global report and a tenant/personal copy | `forked_from_id` + `forked_from_version` | Required by the Hub/Spoke publish/accept/fork plan and by RPT-R-071 |
| `ComparisonItem.XmlData` — a serialised blob | Normalised rows | An unqueryable blob cannot be reported on or migrated cleanly |
| Per-field **Value Javascript** for computed report values | Declarative expressions, or server-side computed fields | Stored arbitrary JavaScript is unreviewable |
| Report filters and field-display conditions in one table | Two tables | See [conditional-fields.md](../layouts-and-forms/conditional-fields.md) |
| Demographics / trade-area analytics | Out of scope | Not lease accounting |
| Generate Enterprise Report File | Do not build | ASG: *"we do not use"* it |

## Migration implications

The workbook names **Reports Migration**, **Layout Migration** and **Field Migration** as separate
work areas. Given that reports, layouts and forms are all `PageLayout` rows and all draw on
`ReportGroupAvailableField`, these are **one extraction with three projections**, not three
extractions. Sequencing:

1. **Fields first.** Extract `ReportGroupData` + `ReportGroupAvailableField` (Global and Firm).
   Nothing else can be resolved until field ids map.
2. **Layouts second**, all types together — `PageLayout` + `PageLayoutField` + `PageLayoutFilter`.
   Splitting by type means re-reading the same tables three times and inventing three id mappings.
3. **Then project** into Summary Pages, Forms, Reports, Custom Lists per `PageLayoutType`.
4. **Custom Lists** need the `ClientListRGDID` join plus their row data, whose physical storage is
   still undetermined ([report-field-registry.md](report-field-registry.md#custom-lists-are-registry-rows-not-a-separate-feature)).
5. **Export Configuration** (`MessengerExportData.jsp`) is the most likely extraction vehicle; the
   Data Fields spreadsheet export handles step 1 only, and is single-use per export (RPT-R-061).

## Open questions blocking a decision

| # | Question | Blocks | Who can answer |
|---:|---|---|---|
| 1 | Does Lucernex have charts at all, and if so where is a chart configured? | BRD 8 dashboards; whether reporting is grid-only | Browser: Manage Dashboard Reports |
| 2 | Is there **any** report-run history beyond `LastRunBy`/`LastRunDate`? | Whether run history is migration or greenfield | Browser: Report Log |
| 3 | Does Lucernex schedule reports at all, and where is a schedule stored? | RPT-R-073 scope | Browser: Report Log, Email Log, Job Log |
| 4 | What is the `OutputType` value set? | The output-format enum | Browser: GraphQL Explorer |
| 5 | ~~Are `PageLayout*` exposed over GraphQL?~~ **Answered: no** — 490 types, none of them a layout, report, chart or rule ([graphql-api.md](../../data-model/graphql-api.md)). Does the **REST** tier differ? | Whether migration can use the API at all, or must use Export Configuration | Browser: RESTful WebService Docs |
| 6 | Is Portfolio/Capital-Program scoping enforced at the query level or only in the UI? | Multi-tenant report correctness — a SOC 2 concern | Browser: run a report as a scoped user |
| 7 | Does `Export Configuration` include layouts and reports, or only master data? | The migration vehicle | Browser: inspect an export |
| 8 | Which ADR settles in-transaction audit vs. the ADR-0012 outbox? | `AuditColumn`-equivalent audit reporting | ASG decision — already a tracked blocker |
