# Percentage rent

**Stated up front.** Percentage rent in Lucernex is a **two-clock, two-bucket, eight-tier**
calculation. Sales are *reported* on one frequency and rent is *billed* on another
(`CodeReportingFrequencyID` vs `CodeBillingFrequencyID`), so `VirtualSalesPeriod` carries two
independent date windows — `ReportingBucket*` and `BillingBucket*` — for the same period. Within
the billing bucket, net sales are run through up to **eight** breakpoint tiers, each with an
amount, a count and a rate; the tier rents are summed, clamped between a floor and a cap, reduced
by offsets and by rent already paid, and the remainder is posted as a `PaymentTransaction` carrying
`PercentageRentID`.

The single most important modelling decision Lucernex makes: a **natural** breakpoint is not stored
as an amount. `PercentageRentBreakpoint.NaturalBreakpointRate` stores the *rate*, and the amount is
derived from base rent. `VirtualPercentageRentPeriod` then carries **both**
`ConfiguredBreakpointRate1` (what the analyst typed) and `BreakpointRate1` (what the engine used) —
the audit trail for that derivation.

Every field name and type below is **Observed** from `_lucernex_objects_summary.txt`; every human
label is **Observed** from `docs/data-fields/`. The arithmetic in §4 is **Inferred** from field
names and labels, and each step is marked with its confidence.

---

## 1. The five objects

| Layer | Object | Fields | Role |
|---|---|---:|---|
| L0 clause | `PercentageRent` | 45 | The clause: type, frequencies, cap/floor, due-day offsets, sales-year boundary, audit right |
| L0 clause | `PercentageRentBreakpoint` | 40 | The tier table: 8 × (amount, count, rate) + the natural rate, date-windowed and `RevNumber`-versioned |
| L0 clause | `SalesExclusion` (19) + `SalesExclusionCap` (23) | 42 | What sales categories are excluded, at what rate, subject to what cap |
| Fact | `Sales` | 28 | Reported gross/net sales per fiscal period, with six adjustment slots |
| L1/L3 | `VirtualSalesPeriod` (66), `VirtualPercentageRentPeriod` (38) | 104 | The computed period: buckets, tiers, tier rents, cap/floor clamp, rent due |
| L3 | `VirtualPRPAggregate` (16), `VirtualPRAccrualPeriod` (20) | 36 | Rent-year rollup and accrual, computed vs posted |
| L2 | `PaymentTransaction` via `PercentageRentID` | — | The posting |

Supporting: `AlternateRentSchedule` (25) can substitute a different percentage-rate formula for a
window and can force-hold the normal percentage-rent run (`SetPRHoldFlag`);
`VariableRentOffset` (20) and `ScheduledOffset` (19) reduce the amount due.

---

## 2. `PercentageRent` — the clause, field by field

| Field | Type | What it controls |
|---|---|---|
| `CodePercentageRentTypeID` | `Dropdown (Percentage Rent Type Code)` | The variant of the calculation. **Members unknown — open question 1.** |
| `CodeReportingFrequencyID` | `Dropdown (Frequency Code)` | How often the tenant *reports* sales → drives `ReportingBucket*` |
| `CodeBillingFrequencyID` | `Dropdown (Frequency Code)` | How often percentage rent is *billed* → drives `BillingBucket*` |
| `CodeCapFrequencyID` | `Dropdown (Frequency Code)` | The window the `CapAmount` applies over (a monthly cap ≠ an annual cap) |
| `CapAmount` / `FloorAmount` | `Currency` | Clamp bounds on the computed rent |
| `OffsetAmount` | `Currency` | A flat reduction applied to the clause |
| `NaturalBreakpointFlag` | `Boolean` | Natural (derive the breakpoint from base rent) vs artificial (use the stated amounts) |
| `CumulativeFlag` | `Boolean` | Year-to-date cumulative accumulation vs each period standing alone |
| `AnnualizeRent` | `Boolean` | Scale a partial period's sales to a full year before applying tiers |
| `UseTrailing12MonthSales` | `Boolean` | Use a rolling 12-month sales window instead of the period's own sales |
| `UseCountBasedRate` | `Boolean` | Tier on **unit count** (`BreakpointCount1..8`) instead of sales **amount** (`BreakpointAmount1..8`) |
| `IsPartialTerm` | `Boolean` | The clause covers less than a full rent year |
| `IsMidMonth` | `Boolean` | Period boundaries fall mid-month |
| `ExtFinalPeriodToLeaseExpDt` | `Boolean` | Stretch the last period to the lease expiration date rather than truncating |
| `RentYearStartMonth` | `Dropdown` | The rent year's start month — independent of the fiscal calendar |
| `SalesYearEndDate` | `Date` | The sales year's end — independent again |
| `CodeProrationMethodID` | `Dropdown (Proration Method Code)` | How a partial period is prorated |
| `CodeSalesGroupID` | `Dropdown (Sales Group)` | Which sales stream feeds this clause |
| `CodeStoreTypeID` | `Dropdown (Store Type Code)` | Store classification (drives different rates in some leases) |
| `AnnualReportDueDays` / `PeriodReportDueDays` | `Number` | Days after period end that the sales **report** is due |
| `AnnualPaymentDueDays` (label: *Last Payment Due Offset Days*) / `PeriodPaymentDueDays` | `Number` | Days after period end that the **payment** is due → `BillingBucketDueDate` |
| `AuditRightFlag` | `Boolean` | Landlord may audit reported sales |
| `Firm_CertifiedSales` | `Boolean` (Firm) | ASG tenant flag: sales must be certified before billing |
| `CodeExpenseGroupID` / `CodeExpenseTypeID` | `Dropdown` | The GL classification the resulting payment inherits |
| `CovenantID` / `AmendmentID` / `Section` | FK / `Text` | Clause provenance |
| `BeginDate` / `EndDate` / `DueDate` | `Date` | Clause validity window |

**Three independent calendars.** `RentYearStartMonth`, `SalesYearEndDate` and the platform's
`FiscalPeriod` (which supports 4-5-4 retail calendars via `Is4or5WeekPeriod` /
`NumberWeeksInPeriod`) are all separate. A rebuild that assumes rent year = fiscal year = calendar
year will be wrong for most retail leases. **Observed** (all three fields exist independently).

---

## 3. Breakpoints — natural vs artificial

### `PercentageRentBreakpoint`, 8 tiers × 3 dimensions

```
BreakpointAmount1 .. BreakpointAmount8   (Currency)    — sales threshold for tier N
BreakpointCount1  .. BreakpointCount8    (Number)      — unit-count threshold for tier N
BreakpointRate1   .. BreakpointRate8     (Percentage)  — rate applied within tier N
NaturalBreakpointRate                     (Percentage) — the single rate used to DERIVE tier 1
CodeSalesGroupID / CodePortionedSalesGroupID (Dropdown (Sales Group))
BeginDate / EndDate / RevNumber           — the tier table is itself date-windowed and versioned
```

`BreakpointAmount` and `BreakpointCount` are **parallel alternatives**, selected by
`PercentageRent.UseCountBasedRate`. Both are always present in the schema; only one is meaningful
for a given clause. **Derived.**

`CodePortionedSalesGroupID` alongside `CodeSalesGroupID` implies a tier table can split its
threshold across two sales groups — a "portioned" breakpoint. **Inferred**; the semantics are an
open question.

### Artificial breakpoint

The stated amount is used directly:

```
tier_N_threshold = BreakpointAmount_N
tier_N_rate      = BreakpointRate_N
```

### Natural breakpoint

`PercentageRent.NaturalBreakpointFlag = true`. The breakpoint is the sales level at which the
percentage rent would exactly equal the minimum/base rent:

```
naturalBreakpoint = annualMinimumRent / NaturalBreakpointRate
```

**Inferred** — this is the standard retail-lease definition, and the schema is consistent with it:
Lucernex stores the *rate* and not the amount, which only makes sense if the amount is derived.
The corroborating evidence is `VirtualPercentageRentPeriod` carrying **both**
`ConfiguredBreakpointRate1` and `BreakpointRate1`, plus `BreakpointAmount1..8` — i.e. the projection
layer materialises the *effective* tier table (including the derived tier-1 amount) next to the
configured rate. **Observed** that both fields exist; **Inferred** that this is why.

The exact numerator (`annualMinimumRent`) is the open question: is it
`Contract.CurrentAnnualBaseRent`, the sum of `ExpenseSetup` rows in the base-rent expense group, or
the `ExpenseSchedule.AnnualAmount` for the period? **This must be confirmed in the live UI** — it
changes every natural-breakpoint number in the system.

---

## 4. How a period's rent is actually derived

The derivation reads directly off `VirtualSalesPeriod`'s field names. Each step is numbered to the
rule in [`rules.md`](rules.md).

### Step 0 — the two buckets (`CON-R-050`)

```
ReportingBucketBeginDate / EndDate / DueDate      ← CodeReportingFrequencyID + PeriodReportDueDays
BillingBucketBeginDate  / EndDate  / DueDate      ← CodeBillingFrequencyID  + PeriodPaymentDueDays
BillingBucketCapAmount  / BillingBucketFloorAmount ← PercentageRent.CapAmount / FloorAmount,
                                                     scaled to CodeCapFrequencyID
```

The reporting bucket also carries its own sales totals — `ReportingBucketGrossSalesAmount`,
`ReportingBucketNetSalesAmount` — separate from the billing bucket's. **Observed.**

### Step 1 — gross sales for the sales period (`CON-R-051`)

```
GrossSalesPeriodAmount = Σ Sales.GrossSalesAmount   for periods in [PeriodBeginDate, PeriodEndDate]
GrossSalesPeriodCount  = Σ Sales.UnitSalesCount
```

`Sales` carries `SalesAdjustment1..6(Currency)` and its own `NetSalesAmount`, so a reported
sales row can already be net of tenant-side adjustments before exclusions are applied. **Observed**;
the precedence between `Sales.NetSalesAmount` and the exclusion engine is an open question.

### Step 2 — exclusions (`CON-R-052` … `CON-R-056`)

Per `SalesExclusion` row, matched on `CodeSalesTypeID` + `CodeSalesGroupID`:

```
rawExcluded_e = salesOfType(e) × SalesExclusion.ExclusionRate
```

Rows sharing an `ExclusionGroupCapID` are aggregated at the `SalesExclusionCap`, whose **computed**
fields spell out the clamp exactly:

| `SalesExclusionCap` field | Meaning |
|---|---|
| `PRPGrossSalesAmount` | Gross sales in the percentage-rent period, for the cap's percentage basis |
| `PRPGrossExcludedAmount` | Σ of raw excluded amounts in this cap group, **before** the cap |
| `PRPComputedCapAmount` | The effective cap: `min(CapAmount, PRPGrossSalesAmount × CapPercent)` |
| `PRPNetExcludedAmount` | `min(PRPGrossExcludedAmount, PRPComputedCapAmount)` — what is actually excluded |
| `PRPExcessExcludedAmount` | `PRPGrossExcludedAmount − PRPNetExcludedAmount` — the disallowed excess, which stays in net sales |
| `SPExcludedAmount` | The same figure resolved at the **sales period** level rather than the rent period |

The existence of both `PRPNetExcludedAmount` and `PRPExcessExcludedAmount` as separate stored
values is what makes the `min()` reading solid rather than speculative — the platform explicitly
keeps the amount it refused to exclude. **Derived** from the field set; the exact form of
`PRPComputedCapAmount` (`min` of both, or `CapAmount` when set else the percentage) is **Inferred**.

Note that `SalesExclusion` carries `CapAmount`/`CapPercent` **and** `SalesExclusionCap` carries
`CapAmount`/`CapPercent` — a per-exclusion cap and a per-group cap. Both apply. **Observed.**

```
ExcludedSalesPeriodAmount = Σ over cap groups of PRPNetExcludedAmount
NetSalesPeriodAmount      = GrossSalesPeriodAmount − ExcludedSalesPeriodAmount
NetSalesPeriodCount       = GrossSalesPeriodCount  − ExcludedSalesPeriodCount
```

### Step 3 — roll sales periods into the rent period (`CON-R-057`)

```
PRPSalesAmount = Σ NetSalesPeriodAmount over sales periods inside the billing bucket
PRPSalesCount  = Σ NetSalesPeriodCount
```

Modified by three clause flags:

| Flag | Effect on `PRPSalesAmount` |
|---|---|
| `UseTrailing12MonthSales` | Replace the bucket sum with a rolling 12-month sum. `VirtualPercentageRentPeriod.TrailingSalesMultiplier(5-Digit Number)` scales it — presumably `12 / monthsAvailable` for a partial history. **Inferred.** |
| `AnnualizeRent` | Scale a partial period up to a full year before applying tiers, then scale the rent back down. **Inferred.** |
| `CumulativeFlag` | Accumulate year-to-date and credit rent already billed, rather than treating each period independently. **Inferred**; the credit mechanism is `SalesPeriodRentPaid` (see step 7). |

### Step 4 — the eight tiers (`CON-R-058`, `CON-R-059`)

```
for N in 1..8:
    PRPSalesPastBreakpoint_N = the portion of PRPSalesAmount falling in tier N
    PRPBreakpointRentDue_N   = PRPSalesPastBreakpoint_N × PRPBreakpointRate_N

PRPBreakpointRent = Σ PRPBreakpointRentDue_N
```

**The marginal-vs-excess ambiguity is unresolved and matters.** The label is literally
*"Sales Past Breakpoint #N"*, which permits two readings:

| Reading | Formula | Consequence |
|---|---|---|
| **(a) marginal band** *(assumed)* | `clamp(PRPSalesAmount, BP_N, BP_{N+1}) − BP_N`, with `BP_9 = ∞` | Σ of tier rents is the standard tiered result; rates are marginal |
| **(b) simple excess** | `max(0, PRPSalesAmount − BP_N)` | Σ would double-count; rates would have to be *incremental deltas* |

Reading (a) is assumed throughout because it is the industry-standard tiered structure and because
`PRPBreakpointRent` is a plain sum. **This is the single highest-value thing to verify in the live
UI** — enter a two-tier breakpoint with sales above both thresholds and read the eight
`Rent Due #N` values. Open question 2.

### Step 5 — cap and floor (`CON-R-060`)

```
PRPCapFloorAdjustedRent = clamp(PRPBreakpointRent,
                                BillingBucketFloorAmount,
                                BillingBucketCapAmount)
```

`BillingBucketCapAmount` / `BillingBucketFloorAmount` are the clause's `CapAmount`/`FloorAmount`
resolved into this specific billing bucket, scaled per `CodeCapFrequencyID`. **Derived** — the
field names carry both the "BillingBucket" prefix and the Cap/Floor role, and `CodeCapFrequencyID`
exists precisely to make the scaling explicit.

### Step 6 — offsets (`CON-R-061`)

`VirtualPRPAggregate` is where offsets land, at the **rent year** level:

| Field | Role |
|---|---|
| `RentYearBeginDate` / `RentYearEndDate` | The rent year, per `RentYearStartMonth` |
| `RentYearHasAltRent(Boolean)` | An `AlternateRentSchedule` window overlaps this rent year |
| `VariableRentOffsetAmount(Currency)` | Sum of applicable `VariableRentOffset` / `ScheduledOffset` |
| `CurrentRentObligation(Currency)` | Gross obligation before credits |
| `CurrentRentPaid(Currency)` | Already billed/paid within the rent year |
| `CurrentRentDue(Currency)` | The balance to bill |
| `NetSalesRentDue(Currency)` | The obligation computed from net sales alone |

`VariableRentOffset` offsets are keyed by expense group/type — `CodeOffsetGroupID`,
`CodeOffsetTypeID`, `CodePRAggregateExpGroupID`, `CodePRAggregateExpTypeID` — i.e. "reduce
percentage rent by what we paid in CAM this year", the classic offset-against-recovery clause. It
carries its own `CapAmount`/`CapPercent` and a `FixedOffsetAmount`. **Observed.**

`ScheduledOffset` is the pre-agreed variant: `TotalAmount`, `CapAmountPerMonth`, `CapPercent`,
`AmountAllocated`, `AmountNotAllocated`, plus a `VendorID` — a landlord credit drawn down over
time. It is applied by the `APPLY_OFFSETS` command and joined to expense group/type through
`LinkSchedOffsetExpGrpType`. **Observed.**

### Step 7 — rent due and posting (`CON-R-062`, `CON-R-063`)

```
PRPTotalRent = the period's total percentage-rent obligation
PRPRentDue   = PRPTotalRent − SalesPeriodRentPaid − offsets
```

**Inferred** — `SalesPeriodRentPaid` and `VirtualPRPAggregate.CurrentRentPaid` exist precisely to
carry the credit; the split of responsibility between `PRPRentDue` (period) and `CurrentRentDue`
(rent year) is not directly observed.

Posting: `GENERATE_PERCENTAGE_RENT_ACCRUALS` writes `AccrualTransaction` rows using the
`PercentRentAccrualAcct1..4Number` GL slots; the billing itself produces a `PaymentTransaction`
carrying `PercentageRentID`.

`VirtualPRAccrualPeriod` reconciles the two:

| Computed | Posted |
|---|---|
| `AccrualAmountThisPeriod` | `PostedAccrualAmountThisPeriod` |
| `AccrualAmountPriorPeriods` | `PostedAccrualAmountPriorPeriods` |
| `AccrualAmountTotal` | `PostedAccrualAmountTotal` |
| — | `IsPosted(Boolean)` |

---

## 5. Alternate rent

`AlternateRentSchedule` (25 fields) substitutes a different rent formula for a window — a COVID-era
or co-tenancy-triggered rent concession:

| Field | Role |
|---|---|
| `CodeAltRentMathID` | `Dropdown (Alt Rent Math Code)` — the substitute formula. **Members unknown.** |
| `PercentRentRate(Percentage)` | A flat percentage-of-sales rate replacing the tier table |
| `CapAmount` / `FloorAmount` | Its own clamp |
| `ExpenseReductionAmount` / `ExpenseReductionPercent` | Reduce the fixed expense side too |
| `PRDeductExclusions(Boolean)` | Whether exclusions still apply under alternate rent |
| `SetExpHoldFlag` / `SetPRHoldFlag` / `SuspendSL` | Force-hold the normal expense schedule, the normal percentage rent, and straight-line accounting |
| `ExpenseSetupID` | Which expense clause it replaces |
| `CodeSalesGroupID`, `BeginDate`/`EndDate`, `RevNumber` | Scope and version |

`PaymentTransaction` records the effect: `InAlternateRent(Boolean)`,
`AlternateRentScheduleID`, and `PreAltRentInvoiceAmount(Currency)` — **what would have been
invoiced without the alternate rent**. That last field is the audit artefact that makes concession
reporting possible, and ASG Edge+ should copy it. `Contract.InAlternateRent(Boolean)` and
`VirtualExpenseForecastPeriod.IgnoreAlternateRent` / `.InAlternateRent` carry the same flag
upward. **Observed.**

---

## 6. Where the ASG tenant actually models exclusions

A significant and easily-missed finding: the American Freight / ASG tenant does **not** use
`SalesExclusion` rows for its main exclusion catalogue. It uses **Firm-scope custom fields on
`Contract`**. Five parallel families, each with the identical eight-field shape:

```
Firm_CustomerPOSSales{Allowable, BeginDate, Cap, CapPercent, Document, Notes, Page, Section}
Firm_CustomerEnterpriseSales{...}
Firm_CustomerShiptoStoreSales{...}
Firm_CustomerSingleSwipeSales{...}
Firm_EmployeeSales{...}
```

plus seven standalone cap percentages:

```
Firm_UncollectedCreditCapPercent          Firm_DeliveryChargesCapPercent
Firm_CreditCardFeesCapPercent             Firm_BankChargesCapPercent
Firm_CustomerInStorePurchaseReturnsCapPercent
Firm_CustomerOnlinePurchaseReturnsCapPercent
Firm_EmployeeOnlinePurchaseReturnsCapPercent
```

All **Observed** in `_lucernex_objects_summary.txt` under `Contract`. Each family carries
`Document`/`Page`/`Section`/`Notes` — i.e. these are *lease-abstract* fields (where in the lease is
this exclusion permitted?), not engine inputs. Whether they also drive the calculation, or are
purely documentary alongside real `SalesExclusion` rows, is **unresolved** and is open question 4.

This matters enormously for the migration: if the tenant's real exclusion rules live in Firm custom
fields, a migration that only moves `SalesExclusion` rows will silently lose them.

---

## 7. Complete field participation list

Every field that participates in percentage rent. **Observed.**

<details><summary><code>PercentageRent</code> (45)</summary>

`AmendmentID`, `AnnualPaymentDueDays`, `AnnualReportDueDays`, `AnnualizeRent`, `AuditRightFlag`,
`BOMapClientRecordID`, `BeginDate`, `CapAmount`, `CodeBillingFrequencyID`, `CodeCapFrequencyID`,
`CodeCurrencyTypeID`, `CodeExpenseGroupID`, `CodeExpenseTypeID`, `CodePercentageRentTypeID`,
`CodeProrationMethodID`, `CodeReportingFrequencyID`, `CodeSalesGroupID`, `CodeStoreTypeID`,
`ContractID`, `CovenantID`, `CumulativeFlag`, `Description`, `DueDate`, `EndDate`,
`ExtFinalPeriodToLeaseExpDt`, `Firm_CertifiedSales`, `Firm_PercentRentDocument`,
`Firm_PercentRentPage`, `FloorAmount`, `IsMidMonth`, `IsPartialTerm`, `ModifiedByID`,
`ModifiedDate`, `NaturalBreakpointFlag`, `Notes`, `OffsetAmount`, `PercentageRentID`,
`PeriodPaymentDueDays`, `PeriodReportDueDays`, `ProjectEntityID`, `RentYearStartMonth`,
`SalesYearEndDate`, `Section`, `UseCountBasedRate`, `UseTrailing12MonthSales`
</details>

<details><summary><code>PercentageRentBreakpoint</code> (40)</summary>

`BOMapClientRecordID`, `BeginDate`, `BreakpointAmount1..8`, `BreakpointCount1..8`,
`BreakpointRate1..8`, `CodePortionedSalesGroupID`, `CodeSalesGroupID`, `ContractID`, `CreatedByID`,
`CreatedDate`, `Description`, `EndDate`, `ModifiedByID`, `ModifiedDate`, `NaturalBreakpointRate`,
`Notes`, `PercentageRentBreakpointID`, `ProjectEntityID`, `RevNumber`
</details>

<details><summary><code>Sales</code> (28)</summary>

`BOMapClientRecordID`, `ClientSalesID`, `CodeCurrencyTypeID`, `CodeSalesCategoryID`,
`CodeSalesGroupID`, `CodeSalesTypeID`, `CodeUnitSalesTypeID`, `ContractID`, `EffectiveDate`,
`GrossSalesAmount`, `MatchingCalendarMonthText`, `MatchingCalendarMonthYearText`,
`MatchingCalendarYear`, `ModifiedByID`, `ModifiedDate`, `NetSalesAmount`, `PostingDate`,
`ProjectEntityID`, `SalesAdjustment1..6`, `SalesID`, `SalesPeriod`, `SalesYear`, `UnitSalesCount`
</details>

<details><summary><code>SalesExclusion</code> (19) + <code>SalesExclusionCap</code> (23)</summary>

`SalesExclusion`: `BOMapClientRecordID`, `BeginDate`, `CapAmount`, `CapPercent`,
`CodeCurrencyTypeID`, `CodeSalesGroupID`, `CodeSalesTypeID`, `ContractID`, `CreatedByID`,
`CreatedDate`, `EndDate`, `ExclusionGroupCapID`, `ExclusionRate`, `ModifiedByID`, `ModifiedDate`,
`Notes`, `ProjectEntityID`, `RevNumber`, `SalesExclusionID`

`SalesExclusionCap`: `BOMapClientRecordID`, `BeginDate`, `CapAmount`, `CapPercent`,
`CodeCurrencyTypeID`, `CodeExclusionCapID`, `CodeSalesGroupID`, `ContractID`, `CreatedByID`,
`CreatedDate`, `EndDate`, `ModifiedByID`, `ModifiedDate`, `Notes`, `PRPComputedCapAmount`,
`PRPExcessExcludedAmount`, `PRPGrossExcludedAmount`, `PRPGrossSalesAmount`, `PRPNetExcludedAmount`,
`ProjectEntityID`, `RevNumber`, `SPExcludedAmount`, `SalesExclusionCapID`
</details>

<details><summary><code>VirtualSalesPeriod</code> (66)</summary>

`BillingBucketBeginDate`, `BillingBucketCapAmount`, `BillingBucketDueDate`, `BillingBucketEndDate`,
`BillingBucketFloorAmount`, `CodeSalesGroupID`, `ContractID`, `ExcludedSalesPeriodAmount`,
`ExcludedSalesPeriodCount`, `GrossSalesPeriodAmount`, `GrossSalesPeriodCount`, `IsActual`,
`NetSalesPeriodAmount`, `NetSalesPeriodCount`, `PRPBreakpointAmount1..8`, `PRPBreakpointRate1..8`,
`PRPBreakpointRent`, `PRPBreakpointRentDue1..8`, `PRPCapFloorAdjustedRent`, `PRPRentDue`,
`PRPSalesAmount`, `PRPSalesCount`, `PRPSalesPastBreakpoint1..8`, `PRPTotalRent`, `PeriodBeginDate`,
`PeriodEndDate`, `ReportingBucketBeginDate`, `ReportingBucketDueDate`, `ReportingBucketEndDate`,
`ReportingBucketGrossSalesAmount`, `ReportingBucketNetSalesAmount`, `SalesMonth`,
`SalesMonthYearSort`, `SalesMonthYearText`, `SalesPeriodRentPaid`, `SalesPeriodSort`,
`SalesPeriodText`, `SalesYear`
</details>

<details><summary><code>VirtualPercentageRentPeriod</code> (38), <code>VirtualPRPAggregate</code> (16), <code>VirtualPRAccrualPeriod</code> (20)</summary>

`VirtualPercentageRentPeriod`: `ActualNetSalesAmount`, `BreakpointAmount1..8`,
`BreakpointCount1..8`, `BreakpointRate1..8`, `CapAmount`, `CodeCapFrequencyID`, `CodeSalesGroupID`,
`ConfiguredBreakpointRate1`, `ContractID`, `FloorAmount`, `IsPartialTerm`, `NaturalBreakpointRate`,
`PeriodBeginDate`, `PeriodDateRange`, `PeriodEndDate`, `ProjectEntityID`, `TrailingSalesMultiplier`

`VirtualPRPAggregate`: `CodeBillingFrequencyID`, `CodeExpenseGroupID`, `CodeExpenseTypeID`,
`CodePercentageRentTypeID`, `ContractID`, `CurrentRentDue`, `CurrentRentObligation`,
`CurrentRentPaid`, `NetSalesRentDue`, `PeriodBeginDate`, `PeriodEndDate`, `ProjectEntityID`,
`RentYearBeginDate`, `RentYearEndDate`, `RentYearHasAltRent`, `VariableRentOffsetAmount`

`VirtualPRAccrualPeriod`: `AccrualAmountPriorPeriods`, `AccrualAmountThisPeriod`,
`AccrualAmountTotal`, `BeginDate`, `ContractID`, `EndDate`, `FiscalPeriodName`,
`FiscalPeriodNameSort`, `IsPosted`, `MatchingCalendarMonth`, `MatchingCalendarYear`,
`NumberDaysInPeriod`, `NumberWeeksInPeriod`, `Period`, `PostedAccrualAmountPriorPeriods`,
`PostedAccrualAmountThisPeriod`, `PostedAccrualAmountTotal`, `ProjectEntityID`, `Quarter`, `Year`
</details>

---

## 8. Use-based rent is the same engine

`UseBasedRent` / `UseBasedRentBreakpoint` / `VirtualUsagePeriod` / `VirtualUseBasedRentPeriod` /
`Usage` are structurally identical to the percentage-rent family with two substitutions:
`Sales` → `Usage` and the `PRP` prefix → `UBRP`. The only genuine differences:

| Percentage rent | Use-based rent |
|---|---|
| `BreakpointAmount1..8(Currency)` | `BreakpointCost1..8(Currency)` — a **unit cost**, not a threshold |
| `BreakpointRate1..8(Percentage)` | *(none — the cost per unit **is** the rate)* |
| `PRPSalesAmount` | `UBRPUsageAmount` + `UBRPUsageCount` + `UBRPUsageShare` |
| `Sales.GrossSalesAmount` | `Usage.UsageCount` + `Usage.UsageShare(Percentage)` |
| — | `CodeUseRentModelTypeID` (`Dropdown (Use Rent Model Type Code)`) |
| `sTYPE_MONEY` precision | `sTYPE_NUMBER_FRACTION6DIGITS` — **6 decimal places** on unit rates |

`VirtualUsagePeriod` carries `UBRPBreakpointAmount1..8` as `5-Digit Number` (usage thresholds) and
`UBRPBreakpointCost1..8` as `Currency`. The tier structure, the cap/floor clamp
(`UBRPCapFloorAdjustedRent`), the rent-due chain (`UBRPRentDue`, `UBRPTotalRent`,
`UsagePeriodRentPaid`) and the two-bucket date model are byte-for-byte the same shape.
**Observed.** Build one engine.

The 6-decimal precision requirement is a hard constraint: a per-kWh or per-gallon rate at
`sTYPE_NUMBER_FRACTION6DIGITS` multiplied by a large usage count is exactly where a `double` loses
money. **Constitution §4.4 applies with force here.**

---

## Open questions

Ranked by impact on the frozen schema.

1. **What are the members of `Dropdown (Percentage Rent Type Code)`?** This is the calculation
   variant selector and the single largest unknown in the whole clause. Readable from Manage Firm
   Drop Downs / Client Drop Downs (screen 007 route, `FirmCodeList.jsp`).
2. **Marginal band or simple excess for `PRPSalesPastBreakpoint_N`?** (§4 step 4.) Enter a
   two-tier breakpoint, post sales above both thresholds, and read the eight `Rent Due #N` values
   on the Sales Period list. Every percentage-rent number in a rebuilt system depends on this.
3. **What is the numerator in `naturalBreakpoint = minimumRent / NaturalBreakpointRate`?**
   `Contract.CurrentAnnualBaseRent`, the base-rent `ExpenseSetup` sum, or the period's
   `ExpenseSchedule.AnnualAmount`? Compare a natural-breakpoint contract's derived
   `PRPBreakpointAmount1` against each candidate.
4. **Are the `Firm_*Sales*` exclusion families on `Contract` documentary or functional?** (§6.)
   Check whether a contract with `Firm_EmployeeSalesAllowable` set but no `SalesExclusion` row
   still excludes employee sales.
5. **What does `CodePortionedSalesGroupID` do on `PercentageRentBreakpoint`?** A second sales group
   on the tier table implies split-threshold behaviour that nothing else explains.
6. **Precedence: `Sales.NetSalesAmount` vs the exclusion engine.** Does a reported net figure
   bypass `SalesExclusion` entirely, or are exclusions applied on top?
7. **What are the members of `Dropdown (Alt Rent Math Code)`?** Determines how many alternate-rent
   formulas must be supported.
8. **How does `CumulativeFlag` interact with `SalesPeriodRentPaid`?** Cumulative percentage rent
   with a mid-year rate change is the classic source of retail-lease disputes.
