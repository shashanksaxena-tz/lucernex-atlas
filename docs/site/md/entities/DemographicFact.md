# DemographicFact

*10 fields · module: Facilities, Locations & Sites · Postgres: `demographic_fact`*

One data point within a demographic report, with an ordering sequence for display.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

## Fields

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeMarketDemographicsID` | Market Demographics | Dropdown (Market Demographics Code) | Global | yes | Market Demographics Code |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ComputedSequenceNumber` | Computed Sequence Number | Number | Global |  |  |
| `DemographicFactID` | Demographic Fact RecID | Number | Global |  |  |
| `ParentID` | Parent ID | Number | Global |  |  |
| `PreviousID` | Previous ID | Number | Global |  |  |
| `Weighting` |  | Number | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsOrdered` | Is Ordered? | Boolean | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `OrderRecordName` | Order Record Name | Text | Global |  |  |
| `OrderRecordType` | Order Record Type | Text | Global |  |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Demographic Fact ClientID | Text | Global | yes |  |
