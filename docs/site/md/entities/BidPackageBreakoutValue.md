# BidPackageBreakoutValue

*6 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `bid_package_breakout_value`*

The dollar value a bidder submitted for one BidPackageBreakout line item.

Source: `data-fields/bid-package-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
| Fields with a vendor definition | 0 of 6 inventoried |
| Physical tables | — |
| Replication database | — |
| Catalogued fields | 5 (5 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### 6 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 6 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | not extracted | [ProjectEntity](ProjectEntity.md) |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Value` | Breakout Value |  | Currency | Global | yes | not extracted |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidPackageBreakoutID` | Bid Package Breakout |  | Text | Global |  | not extracted |  |
| `BudgetColumnID` | Budget Column |  | Text | Global | yes | not extracted |  |
| `BudgetLineItemID` | Budget Line Item |  | Text | Global | yes | not extracted |  |
| `Description` |  |  | Text | Global |  | not extracted |  |
