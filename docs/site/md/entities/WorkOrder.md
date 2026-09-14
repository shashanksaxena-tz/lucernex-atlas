# WorkOrder

*30 fields · module: Assets, Equipment & Maintenance · Postgres: `work_order`*

The dispatched maintenance work order resulting from a ServiceRequest — actual completion date, cost, labor hours, and vendor assignment. 29 Global fields under Specialized Forms.

Source: `data-fields/work-order.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 30 |
| Catalogued fields | 29 (29 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
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

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AlternateVendorID` | Alternate Vendor | Employer ID | Global |  | [Employer](Employer.md) |
| `ApproverMemberID` | Approver | Member ID | Global |  | [Member](Member.md) |
| `PrimaryVendorID` | Primary Vendor | Employer ID | Global |  | [Employer](Employer.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `SecondaryVendorID` | Secondary Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeClassificationID` | Classification | Dropdown (Classification Code) | Global |  | Classification Code |
| `CodeEvaluationRatingID` | Evaluation Rating | Dropdown (Evaluation Rating Code) | Global |  | Evaluation Rating Code |
| `CodePriorityID` | Priority | Dropdown (Priority Code) | Global |  | Priority Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualCost` | Actual Cost | Currency | Global |  |  |
| `EstimatedCost` | Estimated Cost | Currency | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualLaborHours` | Actual Labor Hours | Number | Global |  |  |
| `EstimatedLaborHours` | Estimated Labor Hours | Number | Global |  |  |
| `WorkOrderID` | Work Order RecID | Number | Global |  |  |

### Dates & timestamps (5)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualCompletionDate` | Actual Completion Date | Time | Global |  |  |
| `ActualStartDate` | Actual Start Date | Time | Global |  |  |
| `ApprovalDate` | Approval Date | Date | Global |  |  |
| `EstimatedCompletionDate` | Estimated Completion Date | Time | Global |  |  |
| `EstimatedStartDate` | Estimated Start Date | Time | Global |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Comments` |  | Text | Global |  |  |
| `EvaluationComment` | Evaluation Comment | Text | Global |  |  |
| `IssueID` | Work Order Issue | Text | Global | yes |  |
| `ReferenceNumber` | Reference Number | Text | Global |  |  |
| `SequenceNumber` | Number | Text | Global | yes |  |
| `ServiceRequestID` | Service Request | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Order ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
