# The straight-line engine

**Stated up front.** `SLSummary` / `SLPeriod` is a classic **summary/period** pair: one header row per
accounting schedule, one child row per fiscal period. The name is historical — the same pair carries
ASC 840 straight-line schedules, ASC 842 schedules and IFRS 16 schedules, distinguished only by the
three flags `IsSLSchedule` / `IsASC842Schedule` / `IsIFRS16Schedule`. In the live tenant only one of
the three is usable: the `Straight Line Schedule Type Code` and `IFRS 16 Schedule Type Code` tables
are both **empty**, and `ASC 842 Schedule Type Code` holds exactly one row, `842 Rent`. The straight-line arithmetic
proper survives in two `SLPeriod` fields: `PeriodExpenseAmount` (*"The cash rent straight lined over
the life of the schedule"*) and `PeriodDeferredAmount` (*"The difference between the period cash rent
and straight line rent expense"*), accumulating into `CumulativeDeferredBalance`.

Two things in the brief for this document turned out to be wrong against the evidence, and are
corrected below: `SuspendSL` is **dead**, and the two hold flags belong to `AlternateRentSchedule`,
not to the straight-line engine.

*Evidence class: **Observed** unless stated. Vendor quotations from `_xlsx_lucernex_jcrew.txt`
`Definition` column; field types from `docs/data-fields/sl-summary.md`, `sl-period.md`,
`alternate-rent-schedule.md`; admin route from `docs/admin/004-company-administration.md`.*

## ⚠ The legacy straight-line schedule type is not configured

**Observed**, 2026-09-10, `FirmCodeEdit.jsp?TableType=2161`: the `Straight Line Schedule Type Code`
table returns "No rows to display". Its ASC 842 sibling (2162) holds one row; its IFRS 16 sibling
(2163) is likewise empty. *(Source: `docs/data-model/code-table-registry.md`.)*

So the tables in this document are, in production, an **ASC 842 engine wearing a straight-line
engine's name**. Three consequences:

| Consequence | Confidence |
|---|---|
| `SLSummary.CodeSLScheduleID` has no valid target, so no new legacy straight-line schedule can be created | **Derived** |
| `CodeExpenseType.CodeSLScheduleID` must be null on every expense type | **Derived** |
| `SLSummary.IsSLSchedule` should be false on every row — a true value would mean a schedule outlived deletion of its schedule type | **Derived**; worth querying as a data-integrity check |

The straight-line *arithmetic* is not dead — `PeriodExpenseAmount`, `PeriodDeferredAmount` and
`CumulativeDeferredBalance` are exactly how an ASC 842 operating lease is expensed. What is dead is
the *ASC 840 schedule type* that predates the standard. This also explains why
`Contract.Firm_LastDeferredSLEntry` / `.Firm_LastDeferredSLEntryDate` / `.Firm_LastDeferredSLTotal`
exist as **firm-scoped custom fields**: ASG built its own ASC 840 deferred-rent carry-forward rather
than keeping a legacy schedule type alive. That makes those three fields a likely migration
requirement, not a curiosity.

## Summary vs. period: the division of labour

| | `SLSummary` (`s_l_summary`, 134 fields) | `SLPeriod` (`s_l_period`, 79 fields) |
|---|---|---|
| Grain | One schedule | One fiscal period of one schedule |
| Holds | Assumptions, initial balances, PV components, modification deltas, recalculation state, disclosure rollups | The period ledger: cash, expense, interest, amortization, balances, FX |
| Written by | Schedule creation / remeasurement | Schedule generation, one row per period |
| Read by | Roll-forward and maturity reports | The rent schedule grid, the GL export |
| Denormalized onto `Contract` | `CurrentStraightLineAssetBalance`, `CurrentStraightLineLiabilityBalance` — *"The asset/liability balance value from the first active period"* | — |

`SLSummary` also carries a *second* rollup layer inside itself: 25 roll-forward fields and 14
maturity-ladder fields that are aggregates over its own `SLPeriod` children. So the module has three
levels of aggregation — period → schedule → contract — and the middle one is stored, not derived at
read time.

## What a period row holds

Full field-by-field composition is in [`data-model.md`](data-model.md#the-slperiod-row-shape). The
accounting payload, with the vendor's own definitions:

| Field | Vendor definition |
|---|---|
| `PeriodCashAmount` | *"The amount of cash payments made during the period."* |
| `PeriodExpenseAmount` | *"The cash rent straight lined over the life of the schedule."* |
| `PeriodDeferredAmount` | *"The difference between the period cash rent and straight line rent expense."* |
| `CumulativeDeferredBalance` | *"The sum of the deferred rent from the beginning of the schedule to the current period in the straight line schedule."* |
| `PeriodInterestAmount` | *"The interest owed on the liability based on the discount rate."* |
| `PVOfPeriodCashAmount` | *"The Present Value of a future cash payment in today's valuation. This value is discounted to present value from the period that the payment will be made."* |
| `AssetAmount` | *"This is the current value of the rented asset. The value of your asset is dependent upon whether you are calculating your lease as a Finance or Operating lease."* |
| `LiabilityAmount` | *"This is the current value of the liability. The value of your liability is dependent upon whether you are calculating your lease as a Finance or Operating lease."* |
| `PeriodAssetAmortizationExpense` | *"The amount that the asset value is reduced from one period to the next."* |
| `PeriodLiabilityAmortizationExpense` | *"The amount that the liability value is reduced from one period to the next."* |
| `CumulativeAssetAmortExpense` (label **Accumulated Amortization Balance**) | *"For the first period of your schedule, this field's value is equal to the Asset Amortization Expense. For each subsequent period, this field's value is equal to the Asset Amortization Expense + the previous period's Accumulated Amortization Balance."* |
| `GrossAssetBalance` | *"This field's value is equal to the Asset Balance + the Accumulated Amortization Balance."* |
| `ShortTermRentExpense` | *"The sum of all the rent expenses for the next 12 months."* |
| `LongTermRentExpense` | *"The sum of all rent expenses beyond 12 months."* |
| `Forward12MonthAssetChange` | *"This is the sum of the asset amortization for the next 12 months."* |
| `Forward12MonthLiabilityChange` | *"This is the sum of the liability amortization for the next 12 months."* |
| `LongTermLiability` | *"The long-term liability is the current liability balance minus the short-term liability."* |
| `NumberDays` | *"The length of the period in days."* |
| `CumulativePeriodNumber` | *"The current period number out of the total cumulative number of periods in the lease."* |
| `RecordStatus` | *"This field displays the current status of the period — either posted, not posted, or mixed."* |

Two of these are the closed-form straight-line identities a rule engine can consume directly:

```
GrossAssetBalance[n]        = AssetAmount[n] + CumulativeAssetAmortExpense[n]
CumulativeAssetAmortExpense[n] = PeriodAssetAmortizationExpense[n]
                               + (n = 1 ? 0 : CumulativeAssetAmortExpense[n-1])
LongTermLiability[n]        = LiabilityAmount[n] − shortTermLiability[n]
PeriodDeferredAmount[n]     = PeriodCashAmount[n] − PeriodExpenseAmount[n]
```

### The short-term liability is firm-configurable

`SLPeriod` stores **both** candidate short-term liability figures and lets a firm setting choose:

| Field | Vendor definition |
|---|---|
| `Forward12MonthLiabilityAmortBased` | *"This is the 12-Month Forward Change in Liability Balance if you have selected **Liability Amortization Based** as your setting for the Short-Term/Long-Term Liability Calculation Method."* |
| `Forward12MonthLiabilityPVBased` | *"…if you have selected **PV Based** … Please see the Lucernex Online Help > Toolbar > System Administrator Dashboard > Company Administration > Manage Company > Financial Settings page for the formula this setting uses."* |

The setting lives on `Admin > Manage Company > Financial Settings`, which is **not** an object in the
223-object dump — `Firm` has only 18 fields and the plausible carrier is `JSONConfigText(Text)`.
The PV-based formula itself is not in any offline artifact.

### The amortisation basis is a portfolio setting, not a schedule property

*Added 2026-09-10 from the live tenant.* Three independent `Program` (Portfolio) columns decide how
each schedule column is spread across periods:

| Column | Governs | Restriction |
|---|---|---|
| `Program.SLAssetAmortizeMethod` | `SLPeriod.PeriodAssetAmortizationExpense` | *"This setting impacts **only ASC 842 Finance leases**."* — and ASC 842 is the only standard configured in this tenant |
| `Program.SLCashAmortizeMethod` | `SLPeriod.PeriodCashAmount` | none stated |
| `Program.SLExpenseAmortizeMethod` | `SLPeriod.PeriodExpenseAmount` | none stated |

Each takes one of two values, named in the live GraphQL API as the enum
`GaapAmortizeMode { PER_DAY, PER_PERIOD }`:

- **`PER_PERIOD`** — *"distributes the amortization equally among periods"*. Every period gets
  `total / N`, regardless of length.
- **`PER_DAY`** — *"distributes the amortization according to the number of days in the period"*.
  Each period is weighted by `SLPeriod.NumberDays`.

That is what `SLPeriod.NumberDays` is for, and it is why it is stored on every row rather than
derived from `BeginDate`/`EndDate` at read time.

`Program.SLProrate35As28` modifies `PER_PERIOD` only: a partial first or last period is prorated on a
28-day multiplier, and *"If you have a partial period that is greater than or equal to 28 days, it
will be considered a whole period by the system and will not prorate."* On a 13-period retail
calendar — where periods are 4 or 5 weeks (`FiscalPeriod.Is4or5WeekPeriod`) — this switch and the
`PER_DAY`/`PER_PERIOD` switch together change the number in every single period.

See `ACC-R-056` and `ACC-R-057`. *(Sources: `_xlsx_lucernex_jcrew.txt`;
`docs/data-model/graphql-api.md`.)*

### FX: 12 of the 79 fields

| Field | Vendor definition |
|---|---|
| `AssetTranslationAdjustment` | *"Asset Translation Adjustment = Current Asset Balance + Current Asset Amortization Expense − Prior Month's Asset Balance"* |
| `LiabilityTranslationAdjustment` | *"Liability Translation Adjustment = Current Asset Balance + (Current Month's Payment − Current Month's Interest) − Prior Month's Asset Balance"* |
| `CumulativeTranslationAdjustment` | *"Cumulative Translation Adjustment = Current Month's Asset Translation Adjustment − Liability Translation Adjustment"* |
| `LiabilityFXImpact` | *"Period Liability FX Impact = (FX rate for this period − initial FX rate) × Period Liability Balance"* |
| `ConversionRateAverage` / `ConversionRateMonthEnd` | *"The period average rate."* / *"The cash rate."* — both `sTYPE_NUMBER_FRACTION6DIGITS` |
| `AssetAmountTranslated`, `LeaseLiabilityTranslated`, `InterestTranslated`, `CashPaymentTranslated`, `AssetAmortizationExpenseTranslated` | *"The translated value of the … column in your lease accounting schedule."* |
| `FXGainLoss` | (no vendor definition) |

**The `LiabilityTranslationAdjustment` formula as published is almost certainly a documentation
error** — it subtracts prior-month *asset* balance from current *asset* balance while calling itself a
liability adjustment. Flagged as an open question; do not code it as written.

These fields populate *"in the Fiscal Details grid when you calculate the FX Impact on the Rent
Schedule page when a contract or equipment contract is marked as In Translation"* — i.e. gated on
`Contract.IsTranslation`.

**Which rate is used is chosen per column, at portfolio level.** `Program` carries fourteen
`Exchange Rate Type Code` selectors — seven schedule columns (asset amortisation, asset balance,
liability amortisation, liability balance, cash expenses, interest, single lease expense) x two
modes, where the `...SubFXTypeID` variant applies to *"contracts in need of translation"* and the
plain variant to *"contracts in need of revaluation"*. See `ACC-R-059`. This partly answers the
Translation-vs-Revaluation open question: the "mapping" that `Contract.IsTranslation` selects between
is portfolio-scoped and column-by-column, not a single firm-wide toggle.

## The recalculation state machine

The engine does not recompute on every edit. It sets a dirty flag and waits.

| Field | Type | Vendor definition |
|---|---|---|
| `NeedsRecalculation` (label **Recalc?**) | `sTYPE_CHECKBOX` | *"When set to Yes, this flag indicates that the lease accounting schedule must be recalculated."* |
| `RecalcTriggerDate` | `sTYPE_DATE` | *"The date that the Recalc? flag was triggered."* |
| `NeedsRecalcModifiedByLastMember` | `sTYPE_MEMBER` | *"This field lists **the last** member whose action would have caused the Recalc? flag to change."* |
| `NeedsRecalcModifiedByMemberIDList` | `sTYPE_MEMBER` | *"This field lists **all** members who have made changes that would cause the Recalc? flag to change."* |
| `RecalcOverrideNotesIDList` | `sTYPE_RECALC_NOTES` | Links to `RecalcOverrideNotes` — *"A free-text note explaining why a financial recalculation was manually overridden."* |

### Documented triggers

| Trigger | Evidence |
|---|---|
| Changing `CodeASC842ScheduleID` or `CodeIFRS16ScheduleID` **on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page** | Vendor definition, repeated verbatim on all five objects that carry the field (`SLSummary`, `ContractFinancialTest`, `AcctingAssumptionAdjust`, `Covenant`, `CodeExpenseType`) |
| Creating a new `ExpenseSetup` with an `ExpenseSchedule` whose expense type is used by the schedule | Vendor definition of `SLSummary.AssociatedExpenseSetupIDs`: *"If a new expense setup with an expense schedule is created, the accounting schedule associated with the expense type will have its Recalc? flag flipped to Yes."* |
| Changing `SLSummary.CodeAccountingMethodID` | Vendor: *"If its value is changed, you will need to remeasure your schedule."* (states the consequence, not the flag) |

**Derived**: `AssociatedExpenseSetupIDs` is a maintained reverse index — *"returns a list of associated
expense setup IDs that use the expense type used in the accounting schedule you are viewing"* — and it
exists specifically so the engine can find which schedules to dirty when an expense setup changes. A
rebuild that omits it will need an equivalent index or an expensive scan.

The dashboard widget **"ASC 842 Recalculations"** is the operational surface for this flag.
*(Observed, `docs/screens/001-dashboard-home.md` line 72.)*

## Approval and posting

| Field | Type | Vendor definition |
|---|---|---|
| `SLSummary.IsApproved` | `sTYPE_CHECKBOX` | *"This flag indicates that the schedule has been approved. **Once a schedule has been approved, it cannot be un-approved.**"* — but see the workflow below: this flag is the *end* of a three-step process, not a checkbox a user ticks |
| `SLSummary.LastPostedDate` | `sTYPE_DATE` | *"the begin date of the last posted period"* |
| `SLSummary.LastPostedEndDate` | `sTYPE_DATE` | *"the end date of the last posted period"* |
| `SLSummary.PostedEndDate` | `sTYPE_DATE` | *"The last posted fiscal period End Date of the schedule being modified."* |
| `SLSummary.LastBalancePosted` | `sTYPE_MONEY` | *"This is the asset minus the liability as of the last posted period."* |
| `SLSummary.LastPostedBalanceSheetImpact` | `sTYPE_MONEY` | *"the portion of the last posted balance that is to remain on the balance sheet"* |
| `SLPeriod.PostedDate` | `sTYPE_DATE` | *"The date that the Accounts Receivable transaction was posted."* |
| `SLPeriod.RecordStatus` | `sTYPE_TEXT` | posted / not posted / **mixed** |

Approval is one-way. Posting is per-period and can be partial within a period ("mixed"). Together,
`LastPostedEndDate` is the cut line: everything at or before it is closed, everything after is
re-derivable, and a modification measures its deltas against that line.

### Approval is a three-step, two-party workflow

*Added 2026-09-10. **Observed** in the running tenant at build `26.08.0.46`; full capture in
[`../layouts-and-forms/forms-vs-pages-vs-layouts.md`](../layouts-and-forms/forms-vs-pages-vs-layouts.md).*

The tenant runs a live workflow named **"ASC 842 Schedule Review/Approval"** — three ordered steps,
every one `Type = Form`, every one `Approval Level = Member`, each bound to its own form layout:

| # | Step | Bound layout |
|---:|---|---|
| - | (submission) | `ASR Submit ASC 842 Schedules` |
| 1 | Initial Review of ASC 842 Schedules | `ASR Initial Review of ASC 842 Schedule` |
| 2 | Approve ASC 842 Schedules (ASG) | `ASR Approve ASC 842 Schedules (ASG)` |
| 3 | Approve ASC 842 Schedules (Client) | `ASR Approve ASC 842 Schedules (Client)` |

The form type carries sequence prefix `ASR` and is attachable **only** to `Portfolio` and
`RE Contract` — notably **not** to `Equipment Contract`, even though equipment leases generate ASC 842
schedules.

Three consequences for the rebuild:

1. **Generating a schedule does not publish it.** The calculation produces a candidate; a human chain
   accepts it. `SLSummary.IsApproved` is the *terminal* state of that chain.
2. **A schedule has a state, not a flag.** `draft -> submitted -> under initial review ->
   ASG-approved -> client-approved`. Only the last of those five is representable on `SLSummary`; the
   intermediate states live in the workflow instance. Nothing in the offline schema hints at this.
3. **Two parties sign off.** ASG approves, then the client approves. An accounting engine that models
   a single approver has modelled the wrong process.

See `ACC-R-060`, `ACC-R-061`, `ACC-R-062`.

## Schedule lifecycle

```
                          ┌─────────────────────────────────┐
 GenerateStraightLineRent │                                 │
 GenerateFASBSchedule ───►│  SLSummary (active)             │
 GenerateIFRS16Schedule   │  Inactive = false               │
                          │  IsApproved = false             │──► SLPeriod × N
                          └──────────────┬──────────────────┘
                                         │
                 ASC 842 Schedule Review/Approval workflow — 3 form steps
                 submit ► initial review ► approve (ASG) ► approve (Client)
                                         │
                                         │ IsApproved := true   (one-way)
                                         │ periods posted       (RecordStatus)
                                         │
        contract change / expense-type change / covenant change
                                         │
                                         ▼
                          NeedsRecalculation := true, RecalcTriggerDate := today
                          NeedsRecalcModifiedBy{LastMember,MemberIDList} updated
                                         │
              ┌──────────────────────────┼──────────────────────────┐
              │                          │                          │
        recalculate in place      create replacement          override with a
                                  SLSummary                    RecalcOverrideNotes
                                         │
                                         ▼
                          new SLSummary.PriorLastPostedPeriodID := old SLSummaryID
                          new SLSummary.PostedEndDate           := old LastPostedEndDate
                          new SLSummary.PostedInit{Asset,Liability}Adj computed
                          old SLSummary.Inactive := true, InactiveDate := today
```

*Evidence class: **Derived**. Every box and field is Observed; the transitions between them are
reconstructed from the vendor definitions of `Inactive`, `PriorLastPostedPeriodID`, `PostedEndDate`
and the four `Posted*Adj*` fields. The three generate buttons are Observed
(`sTYPE_SUBMITBUTTON` on `Contract`). Whether recalculation happens in place or always creates a
replacement is the central open question below.*

## Suspension and hold flags — correcting the brief

All three flags named in the brief live on **`AlternateRentSchedule`** (`alternate_rent_schedule`,
25 fields), not on `SLSummary` or `SLPeriod`. Exhaustive search of all 223 objects finds
`SuspendSL`, `SetExpHoldFlag` and `SetPRHoldFlag` exactly once each, all on that one object.

| Field | Label | `Functional Field` | Vendor definition |
|---|---|---|---|
| `SuspendSL` | Suspend SL? | **No** | **"This field is no longer used."** |
| `SetExpHoldFlag` | Set payments for Recurring Expenses on Hold | **No** | *"This check box sets a Hold flag on all recurring expense transactions generated while the contract is in alternate rent."* |
| `SetPRHoldFlag` | Set payments for Percent Rent on Hold | **No** | *"This check box sets a Hold flag on all percentage rent transactions generated while the contract is in alternate rent."* |

Three findings follow:

1. **`SuspendSL` is dead and must not be rebuilt.** Whatever "suspend straight-line" meant in an
   earlier Lucernex release, the current product does not implement it. If ASG Edge+ needs schedule
   suspension it is a **new** requirement, not a port.
2. **The two hold flags do not touch the accounting schedule at all.** They set
   `PaymentTransaction.HoldFlag` / `ExpenseSchedule.HoldFlag` on *generated cash transactions* during
   an alternate-rent window. They are a cash-side control.
3. **Every `HoldFlag` in the module is documented as inert.** `AccrualTransaction.HoldFlag` and
   `ExpenseAccrualSetup.HoldFlag` both read *"This flag is informational-only."* `HoldFlag` also
   appears on `ExpenseSchedule`, `ExpenseSetup`, `PaymentTransaction` and `PropertyTaxBill` — seven
   occurrences in total, all Boolean.

The nearest thing to a genuine suspension mechanism anywhere in the module is
`Asset.CodeAssetSuspensionStatusID` (`sCODE_ASSET_SUSPENSION_STATUS`), whose vendor definition is only
*"Select the asset suspension status from this field"* and whose code values are not available
offline.

## "Modify Straight Line Status"

**There are two distinct controls with this name, and they are not the same thing.**

| | Admin utility | Contract action button |
|---|---|---|
| Where | System Administrator Dashboard → **Data/PS Tools** | Contract summary page → `Summary Information / Summary Page Buttons` |
| Identifier | Route `/en/admin/lxadmin/SLDemoTweaks.jsp` | Field `Contract.ModifyStraightLineStatus`, type `sTYPE_SUBMITBUTTON` |
| Label | "Modify Straight Line Status" | "Modify Straight-Line Status" |
| Scope | Firm-wide (it sits beside *Data Conversion Cleaner*, *Delete Entities*, *Export Schema*) | One contract |
| Evidence | **Observed**, `docs/admin/004-company-administration.md` line 162; classified there as *"Explicitly mutating/high risk; not activated"* | **Observed**, `docs/data-fields/all-fields.csv` and `contract.md`; no vendor definition |

### What the admin utility plausibly acts on

*Evidence class: **Inferred**. The page was deliberately not opened during exploration. What follows
is reasoning from the route name, its placement, and the schema — it is a hypothesis list for the live
check, not a finding.*

The route is `SLDemoTweaks.jsp` under `lxadmin`. `lxadmin` is Accruent's internal-support namespace
(its siblings are `DataLoadTweaks.jsp`, `EmailTest.jsp`, `DeleteEntities.jsp`), and "Tweaks" plus
"Demo" reads as a support/demo-data fixer rather than a customer-facing accounting function. The
`SLSummary` fields it would need to touch, in descending order of likelihood:

| Rank | Candidate | Why |
|---|---|---|
| 1 | `NeedsRecalculation`, `RecalcTriggerDate` | The only schedule "status" a support engineer routinely needs to force. Clearing a stuck Recalc? flag across a firm is exactly the shape of a Data/PS Tool. |
| 2 | `IsApproved` | Approval is documented as **irreversible** through the normal UI. An admin back door is the only way to undo it, and back doors for irreversible flags are precisely what `lxadmin` holds. |
| 3 | `Inactive`, `InactiveDate` | Reactivating a schedule superseded in error. |
| 4 | `SLPeriod.RecordStatus`, `SLPeriod.PostedDate`, `SLSummary.LastPosted*` | Un-posting periods after a bad GL export. |
| 5 | `IsSLSchedule` / `IsASC842Schedule` / `IsIFRS16Schedule` | Re-badging a schedule generated under the wrong standard — a plausible demo-data fix. |

The Contract-level button is the far more likely home of ordinary user-facing behaviour: given that
`IsApproved`, `Inactive` and `NeedsRecalculation` are the three status flags on `SLSummary`, and given
that the button sits next to `GenerateStraightLineRent` / `GenerateFASBSchedule` /
`GenerateIFRS16Schedule` on the same summary page, it most plausibly opens a modal to approve,
inactivate, or clear the recalc flag on that contract's schedules. This is **Inferred** and is the
first open question below.

## Open questions

Ranked by rebuild impact.

1. **(new) ⚠ Are there any `SLSummary` rows with `IsSLSchedule = true`?** The straight-line schedule
   type table is empty, so there should be none. Any that exist are orphaned schedules whose type was
   deleted — and they would still be carrying balances. A one-query data-integrity check with real
   migration consequences.
2. **(new) ⚠ How are equipment-lease ASC 842 schedules approved?** The `ASC 842 Schedule
   Review/Approval` form type has `Equipment Contract = No`, yet `Asset` carries the full ASC 842
   field set and equipment contracts have a `GenerateFASBSchedule` button. Either equipment schedules
   bypass the gate or they are approved at portfolio level.
3. **(new) What does each `ASR` form layout collect?** Four layouts define the approval record —
   `Submit`, `Initial Review`, `Approve (ASG)`, `Approve (Client)`. None has been opened. Their field
   sets are what ASG Edge+ must reproduce as the approval payload.
4. **(new) What happens on rejection at step 2 or 3?** No rollback or re-open path is documented, and
   `SLSummary` has no "rejected" representation.
5. **(new) Do the three `Program.SL*AmortizeMethod` columns store the enum name (`PER_DAY`), a
   display string (`Per Day`), or a code?** They are `Text` in Postgres; the API enum is
   `GaapAmortizeMode`. A migration needs the stored form.
6. **(resolved 2026-09-10)** *What is the amortisation basis?* — `Program.SLAssetAmortizeMethod` /
   `.SLCashAmortizeMethod` / `.SLExpenseAmortizeMethod`, values `PER_DAY` / `PER_PERIOD`.
   See `ACC-R-056`.
7. **Does a recalculation update the existing `SLSummary` in place, or always create a replacement?**
   If in place, the schedule-version chain is only used for modifications; if always, every recalc
   creates a new row and the `Inactive` chain is long. This determines the entire persistence design.
8. **What does the Contract-level `ModifyStraightLineStatus` button actually do?** Open a contract with
   an approved schedule and click it (read the modal; do not submit). Record every field it offers.
9. **What does `/en/admin/lxadmin/SLDemoTweaks.jsp` render?** Open read-only. The five candidates above
   are ranked guesses.
10. **What are the values of `Schedule Creation Reason Code`?** Shared with
   [`asc-842.md`](asc-842.md#open-questions) — it is the field that would answer question 7 by
   inspection.
11. **Is the published `LiabilityTranslationAdjustment` formula correct?** As written it references the
   asset balance twice and never the liability balance. Confirm against a live FX-impact grid before
   coding.
12. **What is the PV-Based short-term-liability formula?** Vendor points to a help page not available
   offline. Read `Admin > Manage Company > Financial Settings`.
13. **Where does `Admin > Manage Company > Financial Settings` persist?** `Firm.JSONConfigText` is the
   only plausible column in the 18-field `Firm` object.
14. **What are the `Asset Suspension Status Code` values, and does the status affect the accounting
   schedule or only the physical asset record?**
15. **What is `SLPeriod.SLPeriodAllocations` (`sTYPE_TEXT`, `Functional Field = No`)?** Vendor says only
   *"Enter any straight line period allocations in this field"* — a free-text field in the middle of a
   calculated ledger.
16. **Are `Firm_LastDeferredSLEntry` / `Firm_LastDeferredSLEntryDate` / `Firm_LastDeferredSLTotal` on
    `Contract` (firm-scoped custom fields) a client-built ASC 840 carry-forward that must migrate?**
