# Lease Accounting & Payments

*In scope for the rebuild*

ASC 842 / IFRS 16 / straight-line schedules, expense setups and their generated schedules, accruals, escalation indices, and the payment/invoice ledger.

Stated up front. Lx does not have "an ASC 842 module" and "an IFRS 16 module". It has one lease-accounting engine built on a single summary/period pair — SLSummary (s_l_summary, 134 fields) and SLPeriod (s_l_period, 79 fields) — and three mutually exclusive boolean flags on the summary (IsSLSchedule, IsASC842Schedule, IsIFRS16Schedule) that say which standard a given schedule was generated under. Classification (operating vs. finance) is a separate record, ContractFinancialTest (contract_financial_test, 93 fields), which runs the five ASC 842 tests and holds both the ASC 842 and IFRS 16 measurement results side by side. A third, older test — the "Cap Lease Test" — still lives directly on Contract as Test1Result…Test5aResult/Test5bResult and is the ASC 840 predecessor. All three coexist in the schema.

|  | Count |
|---|---|
| Record types | 38 |
| Fields | 1,265 |
| Keys in | 1 |
| Keys out | 146 |
| Rules | 62 |

## What was found here

### One engine, three standards

**Observed.** There is no separate ASC 842 module. There is one summary/period pair — SLSummary with 134 fields and SLPeriod with 79 — plus three mutually exclusive flags saying which standard a schedule was produced under.

### Classification is a separate record

**Observed.** ContractFinancialTest, 93 fields, runs the five ASC 842 tests and holds ASC 842 and IFRS 16 results side by side. An older ASC 840 Cap Lease Test still sits directly on Contract.

### Schedules are approved, not published

**Observed.** The ASC 842 Schedule Review/Approval workflow gates output: generate, initial review, ASG approve, client approve. The rebuild needs a schedule state machine, not just a calculator.

### This tenant runs ASC 842 only

**Observed.** The ASC 842 Schedule Type table holds exactly one value, 842 Rent. The Straight Line and IFRS 16 schedule-type tables are both empty. The capability is present and unused — whether the rebuild needs IFRS 16 is a business question.

### Amortisation has a policy switch

**Observed.** GaapAmortizeMode has exactly two values: PER_DAY and PER_PERIOD.

### Every non-key column is TEXT

**Observed.** In the physical Postgres export, 6,882 of 7,069 columns are TEXT, currency and percentage included. The other 187 are all primary keys. There is no numeric typing to inherit.

### Some fields are magnitude-typed

**Observed.** SLSummary.SLRemainingAssetBalance is read as a percentage when 0 to 100 and as currency at 100.01 and above. A genuine data-integrity hazard to design out.

### GL account slots are numbered, not named

**Observed.** Each schedule type carries ExportAcct1Number through ExportAcct20Number. Which accounting concept each slot represents — lease liability, ROU asset, interest expense, amortisation — is recorded nowhere in the schema.

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [SLSummary](../entities/SLSummary.md) | `s_l_summary` | 134 | 2 |
| [PaymentTransaction](../entities/PaymentTransaction.md) | `payment_transaction` | 118 | 4 |
| [PaymentTransactionFullImport](../entities/PaymentTransactionFullImport.md) | `—` | 118 | 0 |
| [ExpenseSetup](../entities/ExpenseSetup.md) | `expense_setup` | 96 | 10 |
| [SLPeriod](../entities/SLPeriod.md) | `s_l_period` | 79 | 0 |
| [AccrualTransaction](../entities/AccrualTransaction.md) | `accrual_transaction` | 55 | 0 |
| [ExpenseSchedule](../entities/ExpenseSchedule.md) | `expense_schedule` | 51 | 0 |
| [CodeExpenseType](../entities/CodeExpenseType.md) | `code_expense_type` | 31 | 0 |
| [ExpenseAccrualSchedule](../entities/ExpenseAccrualSchedule.md) | `expense_accrual_schedule` | 31 | 1 |
| [ExpenseAccrualSetup](../entities/ExpenseAccrualSetup.md) | `expense_accrual_setup` | 31 | 0 |
| [LandlordInvoice](../entities/LandlordInvoice.md) | `landlord_invoice` | 31 | 0 |
| [ExpenseEscalation](../entities/ExpenseEscalation.md) | `expense_escalation` | 28 | 0 |
| [LandlordInvoiceItem](../entities/LandlordInvoiceItem.md) | `landlord_invoice_item` | 28 | 0 |
| [AlternateRentSchedule](../entities/AlternateRentSchedule.md) | `alternate_rent_schedule` | 25 | 2 |
| [CodeASC842Schedule](../entities/CodeASC842Schedule.md) | `code_a_s_c842_schedule` | 24 | 0 |
| [CodeIFRS16Schedule](../entities/CodeIFRS16Schedule.md) | `code_i_f_r_s16_schedule` | 24 | 0 |
| [CodeSLSchedule](../entities/CodeSLSchedule.md) | `code_s_l_schedule` | 24 | 0 |
| [InvoiceIssue](../entities/InvoiceIssue.md) | `invoice_issue` | 23 | 0 |
| [PaymentReceipt](../entities/PaymentReceipt.md) | `payment_receipt` | 21 | 1 |
| [PurchaseOrder](../entities/PurchaseOrder.md) | `purchase_order` | 20 | 2 |
| [VariableRentOffset](../entities/VariableRentOffset.md) | `variable_rent_offset` | 20 | 0 |
| [VirtualExpenseForecastPeriod](../entities/VirtualExpenseForecastPeriod.md) | `virtual_expense_forecast_period` | 20 | 0 |
| [AcctingAssumptionAdjust](../entities/AcctingAssumptionAdjust.md) | `accting_assumption_adjust` | 19 | 0 |
| [FinancialAdjustment](../entities/FinancialAdjustment.md) | `financial_adjustment` | 19 | 0 |
| [ScheduledOffset](../entities/ScheduledOffset.md) | `scheduled_offset` | 19 | 0 |
| [InvoiceItem](../entities/InvoiceItem.md) | `invoice_item` | 18 | 0 |
| [FiscalPeriod](../entities/FiscalPeriod.md) | `fiscal_period` | 17 | 0 |
| [DiscountRate](../entities/DiscountRate.md) | `discount_rate` | 16 | 0 |
| [ExpenseVendorAllocation](../entities/ExpenseVendorAllocation.md) | `expense_vendor_allocation` | 16 | 0 |
| [ExpenseAllocation](../entities/ExpenseAllocation.md) | `expense_allocation` | 15 | 0 |
| [PayApp](../entities/PayApp.md) | `pay_app` | 15 | 0 |
| [LinkLandlordInvPaymentTxn](../entities/LinkLandlordInvPaymentTxn.md) | `link_landlord_inv_payment_txn` | 13 | 0 |
| [VirtualExpAccrualForecastPeriod](../entities/VirtualExpAccrualForecastPeriod.md) | `virtual_exp_accrual_forecast_period` | 13 | 0 |
| [EscalationIndex](../entities/EscalationIndex.md) | `escalation_index` | 12 | 1 |
| [LinkReceiptTransaction](../entities/LinkReceiptTransaction.md) | `link_receipt_transaction` | 12 | 0 |
| [LinkSchedOffsetExpGrpType](../entities/LinkSchedOffsetExpGrpType.md) | `link_sched_offset_exp_grp_type` | 12 | 0 |
| [CPI](../entities/CPI.md) | `c_p_i` | 10 | 0 |
| [RecalcOverrideNotes](../entities/RecalcOverrideNotes.md) | `recalc_override_notes` | 7 | 1 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [ACC-R-001](../rules/ACC-R-001.md) | Default discount rate resolution ↑ upgraded | resolve Portfolio-level rate first; if none exists, Firm-level rate. Do not read the contract-level rate | Observed |
| [ACC-R-002](../rules/ACC-R-002.md) | Contract-level discount rate override | if `Contract.DiscountRate` is populated it is the rate used; otherwise `ComputedSLDiscountRate` | Inferred |
| [ACC-R-003](../rules/ACC-R-003.md) | Asset-level discount rate override | if populated, it supersedes ACC-R-001/002 for that asset | Observed |
| [ACC-R-004](../rules/ACC-R-004.md) | Discount rate applicability scoping | a blank `CodeAccountingMethodID` matches both Finance and Operating. `MinSchedMons`/`MaxSchedMons` bound the schedule length in months for which the rate applies | Observed |
| [ACC-R-005](../rules/ACC-R-005.md) | Test 1: title transfer | `DoesTitleRevertToTenant = true` ⇒ Fail; false ⇒ Pass | Observed |
| [ACC-R-006](../rules/ACC-R-006.md) | Test 2: purchase option reasonably certain to be exercised | true ⇒ Fail; false ⇒ Pass | Observed |
| [ACC-R-007](../rules/ACC-R-007.md) | Test 3: major part of remaining economic life | `< RemainingEconomicLifeThreshold` ⇒ Pass; otherwise Fail. Default threshold "usually set to 75%" | Observed |
| [ACC-R-008](../rules/ACC-R-008.md) | Test 3 override: commencement near end of economic life | `IsLeaseNearEnd = true` ⇒ `Test3Result := Pass`, unconditionally | Observed |
| [ACC-R-009](../rules/ACC-R-009.md) | Test 4: substantially all of fair value | `InitialLiabilityBalance > ThresholdFairValueControlled` ⇒ Fail. Default threshold "usually set to 90%" | Observed |
| [ACC-R-010](../rules/ACC-R-010.md) | Test 5: specialised asset | true ⇒ Fail; false ⇒ Pass | Observed |
| [ACC-R-011](../rules/ACC-R-011.md) | ⚠ Final classification (inverted polarity) | any result = Fail ⇒ `Finance`; all five = Pass ⇒ `Operating` | Observed |
| [ACC-R-012](../rules/ACC-R-012.md) | Accounting method override | if populated, the override supersedes the computed `CodeAccountingMethodID` | Derived |
| [ACC-R-013](../rules/ACC-R-013.md) | Test locking | a locked test cannot be modified and cannot be deleted. Superseding is by creating a new `ContractFinancialTest` row | Observed |
| [ACC-R-014](../rules/ACC-R-014.md) | Propagation of the authoritative result | take the most recently locked row's `FinalResult` | Observed |
| [ACC-R-015](../rules/ACC-R-015.md) | Auto-computation marker | `ContractFinancialTest.AutoComputed := true` | Observed |
| [ACC-R-016](../rules/ACC-R-016.md) | Term-length sourcing | - `TermLength = ExpireDate − CommenceDate` (the contractual term); - `LikelyTermLength` = length through the last term marked Likely on `Abstract Info > Terms`; - `LastLikelyOptionDate` = end date of  | Observed |
| [ACC-R-017](../rules/ACC-R-017.md) | Accounting date window | `Topic842BeginDate = max(adoption date, PossessionBeginDate)`; `Topic842EndDate` = end of accounting including likely options | Observed |
| [ACC-R-018](../rules/ACC-R-018.md) | Asset-level accounting date override (equipment leases) | if the override dates are populated they set the test/schedule window; otherwise the window comes from the expense schedule dates | Observed |
| [ACC-R-019](../rules/ACC-R-019.md) | Covenant-sourced measurement adjustments | the covenant amount is pulled into the accounting assumptions and the accounting schedule only if `CodeAccountingAdjustmentTypeID` ∈ {`Purchase Option`, `Cancellation Option`, `Residual Value Guarante | Observed |
| [ACC-R-020](../rules/ACC-R-020.md) | Schedule-type change dirties the schedule | `SLSummary.NeedsRecalculation := true` | Observed |
| [ACC-R-021](../rules/ACC-R-021.md) | New expense setup dirties the schedule that uses its expense type | the accounting schedule associated with that expense type is dirtied | Observed |
| [ACC-R-022](../rules/ACC-R-022.md) | Accounting method change requires remeasurement | the schedule must be remeasured | Observed |
| [ACC-R-023](../rules/ACC-R-023.md) | Recalculation audit trail | `RecalcTriggerDate := today`; `NeedsRecalcModifiedByLastMember := current member`; current member appended to `NeedsRecalcModifiedByMemberIDList` | Observed |
| [ACC-R-024](../rules/ACC-R-024.md) | Recalculation override | a `RecalcOverrideNotes` row linked by `SLSummaryID`; the id appended to `SLSummary.RecalcOverrideNotesIDList` | Derived |
| [ACC-R-025](../rules/ACC-R-025.md) | Cash-flow routing by expense type | each period cash flow is routed to the schedule type its expense type designates for the standard being generated | Derived |
| [ACC-R-026](../rules/ACC-R-026.md) | Secondary schedule allocation | the stated percentage of the amount is allocated to a secondary schedule; the remainder to the primary | Observed |
| [ACC-R-027](../rules/ACC-R-027.md) | Schedule-type flag stamping | `SLSummary.IsSLSchedule` / `.IsASC842Schedule` / `.IsIFRS16Schedule := true` respectively | Derived |
| [ACC-R-028](../rules/ACC-R-028.md) | Period row generation | one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber` | Derived |
| [ACC-R-029](../rules/ACC-R-029.md) | GL account denormalization | copied verbatim onto `SLPeriod.ExportAcct1Number` … `ExportAcct20Number` | Derived |
| [ACC-R-030](../rules/ACC-R-030.md) | Suppress ROU asset amortization | if true, no asset amortization is recognised for schedules of this type | Inferred |
| [ACC-R-031](../rules/ACC-R-031.md) | Initial liability balance | `InitialLiabilityBalance = Σ PVOfPeriodCashAmount` | Observed |
| [ACC-R-032](../rules/ACC-R-032.md) | Present value of a period payment | discount the cash payment from the period it is made back to the accounting begin date | Observed |
| [ACC-R-033](../rules/ACC-R-033.md) | Initial asset balance | not documented. The vendor says only "This is a calculated value which contains the initial value over the asset of the lease." | Inferred |
| [ACC-R-034](../rules/ACC-R-034.md) | Balance forward and its split | ``` BalanceForward = InitialAssetBalance − InitialLiabilityBalance BalanceForward = RemeasurementBalanceForward + ProfitAndLossImpact ``` | Observed |
| [ACC-R-035](../rules/ACC-R-035.md) | Total commitment | `TotalCommitment = Σ` all rent payments for the life of the lease | Observed |
| [ACC-R-036](../rules/ACC-R-036.md) | Remaining cash balance | `CurrentRemainingCashBalance` = sum of current and future remaining lease payments; `CurrentRemainingCashBalanceAfterReportEnd` = the same excluding the current period | Observed |
| [ACC-R-037](../rules/ACC-R-037.md) | Straight-line expense and deferral | ``` PeriodExpenseAmount[n] = total cash rent straight-lined over the schedule life PeriodDeferredAmount[n] = PeriodCashAmount[n] − PeriodExpenseAmount[n] CumulativeDeferredBalance[n] = Σ(1..n) PeriodD | Observed |
| [ACC-R-038](../rules/ACC-R-038.md) | Interest expense | `PeriodInterestAmount[n]` = interest owed on the liability, at the discount rate | Observed |
| [ACC-R-039](../rules/ACC-R-039.md) | Accumulated amortization recurrence | ``` CumulativeAssetAmortExpense[1] = PeriodAssetAmortizationExpense[1] CumulativeAssetAmortExpense[n] = PeriodAssetAmortizationExpense[n] + CumulativeAssetAmortExpense[n−1] ``` | Observed |
| [ACC-R-040](../rules/ACC-R-040.md) | Gross asset balance | `GrossAssetBalance[n] = AssetAmount[n] + CumulativeAssetAmortExpense[n]` | Observed |
| [ACC-R-041](../rules/ACC-R-041.md) | Short-term / long-term split | ``` Forward12MonthAssetChange[n] = Σ asset amortization, periods n+1 … n+12 Forward12MonthLiabilityChange[n] = Σ liability amortization, periods n+1 … n+12 ShortTermRentExpense[n] = Σ rent expense, ne | Observed |
| [ACC-R-042](../rules/ACC-R-042.md) | Which short-term liability is reported | `Liability Amortization Based` ⇒ use `Forward12MonthLiabilityAmortBased`; `PV Based` ⇒ use `Forward12MonthLiabilityPVBased` | Observed |
| [ACC-R-043](../rules/ACC-R-043.md) | Currency translation | ``` AssetTranslationAdjustment = AssetBalance[n] + AssetAmortizationExpense[n] − AssetBalance[n−1] LiabilityTranslationAdjustment = AssetBalance[n] + (Payment[n] − Interest[n]) − AssetBalance[n−1] Cum | Observed |
| [ACC-R-044](../rules/ACC-R-044.md) | Translation vs. revaluation mapping | `Contract.IsTranslation = true` ⇒ use the Translation mapping on `Admin > Manage Company > Financial Settings`; false ⇒ the Revaluation mapping | Observed |
| [ACC-R-045](../rules/ACC-R-045.md) | Schedule supersession | ``` new.PriorLastPostedPeriodID := old.SLSummaryID new.PostedEndDate := old.LastPostedEndDate new.PostedInitAssetAdj := new.InitialAssetBalance − old.AssetBalance(as of PostedEndDate) new.PostedInitLi | Observed |
| [ACC-R-046](../rules/ACC-R-046.md) | Mid-period remeasurement split | `InterestBeforeMidRemeasure` = partial interest from period start to the remeasurement date; `SleBeforeMidRemeasure` = partial single lease expense over the same span | Observed |
| [ACC-R-047](../rules/ACC-R-047.md) | Term shortening | ``` ShortenedSchedInitLiabilityBal = initial liability over the remaining periods of the original schedule, restated over the shortened term ShortenedLeaseLiabilityDiff = ShortenedSchedInitLiabilityBa | Observed |
| [ACC-R-048](../rules/ACC-R-048.md) | Impairment | `TotalImpairmentImpact = ImpairmentAmount + PriorAccumulatedAmortizationBalance`, where `PriorAccumulatedAmortizationBalance` is "the Accumulated Amortization Balance of the accounting period prior to | Observed |
| [ACC-R-049](../rules/ACC-R-049.md) | Final asset amount / residual carve-out | these four fields are "only made available on Finance contracts". `FinalAssetDate` defaults to the schedule end date; a later date amortizes beyond the schedule end | Observed |
| [ACC-R-050](../rules/ACC-R-050.md) | Approval is irreversible ↑ upgraded | `SLSummary.IsApproved := true`, and cannot be reversed through the application | Observed |
| [ACC-R-051](../rules/ACC-R-051.md) | Posting state and the closed cut-line | `SLSummary.LastPostedDate` = begin date of the last posted period; `LastPostedEndDate` = its end date; `LastBalancePosted` = "the asset minus the liability as of the last posted period"; `LastPostedBa | Observed |
| [ACC-R-052](../rules/ACC-R-052.md) | Accrual amount derivation | entering any one of annual amount / period amount / accrual rate auto-populates the other two plus `FirstPaymentAmount` and `LastPaymentAmount`. Rate-based entry requires `RentableArea` to be populate | Observed |
| [ACC-R-053](../rules/ACC-R-053.md) | Accrual transaction tax handling | - `TaxesIncludedFlag = false` ⇒ `TotalAmount = PeriodAmount + Σ TaxAmountN`, `TotalAmount` read-only. - `TaxesIncludedFlag = true` ⇒ `PeriodAmount` becomes disabled, the system subtracts the tax amoun | Observed |
| [ACC-R-054](../rules/ACC-R-054.md) | Accrual transaction immutability | "Warning - once you mark a transaction as processed, you cannot change it." | Observed |
| [ACC-R-055](../rules/ACC-R-055.md) | Alternate-rent hold propagation | a hold flag is set on all recurring-expense transactions (resp. percentage-rent transactions) generated during the window | Observed |
| [ACC-R-056](../rules/ACC-R-056.md) | Amortisation basis: Per Day or Per Period | - `PER_PERIOD` ⇒ "distributes the amortization equally among periods"; - `PER_DAY` ⇒ "distributes the amortization according to the number of days in the period", i.e. weight each period by `SLPeriod. | Observed |
| [ACC-R-057](../rules/ACC-R-057.md) | 28-day proration of partial first and last periods | when true, prorate the partial period on a 28-day multiplier; and "If you have a partial period that is greater than or equal to 28 days, it will be considered a whole period by the system and will no | Observed |
| [ACC-R-058](../rules/ACC-R-058.md) | Fiscal / calendar year-end matching | "This field determines if the program allows for matching of fiscal/calendar year rent." | Observed |
| [ACC-R-059](../rules/ACC-R-059.md) | Per-column FX rate-type selection | the `Sub` variant applies to "contracts in need of translation", the plain variant to "contracts in need of revaluation" — selected per contract by `Contract.IsTranslation` (`ACC-R-044`) | Observed |
| [ACC-R-060](../rules/ACC-R-060.md) | ⚠ Schedules are not auto-published | on completion of step 3, `SLSummary.IsApproved := true` (`ACC-R-050`) | Observed |
| [ACC-R-061](../rules/ACC-R-061.md) | What an ASC 842 review request may be raised against | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Pr | Observed |
| [ACC-R-062](../rules/ACC-R-062.md) | Approver resolution | all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position | Observed |
