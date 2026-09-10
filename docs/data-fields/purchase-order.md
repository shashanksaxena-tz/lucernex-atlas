# PurchaseOrder — Data Fields

A capital-project purchase order — approved change order amount and estimate amount, tied into the ChangeOrder/CostTrackingTemplate variance-tracking chain. 19 Global fields under Specialized Forms.

**Table Association:** `PurchaseOrder` &nbsp;·&nbsp; **Total fields:** 19 (Global: 19, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Approved Change Order Amount | `ApprovedChangeOrderAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Purchase Order |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Purchase Order |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Purchase Order |
| Estimate Amount | `EstimateAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Purchase Order |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Purchase Order |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Purchase Order |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Purchase Order |
| Number of Change Orders | `NumberChangeOrders` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Purchase Order |
| Number of Pay Apps | `NumberPayApps` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Purchase Order |
| Original Retainage | `RetainagePercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Specialized Forms / Purchase Order |
| Outstanding Change Order Amount | `OutstandingChangeOrderAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Purchase Order |
| Pay App Amount | `PayAppAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Purchase Order |
| Purchase Order Amount | `PurchaseOrderAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Purchase Order |
| Purchase Order ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Purchase Order |
| Purchase Order Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Purchase Order |
| Purchase Order RecID | `PurchaseOrderID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Purchase Order |
| Purchase Order Sequence Number | `PurchaseOrderSequenceNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Purchase Order |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Purchase Order |
| Vendor PO Number | `VendorPONumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Purchase Order |
