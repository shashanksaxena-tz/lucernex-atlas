# BudgetOption

*13 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_option`*

A selectable alternative version of a budget-column entity type.

Source: `data-fields/budget-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Fields with a vendor definition | 12 of 13 inventoried |
| Physical tables | `budget_option` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 12 (12 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in budget_option

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 12 fields carry a vendor definition

**Observed.** 12 of this record's 13 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 5 of this record's fields required; the Data Fields catalogue marks 5; 5 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetOptionTemplateID` | Budget Option Template | Select the budget option template from this field. | Entity ID | Global | yes | `budget_option.BudgetOptionTemplateID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `CreatedByMemberID` | Created By Member | The member ID of the user who applied the budget option template. | Member ID | Global | yes | `budget_option.CreatedByMemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `budget_option.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetOptionID` | Budget Option RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `budget_option.BudgetOptionID · VARCHAR(64) NOT NULL` |  |
| `BudgetOptionTemplatePEID` | Budget Option Template PEID | The project entity ID of the budget template that the budget option is related to. | Number | Global |  | `budget_option.BudgetOptionTemplatePEID · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BotEntityType` | Bot Entity Type | This is an internal field that identifies the record as a budget option template. | Text | Global | yes | `budget_option.BotEntityType · TEXT` |  |
| `BudgetColumnID` | Budget Column | The ID of the budget type at the budget option was applied to. | Text | Global | yes | `budget_option.BudgetColumnID · TEXT` |  |
| `BudgetOptionName` | Budget Option Name | The budget option name. | Text | Global |  | `budget_option.BudgetOptionName · TEXT` |  |
| `InitializedFromBudgetColumnID` | Initialized From Budget Column | Select the budget template this budget option should be based upon from this field. | Text | Global |  | `budget_option.InitializedFromBudgetColumnID · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Option ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `budget_option.BOMapClientRecordID · TEXT` |  |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `budget_option.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `budget_option.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `budget_option.ModifiedDate · TEXT` |  |
