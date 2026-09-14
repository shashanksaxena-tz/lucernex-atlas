# WorkOrder

*30 fields · module: Assets, Equipment & Maintenance · Postgres: `work_order`*

The dispatched maintenance work order resulting from a ServiceRequest — actual completion date, cost, labor hours, and vendor assignment. 29 Global fields under Specialized Forms.

Source: `data-fields/work-order.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 30 |
| Fields with a vendor definition | 29 of 30 inventoried |
| Physical tables | `work_order` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 29 (29 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in work_order

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

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AlternateVendorID` | Alternate Vendor | Select an alternate vendor from this field. | Employer ID | Global |  | `work_order.AlternateVendorID · TEXT` | [Employer](Employer.md) |
| `ApproverMemberID` | Approver | Select the approver from this field. | Member ID | Global |  | `work_order.ApproverMemberID · TEXT` | [Member](Member.md) |
| `PrimaryVendorID` | Primary Vendor | Select the primary vendor from this field. | Employer ID | Global |  | `work_order.PrimaryVendorID · TEXT` | [Employer](Employer.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `work_order.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SecondaryVendorID` | Secondary Vendor | Select a secondary vendor from this field. | Employer ID | Global |  | `work_order.SecondaryVendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeClassificationID` | Classification | Select the work order classification from this field. The values in this field are defined by your system administrator. | Dropdown (Classification Code) | Global |  | `work_order.CodeClassificationID · TEXT` | Classification Code |
| `CodeEvaluationRatingID` | Evaluation Rating | Select the evaluation rating from this field. The values in this field are defined by your system administrator. | Dropdown (Evaluation Rating Code) | Global |  | `work_order.CodeEvaluationRatingID · TEXT` | Evaluation Rating Code |
| `CodePriorityID` | Priority | Select the priority of this work order from this field. | Dropdown (Priority Code) | Global |  | `work_order.CodePriorityID · TEXT` | Priority Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualCost` | Actual Cost | Enter the cost of the work order in this field. | Currency | Global |  | `work_order.ActualCost · TEXT` |  |
| `EstimatedCost` | Estimated Cost | Enter the estimated cost in this field. | Currency | Global |  | `work_order.EstimatedCost · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLaborHours` | Actual Labor Hours | Enter the number of labor hours in this field. | Number | Global |  | `work_order.ActualLaborHours · TEXT` |  |
| `EstimatedLaborHours` | Estimated Labor Hours | Enter the estimated labor hours in this field. | Number | Global |  | `work_order.EstimatedLaborHours · TEXT` |  |
| `WorkOrderID` | Work Order RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_order.WorkOrderID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (5)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualCompletionDate` | Actual Completion Date | Enter the actual completion date / time in this field. | Time | Global |  | `work_order.ActualCompletionDate · TEXT` |  |
| `ActualStartDate` | Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Time | Global |  | `work_order.ActualStartDate · TEXT` |  |
| `ApprovalDate` | Approval Date | Enter the approval date in this field. | Date | Global |  | `work_order.ApprovalDate · TEXT` |  |
| `EstimatedCompletionDate` | Estimated Completion Date | Enter the estimated completion date / time in this field. | Time | Global |  | `work_order.EstimatedCompletionDate · TEXT` |  |
| `EstimatedStartDate` | Estimated Start Date | Enter the estimated start date / time in this field. | Time | Global |  | `work_order.EstimatedStartDate · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Comments` |  | Enter any comments in this field. | Text | Global |  | `work_order.Comments · TEXT` |  |
| `EvaluationComment` | Evaluation Comment | Enter any comments about the evaluation in this field. | Text | Global |  | `work_order.EvaluationComment · TEXT` |  |
| `IssueID` | Work Order Issue | The ID of the form. | Text | Global | yes | `work_order.IssueID · TEXT` |  |
| `ReferenceNumber` | Reference Number | Enter a reference number for the work order in this field. | Text | Global |  | `work_order.ReferenceNumber · TEXT` |  |
| `SequenceNumber` | Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Text | Global | yes | `work_order.SequenceNumber · TEXT` |  |
| `ServiceRequestID` | Service Request | Select the service request this work order is associated with from this field. | Text | Global |  | `work_order.ServiceRequestID · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Order ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_order.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `work_order.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `work_order.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_order.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_order.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `work_order.RevNumber · TEXT` |  |
