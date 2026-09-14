# LandlordInvoice

*31 fields · module: Lease Accounting & Payments · Postgres: `landlord_invoice`*

An invoice received from a landlord for billing outside the standard recovery/rent cycle — coverage period and allocation-status amounts, anchoring LandlordInvoiceItem as its line-item detail. 31 Global fields under Contract.

Source: `data-fields/landlord-invoice.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 0 of 31 inventoried |
| Physical tables | `landlord_invoice` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in landlord_invoice

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required-ness: 2 disagree of 31 comparable

**Observed.** Over the 31 fields both captures contain, they agree on 29. The exceptions are ContractID, ProjectEntityID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssociatedDocumentID` | Document |  | Document ID | Global |  | `landlord_invoice.AssociatedDocumentID · TEXT` | [Document](Document.md) |
| `ContractID` | Contract |  | Contract ID | Global | yes | `landlord_invoice.ContractID · TEXT` | [Contract](Contract.md) |
| `EmployerID` | Vendor |  | Employer ID | Global |  | `landlord_invoice.EmployerID · TEXT` | [Employer](Employer.md) |
| `FolderID` | Folder |  | Folder ID | Global |  | `landlord_invoice.FolderID · TEXT` | [Folder](Folder.md) |
| `ProjectEntityID` | Project Entity |  | Entity ID | Global | yes | `landlord_invoice.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type |  | Dropdown (Currency Type Code) | Global |  | `landlord_invoice.CodeCurrencyTypeID · TEXT` | Currency Type Code |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmountAllocated` | Amount Allocated |  | Currency | Global |  | `landlord_invoice.AmountAllocated · TEXT` |  |
| `AmountNotAllocated` | Amount Not Allocated |  | Currency | Global |  | `landlord_invoice.AmountNotAllocated · TEXT` |  |
| `InvoiceTotal` | Invoice Total |  | Currency | Global |  | `landlord_invoice.InvoiceTotal · TEXT` |  |
| `SubTotal` | Sub Total |  | Currency | Global |  | `landlord_invoice.SubTotal · TEXT` |  |
| `TotalTax` | Total Tax |  | Currency | Global |  | `landlord_invoice.TotalTax · TEXT` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DueDate` | Due Date |  | Date | Global |  | `landlord_invoice.DueDate · TEXT` |  |
| `InvoiceDate` | Invoice Date |  | Date | Global |  | `landlord_invoice.InvoiceDate · TEXT` |  |
| `ServicePeriodEndDate` | Coverage End Date |  | Date | Global |  | `landlord_invoice.ServicePeriodEndDate · TEXT` |  |
| `ServicePeriodStartDate` | Coverage Begin Date |  | Date | Global |  | `landlord_invoice.ServicePeriodStartDate · TEXT` |  |

### Text & notes (12)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CustomerAddress` | Customer Address |  | Text | Global |  | `landlord_invoice.CustomerAddress · TEXT` |  |
| `CustomerAddressRecipient` | Customer Address Recipient |  | Text | Global |  | `landlord_invoice.CustomerAddressRecipient · TEXT` |  |
| `CustomerID` |  |  | Text | Global |  | `landlord_invoice.CustomerID · TEXT` |  |
| `CustomerName` | Customer Name |  | Text | Global |  | `landlord_invoice.CustomerName · TEXT` |  |
| `CustomerTaxID` | Customer Tax ID |  | Text | Global |  | `landlord_invoice.CustomerTaxID · TEXT` |  |
| `InvoiceNumber` | Invoice Number |  | Text | Global |  | `landlord_invoice.InvoiceNumber · TEXT` |  |
| `Notes` |  |  | Text | Global |  | `landlord_invoice.Notes · TEXT` |  |
| `PaymentTerm` | Payment Term |  | Text | Global |  | `landlord_invoice.PaymentTerm · TEXT` |  |
| `VendorAddress` | Vendor Address |  | Text | Global |  | `landlord_invoice.VendorAddress · TEXT` |  |
| `VendorAddressRecipient` | Vendor Address Recipient |  | Text | Global |  | `landlord_invoice.VendorAddressRecipient · TEXT` |  |
| `VendorName` | Vendor Name |  | Text | Global |  | `landlord_invoice.VendorName · TEXT` |  |
| `VendorTaxID` | Vendor Tax ID |  | Text | Global |  | `landlord_invoice.VendorTaxID · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By |  | Member ID | Global |  | `landlord_invoice.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date |  | Time | Global |  | `landlord_invoice.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `landlord_invoice.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `landlord_invoice.ModifiedDate · TEXT` |  |
