# BidPackageTemplate — Data Fields

A reusable bid solicitation template — pre-assigns the page layouts used at each stage of a bid (Award, Invitation) and default budget view/column types, so a new BidPackage doesn't need each layout chosen manually. 31 Global fields under Specialized Forms.

**Table Association:** `BidPackageTemplate` &nbsp;·&nbsp; **Total fields:** 31 (Global: 31, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Award Approval Layout | `AwardApprovalLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Award Layout | `BidAwardLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Budget View | `BudgetViewID` | `sTYPE_BUDGET_VIEW` | Global | Yes | No |  | Specialized Forms / Bid Package Template |
| Bid Column Type | `BidColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Estimate Budget Column Type | `EstimateBudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Invitation Layout | `BidInvitationLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | Yes | No |  | Specialized Forms / Bid Package Template |
| Bid Package Kickoff Layout | `BidPackageKickoffLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | Yes | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Name | `TemplateName` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template RecID | `BidPackageTemplateID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Cap Program? | `IsValidForCapProgram` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Cap Project? | `IsValidForCapProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Equipment Contract? | `IsValidForEquipContract` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Facility? | `IsValidForFacility` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Location? | `IsValidForLocation` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Open Project? | `IsValidForOpenProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Parcel? | `IsValidForParcel` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Portfolio? | `IsValidForPortfolio` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Potential Project? | `IsValidForPotentialProject` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for Prototype? | `IsValidForPrototype` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Package Template Valid for RE Contract? | `IsValidForContract` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Bid Pre-Accept User Class | `CodePreAcceptUserClassID` | `sCODE_USER_CLASS` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Default Assignee Job Title List | `DefaultAssigneeCodeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Default Job Title List | `QnACodeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Post Award Layout | `PostAwardLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Specialized Forms / Bid Package Template |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Bid Package Template |
