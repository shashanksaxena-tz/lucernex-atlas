# ChangeOrder — Data Fields

A cost change against an active capital project — approved amount, sequence number, and cost-tracking-variance linkage back to CostTrackingTemplate. 15 Global fields under Specialized Forms.

**Table Association:** `ChangeOrder` &nbsp;·&nbsp; **Total fields:** 15 (Global: 15, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Approved Change Order Amount | `ApprovedChangeOrderAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Change Order |
| Change Order ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Change Order |
| Change Order Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Change Order |
| Change Order RecID | `ChangeOrderID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Change Order |
| Change Order Sequence Number | `ChangeOrderSequenceNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Change Order |
| Cost Tracking Variance | `CostTrackingVariance` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Change Order |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Change Order |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Change Order |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Change Order |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Change Order |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Change Order |
| Outstanding Change Order Amount | `OutstandingChangeOrderAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Change Order |
| Related Purchase Order | `PurchaseOrderID` | `sTYPE_PURCHASE_ORDER` | Global | No | No |  | Specialized Forms / Change Order |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Change Order |
| Vendor CO Number | `VendorCONumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Change Order |
