# BidPackage

*48 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `bid_package`*

The competitive-bid solicitation record for a capital project — ranked bidder results (1st Place Bidder Name/Amount, and by pattern 2nd/3rd) plus its own page-layout assignment (Bid Award and Cancellation Layout) and approval-status/date fields for the award decision. 53 Global fields under Specialized Forms; it anchors a large ancillary family (BidPackageTemplate, BidderIssue, BidPackageAlternate/Breakout and their Value variants) that model the line items and alternates within a single bid.

Source: `data-fields/bid-package.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 48 |
| Catalogued fields | 53 (53 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 12 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (13)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidAwardByID` | Bid Awarded By | Member ID | Global |  | [Member](Member.md) |
| `BidAwardLayoutID` | Bid Award and Cancellation Layout | item ID | Global |  | unresolved |
| `BidBudgetColumnTypeID` | Bid Budget Column Type | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `BidCancelledByID` | Bid Cancelled By | Member ID | Global |  | [Member](Member.md) |
| `BidInvitationLayoutID` | Bid Invitation Layout | item ID | Global |  | unresolved |
| `BidLossLayoutID` | Bid Loss Layout | item ID | Global |  | unresolved |
| `BidPackageTemplateID` | Bid Package Template | Bid Package Template ID | Global |  | [BidPackageTemplate](BidPackageTemplate.md) |
| `BudgetViewID` | Budget View | Budget Template View ID | Global |  | [BudgetView](BudgetView.md) |
| `ConditionBudgetColumnTypeID` | Condition Budget Column Type | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `EstimateBudgetColumnTypeID` | Estimate Budget Column Type | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `WinningBidMemberIDList` | Winning Bid Member | Member ID | Global |  | [Member](Member.md) |
| `WinningBidVendorID` | Winning Bid Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBidGracePeriodTimeUnitID` | Bid Grace Period Time Unit | Dropdown (Bid Grace Period Time Unit Code) | Global |  | Bid Grace Period Time Unit Code |
| `CodeBidPackageAwardStatusID` | Bid Award Approval Status | Dropdown (Last Action Status Code) | Global |  | Last Action Status Code |
| `CodeBidPackageStatusID` | Bid Package Status | Dropdown (Bid Package Status Code) | Global | yes | Bid Package Status Code |
| `CodePreAcceptFolderSecurityID` | Pre-Accept Folder Security User Class | Dropdown (User Class) | Global |  | User Class |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EstimatedBidAmount` | Estimated Bid Amount | Currency | Global |  |  |
| `FirstPlaceConditionedAmount` | 1st Place ConditionedAmount | Currency | Global |  |  |
| `FirstPlaceSubmittedAmount` | 1st Place Submitted Amount | Currency | Global |  |  |
| `WinningConditionedBidAmount` | Winning Conditioned Bid Amount | Currency | Global |  |  |
| `WinningSubmittedBidAmount` | Winning Submitted Bid Amount | Currency | Global |  |  |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidGracePeriod` | Bid Grace Period | Number | Global |  |  |
| `BidPackageID` | Bid Package RecID | Number | Global |  |  |
| `MaxNumberOfBids` | Max Number Of Bids | Number | Global |  |  |
| `NumberOfActiveBidders` | Number Of Active Bidders | Number | Global |  |  |
| `NumberOfBidInvitesAccepted` | Number Of Bid Invites Accepted | Number | Global |  |  |
| `NumberOfBidInvitesDeclined` | Number Of Bid Invites Declined | Number | Global |  |  |
| `NumberOfBidInvitesUsed` | Number Of Bid Invites Used | Number | Global |  |  |
| `NumberOfBidInvitesWaiting` | Number Of Bid Invites Waiting | Number | Global |  |  |
| `TotalNumberOfBidders` | Total Number Of Bidders | Number | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidAwardDate` | Bid Award Date | Time | Global |  |  |
| `BidCancelledDate` | Bid Cancelled Date | Time | Global |  |  |
| `BidCloseDate` | Bid Close Date | Time | Global |  |  |
| `BidOpenDate` | Bid Open Date | Time | Global |  |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidderKickOffPageLayoutID` | Bidder Kick Off Page Layout | Text | Global |  |  |
| `FirstPlaceBidderName` | 1st Place Bidder Name | Text | Global |  |  |
| `FirstPlaceBidderVendorName` | 1st Place Bidder Vendor Name | Text | Global |  |  |
| `IssueID` | Bid Package Issue | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |
| `SequenceNumber` | Number | Text | Global | yes |  |
| `WinningBidderIssueID` | Winning Bid | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Bid Package ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
