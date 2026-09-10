# LandPurchaseSummary — Data Fields

The land-acquisition deal record for ground purchases — asking price, acreage, and commencement date, anchoring the Purchase Management group alongside Ownership and DevelopmentPlan. 34 Global fields.

**Table Association:** `LandPurchaseSummary` &nbsp;·&nbsp; **Total fields:** 34 (Global: 34, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Purchase Management / Audit Info |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Purchase Management / Audit Info |
| Acreage | `Acreage` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Amended Commencement Date | `AmendedCommencementDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Asking Price | `AskingPrice` | `sTYPE_MONEY` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Commencement Date | `CommencementDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Contract Options | `ContractOptions` | `sTYPE_TEXTAREA` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Date Purchaser Signed | `SignedPurchaserDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Date Seller Signed | `SignedSellerDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Earnest Money Hard Date | `EarnestMoneyHardDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Earnest money | `EarnestMoney` | `sTYPE_MONEY` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Environment Engineer | `EnvironmentalEngineerID` | `sTYPE_PERSON` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Expected Store Opening Date | `FacilityOpenDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Expected contract signing date | `ClosingDate` | `sTYPE_DATE` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Finance Agent | `FinanceAgentID` | `sTYPE_PERSON` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Property Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Purchase Summary ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Purchase Management / Purchase Management Info |
| Purchase Summary RecID | `LandPurchaseSummaryID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Purchaser | `OwnerID` | `sTYPE_OWNER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Purchaser Attorney | `OwnerLawyerID` | `sTYPE_LAWYER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Purchaser Broker | `OwnerBrokerID` | `sTYPE_BROKER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Purchaser Commission | `BuyingCommissionAmount` | `sTYPE_MONEY` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Purchaser Signee | `OwnerSigneeID` | `sTYPE_PERSON` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Sales Price | `SalePrice` | `sTYPE_MONEY` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Seller | `SellerID` | `sTYPE_OWNER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Seller Commission | `SellingCommissionAmount` | `sTYPE_MONEY` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Seller Signee | `SellerSigneeID` | `sTYPE_PERSON` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Seller's Lawyer | `SellerLawyerID` | `sTYPE_LAWYER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Selling Broker | `SellerBrokerID` | `sTYPE_BROKER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Survey Review Period | `SurveyReviewDays` | `sTYPE_NUMBER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Title Review Period | `TitleReviewDays` | `sTYPE_NUMBER` | Global | No | No |  | Purchase Management / Purchase Management Info |
| Waiver Period | `WaiverDays` | `sTYPE_NUMBER` | Global | No | No |  | Purchase Management / Purchase Management Info |
