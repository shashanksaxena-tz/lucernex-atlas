# ContractFinancialTest

*93 fields · module: Contracts & Leases · Postgres: `contract_financial_test`*

The ASC 842 / IFRS 16 lease-classification and present-value calculation record for a contract — initial asset and liability balances, PV of financial terms before and after adjustments, and the aggregate lease value under each standard. 92 Global fields; the near-identical field pairs prefixed 'ASC 842' and (by pattern) 'IFRS 16' show Lx runs the same lease-accounting calculation twice per contract, once under each standard, so a tenant reporting under only one standard still carries both sets of fields.

Source: `data-fields/contract-financial-test.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 93 |
| Fields with a vendor definition | 92 of 93 inventoried |
| Physical tables | `contract_financial_test` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 92 (92 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 12 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in contract_financial_test

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 92 fields carry a vendor definition

**Observed.** 92 of this record's 93 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 1 field marked required

**Observed.** The inventory marks 1 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Asset | The asset ID of the associated equipment asset. | Equipment ID | Global |  | `contract_financial_test.AssetID · TEXT` | [Asset](Asset.md) |
| `AssociatedDocumentID` | Associated Document | The ID of a document associated with this record. | Document ID | Global |  | `contract_financial_test.AssociatedDocumentID · TEXT` | [Document](Document.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `contract_financial_test.ContractID · TEXT` | [Contract](Contract.md) |
| `FolderID` | Folder | The folder ID of the document connected to the fair value source on your ASC 842 Test. | Folder ID | Global |  | `contract_financial_test.FolderID · TEXT` | [Folder](Folder.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `contract_financial_test.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Asset Associated Entity | This is a reporting field that returns data about the asset associated with the entity. | Entity | Global |  | `contract_financial_test.AssetAssociatedProjectEntityID · TEXT` |  |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (ASC 842 Schedule Type) | Global |  | `contract_financial_test.CodeASC842ScheduleID · TEXT` | ASC 842 Schedule Type |
| `CodeAccountingMethodID` | Accounting Method | Select whether you want to calculate your schedule as an Operating schedule or a Finance schedule from this field. | Dropdown (Accounting Method Code) | Global |  | `contract_financial_test.CodeAccountingMethodID · TEXT` | Accounting Method Code |
| `CodeAcctMethodOverrideID` | Accounting Type Override | Select the accounting method you want to use from this field. | Dropdown (Accounting Method Code) | Global |  | `contract_financial_test.CodeAcctMethodOverrideID · TEXT` | Accounting Method Code |
| `CodeAssetTypeTestID` | Asset Type Tested | This field is no longer in use. | Dropdown (Asset Type Test Code) | Global |  | `contract_financial_test.CodeAssetTypeTestID · TEXT` | Asset Type Test Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule Selector | The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (IFRS 16 Schedule Type) | Global |  | `contract_financial_test.CodeIFRS16ScheduleID · TEXT` | IFRS 16 Schedule Type |
| `CodeRemainingLifeFreqUnitID` | Remaining Life Freq Unit | Select the frequency unit used to describe the remaining economic life of the asset. Example frequency units are weeks, months, and years. | Dropdown (Frequency Unit Code) | Global |  | `contract_financial_test.CodeRemainingLifeFreqUnitID · TEXT` | Frequency Unit Code |

### Money (32)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ASC842CalcAggValOfLeaseNoAdj` | ASC 842 Aggregate Value Of Lease Before Adjustments | This field displays the cash value of the lease between the accounting begin date and end date. | Currency | Global |  | `contract_financial_test.ASC842CalcAggValOfLeaseNoAdj · TEXT` |  |
| `ASC842CalcAggValueOfLease` | ASC 842 Aggregate Value Of Lease | This field displays the cash value of the lease between the accounting begin date and end date with accounting assumption adjustments. | Currency | Global |  | `contract_financial_test.ASC842CalcAggValueOfLease · TEXT` |  |
| `ASC842CalcPVOfFinTermsNoAdj` | ASC 842 PV Of Financial Terms Before Adjustments | This field displays the present value of your financial terms as of your accounting begin date, prior to any accounting assumption adjustments. | Currency | Global |  | `contract_financial_test.ASC842CalcPVOfFinTermsNoAdj · TEXT` |  |
| `ASC842CalcPVOfFinancialTerms` | ASC 842 PV Of Financial Terms | This field displays the present value of your financial terms of your accounting begin date, after accounting assumption adjustments. | Currency | Global |  | `contract_financial_test.ASC842CalcPVOfFinancialTerms · TEXT` |  |
| `ASC842InitialAssetBalance` | ASC 842 Initial Asset Balance | This field displays the asset balance as of the accounting begin date. | Currency | Global |  | `contract_financial_test.ASC842InitialAssetBalance · TEXT` |  |
| `ASC842InitialLiabilityBalance` | ASC 842 Initial Liability Balance | This field displays the liability balance as of the accounting begin date. | Currency | Global |  | `contract_financial_test.ASC842InitialLiabilityBalance · TEXT` |  |
| `ASC842NetLeaseLiabilityBalance` | ASC 842 Net Lease Liability Balance | This field displays the cash value of lease payments plus any adjustments due to covenants. | Currency | Global |  | `contract_financial_test.ASC842NetLeaseLiabilityBalance · TEXT` |  |
| `CancellationOptionAmount` | Cancellation Option Amount | This field pulls the value of any cancellation options from the Covenants table. | Currency | Global |  | `contract_financial_test.CancellationOptionAmount · TEXT` |  |
| `DismantlingStorageCostAmount` | Dismantling / Restoring Cost Amount | Enter the cost of any activity necessary to restore the asset to its original state prior to the expiration of the lease. | Currency | Global |  | `contract_financial_test.DismantlingStorageCostAmount · TEXT` |  |
| `FairValueControlled` | Fair Value Controlled | The Fair Value of the Asset multiplied by the Portion of the Asset Controlled. The value in this field is used to set the overall market value of your portion of the asset, and is used in the calculation of the Threshold Fair Value Controlled. | Currency | Global |  | `contract_financial_test.FairValueControlled · TEXT` |  |
| `FairValueOfAsset` | Fair Value Of Asset | Enter the fair value of the asset. FASB 842.10.20 defines fair value as the price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date. | Currency | Global |  | `contract_financial_test.FairValueOfAsset · TEXT` |  |
| `IFRS16CalcAggValOfLeaseNoAdj` | IFRS 16 Aggregate Value Of Lease Before Adjustments | This field displays the cash value of the lease between the accounting begin date and end date. | Currency | Global |  | `contract_financial_test.IFRS16CalcAggValOfLeaseNoAdj · TEXT` |  |
| `IFRS16CalcAggValueOfLease` | IFRS 16 Aggregate Value Of Lease | This field displays the cash value of the lease between the accounting begin date and end date with accounting assumption adjustments. | Currency | Global |  | `contract_financial_test.IFRS16CalcAggValueOfLease · TEXT` |  |
| `IFRS16CalcPVOfFinTermsNoAdj` | IFRS 16 PV Of Financial Terms Before Adjustments | This field displays the present value of your financial terms as of your accounting begin date, prior to any accounting assumption adjustments. | Currency | Global |  | `contract_financial_test.IFRS16CalcPVOfFinTermsNoAdj · TEXT` |  |
| `IFRS16CalcPVOfFinancialTerms` | IFRS 16 PV Of Financial Terms | This field displays the present value of your financial terms of your accounting begin date, after accounting assumption adjustments. | Currency | Global |  | `contract_financial_test.IFRS16CalcPVOfFinancialTerms · TEXT` |  |
| `IFRS16InitialAssetBalance` | IFRS 16 Initial Asset Balance | This field displays the asset balance as of the accounting begin date. | Currency | Global |  | `contract_financial_test.IFRS16InitialAssetBalance · TEXT` |  |
| `IFRS16InitialLiabilityBalance` | IFRS 16 Initial Liability Balance | This field displays the liability balance as of the accounting begin date. | Currency | Global |  | `contract_financial_test.IFRS16InitialLiabilityBalance · TEXT` |  |
| `IFRS16NetLeaseLiabilityBalance` | IFRS 16 Net Lease Liability Balance | This field displays the cash value of lease payments plus any adjustments due to covenants. | Currency | Global |  | `contract_financial_test.IFRS16NetLeaseLiabilityBalance · TEXT` |  |
| `ImpairmentsAmount` | Impairments Amount | Enter any deductions related to the diminished value of the asset as a negative number. | Currency | Global |  | `contract_financial_test.ImpairmentsAmount · TEXT` |  |
| `InitialDirectCostsAmount` | Initial Direct Costs Amount | Enter the incremental costs of a lease that would not have been incurred if the lease had not been obtained. For example, for contracts broker s fees, certain legal fees, and certain payments to tenants to move out. | Currency | Global |  | `contract_financial_test.InitialDirectCostsAmount · TEXT` |  |
| `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Enter any adjustments to the initial liability for the asset in this field. | Currency | Global |  | `contract_financial_test.InitialLiabilityBalanceAdjust · TEXT` |  |
| `LeaseIncentivesAmount` | Lease Incentives Amount | Enter any incentives that have reduced the cost of the lease. | Currency | Global |  | `contract_financial_test.LeaseIncentivesAmount · TEXT` |  |
| `PVOfCancellationOption` | PV Of Cancellation Option | Enter the present value of the cancellation option. | Currency | Global |  | `contract_financial_test.PVOfCancellationOption · TEXT` |  |
| `PVOfFinancialTermsWithAdjustments` | PV Of Financial Terms With Adjustments | This field displays the present value of your financial terms minus any accounting assumption adjustments added to the Accounting Assumption Adjustments table. | Currency | Global |  | `contract_financial_test.PVOfFinancialTermsWithAdjustments · TEXT` |  |
| `PVOfOtherAdjustments` | PV Of Other Adjustments | Enter any other miscellaneous costs that should be accounted for in the schedule. | Currency | Global |  | `contract_financial_test.PVOfOtherAdjustments · TEXT` |  |
| `PVOfPurchaseOption` | PV Of Purchase Option | Enter the present value of the purchase option. | Currency | Global |  | `contract_financial_test.PVOfPurchaseOption · TEXT` |  |
| `PVOfResidualValueGuarantees` | PV Of Residual Value Guarantees | Enter the present value of the residual value guarantee. | Currency | Global |  | `contract_financial_test.PVOfResidualValueGuarantees · TEXT` |  |
| `PVOfStructuringCosts` | PV Of Structuring Costs | Enter any fees paid to the owners of a special-purpose entity for structuring the transaction. | Currency | Global |  | `contract_financial_test.PVOfStructuringCosts · TEXT` |  |
| `PreCommencePayAmount` | Pre-Commencement Payments Amount | Enter the amount paid towards rent prior to the commencement date, minus any incentives that have reduced the cost of the lease. You should also include your Cumulative Deferred Balance in this value if you are converting from an ASC 840 Straight Line Schedule. | Currency | Global |  | `contract_financial_test.PreCommencePayAmount · TEXT` |  |
| `PurchaseOptionAmount` | Purchase Option Amount | This field pulls the value of any purchase options from the Covenant table. | Currency | Global |  | `contract_financial_test.PurchaseOptionAmount · TEXT` |  |
| `ResidualValueGuarantees` | Residual Value Guarantees | This field pulls the value of any residual value guarantees from the Covenant table. | Currency | Global |  | `contract_financial_test.ResidualValueGuarantees · TEXT` |  |
| `ThresholdFairValueControlled` | Threshold Fair Value Controlled | The value in this field is the Fair Value Controlled multiplied by the Fair Value Threshold. This value sets the benchmark to which you will compare your Initial Liability Balance (Adjusted). If you exceed your Threshold Fair Value Controlled, your Test #4 result will be "Failed". | Currency | Global |  | `contract_financial_test.ThresholdFairValueControlled · TEXT` |  |

### Rates & percentages (6)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComputedTestTermLengthToRemainingLife` | Test Term Length to Remaining Life | This value is calculated by the system. The value of this field is the Term Length (based on Test) divided by the Remaining Economic Life. The comparison of this percentage to the Remaining Economic Life Threshold determines the pass / fail value displayed for the Test 3 result. | Percentage | Global |  | `contract_financial_test.ComputedTestTermLengthToRemainingLife · TEXT` |  |
| `DiscountRate` | Discount Rate | This field is where you enter the Discount Rate (also known as the Interest Rate or the Internal Borrower Rate [IBR]). | Percentage | Global |  | `contract_financial_test.DiscountRate · TEXT` |  |
| `FairValueThreshold` | Fair Value Threshold | Enter the fraction of the fair value of the underlying asset that amounts to substantially all of its fair value. This value is usually set to 90%. | Percentage | Global |  | `contract_financial_test.FairValueThreshold · TEXT` |  |
| `InitLiabilityBalToThreshFairValueCtrld` | Initial Liability Balance to Threshold Fair Value Controlled | The value of this field is equal to the Initial Liability Balance divided by the Threshold Fair Value Controlled. The value of this field is displayed as a percentage. | Percentage | Global |  | `contract_financial_test.InitLiabilityBalToThreshFairValueCtrld · TEXT` |  |
| `PortionOfAssetControlled` | Portion Of Asset Controlled | Enter the percentage based upon the rentable area divided by the total area of the asset. | Percentage | Global |  | `contract_financial_test.PortionOfAssetControlled · TEXT` |  |
| `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | Enter the fraction of the economic life of the underlying asset that amounts to a major part of that remaining economic life. This value is usually set to 75%. | Percentage | Global |  | `contract_financial_test.RemainingEconomicLifeThreshold · TEXT` |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractFinancialTestID` | Contract Financial Test RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `contract_financial_test.ContractFinancialTestID · VARCHAR(64) NOT NULL` |  |
| `LikelyTermLength` | Likely Term Length | If you have marked any terms as Likely on the Abstract Info > Terms page, this field will calculate the length of your likely term. | Number | Global |  | `contract_financial_test.LikelyTermLength · TEXT` |  |
| `RemainingLife` | Remaining Life | Enter the number value of the remaining economic life in this field. | 2-Digit Number | Global |  | `contract_financial_test.RemainingLife · TEXT` |  |
| `TermLength` | Term Length | This field displays the term length of your lease based upon the difference between the Commencement Date and the Expiration Date of the lease. This value is automatically calculated by the system. | Number | Global |  | `contract_financial_test.TermLength · TEXT` |  |
| `TestTermLength` | Test Term Length | This field displays the length of the test term that you have selected using the Test Begin Date and Test End Date fields. It is automatically calulcated by the system. | Number | Global |  | `contract_financial_test.TestTermLength · TEXT` |  |
| `YearBuilt` | Year Built | Select the year that the asset's useful life began, or the year the asset was built from the field. | Number | Global |  | `contract_financial_test.YearBuilt · TEXT` |  |

### Dates & timestamps (5)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CommenceDate` | Commence Date | This field pulls the commencement date of the lease entered on the Contract / Equipment Contract > Details > Summary page. | Date | Global |  | `contract_financial_test.CommenceDate · TEXT` |  |
| `ExpireDate` | Expire Date | This field pulls the expiration date of the lease entered on the Contract / Equipment Contract > Details > Summary page. | Date | Global |  | `contract_financial_test.ExpireDate · TEXT` |  |
| `LastLikelyOptionDate` | Last Likely Option Date | If you have marked any terms as Likely on the Abstract Info > Terms page, this field will pull the end date of the last likely term. | Date | Global |  | `contract_financial_test.LastLikelyOptionDate · TEXT` |  |
| `Topic842BeginDate` | Accounting Begin Date | This date is the date your organization is adopting ASC 842, or the Possession Begin Date, whichever is later. | Date | Global |  | `contract_financial_test.Topic842BeginDate · TEXT` |  |
| `Topic842EndDate` | Accounting End Date | This is the end date of your ASC 842 financial accounting for the contract, including any likely options. | Date | Global |  | `contract_financial_test.Topic842EndDate · TEXT` |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutoComputed` | Auto Computed? | This field will have a true value if the ASC 842 test was computed automatically by the system. | Boolean | Global |  | `contract_financial_test.AutoComputed · TEXT` |  |
| `ContainsBargainPurchaseOption` | Contains Bargain Purchase Option? | This check box is Test 2 of the ASC 842 Test. Select this check box if the lease contains a purchase option that the tenant is likely to exercise. | Boolean | Global |  | `contract_financial_test.ContainsBargainPurchaseOption · TEXT` |  |
| `DoesTitleRevertToTenant` | Does Ownership Revert To Tenant? | This check box is Test 1 of the ASC 842 test. Select this check box if the ownership of the asset reverts to the tenant at the end of the lease term. | Boolean | Global |  | `contract_financial_test.DoesTitleRevertToTenant · TEXT` |  |
| `IsAssetTooSpecializedForLessor` | Is Asset Too Specialized For Lessor? | This check box is Test 5 of the ASC 842 Test. Select this check box if the asset has a specialized use, such as that the lessor will have no alternative use for it. | Boolean | Global |  | `contract_financial_test.IsAssetTooSpecializedForLessor · TEXT` |  |
| `IsLeaseNearEnd` | Is the lease commencement at or near the end of the economic life of the asset? | This check box is in Test 3 of the ASC 842 Test. Select this check box if the lease commencement is at or near the end of the economic life of the asset. If this check box is selected, Test 3 s outcome will change to Pass regardless of whether the value the Test Term Length to Remaining Life field is greater than the Remaining Economic Life Threshold field. | Boolean | Global |  | `contract_financial_test.IsLeaseNearEnd · TEXT` |  |
| `IsLocked` | Is Locked? | Once you are certain that the results of your ASC 842 Test are correct, select this check box. Locking the test ensures that the test cannot be modified. You cannot delete a classification test once it has been locked, but you can create another test as necessary. | Boolean | Global |  | `contract_financial_test.IsLocked · TEXT` |  |
| `Test1Result` | Test #1 Result | This field displays the results of Test 1 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance lease. If you "pass" all tests, the lease will be considered an Operating lease. Test 1 asks if the ownership of the asset reverts to the tenant at the end of the lease term. | Boolean | Global |  | `contract_financial_test.Test1Result · TEXT` |  |
| `Test2Result` | Test #2 Result | This field displays the results of Test 2 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance lease. If you "pass" all tests, the lease will be considered an Operating lease. Test 2 asks if the lease contains a purchase option that the tenant is likely to exercise. | Boolean | Global |  | `contract_financial_test.Test2Result · TEXT` |  |
| `Test3Result` | Test #3 Result | This field displays the results of Test 3 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance lease. If you "pass" all tests, the lease will be considered an Operating lease. This test compares the Remaining Economic Life of the lease to the Test Begin and End Dates. If this value is below the Remaining Economic Life Threshold, your lease will pass this test. | Boolean | Global |  | `contract_financial_test.Test3Result · TEXT` |  |
| `Test4Result` | Test #4 Result | This field displays the results of Test 4 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance lease. If you "pass" all tests, the lease will be considered an Operating lease. This test determines whether you are paying more for the asset than the percentage of the asset you control, or whether the initial liability balance is less than or greater than the threshold fair value controlled. | Boolean | Global |  | `contract_financial_test.Test4Result · TEXT` |  |
| `Test5Result` | Test #5 Result | This field displays the results of Test 5 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance lease. If you "pass" all tests, the lease will be considered an Operating lease. This test asks if the asset has a specialized use, such as that the lessor will have no alternative use for it. | Boolean | Global |  | `contract_financial_test.Test5Result · TEXT` |  |

### Text & notes (15)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseName` | Base Name | This field displays the file name of the file attached to the record. | Text | Global |  | `contract_financial_test.BaseName · TEXT` |  |
| `DismantlingStorageCostDesc` | Dismantling / Restoring Cost Desc | Enter a description of the cost of any activity necessary to restore the asset to its original state prior to the expiration of the lease. | Text | Global |  | `contract_financial_test.DismantlingStorageCostDesc · TEXT` |  |
| `FairValueSource` | Fair Value Source | Enter the name of the person who assessed the fair value of the asset. | Text | Global |  | `contract_financial_test.FairValueSource · TEXT` |  |
| `FinalResult` | Final Result | The final result of the ASC 842 test. If you "failed" at least one of the five tests, your lease is considered a Finance lease. If you "passed" all five tests, your lease is considered an Operating lease. | Text | Global |  | `contract_financial_test.FinalResult · TEXT` |  |
| `ImpairmentsDesc` | Impairments Description | Enter a description of the costs related to the diminished value of the asset. | Text | Global |  | `contract_financial_test.ImpairmentsDesc · TEXT` |  |
| `InitialDirectCostsDesc` | Initial Direct Costs Description | Enter a description of the incremental costs of a lease that would not have been incurred if the lease had not been obtained. | Text | Global |  | `contract_financial_test.InitialDirectCostsDesc · TEXT` |  |
| `LeaseIncentivesDesc` | Lease Incentives Description | Enter a description of any incentive amounts that have reduced the cost of the lease. | Text | Global |  | `contract_financial_test.LeaseIncentivesDesc · TEXT` |  |
| `LineNumber` | Line Number | Enter the line number where the fair value is referenced in the lease document. | Text | Global |  | `contract_financial_test.LineNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `contract_financial_test.Notes · TEXT` |  |
| `PVOfOtherAdjustmentsDesc` | Other Adjustments Description | Enter a description of any other miscellaneous costs that should be accounted for in the schedule. | Text | Global |  | `contract_financial_test.PVOfOtherAdjustmentsDesc · TEXT` |  |
| `PVOfStructuringCostsDesc` | Structuring Costs Description | Enter a description of any fees paid to the owners of a special-purpose entity for structuring the transaction. | Text | Global |  | `contract_financial_test.PVOfStructuringCostsDesc · TEXT` |  |
| `PageNumber` | Page Number | Enter the page number where the fair value is referenced in the lease document. | Text | Global |  | `contract_financial_test.PageNumber · TEXT` |  |
| `ParagraphNumber` | Paragraph Number | Enter the paragraph number where the fair value is referenced in the lease document. | Text | Global |  | `contract_financial_test.ParagraphNumber · TEXT` |  |
| `PreCommencePayDesc` | Pre-Commencement Payments Description | Enter a description of the amount paid towards rent prior to the commencement date, minus any incentives that have reduced the cost of the lease. | Text | Global |  | `contract_financial_test.PreCommencePayDesc · TEXT` |  |
| `SectionNumber` | Section Number | This field is no longer in use. | Text | Global |  | `contract_financial_test.SectionNumber · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Contract Financial Test ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `contract_financial_test.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `contract_financial_test.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `contract_financial_test.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `contract_financial_test.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `contract_financial_test.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `contract_financial_test.RevNumber · TEXT` |  |
