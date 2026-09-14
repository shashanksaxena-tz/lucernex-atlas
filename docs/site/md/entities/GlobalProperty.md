# GlobalProperty

*4 fields · module: Platform & Tenancy · Postgres: `global_property`*

A generic firm-scoped key/value configuration setting, organized by property section — a low-level settings-store table.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Catalogued fields | 4 (4 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-005](../rules/PLT-R-005.md) | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GlobalPropertySectionID` | Property Section | Global Property Section ID | Global |  | [GlobalProperty](GlobalProperty.md) |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FirmID` |  | Text | Global |  |  |
| `PropertyKey` | Property Key | Text | Global | yes |  |
| `PropertyValue` | Property Value | Text | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [GlobalProperty](GlobalProperty.md) | `GlobalPropertySectionID` |
