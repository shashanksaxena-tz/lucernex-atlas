# Platform & Tenancy

*In scope for the rebuild*

The tenant/partition spine and cross-cutting platform plumbing: the Firm (tenant), the polymorphic ProjectEntity node every business record hangs off, geography and currency reference data, security, and audit scaffolding.

Stated up front. This module is not one thing in Lx's own admin taxonomy — it is the assembled scaffolding a multi-tenant, entity-polymorphic product needs underneath every other module: the tenant record (Firm), the universal entity spine (ProjectEntity, fully derived in ../../data-model/project-entity.md and cited, not repeated, throughout this folder), the permission ladder (Security/UserClassSecurity), shared geography (StateProvinceCountry/Jurisdiction), currency (ExchangeRate), the org-chart region hierarchy (Region), the per-entity roster join (LinkMemberProjectEntity), and a handful of audit and stub tables. 21 objects, 385 fields, captured 2026-09-10 from _lucernex_objects_summary.txt and the GraphQL schema, tenant (ASG)American Freight, build 26.08.0.46.

|  | Count |
|---|---|
| Record types | 21 |
| Fields | 385 |
| Keys in | 237 |
| Keys out | 34 |
| Rules | 16 |

## What was found here

### ProjectEntity is the spine, but not the tenant key

**Observed.** 163 foreign keys point at it and it is a declared interface in the GraphQL schema. It is the universal entity supertype — one row per thing you can own. The tenant key is FirmID; ProjectEntity partitions within a tenant.

### The tenant travels in the token

**Observed.** The session JWT carries firmname and a cluster claim shaped host:tenant — evidence that Lx routes each request to a tenant-specific database using a value inside the token.

### 448 field-type codes hide a 10-value system

**Observed.** The API's FieldType enum is BOOLEAN, COMPUTED, DATE, DATETIME, FK, FLOAT, INTEGER, MONEY, PERCENTAGE, STRING. COMPUTED and FK are first-class types — the platform distinguishes engine-calculated values from user input in its type system.

### Money is never a float

**Observed.** BigDecimal is a declared GraphQL scalar, and MONEY and PERCENTAGE are distinct from FLOAT. The vendor reached the same conclusion the rebuild's constitution mandates.

### One code-table registry, 207 entries

**Observed.** All Firm Drop Downs are values of a single TableType discriminator on one generic editor. TableType 2035 is Issue Type Code — which is why Manage Forms opens that same editor.

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Project](../entities/Project.md) | `project` | 111 | 0 |
| [ProjectEntity](../entities/ProjectEntity.md) | `project_entity` | 107 | 163 |
| [Security](../entities/Security.md) | `—` | 21 | 0 |
| [UserClassSecurity](../entities/UserClassSecurity.md) | `user_class_security` | 21 | 0 |
| [Firm](../entities/Firm.md) | `firm` | 18 | 0 |
| [TemplateAudit](../entities/TemplateAudit.md) | `template_audit` | 18 | 0 |
| [Organization](../entities/Organization.md) | `organization` | 17 | 8 |
| [AuditColumn](../entities/AuditColumn.md) | `—` | 14 | 0 |
| [Jurisdiction](../entities/Jurisdiction.md) | `jurisdiction` | 11 | 17 |
| [StateProvinceCountry](../entities/StateProvinceCountry.md) | `state_province_country` | 11 | 26 |
| [MapClientSchedule](../entities/MapClientSchedule.md) | `map_client_schedule` | 10 | 0 |
| [ExchangeRate](../entities/ExchangeRate.md) | `exchange_rate` | 8 | 0 |
| [LinkMemberProjectEntity](../entities/LinkMemberProjectEntity.md) | `link_member_project_entity` | 7 | 0 |
| [GlobalProperty](../entities/GlobalProperty.md) | `global_property` | 4 | 1 |
| [AuditTable](../entities/AuditTable.md) | `audit_table` | 1 | 0 |
| [EntityTemplate](../entities/EntityTemplate.md) | `entity_template` | 1 | 16 |
| [LinkPEMemberCodeJobTitle](../entities/LinkPEMemberCodeJobTitle.md) | `link_p_e_member_code_job_title` | 1 | 0 |
| [LinkRegionManager](../entities/LinkRegionManager.md) | `link_region_manager` | 1 | 0 |
| [Notify](../entities/Notify.md) | `notify` | 1 | 0 |
| [Region](../entities/Region.md) | `region` | 1 | 34 |
| [ScratchPad](../entities/ScratchPad.md) | `scratch_pad` | 1 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [PLT-R-001](../rules/PLT-R-001.md) | Tenant isolation is one join deep | The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or one of its 9 subtype roots) | Derived |
| [PLT-R-002](../rules/PLT-R-002.md) | `FirmID` is not a first-class reference type | No `Firm ID` type exists among the declared FK types | Derived |
| [PLT-R-003](../rules/PLT-R-003.md) | `ProjectEntityID` survives database-per-tenant; `FirmID` does not need to | The target architecture is database-per-tenant (one Spoke database per firm) | Derived |
| [PLT-R-004](../rules/PLT-R-004.md) | A new `ProjectEntity` subtype requires a new `Firm` column | The new subtype needs a default setup-page-layout assignment, the same way the existing eleven do | Observed |
| [PLT-R-005](../rules/PLT-R-005.md) | Global/Firm scope is a column, not a second schema | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically | Observed |
| [PLT-R-006](../rules/PLT-R-006.md) | `Security` is a read-only, computed shadow of `UserClassSecurity` | Both declare the same 21 fields | Derived |
| [PLT-R-007](../rules/PLT-R-007.md) | A permission grant targets exactly one of four surfaces | The grant is scoped to a whole page layout, a single field-registry leaf, a field-registry subtree, or a dashboard component — never more than one kind at a time, and the level (`SecurityLevelByteValu | Observed |
| [PLT-R-008](../rules/PLT-R-008.md) | Region is a three-level hierarchy resolved by `RegionID`/`RootRegionID`/`SubRegionID` | The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2) | Derived |
| [PLT-R-009](../rules/PLT-R-009.md) | `Region`'s real shape is not in this export | 12 other objects reference `Region` across 34 columns | Derived |
| [PLT-R-010](../rules/PLT-R-010.md) | Geography is two-level: country/state master, then jurisdiction | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/st | Derived |
| [PLT-R-011](../rules/PLT-R-011.md) | Exchange rates are point-in-time captures, not a live feed | The rate used for a calculation is whatever was captured effective as of a given date, not a re-derived live lookup — supports historical reporting without recomputation | Derived |
| [PLT-R-012](../rules/PLT-R-012.md) | Two unreconciled audit mechanisms coexist | 162 of 223 objects carry the inline stamps (161 `ModifiedByID`, only 79 `CreatedByID`); it is unknown which objects also emit `AuditColumn` rows | Derived |
| [PLT-R-013](../rules/PLT-R-013.md) | Audit entries file under the field-registry tree, not a separate taxonomy | "Group Name"/"Sub-Group" columns a user sees in an Audit Log screen are the same registry group/subgroup names used everywhere else field metadata is organised | Derived |
| [PLT-R-014](../rules/PLT-R-014.md) | Single-field objects rely entirely on a join or virtual pattern for content | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |
| [PLT-R-015](../rules/PLT-R-015.md) | `TemplateAudit` names four template kinds; this module owns one | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here | Observed |
| [PLT-R-016](../rules/PLT-R-016.md) | `Project` and `ProjectEntity` are both live, unreconciled candidates for "the spine" | Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open | Derived |
