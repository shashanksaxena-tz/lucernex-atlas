# ContractFinancialTest — Data Fields

The ASC 842 / IFRS 16 lease-classification and present-value calculation record for a contract — initial asset and liability balances, PV of financial terms before and after adjustments, and the aggregate lease value under each standard. 92 Global fields; the near-identical field pairs prefixed 'ASC 842' and (by pattern) 'IFRS 16' show Lucernex runs the same lease-accounting calculation twice per contract, once under each standard, so a tenant reporting under only one standard still carries both sets of fields.

**Table Association:** `ContractFinancialTest` &nbsp;·&nbsp; **Total fields:** 92 (Global: 92, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| ASC 842 Aggregate Value Of Lease | `ASC842CalcAggValueOfLease` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| ASC 842 Aggregate Value Of Lease Before Adjustments | `ASC842CalcAggValOfLeaseNoAdj` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| ASC 842 Initial Asset Balance | `ASC842InitialAssetBalance` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Accounting Assumptions |
| ASC 842 Initial Liability Balance | `ASC842InitialLiabilityBalance` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Accounting Assumptions |
| ASC 842 Net Lease Liability Balance | `ASC842NetLeaseLiabilityBalance` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Accounting Assumptions |
| ASC 842 PV Of Financial Terms | `ASC842CalcPVOfFinancialTerms` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| ASC 842 PV Of Financial Terms Before Adjustments | `ASC842CalcPVOfFinTermsNoAdj` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| ASC 842 Schedule | `CodeASC842ScheduleID` | `sCODE_ASC842_SCHEDULE` | Global | No | No |  | Contract / Accounting Assumptions |
| Accounting Begin Date | `Topic842BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Accounting Assumptions |
| Accounting End Date | `Topic842EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Accounting Assumptions |
| Accounting Method | `CodeAccountingMethodID` | `sCODE_ACCOUNTING_METHOD` | Global | No | No |  | Contract / Accounting Assumptions |
| Asset Type Tested | `CodeAssetTypeTestID` | `sCODE_ASSET_TYPE_TEST` | Global | No | No |  | Contract / Accounting Assumptions |
| Cancellation Option Amount | `CancellationOptionAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Discount Rate | `DiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Accounting Assumptions |
| Dismantling / Restoring Cost Amount | `DismantlingStorageCostAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Dismantling / Restoring Cost Desc | `DismantlingStorageCostDesc` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 Aggregate Value Of Lease | `IFRS16CalcAggValueOfLease` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 Aggregate Value Of Lease Before Adjustments | `IFRS16CalcAggValOfLeaseNoAdj` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 Initial Asset Balance | `IFRS16InitialAssetBalance` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 Initial Liability Balance | `IFRS16InitialLiabilityBalance` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 Net Lease Liability Balance | `IFRS16NetLeaseLiabilityBalance` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 PV Of Financial Terms | `IFRS16CalcPVOfFinancialTerms` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 PV Of Financial Terms Before Adjustments | `IFRS16CalcPVOfFinTermsNoAdj` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| IFRS 16 Schedule Selector | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Global | No | No |  | Contract / Accounting Assumptions |
| Impairments Amount | `ImpairmentsAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Impairments Description | `ImpairmentsDesc` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accounting Assumptions |
| Initial Direct Costs Amount | `InitialDirectCostsAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Initial Direct Costs Description | `InitialDirectCostsDesc` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accounting Assumptions |
| Lease Incentives Amount | `LeaseIncentivesAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Lease Incentives Description | `LeaseIncentivesDesc` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accounting Assumptions |
| Other Adjustments Description | `PVOfOtherAdjustmentsDesc` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accounting Assumptions |
| PV Of Cancellation Option | `PVOfCancellationOption` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| PV Of Financial Terms With Adjustments | `PVOfFinancialTermsWithAdjustments` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Accounting Assumptions |
| PV Of Other Adjustments | `PVOfOtherAdjustments` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| PV Of Purchase Option | `PVOfPurchaseOption` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| PV Of Residual Value Guarantees | `PVOfResidualValueGuarantees` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| PV Of Structuring Costs | `PVOfStructuringCosts` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Pre-Commencement Payments Amount | `PreCommencePayAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Pre-Commencement Payments Description | `PreCommencePayDesc` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accounting Assumptions |
| Purchase Option Amount | `PurchaseOptionAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Residual Value Guarantees | `ResidualValueGuarantees` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions |
| Structuring Costs Description | `PVOfStructuringCostsDesc` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accounting Assumptions |
| Accounting Type Override | `CodeAcctMethodOverrideID` | `sCODE_ACCOUNTING_METHOD` | Global | No | No |  | Contract / Financial Test |
| Asset | `AssetID` | `sTYPE_ASSET` | Global | No | No |  | Contract / Financial Test |
| Asset Associated Entity | `AssetAssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Contract / Financial Test |
| Associated Document | `AssociatedDocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Financial Test |
| Auto Computed? | `AutoComputed` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Financial Test |
| Base Name | `BaseName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Financial Test |
| Commence Date | `CommenceDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Financial Test |
| Contains Bargain Purchase Option? | `ContainsBargainPurchaseOption` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Financial Test |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Financial Test |
| Contract Financial Test ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Financial Test |
| Contract Financial Test RecID | `ContractFinancialTestID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Financial Test |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Financial Test |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Financial Test |
| Does Ownership Revert To Tenant? | `DoesTitleRevertToTenant` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Financial Test |
| Expire Date | `ExpireDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Financial Test |
| Fair Value Controlled | `FairValueControlled` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Financial Test |
| Fair Value Of Asset | `FairValueOfAsset` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial Test |
| Fair Value Source | `FairValueSource` | `sTYPE_TEXT` | Global | No | No |  | Contract / Financial Test |
| Fair Value Threshold | `FairValueThreshold` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Financial Test |
| Final Result | `FinalResult` | `sTYPE_TEXT` | Global | No | No |  | Contract / Financial Test |
| Folder | `FolderID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Financial Test |
| Initial Liability Balance Adjustment | `InitialLiabilityBalanceAdjust` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial Test |
| Initial Liability Balance to Threshold Fair Value Controlled | `InitLiabilityBalToThreshFairValueCtrld` | `sTYPE_PERCENT_MATH_OPERATION` | Global | No | No |  | Contract / Financial Test |
| Is Asset Too Specialized For Lessor? | `IsAssetTooSpecializedForLessor` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Financial Test |
| Is Locked? | `IsLocked` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Financial Test |
| Is the lease commencement at or near the end of the economic life of the asset? | `IsLeaseNearEnd` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Financial Test |
| Last Likely Option Date | `LastLikelyOptionDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Financial Test |
| Likely Term Length | `LikelyTermLength` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Contract / Financial Test |
| Line Number | `LineNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Financial Test |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Financial Test |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Financial Test |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Financial Test |
| Page Number | `PageNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Financial Test |
| Paragraph Number | `ParagraphNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Financial Test |
| Portion Of Asset Controlled | `PortionOfAssetControlled` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Financial Test |
| Remaining Economic Life Threshold | `RemainingEconomicLifeThreshold` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Financial Test |
| Remaining Life | `RemainingLife` | `sTYPE_NUMBER_FRACTION2DIGITS` | Global | No | No |  | Contract / Financial Test |
| Remaining Life Freq Unit | `CodeRemainingLifeFreqUnitID` | `sCODE_FREQUENCY_UNIT` | Global | No | No |  | Contract / Financial Test |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Financial Test |
| Section Number | `SectionNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Financial Test |
| Term Length | `TermLength` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Contract / Financial Test |
| Test #1 Result | `Test1Result` | `sTYPE_PASS_FAIL` | Global | No | No |  | Contract / Financial Test |
| Test #2 Result | `Test2Result` | `sTYPE_PASS_FAIL` | Global | No | No |  | Contract / Financial Test |
| Test #3 Result | `Test3Result` | `sTYPE_PASS_FAIL` | Global | No | No |  | Contract / Financial Test |
| Test #4 Result | `Test4Result` | `sTYPE_PASS_FAIL` | Global | No | No |  | Contract / Financial Test |
| Test #5 Result | `Test5Result` | `sTYPE_PASS_FAIL` | Global | No | No |  | Contract / Financial Test |
| Test Term Length | `TestTermLength` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Contract / Financial Test |
| Test Term Length to Remaining Life | `ComputedTestTermLengthToRemainingLife` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Financial Test |
| Threshold Fair Value Controlled | `ThresholdFairValueControlled` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Contract / Financial Test |
| Year Built | `YearBuilt` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Financial Test |
