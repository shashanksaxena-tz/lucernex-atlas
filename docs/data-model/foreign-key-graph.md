# The foreign-key graph

**Stated up front.** 972 of the 7,421 fields are FK-typed columns. 912 resolve to one of the 223
objects, forming **701 distinct object→object edges** plus 13 self-references. The graph is
extremely centralised: **two objects — `Member` and `ProjectEntity` — are each pointed at by 161 of
the other 222.** The next hub, `Contract`, is pointed at by 61. After the top 10, in-degree falls
below 13, and **167 of 223 objects have in-degree 0**.

That is not a flaw. It is what an aggregate-root model looks like when read from the FK direction:
children hold the pointer to their parent, so parents accumulate in-degree and children have none.
The in-degree-0 set is therefore *mostly* leaf/child tables — but it also contains the genuinely
disconnected subsystems, and separating the two is the useful part of this document (§4).

**Scope note.** Budgeting / Bid / Cost Tracking is out of scope by user decision (2026-09-10). Its
27 objects stay in this graph so the edge inventory is whole and the degrees are honest, but they
get no write-up: they are marked *out of scope* wherever they appear below. The excision is cheap —
**only 13 FK columns cross from in-scope objects into that module**, and 9 of them are the same
column (`BudgetTemplateID`, one per entity subtype). See §3.1.

The FK types themselves are **Observed** schema metadata, read off Lucernex's own View Object Model
tool ([`../admin/009-related-fields-and-data-model.md`](../admin/009-related-fields-and-data-model.md)).
The resolution of a type name to a target object is **Derived** where the names match and
**Inferred** where an alias was needed; every edge in
[`../mindmap/edges.json`](../mindmap/edges.json) carries its own `resolution` and `rationale`.

## 1. Edge inventory

| Measure | Count |
|---|---:|
| FK-typed columns | 972 |
| Resolved to one of the 223 objects | 912 |
| Unresolved | 60 |
| Distinct object→object edges (excluding self-loops) | 701 |
| Self-referencing columns | 13 |
| Distinct FK types | 60 |

### Resolution confidence

| Resolution | Columns | Meaning |
|---|---:|---|
| `high` | 819 | Type name matches an object name exactly after normalisation, or is corroborated by [009](../admin/009-related-fields-and-data-model.md) / a PK-type check / [`../data-fields/INDEX.md`](../data-fields/INDEX.md). |
| `medium` | 87 | Single-source naming or domain inference (e.g. `County ID` → `Jurisdiction`, because every such column is named `JurisdictionID`). |
| `low` | 6 | Best guess, flagged for follow-up (`Report/Form Field ID`, `Action ID`, `Folder Template Action ID`). |
| `unresolved` | 60 | No object matches — see §1.1. |

### 1.1 The 60 unresolved columns are not database FKs

| Type | Columns | Column names | Reading |
|---|---:|---|---|
| `item ID` | 56 | 54 are `*PageLayoutID` / `*LayoutID` / `*ReportGroupDataID`; 2 are `AuditColumn.GroupID`, `.SubGroupID` | Pointers into **configuration metadata** — Page Layouts, Report Groups, Data-Field groups (docs/admin/005–008), none of which is a business object in this export. The lower-case `item`, unique among 60 Title-Case FK types, marks it as a different kind of handle. **Derived**, high confidence. |
| `Custom Drop Down ID` | 2 | `CustomCodeField.CustomCodeTableID`, `.ParentCustomCodeTableID` | Points at Client Drop Down definitions (docs/admin/007), also configuration. |
| `DashboardComponent ID` | 2 | `Security.DashboardComponentID`, `UserClassSecurity.DashboardComponentID` | Points at dashboard configuration. |

All 60 point **out of the business-object model into the configuration model**. This is a finding
about the product's internal boundary, and it lands squarely on the ASG Edge+ Configuration-Service
scope line: business objects reference layouts and code lists by id, and those live somewhere else.

`Firm` alone holds 11 of the 56 `item ID` columns (`ContractSetupPageLayoutID`,
`FacilitySetupPageLayoutID`, `LocationSetupPageLayoutID`, `ParcelSetupPageLayoutID`,
`PrototypeSetupPageLayoutID`, `SiteSetupPageLayoutID`, `OpenProjectSetupPageLayoutID`,
`EquipmentContractSetupPageLayoutID`, `CapProjectSetupPageLayoutID`, …) — i.e. **the tenant record
itself names the default page layout for each entity type**, which is exactly the central
layout-push model of ASG Edge+ decision D-01.

## 2. The hubs — what a rebuild must model first

In-degree here means *how many distinct objects hold a typed FK to this one*, which is the honest
measure of "how many things break if you get this wrong".

| Rank | Object | Referencing objects | FK columns | Module | Why it is a hub |
|---:|---|---:|---:|---|---|
| 1 | `Member` | 161 | 290 | people-parties | Almost entirely audit: 240 of the 290 columns are `ModifiedByID` (161) or `CreatedByID` (79). One cross-cutting concern, not 161 relationships. |
| 2 | `ProjectEntity` | 161 | 163 | platform-tenancy | The universal entity spine. See [`project-entity.md`](project-entity.md). |
| 3 | `Contract` | 61 | 62 | contracts-leases | The lease aggregate root. `walkHierarchy.jsp` nests ~70 owned child tables under it (**Observed**, [009](../admin/009-related-fields-and-data-model.md)). |
| 4 | `Employer` | 30 | 40 | people-parties | The single company table behind landlord, tenant and vendor alike — `PaymentTransaction.VendorID` is typed `Employer ID` (**Observed**, [009](../admin/009-related-fields-and-data-model.md)). |
| 5 | `StateProvinceCountry` | 22 | 26 | platform-tenancy | Geography reference data, via the `Country, State, County ID` type. |
| 6 | `Jurisdiction` | 16 | 17 | platform-tenancy | Taxing authority, via the `County ID` type. |
| 7 | `Covenant` | 15 | 15 | contracts-leases | Surprisingly high — lease covenants are referenced across accounting, allowances and variable rent, not just from Contract. |
| 8 | `BudgetTemplate` | 14 | 14 | *out of scope* | — not analysed. Listed so the ranking is not silently wrong. |
| 9 | `ContractAmendment` | 13 | 13 | contracts-leases | Almost every contract child carries `AmendmentID` — amendments version the whole lease, not just the header. |
| 10 | `Asset` | 13 | 14 | assets-equipment | Via `Equipment ID`; assets are referenced from accounting and payments as well as maintenance. |
| 11 | `Region` | 12 | 34 | platform-tenancy | 34 columns from only 12 objects — `RegionID` / `RootRegionID` / `SubRegionID` appear together, so Region is a **hierarchy**. |
| 12 | `Complex` | 11 | 11 | facilities-locations | |
| 13 | `Prototype` | 11 | 11 | facilities-locations | |
| 14 | `Program` | 11 | 12 | portfolio-transactions | Reached via the `Portfolio ID` type (**Observed** mismatch, [009](../admin/009-related-fields-and-data-model.md)). |
| 15 | `TaskGroup` | 11 | 18 | projects-capital | Via `Task/Group ID`; self-referencing through `ParentTaskID`. |
| 16 | `ExpenseSetup` | 10 | 10 | accounting | The root of the expense-schedule generation chain. |
| 17 | `DMA` | 10 | 10 | facilities-locations | Designated Market Area — demographics reference data. |
| 18 | `Document` | 10 | 10 | documents-folders | |
| 19 | `Location` | 9 | 9 | facilities-locations | |
| 20 | `Organization` | 8 | 8 | platform-tenancy | |

`BudgetTemplate` (rank 8) is the only out-of-scope object inside the top 20. `BudgetColumnType`
also has in-degree 8, tying at the table's cut-off. Neither is analysed further.

**The build order this implies.** `ProjectEntity` + `Member` + `Firm` before anything (they are the
partition, identity and tenant), then `Employer`, `StateProvinceCountry`, `Jurisdiction`, `Region`,
`Organization` as reference data, then `Contract` with `ContractAmendment` and `Covenant`, then
`Facility`/`Location`/`Complex`/`Parcel`/`Prototype`, then everything else. Nothing below rank 20
constrains build order.

### Out-degree — the objects that reach furthest

| Object | Distinct targets | FK columns |
|---|---:|---:|
| `Contract` | 13 | 18 |
| `Parcel` | 13 | 18 |
| `PaymentTransactionFullImport` | 13 | 13 |
| `Issue` | 7 | 14 |
| `Project` | 11 | 14 |
| `RETransaction` | 8 | 14 |
| `Facility` | 10 | 13 |
| `Location` | 10 | 13 |
| `PaymentTransaction` | 12 | 13 |
| `PotentialProject` | 10 | 13 |
| `Program` | 9 | 13 |

The subtype roots (`Contract`, `Parcel`, `Facility`, `Location`, `Program`, `Project`,
`PotentialProject`, `Prototype`) dominate both lists — they are simultaneously the most-referenced
and the most-referencing objects, which is the signature of a hub-and-spoke schema rather than a
layered one.

### Self-references (13)

| Object | Column | Type | Reading |
|---|---|---|---|
| `Contract` | `MasterContractID` | `Contract ID` | Master-lease → sublease. **Observed** in [009](../admin/009-related-fields-and-data-model.md). |
| `Parcel` | `MasterParcelID` | `Parcel ID` | Parcel subdivision. |
| `TaskGroup` | `ParentTaskID` | `Task/Group ID` | Task tree. |
| `TaskGroup` | `TskPredVal_PredecessorTaskID` | `Task/Group ID` | Schedule predecessor link. |
| `Member` | `SupervisorID` | `Member ID` | Org chart. |
| `Member` | `ModifiedByID` | `Member ID` | Audit (a member modifies a member). |
| `Program` | `OrgChartProgramID` | `Portfolio ID` | Portfolio hierarchy. |
| `PaymentTransaction` | `AppliedToPayTranID` | `Payment Transaction ID` | Payment application/offset chain. |
| `RETransaction` | `RelatedTransactionID` | `RE Transaction ID` | Linked deals. |
| `CustomCodeField` | `ParentCustomCodeFieldID` | `Custom Field ID` | Nested custom lists. |
| `GlobalProperty` | `GlobalPropertySectionID` | `Global Property Section ID` | Property sectioning. |
| `WorkFlow` | `WorkFlowTemplateID` | `Work Flow ID` | Instance → template. Note the type is `Work Flow ID`, not `Work Flow Template ID` — template and instance share a table. |
| `WorkFlowStep` | `WorkFlowTemplateStepID` | `Step ID` | Same pattern one level down. |

The last two are a real modelling decision, not an oddity: **Lucernex stores workflow templates and
workflow instances in the same tables**, distinguished by whether the template pointer is set. ASG
Edge+ should decide this deliberately rather than inherit it.

## 3. Module dependency matrix

Modules and their assignment are defined in [`../mindmap/taxonomy.md`](../mindmap/taxonomy.md).
"Out" and "In" count FK columns crossing a module boundary.

| Module | Objects | Fields | Internal edges | Out | In | Depends most on |
|---|---:|---:|---:|---:|---:|---|
| `accounting` | 38 | 1,265 | 23 | 146 | 1 | people-parties (60), platform-tenancy (37), contracts-leases (30) |
| `contracts-leases` | 14 | 1,166 | 29 | 48 | 67 | platform-tenancy (19), people-parties (17), facilities-locations (5) |
| `facilities-locations` | 20 | 918 | 23 | 82 | 34 | platform-tenancy (40), people-parties (26), documents-folders (5) |
| `expense-recovery` | 3 | 618 | 0 | 13 | 0 | contracts-leases (5), people-parties (4), platform-tenancy (3) |
| `portfolio-transactions` | 11 | 513 | 12 | 66 | 10 | platform-tenancy (26), people-parties (17), facilities-locations (10) |
| `variable-rent` | 17 | 472 | 1 | 44 | 2 | contracts-leases (19), platform-tenancy (13), people-parties (12) |
| `projects-capital` | 23 | 376 | 11 | 62 | 8 | people-parties (35), platform-tenancy (21), assets-equipment (3) |
| `platform-tenancy` | 21 | 385 | 28 | 34 | **237** | people-parties (15), facilities-locations (9) |
| `people-parties` | 10 | 301 | 22 | 14 | **309** | platform-tenancy (13), contracts-leases (1) |
| `workflow` | 9 | 262 | 15 | 44 | 0 | people-parties (34), platform-tenancy (7), projects-capital (3) |
| `assets-equipment` | 8 | 230 | 1 | 29 | 13 | people-parties (24), platform-tenancy (3), contracts-leases (2) |
| `property-tax` | 6 | 163 | 5 | 28 | 2 | people-parties (16), facilities-locations (6), platform-tenancy (6) |
| `layouts-forms-reporting` | 6 | 107 | 3 | 13 | 2 | people-parties (8), platform-tenancy (3), assets-equipment (2) |
| `documents-folders` | 10 | 99 | 2 | 20 | 16 | platform-tenancy (13), people-parties (7) |
| **In-scope total** | **196** | **6,875** | **175** | | | |
| ~~`out-of-scope-cost-budget`~~ | ~~27~~ | ~~546~~ | ~~23~~ | ~~71~~ | ~~13~~ | **Excluded by user decision — listed for completeness only, not analysed.** |

Three things fall out of this:

1. **`platform-tenancy` and `people-parties` are pure sinks** (237 and 309 inbound, 34 and 14
   outbound). Everything depends on them; they depend on almost nothing. They are the foundation
   layer and must be built first.
2. **`workflow` and `expense-recovery` have zero inbound edges.** Nothing in the product points at
   a workflow or a recovery. They are terminal consumers — safely extractable as their own
   services, and safely built last.
3. **`variable-rent` has one internal edge across 17 objects.** Its cohesion comes almost entirely
   from `ContractID`, not from internal structure — because 7 of its 17 objects are `Virtual*`
   projections with no keys at all (§5).

### 3.1 The out-of-scope boundary is cheap to cut

Only **13 FK columns** point from an in-scope object into `out-of-scope-cost-budget`:

| Source | Column | Target | Count |
|---|---|---|---:|
| `ProjectEntity` and all 8 subtype roots (`Contract`, `Facility`, `Location`, `Parcel`, `Program`, `Project`, `PotentialProject`, `Prototype`) | `BudgetTemplateID` | `BudgetTemplate` | 9 |
| `Issue` | `BudgetColumnTypeID` ×2 | `BudgetColumnType` | 2 |
| `Security`, `UserClassSecurity` | `BudgetColumnTypeID` | `BudgetColumnType` | 2 |

Dropping the module therefore costs the in-scope model **one nullable column per entity subtype**
(the entity's default budget template) and **four permission/issue columns**. Traffic runs
overwhelmingly the other way — 71 columns point *out* of the module into in-scope objects, mostly
`ProjectEntityID` and `ModifiedByID`. That asymmetry is what makes this a clean excision rather than
a costly one, and it is worth recording in case the decision is ever revisited.

## 4. In-degree 0 — 167 objects, and what the zero actually means

Nothing holds a typed FK to 167 of the 223 objects. Sorting them by *why* is what makes the number
usable:

| Reason | Count | Examples | Rebuild reading |
|---|---:|---|---|
| **Owned child of an aggregate root** — holds `ProjectEntityID` or `ContractID` and is reached by composition, never by reference | 97 | `KeyDate`, `SecurityDeposit`, `Insurance`, `CoTenancy`, `Responsibility`, `AllowanceTransaction`, `Sales`, `TaskItem`, `IssueResponse` | Normal and expected. `walkHierarchy.jsp` nests ~70 of these under `Contract` alone (**Observed**, [009](../admin/009-related-fields-and-data-model.md)). Model as owned children. |
| **Computed projection** — no key at all | 13 | all `Virtual*` | Not tables. See §5. |
| **Import/integration projection** | 2 | `PaymentTransactionFullImport`, `WFStepFullImport` | Same shape as their base object. Do not rebuild as tables. |
| **Join/link table** | 18 | `Link*` | In-degree 0 by definition; edges point outward. |
| **Reference code list nothing FK-types to** | 11 | `CodeASC842Schedule`, `CodeIFRS16Schedule`, `CodeSLSchedule`, `CodeSalesGroup`, `CodeSalesType`, `CodeIssueType`, `CodeProblem`, `CodeResponsibleParty`, `CodeExpenseType`, `CodeAssetCategory`, `CodeBudgetColumnStatus` | These are reached through the **`Dropdown (…)` type**, not through an FK type — a second, parallel reference mechanism the FK graph cannot see. Do not read as dead. |
| **Standalone roots and candidate dead subsystems** | 26 | `Firm`, `Person`, `NonMember`, `Part`, `PartPackage`, `WorkFlowTemplate`, `WorkFlowTemplateStep`, `HolidaySchedule`, `Demographic*`, `Security`, `PotentialProject`, `Project`, … | Worth a decision — see below. |

### Candidate standalone or dead subsystems

| Object(s) | Fields | Why it looks standalone |
|---|---:|---|
| `LeaseInfo` | 219 | The third-largest object in the product. In-degree 0, and only **two** FK columns out. A very wide, almost edgeless read model of the lease. Either a reporting projection or a legacy pre-`Contract` table. **This is the single biggest open question in the catalog.** |
| `Competitor`, `DemographicFact`, `DemographicReport`, `DemographicResults`, `DemographicStudyArea`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection` | 227 combined | The whole site-selection/demographics subsystem is reachable only via `ProjectEntityID`. It is a coherent, self-contained module — the clean extraction candidate, and the one most likely out of scope for ASG Edge+. |
| `CommitteePackage`, `Notify`, `ScratchPad`, `LeaseAudit`, `IssueSubmittal`, `DocumentMarkup`, `EMailSentLog` | 1 each | One declared field, in-degree 0, no obvious consumer. Either truncated in the export or vestigial. |
| `ProcessTimeline`, `ProcessTimelineTemplate` | 41 | A second, parallel milestone mechanism alongside `Task`/`TaskGroup`/`KeyDate`. Three ways to express "a dated milestone" is a consolidation opportunity. |
| `MapClientSchedule`, `RecalcOverrideNotes`, `GlobalProperty` | 21 | Platform utility tables with no inbound references. |

## 5. The `Virtual*` family — computed projections, not tables

**Conclusion: they are computed projections (views or generated result sets), not persisted
tables. Confidence: high. Derived.**

The evidence is a clean, exceptionless signature across all 13:

| Test | `Virtual*` (13) | Every other object |
|---|---|---|
| Has a `<ObjectName>ID` primary-key column | **0 of 13** | 147 of 210 do |
| Has any audit column (`CreatedByID`, `CreatedDate`, `ModifiedByID`, `ModifiedDate`, `RevNumber`, `BOMapClientRecordID`) | **0 of 13** | 173 of 210 do |
| Has `BOMapClientRecordID` (the client-record integration key) | **0 of 13** | 141 of 210 do |

A persisted Lucernex table has a key and a modification stamp. Not one `Virtual*` object has
either. They are named `virtual_*` in the `PG TABLE` column, which for 12 of the 13 is a *declared
view name*; `VirtualSalesPeriod` names no table at all.

They split into three shapes:

| Shape | Objects | What it computes |
|---|---|---|
| **Period expansion** | `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForecastPeriod` (20), `VirtualExpAccrualForecastPeriod` (13) | Explodes a setup/schedule into a per-period grid. Always `ContractID` + `BeginDate`/`EndDate`/`Period`/`Year` + computed amounts. This is the calculation engine's output surface. |
| **Aggregate** | `VirtualPRPAggregate` (16), `VirtualUBRPAggregate` (14) | Rolls periods up to a rent-year total (`CurrentRentDue`, `CurrentRentObligation`, `CurrentRentPaid`). |
| **Template applicability** | `VirtualTemplateBudget` (17), `VirtualTemplateBudgetOption` (17), `VirtualTemplateFolder` (16), `VirtualTemplateSchedule` (16) | A union view over the four template tables. Each carries `TemplateID`, `TemplateName`, `Description` and the **same 11 `IsValidFor*` boolean flags**. |

Those 11 flags are independently valuable — they enumerate the product's entity types:
`IsValidForCapProgram`, `IsValidForCapProject`, `IsValidForContract`, `IsValidForEquipContract`,
`IsValidForFacility`, `IsValidForLocation`, `IsValidForOpenProject`, `IsValidForParcel`,
`IsValidForPortfolio`, `IsValidForPotentialProject`, `IsValidForPrototype`. That list corroborates
`walkHierarchy.jsp`'s aggregate-root dropdown almost exactly (**Observed**,
[009](../admin/009-related-fields-and-data-model.md)) and is used as evidence in
[`project-entity.md`](project-entity.md) §4.

**Rebuild consequence.** The 7 period-expansion views represent 246 fields of pure calculation
output. In ASG Edge+ they are not tables to migrate — they are the *specification of what the rent
calculation engine must produce*. Reading them as schema would be a serious mistake.

## 6. Objects with no physical table

Seven objects have an empty `PG TABLE` cell. They are not one thing:

| Object | Fields | Has PK | Has audit cols | Reading | Confidence |
|---|---:|---|---|---|---|
| `VirtualSalesPeriod` | 66 | no | no | Computed projection, like the other 12 `Virtual*` — but not even a view name is declared, so it is likely materialised in application code or by a stored procedure. | High (**Derived**) |
| `PaymentTransactionFullImport` | 118 | no | yes | Field-for-field identical in size to `PaymentTransaction` (118). An import/staging projection over the same physical table. | High (**Derived**) |
| `BudgetOptionTemplate` *(out of scope)* | 107 | no | yes | Carries `ProjectEntity`'s entire inherited column block. A denormalised `ProjectEntity` × `BudgetTemplate` join view — noted only because it is a false positive of the `subtype_root` test in [`project-entity.md`](project-entity.md) §2. | Medium (**Inferred**) |
| `Security` | 21 | no | yes | Effective-permission resolution over `CodeUserClassID`, `PageLayoutID`, `ReportGroupDataID`, `DashboardComponentID`, `SecurityLevelByteValue`. A computed access-control view, mirroring `UserClassSecurity` (which *does* have a table). | Medium (**Inferred**) |
| `BudgetColumnItemValue` *(out of scope)* | 19 | **yes** | yes | Has `BudgetColumnItemValueID`, `ModifiedByID`, `ModifiedDate` — the full persisted signature, but no table name. Most likely stored inside `budget_column` or a partition the export did not name. | Low — genuinely unexplained |
| `AuditColumn` | 14 | no | `CreatedByID`/`CreatedDate` only | A view over the audit log (`OldValue`, `NewValue`, `AuditAction`, `ScriptName`, `AccessorName`). Likely partitioned by date. | Medium (**Inferred**) |
| `BidPackageBreakout` *(out of scope)* | 4 | no | no | Four columns, all keys. A join view. | Medium (**Inferred**) |

**What an empty cell most likely means:** the object is exposed by the business-object layer but has
no single owning table — because it is a view, a projection over another object's table, or
partitioned. It does **not** mean the object is unused: `Security` and `BudgetOptionTemplate` are
both referenced elsewhere in the model.

## 7. `ExpenseRecovery` — 565 fields across four tables

`ExpenseRecovery` declares 565 fields and names four physical tables:
`expense_recovery_part1`, `expense_recovery_part2`, `expense_recovery_part3`,
`expense_recovery_part4`.

**The direct evidence for what the split is.** Parsing the field list finds `ExpenseRecoveryID`
repeated **exactly four times** and `ModifiedDate` repeated **exactly four times** — once per part.
That is the unmistakable signature of **1:1 vertical partitioning on a replicated primary key**: one
logical row shredded across four physical rows that must be joined back on every read.

**Why a platform does this.** Not for Postgres's sake — Postgres allows 1,600 columns. It is a
row-width limit: SQL Server caps a non-LOB row at 8,060 bytes and a table at 1,024 columns; Oracle
at 1,000 columns. 565 columns of `Currency`, `Date` and `Text` blows the 8,060-byte row limit
comfortably. **Inferred, but strongly**: the `part1..part4` naming is mechanical, carries no
semantic meaning, and is the classic workaround for a legacy SQL Server/Oracle origin — consistent
with Lucernex being a JSP application (`.jsp` routes throughout docs/admin/004–009) later ported to
Postgres, carrying its physical layout with it.

**Contrast with `Contract`.** `Contract` is 570 fields across four tables too, but the names are
*semantic*: `contract_admin`, `contract_financial`, `contract_firm`, `contract_firm1`. And
`ContractID` repeats only **three** times, not four. So `Contract`'s split is a deliberate
functional partition (administration / financials / tenant-custom) with `contract_firm1` as
overflow of the tenant-custom shard, while `ExpenseRecovery`'s is pure mechanical overflow.

**The `Contract` split carries a second, sharper finding:** **258 of `Contract`'s 570 fields are
`Firm_`-prefixed tenant-custom columns**, physically living in `contract_firm` / `contract_firm1`.
45% of the largest object in the product is one tenant's customisation, stored as real columns in
the core schema.

### Rebuild considerations

| Finding | Consequence for ASG Edge+ |
|---|---|
| A single logical entity spanning 4 tables joined 1:1 on every read | Do **not** port the partitioning. It is a workaround for a constraint Postgres does not have. Model `ExpenseRecovery` as one table, or — better — decompose it properly (565 columns is not a normalised entity; the `ABVariance*`/`Reported*`/`*Gross`/`*Net` column families are repeating groups that want to be rows). |
| 565 columns with repeating `*Gross`/`*Net` and `SubTotal1..n` families | This is a spreadsheet flattened into a table. The CAM-reconciliation domain model needs designing from the business rules, not transliterating from these columns. |
| Tenant-custom columns (`Firm_*`) physically merged into core tables | Directly contradicts database-per-tenant (ADR-004, `KnowledgeFolder/asg-edge-plus-kb/decisions/`). ASG Edge+'s Firm-scope Data Fields must **not** become columns on the platform's core tables. |
| Vertical partitioning is invisible above the data layer — the object model shows one 565-field object | Whatever ASG Edge+ chooses, the physical layout must not leak into the domain model the way it does here (the export literally shows `ExpenseRecoveryID` four times). |

## Open questions

1. **Is referential integrity enforced?** The FK *types* are declared, but nothing in this export
   shows whether the database has constraints. If not, migrated data may contain dangling
   references and ASG Edge+ cannot assume clean joins.
2. **What is `LeaseInfo`?** 219 fields, in-degree 0, two outbound FKs. Reporting projection, or a
   legacy table superseded by `Contract`? It is the third-largest object in the product and nothing
   in the corpus explains it.
3. **`item ID`'s physical target.** Confirmed to point at configuration metadata; the actual table
   is unknown. A `ShowObjectDetails.jsp` pass on `Firm` (11 such columns) would settle it.
4. **Do templates and instances really share tables?** `WorkFlow.WorkFlowTemplateID` typed
   `Work Flow ID` and `WorkFlowStep.WorkFlowTemplateStepID` typed `Step ID` say yes, but
   `WorkFlowTemplate` and `WorkFlowTemplateStep` also exist as separate objects with their own
   tables. Both cannot be the whole story.
5. **Three parallel milestone mechanisms** (`KeyDate`, `Task`/`TaskGroup`/`TaskItem`,
   `ProcessTimeline`). Are these genuinely different concepts, or accreted duplicates? This matters
   before ASG Edge+ builds any of them.
