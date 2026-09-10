# Accounting engine — data model

**Stated up front.** Twenty objects carry the accounting engine. The spine is
`Contract → ContractFinancialTest → SLSummary → SLPeriod`: a contract has many classification tests
(only the locked ones count), many accounting schedules (only one active per standard), and each
schedule has one row per fiscal period. Every FK in this module is expressed in
`_lucernex_objects_summary.txt` as a *typed* column — `ContractID(Contract ID)`,
`SLSummaryID(Straight-Line Schedule ID)`, `AssetID(Equipment ID)` — not as a database constraint; in
the PostgreSQL export every one of them is a `TEXT` column carrying
`Key Role = Foreign key (ID reference)`, while the referenced primary keys are the only
`VARCHAR(64) NOT NULL` columns in the whole export.

## Object inventory

*Field counts: **Observed**. Left column from `_lucernex_objects_summary.txt`; right column from
`docs/data-fields/all-fields.csv` (the Manage Data Fields catalog). The two differ systematically:
the objects summary carries `ProjectEntityID` (the entity/tenant key) on every business object,
which the Data Fields catalog does not expose as a leaf; the code tables' generic
`ShortName`/`ActualLongName`/`Inactive` columns are likewise absent from the catalog.*

| Object | PG table(s) | Fields (object dump) | Fields (Data Fields catalog) | Role |
|---|---|---:|---:|---|
| `SLSummary` | `s_l_summary` | 134 | 135 | Accounting schedule header — one per standard per contract |
| `SLPeriod` | `s_l_period` | 79 | 78 | One row per fiscal period of a schedule |
| `ContractFinancialTest` | `contract_financial_test` | 93 | 92 | ASC 842 five-test classification + dual ASC 842/IFRS 16 measurement |
| `Contract` | `contract_admin`, `contract_financial`, `contract_firm`, `contract_firm1` | 570 | 441 | Owns the legacy Cap Lease Test, the engine action buttons, and denormalized SL balances |
| `Asset` | `asset` | 122 | 126 | Equipment-lease ROU asset; carries its own classification inputs and overrides |
| `AccrualTransaction` | `accrual_transaction` | 55 | 54 | Individual accrual posting with 8+16 GL account slots |
| `Covenant` | `covenant` | 44 | 44 | Source of Purchase Option / Cancellation Option / RVG amounts |
| `ExpenseAccrualSetup` | `expense_accrual_setup` | 31 | 30 | Accrual/forecast/plan configuration |
| `ExpenseAccrualSchedule` | `expense_accrual_schedule` | 31 | 30 | Generated period-by-period accrual amounts |
| `CodeExpenseType` | `code_expense_type` | 31 | 29 | **Routes each expense type to a schedule type per standard** |
| `AlternateRentSchedule` | `alternate_rent_schedule` | 25 | 24 | Alternate-rent overlay; carries the (dead) `SuspendSL` and the two hold flags |
| `CodeASC842Schedule` | `code_a_s_c842_schedule` | 24 | 21 | ASC 842 schedule type + 20 GL export account slots |
| `CodeIFRS16Schedule` | `code_i_f_r_s16_schedule` | 24 | 21 | IFRS 16 schedule type — structurally identical |
| `CodeSLSchedule` | `code_s_l_schedule` | 24 | 21 | Legacy straight-line schedule type — structurally identical |
| `AcctingAssumptionAdjust` | `accting_assumption_adjust` | 19 | 18 | Accounting-only payment overlay (does not create cash) |
| `FinancialAdjustment` | `financial_adjustment` | 19 | 18 | Manual RVG / purchase-option / cancellation-option adjustment |
| `FiscalPeriod` | `fiscal_period` | 17 | 16 | Fiscal calendar — 12- or 13-period, 4/5-week |
| `Program` (UI: **Portfolio**) | `program` | 180 | 85 | ⚠ **The portfolio-level accounting policy carrier** — discount rate, both ASC 842 thresholds, three amortisation-basis switches, two proration switches, fiscal year end, 14 FX rate-type selectors |
| `DiscountRate` | `discount_rate` | 16 | 16 | Portfolio/firm-scoped rate table keyed by country, use and term band |
| `RecalcOverrideNotes` | `recalc_override_notes` | 7 | 6 | Justification note attached to a recalculation override |

## Foreign-key edges

*All **Observed** from the typed FK columns in `_lucernex_objects_summary.txt`; the `Key Role` column
of `_xlsx_lucernex_jcrew.txt` independently confirms each as `Foreign key (ID reference)`.*

| From | Column (declared type) | To | Cardinality |
|---|---|---|---|
| `ContractFinancialTest` | `ContractID(Contract ID)` | `Contract` | N:1 |
| `ContractFinancialTest` | `AssetID(Equipment ID)` | `Asset` | N:1, nullable |
| `ContractFinancialTest` | `AssociatedDocumentID(Document ID)`, `FolderID(Folder ID)` | `Document`, `Folder` | N:1, nullable |
| `ContractFinancialTest` | `CodeASC842ScheduleID`, `CodeIFRS16ScheduleID` | `CodeASC842Schedule`, `CodeIFRS16Schedule` | N:1 |
| `ContractFinancialTest` | `CodeAccountingMethodID`, `CodeAcctMethodOverrideID` | Accounting Method code table | N:1 |
| `SLSummary` | `ContractID(Contract ID)` | `Contract` | N:1 |
| `SLSummary` | `AssetID(Equipment ID)` | `Asset` | N:1, nullable |
| `SLSummary` | `CodeASC842ScheduleID` / `CodeIFRS16ScheduleID` / `CodeSLScheduleID` | the three schedule-type code tables | N:1 each |
| `SLSummary` | `CodeAccountingMethodID` | Accounting Method code table | N:1 |
| `SLSummary` | `CodeScheduleCreationReasonID` | Schedule Creation Reason code table | N:1 |
| `SLSummary` | `PriorLastPostedPeriodID(Number)` | prior `SLSummary` | N:1 — **schedule-version chain** |
| `SLSummary` | `RecalcOverrideNotesIDList(Recalc Override Notes ID)` | `RecalcOverrideNotes` | 1:N (list-in-column) |
| `SLSummary` | `AssociatedExpenseSetupIDs(Text)` | `ExpenseSetup` | 1:N (list-in-column, **not typed as an FK**) |
| `SLPeriod` | `SLSummaryID(Straight-Line Schedule ID)` | `SLSummary` | N:1 |
| `SLPeriod` | `ContractID`, `AssetID`, `CodeSLScheduleID` | as above | N:1 |
| `RecalcOverrideNotes` | `SLSummaryID(Straight-Line Schedule ID)` | `SLSummary` | N:1 |
| `AcctingAssumptionAdjust` | `ContractID`, `ExpenseSetupID(Expense Setup ID)` | `Contract`, `ExpenseSetup` | N:1 |
| `AcctingAssumptionAdjust` | `CodeASC842ScheduleID`, `CodeIFRS16ScheduleID`, `CodeFrequencyID`, `CodeProrationMethodID` | code tables | N:1 |
| `FinancialAdjustment` | `ContractID`, `AssetID`, `CovenantID(Covenant ID)` | `Contract`, `Asset`, `Covenant` | N:1 |
| `Covenant` | `ContractID`, `AmendmentID(Contract Amendment ID)` | `Contract`, `ContractAmendment` | N:1 |
| `Covenant` | `CodeASC842ScheduleID`, `CodeIFRS16ScheduleID`, `CodeAccountingAdjustmentTypeID` | code tables | N:1 |
| `CodeExpenseType` | `CodeASC842ScheduleID`, `CodeIFRS16ScheduleID`, `CodeSLScheduleID` | the three schedule-type code tables | N:1 each |
| `CodeExpenseType` | `ParentCodeExpenseGroupID`, `ParentID` | Expense Group code table | N:1 |
| `ExpenseAccrualSetup` | `ContractID`, `ExpenseSetupID`, `CovenantID`, `AmendmentID` | as above | N:1 |
| `ExpenseAccrualSchedule` | `ExpenseAccrualSetupID(Text)` | `ExpenseAccrualSetup` | N:1 — **declared as `Text`, not as an FK type** |
| `AccrualTransaction` | `ContractID`, `ExpenseAccrualSetupID(Text)`, `OrganizationID(Organization ID)` | as above | N:1 |
| `AlternateRentSchedule` | `ContractID`, `ExpenseSetupID`, `CodeSalesGroupID` | as above | N:1 |
| `Asset` | `FinancialContractID(Contract ID)` | `Contract` (the *equipment* contract) | N:1 |
| `DiscountRate` | `ProgramID(Portfolio ID)`, `CountryID`, `CountryIDList`, `StateProvinceIDList`, `CodeContractUseID`, `CodeAccountingMethodID` | scoping keys | N:1 |
| `FiscalPeriod` | `ProgramID(Portfolio ID)` | `Program` (Portfolio) | N:1 |
| `Contract` | `ProgramID(Portfolio ID)` | `Program` (Portfolio) | N:1 — the edge that carries every policy default in `ACC-R-056`…`059` down to a schedule |
| every object | `ProjectEntityID(Entity ID)` | `ProjectEntity` | N:1 — the entity/tenant discriminator |

### Two FKs that are not typed as FKs

`ExpenseAccrualSchedule.ExpenseAccrualSetupID` and `AccrualTransaction.ExpenseAccrualSetupID` are
declared `Text` in the object dump, while every other parent reference in the module carries a typed
FK (`Contract ID`, `Covenant ID`, …). `SLSummary.AssociatedExpenseSetupIDs` is likewise plain `Text`
and holds a *list*. **Derived**: these three are join keys that Lucernex chose not to model as
references, and a rebuild that adds real FK constraints there will surface orphan rows during
migration. Confirm the actual cardinality in the live data before enforcing.

## Where each field group physically lives on `Contract`

`Contract` is split across four PostgreSQL tables. The accounting-relevant split is
**Observed** in `_xlsx_lucernex_jcrew.txt`:

| PG table | Accounting content |
|---|---|
| `contract_admin` | The **legacy Cap Lease Test** (`Test1Result`…`Test5bResult`, `FinalResult`, `FMVOfBuilding`, `FMVOfLand`, `FMVSource`, `RemainingLife`, `YearBuilt`, `DoesTitleRevertToTenant`, `ContainsBargainPurchaseOption`, the four dead `Ratio*` fields, the four dead `*Renewal*` fields), `CommenceDate`, `ExpireDate`, `TermLength`, `LatestFinancialTestFinalResult`, `CurrentStraightLineAssetBalance`, `CurrentStraightLineLiabilityBalance`, `IsShortTerm`, `IsLowAssetValue`, `MonthToMonth`, `IsTranslation` |
| `contract_financial` | `DiscountRate`, `ComputedSLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `AggregateNNNBaseRentNPV`, `BaseYearOperatingExpenses`, `BaseYearOtherExpenses`, `BaseYearRETax`, `LeasedLandArea`, `ProjectLandArea`, `InAlternateRent`, and the whole Financial-Calendar / Financial-Fiscal rent-rollup block |
| `contract_firm`, `contract_firm1` | Firm-scoped custom fields, including `Firm_LastDeferredSLEntry`, `Firm_LastDeferredSLEntryDate`, `Firm_LastDeferredSLTotal` — a tenant-built ASC 840 deferred-rent carry-forward, **not** a platform field |

## The `SLSummary` field blocks

`SLSummary`'s 134 fields fall into five named UI subgroups, **Observed** in the
`Notes (Group / Subgroup)` column of `docs/data-fields/sl-summary.md`:

| Subgroup | Count | Content |
|---|---:|---|
| `Contract / Straight Line Summary` | ~110 | The schedule header proper: dates, discount rate, the initial/current asset and liability balances, all PV components, the modification/remeasurement deltas, the recalculation flags |
| `Contract / Roll Forward Report` | 25 | The ASC 842/IFRS 16 roll-forward disclosure: prior-period balances, new leases, remeasurement impacts, reclassification impacts, lease-expiration impacts, ending balances |
| `Contract / Financial - Rent Schedule` | 14 | The maturity-analysis disclosure: cash expense by fiscal year (current, next, 3rd–6th, beyond 5th, beyond 6th) and by quarter within the current fiscal year |

*The remaining fields are audit/system columns.*

## The `SLPeriod` row shape

A `SLPeriod` row is the atomic accounting output. **Observed** field composition:

| Block | Fields |
|---|---|
| Period identity | `SLPeriodID`, `SLSummaryID`, `ContractID`, `AssetID`, `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber`, `RecordStatus`, `PostedDate` |
| Cash | `PeriodCashAmount`, `PVOfPeriodCashAmount` |
| Expense | `PeriodExpenseAmount` (the straight-lined figure), `PeriodInterestAmount`, `PeriodAssetAmortizationExpense`, `PeriodLiabilityAmortizationExpense`, `PeriodDeferredAmount` |
| Balances | `AssetAmount`, `LiabilityAmount`, `GrossAssetBalance`, `CumulativeAssetAmortExpense`, `CumulativeDeferredBalance`, `ScheduleCumulativeAmortExpense`, `InitialAssetBalance`, `InitialLiabilityBalance` |
| Short/long split | `ShortTermRentExpense`, `LongTermRentExpense`, `LongTermLiability`, `Forward12MonthAssetChange`, `Forward12MonthLiabilityChange`, `Forward12MonthLiabilityAmortBased`, `Forward12MonthLiabilityPVBased` |
| FX | `ConversionRateAverage`, `ConversionRateMonthEnd`, `AssetAmountTranslated`, `LeaseLiabilityTranslated`, `InterestTranslated`, `CashPaymentTranslated`, `AssetAmortizationExpenseTranslated`, `AssetTranslationAdjustment`, `LiabilityTranslationAdjustment`, `CumulativeTranslationAdjustment`, `LiabilityFXImpact`, `FXGainLoss` |
| GL export | `ExportAcct1Number`…`ExportAcct20Number`, `SLExportAcct1Number`…`SLExportAcct3Number`, `SLPeriodAllocations` |
| Audit | `CreatedByID`, `CreatedDate`, `ModifiedByID`, `ModifiedDate`, `RevNumber`, `BOMapClientRecordID`, `ProjectEntityID` |

**Derived**: 23 of the 79 fields (29%) exist only to serve currency translation, and a further 23 only
to carry GL account numbers copied down from the schedule type. The genuinely accounting-bearing
payload of a period row is roughly **21 numbers**.

## Code tables the engine depends on

*All **Observed** as `Dropdown (…)` bindings in `_lucernex_objects_summary.txt`. The **values** of
these tables are not in any offline artifact — see [`rules.md`](rules.md) open questions.*

Each is registered in the platform's single code-table registry under a numeric `TableType`; the
IDs below are **Observed** in `docs/data-model/code-table-registry.md`.

| Code table | `TableType` | Referenced by | Known values |
|---|---:|---|---|
| Accounting Method Code | **not in the registry** | `SLSummary`, `ContractFinancialTest` (×2), `Asset`, `DiscountRate` | `Operating`, `Finance` — **Observed** in the vendor definition of `ContractFinancialTest.CodeAccountingMethodID`: *"Select whether you want to calculate your schedule as an Operating schedule or a Finance schedule"* |
| **ASC 842 Schedule Type** | **2162** | `SLSummary`, `ContractFinancialTest`, `AcctingAssumptionAdjust`, `Covenant`, `CodeExpenseType` | ⚠ **exactly one row in this tenant: `842 Rent`** — **Observed**, 2026-09-10 |
| **IFRS 16 Schedule Type** | **2163** | same five | ⚠ **empty — "No rows to display"** — **Observed**, 2026-09-10 |
| **Straight Line Schedule Type** | **2161** | `SLSummary`, `SLPeriod`, `CodeExpenseType` | ⚠ **empty — "No rows to display"** — **Observed**, 2026-09-10 |
| Schedule Creation Reason Code | **2160** | `SLSummary` only | **unknown** — the single most important missing enumeration in this module. It *is* a Firm Drop Down, so it is readable at `FirmCodeEdit.jsp?TableType=2160` |
| Accounting Adjustment Type Code | **not in the registry** | `Covenant`, `FinancialAdjustment` | `Cancellation Option`, `Residual Value Guarantee`, `Purchase Option` — **Observed** in the vendor definition of `FinancialAdjustment.CodeAccountingAdjustmentTypeID` |
| Financial Adjustment Status Code | **2109** | `FinancialAdjustment` | **unknown** — readable at `FirmCodeEdit.jsp?TableType=2109` |
| Accrual Type Code | **not in the registry** | `ExpenseAccrualSetup` | `accrual`, `forecast`, `plan` — **Observed** in the vendor definition of `ExpenseAccrualSetup.CodeAccrualTypeID` |
| Proration Method Code | **not in the registry** | `AcctingAssumptionAdjust`, `ExpenseSetup` | **unknown**; vendor definition: *"tells the system how much a 'day' is worth, when your cost period does not encompass the entirety of the period"* |
| Asset Type Test Code | **2085** | `ContractFinancialTest` | **dead** — vendor definition: *"This field is no longer in use."* |
| Frequency Code | **not in the registry** | `AcctingAssumptionAdjust`, `Asset` (compounding) | **unknown** |
| Frequency Unit Code | **not in the registry** | `ContractFinancialTest`, `Asset` (remaining-life unit) | weeks / months / years — **Observed** in the vendor definition of `ContractFinancialTest.CodeRemainingLifeFreqUnitID` |
| Asset Suspension Status Code | **2005** | `Asset` | **unknown** — readable at `FirmCodeEdit.jsp?TableType=2005` — the only field in the module whose name suggests accounting suspension |
| Expense Type Code | **3013** | `ExpenseSetup`, `ExpenseAccrualSetup`, `AccrualTransaction` | tenant-defined; **this is the routing table** (`ACC-R-025`) |

*`TableType` IDs are **Observed** from the 207-table registry in
`docs/data-model/code-table-registry.md`.*

**A negative result worth recording.** Six code tables this module depends on are **not among the 207
Firm Drop Downs**: Accounting Method, Accounting Adjustment Type, Accrual Type, Proration Method,
Frequency, and Frequency Unit. The same is true of `Work Flow Status Code`, checked because the
approval rules `ACC-R-060`…`062` could plausibly have depended on it — **they do not**; their
`Member` / `Job Title` / `Ad Hoc` vocabulary comes from the workflow-step screen, not a code table.

**Inferred:** the six are platform-internal enumerations that a tenant cannot edit, which is
consistent with their values being fixed by accounting semantics rather than by configuration —
`Operating` and `Finance` are not things a customer gets to redefine. If so, they should be
**hard-coded enums in ASG Edge+, not Masters rows**, and that is a different build decision from the
tenant-editable schedule types. Confirm before the Masters model is sized.

### ⚠ The tenant runs ASC 842 only, through one schedule type

**Observed**, 2026-09-10, `FirmCodeEdit.jsp`:

| `TableType` | Code table | Rows |
|---:|---|---|
| 2162 | ASC 842 Schedule Type Code | **1** — `842 Rent` (`Don't Amortize Asset Value` = no, `Inactive` = no) |
| 2161 | Straight Line Schedule Type Code | **0** — "No rows to display" |
| 2163 | IFRS 16 Schedule Type Code | **0** — "No rows to display" |

All three render the same four columns — `Type*`, `Description`, `Don't Amortize Asset Value`,
`Inactive` — confirming from the UI what the schema dump already showed: the three tables are
structurally identical and differ only in which foreign key points at them.

Four consequences run through the rest of this folder:

1. **There is exactly one set of twenty GL export slots in play today**, not a matrix. The
   `ExportAcctNNumber` mapping question shrinks from "which slot means what, per schedule type" to
   one row to read.
2. **`DontAmortizeAssetValue` is unchecked on the only configured row**, so `ACC-R-030` — the one
   rule in this module resting on a field name alone — is **inert in production**. It cannot be
   observed behaving, and it cannot be validated against this tenant's data.
3. **`CodeExpenseType.CodeSLScheduleID` and `.CodeIFRS16ScheduleID` must be null everywhere**, since
   there is nothing for them to point at. Every cash flow routes to ASC 842 (`ACC-R-025`).
4. **`SLSummary.IsSLSchedule` and `.IsIFRS16Schedule` should be false on every row.** Worth
   verifying — a true value would mean a schedule exists whose schedule type has since been deleted.

### The 2000/3000 `TableType` band hypothesis — refuted

`docs/data-model/code-table-registry.md` proposes (**Derived**) that the registry's two ID bands are
semantic: 2000–2190 plain lookups, 3000–3016 behaviour-bearing. Checking that against the eleven
`Code*` objects the schema dump actually contains **refutes it**:

| Object | `TableType` | Band | Fields | Carries behaviour beyond name/description/inactive? |
|---|---:|---|---:|---|
| `CodeASC842Schedule` | 2162 | 2000 | 24 | **Yes** — `DontAmortizeAssetValue` + 20 GL account slots |
| `CodeIFRS16Schedule` | 2163 | 2000 | 24 | **Yes** — identical |
| `CodeSLSchedule` | 2161 | 2000 | 24 | **Yes** — identical |
| `CodeIssueType` | 2035 | 2000 | 19 | **Yes** — 11 `IsValidFor*` attachability booleans, `IsWorkFlow`, `SequencePrefix`, `IsSequencePerFirm`, `AutoClose`, `AllowReply` |
| `CodeAssetCategory` | 2047 | 2000 | 6 | **Yes** — `GLNumber`, `SubAccount`, `DNEAmount` |
| `CodeResponsibleParty` | 2058 | 2000 | 4 | **Yes** — carries an FK to another code table |
| `CodeExpenseType` | **3013** | **3000** | 31 | **Yes** — the three schedule-routing FKs + 16 GL account slots |
| `CodeProblem` | **3001** | **3000** | 4 | Barely — one `RemedyNote` text column |
| `CodeSalesType` | **3012** | **3000** | 3 | **No** — `ShortName`, `ActualLongName`, `Inactive`. A plain lookup. |
| `CodeSalesGroup` | 2144 | 2000 | 3 | **No** — plain lookup |
| `CodeBudgetColumnStatus` | — | — | 3 | **No** — plain lookup |

Of the three 3000-band tables that have an object in the dump, **only `Expense Type` (3013) supports
the hypothesis**; `Sales Type` (3012) is a bare three-column lookup and `Problem` (3001) is close to
one. Meanwhile the four most behaviour-bearing code tables in this module — the three schedule types
and `Issue Type` — are all in the 2000 band.

**Derived: the band is a registration-order artefact, not a classification.** Behaviour-bearing-ness
has to be read from each table's object, not from its ID. That matters for MDM-01 sizing: the
"which code tables need more than `(code, label, active)`" question cannot be answered by an ID
range, and at least six 2000-band tables need the richer model.

## `Program` — the portfolio-level policy carrier

*Added 2026-09-10. Round one of this document missed `Program` entirely, treating `ProgramID` only as
a scoping key on `DiscountRate` and `FiscalPeriod`. It is in fact where most of the accounting
engine's tenant policy lives. All **Observed** from vendor definitions in `_xlsx_lucernex_jcrew.txt`.*

| Field | Type | Governs | Rule |
|---|---|---|---|
| `SLDiscountRate` | `sTYPE_PERCENTAGE` | The default IBR. ⚠ Entry convention: *"enter the number no % or decimal is necessary"* — `5` means 5% | `ACC-R-001` |
| `FairValueThreshold` | `sTYPE_PERCENTAGE` | ASC 842 Test 4 threshold, *"usually set to 90%"*; *"This field is used in the ASC 842 Test."* | `ACC-R-009` |
| `RemainingEconomicLifeThreshold` | `sTYPE_PERCENTAGE` | ASC 842 Test 3 threshold, *"usually set to 75%"*; *"This field is used in the ASC 842 Test."* | `ACC-R-007` |
| `SLAssetAmortizeMethod` | `sTYPE_TEXT` | Asset amortisation basis — Per Day or Per Period. *"This setting impacts only ASC 842 Finance leases."* | `ACC-R-056` |
| `SLCashAmortizeMethod` | `sTYPE_TEXT` | Cash-rent amortisation basis | `ACC-R-056` |
| `SLExpenseAmortizeMethod` | `sTYPE_TEXT` | Rent-expense amortisation basis | `ACC-R-056` |
| `SLProrate35As28` | `Boolean` | Prorate partial first/last periods on a 28-day multiplier; ≥ 28 days counts as a whole period | `ACC-R-057` |
| `SLMatchYearEnds` | `Boolean` | *"if the program allows for matching of fiscal/calendar year rent"* | `ACC-R-058` |
| `FiscalYearEnd` | `Date` | Month and day the fiscal year ends — the anchor for `FiscalPeriod` | `ACC-R-028` |
| `CodeAssetAmortFXTypeID` / `…SubFXTypeID` | `sCODE_EXCHANGE_RATE_TYPE` ×2 | FX rate type for asset amortisation, revaluation / translation | `ACC-R-059` |
| `CodeAssetBalFXTypeID` / `…SubFXTypeID` | ×2 | asset balance | `ACC-R-059` |
| `CodeLiabAmortFXTypeID` / `…SubFXTypeID` | ×2 | liability amortisation | `ACC-R-059` |
| `CodeLiabilityBalFXTypeID` / `…SubFXTypeID` | ×2 | liability balance | `ACC-R-059` |
| `CodeCashExpensesFXTypeID` / `…SubFXTypeID` | ×2 | cash expenses | `ACC-R-059` |
| `CodeInterestFXTypeID` / `…SubFXTypeID` | ×2 | interest | `ACC-R-059` |
| `CodeSingleLeaseFXTypeID` / `…SubFXTypeID` | ×2 | single lease expense | `ACC-R-059` |

**Derived**: the three-tier resolution for every one of these is Contract → Portfolio → Firm. The
contract-level twins (`Contract.FairValueThreshold`, `Contract.RemainingEconomicLifeThreshold`,
`Contract.ComputedSLDiscountRate`) are all typed `COMPUTED` precisely because they *resolve* this
chain rather than store a value — which is why their vendor definitions read *"This field computes
the default … The system uses the portfolio-level value if one exists, otherwise it uses the
Firm-level value."*

**Rebuild note**: this is the natural home for the ASG Edge+ **Rule Administration UI** parameters —
the Accounting Engine BRD §12 wants exactly these values versioned, effective-dated and four-eyes
approved. Lucernex has them as bare, unversioned columns on the Portfolio.

## Firm-level settings that are not in the object model

Two engine-level behaviours are configured at `Admin > Manage Company > Financial Settings`, which is
**not** exposed as an object in the 223-object dump. (Everything in the section above *is* in the
object model, on `Program` — these two are the residue that is not.) `Firm` itself carries only 18 fields, of which
`JSONConfigText(Text)` is the plausible carrier.

| Setting | Effect | Evidence |
|---|---|---|
| **Short-Term/Long-Term Liability Calculation Method** — `Liability Amortization Based` or `PV Based` | Chooses whether `SLPeriod.Forward12MonthLiabilityAmortBased` or `SLPeriod.Forward12MonthLiabilityPVBased` is the reported short-term liability | **Observed**, vendor definitions of both fields |
| **Translation vs. Revaluation FX mapping** | `Contract.IsTranslation = true` ⇒ use the Translation mapping; false ⇒ the Revaluation mapping | **Observed**, vendor definition of `Contract.IsTranslation` |

Both must be captured somewhere in ASG Edge+; neither has a home in the Lucernex schema you can copy.
