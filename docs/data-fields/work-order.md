# WorkOrder — Data Fields

The dispatched maintenance work order resulting from a ServiceRequest — actual completion date, cost, labor hours, and vendor assignment. 29 Global fields under Specialized Forms.

**Table Association:** `WorkOrder` &nbsp;·&nbsp; **Total fields:** 29 (Global: 29, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Actual Completion Date | `ActualCompletionDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Work Order |
| Actual Cost | `ActualCost` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Work Order |
| Actual Labor Hours | `ActualLaborHours` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Work Order |
| Actual Start Date | `ActualStartDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Work Order |
| Alternate Vendor | `AlternateVendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Specialized Forms / Work Order |
| Approval Date | `ApprovalDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Work Order |
| Approver | `ApproverMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Work Order |
| Classification | `CodeClassificationID` | `sCODE_CLASSIFICATION` | Global | No | No |  | Specialized Forms / Work Order |
| Comments | `Comments` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Work Order |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Work Order |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Work Order |
| Estimated Completion Date | `EstimatedCompletionDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Work Order |
| Estimated Cost | `EstimatedCost` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Work Order |
| Estimated Labor Hours | `EstimatedLaborHours` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Work Order |
| Estimated Start Date | `EstimatedStartDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Work Order |
| Evaluation Comment | `EvaluationComment` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Work Order |
| Evaluation Rating | `CodeEvaluationRatingID` | `sCODE_EVALUATION_RATING` | Global | No | No |  | Specialized Forms / Work Order |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Work Order |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Work Order |
| Number | `SequenceNumber` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Work Order |
| Primary Vendor | `PrimaryVendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Specialized Forms / Work Order |
| Priority | `CodePriorityID` | `sCODE_PRIORITY` | Global | No | No |  | Specialized Forms / Work Order |
| Reference Number | `ReferenceNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Work Order |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Work Order |
| Secondary Vendor | `SecondaryVendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Specialized Forms / Work Order |
| Service Request | `ServiceRequestID` | `sTYPE_SERVICE_REQUEST` | Global | No | No |  | Specialized Forms / Work Order |
| Work Order ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Work Order |
| Work Order Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Work Order |
| Work Order RecID | `WorkOrderID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Work Order |
