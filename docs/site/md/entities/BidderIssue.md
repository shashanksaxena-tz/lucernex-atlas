# BidderIssue

*21 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `bidder_issue`*

One bidder's response to a BidPackage — conditioned bid amount and allow-conditioning flag, letting a bidder submit a qualified rather than firm bid. 20 Global fields under Specialized Forms.

Source: `data-fields/bidder-issue.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Fields with a vendor definition | 20 of 21 inventoried |
| Physical tables | `bidder_issue` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in bidder_issue

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 20 fields carry a vendor definition

**Observed.** 20 of this record's 21 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 6 of this record's fields required; the Data Fields catalogue marks 6; 6 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [AST-R-012](../rules/AST-R-012.md) | Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` record, exactly as `InvoiceIssue`/`BidderIss | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MemberIDList` | Member | This field returns a list of members associated with the bidding form. | Member ID | Global |  | `bidder_issue.MemberIDList · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `bidder_issue.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `UniqueVendorID` | Vendor | This field is used to validate that duplicate members from the same vendor are not added to a bid package. | Employer ID | Global | yes | `bidder_issue.UniqueVendorID · TEXT` | [Employer](Employer.md) |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ConditionedBidAmount` | Conditioned Bid Amount | The conditioned bid amount. | Currency | Global |  | `bidder_issue.ConditionedBidAmount · TEXT` |  |
| `SubmittedBidAmount` | Submitted Bid Amount | The bid amount submitted by the vendor. | Currency | Global |  | `bidder_issue.SubmittedBidAmount · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidderIssueID` | Bidder Issue RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `bidder_issue.BidderIssueID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExtendedBidCloseDate` | Extended Bid Close Date | When a bid close date is extended, The extended bid close date. | Date | Global |  | `bidder_issue.ExtendedBidCloseDate · TEXT` |  |
| `NotificationDate` | Notification Date | The date the bidders were notified about the bid. | Date | Global |  | `bidder_issue.NotificationDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllowConditioning` | Allow Conditioning | Select this check box to enable conditioning for the bidder. | Boolean | Global | yes | `bidder_issue.AllowConditioning · TEXT` |  |
| `IsBidInviteAccepted` | Is Bid Invite Accepted? | This option button is used in the bid invitation form. The bidder selects Yes if they want to accept the bid invitation, or No if they do not want to accept the bid invitation. | Boolean | Global |  | `bidder_issue.IsBidInviteAccepted · TEXT` |  |
| `IsWinningBid` | Is Winning Bid? | This flag indicates which bid is the winning bid. | Boolean | Global |  | `bidder_issue.IsWinningBid · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidPackageID` | Bid Package | The ID of the bid package associated with this bidder form. | Text | Global | yes | `bidder_issue.BidPackageID · TEXT` |  |
| `IssueID` | Bidder Issue Issue | The ID of the form. | Text | Global | yes | `bidder_issue.IssueID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `bidder_issue.Notes · TEXT` |  |
| `SequenceNumber` | Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Text | Global | yes | `bidder_issue.SequenceNumber · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Bidder Issue ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `bidder_issue.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `bidder_issue.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `bidder_issue.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `bidder_issue.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `bidder_issue.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `bidder_issue.RevNumber · TEXT` |  |
