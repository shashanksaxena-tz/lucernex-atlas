# Administration — all 57 tools, classified

**Stated up front.** The administration dashboard exposes **57 tools** in `(ASG)BBW` and the same 57
in `(ASG)American Freight` (AF's dashboard renders six extra anchors, but they are shortcuts into
`FirmCodeEdit.jsp` for individual code tables — `Document Type Code`, `Job Title Code`,
`User Class Code` and three more — not distinct tools). This document is the **complete classified
inventory with routes**, which did not previously exist: the corpus documented nine of the 57 in
depth and named the rest only as a list.

**55 of 57 now have a screenshot.** The two that do not are the two on the capture-exclusion list,
and for the same reason: **`RESTful WebService Docs`** renders a live Basic token and a live JWT, and
**`GraphQL Explorer`** may carry an auth header in its console state
([`../../tenants/CAPTURE-EXCLUSIONS.md`](../../tenants/CAPTURE-EXCLUSIONS.md)). `Delete Entities`
*does* have a screenshot, in both tenants.

> **Screenshot numbers in this document were off by up to two, and the reason is worth keeping.**
> A `RESTful.jsp` capture was written to disk during the BBW sweep, deleted on discovery, and the
> set renumbered — so `bbw-admin/` went from 56 files to 55 and every reference above index 52
> shifted. `Layout Changes` was cited as `56-…`, `Generate Enterprise Report File` as `55-…`, and a
> `54-graphql-explorer.jpg` was cited that has never existed. All three are corrected here. This is
> precisely the rot [`../../CONVENTIONS.md`](../../CONVENTIONS.md) warns about when it asks for
> `code`-formatted paths rather than links — but a `code` path that is *wrong* is no better than a
> broken link, so the rule needs a checker, not just a format.

Three facts fall straight out of the route list and are worth stating before the tables.

**1. `Import Data` and `Export Configuration` are one subsystem.** They are `Messenger.jsp` and
`MessengerExportData.jsp`. Import and export are two ends of "Messenger", which makes a round-trip
plausible in the UI even though there is **no generic export endpoint in the REST API**
([`../import-export/`](../import-export/)).

**2. Firm Drop Downs and Client Drop Downs are genuinely two different registries**, not two views of
one: `FirmCodeList.jsp` (the 207 platform code tables, discriminated by `TableType`) versus
`CustomCodeTableEdit.jsp` (the firm's own `CustomCodeTable` / `CustomCodeField` pair). This was
**Inferred** in [`../drop-downs-code-tables/`](../drop-downs-code-tables/) from the object names; the
routes make it **Observed**.

**3. `Job Log` and `Report Log` are the same screen.** Both are `JobLogEdit.jsp` — two dashboard
entries, one page.

![The whole administration surface on one page. The vendor's own grouping is six boxes -- `Company Administration`, `Portfolio/Capital Program Administration`, `Member Administration`, `Portfolio Administration`, `Folder Administration`, `Data/PS Tools` -- with `Cost Management` and `Manage Defined Fields` as sub-headings inside two of them. The six extra anchors AF renders are the indented `Manage Defined Fields` entries: `Job Function Code`, `Job Title Code`, `User Class Code`, `Document Content Code`, `Document Type Code`, `Client Drop Downs`. They are shortcuts into `FirmCodeEdit.jsp`, not distinct tools. Note `Export Schema` sitting in `Data/PS Tools`, still unopened.](../../assets/screenshots/af-admin/01-admin-dashboard.jpg)


**Coverage, honestly.** **22 of 57** tools now have an owning document, up from 8. The remaining 35
are named, routed and screenshotted but not explained — and 10 of those are deliberate: budget and
bidding are out of scope by decision, and the four `/lxadmin/` tools are vendor-only. So the real
outstanding debt is **25 tools**.

Source: [`../../tenants/bbw-platform-inventory.json`](../../tenants/bbw-platform-inventory.json)
(`DashboardDispatchOld.jsp?dashboardName=admin`) and
[`../../tenants/af-counts.json`](../../tenants/af-counts.json). Screenshots in
`bbw-admin/` and
`af-admin/`. **Observed.** Per-tool status is also tracked in
[`../../COVERAGE.md`](../../COVERAGE.md#2-administration-tools-57).

---

## The inventory

### Configuration — the tenant's own model

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| Manage Data Fields | `/en/pagebuilder/ReportGroupAvailableFieldEdit.jsp` | [data-fields](../data-fields/) | `bbw-admin/10-manage-data-fields.jpg`, `bbw-admin/10-manage-data-fields.jpg` |
| Manage Page Layouts | `/en/pagebuilder/SummaryEntityPageLayoutEdit.jsp` | [page-layouts](../page-layouts/) | `bbw-admin/09-manage-page-layouts.jpg`, `bbw-admin/09-manage-page-layouts.jpg` |
| Manage Forms | `/en/admin/FirmCodeEdit.jsp` | [workflows-forms](../workflows-forms/) | `af-admin/06-manage-forms.jpg`, `bbw-admin/05-manage-forms.jpg`, `af-admin/06-manage-forms.jpg`, `bbw-admin/05-manage-forms.jpg` |
| Manage Custom Lists | `/en/admin/CustomListEdit.jsp` | [custom-lists](../custom-lists/) | `af-admin/07-manage-custom-lists.jpg`, `bbw-admin/06-manage-custom-lists.jpg`, `af-admin/07-manage-custom-lists.jpg`, `bbw-admin/06-manage-custom-lists.jpg` |
| Manage Work Flows | `/en/workflow/WorkFlowTemplateEdit.jsp` | [workflows-forms](../workflows-forms/) | `af-admin/09-manage-work-flows.jpg`, `bbw-admin/08-manage-work-flows.jpg`, `af-admin/09-manage-work-flows.jpg`, `bbw-admin/08-manage-work-flows.jpg` |
| Manage Firm Drop Downs | `/en/admin/FirmCodeList.jsp` | [drop-downs-code-tables](../drop-downs-code-tables/) | `bbw-admin/27-manage-firm-drop-downs.jpg`, `bbw-admin/27-manage-firm-drop-downs.jpg` |
| Client Drop Downs | `/en/admin/CustomCodeTableEdit.jsp` | [drop-downs-code-tables](../drop-downs-code-tables/) | `bbw-admin/28-client-drop-downs.jpg`, `bbw-admin/28-client-drop-downs.jpg` |
| Manage Top Menu | `/en/admin/ManageTopMenu.jsp` | **—** | `bbw-admin/16-manage-top-menu.jpg`, `bbw-admin/16-manage-top-menu.jpg` |
| Manage Firm Dictionary | `/en/admin/Dictionary.jsp` | **—** | `bbw-admin/17-manage-firm-dictionary.jpg`, `bbw-admin/17-manage-firm-dictionary.jpg` |
| Layout Changes | `/en/admin/ShowLayoutChanges.jsp` | **—** | `bbw-admin/54-layout-changes.jpg` |
| Manage Folder Templates | `/en/admin/FolderTemplateEdit.jsp` | [README.md](../../modules/documents-folders/README.md) | `bbw-admin/44-manage-folder-templates.jpg` |
| Manage Binder Templates | `/en/CommitteeDocuments/BinderTemplateEdit.jsp` | **—** | `af-admin/05-manage-binder-templates.jpg`, `bbw-admin/04-manage-binder-templates.jpg`, `af-admin/05-manage-binder-templates.jpg`, `bbw-admin/04-manage-binder-templates.jpg` |
| Manage Schedule Templates | `/en/admin/TaskTemplateEdit.jsp` | [scheduling.md](../../modules/projects-capital/scheduling.md) | `af-admin/03-manage-schedule-templates.jpg`, `bbw-admin/02-manage-schedule-templates.jpg`, `af-admin/03-manage-schedule-templates.jpg`, `bbw-admin/02-manage-schedule-templates.jpg` |
| Manage Milestone Timeline | `/en/admin/ProcessTimelineEdit.jsp` | **—** | `af-admin/04-manage-milestone-timeline.jpg`, `bbw-admin/03-manage-milestone-timeline.jpg`, `af-admin/04-manage-milestone-timeline.jpg`, `bbw-admin/03-manage-milestone-timeline.jpg` |

### Master data — the records a firm administers

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| Manage Company | `/en/admin/FirmEdit.jsp` | [004-company-administration.md](../../admin/004-company-administration.md) | `af-admin/02-manage-company.jpg`, `bbw-admin/01-manage-company.jpg`, `af-admin/02-manage-company.jpg`, `bbw-admin/01-manage-company.jpg` |
| Manage Portfolios/Capital Programs | `/en/admin/ProgramEdit.jsp` | [README.md](../../modules/portfolio-transactions/README.md) | `bbw-admin/29-manage-portfolios-capital-programs.jpg`, `bbw-admin/29-manage-portfolios-capital-programs.jpg` |
| Manage Locations | `/en/admin/LocationEdit.jsp` | **—** | `bbw-admin/41-manage-locations.jpg` |
| Manage Facilities | `/en/admin/FacilityEditForm.jsp` | **—** | `bbw-admin/39-manage-facilities.jpg` |
| Manage Contracts | `/en/admin/ContractEdit.jsp` | **—** | `bbw-admin/40-manage-contracts.jpg` |
| Manage Complex/Center Details | `/en/admin/ComplexEdit.jsp` | **—** | `bbw-admin/42-manage-complex-center-details.jpg` |
| Manage Organizations | `/en/admin/OrganizationEdit.jsp` | **—** | `bbw-admin/43-manage-organizations.jpg` |
| Manage Parts and Inventory | `/en/lease/PartEdit.jsp` | [README.md](../../modules/assets-equipment/README.md) | `af-admin/08-manage-parts-and-inventory.jpg`, `bbw-admin/07-manage-parts-and-inventory.jpg`, `af-admin/08-manage-parts-and-inventory.jpg`, `bbw-admin/07-manage-parts-and-inventory.jpg` |

### People, organisations and access

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| Manage Members/Contacts | `/en/admin/ContactEdit.jsp` | [README.md](../../modules/people-parties/README.md) | `bbw-admin/33-manage-members-contacts.jpg`, `bbw-admin/33-manage-members-contacts.jpg` |
| Manage Membership | `/en/admin/ManageOneMemberManyProjects.jsp` | **—** | `bbw-admin/37-manage-membership.jpg`, `bbw-admin/37-manage-membership.jpg` |
| Manage Employers | `/en/admin/EmployerEdit.jsp` | [README.md](../../modules/people-parties/README.md) | `bbw-admin/35-manage-employers.jpg`, `bbw-admin/35-manage-employers.jpg` |
| Manage Employer Members | `/en/admin/ManageEmployerMembers.jsp` | **—** | `bbw-admin/34-manage-employer-members.jpg`, `bbw-admin/34-manage-employer-members.jpg` |
| Manage Vendors | `/en/admin/VendorActivate.jsp` | **—** | `bbw-admin/36-manage-vendors.jpg`, `bbw-admin/36-manage-vendors.jpg` |
| Manage Regions/Org Chart | `/en/admin/OrgChartEdit.jsp` | [README.md](../../modules/platform-tenancy/README.md) | `bbw-admin/30-manage-regions-org-chart.jpg`, `bbw-admin/30-manage-regions-org-chart.jpg` |
| Manage Security | `/en/admin/SecurityPageAccess.jsp` | **—** | `bbw-admin/38-manage-security.jpg` |

### Financial reference data

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| Manage Exchange Rates | `/en/admin/ManageCurrencyRates.jsp` | **—** | `bbw-admin/24-manage-exchange-rates.jpg`, `bbw-admin/24-manage-exchange-rates.jpg` |
| Manage Discount Rates | `/en/admin/ManageDiscountRates.jsp` | **—** | `bbw-admin/25-manage-discount-rates.jpg`, `bbw-admin/25-manage-discount-rates.jpg` |
| Manage CPI Data | `/en/admin/ManageCPIData.jsp` | **—** | `bbw-admin/26-manage-cpi-data.jpg`, `bbw-admin/26-manage-cpi-data.jpg` |
| Manage Fiscal Calendar | `/en/admin/ManageFiscalPeriod.jsp` | **—** | `bbw-admin/31-manage-fiscal-calendar.jpg`, `bbw-admin/31-manage-fiscal-calendar.jpg` |
| Manage Holiday Calendar | `/en/admin/ManageHolidayCalendar.jsp` | **—** | `bbw-admin/32-manage-holiday-calendar.jpg`, `bbw-admin/32-manage-holiday-calendar.jpg` |

### Import, export and jobs

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| Import Data | `/en/admin/Messenger.jsp` | [import-export](../import-export/) | `bbw-admin/12-import-data.jpg`, `bbw-admin/12-import-data.jpg` |
| Import Best Practice Templates | `/en/admin/BestPracticeTemplates.jsp` | **—** | `bbw-admin/13-import-best-practice-templates.jpg`, `bbw-admin/13-import-best-practice-templates.jpg` |
| Export Configuration | `/en/admin/MessengerExportData.jsp` | [import-export](../import-export/) | `bbw-admin/14-export-configuration.jpg`, `bbw-admin/14-export-configuration.jpg` |
| Job Log | `/en/admin/JobLogEdit.jsp` | [import-export](../import-export/) | `bbw-admin/15-job-log.jpg`, `bbw-admin/15-job-log.jpg` |
| Report Log | `/en/admin/JobLogEdit.jsp` | **—** | `bbw-admin/49-report-log.jpg` |
| Generate Enterprise Report File | `/en/admin/GenBaseReport.jsp` | **—** | `bbw-admin/53-generate-enterprise-report-file.jpg` |

### Diagnostics, logs and developer tools

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| View Object Model | `/en/admin/ShowObjectDetails.jsp` | [README.md](../../data-model/README.md) | `bbw-admin/45-view-object-model.jpg` |
| View Data Model / Data Values (experimental) | `/en/test/walkHierarchy.jsp` | **—** | `bbw-admin/46-view-data-model-data-values-experimental.jpg` |
| Audit Reports | `/en/reports/AuditReport.jsp` | **—** | `bbw-admin/47-audit-reports.jpg` |
| Email Log | `/en/reports/EMailLogs.jsp` | **—** | `bbw-admin/48-email-log.jpg` |
| RESTful WebService Docs | `/en/test/RESTful.jsp` | [import-export](../import-export/) | — |
| GraphQL Explorer | `/en/admin/graphql.jsp` | [graphql-api.md](../../data-model/graphql-api.md) | **—** (capture-excluded) |
| Manage Dashboard Reports | `/en/reports/ManageDashboardModules.jsp` | [admin-tools.md](../../modules/reporting/admin-tools.md) | `bbw-admin/11-manage-dashboard-reports.jpg`, `bbw-admin/11-manage-dashboard-reports.jpg` |

### Budget and bidding — out of scope by decision

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| Manage Budget Templates | `/en/budget/BudgetTemplateEdit.jsp` | **—** | `bbw-admin/19-manage-budget-templates.jpg`, `bbw-admin/19-manage-budget-templates.jpg` |
| Manage Budget Views | `/en/budget/BudgetLayoutView.jsp` | **—** | `bbw-admin/20-manage-budget-views.jpg`, `bbw-admin/20-manage-budget-views.jpg` |
| Manage Budget Types | `/en/budget/BudgetColumnTypeEdit.jsp` | **—** | `bbw-admin/21-manage-budget-types.jpg`, `bbw-admin/21-manage-budget-types.jpg` |
| Manage Budget Summary Page | `/en/budget/BudgetSummaryEdit.jsp` | **—** | `bbw-admin/22-manage-budget-summary-page.jpg`, `bbw-admin/22-manage-budget-summary-page.jpg` |
| Manage Budget Index Variables | `/en/budget/BudgetIndexEdit.jsp` | **—** | `bbw-admin/23-manage-budget-index-variables.jpg`, `bbw-admin/23-manage-budget-index-variables.jpg` |
| Manage Bid Package Templates | `/en/admin/BidPackageTemplate.jsp` | **—** | `bbw-admin/18-manage-bid-package-templates.jpg`, `bbw-admin/18-manage-bid-package-templates.jpg` |

### Vendor-only (`/lxadmin/`) — not a firm capability

| Tool | Route | Doc | Screenshot |
|---|---|---|---|
| Modify Straight Line Status | `/en/admin/lxadmin/SLDemoTweaks.jsp` | **—** | `bbw-admin/50-modify-straight-line-status.jpg` |
| Data Conversion Cleaner | `/en/admin/lxadmin/DataLoadTweaks.jsp` | **—** | `bbw-admin/51-data-conversion-cleaner.jpg` |
| Test Email Address | `/en/admin/lxadmin/EmailTest.jsp` | **—** | `bbw-admin/52-test-email-address.jpg` |
| Delete Entities | `/en/admin/lxadmin/DeleteEntities.jsp` | **—** | `bbw-admin/55-delete-entities.jpg`, `af-admin/64-delete-entities.jpg` |
---

## What the classification shows

**Derived.** The 57 tools split unevenly, and the shape is informative:

| Group | Tools | |
|---|---:|---|
| Configuration — the tenant's own model | 14 | The largest group, and the heart of the product |
| Master data | 8 | |
| People, organisations and access | 7 | |
| Diagnostics and developer tools | 7 | |
| Import, export and jobs | 6 | |
| Budget and bidding | 6 | **Out of scope by decision** |
| Financial reference data | 5 | |
| Vendor-only `/lxadmin/` | 4 | **Not a firm capability** |

**Derived.** **A quarter of the administration surface is the configuration engine** — data fields,
layouts, forms, custom lists, workflows, drop-downs, dictionary, menus, templates. That matches what
the rest of this corpus found from the other direction: Lucernex is a configuration platform with a
lease-accounting application on top, not a lease application with some settings.

**Derived.** There is **no tenant-facing tool for creating an entity type**. Custom Lists and Forms
are the only ways a firm adds a record shape, and both go through the `Issue`/`CodeIssueType`
machinery ([`../custom-lists/`](../custom-lists/)). A firm cannot create a new first-class entity.

**Derived.** Five tools manage **reference data** — exchange rates, discount rates, CPI data, fiscal
calendar, holiday calendar. Four feed the accounting engine; the **holiday calendar does not** — its
own on-screen help says holiday days determine *task completion dates*, so it belongs to project
scheduling, which is out of scope. All five are now documented in
[`../reference-data/`](../reference-data/). `Manage Discount Rates` in particular feeds the ASC 842 / IFRS 16
calculations directly ([`../../modules/accounting/`](../../modules/accounting/)), and
`Manage CPI Data` feeds index-based escalations
([`../../modules/contracts/escalations.md`](../../modules/contracts/escalations.md)). **Now written
up** — see [`../reference-data/`](../reference-data/), which finds that four of the five tables are
empty in BBW and the discount-rate table in particular is empty while the ASC 842 engine runs.

---

## `Manage Firm Dictionary` — every label in this corpus is tenant-overridable

**Observed** (`/en/admin/Dictionary.jsp`,
`bbw-admin/17-manage-firm-dictionary.jpg`).
The screen is titled *"Import bbw Dictionary Spreadsheet"* and has two halves.

**Upload.** *"Note: You can upload new dictionary to provide new translation **or to just overwrite
the field labels**."* Two modes, by radio:

| Mode | Effect |
|---|---|
| `Remove all current translation phrases and replace with uploaded file` | Wholesale replacement |
| **`Append current translation phrases with all non-empty language phrases in uploaded file`** | **Default** — merge |

The file is an **XLSX**, chosen with `Choose file`, then `Upload New Dictionary`.

![`Manage Firm Dictionary`. The upload half replaces or appends translation phrases; the note above it says the file can be used *"to just overwrite the field labels"*. This screen is the reason every UI label in this corpus carries an implicit asterisk.](../../assets/screenshots/bbw-admin/17-manage-firm-dictionary.jpg)


**Download.** Four scopes, plus a multi-select `For Language:` currently holding `English`:

| Option | |
|---|---|
| `All phrases (global and firm specific)` | |
| `Firm specific phrases` | |
| **`Firm specific phrases not translated`** | **Default selection** |
| `All phrases translated by company` | |

**Derived — and this is a caveat on the entire corpus.** A firm can **overwrite field labels**
tenant-wide by uploading a spreadsheet. So **every UI label recorded anywhere in these documents is
potentially tenant-local**: screen names, navigation node names, field labels, code-table value
names. The internal names — `CodeContractStatusID`, `ScriptName`, physical table names — are not
affected, which is exactly why
[`../../CONVENTIONS.md`](../../CONVENTIONS.md) requires real field and table names in `code` rather
than paraphrases. That convention turns out to be load-bearing rather than stylistic.

**Derived.** The dictionary has the same **global / firm-specific** split as the field registry
(`RGAF.IsGlobal` + `FirmID`) and the layout registry (`Firm Layouts` / `Global Layouts`). That is now
**three** subsystems using the identical two-tier pattern — strong support for the Hub/Spoke shape,
and a clear instruction for the rebuild: labels belong in a translatable dictionary with a firm
override layer, not hard-coded on the field.

**Derived.** Labels are **multilingual** — `For Language:` is a multi-select. Nothing else in this
corpus has touched internationalisation, and the REST surface carries `/i18n` ("i18n resource
bundle") and `/membership` ("membership resource bundle") tags to match
([`../import-export/`](../import-export/)).

**Open.** Whether either tenant has actually overridden any label is unknown — the answer is one
`Download Current Dictionary` with `Firm specific phrases` selected. Until then, treat recorded
labels as *probably* platform defaults but not guaranteed.

---

## `Client Drop Downs` — 38 firm-defined drop-downs

**Observed** (`/en/admin/CustomCodeTableEdit.jsp`, tab title **"Manage Custom Drop Down"**,
`bbw-admin/28-client-drop-downs.jpg`).
*"Displaying 1 - 15 of 38"*.

| | |
|---|---|
| Columns | `Actions`, **`Custom Drop Down Name *`**, `Description`, and a fourth column truncated at `Smar…` |
| Row actions | **`edit \| delete` on every row** — none protected |
| Action | `Add Custom Drop Down…` |

**Derived — it supports the provenance hypothesis.** All 38 firm-defined drop-downs are deletable,
while 154 of 1,140 *platform* code-table values are protected by `isReadOnlyRecord`
([`../drop-downs-code-tables/`](../drop-downs-code-tables/)). Firm-owned things are deletable;
platform-owned things are not. That is exactly what the provenance reading predicts.

**Observed.** Fifteen of the 38 names: `ASC 842 Month`, `ASC 842 Year`, `Brands`,
`Change Request Area`, `Contingency Trigger`, `Cost Center`, `Co-Tenancy Violation Alt Rent Sunset`,
`Co-Tenancy Violation Alt Rent Sunset Landlord Option`, `Co-Tenancy Violation Option to Term`,
`Co-Tenancy Violation Type`, `Funds Type`, `Guarantor`, `Increase Type`,
**`Lease Admin Request Type`**, **`Lease Status`**.

**Derived — two of these matter elsewhere.**

1. **`Lease Admin Request Type`** is the source of `Issue.LAR_RequestType`, which drives **44 of the
   54** conditional-field criteria clauses in the tenant
   ([`../page-layouts/`](../page-layouts/#conditional-fields--used-and-the-stored-shape-is-now-known)).
   So the conditional engine's main driver is a **firm-defined** drop-down, not a platform one.
2. **`Lease Status`** is a *custom* drop-down, and it sits alongside the *platform* `Contract Status
   Code` which carries only three values (`Active`, `AI Abstracted`, `Inactive`) and does not match
   BRD-24's Open → Active → Possession → Paying Rent → Closed. **Inferred:** ASG may be tracking the
   real contract lifecycle in this firm-defined `Lease Status` rather than in the platform status
   field. That would resolve the corpus's long-standing contract-lifecycle question
   ([`../../INDEX.md`](../../INDEX.md#what-is-still-open), item 2) — **and it is one screen away**:
   open `Lease Status` and read its values.

**Answered.** The truncated fourth column is **`Smart List Parent Drop Down`**, read in full from the
American Freight capture of the same screen
(`drop-downs/client-lease-status-values.jpg`). It is the UI for the
**dependent/cascading** behaviour that `CustomCodeField.ParentCustomCodeFieldID` implements
([`../drop-downs-code-tables/`](../drop-downs-code-tables/#dependent-drop-downs--an-unnoticed-feature)),
and the value editor carries a matching `<select>` of the same name. The inference was right; it is
now **Observed**.

![`Client Drop Downs` at BBW -- the firm's own registry, distinct from the 207 platform code tables. Every row carries `edit | delete`, with none protected, against 154 of 1,140 protected values in the platform registry. The fourth column is cropped here at `Smar...`; it is `Smart List Parent Drop Down`.](../../assets/screenshots/bbw-admin/28-client-drop-downs.jpg)

---

## The three tools that were answering open questions — all now read

| Tool | Route | What it settled | What remains |
|---|---|---|---|
| **Manage Security** | `/en/admin/SecurityPageAccess.jsp` | **Three independent gates** on a screen; a four-level ladder plus explicit inherit; **four securable kinds** — pages, actions, **fields**, budget columns. Field-level security is the likeliest home of read-only-ness. See [`../security-access/`](../security-access/) | Real user-class values. The screen opened on `Default Security`, which is **not evidence** |
| **Manage Top Menu** | `/en/admin/ManageTopMenu.jsp` | **14 menu structures** exist, reconciling the 892-node count against the 4–5 roots a user meets. `Equipment Contract` is among them. See [`../security-access/`](../security-access/) | Whether a firm may **edit** the tree. If it can, "navigation is platform-seeded" needs qualifying |
| **Layout Changes** | `/en/admin/ShowLayoutChanges.jsp` | The vendor workbook's *"Need further explanation as to what this is"* — it is a **layout change report**, filtered by added/modified version and by **`Firm Layouts` vs `Global Layouts`**. The UI names the two layout tiers directly. Vendor-labelled **experimental**, and it **omits removed fields**. See [`../page-layouts/`](../page-layouts/) | Whether it returns history at all — it was run with the date defaulted to today |

**Derived.** All three were read from screenshots rather than by driving the browser, and each closed
a question that had been open for some time. **The 55 admin screenshots are an under-used asset** —
several of the remaining unread ones probably carry comparable answers.

---

## Open questions

1. **What do the remaining undocumented tools do?** The five reference-data tools are now written up
   in [`../reference-data/`](../reference-data/). Next: `Manage Security`, `Layout Changes` and
   `Manage Top Menu` — see the table above.
2. **Is `Manage Company` the only place the 21 entitlement flags are set?**
   [`af-firm-record.json`](../../tenants/af-firm-record.json) captured 71 Firm fields and 21
   entitlement flags from `FirmEdit.jsp`; whether a firm administrator can change them, or only read
   them, is unobserved — and it matters, because `Allow Equipment Contracts?` is `Yes` at AF while
   the root does not render.
3. **What does `Import Best Practice Templates` import?** A vendor-supplied starter configuration is
   the obvious reading, and if so it is the mechanism behind the "one ASG template set published per
   tenant" model found in [`../page-layouts/`](../page-layouts/#the-publish-and-fork-model).
   **Inferred**, untested.
4. **What is `Generate Enterprise Report File`?** `GenBaseReport.jsp`. Unknown.
5. **Does `Manage Firm Dictionary` rename product-wide labels?** `Dictionary.jsp`. If a firm can
   relabel platform terms, every label in this corpus is tenant-specific — which would be a
   significant caveat on the whole document set.
6. **Why is `Manage Contracts` an admin tool at all**, when contracts are an end-user surface with 39
   screens? Likely a bulk/administrative editor; unconfirmed.
