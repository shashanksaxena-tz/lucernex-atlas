# PaymentReceipt

*21 fields · module: Lease Accounting & Payments · Postgres: `payment_receipt`*

Money received from a tenant/payer (the inverse of PaymentTransaction) — allocated/unallocated amount and bank account/routing number for the depositing account. 20 Global fields under Contract.

Source: `data-fields/payment-receipt.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Fields with a vendor definition | 20 of 21 inventoried |
| Physical tables | `payment_receipt` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in payment_receipt

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 20 fields carry a vendor definition

**Observed.** 20 of this record's 21 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-118](../rules/CON-R-118.md) | Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side. | Observed |
| [CON-R-132](../rules/CON-R-132.md) | Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `payment_receipt.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `payment_receipt.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents a record. | Document List | Global |  | `payment_receipt.DocumentIDList · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `payment_receipt.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeReceiptTypeID` | Receipt Type | Select the type of payment for example, cash or check from this field. | Dropdown (Receipt Type Code) | Global |  | `payment_receipt.CodeReceiptTypeID · TEXT` | Receipt Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmountAllocated` | Amount Allocated | This field automatically calculates the amount that has been applied to transactions so far. | Currency | Global |  | `payment_receipt.AmountAllocated · TEXT` |  |
| `AmountNotAllocated` | Amount Not Allocated | This field automatically calculates the remaining balance of the received transaction. | Currency | Global |  | `payment_receipt.AmountNotAllocated · TEXT` |  |
| `ReceivedAmount` | Received Amount | Enter the amount received in this field. | Currency | Global |  | `payment_receipt.ReceivedAmount · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PaymentReceiptID` | Payment Receipt RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `payment_receipt.PaymentReceiptID · VARCHAR(64) NOT NULL` |  |
| `PeriodMonth` | Period Month | Enter the two-digit period number in this field. | Number | Global |  | `payment_receipt.PeriodMonth · TEXT` |  |
| `PeriodYear` | Period Year | Enter the year in this field. | Number | Global |  | `payment_receipt.PeriodYear · TEXT` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the receipt in this field. | Date | Global |  | `payment_receipt.EffectiveDate · TEXT` |  |
| `PostingDate` | Posting Date | Enter the posting date of the receipt in this field. | Date | Global |  | `payment_receipt.PostingDate · TEXT` |  |
| `ReceiptDate` | Receipt Date | Enter the receipt date of the receipt in this field. | Date | Global |  | `payment_receipt.ReceiptDate · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BankAccountNumber` | Bank Account Number | If the payment type was a check or ACH payment, enter the account number in this field. | Text | Global |  | `payment_receipt.BankAccountNumber · TEXT` |  |
| `BankRoutingNumber` | Bank Routing Number | If the payment type was a check or ACH payment, enter the routing number in this field. | Text | Global |  | `payment_receipt.BankRoutingNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `payment_receipt.Notes · TEXT` |  |
| `ReceiptNumber` | Receipt Number | Enter the receipt number in this field. | Text | Global |  | `payment_receipt.ReceiptNumber · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Payment Receipt ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `payment_receipt.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `payment_receipt.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `payment_receipt.ModifiedDate · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `PaymentReceiptID` |
