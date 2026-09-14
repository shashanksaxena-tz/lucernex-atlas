# BidPackage

*48 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `bid_package`*

The competitive-bid solicitation record for a capital project — ranked bidder results (1st Place Bidder Name/Amount, and by pattern 2nd/3rd) plus its own page-layout assignment (Bid Award and Cancellation Layout) and approval-status/date fields for the award decision. 53 Global fields under Specialized Forms; it anchors a large ancillary family (BidPackageTemplate, BidderIssue, BidPackageAlternate/Breakout and their Value variants) that model the line items and alternates within a single bid.

Source: `data-fields/bid-package.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 48 |
| Fields with a vendor definition | 47 of 48 inventoried |
| Physical tables | `bid_package` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 53 (53 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 12 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in bid_package

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 47 fields carry a vendor definition

**Observed.** 47 of this record's 48 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 4 of this record's fields required; the Data Fields catalogue marks 4; 4 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (13)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidAwardByID` | Bid Awarded By | The name of the user who awarded the bid package. | Member ID | Global |  | `bid_package.BidAwardByID · TEXT` | [Member](Member.md) |
| `BidAwardLayoutID` | Bid Award and Cancellation Layout | The ID of the form layout used to configure the email sent to the winning bidder. | item ID | Global |  | `bid_package.BidAwardLayoutID · TEXT` | unresolved |
| `BidBudgetColumnTypeID` | Bid Budget Column Type | The ID of the bidding budget column associated with this bid package. | Budget Type ID | Global |  | `bid_package.BidBudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `BidCancelledByID` | Bid Cancelled By | The name of the user who cancelled the bid package. | Member ID | Global |  | `bid_package.BidCancelledByID · TEXT` | [Member](Member.md) |
| `BidInvitationLayoutID` | Bid Invitation Layout | The ID of the form layout used to configure the invitation email sent to bidders on this bid package. | item ID | Global |  | `bid_package.BidInvitationLayoutID · TEXT` | unresolved |
| `BidLossLayoutID` | Bid Loss Layout | The ID of the form layout used to configure the email sent to the losing bidders. | item ID | Global |  | `bid_package.BidLossLayoutID · TEXT` | unresolved |
| `BidPackageTemplateID` | Bid Package Template | The ID of the bid package template used to create this bid package. | Bid Package Template ID | Global |  | `bid_package.BidPackageTemplateID · TEXT` | [BidPackageTemplate](BidPackageTemplate.md) |
| `BudgetViewID` | Budget View | The ID of the budget view associated with this bid package. | Budget Template View ID | Global |  | `bid_package.BudgetViewID · TEXT` | [BudgetView](BudgetView.md) |
| `ConditionBudgetColumnTypeID` | Condition Budget Column Type | The ID of the conditioning budget column. | Budget Type ID | Global |  | `bid_package.ConditionBudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `EstimateBudgetColumnTypeID` | Estimate Budget Column Type | The ID of the estimate budget column associated with this bid package. | Budget Type ID | Global |  | `bid_package.EstimateBudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `bid_package.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `WinningBidMemberIDList` | Winning Bid Member | If the BidPackage is awarded, this field will return a list of member IDs who have the same employer ID as the winning bid vendor. If the BidPackage has not been awarded, an empty array will be returned. | Member ID | Global |  | `bid_package.WinningBidMemberIDList · TEXT` | [Member](Member.md) |
| `WinningBidVendorID` | Winning Bid Vendor | This field displays the vendor ID of the winning bidder. | Employer ID | Global |  | `bid_package.WinningBidVendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBidGracePeriodTimeUnitID` | Bid Grace Period Time Unit | Select the time unit for the bid grace period from this field. | Dropdown (Bid Grace Period Time Unit Code) | Global |  | `bid_package.CodeBidGracePeriodTimeUnitID · TEXT` | Bid Grace Period Time Unit Code |
| `CodeBidPackageAwardStatusID` | Bid Award Approval Status | The status of the bid package. | Dropdown (Last Action Status Code) | Global |  | `bid_package.CodeBidPackageAwardStatusID · TEXT` | Last Action Status Code |
| `CodeBidPackageStatusID` | Bid Package Status | The status of the bid package, for example awarded, closed, open, or invite. | Dropdown (Bid Package Status Code) | Global | yes | `bid_package.CodeBidPackageStatusID · TEXT` | Bid Package Status Code |
| `CodePreAcceptFolderSecurityID` | Pre-Accept Folder Security User Class | This field is a placeholder in preparation for an upcoming enhancement. | Dropdown (User Class) | Global |  | `bid_package.CodePreAcceptFolderSecurityID · TEXT` | User Class |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EstimatedBidAmount` | Estimated Bid Amount | The total of your estimated bid line items on the Conditioning tab. | Currency | Global |  | `bid_package.EstimatedBidAmount · TEXT` |  |
| `FirstPlaceConditionedAmount` | 1st Place ConditionedAmount | Pre-award, this field displays the conditioned amount of the top ranked bidder. Post-award, this field displays the awarded amounts. | Currency | Global |  | `bid_package.FirstPlaceConditionedAmount · TEXT` |  |
| `FirstPlaceSubmittedAmount` | 1st Place Submitted Amount | Pre-close date, this field displays the most recently submitted total bid amount, regardless of bidder. Post-close date, this field displays the total amount of the bidder in the 1st ranked position. | Currency | Global |  | `bid_package.FirstPlaceSubmittedAmount · TEXT` |  |
| `WinningConditionedBidAmount` | Winning Conditioned Bid Amount | This field displays the conditioned bid amount of the winning bidder. | Currency | Global |  | `bid_package.WinningConditionedBidAmount · TEXT` |  |
| `WinningSubmittedBidAmount` | Winning Submitted Bid Amount | This field displays the submitted bid amount of the winning bidder. | Currency | Global |  | `bid_package.WinningSubmittedBidAmount · TEXT` |  |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidGracePeriod` | Bid Grace Period | Enter the numeric value for the bid grace period in this field. | Number | Global |  | `bid_package.BidGracePeriod · TEXT` |  |
| `BidPackageID` | Bid Package RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `bid_package.BidPackageID · VARCHAR(64) NOT NULL` |  |
| `MaxNumberOfBids` | Max Number Of Bids | The maximum number of configured bids. | Number | Global |  | `bid_package.MaxNumberOfBids · TEXT` |  |
| `NumberOfActiveBidders` | Number Of Active Bidders | The number of active bidders on the bidding workflow. | Number | Global |  | `bid_package.NumberOfActiveBidders · TEXT` |  |
| `NumberOfBidInvitesAccepted` | Number Of Bid Invites Accepted | The number of bid invitations that were accepted. | Number | Global |  | `bid_package.NumberOfBidInvitesAccepted · TEXT` |  |
| `NumberOfBidInvitesDeclined` | Number Of Bid Invites Declined | The number of bid invitations that were declined. | Number | Global |  | `bid_package.NumberOfBidInvitesDeclined · TEXT` |  |
| `NumberOfBidInvitesUsed` | Number Of Bid Invites Used | The number of bid invitations that were sent. | Number | Global |  | `bid_package.NumberOfBidInvitesUsed · TEXT` |  |
| `NumberOfBidInvitesWaiting` | Number Of Bid Invites Waiting | The number of bid invitations that did not receive a response. | Number | Global |  | `bid_package.NumberOfBidInvitesWaiting · TEXT` |  |
| `TotalNumberOfBidders` | Total Number Of Bidders | This field displays the total number of bidders on the workflow. | Number | Global |  | `bid_package.TotalNumberOfBidders · TEXT` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidAwardDate` | Bid Award Date | The date and time the bid package was awarded. | Time | Global |  | `bid_package.BidAwardDate · TEXT` |  |
| `BidCancelledDate` | Bid Cancelled Date | The date and time the bid package was cancelled. | Time | Global |  | `bid_package.BidCancelledDate · TEXT` |  |
| `BidCloseDate` | Bid Close Date | The Bid Close Date. After the bid close date has passed, bidders can no longer submit revised bids. | Time | Global |  | `bid_package.BidCloseDate · TEXT` |  |
| `BidOpenDate` | Bid Open Date | The Bid Open Date. Bidders cannot submit bids until after the bid open date has passed. | Time | Global |  | `bid_package.BidOpenDate · TEXT` |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidderKickOffPageLayoutID` | Bidder Kick Off Page Layout | This field is used to select the bid invitation layout form that will be used for this work flow. | Text | Global |  | `bid_package.BidderKickOffPageLayoutID · TEXT` |  |
| `FirstPlaceBidderName` | 1st Place Bidder Name | The name of the bidder in first place. This name is anonymized if sealed bidding is enabled. | Text | Global |  | `bid_package.FirstPlaceBidderName · TEXT` |  |
| `FirstPlaceBidderVendorName` | 1st Place Bidder Vendor Name | The name of the vendor in first place. This name is anonymized if sealed bidding is enabled. | Text | Global |  | `bid_package.FirstPlaceBidderVendorName · TEXT` |  |
| `IssueID` | Bid Package Issue | The ID of the form. | Text | Global | yes | `bid_package.IssueID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `bid_package.Notes · TEXT` |  |
| `SequenceNumber` | Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Text | Global | yes | `bid_package.SequenceNumber · TEXT` |  |
| `WinningBidderIssueID` | Winning Bid | If the BidPackage is awarded, The ID of the bid that was selected as the winner. If the BidPackage has not been awarded, NULL will be returned. | Text | Global |  | `bid_package.WinningBidderIssueID · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Bid Package ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `bid_package.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `bid_package.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `bid_package.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `bid_package.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `bid_package.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `bid_package.RevNumber · TEXT` |  |
