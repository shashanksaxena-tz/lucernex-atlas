# ExpenseVendorAllocation

*16 fields · module: Lease Accounting & Payments · Postgres: `expense_vendor_allocation`*

Allocation of a recoverable expense to a specific paying vendor — AP vendor number and begin/end date. 15 Global fields under Contract.

Source: `data-fields/expense-vendor-allocation.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Fields with a vendor definition | 15 of 16 inventoried |
| Physical tables | `expense_vendor_allocation` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 15 (15 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in expense_vendor_allocation

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 15 fields carry a vendor definition

**Observed.** 15 of this record's 16 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |
| [CON-R-039](../rules/CON-R-039.md) | An expense is split across vendors: ExpenseVendorAllocation apportions one clause's payments across vendors by percentage; CHANGE_EXPENSE_ALLOCATION_VENDOR rewrites it. | Observed |
| [CON-R-152](../rules/CON-R-152.md) | An Expense Setup is generated from · `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates · One setup fans out to one transaction per allocation · The vendor split can change mid-term · Observed | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `expense_vendor_allocation.ContractID · TEXT` | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | The ExpenseSetupID field is used to associate an expense vendor allocation with an expense setup record. | Expense Setup ID | Global | yes | `expense_vendor_allocation.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_vendor_allocation.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | Select the vendor who should be paid from this field. | Employer ID | Global | yes | `expense_vendor_allocation.VendorID · TEXT` | [Employer](Employer.md) |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PaymentPercentage` | Payment Percentage | Enter the allocation percentage in this field. Your vendor allocations must total 100%. However, if two vendors are entered with both vendors having an allocation of 100%, both vendors will be paid 100%. Allocations are processed in order from largest to smallest. The smallest allocation will receive what remains of a payment. This means that it is very important that vendor allocations are entered correctly. For example, if two vendors have been entered as having a 60-50 split when the allocation should have been 50-50, the first vendor would be paid 60%, while the second would be paid 40%. If a vendor allocation does not exist, transactions will still be generated with an empty Vendor field. Any changes to the vendor allocation will set current and future expense schedule statuses to Review. They will need to be approved using the Approvals Process procedures. | Percentage | Global |  | `expense_vendor_allocation.PaymentPercentage · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpenseVendorAllocationID` | Vendor Allocation RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `expense_vendor_allocation.ExpenseVendorAllocationID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `expense_vendor_allocation.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `expense_vendor_allocation.EndDate · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `APVendorNumber` | AP Vendor Number | The vendor number from the associated vendor record. | Text | Global |  | `expense_vendor_allocation.APVendorNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `expense_vendor_allocation.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Vendor Allocation ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `expense_vendor_allocation.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `expense_vendor_allocation.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `expense_vendor_allocation.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `expense_vendor_allocation.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `expense_vendor_allocation.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `expense_vendor_allocation.RevNumber · TEXT` |  |
