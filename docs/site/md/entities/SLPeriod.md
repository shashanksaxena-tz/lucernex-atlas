# SLPeriod

*79 fields · module: Lease Accounting & Payments · Postgres: `s_l_period`*

Period-level straight-line rent detail underlying SLSummary — one record per accounting period per contract carrying asset/liability balance, amortization expense, and both the current-currency and '- Translated' value pair for every monetary field, plus 12-Month Forward Change figures used for disclosure roll-forwards. 78 Global fields; where SLSummary is the fiscal-year rollup, SLPeriod is the period-by-period ledger that rollup is built from.

Source: `data-fields/sl-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 79 |
| Catalogued fields | 78 (78 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 11 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-025](../rules/ACC-R-025.md) | each period cash flow is routed to the schedule type its expense type designates for the standard being generated | Derived |
| [ACC-R-028](../rules/ACC-R-028.md) | one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber` | Derived |
| [ACC-R-029](../rules/ACC-R-029.md) | copied verbatim onto `SLPeriod.ExportAcct1Number` … `ExportAcct20Number` | Derived |
| [ACC-R-030](../rules/ACC-R-030.md) | if true, no asset amortization is recognised for schedules of this type | Inferred |
| [ACC-R-031](../rules/ACC-R-031.md) | `InitialLiabilityBalance = Σ PVOfPeriodCashAmount` | Observed |
| [ACC-R-032](../rules/ACC-R-032.md) | discount the cash payment from the period it is made back to the accounting begin date | Observed |
| [ACC-R-036](../rules/ACC-R-036.md) | `CurrentRemainingCashBalance` = sum of current and future remaining lease payments; `CurrentRemainingCashBalanceAfterReportEnd` = the same excluding the current period | Observed |
| [ACC-R-041](../rules/ACC-R-041.md) | ``` Forward12MonthAssetChange[n] = Σ asset amortization, periods n+1 … n+12 Forward12MonthLiabilityChange[n] = Σ liability amortization, periods n+1 … n+12 ShortTermRentExpense[n] = Σ rent expense, next 12 months LongTermRentExpense[n] = Σ  | Observed |
| [ACC-R-051](../rules/ACC-R-051.md) | `SLSummary.LastPostedDate` = begin date of the last posted period; `LastPostedEndDate` = its end date; `LastBalancePosted` = "the asset minus the liability as of the last posted period"; `LastPostedBalanceSheetImpact` = "the portion of the  | Observed |
| [ACC-R-056](../rules/ACC-R-056.md) | - `PER_PERIOD` ⇒ "distributes the amortization equally among periods"; - `PER_DAY` ⇒ "distributes the amortization according to the number of days in the period", i.e. weight each period by `SLPeriod.NumberDays` | Observed |
| [ACC-R-059](../rules/ACC-R-059.md) | the `Sub` variant applies to "contracts in need of translation", the plain variant to "contracts in need of revaluation" — selected per contract by `Contract.IsTranslation` (`ACC-R-044`) | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetID` | Equipment | Equipment ID | Global |  | [Asset](Asset.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `SLSummaryID` | Straight Line Summary | Straight-Line Schedule ID | Global | yes | [SLSummary](SLSummary.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | Entity | Global |  |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeSLScheduleID` | Straight Line Schedule | Dropdown (Straight Line Schedule Type) | Global |  | Straight Line Schedule Type |

### Money (32)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetAmortizationExpenseTranslated` | Asset Amortization Expense - Translated | Currency | Global |  |  |
| `AssetAmount` | Asset Balance | Currency | Global |  |  |
| `AssetAmountTranslated` | Asset Balance - Translated | Currency | Global |  |  |
| `AssetTranslationAdjustment` | Asset Translation Adjustment | Currency | Global |  |  |
| `CashPaymentTranslated` | Cash Payment - Translated | Currency | Global |  |  |
| `CumulativeAssetAmortExpense` | Accumulated Amortization Balance | Currency | Global |  |  |
| `CumulativeDeferredBalance` | Cumulative Deferred Balance | Currency | Global |  |  |
| `CumulativeTranslationAdjustment` | Cumulative Translation Adjustment | Currency | Global |  |  |
| `FXGainLoss` | FX Gain (Loss) | Currency | Global |  |  |
| `Forward12MonthAssetChange` | 12-Month Forward Change in Asset Balance | Currency | Global |  |  |
| `Forward12MonthLiabilityAmortBased` | Short Term Liability (Amortization Based) | Currency | Global |  |  |
| `Forward12MonthLiabilityChange` | 12-Month Forward Change in Liability Balance | Currency | Global |  |  |
| `Forward12MonthLiabilityPVBased` | Short Term Liability (PV Based) | Currency | Global |  |  |
| `GrossAssetBalance` | Gross Asset Balance | Currency | Global |  |  |
| `InitialAssetBalance` | Initial Asset Balance | Currency | Global |  |  |
| `InitialLiabilityBalance` | Initial Liability Balance | Currency | Global |  |  |
| `InterestTranslated` | Interest - Translated | Currency | Global |  |  |
| `LeaseLiabilityTranslated` | Lease Liability - Translated | Currency | Global |  |  |
| `LiabilityAmount` | Liability Balance | Currency | Global |  |  |
| `LiabilityFXImpact` | Liability FX Impact | Currency | Global |  |  |
| `LiabilityTranslationAdjustment` | Liability Translation Adjustment | Currency | Global |  |  |
| `LongTermLiability` | Long Term Liability | Currency | Global |  |  |
| `LongTermRentExpense` | Long Term Rent Expense | Currency | Global |  |  |
| `PVOfPeriodCashAmount` | PV Of Period Cash Amount | Currency | Global |  |  |
| `PeriodAssetAmortizationExpense` | Period Asset Amortization Expense | Currency | Global |  |  |
| `PeriodCashAmount` | Period Cash Amount | Currency | Global |  |  |
| `PeriodDeferredAmount` | Period Deferred Amount | Currency | Global |  |  |
| `PeriodExpenseAmount` | Period Expense Amount | Currency | Global |  |  |
| `PeriodInterestAmount` | Period Interest Amount | Currency | Global |  |  |
| `PeriodLiabilityAmortizationExpense` | Period Liability Amortization Expense | Currency | Global |  |  |
| `ScheduleCumulativeAmortExpense` | Schedule Asset Amortization | Currency | Global |  |  |
| `ShortTermRentExpense` | Short Term Rent Expense | Currency | Global |  |  |

### Quantities (7)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ConversionRateAverage` | Period Average Rate | 5-Digit Number | Global |  |  |
| `ConversionRateMonthEnd` | Cash Rate | 5-Digit Number | Global |  |  |
| `CumulativePeriodNumber` | Cumulative Period Number | Number | Global |  |  |
| `FiscalPeriod` | Fiscal Period | Number | Global |  |  |
| `FiscalPeriodYear` | Fiscal Period Year | Number | Global |  |  |
| `NumberDays` | Number Days | Number | Global |  |  |
| `SLPeriodID` | Straight Line Period RecID | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `PostedDate` | Posted Date | Date | Global |  |  |

### Text & notes (25)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExportAcct10Number` | Schedule Export Account #10 | Text | Global |  |  |
| `ExportAcct11Number` | Schedule Export Account #11 | Text | Global |  |  |
| `ExportAcct12Number` | Schedule Export Account #12 | Text | Global |  |  |
| `ExportAcct13Number` | Schedule Export Account #13 | Text | Global |  |  |
| `ExportAcct14Number` | Schedule Export Account #14 | Text | Global |  |  |
| `ExportAcct15Number` | Schedule Export Account #15 | Text | Global |  |  |
| `ExportAcct16Number` | Schedule Export Account #16 | Text | Global |  |  |
| `ExportAcct17Number` | Schedule Export Account #17 | Text | Global |  |  |
| `ExportAcct18Number` | Schedule Export Account #18 | Text | Global |  |  |
| `ExportAcct19Number` | Schedule Export Account #19 | Text | Global |  |  |
| `ExportAcct1Number` | Schedule Export Account #1 | Text | Global |  |  |
| `ExportAcct20Number` | Schedule Export Account #20 | Text | Global |  |  |
| `ExportAcct2Number` | Schedule Export Account #2 | Text | Global |  |  |
| `ExportAcct3Number` | Schedule Export Account #3 | Text | Global |  |  |
| `ExportAcct4Number` | Schedule Export Account #4 | Text | Global |  |  |
| `ExportAcct5Number` | Schedule Export Account #5 | Text | Global |  |  |
| `ExportAcct6Number` | Schedule Export Account #6 | Text | Global |  |  |
| `ExportAcct7Number` | Schedule Export Account #7 | Text | Global |  |  |
| `ExportAcct8Number` | Schedule Export Account #8 | Text | Global |  |  |
| `ExportAcct9Number` | Schedule Export Account #9 | Text | Global |  |  |
| `RecordStatus` | Record Status | Text | Global | yes |  |
| `SLExportAcct1Number` | SL Schedule Export Account #1 | Text | Global |  |  |
| `SLExportAcct2Number` | SL Schedule Export Account #2 | Text | Global |  |  |
| `SLExportAcct3Number` | SL Schedule Export Account #3 | Text | Global |  |  |
| `SLPeriodAllocations` | Allocations | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Straight Line Period ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
