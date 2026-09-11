# Platform & Tenancy — data model

**Stated up front.** 21 objects, 385 fields, source `_lucernex_objects_summary.txt` parsed by
[`../../mindmap/build_graph.py`](../../mindmap/build_graph.py) (**Derived**, machine-readable in
[`../../mindmap/objects.json`](../../mindmap/objects.json)). Internal edges (both endpoints in this
module): 28. Edges leaving the module: 34. Edges arriving from elsewhere: 237 — this module is
overwhelmingly a target, not a consumer, of the rest of the schema, which is exactly what "platform"
should mean. `people-parties` depends on it for 15 edges and is depended on by it for 13; the
detailed cross-module traffic is in [`README.md`](README.md#the-21-objects-by-role) and
[`tenancy-model.md`](tenancy-model.md).

## The 21 objects

| Object | Table | Fields | Spine role | In/Out FKs | What it is |
|---|---|---:|---|---:|---|
| `ProjectEntity` | `project_entity` | 107 | `supertype` | 161 / 12 | The universal entity spine. Full treatment: [`../../data-model/project-entity.md`](../../data-model/project-entity.md). |
| `Project` | `project` | 111 | `subtype_root` | 0 / 14 | A second, disputed "project identity" record — see [below](#project-vs-projectentity). |
| `Firm` | `firm` | 18 | `firm_global` | 0 / 1 | The tenant record — one row per Lucernex client firm. |
| `Security` | _(none)_ | 21 | `firm_global` | 0 / 3 | Computed effective-permission projection — see [below](#security-is-a-computed-shadow-of-userclasssecurity). |
| `UserClassSecurity` | `user_class_security` | 21 | `firm_global` | 0 / 3 | The real, editable permission-grant table `Security` projects from. |
| `StateProvinceCountry` | `state_province_country` | 11 | `firm_global` | 22 / 1 | Master geography — ISO Alpha-2/3 codes, backs every address block platform-wide. |
| `Jurisdiction` | `jurisdiction` | 11 | `firm_global` | 16 / 3 | Tax/legal jurisdiction reference, referenced by Facility/Parcel/Location address blocks. |
| `ExchangeRate` | `exchange_rate` | 8 | `firm_global` | 0 / 1 | A point-in-time currency rate captured per Contract. |
| `Region` | `region` | 1 | `entity_scoped` | 12 / 1 | The org-chart region hierarchy — see [`README.md`](README.md#the-third-finding). |
| `LinkRegionManager` | `link_region_manager` | 1 | `entity_scoped` | 0 / 1 | Assigns a Member as manager of a Region. |
| `LinkMemberProjectEntity` | `link_member_project_entity` | 7 | `entity_scoped` | 0 / 3 | The per-entity roster join — full field table in [`routing-and-approvals.md` §4](../workflow/routing-and-approvals.md#4-the-entity-roster--how-a-job-title-becomes-a-person). |
| `LinkPEMemberCodeJobTitle` | `link_p_e_member_code_job_title` | 1 | `entity_scoped` | 0 / 1 | Join between a `LinkMemberProjectEntity` assignment and a job-title code; internal-id-only. |
| `Organization` | `organization` | 17 | `firm_global` | 8 / 1 | Parent-company/franchise-group record above `Employer` — see the [boundary note](README.md#a-boundary-note-organization-reads-like-a-party-but-the-taxonomy-files-it-here). |
| `AuditColumn` | _(none)_ | 14 | `entity_scoped` | 0 / 2 | One logged field-change row: which column, old/new value, who, when. |
| `AuditTable` | `audit_table` | 1 | `entity_scoped` | 0 / 1 | Header row naming the table a batch of `AuditColumn` rows belongs to. |
| `TemplateAudit` | `template_audit` | 18 | `entity_scoped` | 0 / 7 | Change history for when a Budget/Entity/Folder template was applied to an entity. |
| `GlobalProperty` | `global_property` | 4 | `firm_global` | 0 / 1 | A generic Firm-scoped key/value settings row. |
| `EntityTemplate` | `entity_template` | 1 | `entity_scoped` | 4 / 1 | A single-field stub for a reusable entity-setup template. |
| `MapClientSchedule` | `map_client_schedule` | 10 | `entity_scoped` | 0 / 3 | Links a real-estate transaction/schedule to auto-push forecast behaviour. |
| `Notify` | `notify` | 1 | `entity_scoped` | 0 / 1 | A single-field stub for a fired notification instance. |
| `ScratchPad` | `scratch_pad` | 1 | `entity_scoped` | 0 / 1 | Free-form scratch-note store. |

Full per-object field lists (types included) were extracted directly from
`_lucernex_objects_summary.txt` for this pass; the four richest are reproduced below because they
carry this module's actual findings. The remaining thin objects (≤10 fields) are exhaustively listed
in the table above — there is nothing left to add.

## `Firm` — the tenant record, and its one-column-per-subtype pattern

**Observed**, 18 fields:

| Field | Type | Note |
|---|---|---|
| `ContractSetupPageLayoutID` | item ID | |
| `FacilitySetupPageLayoutID` | item ID | |
| `LocationSetupPageLayoutID` | item ID | |
| `ParcelSetupPageLayoutID` | item ID | |
| `PrototypeSetupPageLayoutID` | item ID | |
| `SiteSetupPageLayoutID` | item ID | |
| `OpenProjectSetupPageLayoutID` | item ID | |
| `EquipmentContractSetupPageLayoutID` | item ID | |
| `CapProjectSetupPageLayoutID` | item ID | |
| `CapProgramSetupPageLayoutID` | item ID | |
| `PortfolioSetupPageLayoutID` | item ID | |
| `CodeDefaultFolderSecurityID` | Dropdown (Security Type Code) | |
| `CurrentDate` | Current Date | |
| `Firm_HeaderLogo` | Text | |
| `JSONConfigText` | Text | Free-form tenant config blob |
| `SvcChannelFirmID` | Text | |
| `ModifiedByID` / `ModifiedDate` | Member ID / Time | |

**Derived** (corroborating `project-entity.md` §3): eleven of `Firm`'s eighteen fields are
`*SetupPageLayoutID` columns, one per `ProjectEntity` subtype (`Contract`, `Facility`, `Location`,
`Parcel`, `Prototype`, `Site`↔`PotentialProject`, `Opening Project`↔`Project`, `Equipment Contract`,
`Capital Project`, `Capital Program`, `Portfolio`↔`Program`). This is the same enumerable-subtype
signature `project-entity.md` §3 found in the `IsValidFor*` flags, now on the tenant record itself:
**a new subtype requires a new column on `Firm`**, not a row in a lookup table. That is a concrete
extensibility cost the ASG Edge+ rebuild does not have to inherit — see
[`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md).

`FirmID` itself — the tenant key — is **not a column on `Firm`** in this export; it is carried on
`ProjectEntity` and the nine subtype roots (`project-entity.md` §4). `Firm`'s own identity is
implicit: one row exists per tenant and nothing in this export names its own primary key column.
**Open question**, folded into `tenancy-model.md`.

## `Security` is a computed shadow of `UserClassSecurity`

**Derived**, high confidence — an exhaustive field-list diff. Both objects declare exactly these 21
fields, same names, same declared types:

`BOMapClientRecordID`, `BudgetColumnTypeID`, `CodeSecurityPrivilegeID`, `CodeUserClassID`,
`DashboardComponentID`, `DashboardComponentTitle`, `GroupHierarchy`, `GroupHierarchyNoPrefix`,
`ModifiedByID`, `ModifiedDate`, `PageLayoutID`, `ParentGroupName`, `ReportGroupAvailableFieldID`,
`ReportGroupDataID`, `RootReportGroupDataID`, `SecurityLevelByteValue`, `SecurityLevelName`,
`SecurityObjectNameText`, `SecurityType`, `SubReportGroupDataID`, `UserClassSecurityID`.

`Security` names no physical table in the export (`_(none)_`); `UserClassSecurity` names
`user_class_security`. **Derived: `Security` is the read-only, live-evaluated view;
`UserClassSecurity` is the row an administrator actually edits.** The columns themselves are the
whole permission grammar: a grant is `CodeUserClassID` × one of {`PageLayoutID`,
`ReportGroupAvailableFieldID` (a single field), `ReportGroupDataID`/`RootReportGroupDataID`/
`SubReportGroupDataID` (a field-registry subtree — see
[`udf-registry.md`](udf-registry.md)), `DashboardComponentID`} → `SecurityLevelByteValue`, drawn from
the GraphQL `SecurityLevel` enum `[DEFAULT, NO_ACCESS, VIEW, EDIT, DELETE]`
(**Observed**, [`../../data-model/graphql-api.md`](../../data-model/graphql-api.md)). Full detail on
how field-level security composes with the field registry is in
[`../reporting/report-field-registry.md`](../reporting/report-field-registry.md), which this module
does not restate.

## `Region` — a near-empty table twelve objects depend on

**Observed**: `Region` declares exactly one field, `ProjectEntityID(Entity ID)`. **Derived**: 12
distinct objects carry an FK naming `Region` across 34 columns
(`RegionID`, `RootRegionID`, `SubRegionID` — the three-deep region hierarchy repeated on
`ProjectEntity` itself and on `Project`, `TaskGroup`, and others). `LinkRegionManager` assigns a
`Member` as a region's manager. This is the physical structure behind the workflow engine's
`AssigneeType` enum values `REGION1`/`REGION2`/`MARKET`
([`../workflow/routing-and-approvals.md` §2](../workflow/routing-and-approvals.md#2-three-competing-routing-vocabularies-reconciled)):
a region is a real, hierarchical, three-level entity-scoping structure, but this schema dump
describes almost none of its own shape. See [`object-catalog.md`'s open question
1](../../data-model/object-catalog.md#open-questions) — `Region` is one of the 18 one-field objects
whose real content must live in a view or computed projection the export does not surface.

## The template family

`EntityTemplate` (1 field), `TemplateAudit` (18 fields) sit in this module; their siblings
`BudgetTemplate`, `FolderTemplate`, `TaskTemplate` and the four `VirtualTemplate*` projections that
surface their actual content live in other modules (`out-of-scope-cost-budget`,
`documents-folders`, `projects-capital`). `TemplateAudit`'s own fields —
`BudgetEntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID`, plus
`EntityTemplateID` itself — name **four** template kinds, of which `EntityTemplate` is only one and
the export gives it no more shape than its own FK column. **Open question**, carried from
`README.md`.

## `Project` vs `ProjectEntity`

**Unresolved, inherited from [`object-catalog.md`](../../data-model/object-catalog.md#open-questions)
question 2 without new evidence.** `Project` (111 fields) and `ProjectEntity` (107 fields) are both
classified `subtype_root` by the same mechanical test (a `ProjectEntityID` typed `Number`, not
`Entity ID`), both carry near-identical field blocks (phase-status pairs, region hierarchy,
denormalised address, `EntityId`/`EntityEmail`/`EntityPhoto`), and `INDEX.md` calls `Project` "a
lightweight project identity record… distinct from the richer `ProjectEntity`" while reporting only
6 Manage Data Fields leaves for it against 170 for `ProjectEntity`. Both objects are filed in this
module because neither's field list resolves the question of which is the real spine and which is
the legacy or cross-system-reference shadow. Do not build against either reading without opening
`ShowObjectDetails.jsp` on `Project` directly.

## Cross-module traffic

| Direction | Module | Edges | What crosses |
|---|---|---:|---|
| depends on → | `people-parties` | 15 | `LinkMemberProjectEntity.MemberID`, `Firm`/`ProjectEntity`/audit `*ByID` columns → `Member` |
| depends on → | `facilities-locations` | 9 | Address/jurisdiction lookups |
| ← depended on by | `facilities-locations` | 40 | Every `ProjectEntity` subtype's shared column block |
| ← depended on by | `accounting` | 37 | `ExchangeRate`, `FiscalPeriod`-adjacent, audit stamps |
| ← depended on by | `people-parties` | 13 | `Member.SupervisorID`↔org chart, `LinkMemberProjectEntity` |
| ← depended on by | 9 more modules | 1–33 each | Overwhelmingly `ProjectEntityID`/`*ByID` audit-stamp traffic |

Full per-module edge counts: [`../../mindmap/modules.json`](../../mindmap/modules.json) →
`platform-tenancy`. **Derived.**
