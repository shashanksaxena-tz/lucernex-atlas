# LinkRegionManager

*1 fields · module: Platform & Tenancy · Postgres: `link_region_manager`*

Join table assigning a Member as manager of a Region, with a manager flag and operating-status inheritance.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 1 |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-014](../rules/PLT-R-014.md) | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |
| [PPL-R-011](../rules/PPL-R-011.md) | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup | Derived |
| [POR-R-009](../rules/POR-R-009.md) | Notification/routing needs to walk the org chart · `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) · Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a  | Inferred |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
