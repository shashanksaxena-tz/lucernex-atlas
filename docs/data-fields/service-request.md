# ServiceRequest — Data Fields

A facilities service/maintenance ticket tied to an Asset or Contract — approval date/party, asset group/type, anchoring WorkOrder as the dispatched work resulting from the request. 30 Global fields under Specialized Forms.

**Table Association:** `ServiceRequest` &nbsp;·&nbsp; **Total fields:** 30 (Global: 30, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Approval Date | `ApprovalDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Service Request |
| Approver Party | `ApproverPartyID` | `sTYPE_PERSON` | Global | No | No |  | Specialized Forms / Service Request |
| Asset Group | `CodeAssetGroupID` | `sCODE_ASSET_GROUP` | Global | No | No |  | Specialized Forms / Service Request |
| Asset Type | `CodeAssetTypeID` | `sCODE_ASSET_TYPE` | Global | No | No |  | Specialized Forms / Service Request |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Specialized Forms / Service Request |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Service Request |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Service Request |
| DNE Amount | `DNEAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Service Request |
| GL Number | `GLNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Service Request |
| Generate Work Order | `GenerateWorkOrder` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Specialized Forms / Service Request |
| Maintenance Categories | `CodeAssetCategoryID` | `sCODE_ASSET_CATEGORY` | Global | No | No |  | Specialized Forms / Service Request |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Service Request |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Service Request |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Service Request |
| Number | `SequenceNumber` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Service Request |
| Priority | `CodePriorityID` | `sCODE_PRIORITY` | Global | No | No |  | Specialized Forms / Service Request |
| Problem | `CodeProblemID` | `sCODE_PROBLEM` | Global | No | No |  | Specialized Forms / Service Request |
| Reference Number | `ReferenceNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Service Request |
| Request Status | `CodeSRQStatusID` | `sCODE_SRQ_STATUS` | Global | No | No |  | Specialized Forms / Service Request |
| Request Type | `CodeSRQTypeID` | `sCODE_SRQ_TYPE` | Global | No | No |  | Specialized Forms / Service Request |
| Requested Completion Date | `RequestedCompletionDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Service Request |
| Requested For Party | `RequestedForPartyID` | `sTYPE_PERSON` | Global | No | No |  | Specialized Forms / Service Request |
| Requestor Party | `RequestorPartyID` | `sTYPE_PERSON` | Global | No | No |  | Specialized Forms / Service Request |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Service Request |
| Service Request ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Service Request |
| Service Request Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Service Request |
| Service Request RecID | `ServiceRequestID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Service Request |
| Source | `CodeSRQSourceID` | `sCODE_SRQ_SOURCE` | Global | No | No |  | Specialized Forms / Service Request |
| Sub Account | `SubAccount` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Service Request |
| Submission Date | `SubmissionDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Service Request |
