# Admin & Tenancy

The platform underpinnings every feature above stands on: firms (tenants), the universal entity supertype, value lists, and the API. The two keys are constantly confused because both appear on nearly every record.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Platform and firm administrators. 57 admin tools, and the boundary between what the vendor owns and what a firm may change runs through all of them.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

Company Administration and the Data-PS tools.

## FirmID = tenant key

*Observed · capability · source: `docs/data-model/project-entity.md`*

The firm is the tenant, and its ID is the tenant key - NOT the universal entity ID, even though 163 foreign keys point at the entity supertype. The tenant key is typed as plain text, not a declared foreign key: the one relationship every row has is the one the schema declines to model, which is exactly why tenant isolation cannot be enforced by the schema. Decisive for database-per-tenant.

## Tenant in the token

*Observed · capability · source: `Live JWT inspection`*

The tenant travels in the login token: the session JWT carries the firm name and a cluster claim shaped host:tenant - evidence the platform routes each request to a tenant-specific database using a value inside the token, not a lookup in a shared table.

## 448 codes, 10 types

*Observed · capability · source: `docs/data-model/graphql-api.md`*

448 field-type codes hide a 10-value system: the API's type enum is boolean, computed, date, datetime, foreign key, float, integer, money, percentage, string. Computed and foreign-key are first-class types - the platform distinguishes engine-calculated values from user input in its type system. Money and percentage are distinct from float, and BigDecimal is a declared scalar: the vendor reached the same conclusion the rebuild's constitution mandates.

## 207 code tables

*Observed · capability · source: `docs/data-model/code-table-registry.md`*

One value-list registry, 207 entries: all admin-controlled lists are values of a single type discriminator. Master lists - lifecycle states, schedule types, workflow statuses - are configuration, not schema.

## Read-heavy API

*Observed · capability · source: `docs/data-model/graphql-api.md + rest-api.md`*

The API is read-heavy by design: 617 GraphQL queries against 3 mutations. The read surface is rich and typed; the write surface is not. Whatever writes exist run through a thin REST layer whose endpoint shapes never rendered, and remain uncaptured - a standing open item.

## Administration

*Observed · fact · source: `docs/features/administration/README.md`*

What the administration manual settles: All 57 admin tools classified with routes — 55 screenshotted, 22 with an owning doc. Import Data and Export Configuration are one "Messenger" subsystem; Firm and Client Drop Downs are two registries, not two views; Job Log and Report Log are one screen. Biggest open question: The five financial reference-data tools, then Manage Security.

## Manual contents

*Observed · fact · source: `docs/features/administration/README.md`*

The administration manual is organised as: The inventory; What the classification shows; Manage Firm Dictionary — every label in this corpus is tenant-overridable; Client Drop Downs — 38 firm-defined drop-downs; The three tools that were answering open questions — all now read. Read it rather than this node when you need the detail — this is the index.

## Data Fields

*Observed · fact · source: `docs/features/data-fields/README.md`*

What the data fields manual settles: 205 firm custom fields, 0 physical columns — 147 of them CAM clauses on Contract. Definitions are RGAF rows (IsGlobal + FirmID + IsClientExtensionField); the value store is unidentified. Three inventories of the schema, none complete, union 254 tables. Biggest open question: Where firm custom field values are written.

## Manual contents

*Observed · fact · source: `docs/features/data-fields/README.md`*

The data fields manual is organised as: Firm custom fields: 205 leaves, 0 columns; Global versus Firm; Required and ReadOnly; The catalog is not the whole schema; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Drop Downs Code Tables

*Observed · fact · source: `docs/features/drop-downs-code-tables/README.md`*

What the drop downs code tables manual settles: 207 identical code tables, 134 of them empty. delete is gated by a server-supplied isReadOnlyRecord, not a reference count — and the flag changed across a build upgrade, which corrects two claims in data-model/code-table-registry.md. Also: dependent drop-downs exist, via CustomCodeField.ParentCustomCodeFieldID. Biggest open question: Whether isReadOnlyRecord marks provenance — one BBW value sweep settles it.

## Manual contents

*Observed · fact · source: `docs/features/drop-downs-code-tables/README.md`*

The drop downs code tables manual is organised as: 134 of 207 tables are empty; What protects a value from deletion; The flag moved between builds; Inactive is present, and essentially unused; A naming trap worth stating plainly; Dependent drop-downs — an unnoticed feature; The contract lifecycle, and why it is still a problem; What a code-table value is made of; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Custom Lists

*Observed · fact · source: `docs/features/custom-lists/README.md`*

What the custom lists manual settles: A Custom List is a mini record type, not a picklist — and a Form without the workflow, differing only by CodeIssueType.IsWorkFlow. Attachability is 11 boolean columns including IsValidForEquipContract. Biggest open question: Whether list values are real columns on ClientListRow or EAV in SubValue*.

## Manual contents

*Observed · fact · source: `docs/features/custom-lists/README.md`*

The custom lists manual is organised as: Five custom lists in American Freight; A Custom List is a Form without the workflow; Where the rows live; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Reference Data

*Observed · fact · source: `docs/features/reference-data/README.md`*

What the reference data manual settles: The five reference tables. Four of five are empty in BBW — including the discount-rate table, while the ASC 842 engine runs. CPI holds 3,683 rows of one BLS series. The fiscal calendar supports 4-4-5 and 13-period retail years and extrapolates past the last defined year. Biggest open question: Where the ASC 842 discount rate actually comes from.

## Manual contents

*Observed · fact · source: `docs/features/reference-data/README.md`*

The reference data manual is organised as: Manage CPI Data — 3,683 rows, one index; Manage Discount Rates — the empty table that matters; Manage Exchange Rates — empty; Manage Fiscal Calendar — retail calendars, and a computed fallback; Manage Holiday Calendar — scheduling, not accounting; What these screens also prove about lists; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Evidence

*Observed · fact · source: `features/administration/README.md`*

Written up in features/administration/README.md, features/data-fields/README.md, features/drop-downs-code-tables/README.md, features/custom-lists/README.md, features/reference-data/README.md. 119 screen captures on disk, under docs/assets/screenshots/bbw-admin, docs/assets/screenshots/af-admin, docs/assets/screenshots/dashboard, docs/assets/screenshots/navigation — the screens themselves, not a description of them. First few: 01-manage-company.jpg, 02-manage-schedule-templates.jpg, 03-manage-milestone-timeline.jpg, 04-manage-binder-templates.jpg, 05-manage-forms.jpg, 06-manage-custom-lists.jpg.

![01-manage-company.jpg](../../assets/screenshots/bbw-admin/01-manage-company.jpg)
![02-manage-schedule-templates.jpg](../../assets/screenshots/bbw-admin/02-manage-schedule-templates.jpg)
![03-manage-milestone-timeline.jpg](../../assets/screenshots/bbw-admin/03-manage-milestone-timeline.jpg)
![04-manage-binder-templates.jpg](../../assets/screenshots/bbw-admin/04-manage-binder-templates.jpg)
![05-manage-forms.jpg](../../assets/screenshots/bbw-admin/05-manage-forms.jpg)
![06-manage-custom-lists.jpg](../../assets/screenshots/bbw-admin/06-manage-custom-lists.jpg)
![07-manage-parts-and-inventory.jpg](../../assets/screenshots/bbw-admin/07-manage-parts-and-inventory.jpg)
![08-manage-work-flows.jpg](../../assets/screenshots/bbw-admin/08-manage-work-flows.jpg)
![09-manage-page-layouts.jpg](../../assets/screenshots/bbw-admin/09-manage-page-layouts.jpg)
![10-manage-data-fields.jpg](../../assets/screenshots/bbw-admin/10-manage-data-fields.jpg)
![11-manage-dashboard-reports.jpg](../../assets/screenshots/bbw-admin/11-manage-dashboard-reports.jpg)
![12-import-data.jpg](../../assets/screenshots/bbw-admin/12-import-data.jpg)
![13-import-best-practice-templates.jpg](../../assets/screenshots/bbw-admin/13-import-best-practice-templates.jpg)
![14-export-configuration.jpg](../../assets/screenshots/bbw-admin/14-export-configuration.jpg)
![15-job-log.jpg](../../assets/screenshots/bbw-admin/15-job-log.jpg)
![16-manage-top-menu.jpg](../../assets/screenshots/bbw-admin/16-manage-top-menu.jpg)
![17-manage-firm-dictionary.jpg](../../assets/screenshots/bbw-admin/17-manage-firm-dictionary.jpg)
![18-manage-bid-package-templates.jpg](../../assets/screenshots/bbw-admin/18-manage-bid-package-templates.jpg)
![19-manage-budget-templates.jpg](../../assets/screenshots/bbw-admin/19-manage-budget-templates.jpg)
![20-manage-budget-views.jpg](../../assets/screenshots/bbw-admin/20-manage-budget-views.jpg)
![21-manage-budget-types.jpg](../../assets/screenshots/bbw-admin/21-manage-budget-types.jpg)
![22-manage-budget-summary-page.jpg](../../assets/screenshots/bbw-admin/22-manage-budget-summary-page.jpg)
![23-manage-budget-index-variables.jpg](../../assets/screenshots/bbw-admin/23-manage-budget-index-variables.jpg)
![24-manage-exchange-rates.jpg](../../assets/screenshots/bbw-admin/24-manage-exchange-rates.jpg)

## Open questions (37)

*Inferred · group*

37 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Does Security ever

*Inferred · question · source: `docs/modules/platform-tenancy/README.md`*

Does Security ever diverge from UserClassSecurity, or is the projection always a pure mirror? No screen renders Security directly (ShowObjectDetails.jsp shows it has no physical table) — confirming it requires reading the live effective-permission API response for a member and diffing it against their UserClassSecurity grants. Nobody has confirmed this. Recorded in modules/platform-tenancy/README.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### What does Region

*Inferred · question · source: `docs/modules/platform-tenancy/README.md`*

What does Region actually store beyond its one declared column? 12 referencing objects and 34 columns depend on a table the export describes almost not at all. A ShowObjectDetails.jsp pass on Region specifically (not yet done — see object-catalog.md open question 1) would settle this and directly unblocks AssigneeType's REGION1/REGION2 reading. Nobody has confirmed this. Recorded in modules/platform-tenancy/README.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Is Project a legacy

*Inferred · question · source: `docs/modules/platform-tenancy/README.md`*

**Is Project a legacy predecessor of ProjectEntity, a lightweight cross-system reference id, or something else entirely?** Unresolved in object-catalog.md open question 2 and inherited here unchanged — both objects are subtype_root-shaped and this module owns both. Nobody has confirmed this. Recorded in modules/platform-tenancy/README.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### What is EntityTemplate

*Inferred · question · source: `docs/modules/platform-tenancy/README.md`*

What is EntityTemplate actually a template *of*, given TemplateAudit references separate BudgetEntityTemplateID/FolderEntityTemplateID/TaskEntityTemplateID columns that don't obviously map to it? See data-model.md. Nobody has confirmed this. Recorded in modules/platform-tenancy/README.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Does the vendor s own

*Inferred · question · source: `docs/modules/platform-tenancy/README.md`*

**Does the vendor's own tenant model use physical database-per-tenant, or is FirmID a row-level discriminator over one shared schema?** The cluster JWT claim (host:tenant) is the only evidence pointing either way, and it's inferential. See tenancy-model.md — this is the single highest-leverage question for the ASG Edge+ architecture decision this folder feeds. Nobody has confirmed this. Recorded in modules/platform-tenancy/README.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Is Lx itself database

*Inferred · question · source: `docs/modules/platform-tenancy/tenancy-model.md`*

Is Lx itself database-per-tenant, schema-per-tenant, or row-discriminated by FirmID? The cluster JWT claim is the only lead. Nothing short of a second training tenant (to compare cluster values and infer whether they point at different physical databases) or a vendor architecture document would settle this from outside. Nobody has confirmed this. Recorded in modules/platform-tenancy/tenancy-model.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Does Location belong

*Inferred · question · source: `docs/modules/platform-tenancy/tenancy-model.md`*

Does Location belong in the ASG Edge+ Hub or the Spoke? Restated from project-entity.md §5.2 because it is this module's own open conflict, not a new one — Location is filed under facilities-locations, not here, but the Hub/Spoke boundary this module is meant to encode depends on resolving it. Nobody has confirmed this. Recorded in modules/platform-tenancy/tenancy-model.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Is FirmID s absence

*Inferred · question · source: `docs/modules/platform-tenancy/tenancy-model.md`*

**Is FirmID's absence from the 161 entity_scoped children a deliberate design (tenant isolation belongs one layer up, at the entity spine) or an artefact of the export missing an implicit tenant column enforced elsewhere** (e.g., a database-level row-security policy not visible in a schema dump)? If the latter, the "isolation is one join deep" reading in this document would be an underestimate of how seriously Lx treats it internally. Nobody has confirmed this. Recorded in modules/platform-tenancy/tenancy-model.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Does the Hub Spoke

*Inferred · question · source: `docs/modules/platform-tenancy/tenancy-model.md`*

**Does the Hub→Spoke publish/accept/fork mechanism the ASG Edge+ workspace index flags as unwritten have a Lx precedent?** ProjectEntity points at firm-global reference data (Complex, DMA, StateProvinceCountry) from what would be Spoke-side rows under either ADR-004 reading — meaning a Spoke database needs read access to Hub reference data on every entity read, which is exactly the mechanism the workspace index says is not yet designed. This is a concrete, evidenced case for that design problem, not a new finding — project-entity.md's own open question 6 raises it first. Nobody has confirmed this. Recorded in modules/platform-tenancy/tenancy-model.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Does UserClassSecurity

*Inferred · question · source: `docs/modules/platform-tenancy/udf-registry.md`*

**Does UserClassSecurity's three-column tree pointer (ReportGroupDataID / RootReportGroupDataID / SubReportGroupDataID) ever disagree with RGAF's own two-FK denormalised path** (ReportGroupDataID + ParentReportGroupDataID, per report-field-registry.md)? Both describe "where in the tree" but use different column names and, in UserClassSecurity's case, a third level. Unresolved without a live capture of a populated security grant. Nobody has confirmed this. Recorded in modules/platform-tenancy/udf-registry.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Is GlobalProperty used

*Inferred · question · source: `docs/modules/platform-tenancy/udf-registry.md`*

Is GlobalProperty used anywhere a rebuild needs to reproduce, or is it dead platform scaffolding? No screen in this corpus renders it directly. Nobody has confirmed this. Recorded in modules/platform-tenancy/udf-registry.md, under the Platform & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### What do the remaining

*Inferred · question · source: `docs/features/administration/README.md`*

What do the remaining undocumented tools do? The five reference-data tools are now written up in ../reference-data/. Next: Manage Security, Layout Changes and Manage Top Menu — see the table above. Nobody has confirmed this. Recorded in features/administration/README.md, under the Admin & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Is Manage Company the

*Inferred · question · source: `docs/features/administration/README.md`*

Is Manage Company the only place the 21 entitlement flags are set? af-firm-record.json captured 71 Firm fields and 21 entitlement flags from FirmEdit.jsp; whether a firm administrator can change them, or only read them, is unobserved — and it matters, because Allow Equipment Contracts? is Yes at AF while the root does not render. Nobody has confirmed this. Recorded in features/administration/README.md, under the Admin & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### What does Import Best

*Inferred · question · source: `docs/features/administration/README.md`*

What does Import Best Practice Templates import? A vendor-supplied starter configuration is the obvious reading, and if so it is the mechanism behind the "one ASG template set published per tenant" model found in ../page-layouts/. Inferred, untested. Nobody has confirmed this. Recorded in features/administration/README.md, under the Admin & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### What is Generate

*Inferred · question · source: `docs/features/administration/README.md`*

What is Generate Enterprise Report File? GenBaseReport.jsp. Unknown. Nobody has confirmed this. Recorded in features/administration/README.md, under the Admin & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Does Manage Firm

*Inferred · question · source: `docs/features/administration/README.md`*

Does Manage Firm Dictionary rename product-wide labels? Dictionary.jsp. If a firm can relabel platform terms, every label in this corpus is tenant-specific — which would be a significant caveat on the whole document set. Nobody has confirmed this. Recorded in features/administration/README.md, under the Admin & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Why is Manage

*Inferred · question · source: `docs/features/administration/README.md`*

Why is Manage Contracts an admin tool at all, when contracts are an end-user surface with 39 screens? Likely a bulk/administrative editor; unconfirmed. Nobody has confirmed this. Recorded in features/administration/README.md, under the Admin & Tenancy area. Until it is settled, anything built on the assumption is a guess.

### Run the provenance

*Inferred · question · source: `docs/features/drop-downs-code-tables/README.md`*

Run the provenance test. Sweep BBW's 207 code tables for values with their lxBOID and isReadOnlyRecord, exactly as af-code-table-actions.json did for AF. Matching ids + matching flags on protected rows confirms the hypothesis; tenant-local ids on deletable rows confirms the other half. One capture settles it. Not yet requested — worth queueing with bbw-tracker. Nobody has confirmed this. Recorded in features/drop-downs-code-tables/README.md, under the Drop Downs & Code Tables area. Until it is settled, anything built on the assumption is a guess.

### What sets

*Inferred · question · source: `docs/features/drop-downs-code-tables/README.md`*

What sets isReadOnlyRecord server-side? Not observable from the client. Needs the REST or GraphQL representation of a FirmCode record, if either exposes more than the four UI fields. Nobody has confirmed this. Recorded in features/drop-downs-code-tables/README.md, under the Drop Downs & Code Tables area. Until it is settled, anything built on the assumption is a guess.

### Did AI Abstracted

*Inferred · question · source: `docs/features/drop-downs-code-tables/README.md`*

Did AI Abstracted really change ownership in 26.09, or did the flag's meaning change? The two readings are not distinguishable from one tenant's before/after. Nobody has confirmed this. Recorded in features/drop-downs-code-tables/README.md, under the Drop Downs & Code Tables area. Until it is settled, anything built on the assumption is a guess.

### Where does contract

*Inferred · question · source: `docs/features/drop-downs-code-tables/README.md`*

Where does contract status actually live, given 2094 has three values and BRD-24 needs five? Best lead: open the firm-defined Lease Status drop-down and read its values. One click. Nobody has confirmed this. Recorded in features/drop-downs-code-tables/README.md, under the Drop Downs & Code Tables area. Until it is settled, anything built on the assumption is a guess.

### Are the 134 empty

*Inferred · question · source: `docs/features/drop-downs-code-tables/README.md`*

Are the 134 empty tables empty in BBW too? The BBW capture has names and ids but no values, so this is unknown. If BBW populates tables AF leaves empty, "empty" is a tenant fact, not a product fact — and the Hub/Spoke seeding decision changes with it. Nobody has confirmed this. Recorded in features/drop-downs-code-tables/README.md, under the Drop Downs & Code Tables area. Until it is settled, anything built on the assumption is a guess.

### Why do Issue Type Code

*Inferred · question · source: `docs/features/drop-downs-code-tables/README.md`*

Why do Issue Type Code and User Class Code lack an Inactive column? Two cases only. Nobody has confirmed this. Recorded in features/drop-downs-code-tables/README.md, under the Drop Downs & Code Tables area. Until it is settled, anything built on the assumption is a guess.

### What does the

*Inferred · question · source: `docs/features/drop-downs-code-tables/README.md`*

What does the portfolio scoping do at runtime — filter the drop-down's options, or only control which portfolios may use the table at all?. Nobody has confirmed this. Recorded in features/drop-downs-code-tables/README.md, under the Drop Downs & Code Tables area. Until it is settled, anything built on the assumption is a guess.

### Are custom list values

*Inferred · question · source: `docs/features/custom-lists/README.md`*

Are custom-list values real columns on ClientListRow, or EAV rows in SubValue*? The two readings above. One REST call decides it. Highest priority here — if it is real columns, a custom list is a DDL operation and inherits the database-per-tenant consequence described in ../data-fields/; if it is EAV, it does not. Nobody has confirmed this. Recorded in features/custom-lists/README.md, under the Custom Lists area. Until it is settled, anything built on the assumption is a guess.

### Why does ClientListRow

*Inferred · question · source: `docs/features/custom-lists/README.md`*

Why does ClientListRow carry procurement and budget columns (PartID, CostPerPart, PurchaseOrderLineSeqNum, BudgetLineItemID)? Either the object is shared with the parts/budget subsystem, or "custom list" originated as a line-item mechanism and was generalised. Nobody has confirmed this. Recorded in features/custom-lists/README.md, under the Custom Lists area. Until it is settled, anything built on the assumption is a guess.

### Can a custom list have

*Inferred · question · source: `docs/features/custom-lists/README.md`*

Can a custom list have a workflow? IsWorkFlow is the only difference from a Form, so structurally yes. Whether the Manage Custom Lists screen exposes the flag is unobserved. Nobody has confirmed this. Recorded in features/custom-lists/README.md, under the Custom Lists area. Until it is settled, anything built on the assumption is a guess.

### How many fields can a

*Inferred · question · source: `docs/features/custom-lists/README.md`*

How many fields can a list have? If reading 1 is right, five SubValue slots would be a hard cap — but Operating Expenses already shows 13 fields, which argues against it. Nobody has confirmed this. Recorded in features/custom-lists/README.md, under the Custom Lists area. Until it is settled, anything built on the assumption is a guess.

### Does BBW carry the

*Inferred · question · source: `docs/features/custom-lists/README.md`*

Does BBW carry the same five lists? The custom-list inventory has only ever been read at American Freight. BBW is the more advanced fork. Nobody has confirmed this. Recorded in features/custom-lists/README.md, under the Custom Lists area. Until it is settled, anything built on the assumption is a guess.

### Is the field prefix

*Inferred · question · source: `docs/features/custom-lists/README.md`*

~~Is the field prefix enforced or conventional?~~ Answered — conventional. The Edit fields modal on Client Request Log shows seven fields, five prefixed CRL_ and two (ModifiedByID, ModifiedDate) not, in the same list (screenshot above). Nothing enforces the namespace, which is exactly the defect a rebuild should not copy. Nobody has confirmed this. Recorded in features/custom-lists/README.md, under the Custom Lists area. Until it is settled, anything built on the assumption is a guess.

### Where does the ASC 842

*Inferred · question · source: `docs/features/reference-data/README.md`*

Where does the ASC 842 discount rate actually come from, given DiscountRate has no rows? Asset.DiscountRateOverride and the SLSummary equivalent are the candidates. **Highest priority** — it blocks the accounting rebuild. Nobody has confirmed this. Recorded in features/reference-data/README.md, under the Reference Data area. Until it is settled, anything built on the assumption is a guess.

### What is CPI month 0

*Inferred · question · source: `docs/features/reference-data/README.md`*

What is CPI month 0? Observed on the 2019 rows in both tenants. Probably an annual or average figure; unconfirmed. Nobody has confirmed this. Recorded in features/reference-data/README.md, under the Reference Data area. Until it is settled, anything built on the assumption is a guess.

### Why does the CPI

*Inferred · question · source: `docs/features/reference-data/README.md`*

Why does the CPI series stop at 2019, with a Published Date of 12/06/2019 on every row? Stale training data, or a real gap that would break any post-2019 index escalation?. Nobody has confirmed this. Recorded in features/reference-data/README.md, under the Reference Data area. Until it is settled, anything built on the assumption is a guess.

### What are the

*Inferred · question · source: `docs/features/reference-data/README.md`*

What are the Accounting Method and Use Type vocabularies on the discount-rate screen? Both are drop-downs; neither appears by those names among the 207 firm code tables. Nobody has confirmed this. Recorded in features/reference-data/README.md, under the Reference Data area. Until it is settled, anything built on the assumption is a guess.

### Does American Freight

*Inferred · question · source: `docs/features/reference-data/README.md`*

~~Does American Freight hold the same data?~~ Answered. AF's discount-rate table is also empty, and its CPI data is identical to BBW's — same index, same 3,683 rows, same published date. AF's exchange-rate, fiscal-calendar and holiday-calendar screens have not been read. **Re-link the AF screenshots once the in-progress re-capture lands**; the observations stand on the BBW captures plus team-lead's independent read. Nobody has confirmed this. Recorded in features/reference-data/README.md, under the Reference Data area. Until it is settled, anything built on the assumption is a guess.

### What does Weeks In

*Inferred · question · source: `docs/features/reference-data/README.md`*

What does Weeks In Quarter offer besides 4-4-5? Only the default was visible. 4-5-4 and 5-4-4 are the other standard retail patterns. Nobody has confirmed this. Recorded in features/reference-data/README.md, under the Reference Data area. Until it is settled, anything built on the assumption is a guess.

### Has any fiscal Year

*Inferred · question · source: `docs/features/reference-data/README.md`*

Has any fiscal Year Details ever been generated? The detail grid was empty for the selected year, so period rows may not exist at all — in which case fiscal-period accounting is configured but unexercised. Nobody has confirmed this. Recorded in features/reference-data/README.md, under the Reference Data area. Until it is settled, anything built on the assumption is a guess.

## Rules (16)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### Tenant isolation is — [PLT-R-001](../rules/PLT-R-001.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or one of its 9 subtype roots).**

|  |  |
|---|---|
| When it fires | Any tenant-scoped read or write |
| What it reads | `ProjectEntityID` on the record; `FirmID` on the `ProjectEntity` row it points at |
| The test | The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or one of its 9 subtype roots) |
| What it writes | The record carries no `FirmID` of its own. Tenant scoping must be enforced by joining to `ProjectEntity` and filtering on its `FirmID`, or not at all |

### FirmID is not a — [PLT-R-002](../rules/PLT-R-002.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**No `Firm ID` type exists among the declared FK types.**

|  |  |
|---|---|
| When it fires | Any code generator or ORM that maps Lx's declared `<Entity> ID` FK types to foreign keys |
| What it reads | The type vocabulary (`Facility ID`, `Contract ID`, `Employer ID`, …, and `FirmID` itself, typed `Text`) |
| The test | No `Firm ID` type exists among the declared FK types |
| What it writes | A schema-driven FK inference tool will silently miss the one relationship every row in the product ultimately has. Tenant references must be modelled deliberately, not discovered |

### ProjectEntityID — [PLT-R-003](../rules/PLT-R-003.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**The target architecture is database-per-tenant (one Spoke database per firm).**

|  |  |
|---|---|
| When it fires | Any migration of a `ProjectEntityID`-scoped record into a per-tenant Spoke database |
| What it reads | The record's `ProjectEntityID` |
| The test | The target architecture is database-per-tenant (one Spoke database per firm) |
| What it writes | `ProjectEntityID` must be retained — it is the intra-tenant partition and access-control unit (`LinkMemberProjectEntity`), not a tenant-scoping column being replaced. Only `FirmID`'s job (which physical database) is subsumed by the database boundary itself |

### A new ProjectEntity — [PLT-R-004](../rules/PLT-R-004.md)

*Observed · rule · source: `docs/modules/platform-tenancy/rules.md`*

**The new subtype needs a default setup-page-layout assignment, the same way the existing eleven do.**

|  |  |
|---|---|
| When it fires | Onboarding a new kind of ownable entity (a 12th subtype beyond the 11 `IsValidFor*` categories) |
| What it reads | `Firm`'s eleven `*SetupPageLayoutID` columns |
| The test | The new subtype needs a default setup-page-layout assignment, the same way the existing eleven do |
| What it writes | `Firm` gains a twelfth column. There is no lookup table of (subtype, default layout) pairs — the enumeration is baked into the tenant record's own schema |

### Global Firm scope is — [PLT-R-005](../rules/PLT-R-005.md)

*Observed · rule · source: `docs/modules/platform-tenancy/rules.md`*

**Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically.**

|  |  |
|---|---|
| When it fires | A tenant customises the field registry, or reads `GlobalProperty` |
| What it reads | `IsGlobal` + `FirmID` on `ReportGroupAvailableField`/`ReportGroupData`; `FirmID` alone on `GlobalProperty` |
| What it writes | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically |

### Security is a read — [PLT-R-006](../rules/PLT-R-006.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**Both declare the same 21 fields.**

|  |  |
|---|---|
| When it fires | Any permission check |
| What it reads | `UserClassSecurity` (has a physical table) and `Security` (does not) |
| The test | Both declare the same 21 fields |
| What it writes | `UserClassSecurity` is the editable grant; `Security` is what a rebuild's authorization service would compute and cache, never what an admin edits directly |

### A permission grant — [PLT-R-007](../rules/PLT-R-007.md)

*Observed · rule · source: `docs/modules/platform-tenancy/rules.md`*

**The grant is scoped to a whole page layout, a single field-registry leaf, a field-registry subtree, or a dashboard component — never more than one kind at a time, and the level (`SecurityLevelByteValue`) is one of `DEFAULT | NO_ACCESS | VIEW | EDIT | DELETE`.**

|  |  |
|---|---|
| When it fires | A `UserClassSecurity` row is created |
| What it reads | `PageLayoutID`, `ReportGroupAvailableFieldID`, `ReportGroupDataID`/`RootReportGroupDataID`/ `SubReportGroupDataID`, `DashboardComponentID` |
| What it writes | The grant is scoped to a whole page layout, a single field-registry leaf, a field-registry subtree, or a dashboard component — never more than one kind at a time, and the level (`SecurityLevelByteValue`) is one of `DEFAULT \| NO_ACCESS \| VIEW \| EDIT \| DELETE` |

### Region is a three — [PLT-R-008](../rules/PLT-R-008.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2).**

|  |  |
|---|---|
| When it fires | Workflow routing with `AssigneeType = REGION1 \| REGION2 \| MARKET` |
| What it reads | `ProjectEntity.RegionID`, `RootRegionID`, `SubRegionID`, `CodeMarketAreaID`, `CodeMarketTypeID` |
| The test | The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2) |
| What it writes | The scope resolves against this three-column region hierarchy on the entity, not against a separate routing table. `Region` itself declares almost none of this shape directly — see `PLT-R-009` |

### Region s real shape — [PLT-R-009](../rules/PLT-R-009.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**12 other objects reference `Region` across 34 columns.**

|  |  |
|---|---|
| When it fires | Any attempt to enumerate a region's own attributes (name, parent, level number) |
| What it reads | `Region`'s one declared field, `ProjectEntityID` |
| The test | 12 other objects reference `Region` across 34 columns |
| What it writes | A rebuild cannot fully specify the `Region` entity from this corpus alone; treat it as a known gap, not an empty table |

### Geography is two — [PLT-R-010](../rules/PLT-R-010.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly.**

|  |  |
|---|---|
| When it fires | Any address capture on `Facility`, `Location`, `Parcel`, `Project`, `ProjectEntity`, or a person/company record in `people-parties` |
| What it reads | `StateProvinceCountryID` → `StateProvinceCountry` (ISO Alpha-2/3 codes); `JurisdictionID` → `Jurisdiction` (adds `TaxRate1`/`TaxRate2`) |
| What it writes | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly |

### Exchange rates are — [PLT-R-011](../rules/PLT-R-011.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**The rate used for a calculation is whatever was captured effective as of a given date, not a re-derived live lookup — supports historical reporting without recomputation.**

|  |  |
|---|---|
| When it fires | A multi-currency Contract calculation |
| What it reads | `ExchangeRate.ContractID`, `ConversionRate`, `EffectiveDate` |
| What it writes | The rate used for a calculation is whatever was captured effective as of a given date, not a re-derived live lookup — supports historical reporting without recomputation |

### Two unreconciled — [PLT-R-012](../rules/PLT-R-012.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**162 of 223 objects carry the inline stamps (161 `ModifiedByID`, only 79 `CreatedByID`); it is unknown which objects also emit `AuditColumn` rows.**

|  |  |
|---|---|
| When it fires | Any change to a tracked field |
| What it reads | `AuditColumn`/`AuditTable` (explicit change log, keyed to the field-registry tree via `GroupID`/`SubGroupID`) and inline `CreatedByID`/`ModifiedByID` stamps present on most objects |
| The test | 162 of 223 objects carry the inline stamps (161 `ModifiedByID`, only 79 `CreatedByID`); it is unknown which objects also emit `AuditColumn` rows |
| What it writes | A rebuild inherits the same open question ASG Edge+'s own unresolved ADR-0020 (in-transaction audit vs. the ADR-0012 outbox) poses — Lx appears to run a version of both, unreconciled |

### Audit entries file — [PLT-R-013](../rules/PLT-R-013.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**"Group Name"/"Sub-Group" columns a user sees in an Audit Log screen are the same registry group/subgroup names used everywhere else field metadata is organised.**

|  |  |
|---|---|
| When it fires | An `AuditColumn` row is written |
| What it reads | `GroupID`, `SubGroupID` (typed `sTYPE_REPORT_GROUP_DATA`) |
| What it writes | "Group Name"/"Sub-Group" columns a user sees in an Audit Log screen are the same registry group/subgroup names used everywhere else field metadata is organised |

### Single field objects — [PLT-R-014](../rules/PLT-R-014.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture.**

|  |  |
|---|---|
| When it fires | Any attempt to fully specify `EntityTemplate`, `MapClientSchedule`'s peers, `Notify`, `ScratchPad`, `AuditTable`, `Region`, `LinkPEMemberCodeJobTitle`, or `LinkRegionManager` from this export alone |
| What it reads | Each declares ≤1 stored field (`MapClientSchedule` is the exception at 10) |
| What it writes | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture |

### TemplateAudit names — [PLT-R-015](../rules/PLT-R-015.md)

*Observed · rule · source: `docs/modules/platform-tenancy/rules.md`*

**A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here.**

|  |  |
|---|---|
| When it fires | A Budget, Entity, Folder, or Task template is applied to a `ProjectEntity` |
| What it reads | `TemplateAudit.BudgetEntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID`, `EntityTemplateID` |
| What it writes | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here |

### Project and — [PLT-R-016](../rules/PLT-R-016.md)

*Derived · rule · source: `docs/modules/platform-tenancy/rules.md`*

**Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open.**

|  |  |
|---|---|
| When it fires | Any decision about which object is the entity supertype |
| What it reads | Both objects are classified `subtype_root`-shaped by the same mechanical test; field counts (111 vs. 107) and Data-Fields leaf counts (6 vs. 170) disagree about which is "lightweight." |
| What it writes | Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open |
