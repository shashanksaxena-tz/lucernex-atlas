# ContractFinancialTest

*93 fields · module: Contracts & Leases · Postgres: `contract_financial_test`*

The ASC 842 / IFRS 16 lease-classification and present-value calculation record for a contract — initial asset and liability balances, PV of financial terms before and after adjustments, and the aggregate lease value under each standard. 92 Global fields; the near-identical field pairs prefixed 'ASC 842' and (by pattern) 'IFRS 16' show Lx runs the same lease-accounting calculation twice per contract, once under each standard, so a tenant reporting under only one standard still carries both sets of fields.

Source: `data-fields/contract-financial-test.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 93 |
| Catalogued fields | 92 (92 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 12 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-002](../rules/ACC-R-002.md) | if `Contract.DiscountRate` is populated it is the rate used; otherwise `ComputedSLDiscountRate` | Inferred |
| [ACC-R-004](../rules/ACC-R-004.md) | a blank `CodeAccountingMethodID` matches both Finance and Operating. `MinSchedMons`/`MaxSchedMons` bound the schedule length in months for which the rate applies | Observed |
| [ACC-R-005](../rules/ACC-R-005.md) | `DoesTitleRevertToTenant = true` ⇒ Fail; false ⇒ Pass | Observed |
| [ACC-R-006](../rules/ACC-R-006.md) | true ⇒ Fail; false ⇒ Pass | Observed |
| [ACC-R-011](../rules/ACC-R-011.md) | any result = Fail ⇒ `Finance`; all five = Pass ⇒ `Operating` | Observed |
| [ACC-R-012](../rules/ACC-R-012.md) | if populated, the override supersedes the computed `CodeAccountingMethodID` | Derived |
| [ACC-R-013](../rules/ACC-R-013.md) | a locked test cannot be modified and cannot be deleted. Superseding is by creating a new `ContractFinancialTest` row | Observed |
| [ACC-R-014](../rules/ACC-R-014.md) | take the most recently locked row's `FinalResult` | Observed |
| [ACC-R-019](../rules/ACC-R-019.md) | the covenant amount is pulled into the accounting assumptions and the accounting schedule only if `CodeAccountingAdjustmentTypeID` ∈ {`Purchase Option`, `Cancellation Option`, `Residual Value Guarantee`} | Observed |
| [ACC-R-020](../rules/ACC-R-020.md) | `SLSummary.NeedsRecalculation := true` | Observed |
| [ACC-R-048](../rules/ACC-R-048.md) | `TotalImpairmentImpact = ImpairmentAmount + PriorAccumulatedAmortizationBalance`, where `PriorAccumulatedAmortizationBalance` is "the Accumulated Amortization Balance of the accounting period prior to the impairment." | Observed |
| [AST-R-004](../rules/AST-R-004.md) | Input: The 13-field block enumerated in `data-model.md` and detailed in `equipment-leases.md`. Effect: Equipment-lease classification can run per asset, using asset-supplied inputs, rather than only at the contract level. | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetID` | Asset | Equipment ID | Global |  | [Asset](Asset.md) |
| `AssociatedDocumentID` | Associated Document | Document ID | Global |  | [Document](Document.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `FolderID` | Folder | Folder ID | Global |  | [Folder](Folder.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Asset Associated Entity | Entity | Global |  |  |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | Global |  | ASC 842 Schedule Type |
| `CodeAccountingMethodID` | Accounting Method | Dropdown (Accounting Method Code) | Global |  | Accounting Method Code |
| `CodeAcctMethodOverrideID` | Accounting Type Override | Dropdown (Accounting Method Code) | Global |  | Accounting Method Code |
| `CodeAssetTypeTestID` | Asset Type Tested | Dropdown (Asset Type Test Code) | Global |  | Asset Type Test Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule Selector | Dropdown (IFRS 16 Schedule Type) | Global |  | IFRS 16 Schedule Type |
| `CodeRemainingLifeFreqUnitID` | Remaining Life Freq Unit | Dropdown (Frequency Unit Code) | Global |  | Frequency Unit Code |

### Money (32)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ASC842CalcAggValOfLeaseNoAdj` | ASC 842 Aggregate Value Of Lease Before Adjustments | Currency | Global |  |  |
| `ASC842CalcAggValueOfLease` | ASC 842 Aggregate Value Of Lease | Currency | Global |  |  |
| `ASC842CalcPVOfFinTermsNoAdj` | ASC 842 PV Of Financial Terms Before Adjustments | Currency | Global |  |  |
| `ASC842CalcPVOfFinancialTerms` | ASC 842 PV Of Financial Terms | Currency | Global |  |  |
| `ASC842InitialAssetBalance` | ASC 842 Initial Asset Balance | Currency | Global |  |  |
| `ASC842InitialLiabilityBalance` | ASC 842 Initial Liability Balance | Currency | Global |  |  |
| `ASC842NetLeaseLiabilityBalance` | ASC 842 Net Lease Liability Balance | Currency | Global |  |  |
| `CancellationOptionAmount` | Cancellation Option Amount | Currency | Global |  |  |
| `DismantlingStorageCostAmount` | Dismantling / Restoring Cost Amount | Currency | Global |  |  |
| `FairValueControlled` | Fair Value Controlled | Currency | Global |  |  |
| `FairValueOfAsset` | Fair Value Of Asset | Currency | Global |  |  |
| `IFRS16CalcAggValOfLeaseNoAdj` | IFRS 16 Aggregate Value Of Lease Before Adjustments | Currency | Global |  |  |
| `IFRS16CalcAggValueOfLease` | IFRS 16 Aggregate Value Of Lease | Currency | Global |  |  |
| `IFRS16CalcPVOfFinTermsNoAdj` | IFRS 16 PV Of Financial Terms Before Adjustments | Currency | Global |  |  |
| `IFRS16CalcPVOfFinancialTerms` | IFRS 16 PV Of Financial Terms | Currency | Global |  |  |
| `IFRS16InitialAssetBalance` | IFRS 16 Initial Asset Balance | Currency | Global |  |  |
| `IFRS16InitialLiabilityBalance` | IFRS 16 Initial Liability Balance | Currency | Global |  |  |
| `IFRS16NetLeaseLiabilityBalance` | IFRS 16 Net Lease Liability Balance | Currency | Global |  |  |
| `ImpairmentsAmount` | Impairments Amount | Currency | Global |  |  |
| `InitialDirectCostsAmount` | Initial Direct Costs Amount | Currency | Global |  |  |
| `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Currency | Global |  |  |
| `LeaseIncentivesAmount` | Lease Incentives Amount | Currency | Global |  |  |
| `PVOfCancellationOption` | PV Of Cancellation Option | Currency | Global |  |  |
| `PVOfFinancialTermsWithAdjustments` | PV Of Financial Terms With Adjustments | Currency | Global |  |  |
| `PVOfOtherAdjustments` | PV Of Other Adjustments | Currency | Global |  |  |
| `PVOfPurchaseOption` | PV Of Purchase Option | Currency | Global |  |  |
| `PVOfResidualValueGuarantees` | PV Of Residual Value Guarantees | Currency | Global |  |  |
| `PVOfStructuringCosts` | PV Of Structuring Costs | Currency | Global |  |  |
| `PreCommencePayAmount` | Pre-Commencement Payments Amount | Currency | Global |  |  |
| `PurchaseOptionAmount` | Purchase Option Amount | Currency | Global |  |  |
| `ResidualValueGuarantees` | Residual Value Guarantees | Currency | Global |  |  |
| `ThresholdFairValueControlled` | Threshold Fair Value Controlled | Currency | Global |  |  |

### Rates & percentages (6)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ComputedTestTermLengthToRemainingLife` | Test Term Length to Remaining Life | Percentage | Global |  |  |
| `DiscountRate` | Discount Rate | Percentage | Global |  |  |
| `FairValueThreshold` | Fair Value Threshold | Percentage | Global |  |  |
| `InitLiabilityBalToThreshFairValueCtrld` | Initial Liability Balance to Threshold Fair Value Controlled | Percentage | Global |  |  |
| `PortionOfAssetControlled` | Portion Of Asset Controlled | Percentage | Global |  |  |
| `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | Percentage | Global |  |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractFinancialTestID` | Contract Financial Test RecID | Number | Global |  |  |
| `LikelyTermLength` | Likely Term Length | Number | Global |  |  |
| `RemainingLife` | Remaining Life | 2-Digit Number | Global |  |  |
| `TermLength` | Term Length | Number | Global |  |  |
| `TestTermLength` | Test Term Length | Number | Global |  |  |
| `YearBuilt` | Year Built | Number | Global |  |  |

### Dates & timestamps (5)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CommenceDate` | Commence Date | Date | Global |  |  |
| `ExpireDate` | Expire Date | Date | Global |  |  |
| `LastLikelyOptionDate` | Last Likely Option Date | Date | Global |  |  |
| `Topic842BeginDate` | Accounting Begin Date | Date | Global |  |  |
| `Topic842EndDate` | Accounting End Date | Date | Global |  |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutoComputed` | Auto Computed? | Boolean | Global |  |  |
| `ContainsBargainPurchaseOption` | Contains Bargain Purchase Option? | Boolean | Global |  |  |
| `DoesTitleRevertToTenant` | Does Ownership Revert To Tenant? | Boolean | Global |  |  |
| `IsAssetTooSpecializedForLessor` | Is Asset Too Specialized For Lessor? | Boolean | Global |  |  |
| `IsLeaseNearEnd` | Is the lease commencement at or near the end of the economic life of the asset? | Boolean | Global |  |  |
| `IsLocked` | Is Locked? | Boolean | Global |  |  |
| `Test1Result` | Test #1 Result | Boolean | Global |  |  |
| `Test2Result` | Test #2 Result | Boolean | Global |  |  |
| `Test3Result` | Test #3 Result | Boolean | Global |  |  |
| `Test4Result` | Test #4 Result | Boolean | Global |  |  |
| `Test5Result` | Test #5 Result | Boolean | Global |  |  |

### Text & notes (15)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseName` | Base Name | Text | Global |  |  |
| `DismantlingStorageCostDesc` | Dismantling / Restoring Cost Desc | Text | Global |  |  |
| `FairValueSource` | Fair Value Source | Text | Global |  |  |
| `FinalResult` | Final Result | Text | Global |  |  |
| `ImpairmentsDesc` | Impairments Description | Text | Global |  |  |
| `InitialDirectCostsDesc` | Initial Direct Costs Description | Text | Global |  |  |
| `LeaseIncentivesDesc` | Lease Incentives Description | Text | Global |  |  |
| `LineNumber` | Line Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PVOfOtherAdjustmentsDesc` | Other Adjustments Description | Text | Global |  |  |
| `PVOfStructuringCostsDesc` | Structuring Costs Description | Text | Global |  |  |
| `PageNumber` | Page Number | Text | Global |  |  |
| `ParagraphNumber` | Paragraph Number | Text | Global |  |  |
| `PreCommencePayDesc` | Pre-Commencement Payments Description | Text | Global |  |  |
| `SectionNumber` | Section Number | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Contract Financial Test ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
