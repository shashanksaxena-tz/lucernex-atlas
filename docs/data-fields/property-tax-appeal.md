# PropertyTaxAppeal — Data Fields

A property-tax assessment appeal filed against a Parcel — filing date, appraisal fee, attorney fee, and the resulting assessment reduction, anchoring a sub-family (PropertyTaxAppealAward) for tracking the appeal's financial outcome. 40 Global fields under Parcel.

**Table Association:** `PropertyTaxAppeal` &nbsp;·&nbsp; **Total fields:** 40 (Global: 40, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Appeal Filed Date | `AppealFiledDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Appeal |
| Appeal Year | `AppealYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Parcel / Property Tax Appeal |
| Appraisal Fee | `AppraisalFee` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Assessment Reduction | `AssessmentReduction` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Attorney Fee | `AttorneyFee` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Certified Assessment | `CertifiedAssessment` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Appeal |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Appeal |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Appeal |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Appeal |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Parcel / Property Tax Appeal |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Parcel / Property Tax Appeal |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Appeal |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Appeal |
| Net Tax Reduction | `NetTaxReduction` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| New Assessment Date | `NewAssessmentDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Appeal |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Property Tax Appeal |
| Parcel | `ParcelID` | `sTYPE_PARCEL` | Global | Yes | No |  | Parcel / Property Tax Appeal |
| Prior Assessment | `PriorAssessment` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Prior Year Assessment | `PriorYearAssessment` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Property Tax Appeal ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Property Tax Appeal |
| Property Tax Appeal RecID | `PropertyTaxAppealID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Appeal |
| Property Tax Assessment | `PropertyTaxAssessmentID` | `sTYPE_PROPERTY_TAX_ASSESSMENT` | Global | Yes | No |  | Parcel / Property Tax Appeal |
| Proposed Assessment | `ProposedAssessment` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Reduced Assessment | `ReducedAssessment` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Refund Fee Amount | `RefundFeeAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Rendered Assessment | `RenderedAssessment` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Appeal |
| Revised Adjustment Amount | `RevisedAdjustmentAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Revised Assessment - Adjustments | `RevisedAssessAmtAdjustments` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Revised Assessment - Improvements | `RevisedAssessAmtImprovements` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Revised Assessment - Land | `RevisedAssessmentAmountLand` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Revised Assessment - Other | `RevisedAssessmentAmountOther` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Revised Assessment Amount | `RevisedAssessmentAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Revised Tax Amount | `RevisedTaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Tax Appeal Result | `CodeTaxAppealResultID` | `sCODE_TAX_APPEAL_RESULT` | Global | No | No |  | Parcel / Property Tax Appeal |
| Tax Appeal Status | `CodeTaxAppealStatusID` | `sCODE_TAX_APPEAL_STATUS` | Global | No | No |  | Parcel / Property Tax Appeal |
| Tax Attorney | `TaxAttorneyID` | `sTYPE_PERSON` | Global | No | No |  | Parcel / Property Tax Appeal |
| Tax Attorney Fee | `TaxAttorneyFee` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
| Tax Reduction | `TaxReduction` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal |
