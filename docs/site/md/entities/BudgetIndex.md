# BudgetIndex

*6 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_index`*

A named escalation index (e.g., a cost inflation index) applied to capital budgets, the header record for BudgetIndexValue.

Source: `data-fields/budget-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
| Fields with a vendor definition | 6 of 6 inventoried |
| Physical tables | `budget_index` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 6 (6 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in budget_index

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 6 fields carry a vendor definition

**Observed.** 6 of this record's 6 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 2; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetIndexID` | Budget Index RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `budget_index.BudgetIndexID · VARCHAR(64) NOT NULL` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetIndexName` | Budget Index Name | Enter the name of your budget index in this field. | Text | Global | yes | `budget_index.BudgetIndexName · TEXT` |  |
| `Description` | Budget Index Description | Write a description of the record. | Text | Global |  | `budget_index.Description · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Index ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `budget_index.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `budget_index.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `budget_index.ModifiedDate · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [BudgetIndexValue](BudgetIndexValue.md) | `BudgetIndexID` |
