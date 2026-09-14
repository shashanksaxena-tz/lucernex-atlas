# AllowanceTransaction

*20 fields · module: Contracts & Leases · Postgres: `allowance_transaction`*

An individual draw/payment transaction against an Allowance — due date and linkage back to the Allowance and Contract.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 13 of 15 inventoried |
| Physical tables | `allowance_transaction` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in allowance_transaction

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 13 fields carry a vendor definition

**Observed.** 13 of this record's 15 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllowanceID` | Allowance | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Allowance ID | Global | yes | `allowance_transaction.AllowanceID · TEXT` | [Allowance](Allowance.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `allowance_transaction.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `allowance_transaction.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PaymentTerms` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |

### Money (6)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_AllowableAmount` |  |  | Currency | — |  |  |  |
| `Firm_ApprovedLandlordDeduction` |  |  | Currency | — |  |  |  |
| `Firm_LandlordRentOffset` |  |  | Currency | — |  |  |  |
| `PenaltyAmount` | Penalty Amount | Enter the penalty amount as specified in your contract. Some contracts specify that if the tenant does not receive the allowance within a certain time period, the tenant is allowed to impose a penalty amount. | Currency | Global |  | `allowance_transaction.PenaltyAmount · TEXT` |  |
| `ReceiveAmount` | Receive Amount | Enter the allowance amount received in this field. | Currency | Global |  | `allowance_transaction.ReceiveAmount · TEXT` |  |
| `RequestAmount` | Request Amount | Enter the allowance amount requested in this field. | Currency | Global |  | `allowance_transaction.RequestAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PercentageInstallment` |  |  | Percentage | — |  |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllowanceTransactionID` | Allowance Transaction RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `allowance_transaction.AllowanceTransactionID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DueDate` | Due Date | Enter the date by which the tenant was required to receive the allowance. For example, some contracts specify that if the tenant does not receive the allowance within a certain time period, the tenant is allowed to impose a penalty amount. | Date | Global |  | `allowance_transaction.DueDate · TEXT` |  |
| `Firm_RevisedDueDate` |  |  | Date | — |  |  |  |
| `ReceiveDate` | Receive Date | Enter the date the allowance amount was received in this field. | Date | Global |  | `allowance_transaction.ReceiveDate · TEXT` |  |
| `RequestDate` | Request Date | Enter the date the allowance amount was requested in this field. | Date | Global |  | `allowance_transaction.RequestDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `allowance_transaction.Notes · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Allowance Transaction ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `allowance_transaction.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `allowance_transaction.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `allowance_transaction.ModifiedDate · TEXT` |  |
