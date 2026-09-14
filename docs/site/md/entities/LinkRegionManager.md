# LinkRegionManager

*1 fields · module: Platform & Tenancy · Postgres: `link_region_manager`*

Join table assigning a Member as manager of a Region, with a manager flag and operating-status inheritance.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 1 |
| Fields with a vendor definition | 0 of 1 inventoried |
| Physical tables | `link_region_manager` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_region_manager

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required: the two captures disagree

**Observed.** The field inventory marks 0 of this record's fields required; the Data Fields catalogue marks 5; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-014](../rules/PLT-R-014.md) | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |
| [PPL-R-011](../rules/PPL-R-011.md) | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup | Derived |
| [POR-R-009](../rules/POR-R-009.md) | Notification/routing needs to walk the org chart · `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) · Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a  | Inferred |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `link_region_manager.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
