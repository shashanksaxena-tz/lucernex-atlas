# LinkProjectEntityVendor

*4 fields · module: People & Parties · Postgres: `link_project_entity_vendor`*

Join table linking a ProjectEntity (portfolio) to an approved Vendor.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Catalogued fields | 4 (4 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-006](../rules/PPL-R-006.md) | Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` | Porfolio | Entity ID | Global | yes | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | Employer ID | Global | yes | [Employer](Employer.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkProjectEntityVendorID` | Link Portfolio Vendor RecID | Number | Global |  |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Link Portfolio Vendor ClientID | Text | Global | yes |  |
