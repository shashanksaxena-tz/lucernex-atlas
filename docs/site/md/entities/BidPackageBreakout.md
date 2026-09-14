# BidPackageBreakout

*4 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `none exported`*

A cost breakout line item within a BidPackage tied to a specific budget line.

Source: `data-fields/bid-package-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Catalogued fields | 3 (3 global, 0 firm) |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidPackageID` | Bid Package | Text | Global | yes |  |
| `BudgetLineItemID` | Budget Line Item | Text | Global | yes |  |
| `Description` |  | Text | Global |  |  |
