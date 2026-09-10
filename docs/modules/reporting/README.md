# Reporting

**Stated up front.** Lucernex has no report engine separate from its page engine. There is no
`Report` table anywhere in the 223-object schema. **A report is a `PageLayout` row with
`IsReport = true`** — run-tracked by `LastRunBy`/`LastRunDate`, formatted by `OutputType`,
parameterised by `RunModeFilters`, its columns held as `PageLayoutField` rows and its filters,
groupings and subtotals as `PageLayoutFilter` rows. Its columns are drawn from the same field
registry that forms use, whose foreign-key type Lucernex itself names **`Report/Form Field ID`**.

Around that generic engine sit four purpose-built report types with their own tables — Comparison
Report and the `Virtual*` computed-projection family — plus `AuditColumn`
for change auditing. There is **no** schedule table, **no** run-history table, **no** subscription
table and **no** chart table. Those four absences define most of what ASG Edge+ has to build from
scratch.

## Contents

| Document | What it covers |
|---|---|
| [report-field-registry.md](report-field-registry.md) | **The shared-registry proof.** Five independent pieces of evidence that the data-field catalog and the report-field catalog are one table; the registry's shape; its six consumers; what it does not hold |
| [data-model.md](data-model.md) | The generic engine, the four purpose-built report types, audit reporting, and a table of what is missing from the schema |
| [rules.md](rules.md) | `RPT-R-001` … `RPT-R-077`, each labelled Observed / Derived / Inferred, ending with the eight reporting requirements ASG has already recorded |
| [admin-tools.md](admin-tools.md) | The nine dashboard tools, what each most likely is, ASG's own required/reviewed decision for each, and a ranked priority for a live visit |
| [asg-edgeplus-mapping.md](asg-edgeplus-mapping.md) | Concept mapping onto work areas 27-31, schemas for the three tables Lucernex lacks, financial-correctness requirements, and migration sequencing |

## Related documents

| Document | Relationship |
|---|---|
| [modules/layouts-and-forms/](../layouts-and-forms/README.md) | The layout engine. A report is one of its faces; the two folders describe one system |
| [admin/005 — Manage Data Fields](../../admin/005-manage-data-fields.md) | The field registry as a screen. Its route is `ReportGroupAvailableFieldEdit.jsp` |
| [admin/008 — Manage Page Layouts](../../admin/008-manage-page-layouts.md) | The layout builder; the "(Run Report Action)" button kind |
| [admin/007 — Firm and Client Drop Downs](../../admin/007-firm-and-client-drop-downs.md) | The observed Audit Log dialog, which matches `AuditColumn` column-for-column |
| [admin/004 — Company Administration](../../admin/004-company-administration.md) | The admin tool routes |
| [admin/009 — Related Fields](../../admin/009-related-fields-and-data-model.md) | Why a report can include related-table fields |
| [data-model/graphql-api.md](../../data-model/graphql-api.md) | 490 types, 617 queries, 3 mutations, and the 10-value canonical type system behind the 448 `sTYPE_*` codes |

## The five sentences that matter

1. There is **no `Report` table**. `PageLayout.IsReport`, `IsDashboardReport`, `IsGlobalReport`,
   `OutputType`, `RunModeFilters`, `EntitySelectionFilter`, `LastRunBy` and `LastRunDate` are all
   columns on the page-layout record.
2. The FK type to the field catalog is literally named **`Report/Form Field ID`** — the vendor's own
   schema says the report field catalog and the form field catalog are one thing.
3. `PageLayoutFilter` carries `RowOrderBy`, `ColumnOrderBy` and `ShowSubtotal` on the same row as
   the filter criteria: **Lucernex reporting is pivot-shaped**, not flat-list-shaped.
4. `PageLayout` records only a **single most-recent run stamp**. There is no run history, no
   schedule, no subscription — which is exactly what ASG's "blank reports still sent" and
   "scheduled & external delivery" requirements need.
5. `AuditColumn.GroupID`/`SubGroupID` point at `ReportGroupData`, so **the audit trail is filed
   under the Data Fields taxonomy** — the registry organises audit as well as forms and reports.

## Open questions

Ranked by how much each blocks the ASG Edge+ rebuild. The lead has browser access to Manage
Dashboard Reports, GraphQL Explorer and the RESTful WebService Docs.

1. **Does Lucernex have charts at all?** No chart, series, axis, widget or visualisation object
   exists in the 223-table schema. Either dashboard tiles are grid/text only, or configuration is
   packed into `PageLayout.JSONConfigText`. This decides whether BRD 8's dashboards are a parity
   feature or a greenfield one. *Check:* open Manage Dashboard Reports and inspect one tile.
2. **Is there any report-run history beyond `LastRunBy`/`LastRunDate`?** Report Log is the same JSP
   as Job Log with `type=reportlog`, i.e. a *job* log. If no run history exists, ASG's operational
   requirements (RPT-R-075, "blank reports still sent") are greenfield, not migration. *Check:* open
   Report Log.
3. **Does Lucernex schedule reports, and where is a schedule stored?** No schedule or subscription
   table exists in the schema. RPT-R-073 (scheduled + SFTP delivery, Major) may have nothing to
   migrate from. *Check:* Report Log, Email Log, Job Log.
4. ~~**Are `PageLayout` / `PageLayoutField` / `PageLayoutFilter` exposed over GraphQL?**~~
   **Answered: no.** The schema has 490 types, 433 of them objects, and contains no layout, report,
   chart or rule type — 617 queries against 3 mutations, all over business objects
   ([graphql-api.md](../../data-model/graphql-api.md)). Reports and layouts cannot be migrated
   through the data API. *Still to check:* whether the REST tier differs, since it appears to be the
   write surface.
5. **What are the `OutputType` and `PageLayoutType` value sets?** Sets the output-format and
   layout-type enums, and the true scope of work areas 27-31. *Check:* GraphQL introspection, or
   distinct `EquivalentPLTypes` values.
6. **Is Portfolio/Capital-Program scoping enforced at the query level or only in the UI?** A
   multi-tenant correctness and SOC 2 question, raised but unresolved in
   [007](../../admin/007-firm-and-client-drop-downs.md). *Check:* run a report as a scoped user.
7. **Does Export Configuration include layouts and reports, or only master data?** Determines the
   migration vehicle for Reports/Layout/Field Migration. *Check:* inspect an export.
8. **Where does `ReportGroupData` store the three "Valid For..." applicability flags?** They are
   rendered by Manage Data Fields but exist on neither RGAF nor RGD in the object model. Affects how
   ASG Edge+ models field applicability.
9. **What does `ComparisonItem.XmlData` contain?** A serialised blob at the heart of the comparison
   report; unqueryable and a migration risk.
10. **How is a report's Portfolio/Capital-Program scope stored?** The chip control is observed on the
    layout edit dialog; no column in either offline artefact holds it.
