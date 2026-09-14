# ExpenseVendorAllocation

*16 fields · module: Lease Accounting & Payments · Postgres: `expense_vendor_allocation`*

Allocation of a recoverable expense to a specific paying vendor — AP vendor number and begin/end date. 15 Global fields under Contract.

Source: `data-fields/expense-vendor-allocation.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | 15 (15 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |
| [CON-R-039](../rules/CON-R-039.md) | An expense is split across vendors: ExpenseVendorAllocation apportions one clause's payments across vendors by percentage; CHANGE_EXPENSE_ALLOCATION_VENDOR rewrites it. | Observed |
| [CON-R-152](../rules/CON-R-152.md) | An Expense Setup is generated from · `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates · One setup fans out to one transaction per allocation · The vendor split can change mid-term · Observed | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | Expense Setup ID | Global | yes | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | Employer ID | Global | yes | [Employer](Employer.md) |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PaymentPercentage` | Payment Percentage | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExpenseVendorAllocationID` | Vendor Allocation RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `APVendorNumber` | AP Vendor Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Vendor Allocation ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
