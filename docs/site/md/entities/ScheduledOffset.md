# ScheduledOffset

*19 fields · module: Lease Accounting & Payments · Postgres: `scheduled_offset`*

A pre-scheduled (as opposed to variable) rent offset — cap amount per month/percent and allocation tracking. 18 Global fields under Contract.

Source: `data-fields/scheduled-offset.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Fields with a vendor definition | 18 of 19 inventoried |
| Physical tables | `scheduled_offset` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 18 (18 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in scheduled_offset

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 18 fields carry a vendor definition

**Observed.** 18 of this record's 19 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |
| [CON-R-061](../rules/CON-R-061.md) | Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation. | Observed |
| [CON-R-076](../rules/CON-R-076.md) | A ScheduledOffset is drawn down: a landlord credit (TotalAmount, CapAmountPerMonth) is drawn down over time against named expense group/types, via APPLY_OFFSETS. | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `scheduled_offset.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `scheduled_offset.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | Select the vendor associated with this offset from the field. | Employer ID | Global |  | `scheduled_offset.VendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `scheduled_offset.CodeCurrencyTypeID · TEXT` | Currency Type Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmountAllocated` | Amount Allocated | This field automatically calculates the amount that has been applied to transactions so far. | Currency | Global |  | `scheduled_offset.AmountAllocated · TEXT` |  |
| `AmountNotAllocated` | Amount Not Allocated | This field automatically calculates the remaining balance of the offset. | Currency | Global |  | `scheduled_offset.AmountNotAllocated · TEXT` |  |
| `CapAmountPerMonth` | Cap Amount Per Month | Enter the cap amount per month in this field. | Currency | Global |  | `scheduled_offset.CapAmountPerMonth · TEXT` |  |
| `TotalAmount` | Total Amount | Enter the total amount of the offset in this field. | Currency | Global |  | `scheduled_offset.TotalAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapPercent` | Cap Percent | Enter the cap percentage in this field. | Percentage | Global |  | `scheduled_offset.CapPercent · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ScheduledOffsetID` | Scheduled Offset RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `scheduled_offset.ScheduledOffsetID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `scheduled_offset.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `scheduled_offset.EndDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `scheduled_offset.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Scheduled Offset ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `scheduled_offset.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `scheduled_offset.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `scheduled_offset.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `scheduled_offset.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `scheduled_offset.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `scheduled_offset.RevNumber · TEXT` |  |
