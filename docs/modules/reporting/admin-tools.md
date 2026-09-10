# Reporting-related administration tools

**Stated up front.** Nine System Administrator Dashboard entries touch reporting. Two are report
*authoring* surfaces (Manage Dashboard Reports, Generate Enterprise Report File), three are
*operational* views (Report Log, Audit Reports, Email Log), two are *bulk data movement* (Export
Schema, Export Configuration, Import Data), and two are *API discovery* (RESTful WebService Docs,
GraphQL Explorer). Only Manage Dashboard Reports and the three operational views have been reasoned
about from schema evidence; the rest are inventory with route-level evidence only. **None has been
opened.** Every "what it most likely is" column below is **Inferred** unless stated otherwise.

The ASG columns come from `_xlsx_feature_list.txt` (sheets `ExistingModules` and
`ASG Edge Plus Modules`) and are **Observed** — they are ASG's own recorded decisions, not
interpretation.

## The inventory

| Tool | Route | Section | ASG: required? | ASG: reviewed? | ASG's own note |
|---|---|---|:---:|:---:|---|
| Manage Dashboard Reports | `/en/reports/ManageDashboardModules.jsp` | Company Administration | **Yes** | Yes | *"this will be at client level, done"* / *"Move to UI & Structural Configuration (Client Level), need to move to standard reports, shud be under reports module"* |
| Report Log | `/en/admin/JobLogEdit.jsp?type=reportlog` | Data/PS Tools | **Yes** | No | *"Correct"* |
| Audit Reports | `/en/reports/AuditReport.jsp` | Data/PS Tools | **Yes** | No | *"Correct"* |
| Email Log | `/en/reports/EMailLogs.jsp` | Data/PS Tools | **Yes** | No | *"Correct"* |
| Generate Enterprise Report File | `/en/admin/GenBaseReport.jsp` | Data/PS Tools | ? | No | *"we do not use Generate Enterprise Report File. We use the Audit Log to the best of our ability but a lot information is not provided in the log file."* |
| Export Schema | `javascript:` handler | Data/PS Tools | ? | No | *"Move to Data Tools"* — marked Done |
| Export Configuration | `/en/admin/MessengerExportData.jsp` | Company Administration | **Yes** | Yes | *"Correct"* |
| Import Data | `/en/admin/Messenger.jsp` | Company Administration | **Yes** | Yes | *"Correct"* |
| RESTful WebService Docs | `/en/test/RESTful.jsp` | Data/PS Tools | ? | No | *"Move to Data Tools"* — marked Done |
| GraphQL Explorer | `/en/admin/graphql.jsp` | Data/PS Tools | ? | No | *"Move to Data Tools"* — marked Done |

Routes are **Observed** ([004](../../admin/004-company-administration.md)). "?" in the required
column is ASG's own literal entry, meaning undecided.

## What each one most likely is

### Manage Dashboard Reports — `/en/reports/ManageDashboardModules.jsp`

The route says *modules*, not *reports*: this administers **dashboard tiles**. Schema support:
`PageLayout.IsDashboardReport` (boolean) and `UserClassSecurity.DashboardComponentTitle` (text).
**Observed** columns. So a dashboard tile is a `PageLayout` row with that flag set, and access to it
is granted per user class **by its title string**.

Three things to confirm on a live visit, in priority order:

1. **How does a tile render a chart?** The 223-object schema contains no chart, series, axis,
   widget or visualisation table (**Derived**, exhaustive grep). Either tiles are grid/text only, or
   chart configuration is packed into `PageLayout.JSONConfigText`. This is the largest single
   unknown in the reporting subsystem.
2. Does this screen edit `PageLayout` records directly, or does it maintain a separate module
   registry that *points at* layouts?
3. Are tiles per-user, per-user-class, or per-tenant?

ASG has already decided this belongs under a Reports module rather than admin, and at client level.

### Report Log — `/en/admin/JobLogEdit.jsp?type=reportlog`

Same JSP as **Job Log** (`?type=joblog`), a different `type` parameter. **Observed.** So Report Log
is the job log filtered to report-generation jobs — a *background job* history, not a
report-execution history.

That matters because the schema has **no report-run history table**: `PageLayout` carries only
`LastRunBy`/`LastRunDate`, a single most-recent stamp. **Derived.** Anything resembling per-run
history must therefore live in the job subsystem, which is not represented in the object model
either. Confirm what columns this screen actually shows; it is the only visible source of report
execution history.

ASG's recorded pain point is directly about this: *"There is a 'Job Log' link under Company
Administration. sysadmin checks this to see if scheduled jobs ran. It's a click-away list, not an
at-a-glance status board"*, and *"Blank Reports Still Sent"* (`_xlsx_feature_list.txt` line 247).
**Observed.**

### Audit Reports — `/en/reports/AuditReport.jsp`

Under `/en/reports/`, so it is a report screen, and its backing table is almost certainly
`AuditColumn` — whose columns match the Audit Log dialog observed in
[007](../../admin/007-firm-and-client-drop-downs.md#value-level-editor--scoping-and-audit-log)
eleven for eleven (**Derived**; see [data-model.md](data-model.md#audit-reporting--auditcolumn)).
The dialog in 007 is a record-scoped viewer; this screen is presumably the tenant-wide one.

Worth confirming: whether it can filter by `GroupID`/`SubGroupID` — i.e. whether an administrator
can ask "show me every change to any field in *Contract / Common Area Maintenance*". The schema
supports it. ASG's stated requirement is *"Readable Logs — audit tools are just raw links"*
(line 241), so this is a screen ASG intends to replace rather than reproduce.

### Email Log — `/en/reports/EMailLogs.jsp`

Backed by `EMailSentLog` (1 exposed field) and `EMailReceivedLog` (15). **Observed** object names.
If scheduled report delivery exists in Lucernex, its evidence would surface here — this is the only
place to look, given there is no schedule or subscription table in the schema. Contains personal
data; treat accordingly.

### Generate Enterprise Report File — `/en/admin/GenBaseReport.jsp`

"Base report" plus "enterprise" plus "file" reads as a full-tenant data extract for downstream
consumption — a periodic bulk file rather than an interactive report. **Inferred**, low confidence.

ASG's note settles the priority regardless: *"we do not use Generate Enterprise Report File."*
**Observed.** Low value to investigate; document it and move on.

### Export Schema — `javascript:` handler

No route was captured, only a JS handler. **Observed** (as a gap). Almost certainly emits the DDL
or object-model definition — probably the same content as `ShowObjectDetails.jsp`
([009](../../admin/009-related-fields-and-data-model.md)) in file form.

**This is the highest-value tool on the list for the rebuild** and the one thing that could resolve
several open questions at once. `_lucernex_objects_summary.txt` covers 223 business objects but
**omits `PageLayout`, `PageLayoutField` and `PageLayoutFilter` entirely**
(**Derived**; see [layouts-and-forms/conditional-fields.md § 2.1](../layouts-and-forms/data-model.md#table-inventory)).
If Export Schema emits the *physical* schema rather than the business-object model, it would give
the real column list for the layout tables — including whatever holds the conditional-field target
link and per-placement required-ness.

Read-only by name, but it is a generation action; confirm before running.

### Export Configuration — `/en/admin/MessengerExportData.jsp`

Paired with Import Data (`Messenger.jsp`) — the same "Messenger" subsystem, export and import
halves. **Observed** routes. Exports *tenant configuration* (layouts, fields, dropdowns, workflows)
rather than business data, which makes it the natural migration path for a Lucernex→ASG Edge+ move
and the direct counterpart of the workbook's **Layout Migration** and **Field Migration** work
areas.

Second-highest value after Export Schema, for the same reason: it should contain the layout
configuration in a serialised, inspectable form.

### Import Data — `/en/admin/Messenger.jsp`

The mutating half. ASG marked it required and reviewed. Their stated requirement is a **bulk action
confirmation dashboard**: *"After bulk import, no preview of changes before execution. No
'rollback' visibility"*, priority Critical (line 250). **Observed.** Do not activate.

### RESTful WebService Docs — `/en/test/RESTful.jsp`

Under `/en/test/`, like `walkHierarchy.jsp` — a developer tool exposed to administrators.
**Observed** route. Self-documenting REST API surface. Its value here is confirming whether
`PageLayout`, `PageLayoutField` and `PageLayoutFilter` are exposed over the API at all; the
business-object-model boundary suggests they may not be.

### GraphQL Explorer — `/en/admin/graphql.jsp`

**Now visited** — introspected in [data-model/graphql-api.md](../../data-model/graphql-api.md).
Headline results: **490 types** (433 objects, 31 input objects, 10 scalars, 10 enums, 6 interfaces),
**617 queries against 3 mutations**, a **10-value canonical field-type system**
(`BOOLEAN COMPUTED DATE DATETIME FK FLOAT INTEGER MONEY PERCENTAGE STRING`) underneath the 448
`sTYPE_*`/`sCODE_*` presentation codes, a `BigDecimal` scalar, and six interfaces including
`HasUDFs`, `ClientListRowInterface` and `IssueInterface`.

**The decisive negative for reporting: there is no layout, report, chart or rule type anywhere in
the schema.** Presentation and reporting metadata is invisible to the data API. A report or layout
migration cannot run through GraphQL.

What it could still settle in a second session:

| Question | Query |
|---|---|
| Which column persists `json.conditionalFieldsConfig`? | `PageLayoutField.DisplayOptionJSON`, `PageLayoutField.JSONConfigText`, `PageLayout.JSONConfigText` for a layout with rules |
| The `CriteriaType` operator codebook | distinct `CriteriaType1`/`CriteriaType2` values |
| The `PageLayoutType` and `OutputType` vocabularies | distinct values, or enum introspection |
| Where per-placement required-ness lives | full `PageLayoutField` type introspection |
| Whether layout metadata is API-exposed at all | schema introspection |

Caution: an explorer with mutation support can change data. Read-only queries only.

## Priority for a live visit

| Rank | Tool | What it unblocks |
|---:|---|---|
| 1 | **GraphQL Explorer** | The conditional-field model; operator codebook; layout type vocabulary; required-ness storage |
| 2 | **Export Configuration** | Serialised layout configuration — the migration path, and a second route to the same answers |
| 3 | **Manage Dashboard Reports** | How a tile renders; whether charts exist at all |
| 4 | **Export Schema** | The physical schema for the three layout tables |
| 5 | **Report Log** | Whether any report-run history exists |
| 6 | **RESTful WebService Docs** | API surface; cross-check on GraphQL findings |
| 7 | **Audit Reports** | Whether audit can be grouped by the registry tree |
| 8 | Email Log | Evidence of scheduled delivery |
| 9 | Generate Enterprise Report File | ASG does not use it |

## Tools not on the lead's list but relevant

| Tool | Route | Why it matters |
|---|---|---|
| **View Object Model** | `/en/admin/ShowObjectDetails.jsp` | Already used in [009](../../admin/009-related-fields-and-data-model.md). 224 tables; `sqlTableID` values collected: Contract 2792, Facility 2530, Location 2804, Employer 2529, PaymentTransaction 2810, Complex 2791. Check whether `PageLayout` is selectable in its dropdown — if it is, the whole layout schema is one click away |
| **View Data Model (experimental)** | `/en/test/walkHierarchy.jsp` | Its unexercised `Schema With Fields` mode would annotate FK columns onto the aggregate tree |
| **Layout Changes** | `/en/admin/ShowLayoutChanges.jsp` | Layout configuration audit. ASG's note: *"Need further explanation as to what this is"* |
| **Job Log** | `/en/admin/JobLogEdit.jsp?type=joblog` | The other half of Report Log; where scheduling evidence would be |
| **Manage Features / Global Properties** | not captured in 004 | `GlobalProperty` (4 fields) — feature flags. Listed in the workbook, not in the 004 capture |
| **Manage Scratch Pads** | not captured in 004 | `ScratchPad` (1 field). Listed in the workbook only |
| **Manage Excel Service** | not captured in 004 | Listed in the workbook only. Given ASG's report-to-import requirement, worth identifying |

The last three are **Observed** in `_xlsx_feature_list.txt` (`ExistingModules` sheet, Data/PS Tools)
but absent from the [004](../../admin/004-company-administration.md) capture — either they are
newer than that capture, or they were missed. Worth reconciling.
