# DemographicFact

*10 fields · module: Facilities, Locations & Sites · Postgres: `demographic_fact`*

One data point within a demographic report, with an ordering sequence for display.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Fields with a vendor definition | 6 of 10 inventoried |
| Physical tables | `demographic_fact` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in demographic_fact

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 6 fields carry a vendor definition

**Observed.** 6 of this record's 10 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeMarketDemographicsID` | Market Demographics |  | Dropdown (Market Demographics Code) | Global | yes | `demographic_fact.CodeMarketDemographicsID · TEXT` | Market Demographics Code |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComputedSequenceNumber` | Computed Sequence Number | The sequence number of the record. Each new record receives the next number in the sequence. | Number | Global |  | `demographic_fact.ComputedSequenceNumber · TEXT` |  |
| `DemographicFactID` | Demographic Fact RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `demographic_fact.DemographicFactID · VARCHAR(64) NOT NULL` |  |
| `ParentID` | Parent ID |  | Number | Global |  | `demographic_fact.ParentID · TEXT` |  |
| `PreviousID` | Previous ID |  | Number | Global |  | `demographic_fact.PreviousID · TEXT` |  |
| `Weighting` |  |  | Number | Global |  | `demographic_fact.Weighting · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsOrdered` | Is Ordered? | This field does not impact any current functionality. | Boolean | Global |  | `demographic_fact.IsOrdered · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `OrderRecordName` | Order Record Name | This field does not impact any current functionality. | Text | Global |  | `demographic_fact.OrderRecordName · TEXT` |  |
| `OrderRecordType` | Order Record Type | This field does not impact any current functionality. | Text | Global |  | `demographic_fact.OrderRecordType · TEXT` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Demographic Fact ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `demographic_fact.BOMapClientRecordID · TEXT` |  |
