# CostTrackingTemplate — Data Fields

A reusable cost-tracking configuration for capital projects — which budget column represents 'Approved Change Order' and how variance is calculated, applied across ProjectEntity records. 27 Global fields under Company Items.

**Table Association:** `CostTrackingTemplate` &nbsp;·&nbsp; **Total fields:** 27 (Global: 27, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Approved CO Column | `ApprovedCOBudgetColTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Summary Variance Calculation | `SummaryVarianceCalc` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Name | `TemplateName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template RecID | `CostTrackingTemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Cap Program? | `IsValidForCapProgram` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Cap Project? | `IsValidForCapProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Equipment Contract? | `IsValidForEquipContract` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Facility? | `IsValidForFacility` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Location? | `IsValidForLocation` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Open Project? | `IsValidForOpenProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Parcel? | `IsValidForParcel` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Portfolio? | `IsValidForPortfolio` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Potential Project? | `IsValidForPotentialProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for Prototype? | `IsValidForPrototype` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Cost Tracking Template Valid for RE Contract? | `IsValidForContract` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Cost Tracking Template |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Cost Tracking Template |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Cost Tracking Template |
| Estimate Column | `EstimateBudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Company Items / Cost Tracking Template |
| Invoice Column | `InvoiceBudgetColTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Company Items / Cost Tracking Template |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Cost Tracking Template |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Cost Tracking Template |
| Outstanding CO Column | `OutstandingCOBudgetColTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Company Items / Cost Tracking Template |
| PO Column | `POBudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | Yes | No |  | Company Items / Cost Tracking Template |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Cost Tracking Template |
| Vendor Breakdown Variance Calculation | `VendorBreakdownVarianceCalc` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Cost Tracking Template |
