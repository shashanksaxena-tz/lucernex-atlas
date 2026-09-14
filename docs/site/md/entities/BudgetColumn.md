# BudgetColumn

*21 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_column`*

One column within a capital project budget (e.g., 'Original Budget', 'Approved Change Orders') — status, type, and an 'Allow UI Edit?' flag, the representative example walked through in 005's own documentation. 20 Global fields under Budget.

Source: `data-fields/budget-column.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnTypeID` | Budget Column Type | Budget Type ID | Global | yes | [BudgetColumnType](BudgetColumnType.md) |
| `BudgetTemplateID` | Budget Template | Template ID | Global | yes | [BudgetTemplate](BudgetTemplate.md) |
| `CreatedByMemberID` | Created By Member | Member ID | Global | yes | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `ThirdPartyVendorID` | Third Party Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBudgetColumnStatusID` | Budget Column Status | Dropdown (Budget Status) | Global | yes | Budget Status |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnID` | Budget Column RecID | Number | Global |  |  |
| `SealedBidNumber` | Sealed Bid Number | Number | Global |  |  |
| `SequenceNumber` | Sequence Number | Number | Global | yes |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AllowUIEdit` | Allow UI Edit? | Boolean | Global |  |  |
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `IsLocked` | Is Locked? | Boolean | Global |  |  |
| `IsSelected` | Is Selected? | Boolean | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidPackageID` | Bid Package | Text | Global |  |  |
| `BudgetColumnName` | Budget Column Name | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `InitializedFromBudgetColumnID` | Initialized From Budget Column | Text | Global |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Column ClientID | Text | Global | yes |  |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
