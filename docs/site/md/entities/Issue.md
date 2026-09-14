# Issue

*56 fields · module: Capital Projects & Scheduling · Postgres: `issue`*

A bid-package issue/question thread header — date range and type, the object Question and IssueResponse attach to.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 56 |
| Catalogued fields | 4 (4 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 14 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 9 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Census and catalogue disagree

**Observed.** The object census declares 56 fields; the Data Fields catalogue lists 4. The 52-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-015](../rules/WF-R-015.md) | When a form matching the configured kick-off layout is completed, a WorkFlow row is created with KickOffIssueID pointing at that form. | Observed |
| [WF-R-055](../rules/WF-R-055.md) | CodeLastActionStatusID writes Issue.CodeLastActionStatusID and Issue.LastActionStatusChangeDate. This is the only field the engine can write on the record it is routing. | Derived |
| [LAY-R-160](../rules/LAY-R-160.md) | A Form Type is a `CodeIssueType` row. Lx's schema names the dropdown that selects one `Dropdown (Form Type)`. | Observed |
| [LAY-R-161](../rules/LAY-R-161.md) | Manage Forms administers a firm code table (`FirmCodeEdit.jsp?TableType=2035`), i.e. the catalog of Form Types — not a layout builder. | Observed |
| [LAY-R-164](../rules/LAY-R-164.md) | A form instance is an `Issue` record. `Issue.LastPageLayoutID` records "the name of the last form layout used to update the issue" — singular, so it is depth-1 history, not a per-step audit trail. | Observed |
| [AST-R-012](../rules/AST-R-012.md) | Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` record, exactly as `InvoiceIssue`/`BidderIss | Observed |
| [AST-R-014](../rules/AST-R-014.md) | Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `Wo | Derived |
| [PRJ-R-004](../rules/PRJ-R-004.md) | The Manage Data Fields admin screen renders `Issue`'s configurable surface · `Issue` (56 raw fields) vs. `docs/data-fields/all-fields.csv` (4 rows) · Only 4 of 56 fields are tenant-admin-configurable; | Observed |
| [PRJ-R-009](../rules/PRJ-R-009.md) | A part is consumed or ordered against a work-order `Issue` · `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) · Two distinct records — one for parts actually us | Observed |

## Fields

### Relationships (foreign keys) (14)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssignedToMemberIDs` |  | Member ID | — |  | [Member](Member.md) |
| `AttentionEmailTo` |  | Member ID | — |  | [Member](Member.md) |
| `Budget` |  | Budget Type ID | — |  | [BudgetColumnType](BudgetColumnType.md) |
| `BudgetColumnTypeID` |  | Budget Type ID | — |  | [BudgetColumnType](BudgetColumnType.md) |
| `CheckedOutByMemberID` |  | Member ID | — |  | [Member](Member.md) |
| `EmployerSiteID` |  | Vendor Site ID | — |  | [EmployerSite](EmployerSite.md) |
| `EquipmentID` |  | Equipment ID | — |  | [Asset](Asset.md) |
| `EquipmentIDList` |  | Equipment ID | — |  | [Asset](Asset.md) |
| `InitiatedByMemberID` |  | Member ID | — |  | [Member](Member.md) |
| `LastPageLayoutID` |  | item ID | — |  | unresolved |
| `ManagerMemberIDs` |  | Member ID | — |  | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `TaskIDList` |  | Task/Group ID | — |  | [TaskGroup](TaskGroup.md) |
| `VendorID` |  | Employer ID | — |  | [Employer](Employer.md) |

### Soft references (4)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IssueDateRange` | Issue Date Range | Dropdown | Global |  |  |
| `IssueDateType` | Issue Date Type | Dropdown | Global |  |  |
| `PersonContactedID` |  | Contact | — |  |  |
| `WorkFlowAdhocMemberID` |  | Member | — |  |  |

### Coded values (drop-downs) (7)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeChangeReasonID` |  | Dropdown (Change Reason Code) | — |  | Change Reason Code |
| `CodeDisciplineID` |  | Dropdown (Discipline Code) | — |  | Discipline Code |
| `CodeIssueTypeID` |  | Dropdown (Form Type) | — |  | Form Type |
| `CodeLastActionStatusID` |  | Dropdown (Last Action Status Code) | — |  | Last Action Status Code |
| `CodeLocationID` |  | Dropdown (Location Code) | — |  | Location Code |
| `CodeMethodOfContactID` |  | Dropdown (Method Of Contact Code) | — |  | Method Of Contact Code |
| `CodeOrderStatusID` |  | Dropdown (Part Order Status Code) | — |  | Part Order Status Code |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentIDList` |  | Number | — |  |  |
| `IssueID` |  | Number | — |  |  |
| `NumberOfResponses` |  | Number | — |  |  |
| `PartNumberIDList` |  | Number | — |  |  |
| `PriorIssueID` |  | Number | — |  |  |

### Dates & timestamps (6)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CheckedOutDate` |  | Date | — |  |  |
| `ClosedDate` |  | Date | — |  |  |
| `DueDate` |  | Date | — |  |  |
| `DueDateConv` |  | Date | — |  |  |
| `LastActionStatusChangeDate` |  | Date | — |  |  |
| `LastResponseDate` |  | Date | — |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsClosed` |  | Boolean | — |  |  |
| `IsCritical` |  | Boolean | — |  |  |
| `IsPrivate` |  | Boolean | — |  |  |

### Text & notes (13)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActionComment` |  | Text | — |  |  |
| `BidLevelerBudget` |  | Text | — |  |  |
| `BidderBudget` | Submit Bid | Text | Global |  |  |
| `Body` |  | Text | — |  |  |
| `BudgetStatus` |  | Text | — |  |  |
| `PONumber` |  | Text | — |  |  |
| `PartOrderList` |  | Text | — |  |  |
| `Photos` |  | Text | — |  |  |
| `RelatedIssueID` |  | Text | — |  |  |
| `SearchField` |  | Text | — |  |  |
| `SequenceNumber` |  | Text | — |  |  |
| `Subject` |  | Text | — |  |  |
| `VendorSiteID` |  | Text | — |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` |  | Text | — |  |  |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
