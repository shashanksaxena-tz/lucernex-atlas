# GlobalProperty

*4 fields · module: Platform & Tenancy · Postgres: `global_property`*

A generic firm-scoped key/value configuration setting, organized by property section — a low-level settings-store table.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Fields with a vendor definition | 4 of 4 inventoried |
| Physical tables | `global_property` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 4 (4 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in global_property

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 4 fields carry a vendor definition

**Observed.** 4 of this record's 4 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 1; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-005](../rules/PLT-R-005.md) | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GlobalPropertySectionID` | Property Section | The ID of the global property section that the property belongs to. This field is not editable by end-users. | Global Property Section ID | Global |  | `global_property.GlobalPropertySectionID · TEXT` | [GlobalProperty](GlobalProperty.md) |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FirmID` |  | The record's Firm ID. | Text | Global |  | `global_property.FirmID · TEXT` |  |
| `PropertyKey` | Property Key | This field is used to override a global property value at the firm-level. This field is only usable by Accruent Administrators. | Text | Global | yes | `global_property.PropertyKey · TEXT` |  |
| `PropertyValue` | Property Value | This field is used to override a global property value at the firm-level. This field is only usable by Accruent Administrators. | Text | Global |  | `global_property.PropertyValue · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [GlobalProperty](GlobalProperty.md) | `GlobalPropertySectionID` |
