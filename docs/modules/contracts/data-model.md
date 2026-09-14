# Contracts — data model

**Stated up front.** The contract financial engine is **55 objects** hanging off one aggregate root
(`Contract`) — 22 clause, 5 schedule, 5 transaction, 8 projection, 8 source-data, 3 link and 4 behaviour-carrying reference objects — totalling roughly 2,700 fields — about 44% of the entire 6,158-leaf product catalog.
Every one of them carries `ContractID(Contract ID)` as its parent key; there is no join table
between a contract and its financial children. The only many-to-many structures in the whole module
are three explicit link tables (`LinkLandlordInvPaymentTxn`, `LinkSchedOffsetExpGrpType`,
`ExpenseRecoveryItemMapping`). Everything else is a strict composition tree.

All field names, counts and declared types below are **Observed** from
`_lucernex_objects_summary.txt` (Lucernex's own `ShowObjectDetails.jsp` export). Human labels and
Global/Firm scope are **Observed** from `docs/data-fields/`. Physical Postgres column types are
**Observed** from `_crossmap.tsv`.

---

## 1. The object inventory

### L0 — Clause objects

| Object | PG table | Fields | Parent key | Clause markers |
|---|---|---:|---|---|
| `ExpenseSetup` | `expense_setup` | 96 | `ContractID` | `AmendmentID`, `CovenantID`, `Section` |
| `ExpenseAccrualSetup` | `expense_accrual_setup` | 31 | `ContractID` | `AmendmentID`, `CovenantID`, `Section`, `RevNumber` |
| `ExpenseEscalation` | `expense_escalation` | 28 | `ContractID` | `ExpenseSetupID`, `EscalationIndexID` |
| `ExpenseRecovery` | `expense_recovery_part1..part4` | 565 | `ContractID` | `AmendmentID`, `CovenantID`, `Section`, `RevNumber` |
| `PercentageRent` | `percentage_rent` | 45 | `ContractID` | `AmendmentID`, `CovenantID`, `Section` |
| `PercentageRentBreakpoint` | `percentage_rent_breakpoint` | 40 | `ContractID` | `RevNumber` |
| `SalesExclusion` | `sales_exclusion` | 19 | `ContractID` | `ExclusionGroupCapID`, `RevNumber` |
| `SalesExclusionCap` | `sales_exclusion_cap` | 23 | `ContractID` | `RevNumber` |
| `UseBasedRent` | `use_based_rent` | 23 | `ContractID` | `AmendmentID`, `CovenantID` |
| `UseBasedRentBreakpoint` | `use_based_rent_breakpoint` | 31 | `ContractID` | `RevNumber` |
| `AlternateRentSchedule` | `alternate_rent_schedule` | 25 | `ContractID` | `ExpenseSetupID`, `RevNumber` |
| `VariableRentOffset` | `variable_rent_offset` | 20 | `ContractID` | — |
| `ScheduledOffset` | `scheduled_offset` | 19 | `ContractID` | `VendorID`, `RevNumber` |
| `Allowance` | `allowance` | 23 | `ContractID` | `AmendmentID`, `CovenantID`, `Section` |
| `SecurityDeposit` | `security_deposit` | 25 | `ContractID` | `AmendmentID`, `CovenantID`, `Section`, `PartyID` |
| `Covenant` | `covenant` | 44 | `ContractID` | `AmendmentID`, `SectionNumber`, `ParagraphNumber`, `PageNumber`, `LineNumber` |
| `CoTenancy` | `co_tenancy` | 27 | `ContractID` | `AmendmentID`, `CovenantID`, `Section` |
| `ContractTerm` | `contract_term` | 26 | `ContractID` | `AmendmentID`, `CovenantID`, `Section` |
| `ContractAmendment` | `contract_amendment` | 20 | `ContractID` | — (it *is* the amendment) |
| `FinancialAdjustment` | `financial_adjustment` | 19 | `ContractID` | `CovenantID`, `RevNumber` |
| `ExpenseAllocation` | `expense_allocation` | 15 | `ContractID` | `ExpenseSetupID`, `OrganizationID` |
| `ExpenseVendorAllocation` | `expense_vendor_allocation` | 16 | `ContractID` | `ExpenseSetupID`, `VendorID`, `RevNumber` |

### L1 — Schedule objects

| Object | PG table | Fields | Generated from | State flags |
|---|---|---:|---|---|
| `ExpenseSchedule` | `expense_schedule` | 51 | `ExpenseSetupID` | `ProcessedFlag`, `ProcessedDate`, `ReadyForPaymentFlag`, `HoldFlag`, `CodeApprovalStatusID` |
| `ExpenseAccrualSchedule` | `expense_accrual_schedule` | 31 | `ExpenseAccrualSetupID` (typed `Text` — see §5) | `RevNumber` |
| `SLSummary` | `s_l_summary` | 134 | `GenerateStraightLineRent` / 842 / IFRS16 | `IsApproved`, `NeedsRecalculation`, `LastPostedDate` |
| `SLPeriod` | `s_l_period` | 79 | `SLSummaryID` | `PostedDate`, `RecordStatus` |
| `ContractFinancialTest` | `contract_financial_test` | 93 | classification run | — |

### L2 — Transaction objects

| Object | PG table | Fields | Provenance columns |
|---|---|---:|---|
| `PaymentTransaction` | `payment_transaction` | 118 | `ExpenseSetupID`, `ExpenseRecoveryID`, `PercentageRentID`, `AlternateRentScheduleID`, `ScheduledOffsetID`, `PropertyTaxBillID`, `AppliedToPayTranID`, `SourceEntityTable`, `CodeSourceEntityID` |
| `AccrualTransaction` | `accrual_transaction` | 55 | `ExpenseAccrualSetupID`, `SourceEntityTable` |
| `PaymentReceipt` | `payment_receipt` | 21 | `ContractID` only |
| `AllowanceTransaction` | `allowance_transaction` | 20 | `AllowanceID` |
| `PaymentTransactionFullImport` | *(none)* | 118 | field-for-field mirror of `PaymentTransaction` — an import staging buffer |

### L3 — Projection objects

| Object | PG table | Fields | Projects |
|---|---|---:|---|
| `VirtualSalesPeriod` | *(none)* | 66 | sales-period rent derivation, both buckets |
| `VirtualPercentageRentPeriod` | `virtual_percentage_rent_period` | 38 | breakpoint tiers per period |
| `VirtualPRAccrualPeriod` | `virtual_pr_accrual_period` | 20 | percentage-rent accrual, computed vs posted |
| `VirtualPRPAggregate` | `virtual_p_r_p_aggregate` | 16 | whole-rent-year percentage-rent obligation |
| `VirtualUsagePeriod` | `virtual_usage_period` | 66 | usage-period rent derivation (mirror of `VirtualSalesPeriod`) |
| `VirtualUseBasedRentPeriod` | `virtual_use_based_rent_period` | 23 | use-based breakpoint tiers per period |
| `VirtualExpenseForecastPeriod` | `virtual_expense_forecast_period` | 20 | forward expense forecast |
| `VirtualExpAccrualForecastPeriod` | `virtual_exp_accrual_forecast_period` | 13 | forward accrual forecast |

### Source-data objects (facts fed in from outside)

| Object | PG table | Fields | What it holds |
|---|---|---:|---|
| `Sales` | `sales` | 28 | Reported gross/net sales per fiscal period, plus six `SalesAdjustment1..6` slots |
| `Usage` | `usage` | 14 | Reported usage count and share per effective date |
| `EscalationIndex` | `escalation_index` | 12 | One published index value (CPI etc.) for one month/year |
| `LandlordInvoice` | `landlord_invoice` | 31 | An invoice received from the landlord |
| `LandlordInvoiceItem` | `landlord_invoice_item` | 28 | Its line items |
| `ExpenseRecoveryItem` | `expense_recovery_item` | 47 | CAM reconciliation line detail |
| `InvoiceIssue` / `InvoiceItem` | `invoice_issue` / `invoice_item` | 23 / 18 | Outbound invoicing batch (Specialized Forms group, not Contract) |
| `FacilityExpense` | `facility_expense` | 22 | Facility-level (not contract-level) expense actual/budget/planned/revised |

### Link tables (the only many-to-many)

| Object | PG table | Fields | Joins | Payload |
|---|---|---:|---|---|
| `LinkLandlordInvPaymentTxn` | `link_landlord_inv_payment_txn` | 13 | `LandlordInvoiceItemID` ↔ `PaymentTransactionID` | `AllocationAmount`, `AllocationDate`, `VarianceAmount`, `VarianceReason`, `ReconciliationStatus` |
| `LinkSchedOffsetExpGrpType` | `link_sched_offset_exp_grp_type` | 12 | `ScheduledOffsetID` ↔ (`CodeExpenseGroupID`, `CodeExpenseTypeID`) | — (pure link) |
| `ExpenseRecoveryItemMapping` | `expense_recovery_item_mapping` | 6 | `ExpenseRecoveryItemID` ↔ `DocumentID` | `InvoiceLineItemName`, `JSONConfigText` |

`LinkLandlordInvPaymentTxn` is the **three-way match**: it is where "what the landlord billed"
meets "what we paid", with the difference and its reason recorded on the join itself. That is a
model ASG Edge+ should copy verbatim.

`ExpenseRecoveryItemMapping` maps a free-text line-item name off a scanned landlord statement
(`InvoiceLineItemName`) onto a structured `ExpenseRecoveryItem`, with a `JSONConfigText` blob
holding the extraction configuration. **Inferred** purpose (document-to-line-item extraction
mapping) from the field set; not confirmed in the UI.

### Classification / reference objects that carry behaviour

| Object | PG table | Fields | Why it is not "just a code list" |
|---|---|---:|---|
| `CodeExpenseType` | `code_expense_type` | 31 | Carries **20 GL account-number slots** (`APExportBase/Prepaid/Tax1..4`, `ExpAccrualAcct1..4`, `PercentRentAccrualAcct1..4`, `RETaxAccrualAcct1..4`) **and** the accounting-treatment bindings `CodeASC842ScheduleID`, `CodeIFRS16ScheduleID`, `CodeSLScheduleID`. Choosing an expense type chooses both the GL coding and the lease-accounting treatment. |
| `CodeSLSchedule` | `code_s_l_schedule` | 24 | Carries `ExportAcct1..20Number` and `DontAmortizeAssetValue` |
| `FiscalPeriod` | `fiscal_period` | 17 | `Is4or5WeekPeriod`, `NumberWeeksInPeriod` — retail 4-5-4 calendar support, keyed by `ProgramID` (portfolio) |
| `DiscountRate` | `discount_rate` | 16 | Rate lookup keyed by `CodeAccountingMethodID` + `CodeContractUseID` + geography + `MinSchedMons`/`MaxSchedMons` term band |

---

## 2. The FK edge list

Every edge below is a declared, typed column. `→` reads "points at".

### Into `Contract`

```
Contract.FacilityID        → Facility          (type: Facility ID)
Contract.LocationID        → Location          (type: Location ID)
Contract.OrganizationID    → Organization      (type: Organization ID)
Contract.ComplexID         → Complex           (type: Complex ID)
Contract.ProgramID         → Portfolio         (type: Portfolio ID)   [name/label mismatch]
Contract.PrototypeID       → Prototype         (type: Prototype ID)
Contract.MasterContractID  → Contract          (type: Contract ID)    [SELF-REFERENCE]
Contract.NextAvailableTermID → ContractTerm    (type: Contract Term ID)
Contract.BudgetTemplateID  → Template          (type: Template ID)
Contract.RegionID / SubRegionID / RootRegionID → Region
Contract.JurisdictionID    → County
Contract.IStateProvinceCountryID → Country, State, County
Contract.DemographicDMAID  → DMA
Contract.Firm_LeaseAnalyst → Member            (type: Member ID)
```

Contract has **no Vendor/Employer FK**. See [`contract-hierarchy.md`](contract-hierarchy.md).

### Financial child → parent

```
ExpenseSetup.ContractID              → Contract
ExpenseSetup.AmendmentID             → ContractAmendment
ExpenseSetup.CovenantID              → Covenant
ExpenseSetup.VendorID                → Employer          (declared "Employer ID")
ExpenseSetup.ProjectEntityID         → Entity            (polymorphic root, see §4)

ExpenseSchedule.ExpenseSetupID       → ExpenseSetup      (type: Expense Setup ID)
ExpenseSchedule.ContractID           → Contract
ExpenseSchedule.ContractTermID       → ContractTerm
ExpenseSchedule.AssetID              → Equipment
ExpenseSchedule.PreviousExpenseScheduleID / NextExpenseScheduleID → ExpenseSchedule  [typed Text!]

ExpenseEscalation.ExpenseSetupID     → ExpenseSetup
ExpenseEscalation.EscalationIndexID  → EscalationIndex   (type: Escalation Index ID)

ExpenseAllocation.ExpenseSetupID     → ExpenseSetup
ExpenseAllocation.OrganizationID     → Organization
ExpenseVendorAllocation.ExpenseSetupID → ExpenseSetup
ExpenseVendorAllocation.VendorID     → Employer

AlternateRentSchedule.ExpenseSetupID → ExpenseSetup

PaymentTransaction.ContractID        → Contract
PaymentTransaction.ExpenseSetupID    → ExpenseSetup
PaymentTransaction.PercentageRentID  → PercentageRent    (type: Percentage Rent ID)
PaymentTransaction.AlternateRentScheduleID → AlternateRentSchedule
PaymentTransaction.PropertyTaxBillID → PropertyTaxBill
PaymentTransaction.AppliedToPayTranID → PaymentTransaction  [SELF-REFERENCE: credit application]
PaymentTransaction.VendorID          → Employer          (declared "Employer ID"; UI label "Vendor")
PaymentTransaction.OrganizationID    → Organization
PaymentTransaction.AssociatedDocumentID → Document
PaymentTransaction.FolderID          → Folder
PaymentTransaction.ExpenseRecoveryID → ExpenseRecovery   [typed Text!]
PaymentTransaction.ScheduledOffsetID → ScheduledOffset   [typed Text!]

AccrualTransaction.ExpenseAccrualSetupID → ExpenseAccrualSetup   [typed Text!]
AccrualTransaction.OrganizationID    → Organization

SalesExclusion.ExclusionGroupCapID   → SalesExclusionCap (type: Sales Exclusion Cap ID)

LandlordInvoice.EmployerID           → Employer
LandlordInvoiceItem.LandlordInvoiceID → LandlordInvoice  [typed Text!]

AllowanceTransaction.AllowanceID     → Allowance         (type: Allowance ID)
SecurityDeposit.PartyID              → Employer

SLPeriod.SLSummaryID                 → SLSummary         (type: Straight-Line Schedule ID)
ExpenseAccrualSchedule.ExpenseAccrualSetupID → ExpenseAccrualSetup [typed Text!]
ExpenseRecoveryItem.ExpenseRecoveryID → ExpenseRecovery  [typed Text!]
VirtualExpAccrualForecastPeriod.ExpenseAccrualScheduleID → ExpenseAccrualSchedule (typed properly)
```

### The seven weak FKs

Seven relationships are declared `Text` rather than as a typed FK, even though a proper FK type
for the target exists elsewhere in the same schema:

| Column | Should be | Evidence the type exists |
|---|---|---|
| `PaymentTransaction.ExpenseRecoveryID` | `Expense Recovery ID` | Manage Data Fields types the same leaf `sTYPE_EXPENSE_RECOVERY` |
| `PaymentTransaction.ScheduledOffsetID` | `Scheduled Offset ID` | Manage Data Fields types it `sTYPE_SCHEDULED_OFFSET` |
| `ExpenseSchedule.PreviousExpenseScheduleID` / `NextExpenseScheduleID` | `Expense Schedule ID` | Manage Data Fields types both `sTYPE_EXPENSE_SCHEDULE` |
| `ExpenseAccrualSchedule.ExpenseAccrualSetupID` | `Expense Accrual Setup ID` | — |
| `AccrualTransaction.ExpenseAccrualSetupID` | `Expense Accrual Setup ID` | — |
| `ExpenseRecoveryItem.ExpenseRecoveryID` | `Expense Recovery ID` | — |
| `LandlordInvoiceItem.LandlordInvoiceID` | `Landlord Invoice ID` | — |

**Observed** in both sources; the disagreement between View Object Model (`Text`) and Manage Data
Fields (`sTYPE_EXPENSE_SCHEDULE`) is itself observed and is exactly the pattern
[`../../admin/009-related-fields-and-data-model.md`](../../admin/009-related-fields-and-data-model.md)
documented for `VendorID` — presentation-layer type versus storage type. **Implication for ASG
Edge+: these are referential-integrity holes.** Every one of them is a parent-child edge on the
financial critical path. Model them as real FKs.

---

## 3. Physical storage: the four-table vertical partition

Two objects in this module are split across multiple Postgres tables:

| Object | Tables | Fields |
|---|---|---:|
| `Contract` | `contract_admin`, `contract_financial`, `contract_firm`, `contract_firm1` | 570 |
| `ExpenseRecovery` | `expense_recovery_part1`, `expense_recovery_part2`, `expense_recovery_part3`, `expense_recovery_part4` | 565 |

`Contract`'s split is **semantic** — administrative fields, financial fields, and two tables of
tenant custom fields. `ExpenseRecovery`'s split is **mechanical** — `part1..part4` is a column-count
workaround, ~141 columns each. Both are visible as multi-valued PG TABLE cells in
`_lucernex_objects_summary.txt`. **Observed.**

The `ExpenseRecovery` field export confirms the mechanical split directly: `ExpenseRecoveryID` and
`ModifiedDate` each appear **four times** in its field list — once per part table. Any rebuild must
not replicate this; it is a symptom of the field-per-variant modelling described in
[`expense-recovery-cam.md`](expense-recovery-cam.md).

---

## 4. `ProjectEntityID` — the polymorphic root

Almost every object in the module carries `ProjectEntityID(Entity ID)` **in addition to**
`ContractID(Contract ID)`. `Contract` itself carries both `ContractID(Number)` and
`ProjectEntityID(Number)`.

Reading, **Inferred**: `ProjectEntity` is a supertype spanning `Contract`, `Facility`, `Location`,
`Project`, `Asset`, `Portfolio` and the other aggregate roots enumerated in `walkHierarchy.jsp`'s
Show dropdown (per [009](../../admin/009-related-fields-and-data-model.md)). Financial children
carry it so that the same `ExpenseSetup`/`PaymentTransaction` machinery can hang off an equipment
contract or a capital project as easily as a real-estate lease — which is corroborated by
`ExpenseSchedule.AssetID(Equipment ID)`, `PaymentTransaction.AssetID(Equipment ID)` and the
`GENERATE_ASSET_RENT` / `DELETE_ASSET_PAYMENTS` / `EXTEND_ASSET_CONTRACTS` command family. **Not
confirmed** — no schema screen inspected named the discriminator column.

The corollary matters for ASG Edge+: `PaymentTransaction` is **not** a contract-only table. It is
the platform's single money-movement ledger, tenanted by `ProjectEntityID` and typed by
`SourceEntityTable`.

---

## 5. Postgres reality: every column is `TEXT`

`_crossmap.tsv` cross-maps 1,194 leaves onto real Postgres columns across 33 landed tables. The
type distribution is:

| PG type | Count |
|---|---:|
| `TEXT` | 1,163 |
| `VARCHAR(64) NOT NULL` | 31 (all primary keys) |

There are **no numeric, decimal, date or boolean columns at all**. Worked example, `sales`:

| Leaf label | Column | Catalog type | PG type |
|---|---|---|---|
| Gross Sales Amount | `sales.GrossSalesAmount` | `sTYPE_MONEY` | `TEXT` |
| Net Sales Amount | `sales.NetSalesAmount` | `sTYPE_MONEY` | `TEXT` |
| Sales Adjustment #1–#6 | `sales.SalesAdjustment1..6` | `sTYPE_MONEY` | `TEXT` |
| Effective Date | `sales.EffectiveDate` | `sTYPE_DATE` | `TEXT` |
| Unit Sales Count | `sales.UnitSalesCount` | `sTYPE_NUMBER` | `TEXT` |
| Sales RecID | `sales.SalesID` | `sTYPE_UNFORMATTED_NUMBER` | `VARCHAR(64) NOT NULL` (PK) |

Across the money-typed leaves specifically: 71 `sTYPE_MONEY`, 29 `sTYPE_PERCENTAGE`, 1
`sTYPE_MONEY_MATH_OPERATION` and 1 `sTYPE_PERCENT_OR_AMOUNT` all land as `TEXT`.

**This is the Constitution §4.4 headline hazard.** It is not a Lucernex application-layer choice
being reported here — the application layer types these fields correctly as money. It is the
*landed schema* being untyped. Whatever pipeline produced `_crossmap.tsv` is the boundary where
precision can be lost, and it is exactly the boundary ASG Edge+ will build a migration across.
Full register in [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md#41-typing-hazard-register-constitution-44).

---

## 6. Numeric precision types in use

| Catalog type | Meaning | Count (catalog-wide) | Where it matters here |
|---|---|---:|---|
| `sTYPE_MONEY` | Currency amount | 899 | everywhere |
| `sTYPE_MONEY_MATH_OPERATION` | **System-calculated** currency (not entered) | 262 | 233 of them are in `ExpenseRecovery` alone |
| `sTYPE_PERCENTAGE` | Percentage input | 188 | breakpoint rates, pro-rata share, caps |
| `sTYPE_PERCENT_MATH_OPERATION` | System-calculated percentage | 134 | 127 of them in `ExpenseRecovery` |
| `sTYPE_NUMBER_FRACTION6DIGITS` | Fixed 6 decimal places | 34 | usage unit-cost rates (`VirtualUsagePeriod`) |
| `sTYPE_PERCENT_OR_AMOUNT` | Toggle: percentage **or** flat amount in one field | 2 | `SLSummary.SLRemainingAssetBalance` is typed `Percent or Currency` |
| `sTYPE_MATH_OPERATION` / `sTYPE_DATE_MATH_OPERATION` | System-calculated number / date | 23 / 9 | `ExpenseRecovery.NumDaysInRecoveryPeriod` |

The `Number` vs `5-Digit Number` vs `2-Digit Number` vs `Number with no digits` distinctions in
the object-model export are display-precision hints, not storage types.
`VirtualPercentageRentPeriod.TrailingSalesMultiplier(5-Digit Number)` and
`VirtualUsagePeriod.GrossUsagePeriodCount(5-Digit Number)` are the ones that carry real
arithmetic weight.

---

## 7. The Contract sub-group taxonomy (2,678 fields across 97 sub-groups)

Aggregated from the `Notes (Group / Subgroup)` column of every `docs/data-fields/*.md` file, for
the `Contract` top group. **Derived** (counted from an Observed source).

| Fields | Sub-group | Backing object |
|---:|---|---|
| 117 | Payment Transaction | `PaymentTransaction` |
| 96 | Straight Line Summary | `SLSummary` |
| 79 | Expense Setup | `ExpenseSetup` |
| 78 | Straight Line Period | `SLPeriod` |
| 70 | Contract Info | `Contract` |
| 66 | Usage Period | `VirtualUsagePeriod` |
| 66 | Sales Period | `VirtualSalesPeriod` |
| 65 | Expense Recovery | `ExpenseRecovery` (config only) |
| 54 | Accrual Transaction | `AccrualTransaction` |
| 50 | Financial Test | `ContractFinancialTest` |
| 50 | Expense Schedule | `ExpenseSchedule` |
| **47** | **Common Area Maintenance** | **`Contract` — 100% Firm scope** |
| 46 | Expense Recovery Item | `ExpenseRecoveryItem` |
| 44 | Percentage Rent | `PercentageRent` |
| **44** | **Real Estate Taxes** | **`Contract` — 100% Firm scope** |
| 43 | Accounting Assumptions | `Contract` + `ContractFinancialTest` |
| 43 | Covenant | `Covenant` |
| 41 | Key Date | `KeyDate` |
| 39 | Percentage Rent Breakpoints | `PercentageRentBreakpoint` |
| 37 | Percentage Rent Schedule | `VirtualPercentageRentPeriod` |
| 34 / 30 / 28 / 28 | Financial – Calendar / Calendar w-Tax / Fiscal / Fiscal w-Tax | `Contract` rollups (§8) |
| 31 | Landlord Invoice | `LandlordInvoice` |
| 30 | Expense Accrual Setup / Schedule | `ExpenseAccrualSetup` / `ExpenseAccrualSchedule` |
| 30 | Use Based Rent Breakpoints | `UseBasedRentBreakpoint` |
| 29 | Expense Type | `CodeExpenseType` |
| 28 | Cap Lease Test | `Contract` |
| 28 | Landlord Invoice Item | `LandlordInvoiceItem` |
| 27 | Expense Escalation / Sales | `ExpenseEscalation` / `Sales` |
| 26 | Co Tenancy / Insurance | `CoTenancy` / `Insurance` |
| 25 | Security Deposit / Roll Forward Report | `SecurityDeposit` / `SLSummary` |
| 24 | Alternate Rent Schedule | `AlternateRentSchedule` |
| 22 | Use Based Rent Schedule / Sales Exclusion Cap / Use Based Rent | — |
| 21 | ASC 842 / IFRS 16 / SL Schedule Type | the three `Code*Schedule` tables |
| 20 | Allowance / Payment Receipt / Contract Dates / Expense Forecast | — |
| 19 | Expense Offset / Contract Amendment / PR Accrual Period | — |
| 18 | Accounting Assumptions Adjustments / Scheduled Offsets / Sales Exclusion / Financial Adjustment | — |
| 15 | Expense Vendor Allocation / Percentage Rent Summary Schedule (`VirtualPRPAggregate`) | — |
| 13 / 9 | Ongoing Co Tenancy / Opening Co Tenancy | `Contract` — 100% Firm scope |
| 8 | Delivery Requirements | `Contract` — 100% Firm scope |
| **×26** | **Statement Audit – …** (26 sub-groups, 434 fields) | `ExpenseRecovery` |

`docs/contracts-explained.html` states 2,823 fields under the Contract top group; this aggregation
finds 2,678 across 97 sub-groups. The ~145-field gap is unexplained and is an open question — most
likely sub-groups whose backing entity file groups them under a different top group. **Derived,
discrepancy noted.**

---

## 8. The code-table bands, refuted — with a better predictor

[`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md) records, as
**Derived**, that Lucernex's 207 platform code tables fall into two ID bands (2000–2190 and
3000–3016) and that the 3000-band tables are the behaviour-bearing ones. This module's field
inventory lets that be tested directly, and **it does not hold.**

The baseline code-table shape is exactly three fields — `ShortName`, `ActualLongName`, `Inactive`
(confirmed on `CodeSalesType`, `CodeSalesGroup`, `CodeBudgetColumnStatus`). Anything above three is
behaviour-bearing. Only **11 of the 207** code tables have a dedicated `Code*` object in the
223-object export at all; the rest are handled generically by `FirmCodeEdit.jsp`. All eleven, with
their bands:

| Band | Code table | Object | Fields | Behaviour-bearing? | What it carries beyond the baseline |
|---:|---|---|---:|:---:|---|
| **3013** | Expense Type | `CodeExpenseType` | 31 | **Yes** | 20 GL account slots, 3 accounting-treatment FKs, `ParentCodeExpenseGroupID` |
| **2161** | Straight Line Schedule Type | `CodeSLSchedule` | 24 | **Yes** | `ExportAcct1..20Number`, `DontAmortizeAssetValue` |
| **2162** | ASC 842 Schedule Type | `CodeASC842Schedule` | 24 | **Yes** | identical to 2161 |
| **2163** | IFRS 16 Schedule Type | `CodeIFRS16Schedule` | 24 | **Yes** | identical to 2161 |
| **2035** | Issue Type | `CodeIssueType` | 19 | **Yes** | 11 `IsValidFor*` attachability flags, `IsWorkFlow`, `SequencePrefix`, `IsSequencePerFirm`, `AutoClose`, `AllowReply` |
| **2047** | Asset Category | `CodeAssetCategory` | 6 | **Yes** | `GLNumber`, `SubAccount`, `DNEAmount(Currency)` |
| 3001 | Problem | `CodeProblem` | 4 | Marginal | `RemedyNote(Text)` |
| 2058 | Responsible Party | `CodeResponsibleParty` | 4 | Marginal | one FK to `Responsible Party System Code` |
| 3012 | Sales Type | `CodeSalesType` | 3 | **No** | baseline |
| 2144 | Sales Group | `CodeSalesGroup` | 3 | **No** | baseline |
| 2007 | Budget Column Status | `CodeBudgetColumnStatus` | 3 | **No** | baseline |

**Verdict: refuted.** Five of the six clearly behaviour-bearing code tables are in the **2000** band.
`CodeExpenseType` (3013) is the exception the original hypothesis generalised from, and the only
other 3000-band table with a modelled object at all — `CodeSalesType` (3012) — is a plain 3-field
lookup. Fourteen of the seventeen 3000-band tables (`Asset Type` 3000, `Amendment Type` 3002,
`Contract Type` 3003, `Covenant Type` 3004, `Facility Type` 3005, `Key Date Type` 3006,
`Location Type` 3007, `Parcel Type` 3008, `Usage Group` 3009, `Usage Type` 3010,
`Responsibility Type` 3011, `Parcel Access Type` 3014, `Recovery Type` 3015,
`Recovery Item Type` 3016) have **no object in the export**, so there is no evidence they carry
anything at all. **Observed** field counts; **Derived** verdict.

### What the 3000 band actually is

The band tracks **naming, not behaviour**: 3000 is the *primary `Type` discriminator of an entity*,
2000 is every other classification of that same entity plus all standalone lookups. The pattern is
near-perfect:

| Entity | Primary Type (3000 band) | Its other classifications (2000 band) |
|---|---|---|
| Contract | **Contract Type 3003** | Category 2092, Group 2093, Status 2094, Use 2095 |
| Covenant | **Covenant Type 3004** | Category 2156, Group 2096, Status 2157, Template 2097 |
| Facility | **Facility Type 3005** | Category 2105, Group 2106, Status 2107, Use 2108 |
| Location | **Location Type 3007** | Category 2116, Group 2117, Status 2118, Use 2119 |
| Parcel | **Parcel Type 3008** | Category 2123, Group 2124, Status 2125, Use 2126 |
| Asset | **Asset Type 3000** | Category 2047, Group 2002, Department 2001, Product Type 2004 |
| Recovery | **Recovery Type 3015**, **Recovery Item Type 3016** | Group 2179, Item Group 2180 |
| Sales | **Sales Type 3012** | Category 2143, Group 2144, Unit Sales Type 2133 |

Sixteen of seventeen fit. The exceptions are `Usage Group` (3009), which sits with `Usage Type`
(3010) while `Usage Category` (2135) and `Usage Unit Type` (2134) stay in the 2000 band; and
`Problem` (3001), whose name carries no entity at all. **Derived.**

### The predictor ASG Edge+ should actually use

Not the band. **"Does the code table have a dedicated object?"** — 11 do, 196 do not, and those 11
are precisely the ones that cannot be modelled as a `(code, label, active)` triple. That is the set
Configuration-Service's Masters model must be sized for. Two of them
(`CodeExpenseType`, `CodeAssetCategory`) carry **firm-specific GL account numbers** on what is
otherwise platform-global reference data, which is the hard case for the Hub/Spoke publish/accept
mechanism.

---

## Open questions

1. **What is the `ProjectEntity` supertype's discriminator column, and is `ProjectEntityID`
   globally unique across all entity types?** This determines whether ASG Edge+'s payment ledger
   can be single-table-polymorphic or needs separate ledgers per entity type. *(Check
   `ShowObjectDetails.jsp?sqlTableID=` for `ProjectEntity`.)*
2. **What does the ~145-field gap between 2,678 and 2,823 consist of?** *(Re-run the Manage Data
   Fields Contract-group export and diff.)*
3. **Are the seven weak (`Text`-typed) FKs enforced anywhere?** If Lucernex tolerates dangling
   `PaymentTransaction.ExpenseRecoveryID`, the migration needs an orphan-handling policy.
4. **Does `Contract`'s four-table split imply four separate row lifecycles**, or is it one row
   spread across four tables with a shared PK? *(Check whether `contract_firm1` rows can exist
   without a `contract_admin` row.)*
5. **Do the fourteen 3000-band code tables with no modelled object carry anything beyond
   `(ShortName, ActualLongName, Inactive)`?** (§8.) `Contract Type` (3003) and `Key Date Type`
   (3006) are the two that would most change this module if they did — the first is a candidate
   home for the master-lease/sublease role discriminator, the second for the lifecycle key-date
   taxonomy. Open each in `FirmCodeEdit.jsp` and count the columns.
6. **Which of the 33 landed Postgres tables in `_crossmap.tsv` are the complete set?** None of the
   core financial tables (`payment_transaction`, `expense_setup`, `expense_schedule`,
   `expense_recovery_part*`) appear in it — only `covenant`, `sales`, `usage`, `allowance`,
   `insurance`, `responsibility`, `party` do. Whether the financial tables land as `TEXT` too is
   **unverified** and is the highest-value single fact still missing.
