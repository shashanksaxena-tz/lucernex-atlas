# SLPeriod

*79 fields · module: Lease Accounting & Payments · Postgres: `s_l_period`*

Period-level straight-line rent detail underlying SLSummary — one record per accounting period per contract carrying asset/liability balance, amortization expense, and both the current-currency and '- Translated' value pair for every monetary field, plus 12-Month Forward Change figures used for disclosure roll-forwards. 78 Global fields; where SLSummary is the fiscal-year rollup, SLPeriod is the period-by-period ledger that rollup is built from.

Source: `data-fields/sl-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 79 |
| Fields with a vendor definition | 76 of 79 inventoried |
| Physical tables | `s_l_period` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 78 (78 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 11 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in s_l_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 76 fields carry a vendor definition

**Observed.** 76 of this record's 79 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 4 of this record's fields required; the Data Fields catalogue marks 4; 4 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Equipment | The asset ID of the equipment associated with this period. | Equipment ID | Global |  | `s_l_period.AssetID · TEXT` | [Asset](Asset.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `s_l_period.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `s_l_period.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SLSummaryID` | Straight Line Summary | The ID of the lease accounting schedule associated with this period. | Straight-Line Schedule ID | Global | yes | `s_l_period.SLSummaryID · TEXT` | [SLSummary](SLSummary.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | This is a reporting field that returns data about the asset associated with the entity. | Entity | Global |  | `s_l_period.AssetAssociatedProjectEntityID · TEXT` |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeSLScheduleID` | Straight Line Schedule | This field displays the Straight Line Schedule ID. | Dropdown (Straight Line Schedule Type) | Global |  | `s_l_period.CodeSLScheduleID · TEXT` | Straight Line Schedule Type |

### Money (32)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAmortizationExpenseTranslated` | Asset Amortization Expense - Translated | The translated value of the Asset Amortization Expense column in your lease accounting schedule. | Currency | Global |  | `s_l_period.AssetAmortizationExpenseTranslated · TEXT` |  |
| `AssetAmount` | Asset Balance | This is the current value of the rented asset. The value of your asset is dependent upon whether you are calculating your lease as a Finance or Operating lease. In Report Builder currency conversions, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of the first accounting period. Please see the Accounting Schedule Calculations page in the Online Help for more information. | Currency | Global |  | `s_l_period.AssetAmount · TEXT` |  |
| `AssetAmountTranslated` | Asset Balance - Translated | The translated value of the Asset Balance column in your lease accounting schedule. | Currency | Global |  | `s_l_period.AssetAmountTranslated · TEXT` |  |
| `AssetTranslationAdjustment` | Asset Translation Adjustment | This field appears in the Fiscal Details grid when you calculate the FX Impact on the Rent Schedule page when a contract or equipment contract is marked as In Translation. The value of this field equals the current month's asset balance plus the current month's asset amortization expense minus the prior month's asset balance. (Asset Translation Adjustment = Current Asset Balance + Current Asset Amortization Expense - Prior Month's Asset Balance) | Currency | Global |  | `s_l_period.AssetTranslationAdjustment · TEXT` |  |
| `CashPaymentTranslated` | Cash Payment - Translated | The translated value of the Cash Expense column in your lease accounting schedule. | Currency | Global |  | `s_l_period.CashPaymentTranslated · TEXT` |  |
| `CumulativeAssetAmortExpense` | Accumulated Amortization Balance | For the first period of your schedule, this field's value is equal to the Asset Amortization Expense. For each subsequent period, this field's value is equal to the Asset Amortization Expense + the previous period s Accumulated Amortization Balance. | Currency | Global |  | `s_l_period.CumulativeAssetAmortExpense · TEXT` |  |
| `CumulativeDeferredBalance` | Cumulative Deferred Balance | The sum of the deferred rent from the beginning of the schedule to the current period in the straight line schedule. | Currency | Global |  | `s_l_period.CumulativeDeferredBalance · TEXT` |  |
| `CumulativeTranslationAdjustment` | Cumulative Translation Adjustment | This field appears in the Fiscal Details grid when you calculate the FX Impact on the Rent Schedule page when a contract or equipment contract is marked as In Translation. The value of this field is the current month's liability translation adjustment minus the current month's asset translation adjustment. (Cumulative Translation Adjustment = Current Month's Asset Translation Adjustment - Liability Translation Adjustment ) | Currency | Global |  | `s_l_period.CumulativeTranslationAdjustment · TEXT` |  |
| `FXGainLoss` | FX Gain (Loss) |  | Currency | Global |  | `s_l_period.FXGainLoss · TEXT` |  |
| `Forward12MonthAssetChange` | 12-Month Forward Change in Asset Balance | This is the sum of the asset amortization for the next 12 months. | Currency | Global |  | `s_l_period.Forward12MonthAssetChange · TEXT` |  |
| `Forward12MonthLiabilityAmortBased` | Short Term Liability (Amortization Based) | This is the 12-Month Forward Change in Liability Balance if you have selected Liability Amortization Based as your setting for the Short-Term/Long-Term Liability Calculation Method. | Currency | Global |  | `s_l_period.Forward12MonthLiabilityAmortBased · TEXT` |  |
| `Forward12MonthLiabilityChange` | 12-Month Forward Change in Liability Balance | This is the sum of the liability amortization for the next 12 months. | Currency | Global |  | `s_l_period.Forward12MonthLiabilityChange · TEXT` |  |
| `Forward12MonthLiabilityPVBased` | Short Term Liability (PV Based) | This is the 12-Month Forward Change in Liability Balance if you have selected PV Based as your setting for the Short-Term/Long-Term Liability Calculation Method. Please see the Lx Online Help > Toolbar > System Administrator Dashboard > Company Administration > Manage Company > Financial Settings page for the formula this setting uses. | Currency | Global |  | `s_l_period.Forward12MonthLiabilityPVBased · TEXT` |  |
| `GrossAssetBalance` | Gross Asset Balance | This field s value is equal to the Asset Balance + the Accumulated Amortization Balance. | Currency | Global |  | `s_l_period.GrossAssetBalance · TEXT` |  |
| `InitialAssetBalance` | Initial Asset Balance | This is a calculated value which contains the initial value over the asset of the lease. | Currency | Global |  | `s_l_period.InitialAssetBalance · TEXT` |  |
| `InitialLiabilityBalance` | Initial Liability Balance | This is the total of all of the Period Payment Present Values over the life of the lease. | Currency | Global |  | `s_l_period.InitialLiabilityBalance · TEXT` |  |
| `InterestTranslated` | Interest - Translated | The translated value of the Interest Expense column in your lease accounting schedule. | Currency | Global |  | `s_l_period.InterestTranslated · TEXT` |  |
| `LeaseLiabilityTranslated` | Lease Liability - Translated | The translated value of the Lease Liability column in your lease accounting schedule. | Currency | Global |  | `s_l_period.LeaseLiabilityTranslated · TEXT` |  |
| `LiabilityAmount` | Liability Balance | This is the current value of the liability. The value of your liability is dependent upon whether you are calculating your lease as a Finance or Operating lease. Please see the Accounting Schedule Calculations page in the Online Help for more information. In Report Builder currency conversions, this field will be converted according to the foreign exchange rate record appropriate for each accounting period. That is, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of that accounting period. | Currency | Global |  | `s_l_period.LiabilityAmount · TEXT` |  |
| `LiabilityFXImpact` | Liability FX Impact | This field allows you to report the foreign exchange liability impact. The calculation for this field is Period Liability FX Impact = (FX rate for this period - initial FX rate) * Period Liability Balance. | Currency | Global |  | `s_l_period.LiabilityFXImpact · TEXT` |  |
| `LiabilityTranslationAdjustment` | Liability Translation Adjustment | This field appears in the Fiscal Details grid when you calculate the FX Impact on the Rent Schedule page when a contract or equipment contract is marked as In Translation. The value of this field equals the current month's asset balance plus the difference between the current month's payment and interest, minus the prior month's asset balance. (Liability Translation Adjustment = Current Asset Balance + (Current Month's Payment - Current Month's Interest) - Prior Month's Asset Balance) | Currency | Global |  | `s_l_period.LiabilityTranslationAdjustment · TEXT` |  |
| `LongTermLiability` | Long Term Liability | The long-term liability is the current liability balance minus the short-term liability. | Currency | Global |  | `s_l_period.LongTermLiability · TEXT` |  |
| `LongTermRentExpense` | Long Term Rent Expense | The sum of all rent expenses beyond 12 months. | Currency | Global |  | `s_l_period.LongTermRentExpense · TEXT` |  |
| `PVOfPeriodCashAmount` | PV Of Period Cash Amount | The Present Value of a future cash payment in today's valuation. This value is discounted to present value from the period that the payment will be made. | Currency | Global |  | `s_l_period.PVOfPeriodCashAmount · TEXT` |  |
| `PeriodAssetAmortizationExpense` | Period Asset Amortization Expense | The amount that the asset value is reduced from one period to the next. In Report Builder currency conversions, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of the first accounting period. | Currency | Global |  | `s_l_period.PeriodAssetAmortizationExpense · TEXT` |  |
| `PeriodCashAmount` | Period Cash Amount | The amount of cash payments made during the period. | Currency | Global |  | `s_l_period.PeriodCashAmount · TEXT` |  |
| `PeriodDeferredAmount` | Period Deferred Amount | The difference between the period cash rent and straight line rent expense. | Currency | Global |  | `s_l_period.PeriodDeferredAmount · TEXT` |  |
| `PeriodExpenseAmount` | Period Expense Amount | The cash rent straight lined over the life of the schedule. | Currency | Global |  | `s_l_period.PeriodExpenseAmount · TEXT` |  |
| `PeriodInterestAmount` | Period Interest Amount | The interest owed on the liability based on the discount rate. | Currency | Global |  | `s_l_period.PeriodInterestAmount · TEXT` |  |
| `PeriodLiabilityAmortizationExpense` | Period Liability Amortization Expense | The amount that the liability value is reduced from one period to the next. In Report Builder currency conversions, this fields will be converted according to the foreign exchange rate record appropriate for each accounting period. That is, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of that accounting period. | Currency | Global |  | `s_l_period.PeriodLiabilityAmortizationExpense · TEXT` |  |
| `ScheduleCumulativeAmortExpense` | Schedule Asset Amortization |  | Currency | Global |  | `s_l_period.ScheduleCumulativeAmortExpense · TEXT` |  |
| `ShortTermRentExpense` | Short Term Rent Expense | The sum of all the rent expenses for the next 12 months. | Currency | Global |  | `s_l_period.ShortTermRentExpense · TEXT` |  |

### Quantities (7)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ConversionRateAverage` | Period Average Rate | The period average rate. | 5-Digit Number | Global |  | `s_l_period.ConversionRateAverage · TEXT` |  |
| `ConversionRateMonthEnd` | Cash Rate | The cash rate. | 5-Digit Number | Global |  | `s_l_period.ConversionRateMonthEnd · TEXT` |  |
| `CumulativePeriodNumber` | Cumulative Period Number | The current period number out of the total cumulative number of periods in the lease. | Number | Global |  | `s_l_period.CumulativePeriodNumber · TEXT` |  |
| `FiscalPeriod` | Fiscal Period | This is the period number for your fiscal year. There are normally 12 periods in a year, except if you use 13-period accounting. | Number | Global |  | `s_l_period.FiscalPeriod · TEXT` |  |
| `FiscalPeriodYear` | Fiscal Period Year | This is your fiscal year. | Number | Global |  | `s_l_period.FiscalPeriodYear · TEXT` |  |
| `NumberDays` | Number Days | The length of the period in days. | Number | Global |  | `s_l_period.NumberDays · TEXT` |  |
| `SLPeriodID` | Straight Line Period RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `s_l_period.SLPeriodID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `s_l_period.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `s_l_period.EndDate · TEXT` |  |
| `PostedDate` | Posted Date | The date that the Accounts Receivable transaction was posted. | Date | Global |  | `s_l_period.PostedDate · TEXT` |  |

### Text & notes (25)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExportAcct10Number` | Schedule Export Account #10 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct10Number · TEXT` |  |
| `ExportAcct11Number` | Schedule Export Account #11 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct11Number · TEXT` |  |
| `ExportAcct12Number` | Schedule Export Account #12 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct12Number · TEXT` |  |
| `ExportAcct13Number` | Schedule Export Account #13 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct13Number · TEXT` |  |
| `ExportAcct14Number` | Schedule Export Account #14 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct14Number · TEXT` |  |
| `ExportAcct15Number` | Schedule Export Account #15 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct15Number · TEXT` |  |
| `ExportAcct16Number` | Schedule Export Account #16 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct16Number · TEXT` |  |
| `ExportAcct17Number` | Schedule Export Account #17 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct17Number · TEXT` |  |
| `ExportAcct18Number` | Schedule Export Account #18 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct18Number · TEXT` |  |
| `ExportAcct19Number` | Schedule Export Account #19 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct19Number · TEXT` |  |
| `ExportAcct1Number` | Schedule Export Account #1 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct1Number · TEXT` |  |
| `ExportAcct20Number` | Schedule Export Account #20 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct20Number · TEXT` |  |
| `ExportAcct2Number` | Schedule Export Account #2 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct2Number · TEXT` |  |
| `ExportAcct3Number` | Schedule Export Account #3 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct3Number · TEXT` |  |
| `ExportAcct4Number` | Schedule Export Account #4 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct4Number · TEXT` |  |
| `ExportAcct5Number` | Schedule Export Account #5 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct5Number · TEXT` |  |
| `ExportAcct6Number` | Schedule Export Account #6 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct6Number · TEXT` |  |
| `ExportAcct7Number` | Schedule Export Account #7 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct7Number · TEXT` |  |
| `ExportAcct8Number` | Schedule Export Account #8 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct8Number · TEXT` |  |
| `ExportAcct9Number` | Schedule Export Account #9 | Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.ExportAcct9Number · TEXT` |  |
| `RecordStatus` | Record Status | This field displays the current status of the period--either posted, not posted, or mixed. | Text | Global | yes | `s_l_period.RecordStatus · TEXT` |  |
| `SLExportAcct1Number` | SL Schedule Export Account #1 | This field contains an export account number. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.SLExportAcct1Number · TEXT` |  |
| `SLExportAcct2Number` | SL Schedule Export Account #2 | This field contains an export account number. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.SLExportAcct2Number · TEXT` |  |
| `SLExportAcct3Number` | SL Schedule Export Account #3 | This field contains an export account number. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System. | Text | Global |  | `s_l_period.SLExportAcct3Number · TEXT` |  |
| `SLPeriodAllocations` | Allocations | Enter any straight line period allocations in this field. | Text | Global |  | `s_l_period.SLPeriodAllocations · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Straight Line Period ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `s_l_period.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `s_l_period.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `s_l_period.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `s_l_period.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `s_l_period.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `s_l_period.RevNumber · TEXT` |  |
