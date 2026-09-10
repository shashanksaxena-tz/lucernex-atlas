# PropertyTaxAssessment — Data Fields

The underlying assessed value detail for a Parcel — land, improvements, and adjustment components of the total assessment, feeding PropertyTaxBill and PropertyTaxSummary. 24 Global fields under Parcel.

**Table Association:** `PropertyTaxAssessment` &nbsp;·&nbsp; **Total fields:** 24 (Global: 24, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Appraisal Date | `AppraisalDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Assessment |
| Appraisal Value | `AppraisalValue` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Assessment |
| Appraiser | `AppraiserID` | `sTYPE_EMPLOYER` | Global | No | No |  | Parcel / Property Tax Assessment |
| Assessment - Adjustments | `AssessmentAmountAdjustments` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Assessment |
| Assessment - Improvements | `AssessmentAmountImprovements` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Assessment |
| Assessment - Land | `AssessmentAmountLand` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Assessment |
| Assessment - Other | `AssessmentAmountOther` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Assessment |
| Assessment Amount Total | `AssessmentAmountTotal` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Assessment |
| Assessment Percentage | `AssessmentPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Assessment |
| Auto Calc? | `AutoCalcFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Property Tax Assessment |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Assessment |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Assessment |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Property Tax Assessment |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Assessment |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Assessment |
| Market Value | `MarketValue` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Assessment |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Assessment |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Assessment |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Property Tax Assessment |
| Parcel | `ParcelID` | `sTYPE_PARCEL` | Global | Yes | No |  | Parcel / Property Tax Assessment |
| Property Tax Assessment ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Property Tax Assessment |
| Property Tax Assessment RecID | `PropertyTaxAssessmentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Assessment |
| Property Tax Summary | `PropertyTaxSummaryID` | `sTYPE_PROPERTY_TAX_SUMMARY` | Global | Yes | No |  | Parcel / Property Tax Assessment |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Assessment |
