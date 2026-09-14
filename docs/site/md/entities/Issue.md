# Issue

*56 fields · module: Capital Projects & Scheduling · Postgres: `issue`*

A bid-package issue/question thread header — date range and type, the object Question and IssueResponse attach to.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 56 |
| Fields with a vendor definition | 49 of 56 inventoried |
| Physical tables | `issue` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in issue

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 49 fields carry a vendor definition

**Observed.** 49 of this record's 56 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 6 of this record's fields required; the Data Fields catalogue marks 0; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssignedToMemberIDs` | Assignee(s) | The assignees of this form. | Member ID | — |  | `issue.AssignedToMemberIDs · TEXT` | [Member](Member.md) |
| `AttentionEmailTo` | Attention Email To: | This field is not implemented. | Member ID | — |  | `issue.AttentionEmailTo · TEXT` | [Member](Member.md) |
| `Budget` |  | This field is not implemented. | Budget Type ID | — |  | `issue.Budget · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `BudgetColumnTypeID` | Bid Type | Select the budget type from this field. | Budget Type ID | — |  | `issue.BudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `CheckedOutByMemberID` | Checked Out By | The name of the person who checked out the form. | Member ID | — |  | `issue.CheckedOutByMemberID · TEXT` | [Member](Member.md) |
| `EmployerSiteID` | Vendor Site |  | Vendor Site ID | — |  | `issue.EmployerSiteID · TEXT` | [EmployerSite](EmployerSite.md) |
| `EquipmentID` | Equipment | This field allows you to select a piece of equipment associated with the entity. | Equipment ID | — |  | `issue.EquipmentID · TEXT` | [Asset](Asset.md) |
| `EquipmentIDList` | Equipment List | This field is required if you want to use Lx's work orders functionality. This field allows you to select one or more pieces of equipment associated with the entity. | Equipment ID | — |  | `issue.EquipmentIDList · TEXT` | [Asset](Asset.md) |
| `InitiatedByMemberID` | Creator | The member ID of the person who added the form. | Member ID | — |  | `issue.InitiatedByMemberID · TEXT` | [Member](Member.md) |
| `LastPageLayoutID` | Last Layout Used | The name of the last form layout used to update the issue. | item ID | — | yes | `issue.LastPageLayoutID · TEXT` | unresolved |
| `ManagerMemberIDs` | Assignee(s) / Manager(s) | When added to a form, this field adds a series of fields that allow you to select managers, members, assignees, and approvers. | Member ID | — |  | `issue.ManagerMemberIDs · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `issue.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `TaskIDList` | Associated Task | This field allows you to associate the form with a task in your schedule. | Task/Group ID | — |  | `issue.TaskIDList · TEXT` | [TaskGroup](TaskGroup.md) |
| `VendorID` | Vendor |  | Employer ID | — |  | `issue.VendorID · TEXT` | [Employer](Employer.md) |

### Soft references (4)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IssueDateRange` | Issue Date Range | This field is not implemented. | Dropdown | Global |  | `issue.IssueDateRange · TEXT` |  |
| `IssueDateType` | Issue Date Type | This field is not implemented. | Dropdown | Global |  | `issue.IssueDateType · TEXT` |  |
| `PersonContactedID` | Contacted Contact | Select the person who was contacted from this field. | Contact | — |  | `issue.PersonContactedID · TEXT` |  |
| `WorkFlowAdhocMemberID` | Ad Hoc WF Assignee | This field lists the members of the entity who can be selected as an ad hoc assignee. | Member | — |  | `issue.WorkFlowAdhocMemberID · TEXT` |  |

### Coded values (drop-downs) (7)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeChangeReasonID` | Cause | This field allows you to select a change reason. The values in this field are defined by your system administrator. | Dropdown (Change Reason Code) | — |  | `issue.CodeChangeReasonID · TEXT` | Change Reason Code |
| `CodeDisciplineID` | Discipline | This field allows you to select a discipline. The values in this field are defined by your system administrator. | Dropdown (Discipline Code) | — |  | `issue.CodeDisciplineID · TEXT` | Discipline Code |
| `CodeIssueTypeID` | Type | This field displays the name of the form layout. | Dropdown (Form Type) | — | yes | `issue.CodeIssueTypeID · TEXT` | Form Type |
| `CodeLastActionStatusID` | Last Action Status |  | Dropdown (Last Action Status Code) | — |  | `issue.CodeLastActionStatusID · TEXT` | Last Action Status Code |
| `CodeLocationID` | Location | This field allows you to select a location. The values in this field are defined by your system administrator. | Dropdown (Location Code) | — |  | `issue.CodeLocationID · TEXT` | Location Code |
| `CodeMethodOfContactID` | Method Of Contact | This field allows you to select a method of contact. The values in this field are defined by your system administrator. | Dropdown (Method Of Contact Code) | — |  | `issue.CodeMethodOfContactID · TEXT` | Method Of Contact Code |
| `CodeOrderStatusID` | Order Status | Select the part order status from this field. | Dropdown (Part Order Status Code) | — |  | `issue.CodeOrderStatusID · TEXT` | Part Order Status Code |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents to the form from the Documents page. This field also allows you to upload new documents to the entity and attach them to the form. | Number | — |  | `issue.DocumentIDList · TEXT` |  |
| `IssueID` | Form RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | `issue.IssueID · VARCHAR(64) NOT NULL` |  |
| `NumberOfResponses` | # Replies | The number of replies to a form on the Forms page. | Number | — |  | `issue.NumberOfResponses · TEXT` |  |
| `PartNumberIDList` | Part List | This field is a custom list. It allows you to select pieces of equipment associated with the entity, select parts for the equipment, enter a quantity of parts, cost, and total. | Number | — |  | `issue.PartNumberIDList · TEXT` |  |
| `PriorIssueID` | Prior Issue | If you use the follow-up functionality, this field displays the parent issue that is being followed up on. | Number | — |  | `issue.PriorIssueID · TEXT` |  |

### Dates & timestamps (6)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CheckedOutDate` | Checked Out Date | The date the form was checked out. | Date | — |  | `issue.CheckedOutDate · TEXT` |  |
| `ClosedDate` | Closed Date | The date the form was closed. | Date | — |  | `issue.ClosedDate · TEXT` |  |
| `DueDate` | Due Date | Enter the form due date in this field. | Date | — |  | `issue.DueDate · TEXT` |  |
| `DueDateConv` | Followup | Select this check box to indicate that a follow-up is required for this form. When the check box is selected, a Due Date field will appear. Select the date by which the follow-up must be completed. You must also select the members who need to be assigned to the follow-up. | Date | — |  | `issue.DueDateConv · TEXT` |  |
| `LastActionStatusChangeDate` | Last Action Status Change Date |  | Date | — |  | `issue.LastActionStatusChangeDate · TEXT` |  |
| `LastResponseDate` | Last Reply | The date of the last reply to this form on the Forms page. | Date | — |  | `issue.LastResponseDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsClosed` | Is Closed? | If this field is set to true, it means that the form is closed. If it is set to false, it means that the form is open. | Boolean | — |  | `issue.IsClosed · TEXT` |  |
| `IsCritical` | Is Critical? | If this field is set to true, it means that the form is critical. If it is set to false, it means that the form is not critical. Issues with this flag set to true will appear in the Critical Issues widget on the Dashboard, and will have a flag next to their title on the Forms page. | Boolean | — | yes | `issue.IsCritical · TEXT` |  |
| `IsPrivate` | Private Issue? | If this field is set to true, it means that the form is private. If it is set to false, it means that the form is public. Only certain members will have access to private issues. | Boolean | — | yes | `issue.IsPrivate · TEXT` |  |

### Text & notes (13)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActionComment` | Action Comment | This field captures any comments left by the approver on the approver's action. | Text | — |  | `issue.ActionComment · TEXT` |  |
| `BidLevelerBudget` | Condition Bids | Click this button to condition bids. | Text | — |  | `issue.BidLevelerBudget · TEXT` |  |
| `BidderBudget` | Submit Bid | Click this button to submit your bid. | Text | Global |  | `issue.BidderBudget · TEXT` |  |
| `Body` | Description | Enter a description of the issue in this field. | Text | — |  | `issue.Body · TEXT` |  |
| `BudgetStatus` | Budget Status Button | Click this button to set the budget status. | Text | — |  | `issue.BudgetStatus · TEXT` |  |
| `PONumber` | Invoice Number | This field generates an automatic invoice number based on the currently selected entity and form type. This field is typically used for invoices, but can be used for any forms that need to be auto-numbered. This number starts at 0 and is unique within the firm. This field will not display in Add view, but will appear in View and Edit mode after the form has been saved the first time. | Text | — |  | `issue.PONumber · TEXT` |  |
| `PartOrderList` | Part Order List | This field is a custom list. It allows you to select maintenance categories, vendors, and parts. Then, you must enter the number of parts needed, and the date they are needed by. There are also fields for the status, quantity received, the receipt date, and comments. | Text | — |  | `issue.PartOrderList · TEXT` |  |
| `Photos` |  | This field allows you to upload a photo to the form. You cannot add the photo in Add mode, only in Edit mode. | Text | — |  | `issue.Photos · TEXT` |  |
| `RelatedIssueID` | Related Issue | This field points to a related issue. | Text | — |  | `issue.RelatedIssueID · TEXT` |  |
| `SearchField` | Search Field | This field determines search criteria for the issue list. | Text | — |  | `issue.SearchField · TEXT` |  |
| `SequenceNumber` | Form Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Text | — | yes | `issue.SequenceNumber · TEXT` |  |
| `Subject` | Title | Enter the title of the form in this field. This title is used in the Dashboard and in form and workflow lists. | Text | — |  | `issue.Subject · TEXT` |  |
| `VendorSiteID` | Vendor Site ID |  | Text | — |  | `issue.VendorSiteID · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Form ClientID |  | Text | — | yes | `issue.BOMapClientRecordID · TEXT` |  |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `issue.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `issue.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `issue.ModifiedDate · TEXT` |  |
