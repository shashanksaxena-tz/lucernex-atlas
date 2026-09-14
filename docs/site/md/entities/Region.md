# Region

*1 fields · module: Platform & Tenancy · Postgres: `region`*

A geographic region in the portfolio hierarchy — parent/previous region linkage and operating status, referenced by LinkRegionManager and LinkRegionMarket.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 1 |
| Fields with a vendor definition | 0 of 1 inventoried |
| Physical tables | `region` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 34 keys from 12 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 5 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### A hub: 34 keys point here

**Observed.** 12 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to BudgetOptionTemplate, Contract, DemographicReport, DevelopmentSlot and 8 others.

### Lands in region

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required: the two captures disagree

**Observed.** The field inventory marks 0 of this record's fields required; the Data Fields catalogue marks 3; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-008](../rules/PLT-R-008.md) | The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2) | Derived |
| [PLT-R-009](../rules/PLT-R-009.md) | 12 other objects reference `Region` across 34 columns | Derived |
| [PLT-R-014](../rules/PLT-R-014.md) | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |
| [POR-R-002](../rules/POR-R-002.md) | Workflow routing needs a `REGION1`/`REGION2` assignee · `Program.RegionID` / `RootRegionID` / `SubRegionID` → `Region` · Resolves an org-chart position through the region hierarchy. `MARKET` resolves through `CodeMarketAreaID` instead, a di | Inferred |
| [POR-R-009](../rules/POR-R-009.md) | Notification/routing needs to walk the org chart · `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) · Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a  | Inferred |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `region.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

## What points here (34 keys)

| Record type | Via column |
|---|---|
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [Contract](Contract.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [DevelopmentSlot](DevelopmentSlot.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [Facility](Facility.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [Location](Location.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [Parcel](Parcel.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [PotentialProject](PotentialProject.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [Program](Program.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [Project](Project.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [ProjectEntity](ProjectEntity.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [Prototype](Prototype.md) | `RegionID`, `RootRegionID`, `SubRegionID` |
| [DemographicReport](DemographicReport.md) | `RegionID` |
