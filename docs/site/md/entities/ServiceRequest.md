# ServiceRequest

*30 fields · module: Assets, Equipment & Maintenance · Postgres: `service_request`*

A facilities service/maintenance ticket tied to an Asset or Contract — approval date/party, asset group/type, anchoring WorkOrder as the dispatched work resulting from the request. 30 Global fields under Specialized Forms.

Source: `data-fields/service-request.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 30 |
| Fields with a vendor definition | 29 of 30 inventoried |
| Physical tables | `service_request` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in service_request

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 29 fields carry a vendor definition

**Observed.** 29 of this record's 30 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 29 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [AST-R-011](../rules/AST-R-011.md) | Input: `Asset.GenerateServiceRequest` and `ServiceRequest.GenerateWorkOrder`, both `sTYPE_SUBMITBUTTON`. Effect: A `ServiceRequest` is created from an `Asset`, and a `WorkOrder` from a `ServiceRequest`, only when a user presses the correspo | Observed |
| [AST-R-012](../rules/AST-R-012.md) | Input: `ServiceRequest.IssueID` and `WorkOrder.IssueID`, both `Required = Yes`, field type `sTYPE_ISSUE`. Effect: Each row of `ServiceRequest`/`WorkOrder` is paired 1:1 with an underlying `Issue` record, exactly as `InvoiceIssue`/`BidderIss | Observed |
| [AST-R-013](../rules/AST-R-013.md) | Input: `WorkOrder.ServiceRequestID`, field type `sTYPE_SERVICE_REQUEST`, `Required = No`. Effect: A `WorkOrder` can exist with no parent `ServiceRequest`, even though the UI's normal generation path (`AST-R-011`) always produces one from a  | Observed |
| [AST-R-014](../rules/AST-R-014.md) | Input: `LinkIssuePart.IssueID` + `.AssetID` (typed `Equipment ID`) + `.PartID` + `.Quantity` + `.CostPerPart` + `.TotalCost` + `.SerialNumber` — an object in the `projects-capital` module, not this one. Effect: The practical path from a `Wo | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `service_request.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `service_request.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApproverPartyID` | Approver Party | Select the approver from this field. | Contact | Global |  | `service_request.ApproverPartyID · TEXT` |  |
| `RequestedForPartyID` | Requested For Party | Select the party who requested the service from this field. | Contact | Global |  | `service_request.RequestedForPartyID · TEXT` |  |
| `RequestorPartyID` | Requestor Party | Select the party who requested the service from this field. | Contact | Global |  | `service_request.RequestorPartyID · TEXT` |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAssetCategoryID` | Maintenance Categories | Select the maintenance category from this field. | Dropdown (Asset Category Code) | Global |  | `service_request.CodeAssetCategoryID · TEXT` | Asset Category Code |
| `CodeAssetGroupID` | Asset Group | Select the asset group from this field. Groups are the parents of types, and grandparents of Categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Asset Group Code) | Global |  | `service_request.CodeAssetGroupID · TEXT` | Asset Group Code |
| `CodeAssetTypeID` | Asset Type | Select the asset type from this field. Types are the children of groups, and parents of Categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Asset Type Code) | Global |  | `service_request.CodeAssetTypeID · TEXT` | Asset Type Code |
| `CodePriorityID` | Priority | Select the priority of this service request from this field. | Dropdown (Priority Code) | Global |  | `service_request.CodePriorityID · TEXT` | Priority Code |
| `CodeProblemID` | Problem | Select the problem from this field. Problem codes are linked to maintenance categories. | Dropdown (Problem Code) | Global |  | `service_request.CodeProblemID · TEXT` | Problem Code |
| `CodeSRQSourceID` | Source | This field is used to select the request source of the service request. | Dropdown (SRQ Source Code) | Global |  | `service_request.CodeSRQSourceID · TEXT` | SRQ Source Code |
| `CodeSRQStatusID` | Request Status | This field is used to select the request status of the service request. | Dropdown (SRQ Status Code) | Global |  | `service_request.CodeSRQStatusID · TEXT` | SRQ Status Code |
| `CodeSRQTypeID` | Request Type | This field is used to select the request type of the service request. | Dropdown (SRQ Type Code) | Global |  | `service_request.CodeSRQTypeID · TEXT` | SRQ Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DNEAmount` | DNE Amount | Enter the do not exceed amount in this field. | Currency | Global |  | `service_request.DNEAmount · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ServiceRequestID` | Service Request RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `service_request.ServiceRequestID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApprovalDate` | Approval Date | Enter the approval date in this field. | Date | Global |  | `service_request.ApprovalDate · TEXT` |  |
| `RequestedCompletionDate` | Requested Completion Date | Enter the requested completion date in this field. | Date | Global |  | `service_request.RequestedCompletionDate · TEXT` |  |
| `SubmissionDate` | Submission Date | Enter the submission date in this field. | Date | Global |  | `service_request.SubmissionDate · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GLNumber` | GL Number | The general ledger account number associated with the maintenance category. | Text | Global |  | `service_request.GLNumber · TEXT` |  |
| `IssueID` | Service Request Issue | The ID of the form. | Text | Global | yes | `service_request.IssueID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `service_request.Notes · TEXT` |  |
| `ReferenceNumber` | Reference Number | Enter a reference number for the service request in this field. | Text | Global |  | `service_request.ReferenceNumber · TEXT` |  |
| `SequenceNumber` | Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Text | Global | yes | `service_request.SequenceNumber · TEXT` |  |
| `SubAccount` | Sub Account | The sub account number associated with the maintenance category. | Text | Global |  | `service_request.SubAccount · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Service Request ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `service_request.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `service_request.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `service_request.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `service_request.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `service_request.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `service_request.RevNumber · TEXT` |  |
