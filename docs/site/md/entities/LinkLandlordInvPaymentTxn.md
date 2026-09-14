# LinkLandlordInvPaymentTxn

*13 fields · module: Lease Accounting & Payments · Postgres: `link_landlord_inv_payment_txn`*

Join table linking a LandlordInvoiceItem to the PaymentTransaction that paid it — allocation amount and date.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-115](../rules/CON-R-115.md) | An invoice line is matched to a payment: LinkLandlordInvPaymentTxn allocates AllocationAmount/AllocationDate between LandlordInvoiceItemID and PaymentTransactionID. | Observed |
| [CON-R-116](../rules/CON-R-116.md) | A match has a difference: VarianceAmount and VarianceReason are stored on the join itself, alongside ReconciliationStatus. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PaymentTransactionID` | Payment Transaction | Payment Transaction ID | Global | yes | [PaymentTransaction](PaymentTransaction.md) |
| `ProjectEntityID` | Project Entity | Entity ID | Global | yes | [ProjectEntity](ProjectEntity.md) |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AllocationAmount` | Allocation Amount | Currency | Global | yes |  |
| `VarianceAmount` | Variance Amount | Currency | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AllocationDate` | Allocation Date | Date | Global | yes |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LandlordInvoiceItemID` | Landlord Invoice Item | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |
| `ReconciliationStatus` | Reconciliation Status | Text | Global | yes |  |
| `VarianceReason` | Variance Reason | Text | Global |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
