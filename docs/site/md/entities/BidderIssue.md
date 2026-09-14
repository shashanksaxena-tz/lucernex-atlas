# BidderIssue

*21 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `bidder_issue`*

One bidder's response to a BidPackage — conditioned bid amount and allow-conditioning flag, letting a bidder submit a qualified rather than firm bid. 20 Global fields under Specialized Forms.

Source: `data-fields/bidder-issue.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [AST-R-012](../rules/AST-R-012.md) | Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` record, exactly as `InvoiceIssue`/`BidderIss | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MemberIDList` | Member | Member ID | Global |  | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `UniqueVendorID` | Vendor | Employer ID | Global | yes | [Employer](Employer.md) |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ConditionedBidAmount` | Conditioned Bid Amount | Currency | Global |  |  |
| `SubmittedBidAmount` | Submitted Bid Amount | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidderIssueID` | Bidder Issue RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExtendedBidCloseDate` | Extended Bid Close Date | Date | Global |  |  |
| `NotificationDate` | Notification Date | Date | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AllowConditioning` | Allow Conditioning | Boolean | Global | yes |  |
| `IsBidInviteAccepted` | Is Bid Invite Accepted? | Boolean | Global |  |  |
| `IsWinningBid` | Is Winning Bid? | Boolean | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidPackageID` | Bid Package | Text | Global | yes |  |
| `IssueID` | Bidder Issue Issue | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |
| `SequenceNumber` | Number | Text | Global | yes |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Bidder Issue ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
