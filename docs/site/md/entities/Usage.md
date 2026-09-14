# Usage

*14 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `usage`*

A recorded consumption/usage reading against a contract on a given posting date, feeding usage-based rent calculations.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 14 |
| Fields with a vendor definition | 13 of 14 inventoried |
| Physical tables | `usage` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in usage

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 13 fields carry a vendor definition

**Observed.** 13 of this record's 14 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 1 field marked required

**Observed.** The inventory marks 1 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-077](../rules/CON-R-077.md) | Usage-based rent is computed: structurally identical to the percentage-rent tiering with Sales→Usage and PRP→UBRP; the tier value is a unit cost, not a percentage rate. | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `usage.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `usage.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeUsageCategoryID` | Usage Category | Select the usage category from this field. The default categories are Actual and Forecast. The system will not generate transactions for usage history records with a category of Forecast. | Dropdown (Usage Category Code) | Global |  | `usage.CodeUsageCategoryID · TEXT` | Usage Category Code |
| `CodeUsageGroupID` | Usage Group | Select the usage group from this field. A Usage Group will be used with one and only one Model Type. The model type of a usage group will impact how your use based rent is calculated. | Dropdown (Usage Group Code) | Global |  | `usage.CodeUsageGroupID · TEXT` | Usage Group Code |
| `CodeUsageTypeID` | Usage Type | Select the usage type from this field. | Dropdown (Usage Type Code) | Global |  | `usage.CodeUsageTypeID · TEXT` | Usage Type Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | This field can be used to create custom unit types for count-based usage groups. | Dropdown (Usage Unit Type Code) | Global |  | `usage.CodeUsageUnitTypeID · TEXT` | Usage Unit Type Code |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `UsageShare` | Usage Share | Enter the usage share for the period in this field. | Percentage | Global |  | `usage.UsageShare · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `UsageCount` | Usage Count | Enter the usage count for the period in this field. | Number | Global |  | `usage.UsageCount · TEXT` |  |
| `UsageID` | Usage RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `usage.UsageID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the usage record in this field. | Date | Global |  | `usage.EffectiveDate · TEXT` |  |
| `PostingDate` | Posting Date | The date that the usage number is entered. | Date | Global |  | `usage.PostingDate · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Usage ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `usage.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `usage.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `usage.ModifiedDate · TEXT` |  |
