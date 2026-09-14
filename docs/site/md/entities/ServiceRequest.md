# ServiceRequest

*30 fields · module: Assets, Equipment & Maintenance · Postgres: `service_request`*

A facilities service/maintenance ticket tied to an Asset or Contract — approval date/party, asset group/type, anchoring WorkOrder as the dispatched work resulting from the request. 30 Global fields under Specialized Forms.

Source: `data-fields/service-request.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 30 |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApproverPartyID` | Approver Party | Contact | Global |  |  |
| `RequestedForPartyID` | Requested For Party | Contact | Global |  |  |
| `RequestorPartyID` | Requestor Party | Contact | Global |  |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAssetCategoryID` | Maintenance Categories | Dropdown (Asset Category Code) | Global |  | Asset Category Code |
| `CodeAssetGroupID` | Asset Group | Dropdown (Asset Group Code) | Global |  | Asset Group Code |
| `CodeAssetTypeID` | Asset Type | Dropdown (Asset Type Code) | Global |  | Asset Type Code |
| `CodePriorityID` | Priority | Dropdown (Priority Code) | Global |  | Priority Code |
| `CodeProblemID` | Problem | Dropdown (Problem Code) | Global |  | Problem Code |
| `CodeSRQSourceID` | Source | Dropdown (SRQ Source Code) | Global |  | SRQ Source Code |
| `CodeSRQStatusID` | Request Status | Dropdown (SRQ Status Code) | Global |  | SRQ Status Code |
| `CodeSRQTypeID` | Request Type | Dropdown (SRQ Type Code) | Global |  | SRQ Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DNEAmount` | DNE Amount | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ServiceRequestID` | Service Request RecID | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApprovalDate` | Approval Date | Date | Global |  |  |
| `RequestedCompletionDate` | Requested Completion Date | Date | Global |  |  |
| `SubmissionDate` | Submission Date | Date | Global |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GLNumber` | GL Number | Text | Global |  |  |
| `IssueID` | Service Request Issue | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |
| `ReferenceNumber` | Reference Number | Text | Global |  |  |
| `SequenceNumber` | Number | Text | Global | yes |  |
| `SubAccount` | Sub Account | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Service Request ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
