# FinancialAdjustment

*19 fields · module: Lease Accounting & Payments · Postgres: `financial_adjustment`*

A manual dollar adjustment to an Asset's or Contract's financial position — accounting adjustment type and amount. 18 Global fields under Contract.

Source: `data-fields/financial-adjustment.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Fields with a vendor definition | 18 of 19 inventoried |
| Physical tables | `financial_adjustment` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 18 (18 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in financial_adjustment

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 18 fields carry a vendor definition

**Observed.** 18 of this record's 19 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Asset | The asset ID of the associated equipment asset. | Equipment ID | Global | yes | `financial_adjustment.AssetID · TEXT` | [Asset](Asset.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `financial_adjustment.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `financial_adjustment.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `financial_adjustment.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Asset Associated Entity | This is a reporting field that returns data about the asset associated with the entity. | Entity | Global |  | `financial_adjustment.AssetAssociatedProjectEntityID · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAccountingAdjustmentTypeID` | Accounting Adjustment Type | Select the accounting adjustment type from this field. The available options are Cancellation Option, Residual Value Guarantee, and Purchase Option. | Dropdown (Accounting Adjustment Type Code) | Global |  | `financial_adjustment.CodeAccountingAdjustmentTypeID · TEXT` | Accounting Adjustment Type Code |
| `CodeFinancialAdjustmentStatusID` | Financial Adjustment Status | Select the status of the accounting assumption adjustment from the field. | Dropdown (Financial Adjustment Status Code) | Global |  | `financial_adjustment.CodeFinancialAdjustmentStatusID · TEXT` | Financial Adjustment Status Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Amount` |  | Enter the amount of the accounting assumption adjustment of the asset in this field. This field appears on the Equipment Contract > Payment Info > Recurring Payments > Equipment Payment Setup page in the Add / Edit Financial Adjustment modal window. | Currency | Global |  | `financial_adjustment.Amount · TEXT` |  |
| `ThirdPartyRVGAmount` | Portion Guaranteed By 3rd Party | The total value of the residual value guarantee, positive or negative. | Currency | Global |  | `financial_adjustment.ThirdPartyRVGAmount · TEXT` |  |
| `TotalRVGAmount` | Total Residual Value Guarantee | The residual value guarantee amount which is guaranteed by a third party, positive or negative. Both positive and negative numbers can be entered in this field. | Currency | Global |  | `financial_adjustment.TotalRVGAmount · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FinancialAdjustmentID` | Financial Adjustment RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `financial_adjustment.FinancialAdjustmentID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the accounting assumption adjustment for the asset in this field. This field appears on the Equipment Contract > Payment Info > Recurring Payments > Equipment Payment Setup page in the Add / Edit Financial Adjustment modal window. | Date | Global |  | `financial_adjustment.EffectiveDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `financial_adjustment.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Financial Adjustment ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `financial_adjustment.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `financial_adjustment.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `financial_adjustment.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `financial_adjustment.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `financial_adjustment.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `financial_adjustment.RevNumber · TEXT` |  |
