# ChangeOrder

*16 fields · module: Capital Projects & Scheduling · Postgres: `change_order`*

A cost change against an active capital project — approved amount, sequence number, and cost-tracking-variance linkage back to CostTrackingTemplate. 15 Global fields under Specialized Forms.

Source: `data-fields/change-order.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | 15 (15 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
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

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `PurchaseOrderID` | Related Purchase Order | Purchase Order ID | Global |  | [PurchaseOrder](PurchaseOrder.md) |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApprovedChangeOrderAmount` | Approved Change Order Amount | Currency | Global |  |  |
| `CostTrackingVariance` | Cost Tracking Variance | Currency | Global |  |  |
| `OutstandingChangeOrderAmount` | Outstanding Change Order Amount | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ChangeOrderID` | Change Order RecID | Number | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ChangeOrderSequenceNumber` | Change Order Sequence Number | Text | Global |  |  |
| `IssueID` | Change Order Issue | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |
| `VendorCONumber` | Vendor CO Number | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Change Order ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
