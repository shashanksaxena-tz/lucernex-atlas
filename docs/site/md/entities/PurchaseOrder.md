# PurchaseOrder

*20 fields · module: Lease Accounting & Payments · Postgres: `purchase_order`*

A capital-project purchase order — approved change order amount and estimate amount, tied into the ChangeOrder/CostTrackingTemplate variance-tracking chain. 19 Global fields under Specialized Forms.

Source: `data-fields/purchase-order.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 3 of 20 inventoried |
| Physical tables | `purchase_order` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 19 (19 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in purchase_order

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 3 fields carry a vendor definition

**Observed.** 3 of this record's 20 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 2; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-008](../rules/PRJ-R-008.md) | A change is made against an active capital project's cost · `ChangeOrder.ApprovedChangeOrderAmount`, `OutstandingChangeOrderAmount`, `CostTrackingVariance`, `PurchaseOrderID` · Tracks approved vs. outstanding change amounts against a `Purch | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `purchase_order.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApprovedChangeOrderAmount` | Approved Change Order Amount |  | Currency | Global |  | `purchase_order.ApprovedChangeOrderAmount · TEXT` |  |
| `EstimateAmount` | Estimate Amount |  | Currency | Global |  | `purchase_order.EstimateAmount · TEXT` |  |
| `OutstandingChangeOrderAmount` | Outstanding Change Order Amount |  | Currency | Global |  | `purchase_order.OutstandingChangeOrderAmount · TEXT` |  |
| `PayAppAmount` | Pay App Amount |  | Currency | Global |  | `purchase_order.PayAppAmount · TEXT` |  |
| `PurchaseOrderAmount` | Purchase Order Amount |  | Currency | Global |  | `purchase_order.PurchaseOrderAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `RetainagePercent` | Original Retainage |  | Percentage | Global |  | `purchase_order.RetainagePercent · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `NumberChangeOrders` | Number of Change Orders | This field calculates the number of change orders associated with this purchase order. | Number | Global |  | `purchase_order.NumberChangeOrders · TEXT` |  |
| `NumberPayApps` | Number of Pay Apps | This field calculates the number of payment applications associated with this purchase order. | Number | Global |  | `purchase_order.NumberPayApps · TEXT` |  |
| `PurchaseOrderID` | Purchase Order RecID |  | Number | Global |  | `purchase_order.PurchaseOrderID · VARCHAR(64) NOT NULL` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IssueID` | Purchase Order Issue | The ID of the form. | Text | Global | yes | `purchase_order.IssueID · TEXT` |  |
| `Notes` |  |  | Text | Global |  | `purchase_order.Notes · TEXT` |  |
| `PurchaseOrderSequenceNumber` | Purchase Order Sequence Number |  | Text | Global |  | `purchase_order.PurchaseOrderSequenceNumber · TEXT` |  |
| `VendorPONumber` | Vendor PO Number |  | Text | Global |  | `purchase_order.VendorPONumber · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Purchase Order ClientID |  | Text | Global | yes | `purchase_order.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By |  | Member ID | Global |  | `purchase_order.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date |  | Time | Global |  | `purchase_order.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `purchase_order.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `purchase_order.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number |  | Number | Global |  | `purchase_order.RevNumber · TEXT` |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [ChangeOrder](ChangeOrder.md) | `PurchaseOrderID` |
| [PayApp](PayApp.md) | `PurchaseOrderID` |
