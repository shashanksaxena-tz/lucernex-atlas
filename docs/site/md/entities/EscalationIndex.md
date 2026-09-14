# EscalationIndex

*12 fields · module: Lease Accounting & Payments · Postgres: `escalation_index`*

A named index value series (e.g., a specific published CPI series) used to drive ExpenseEscalation calculations.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 12 |
| Fields with a vendor definition | 12 of 12 inventoried |
| Physical tables | `escalation_index` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 12 (12 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in escalation_index

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 12 fields carry a vendor definition

**Observed.** 12 of this record's 12 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 2; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-042](../rules/CON-R-042.md) | The driver is index-based: rawChange = (IndexAmount / IndexBaseFactor) − 1 — assumes IndexAmount is a level, which is unconfirmed. | Inferred |

## Fields

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeIndexGroupID` | Index Group | Select the index group from this field. | Dropdown (Index Group Code) | Global |  | `escalation_index.CodeIndexGroupID · TEXT` | Index Group Code |
| `CodeIndexSourceID` | Index Source | Select the index source from this field. | Dropdown (Index Source Code) | Global |  | `escalation_index.CodeIndexSourceID · TEXT` | Index Source Code |
| `CodeIndexTypeID` | Index Type | Select the index type from this field. | Dropdown (Index Type Code) | Global |  | `escalation_index.CodeIndexTypeID · TEXT` | Index Type Code |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IndexAmount` | Index Amount | Enter the amount of the escalation index in this field. | Percentage | Global |  | `escalation_index.IndexAmount · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EscalationIndexID` | Escalation Index RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `escalation_index.EscalationIndexID · VARCHAR(64) NOT NULL` |  |
| `PeriodMonth` | Period Month | The period month. | Number | Global |  | `escalation_index.PeriodMonth · TEXT` |  |
| `PeriodYear` | Period Year | The period year. | Number | Global |  | `escalation_index.PeriodYear · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the index in this field. | Date | Global |  | `escalation_index.EffectiveDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EscalationIndexName` | Escalation Index Name | Enter the name of the escalation index in this field. | Text | Global | yes | `escalation_index.EscalationIndexName · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Escalation Index ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `escalation_index.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `escalation_index.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `escalation_index.ModifiedDate · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [ExpenseEscalation](ExpenseEscalation.md) | `EscalationIndexID` |
