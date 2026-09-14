# Percentage & Sales Rent

Turnover and use-based rent: 17 record types, 472 fields, documented under the contracts module because the analysis sat naturally there.

## Sales feed overage

*Derived · capability · source: `docs/modules/contracts/percentage-rent.md`*

Tenant sales are imported, and percentage-rent terms compare sales against breakpoints. The record family covers the term, the sales periods, and the computed overage.

## Sales import step

*Observed · capability · source: `docs/modules/workflow/README.md`*

The single named entry point for sales data in the observed workflows is Lease Admin Request's 'Import Payment History/Sales' step - the product has no separate sales module.

## Rules (27)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### Final asset amount — [ACC-R-049](../rules/ACC-R-049.md)

*Observed · rule · source: `docs/modules/accounting/rules.md`*

**these four fields are "only made available on Finance contracts". `FinalAssetDate` defaults to the schedule end date; a later date amortizes beyond the schedule end.**

|  |  |
|---|---|
| When it fires | schedule generation on a Finance contract |
| What it reads | `SLSummary.FinalAssetAmount`, `.FinalAssetAllocPercent`, `.FinalAssetDate`, `.SLRemainingAssetBalance` |
| The test | these four fields are "only made available on Finance contracts". `FinalAssetDate` defaults to the schedule end date; a later date amortizes beyond the schedule end |
| What it writes | the asset balance remaining after the schedule end date |

### 3 Recurring expense — [CON-R-038](../rules/CON-R-038.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An expense is split across organizations: ExpenseAllocation apportions one clause across organizations by percentage.**

|  |  |
|---|---|
| Stated as | Splitting an expense across orgs |
| Stated as | `ExpenseAllocation.OrganizationID`, `.AllocationPercentage`, `.ExpenseSetupID` |
| Stated as | Allocates one clause across organizations by percentage |
| Stated as | Allocation set |
| Stated as | Observed |

### 3 Recurring expense — [CON-R-039](../rules/CON-R-039.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An expense is split across vendors: ExpenseVendorAllocation apportions one clause's payments across vendors by percentage; CHANGE_EXPENSE_ALLOCATION_VENDOR rewrites it.**

|  |  |
|---|---|
| Stated as | Splitting an expense across vendors |
| Stated as | `ExpenseVendorAllocation.VendorID`, `.PaymentPercentage`, `.APVendorNumber`, `.ExpenseSetupID` |
| Stated as | Allocates one clause's payments across vendors by percentage; `CHANGE_EXPENSE_ALLOCATION_VENDOR` rewrites it |
| Stated as | Vendor allocation set |
| Stated as | Observed |

### 4 Escalations — [CON-R-044](../rules/CON-R-044.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A per-step collar exists: collared = clamp(applied, PeriodMinPercentage, PeriodMaxPercentage).**

|  |  |
|---|---|
| Stated as | A per-step collar exists |
| Stated as | `PeriodMinPercentage`, `PeriodMaxPercentage` |
| Stated as | `collared = clamp(applied, min, max)` |
| Stated as | Collared change |
| Stated as | Derived |

### 4 Escalations — [CON-R-046](../rules/CON-R-046.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A lifetime collar exists: cumulative change across all steps is clamped by LifetimeMinPercentage/LifetimeMaxPercentage.**

|  |  |
|---|---|
| Stated as | A lifetime collar exists |
| Stated as | `LifetimeMinPercentage`, `LifetimeMaxPercentage` |
| Stated as | Cumulative change across all steps is clamped |
| Stated as | Cumulative bound |
| Stated as | Derived |

### 4 Escalations — [CON-R-047](../rules/CON-R-047.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An absolute ceiling exists: CapAmount/CapPercentage cap the escalated amount absolutely; order versus the collar above is unknown.**

|  |  |
|---|---|
| Stated as | An absolute ceiling exists |
| Stated as | `CapAmount`, `CapPercentage` |
| Stated as | The escalated amount is capped absolutely |
| Stated as | Capped amount |
| Stated as | Observed (fields); order vs collar unknown |

### Step 0 the two — [CON-R-050](../rules/CON-R-050.md)

*Observed · rule · source: `docs/modules/contracts/percentage-rent.md`*

**A percentage-rent period is projected: two independent date windows are produced — ReportingBucket{Begin,End,Due}Date and BillingBucket{Begin,End,Due}Date.**

### 5 Percentage rent — [CON-R-053](../rules/CON-R-053.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Exclusions share a cap group (ExclusionGroupCapID): PRPGrossExcludedAmount sums the raw excluded amounts within the group, before the cap.**

|  |  |
|---|---|
| Stated as | Exclusions share a cap group |
| Stated as | `SalesExclusion.ExclusionGroupCapID` → `SalesExclusionCap` |
| Stated as | `PRPGrossExcludedAmount = Σ rawExcluded` in the group |
| Stated as | Pre-cap total |
| Stated as | Derived |

### 5 Percentage rent — [CON-R-054](../rules/CON-R-054.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**A cap group is evaluated: PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent) — the effective cap, whichever binds first.**

|  |  |
|---|---|
| Stated as | A cap group is evaluated |
| Stated as | `SalesExclusionCap.CapAmount`, `.CapPercent`, `.PRPGrossSalesAmount` |
| Stated as | `PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent)` |
| Stated as | Effective cap |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-055](../rules/CON-R-055.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**The cap is applied: PRPNetExcludedAmount = min(gross, cap); PRPExcessExcludedAmount = gross − net — and the platform stores both numbers, which is what makes the min() reading solid rather than speculative.**

|  |  |
|---|---|
| Stated as | The cap is applied |
| Stated as | `PRPGrossExcludedAmount`, `PRPComputedCapAmount` |
| Stated as | `PRPNetExcludedAmount = min(gross, cap)`; `PRPExcessExcludedAmount = gross − net` |
| Stated as | Allowed / disallowed exclusion |
| Stated as | Derived (both fields exist as separate stored values) |

### 5 Percentage rent — [CON-R-056](../rules/CON-R-056.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Net sales are computed: NetSalesPeriodAmount = GrossSalesPeriodAmount − ExcludedSalesPeriodAmount.**

|  |  |
|---|---|
| Stated as | Net sales are computed |
| Stated as | Gross sales, `ExcludedSalesPeriodAmount` |
| Stated as | `NetSalesPeriodAmount = GrossSalesPeriodAmount − ExcludedSalesPeriodAmount`; likewise counts |
| Stated as | Net sales |
| Stated as | Derived |

### 5 Percentage rent — [CON-R-057](../rules/CON-R-057.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Sales periods roll into a rent period: PRPSalesAmount sums NetSalesPeriodAmount over every sales period inside the billing bucket.**

|  |  |
|---|---|
| Stated as | Sales periods roll into a rent period |
| Stated as | Net sales per sales period, `BillingBucket{Begin,End}Date` |
| Stated as | `PRPSalesAmount = Σ NetSalesPeriodAmount` inside the billing bucket |
| Stated as | Rent-period sales |
| Stated as | Derived |

### 5 Percentage rent — [CON-R-059](../rules/CON-R-059.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Tier rent is computed: PRPBreakpointRentDue_N = past_N × rate_N; PRPBreakpointRent = the sum across all eight tiers.**

|  |  |
|---|---|
| Stated as | Tier rent is computed |
| Stated as | `PRPSalesPastBreakpoint_N`, `PRPBreakpointRate_N` |
| Stated as | `PRPBreakpointRentDue_N = past_N × rate_N`; `PRPBreakpointRent = Σ` |
| Stated as | Tier rent |
| Stated as | Derived |

### Step 7 rent due and — [CON-R-062](../rules/CON-R-062.md)

*Inferred · rule · source: `docs/modules/contracts/percentage-rent.md`*

**Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets.**

|  |  |
|---|---|
| Stated as | Computed |
| Stated as | Posted |
| Stated as | `AccrualAmountThisPeriod` |
| Stated as | `PostedAccrualAmountThisPeriod` |
| Stated as | `AccrualAmountPriorPeriods` |
| Stated as | `PostedAccrualAmountPriorPeriods` |

### 5 Percentage rent — [CON-R-063](../rules/CON-R-063.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue.**

|  |  |
|---|---|
| Stated as | Percentage rent is billed |
| Stated as | `PRPRentDue`, `PercentageRent.CodeExpenseTypeID`/`CodeExpenseGroupID` |
| Stated as | A `PaymentTransaction` carrying `PercentageRentID` is generated |
| Stated as | L2 row |
| Stated as | Derived |

### 5 Percentage rent — [CON-R-064](../rules/CON-R-064.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**NaturalBreakpointFlag is set: naturalBreakpoint = annualMinimumRent / NaturalBreakpointRate — see the breakpoint entity above for why the numerator is unresolved.**

|  |  |
|---|---|
| Stated as | `NaturalBreakpointFlag = true` |
| Stated as | `NaturalBreakpointRate`, the contract's annual minimum rent |
| Stated as | `naturalBreakpoint = annualMinimumRent / NaturalBreakpointRate`. The numerator source is unconfirmed |
| Stated as | Derived tier-1 threshold |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-065](../rules/CON-R-065.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A natural breakpoint is derived: the configured rate and the effective rate are stored separately as the derivation's own audit trail.**

|  |  |
|---|---|
| Stated as | A natural breakpoint is derived |
| Stated as | `ConfiguredBreakpointRate1` vs `BreakpointRate1` on `VirtualPercentageRentPeriod` |
| Stated as | The configured rate and the effective rate are stored separately as the derivation's audit trail |
| Stated as | Audit pair |
| Stated as | Observed |

### 5 Percentage rent — [CON-R-066](../rules/CON-R-066.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**UseTrailing12MonthSales is set: replace the bucket sum with a rolling 12-month sum, scaled by TrailingSalesMultiplier for a partial history.**

|  |  |
|---|---|
| Stated as | `UseTrailing12MonthSales = true` |
| Stated as | `TrailingSalesMultiplier`, rolling 12-month sales |
| Stated as | Replace the bucket sum with a rolling 12-month window, scaled by the multiplier for partial history |
| Stated as | Trailing sales |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-067](../rules/CON-R-067.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**AnnualizeRent is set: scale a partial period's sales up to a full year, tier it, then scale the resulting rent back down.**

|  |  |
|---|---|
| Stated as | `AnnualizeRent = true` |
| Stated as | Partial-period sales, period length |
| Stated as | Scale sales to a full year, tier, then scale the rent back |
| Stated as | Annualised rent |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-068](../rules/CON-R-068.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**CumulativeFlag is set: accumulate year-to-date sales and rent, crediting rent already billed, instead of treating each period independently.**

|  |  |
|---|---|
| Stated as | `CumulativeFlag = true` |
| Stated as | Year-to-date sales and rent billed |
| Stated as | Accumulate YTD and credit rent already billed rather than treating each period independently |
| Stated as | Cumulative rent |
| Stated as | Inferred |

### 5 Percentage rent — [CON-R-069](../rules/CON-R-069.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A percentage-rent clause is flagged ExtFinalPeriodToLeaseExpDt: the final period extends to lease expiry instead of truncating at the usual period boundary.**

|  |  |
|---|---|
| Stated as | `ExtFinalPeriodToLeaseExpDt = true` |
| Stated as | `Contract.ExpireDate` |
| Stated as | The final percentage-rent period extends to lease expiry rather than truncating at the period boundary |
| Stated as | Final period end |
| Stated as | Observed (label) |

### The waterfall — [CON-R-081](../rules/CON-R-081.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**An admin-fee rate exists: AdminFeePercentageAmount = SubTotal1 × AdminFeePercentage.**

|  |  |
|---|---|
| Stated as | An admin-fee rate exists |
| Stated as | `{P}SubTotal1`, `{P}AdminFeePercentage` |
| Stated as | `AF%amt = ST1 × AF%` |
| Stated as | `{P}AdminFeePercentageAmount{G/N}` |
| Stated as | Derived |

### Grid structure and — [CON-R-093](../rules/CON-R-093.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**A recovery cap applies: the cap grows period over period by a percentage or a value, cumulatively or not.**

|  |  |
|---|---|
| Stated as | A recovery cap applies |
| Stated as | `CodeCapTypeID`, `CapPercentage`, `CapAmountChangePercent`, `CapAmountChangeValue`, `IsRecoveryCapEscalationNonCum` |
| Stated as | The cap is a growing cap: a starting amount escalating per period by a percentage or a value, cumulatively or not |
| Stated as | Effective cap |
| Stated as | Derived |

### Grid structure and — [CON-R-097](../rules/CON-R-097.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Escrow is trued up: reconcile the current escrow payment, propose a new estimate, and spread any shortfall over CatchUpNumberOfMonths.**

|  |  |
|---|---|
| Stated as | Escrow is trued up |
| Stated as | `CurrentEscrowPayment`, `EscalationPercentage`, `NewEscalationPayment`, `ProposedEscalationPayment`, `CatchUpNumberOfMonths`, `CatchUpPaymentAmount`, `ProposedCatchUpPaymentAmount`, `UPDATE_ESCROW` |
| Stated as | Reconcile, propose a new estimate, spread the shortfall over N months |
| Stated as | New escrow + catch-up |
| Stated as | Derived |

### 9 Payment lifecycle — [CON-R-123](../rules/CON-R-123.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Percentage-rent accrual is reconciled: VirtualPRAccrualPeriod's computed AccrualAmount{ThisPeriod,PriorPeriods,Total} is displayed next to the PostedAccrualAmount{...} that was actually posted, with IsPosted as the flag.**

|  |  |
|---|---|
| Stated as | Percentage-rent accrual is reconciled |
| Stated as | `VirtualPRAccrualPeriod.AccrualAmount{ThisPeriod,PriorPeriods,Total}` vs `PostedAccrualAmount{…}`, `IsPosted` |
| Stated as | Recomputed accrual is displayed against what was actually posted |
| Stated as | Reconciliation pair |
| Stated as | Observed |

### 13 Rent generation — [CON-R-152](../rules/CON-R-152.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An Expense Setup is generated from · `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates · One setup fans out to one transaction per allocation · The vendor split can change mid-term · Observed.**

|  |  |
|---|---|
| Stated as | An Expense Setup is generated from |
| Stated as | `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates |
| Stated as | One setup fans out to one transaction per allocation |
| Stated as | The vendor split can change mid-term |
| Stated as | Observed |

### D Purpose built — [RPT-R-036](../rules/RPT-R-036.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**`Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForecastPeriod` (20) and others — so a report can select from a….**

|  |  |
|---|---|
| Stated as | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForecastPeriod` (20) and others — so a report can select from a calculated period series with no materialisation step. |
| Stated as | Derived (naming pattern, 12 objects) + Inferred (non-persistence) |
| Stated as | `_lucernex_objects_summary.txt` |
