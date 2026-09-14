# LandlordInvoice

*31 fields · module: Lease Accounting & Payments · Postgres: `landlord_invoice`*

An invoice received from a landlord for billing outside the standard recovery/rent cycle — coverage period and allocation-status amounts, anchoring LandlordInvoiceItem as its line-item detail. 31 Global fields under Contract.

Source: `data-fields/landlord-invoice.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssociatedDocumentID` | Document | Document ID | Global |  | [Document](Document.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `EmployerID` | Vendor | Employer ID | Global |  | [Employer](Employer.md) |
| `FolderID` | Folder | Folder ID | Global |  | [Folder](Folder.md) |
| `ProjectEntityID` | Project Entity | Entity ID | Global | yes | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmountAllocated` | Amount Allocated | Currency | Global |  |  |
| `AmountNotAllocated` | Amount Not Allocated | Currency | Global |  |  |
| `InvoiceTotal` | Invoice Total | Currency | Global |  |  |
| `SubTotal` | Sub Total | Currency | Global |  |  |
| `TotalTax` | Total Tax | Currency | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DueDate` | Due Date | Date | Global |  |  |
| `InvoiceDate` | Invoice Date | Date | Global |  |  |
| `ServicePeriodEndDate` | Coverage End Date | Date | Global |  |  |
| `ServicePeriodStartDate` | Coverage Begin Date | Date | Global |  |  |

### Text & notes (12)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CustomerAddress` | Customer Address | Text | Global |  |  |
| `CustomerAddressRecipient` | Customer Address Recipient | Text | Global |  |  |
| `CustomerID` |  | Text | Global |  |  |
| `CustomerName` | Customer Name | Text | Global |  |  |
| `CustomerTaxID` | Customer Tax ID | Text | Global |  |  |
| `InvoiceNumber` | Invoice Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PaymentTerm` | Payment Term | Text | Global |  |  |
| `VendorAddress` | Vendor Address | Text | Global |  |  |
| `VendorAddressRecipient` | Vendor Address Recipient | Text | Global |  |  |
| `VendorName` | Vendor Name | Text | Global |  |  |
| `VendorTaxID` | Vendor Tax ID | Text | Global |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
