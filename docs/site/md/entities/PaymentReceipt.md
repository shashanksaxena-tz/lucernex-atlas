# PaymentReceipt

*21 fields · module: Lease Accounting & Payments · Postgres: `payment_receipt`*

Money received from a tenant/payer (the inverse of PaymentTransaction) — allocated/unallocated amount and bank account/routing number for the depositing account. 20 Global fields under Contract.

Source: `data-fields/payment-receipt.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-118](../rules/CON-R-118.md) | Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side. | Observed |
| [CON-R-132](../rules/CON-R-132.md) | Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentIDList` | Documents | Document List | Global |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeReceiptTypeID` | Receipt Type | Dropdown (Receipt Type Code) | Global |  | Receipt Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmountAllocated` | Amount Allocated | Currency | Global |  |  |
| `AmountNotAllocated` | Amount Not Allocated | Currency | Global |  |  |
| `ReceivedAmount` | Received Amount | Currency | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PaymentReceiptID` | Payment Receipt RecID | Number | Global |  |  |
| `PeriodMonth` | Period Month | Number | Global |  |  |
| `PeriodYear` | Period Year | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `PostingDate` | Posting Date | Date | Global |  |  |
| `ReceiptDate` | Receipt Date | Date | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BankAccountNumber` | Bank Account Number | Text | Global |  |  |
| `BankRoutingNumber` | Bank Routing Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `ReceiptNumber` | Receipt Number | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Payment Receipt ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `PaymentReceiptID` |
