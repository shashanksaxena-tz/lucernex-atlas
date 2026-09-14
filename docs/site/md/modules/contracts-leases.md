# Contracts & Leases

*In scope for the rebuild*

The Contract aggregate root (570 fields across four physical tables) and the lease terms hanging off it: amendments, terms, key dates, covenants, co-tenancy, insurance, security deposits, responsibilities and allowances.

|  | Count |
|---|---|
| Record types | 14 |
| Fields | 1,166 |
| Keys in | 67 |
| Keys out | 48 |
| Rules | 161 |

## What was found here

### Contract is the blocker

**Derived.** 570 fields across four physical tables, and 62 other record types point at it. Payment processing, percentage rent and ASC 842 accounting all sit downstream, which is why the schema freeze gates them.

### Vendor is a relabelled Employer

**Observed.** PaymentTransaction.VendorID has declared type Employer ID. Contract has no direct Vendor foreign key at all — that relationship lives one level down, on Payment Transaction.

### Relationships are asymmetric by cardinality

**Observed.** From Contract, Facility is reached as a single related record. From Facility, Contract is not offered that way — it appears as an embedded child grid. The UI models the one-to-many direction differently from the many-to-one.

### A contract can be its own parent

**Observed.** MasterContractID has declared type Contract ID — a self-reference carrying the master-lease and sublease hierarchy.

### Lifecycle lives in tenant data, not schema

**Observed.** The nine lifecycle states — Open, Future Possession, Possession, Possession - Paying Rent, Active, Closed - Active, Closed, and two Accounting Purposes Only variants — sit in a tenant-authored drop-down. Contract Status Code, the platform field, has only three values and means something different. Both are required on the same form.

### CAM does not follow the pattern

**Derived.** Expense recovery is a reconciliation grid with no schedule layer. Treating it as an instance of the Clause/Schedule/Transaction/Projection pattern would be the single most expensive modelling mistake available here.

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Contract](../entities/Contract.md) | `contract_admin,contract_financial,contract_firm,contract_firm1` | 570 | 62 |
| [LeaseInfo](../entities/LeaseInfo.md) | `lease_info` | 219 | 0 |
| [ContractFinancialTest](../entities/ContractFinancialTest.md) | `contract_financial_test` | 93 | 0 |
| [Covenant](../entities/Covenant.md) | `covenant` | 44 | 15 |
| [KeyDate](../entities/KeyDate.md) | `key_date` | 39 | 0 |
| [Responsibility](../entities/Responsibility.md) | `responsibility` | 32 | 0 |
| [CoTenancy](../entities/CoTenancy.md) | `co_tenancy` | 27 | 0 |
| [Insurance](../entities/Insurance.md) | `insurance` | 27 | 0 |
| [ContractTerm](../entities/ContractTerm.md) | `contract_term` | 26 | 5 |
| [SecurityDeposit](../entities/SecurityDeposit.md) | `security_deposit` | 25 | 0 |
| [Allowance](../entities/Allowance.md) | `allowance` | 23 | 1 |
| [AllowanceTransaction](../entities/AllowanceTransaction.md) | `allowance_transaction` | 20 | 0 |
| [ContractAmendment](../entities/ContractAmendment.md) | `contract_amendment` | 20 | 13 |
| [LeaseAudit](../entities/LeaseAudit.md) | `lease_audit` | 1 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [CON-R-001](../rules/CON-R-001.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Classifying any financial record by its field set: if it carries both AmendmentID and Section, it is an L0 clause record. | Observed |
| [CON-R-002](../rules/CON-R-002.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Classifying any financial record: if it carries an FK to an L0 object and ProcessedFlag, it is an L1 schedule row. | Observed |
| [CON-R-003](../rules/CON-R-003.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Classifying any financial record: if it carries PostingDate and GL account slots and a counterparty FK, it is an L2 transaction. | Observed |
| [CON-R-004](../rules/CON-R-004.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Classifying any financial record by its object name and field set: if the name is prefixed Virtual and it has no RevNumber/ModifiedByID/Firm-scope field, it is an L3 projection. | Observed |
| [CON-R-005](../rules/CON-R-005.md) | 1. The Clause / Schedule / Transaction / Projection pattern | An L0 clause is created or edited: its validity window is its own BeginDate..EndDate; a new RevNumber supersedes the prior revision. | Derived |
| [CON-R-006](../rules/CON-R-006.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Operator invokes a generator command on the L0 clause and its modifiers: the generator materialises L1 rows spanning the clause window. | Observed |
| [CON-R-007](../rules/CON-R-007.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Operator invokes GENERATE_RENT (or a sibling): generate L2 transactions from every eligible L1 row where ProcessedFlag is false; set ProcessedFlag = true, ProcessedDate = now. | Derived |
| [CON-R-008](../rules/CON-R-008.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Generation is requested: both ExpenseSetup.ReadyForPaymentFlag and ExpenseSchedule.ReadyForPaymentFlag must be true for the row to generate — the fields are observed, the exact gate semantics are infe | Observed |
| [CON-R-009](../rules/CON-R-009.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Generation is requested: any HoldFlag = true anywhere in the L0→L1→L2 chain suppresses the row — though whether it prevents generation or merely marks the generated row held is unconfirmed. | Observed |
| [CON-R-010](../rules/CON-R-010.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Correcting generated output: the supported path is DELETE_PAYMENTS then GENERATE_RENT, not editing a posted transaction in place. | Derived |
| [CON-R-011](../rules/CON-R-011.md) | 1. The Clause / Schedule / Transaction / Projection pattern | An L2 row has left the system: a row carrying ExportBatchNumber, CheckNumber or CheckDate has been exported/settled — treat it as an immutability candidate, though enforcement is unverified. | Observed |
| [CON-R-012](../rules/CON-R-012.md) | 1. The Clause / Schedule / Transaction / Projection pattern | Reading an L3 projection: projections are computed, not authored; a tenant cannot customise them because no Firm-scope fields exist on any Virtual* object. | Observed |
| [CON-R-013](../rules/CON-R-013.md) | 1. The Clause / Schedule / Transaction / Projection pattern | An escalation step is materialised: L1 rows form a doubly-linked list; each row carries PreviousAnnualAmount/AnnualAmount/NextAnnualAmount. | Observed |
| [CON-R-014](../rules/CON-R-014.md) | 1. The Clause / Schedule / Transaction / Projection pattern | An L2 row is written: every transaction records SourceEntityTable and CodeSourceEntityID — which generator produced it. | Observed |
| [CON-R-015](../rules/CON-R-015.md) | 2. Contract identity and hierarchy | A contract is created: FacilityID, LocationID, OrganizationID and ProgramID key the contract to building, site, debiting org and portfolio. | Observed |
| [CON-R-016](../rules/CON-R-016.md) | 2. Contract identity and hierarchy | A contract is created: OrganizationID is 'where payments should be debited' in Lx's own field definition — it determines the GL debit side. | Observed |
| [CON-R-017](../rules/CON-R-017.md) | 2. Contract identity and hierarchy | A sublease is created: MasterContractID points at the master lease's ContractID; null means not a sublease. | Observed |
| [CON-R-018](../rules/CON-R-018.md) | 2. Contract identity and hierarchy | Traversing MasterContractID: no depth limit, no cycle guard, no role discriminator and no allocation percentage exist on the edge — the hierarchy is structurally unconstrained. | Observed |
| [CON-R-019](../rules/CON-R-019.md) | 2. Contract identity and hierarchy | Determining payable vs receivable: direction is carried on ExpenseSetup.IsReceivable and PaymentTransaction.IsReceivable, not on the contract, so one contract can be both. | Observed |
| [CON-R-020](../rules/CON-R-020.md) | 2. Contract identity and hierarchy | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, Landl | Derived |
| [CON-R-021](../rules/CON-R-021.md) | 2. Contract identity and hierarchy | Resolving a 'Vendor': VendorID's declared type is Employer ID — Vendor is a relabelled Employer, not a distinct entity. | Observed |
| [CON-R-022](../rules/CON-R-022.md) | 2. Contract identity and hierarchy | Determining the discount rate: look up DiscountRate by accounting method + contract use + geography + a min/max-scheduled-months band, and stamp it onto Contract.DiscountRate. | Derived |
| [CON-R-023](../rules/CON-R-023.md) | 2. Contract identity and hierarchy | Determining the fiscal calendar: the calendar is owned by Contract.ProgramID (the portfolio), not by the firm. | Observed |
| [CON-R-024](../rules/CON-R-024.md) | 2. Contract identity and hierarchy | A retail fiscal period is used: periods may be 4 or 5 weeks (retail 4-5-4), not calendar months, per FiscalPeriod.Is4or5WeekPeriod. | Observed |
| [CON-R-025](../rules/CON-R-025.md) | 2. Contract identity and hierarchy | Computing rent rollups: 120 denormalised sTYPE_MONEY fields on Contract cross {Calendar,Fiscal}×{Base,Total}×{with,without tax}×{period buckets}. | Observed |
| [CON-R-026](../rules/CON-R-026.md) | 2. Contract identity and hierarchy | Any rollup is read: the rollups are denormalised and can be stale — Contract carries no recalculation flag equivalent to SLSummary's. | Derived |
| [CON-R-027](../rules/CON-R-027.md) | 2. Contract identity and hierarchy | Applying contract-level tax: four parallel tax components; each ExpenseSetup opts in per component, producing CalculatedTaxRate1..4 on the schedule. | Derived |
| [CON-R-028](../rules/CON-R-028.md) | 2. Contract identity and hierarchy | A contract term option is created: the Terms Wizard generates N ContractTerm rows of a stated length from a stated start. | Observed |
| [CON-R-029](../rules/CON-R-029.md) | 2. Contract identity and hierarchy | Accruing over an option term: only terms flagged IncludeTermForAccruals participate in accrual schedules. | Observed |
| [CON-R-030](../rules/CON-R-030.md) | 3. Recurring expense: setup and schedule | Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full Expens | Observed |
| [CON-R-031](../rules/CON-R-031.md) | 3. Recurring expense: setup and schedule | The wizard's 'Find Starting Amount' checkbox is set: work backwards from a known later amount and the escalation rule to derive the starting amount — useful for abstracting a lease mid-term. | Inferred |
| [CON-R-032](../rules/CON-R-032.md) | 3. Recurring expense: setup and schedule | Determining billing frequency: CodeFrequencyID, NumberOfPayments and PaymentDueDay drive the number and spacing of ExpenseSchedule rows. | Derived |
| [CON-R-033](../rules/CON-R-033.md) | 3. Recurring expense: setup and schedule | The clause is flagged IsCustomPaymentCoverage: the same ExpenseSetup record supports annual, quarterly or semi-annual coverage without a schema change, via explicit month-and-day markers per frequency | Observed |
| [CON-R-034](../rules/CON-R-034.md) | 3. Recurring expense: setup and schedule | The clause is flagged IsPayArrears: payment is due after the coverage period rather than in advance. | Inferred |
| [CON-R-035](../rules/CON-R-035.md) | 3. Recurring expense: setup and schedule | The clause is flagged IsDailyRent: the period amount is the daily rate multiplied by the day count in the period, rather than a fixed period amount. | Derived |
| [CON-R-036](../rules/CON-R-036.md) | 3. Recurring expense: setup and schedule | A partial first or last period occurs: CodeProrationMethodID governs it, and the schedule's own FirstPaymentAmount / LastPaymentAmount carry the prorated stub amounts. | Observed |
| [CON-R-037](../rules/CON-R-037.md) | 3. Recurring expense: setup and schedule | CalculateScheduleAmounts is invoked: the schedule's amounts are recomputed in place from the clause, its escalation and its tax configuration. | Observed |
| [CON-R-038](../rules/CON-R-038.md) | 3. Recurring expense: setup and schedule | An expense is split across organizations: ExpenseAllocation apportions one clause across organizations by percentage. | Observed |
| [CON-R-039](../rules/CON-R-039.md) | 3. Recurring expense: setup and schedule | An expense is split across vendors: ExpenseVendorAllocation apportions one clause's payments across vendors by percentage; CHANGE_EXPENSE_ALLOCATION_VENDOR rewrites it. | Observed |
| [CON-R-040](../rules/CON-R-040.md) | 4. Escalations | An escalation step falls due: a step occurs every EscalationPeriod × CodeFrequencyID units inside the clause's BeginDate..EndDate window. | Derived |
| [CON-R-041](../rules/CON-R-041.md) | 4. Escalations | The driver is fixed: new amount = f(base or current amount, FixedAmount, EscalationMethod) — but EscalationMethod is free text, so its value space is unknown. | Observed |
| [CON-R-042](../rules/CON-R-042.md) | 4. Escalations | The driver is index-based: rawChange = (IndexAmount / IndexBaseFactor) − 1 — assumes IndexAmount is a level, which is unconfirmed. | Inferred |
| [CON-R-043](../rules/CON-R-043.md) | 4. Escalations | An index change is applied: applied = rawChange × ExpenseSetup.CPIMultiplier. | Inferred |
| [CON-R-044](../rules/CON-R-044.md) | 4. Escalations | A per-step collar exists: collared = clamp(applied, PeriodMinPercentage, PeriodMaxPercentage). | Derived |
| [CON-R-045](../rules/CON-R-045.md) | 4. Escalations | ExpenseSetup.IsCPICompounding is set: true escalates from the current amount; false escalates from BaseAmount. | Derived |
| [CON-R-046](../rules/CON-R-046.md) | 4. Escalations | A lifetime collar exists: cumulative change across all steps is clamped by LifetimeMinPercentage/LifetimeMaxPercentage. | Derived |
| [CON-R-047](../rules/CON-R-047.md) | 4. Escalations | An absolute ceiling exists: CapAmount/CapPercentage cap the escalated amount absolutely; order versus the collar above is unknown. | Observed |
| [CON-R-048](../rules/CON-R-048.md) | 4. Escalations | An expense stop exists: cost above StopAmount transfers to the tenant rather than continuing to escalate. | Inferred |
| [CON-R-049](../rules/CON-R-049.md) | 4. Escalations | Increase/decrease asymmetry: ExpenseSetup.AmountIncreaseCap/AmountDecreaseCap/PercentIncreaseCap/PercentDecreaseCap are a separate, parallel collar to ExpenseEscalation's own min/max, with unspecified | Observed |
| [CON-R-050](../rules/CON-R-050.md) | Step 0 — the two buckets (``) | A percentage-rent period is projected: two independent date windows are produced — ReportingBucket{Begin,End,Due}Date and BillingBucket{Begin,End,Due}Date. | Observed |
| [CON-R-051](../rules/CON-R-051.md) | Step 1 — gross sales for the sales period (``) | Sales are reported: GrossSalesPeriodAmount sums Sales.GrossSalesAmount over the sales period; GrossSalesPeriodCount does the same for unit counts. | Observed |
| [CON-R-052](../rules/CON-R-052.md) | Step 2 — exclusions (`` … `CON-R-056`) | An exclusion applies: rawExcluded = salesOfType × SalesExclusion.ExclusionRate. | Derived |
| [CON-R-053](../rules/CON-R-053.md) | 5. Percentage rent | Exclusions share a cap group (ExclusionGroupCapID): PRPGrossExcludedAmount sums the raw excluded amounts within the group, before the cap. | Derived |
| [CON-R-054](../rules/CON-R-054.md) | 5. Percentage rent | A cap group is evaluated: PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent) — the effective cap, whichever binds first. | Inferred |
| [CON-R-055](../rules/CON-R-055.md) | 5. Percentage rent | The cap is applied: PRPNetExcludedAmount = min(gross, cap); PRPExcessExcludedAmount = gross − net — and the platform stores both numbers, which is what makes the min() reading solid rather than specul | Derived |
| [CON-R-056](../rules/CON-R-056.md) | 5. Percentage rent | Net sales are computed: NetSalesPeriodAmount = GrossSalesPeriodAmount − ExcludedSalesPeriodAmount. | Derived |
| [CON-R-057](../rules/CON-R-057.md) | 5. Percentage rent | Sales periods roll into a rent period: PRPSalesAmount sums NetSalesPeriodAmount over every sales period inside the billing bucket. | Derived |
| [CON-R-058](../rules/CON-R-058.md) | Step 4 — the eight tiers (``, `CON-R-059`) | A percentage-rent period is tiered: PRPSalesPastBreakpoint_N is computed for each of 8 tiers from PRPBreakpointAmount1..8 (or BreakpointCount1..8 under UseCountBasedRate) — assumed to be a marginal ba | Derived |
| [CON-R-059](../rules/CON-R-059.md) | 5. Percentage rent | Tier rent is computed: PRPBreakpointRentDue_N = past_N × rate_N; PRPBreakpointRent = the sum across all eight tiers. | Derived |
| [CON-R-060](../rules/CON-R-060.md) | Step 5 — cap and floor (``) | Cap and floor are applied: PRPCapFloorAdjustedRent = clamp(PRPBreakpointRent, BillingBucketFloorAmount, BillingBucketCapAmount). | Derived |
| [CON-R-061](../rules/CON-R-061.md) | Step 6 — offsets (``) | Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation. | Observed |
| [CON-R-062](../rules/CON-R-062.md) | Step 7 — rent due and posting (``, `CON-R-063`) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [CON-R-063](../rules/CON-R-063.md) | 5. Percentage rent | Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue. | Derived |
| [CON-R-064](../rules/CON-R-064.md) | 5. Percentage rent | NaturalBreakpointFlag is set: naturalBreakpoint = annualMinimumRent / NaturalBreakpointRate — see the breakpoint entity above for why the numerator is unresolved. | Derived |
| [CON-R-065](../rules/CON-R-065.md) | 5. Percentage rent | A natural breakpoint is derived: the configured rate and the effective rate are stored separately as the derivation's own audit trail. | Derived |
| [CON-R-066](../rules/CON-R-066.md) | 5. Percentage rent | UseTrailing12MonthSales is set: replace the bucket sum with a rolling 12-month sum, scaled by TrailingSalesMultiplier for a partial history. | Inferred |
| [CON-R-067](../rules/CON-R-067.md) | 5. Percentage rent | AnnualizeRent is set: scale a partial period's sales up to a full year, tier it, then scale the resulting rent back down. | Inferred |
| [CON-R-068](../rules/CON-R-068.md) | 5. Percentage rent | CumulativeFlag is set: accumulate year-to-date sales and rent, crediting rent already billed, instead of treating each period independently. | Inferred |
| [CON-R-069](../rules/CON-R-069.md) | 5. Percentage rent | A percentage-rent clause is flagged ExtFinalPeriodToLeaseExpDt: the final period extends to lease expiry instead of truncating at the usual period boundary. | Observed |
| [CON-R-070](../rules/CON-R-070.md) | 6. Alternate rent and offsets | An AlternateRentSchedule window is active: a substitute rent formula (CodeAltRentMathID, PercentRentRate) replaces the normal one for the window. | Observed |
| [CON-R-071](../rules/CON-R-071.md) | 6. Alternate rent and offsets | Alternate rent begins: SetExpHoldFlag, SetPRHoldFlag and SuspendSL hold the expense schedule, hold percentage rent, and suspend straight-line accounting — though what releases the holds afterward is n | Observed |
| [CON-R-072](../rules/CON-R-072.md) | 6. Alternate rent and offsets | A payment is generated under alternate rent: PreAltRentInvoiceAmount records what would have been invoiced without the concession. | Observed |
| [CON-R-073](../rules/CON-R-073.md) | 6. Alternate rent and offsets | Alternate rent applies: ExpenseReductionAmount / ExpenseReductionPercent reduce the fixed expense side as well as the variable side. | Observed |
| [CON-R-074](../rules/CON-R-074.md) | 6. Alternate rent and offsets | PRDeductExclusions is set: governs whether sales exclusions still apply under the alternate-rent formula. | Observed |
| [CON-R-075](../rules/CON-R-075.md) | 6. Alternate rent and offsets | A VariableRentOffset applies: percentage rent is reduced by amounts paid in a named expense group/type, subject to its own cap. | Derived |
| [CON-R-076](../rules/CON-R-076.md) | 6. Alternate rent and offsets | A ScheduledOffset is drawn down: a landlord credit (TotalAmount, CapAmountPerMonth) is drawn down over time against named expense group/types, via APPLY_OFFSETS. | Derived |
| [CON-R-077](../rules/CON-R-077.md) | 7. Use-based rent | Usage-based rent is computed: structurally identical to the percentage-rent tiering with Sales→Usage and PRP→UBRP; the tier value is a unit cost, not a percentage rate. | Derived |
| [CON-R-078](../rules/CON-R-078.md) | 7. Use-based rent | Unit rates are stored: usage unit costs carry 6 decimal places (sTYPE_NUMBER_FRACTION6DIGITS); usage counts carry 5 — precision loss here is a direct Constitution §4.4 violation if implemented with fl | Observed |
| [CON-R-079](../rules/CON-R-079.md) | 7. Use-based rent | A use-rent model is selected: CodeUseRentModelTypeID selects the variant; its members are unknown. | Observed |
| [CON-R-080](../rules/CON-R-080.md) | The waterfall (formulas taken verbatim from Lx's own field labels) | A recovery statement is valued: ST1 = C + NC − D — the recoverable pool, literally labelled 'Sub Total #1 (C+NC-D)'. | Observed |
| [CON-R-081](../rules/CON-R-081.md) | The waterfall (formulas taken verbatim from Lx's own field labels) | An admin-fee rate exists: AdminFeePercentageAmount = SubTotal1 × AdminFeePercentage. | Derived |
| [CON-R-082](../rules/CON-R-082.md) | The waterfall (formulas taken verbatim from Lx's own field labels) | Fees and additions are added: PassThrough = ST1 + AF%amt + AdministrationFees + Additions — labelled 'Pass-Through (ST1+AF%+AF+A)'. | Observed |
| [CON-R-083](../rules/CON-R-083.md) | The waterfall (formulas taken verbatim from Lx's own field labels) | Other recoveries are netted: SubTotal2 = PassThrough − Recoveries — labelled 'Sub Total #2 (PT-R)'. | Observed |
| [CON-R-084](../rules/CON-R-084.md) | The waterfall (formulas taken verbatim from Lx's own field labels) | The tenant's share is taken: NetPassThrough = SubTotal2 × ProRataShareRate — labelled 'Net Pass-Through (ST2*PRR)'. | Observed |
| [CON-R-085](../rules/CON-R-085.md) | The waterfall (formulas taken verbatim from Lx's own field labels) | Escrow already paid is credited: NetAmountDue = NetPassThrough − PrePaidAmount — labelled 'Net Amount Due (NPT-PP)'. | Observed |
| [CON-R-086](../rules/CON-R-086.md) | The waterfall (formulas taken verbatim from Lx's own field labels) | A manual adjustment is made: RevisedNetAmountDue = NetAmountDue + AdjustmentAmount — labelled 'Revised Amount Due (Net+Adj)', the final figure billed. | Observed |
| [CON-R-087](../rules/CON-R-087.md) | Grid structure and variances | A recovery record is stored: 565 fields = 63 configuration fields + a 502-cell grid, where the grid is 9 perspectives × roughly 19 measures × {Gross, Net}. | Derived |
| [CON-R-088](../rules/CON-R-088.md) | Grid structure and variances | A within-year variance is computed: RAVariance = Reported − Approved, for both Gross and Net, at 36 fields. | Derived |
| [CON-R-089](../rules/CON-R-089.md) | Grid structure and variances | A within-year variance is computed: ABVariance = Approved − Budgeted, for both Gross and Net. | Derived |
| [CON-R-090](../rules/CON-R-090.md) | Grid structure and variances | A year-over-year variance is computed: {P}PVariance = {P} − Prior{P} for Reported, Approved and Budgeted, each with a percentage sibling. | Derived |
| [CON-R-091](../rules/CON-R-091.md) | Grid structure and variances | Variance families are enumerated: only the three year-over-year families carry a percentage sibling at the header; at the line-item level all five families carry both amount and percent — an asymmetry | Observed |
| [CON-R-092](../rules/CON-R-092.md) | Grid structure and variances | A measure is unset: fields suffixed NoZeroDef return null/blank rather than 0. | Inferred |
| [CON-R-093](../rules/CON-R-093.md) | Grid structure and variances | A recovery cap applies: the cap grows period over period by a percentage or a value, cumulatively or not. | Derived |
| [CON-R-094](../rules/CON-R-094.md) | Grid structure and variances | The cap is applied to the waterfall: where in the sequence the clamp lands is not observable; the strong prior is controllables only. | Inferred |
| [CON-R-095](../rules/CON-R-095.md) | Grid structure and variances | A base year applies: an expense stop subtracts the base-year level; where it enters the waterfall is unobserved. | Inferred |
| [CON-R-096](../rules/CON-R-096.md) | Grid structure and variances | A gross-up applies: variable expenses are grossed up to a notional occupancy using GrossupRate and OccupancyAdjustedThreshold. | Inferred |
| [CON-R-097](../rules/CON-R-097.md) | Grid structure and variances | Escrow is trued up: reconcile the current escrow payment, propose a new estimate, and spread any shortfall over CatchUpNumberOfMonths. | Derived |
| [CON-R-098](../rules/CON-R-098.md) | Grid structure and variances | Recovery exclusions are recorded: RecoveryExclusions is a free-text textarea; there is no structured exclusion model for expense recovery at all. | Observed |
| [CON-R-099](../rules/CON-R-099.md) | Grid structure and variances | A recovery is settled: ReconciledFlag, ReconciledDate, TenantDueDate and TenantSavingsAmount record the audit outcome. | Observed |
| [CON-R-100](../rules/CON-R-100.md) | Line-item level | A recovery line item is valued: the same Reported/Approved/Budgeted/Prior perspectives exist at line-item cardinality. | Observed |
| [CON-R-101](../rules/CON-R-101.md) | Line-item level | A line item's approved total is computed: ComputedApprovedTotalAmount applies its own admin fee and cap per line item, not only at the header. | Derived |
| [CON-R-102](../rules/CON-R-102.md) | Line-item level | A landlord statement is ingested: ExpenseRecoveryItemMapping maps a free-text statement line (InvoiceLineItemName, JSONConfigText) to a structured recovery item. | Inferred |
| [CON-R-103](../rules/CON-R-103.md) | 9. Payment lifecycle | A payment is posted: five independent date axes must be simultaneously representable: GL period, economic effect, cash due, service coverage, settlement. | Observed |
| [CON-R-104](../rules/CON-R-104.md) | 9. Payment lifecycle | Direction is determined: IsReceivable lets one ledger serve both payables and receivables. | Observed |
| [CON-R-105](../rules/CON-R-105.md) | 9. Payment lifecycle | A credit is issued: CreditFlag plus AppliedToPayTranID points a credit transaction at the transaction it offsets. | Observed |
| [CON-R-106](../rules/CON-R-106.md) | 9. Payment lifecycle | Tax is applied: four parallel tax components, with TaxesIncludedFlag saying whether they sit inside TotalAmount or are additional to it. | Observed |
| [CON-R-107](../rules/CON-R-107.md) | 9. Payment lifecycle | Aging is computed: AgingAmountForMonth1..3 and AgingAmountRemainder bucket from the invoice/effective date — the base date itself is inferred, not confirmed. | Observed |
| [CON-R-108](../rules/CON-R-108.md) | 9. Payment lifecycle | Due-date aging is computed: DueDateAgingAmountForMonth1..3 and its remainder use the same buckets measured from DueDate. | Observed |
| [CON-R-109](../rules/CON-R-109.md) | 9. Payment lifecycle | An expense type is chosen: CodeExpenseTypeID selects both the GL account set and the accounting treatment (CodeASC842ScheduleID, CodeIFRS16ScheduleID, CodeSLScheduleID) in one action. | Observed |
| [CON-R-110](../rules/CON-R-110.md) | 9. Payment lifecycle | A transaction is posted: all twenty account numbers from CodeExpenseType are snapshotted onto the transaction row, not looked up again at export time. | Derived |
| [CON-R-111](../rules/CON-R-111.md) | 9. Payment lifecycle | Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is un | Inferred |
| [CON-R-112](../rules/CON-R-112.md) | 9. Payment lifecycle | A batch is exported: ExportBatchNumber is set when the row leaves for AP. | Observed |
| [CON-R-113](../rules/CON-R-113.md) | 9. Payment lifecycle | AP settles a payment: CheckNumber/CheckDate/CheckAmount/CodeCheckCurrencyTypeID are written back — check currency may differ from transaction currency with no FX rate field to reconcile the two. | Observed |
| [CON-R-114](../rules/CON-R-114.md) | 9. Payment lifecycle | A landlord invoice is imported: IMPORT_INVOICE extracts VendorName/Address/TaxID and CustomerName/Address/TaxID as text, kept alongside the resolved EmployerID. | Derived |
| [CON-R-115](../rules/CON-R-115.md) | 9. Payment lifecycle | An invoice line is matched to a payment: LinkLandlordInvPaymentTxn allocates AllocationAmount/AllocationDate between LandlordInvoiceItemID and PaymentTransactionID. | Observed |
| [CON-R-116](../rules/CON-R-116.md) | 9. Payment lifecycle | A match has a difference: VarianceAmount and VarianceReason are stored on the join itself, alongside ReconciliationStatus. | Observed |
| [CON-R-117](../rules/CON-R-117.md) | 9. Payment lifecycle | A payment is fully matched: PaymentTransaction.IsInvoiceReconciled is set when the three-way match completes. | Observed |
| [CON-R-118](../rules/CON-R-118.md) | 9. Payment lifecycle | Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side. | Observed |
| [CON-R-119](../rules/CON-R-119.md) | 9. Payment lifecycle | An accrual is posted: AccrualTransaction carries PeriodAmount, PeriodBeginDate/EndDate, PeriodNumber/Year and PostingDate, with its own GL slots, driven by GENERATE_ACCRUALS. | Observed |
| [CON-R-120](../rules/CON-R-120.md) | 9. Payment lifecycle | An accrual clause is configured: ExpenseAccrualSetup accrues an expense ahead of its billing, using CodeAccrualTypeID, CurrentAnnualExpense/CurrentPeriodExpense, and optionally IsDailyRent + RentableA | Observed |
| [CON-R-121](../rules/CON-R-121.md) | 9. Payment lifecycle | An accrual schedule is generated: period-by-period accrual amounts are produced from AccrualRate/DailyAccrualRate, with the same daily-rate support as recurring expense. | Observed |
| [CON-R-122](../rules/CON-R-122.md) | 9. Payment lifecycle | Accruals are forecast: ForecastCapPercent/ForecastGrowthPercent/ForecastAdjustment and their Plan* twins grow the accrual independently of the contract's own escalation. | Observed |
| [CON-R-123](../rules/CON-R-123.md) | 9. Payment lifecycle | Percentage-rent accrual is reconciled: VirtualPRAccrualPeriod's computed AccrualAmount{ThisPeriod,PriorPeriods,Total} is displayed next to the PostedAccrualAmount{...} that was actually posted, with I | Observed |
| [CON-R-124](../rules/CON-R-124.md) | 9. Payment lifecycle | Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own. | Observed |
| [CON-R-125](../rules/CON-R-125.md) | 10. Suppression and gating | Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer. | Observed |
| [CON-R-126](../rules/CON-R-126.md) | 10. Suppression and gating | Any generation: ReadyForPaymentFlag on ExpenseSetup and ExpenseSchedule is a positive gate — both must be true. | Observed |
| [CON-R-127](../rules/CON-R-127.md) | 10. Suppression and gating | Forecast inclusion: only ExpenseSetup rows flagged IncludeInPlanForecast appear in VirtualExpenseForecastPeriod. | Observed |
| [CON-R-128](../rules/CON-R-128.md) | 10. Suppression and gating | Accrual scope: only ContractTerm rows flagged IncludeTermForAccruals are accrued. | Observed |
| [CON-R-129](../rules/CON-R-129.md) | 10. Suppression and gating | Liability scope: Covenant.HoldAmountInSchedLiability excludes a covenant amount from the ASC 842 scheduled liability. | Observed |
| [CON-R-130](../rules/CON-R-130.md) | 10. Suppression and gating | Disclosure scope: SLSummary.IsIncludeInRollForwardReport controls inclusion in the roll-forward disclosure. | Observed |
| [CON-R-131](../rules/CON-R-131.md) | 4.1 Typing hazard register (Constitution §4.4) | Migrating any landed Postgres column: every column across 33 tables is TEXT except 31 VARCHAR(64) primary keys — no numeric, date or boolean column exists; every value must be parsed and validated on  | Derived |
| [CON-R-132](../rules/CON-R-132.md) | 11. Typing and integrity rules for the rebuild (Constitution §4.4) | Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount. | Observed |
| [CON-R-133](../rules/CON-R-133.md) | 11. Typing and integrity rules for the rebuild (Constitution §4.4) | Migrating LandlordInvoiceItem: money, date and boolean are all stored as text on this reconciliation grid; replace the seven PayTrans* mirror fields with a join. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | 11. Typing and integrity rules for the rebuild (Constitution §4.4) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling p | Observed |
| [CON-R-135](../rules/CON-R-135.md) | 11. Typing and integrity rules for the rebuild (Constitution §4.4) | Any usage-based rent arithmetic: 6-decimal precision is required on unit rates; use BigDecimal with explicit scale and rounding mode, never a binary float. | Observed |
| [CON-R-136](../rules/CON-R-136.md) | 11. Typing and integrity rules for the rebuild (Constitution §4.4) | Any percentage arithmetic: sTYPE_PERCENTAGE fields multiply money in the pro-rata, breakpoint and CPI paths; store as BigDecimal and fix the scale and rounding policy at every multiplication step. | Observed |
| [CON-R-137](../rules/CON-R-137.md) | 11. Typing and integrity rules for the rebuild (Constitution §4.4) | Any recovery measure is unset: for the rebuild, model recovery measures as nullable BigDecimal, never zero-defaulted — a zero default silently produces spurious 100% variances. | Inferred |
| [CON-R-138](../rules/CON-R-138.md) | 12. Contract status and lifecycle | A contract's status is set: CodeContractStatusID resolves to exactly one of three values — AI Abstracted, Active, Inactive — and none is a BRD-24 lifecycle stage. | Observed |
| [CON-R-139](../rules/CON-R-139.md) | 12. Contract status and lifecycle | A status value is deleted: Active carries no delete action — the platform protects at least one seeded value as system-required. | Observed |
| [CON-R-140](../rules/CON-R-140.md) | 12. Contract status and lifecycle | Recording how a contract was abstracted: provenance (AI-abstracted or not) is encoded as a state value, so a contract can be AI-abstracted and active at once — the two axes are conflated in this one f | Observed |
| [CON-R-141](../rules/CON-R-141.md) | 12. Contract status and lifecycle | Determining a contract's lifecycle stage: the stage is derived from date fields (ActualStartDate/OpenYear, StatusEffectiveDate, PossessionBeginDate/EndDate, PaymentsBeginDate/EndDate, ExpireDate/Actua | Derived |
| [CON-R-142](../rules/CON-R-142.md) | 12. Contract status and lifecycle | A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-c | Derived |
| [CON-R-143](../rules/CON-R-143.md) | 12. Contract status and lifecycle | Resolving the phase enumeration: Project Phase Code is used by 11 objects but is not among the 207 Firm Drop Downs — an engine-governed enumeration, not a tenant-configurable one. | Observed |
| [CON-R-144](../rules/CON-R-144.md) | 12. Contract status and lifecycle | The tenant needs a lifecycle status: Contract.Firm_LeaseStatus (a Firm-scope custom code field, with a Firm_LeaseStatusNotes companion) is ASG's own answer, sitting in the same Contract Info sub-group | Observed |
| [CON-R-145](../rules/CON-R-145.md) | §13 Rent generation | A user invokes `Generate Rent` · `ExpenseSchedule` rows for the contract · Generation reads the Schedule layer, not the Setup layer · A contract with Expense Setups but an empty Expense Schedule gener | Derived |
| [CON-R-146](../rules/CON-R-146.md) | §13 Rent generation | The Generate Payments dialog opens · Period (month + year), Posting Date, Batch Date · A batch number is minted as `RNT<yyyymmdd>-<sequence>` · The run is identified by that batch number · Observed | Observed |
| [CON-R-147](../rules/CON-R-147.md) | §13 Rent generation | A user selects a generation scope · `Generate Option` · One of `Single Contract`, `Payables — All Contracts`, `Receivables — All Contracts`, `All Contracts` · Three of the four run across every contra | Observed |
| [CON-R-148](../rules/CON-R-148.md) | §13 Rent generation | A transaction is generated · Expense type, period, proration method · Description is `<MNEMONIC> MM/YYYY`, or `<MNEMONIC> - PRS <from>-<to>` when prorated · The row records how it was computed. Mnemon | Observed |
| [CON-R-149](../rules/CON-R-149.md) | §13 Rent generation | A transaction is generated · `invoiceAmount`, `primaryTax`, `APExportTax1..4Number` · `totalAmount` = `invoiceAmount` + tax · Up to four tax components are carried per transaction · Observed | Observed |
| [CON-R-150](../rules/CON-R-150.md) | §13 Rent generation | A transaction is generated · — · In this tenant every generated row arrives `processedFlag = true` and approval status `Approved` · Whether that is tenant configuration or engine behaviour is unresolv | Observed |
| [CON-R-151](../rules/CON-R-151.md) | §13 Rent generation | A transaction is generated · `exportBatchNumber` · Generation does not set it — null on every row sampled · GL export is a separate, later stage from generation · Derived | Derived |
| [CON-R-152](../rules/CON-R-152.md) | §13 Rent generation | An Expense Setup is generated from · `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates · One setup fans out to one transaction per allocation · The vendor sp | Observed |
| [CON-R-153](../rules/CON-R-153.md) | §14 The CAM recovery waterfall | A recovery period is calculated · Controllable, Non-Controllable, Deductions · `Sub Total #1 = C + NC − D` · `SubTotal1{Gross,Net}` · Observed | Observed |
| [CON-R-154](../rules/CON-R-154.md) | §14 The CAM recovery waterfall | Sub Total #1 is known · Admin Fee % amount, Admin Fee, Additions · `Pass-Through = ST1 + AF% + AF + A` · `PassThrough{Gross,Net}` · Observed | Observed |
| [CON-R-155](../rules/CON-R-155.md) | §14 The CAM recovery waterfall | Pass-Through is known · Recoveries · `Sub Total #2 = PT − R` · `SubTotal2{Gross,Net}` · Observed | Observed |
| [CON-R-156](../rules/CON-R-156.md) | §14 The CAM recovery waterfall | Sub Total #2 is known · Pro Rata Share Rate; Occupancy Factor · `Net Pass-Through = ST2 × PRR` on Budgeted/Reported/Prior, but `ST2 × PRS × Occ` on Approved — the gross-up provision · `NetPassThrough{ | Observed |
| [CON-R-157](../rules/CON-R-157.md) | §14 The CAM recovery waterfall | Net Pass-Through is known · Pre-Paid Amount · `Net Amount Due = NPT − PP` · `NetAmountDue{Gross,Net}` · Observed | Observed |
| [CON-R-158](../rules/CON-R-158.md) | §14 The CAM recovery waterfall | Net Amount Due is known · Adjustments · `Revised Amount Due = Net + Adj` · `RevisedNetAmountDue{Gross,Net}` · Observed | Observed |
| [CON-R-159](../rules/CON-R-159.md) | §14 The CAM recovery waterfall | Any recovery figure is stored · — · Four bases (Budgeted, Reported, Approved, Prior) × {Gross, Net}, with five pairwise variances (A-B, A-P, B-P, R-A, R-P) materialised as both amount and percentage f | Observed |
| [CON-R-160](../rules/CON-R-160.md) | §14 The CAM recovery waterfall | A prior-period measure is absent · `…NoZeroDef` columns · Prior measures are nullable, never zero-defaulted — a missing prior period is unknown, not zero, or every first-year reconciliation reports sp | Observed |
| [CON-R-161](../rules/CON-R-161.md) | §14 The CAM recovery waterfall | Classifying any field · View Object Model filters · Of 7,047 fields: 3,437 editable (49%), 1,804 non-math computed (26%), 422 math (6%). 90% of all formula fields live on `ExpenseRecovery` · Field cla | Observed |
