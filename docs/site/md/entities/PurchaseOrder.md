# PurchaseOrder

*20 fields · module: Lease Accounting & Payments · Postgres: `purchase_order`*

A capital-project purchase order — approved change order amount and estimate amount, tied into the ChangeOrder/CostTrackingTemplate variance-tracking chain. 19 Global fields under Specialized Forms.

Source: `data-fields/purchase-order.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 19 (19 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-008](../rules/PRJ-R-008.md) | A change is made against an active capital project's cost · `ChangeOrder.ApprovedChangeOrderAmount`, `OutstandingChangeOrderAmount`, `CostTrackingVariance`, `PurchaseOrderID` · Tracks approved vs. outstanding change amounts against a `Purch | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApprovedChangeOrderAmount` | Approved Change Order Amount | Currency | Global |  |  |
| `EstimateAmount` | Estimate Amount | Currency | Global |  |  |
| `OutstandingChangeOrderAmount` | Outstanding Change Order Amount | Currency | Global |  |  |
| `PayAppAmount` | Pay App Amount | Currency | Global |  |  |
| `PurchaseOrderAmount` | Purchase Order Amount | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `RetainagePercent` | Original Retainage | Percentage | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `NumberChangeOrders` | Number of Change Orders | Number | Global |  |  |
| `NumberPayApps` | Number of Pay Apps | Number | Global |  |  |
| `PurchaseOrderID` | Purchase Order RecID | Number | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IssueID` | Purchase Order Issue | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |
| `PurchaseOrderSequenceNumber` | Purchase Order Sequence Number | Text | Global |  |  |
| `VendorPONumber` | Vendor PO Number | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Purchase Order ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [ChangeOrder](ChangeOrder.md) | `PurchaseOrderID` |
| [PayApp](PayApp.md) | `PurchaseOrderID` |
