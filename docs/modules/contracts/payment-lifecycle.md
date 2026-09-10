# The payment lifecycle

**Stated up front.** `PaymentTransaction` is not a payment record. It is the platform's **single
money-movement ledger** — payable and receivable, rent and recovery and tax and percentage rent —
tenanted by `ProjectEntityID`, keyed by `ContractID`, and typed by `SourceEntityTable` +
`CodeSourceEntityID`. It carries **four independent date axes**, **five state booleans**, **five
different provenance FKs**, and **twenty GL account-number slots**. That last group is a hard
integration contract: `AccountNumber1..8` plus four families of four accrual accounts each are
copied onto every posted row from `CodeExpenseType`, snapshotted at posting time, and exported in
batches identified by `ExportBatchNumber`.

The lifecycle in one line:

```
ExpenseSetup ─▶ ExpenseSchedule ─▶ PaymentTransaction ─▶ [AP export] ─▶ CheckNumber/CheckDate
                                          ▲                                      │
      LandlordInvoice ─▶ LandlordInvoiceItem ─┘ (LinkLandlordInvPaymentTxn)       │
                                          ▼                                      ▼
                                   PaymentReceipt (inbound)              AccrualTransaction (GL accrual)
```

All field names and types **Observed** from `_lucernex_objects_summary.txt`; labels **Observed**
from `docs/data-fields/payment-transaction.md`, `payment-receipt.md`, `landlord-invoice.md`,
`landlord-invoice-item.md`.

---

## 1. `ExpenseSchedule` → `PaymentTransaction`

### The generation gate

`ExpenseSchedule` (51 fields) holds four state fields that together gate generation:

| Field | Role |
|---|---|
| `ReadyForPaymentFlag(Boolean)` | Approved to generate |
| `CodeApprovalStatusID` + `LastApprovalChangeDate` | Workflow status |
| `HoldFlag(Boolean)` | Suppressed |
| `ProcessedFlag(Boolean)` + `ProcessedDate(Date)` | Already generated — the idempotence guard |

`ExpenseSetup` carries the same `ReadyForPaymentFlag` and `HoldFlag` at the clause level, so both
gates must pass. **Observed.**

### What the schedule row carries into the transaction

| `ExpenseSchedule` field | Becomes / drives |
|---|---|
| `PaymentAmount`, `AnnualAmount`, `PaymentRate` | `PaymentTransaction.TotalAmount` |
| `DailyRentRate` (with `ExpenseSetup.IsDailyRent`) | Per-diem proration for stub periods |
| `FirstPaymentAmount` / `LastPaymentAmount` | The stub amounts at each end |
| `TaxAmount1..4`, `CalculatedTaxAmount1..4`, `CalculatedTaxRate1..4` | `PaymentTransaction.TaxAmount1..4` |
| `BeginDate` / `EndDate` | `CoverageBeginDate` / `CoverageEndDate` |
| `AccountPeriod` / `AccountYear` | `PostingDate` resolution |
| `ContractTermID` | Which option term this belongs to |
| `AssetID` / `AssetAssociatedProjectEntityID` | Equipment-contract rent |
| `OptionRentFlag(Boolean)` | This step is inside an option period |
| `IsCPI(Boolean)` | This step was index-driven |

`ExpenseSchedule` has **two** tax representations: `TaxAmount1..4` and `CalculatedTaxAmount1..4`
plus `CalculatedTaxRate1..4`. Reading: the first is entered, the second derived from the contract
tax rates (`Contract.ContractTaxRate1..4`) and the `ExpenseSetup.ApplyTax1..4Flag` switches.
**Inferred** — the `Calculated` prefix and the `ApplyTaxNFlag` family make it the only coherent
reading. Precedence between the two is open question 3.

### The commands

`GENERATE_RENT` (rent from schedules), `GENERATE_PASS_THROUGH_PAYMENTS` (recovery pass-throughs),
`GENERATE_ASSET_RENT` (equipment), `GENERATE_RETRO_PAYMENT` (catch-up for a retroactive change),
`PROCESS_PAYMENT` / `PROCESS_MID_MONTH_PAYMENT` / `PROCESS_USAGE_PAYMENT`, and the teardown pair
`DELETE_PAYMENTS` / `DELETE_ASSET_PAYMENTS`. `APPROVE_PAYMENTS` exists at the `ProjectEntity`
(batch) level. **Observed** as `sTYPE_SUBMITBUTTON` fields.

---

## 2. `PaymentTransaction` — 118 fields, dissected

### Four independent date axes

| Field | Meaning |
|---|---|
| `PostingDate` | Which GL period it lands in |
| `EffectiveDate` | When it economically takes effect |
| `DueDate` | When cash is due |
| `BillingDate` | When it was billed |
| `CoverageBeginDate` / `CoverageEndDate` | The service period it pays for |
| `InvoiceDate` | Date on the landlord's invoice |
| `CheckDate` | When it settled |

Seven date fields, five genuinely independent axes. A rebuild that collapses posting/effective/due
into one date will lose the ability to post a March-coverage payment in April's GL period against a
February invoice — which is the normal case. **Observed.**

### Amounts

```
TotalAmount(Currency)             — the transaction's value
InvoiceAmount(Currency)           — what the landlord billed
PreAltRentInvoiceAmount(Currency) — what would have been billed without alternate rent
TaxAmount1..4(Currency)           — four parallel tax components
TaxesIncludedFlag(Boolean)        — are taxes inside TotalAmount or additional?
FreightAmount / MiscAmount(Currency)
CheckAmount(Currency)
AmountAllocated / AmountNotAllocated(Currency)
InvoiceAmountAllocated / InvoiceAmountNotAllocated(Currency)
ClientAmount1..3(Currency)        — tenant-defined amount slots
AmountInvoiced(TEXT)              ⚠  see §6
AmountReceived(TEXT)              ⚠  see §6
```

### Aging — two parallel ladders

```
AgingAmountForMonth1 / 2 / 3 / AgingAmountRemainder                  (0-30 / 31-60 / 61-90 / 90+)
DueDateAgingAmountForMonth1 / 2 / 3 / DueDateAgingAmountRemainder    (same buckets, by due date)
```

Labels confirm: *"Total Amount (0-30 days)"* vs *"Total Amount (Due Date 0-30 days)"*. Two aging
bases — presumably invoice date and due date. **Observed** labels; the first ladder's base date is
**Inferred** as invoice/effective date. Open question 4.

### State booleans

| Flag | Meaning |
|---|---|
| `HoldFlag` | Suppressed from processing/export |
| `ProcessedFlag` | Has been through `PROCESS_PAYMENT` |
| `ConfirmedFlag` | Confirmed |
| `PrepaidFlag` | A prepayment |
| `CreditFlag` | A credit rather than a charge |
| `OneTimeFlag` | Not recurring |
| `IsReceivable` | **Direction: receivable rather than payable** |
| `IsInvoiceReconciled` | Matched against a landlord invoice |
| `InAlternateRent` | Generated under an alternate-rent regime |

`IsReceivable` is the field that makes this one ledger rather than two. It also appears on
`ExpenseSetup` — so the *clause* declares direction and the transaction inherits it. **Observed.**

### Provenance — five FKs plus a discriminator

```
ExpenseSetupID(Expense Setup ID)             — generated from a recurring expense clause
ExpenseRecoveryID(Text)                      — a CAM recovery settlement          ⚠ weak FK
PercentageRentID(Percentage Rent ID)         — percentage rent
AlternateRentScheduleID(Alternate Rent Sch.) — alternate rent
ScheduledOffsetID(Text)                      — an offset draw-down                ⚠ weak FK
PropertyTaxBillID(Property Tax Bill ID)      — a property tax bill
AppliedToPayTranID(Payment Transaction ID)   — a credit applied to another transaction ⟲ self-ref
SourceEntityTable(Text) + CodeSourceEntityID(Dropdown (Source Entity Code))
```

`AppliedToPayTranID` is the credit-application self-reference: a credit note points at the
transaction it offsets. Combined with `CreditFlag`, that is a complete credit-memo model.
**Observed.**

### Counterparty and routing

```
VendorID(Employer ID)          — the payee. UI label "Vendor"; declared type Employer ID.
OrganizationID(Organization ID)— the org whose accounts are debited
BankAccountNumber / BankRoutingNumber(Text)   ⚠ see §6
VendorAccountNumber (on ExpenseSetup)
CodePaymentMethodID(Dropdown (Payment Method Code))
RemitMessage(Text)             — remittance advice text
VendorRefNumber(Text)          — label: "Client Reference Number"
InternalRefNumber(Text)
```

Per [009](../../admin/009-related-fields-and-data-model.md): **`Contract` has no Vendor FK.** The
vendor relationship lives here, one level down, and "Vendor" is a relabelled `Employer`. A contract
can therefore have many vendors across its payments — and `ExpenseVendorAllocation` (16 fields:
`VendorID`, `PaymentPercentage`, `APVendorNumber`, `ExpenseSetupID`, `BeginDate`/`EndDate`) splits
a single expense clause across several vendors by percentage. `CHANGE_EXPENSE_ALLOCATION_VENDOR` is
the command that rewrites it. **Observed.**

### Documents

`AssociatedDocumentID(Document ID)`, `DocumentIDList(Document List)`, `FolderID(Folder ID)`,
`BaseName(Text)` (label *"File Name"*). Every payment can carry its supporting documents.

---

## 3. `PaymentReceipt` — the inbound side

21 fields. Deliberately much thinner than `PaymentTransaction`.

```
PaymentReceiptID, ContractID, ProjectEntityID, BOMapClientRecordID
ReceiptNumber(Text), ReceiptDate(Date), EffectiveDate(Date), PostingDate(Date)
PeriodMonth(Number), PeriodYear(Number)
ReceivedAmount(Currency)
AmountAllocated / AmountNotAllocated(Currency)
CodeReceiptTypeID(Dropdown (Receipt Type Code))
CodeCurrencyTypeID
BankAccountNumber / BankRoutingNumber(Text)
DocumentIDList, Notes, ModifiedByID, ModifiedDate
```

There is **no FK from `PaymentReceipt` to `PaymentTransaction`**. The allocation is carried only as
`AmountAllocated` / `AmountNotAllocated` on both sides, and the `RECONCILE_RECEIPT` command joins
them. **Observed absence.** How a receipt is matched to the transactions it settles is open
question 1 — and it is a genuine schema gap ASG Edge+ should close with an explicit allocation
table (the same shape as `LinkLandlordInvPaymentTxn`).

---

## 4. `LandlordInvoice` / `LandlordInvoiceItem` and the three-way match

### `LandlordInvoice` — 31 fields

```
LandlordInvoiceID, ContractID, ProjectEntityID
InvoiceNumber, InvoiceDate, DueDate, PaymentTerm(Text)
ServicePeriodStartDate / ServicePeriodEndDate(Date)
SubTotal / TotalTax / InvoiceTotal(Currency)
AmountAllocated / AmountNotAllocated(Currency)
EmployerID(Employer ID)                       — the landlord
VendorName / VendorAddress / VendorAddressRecipient / VendorTaxID(Text)
CustomerName / CustomerAddress / CustomerAddressRecipient / CustomerID / CustomerTaxID(Text)
AssociatedDocumentID(Document ID), FolderID(Folder ID)
CodeCurrencyTypeID, Notes, Created/Modified
```

The ten denormalised `VendorName`/`VendorAddress`/`VendorTaxID`/`CustomerName`/… `Text` fields
alongside a real `EmployerID` FK are the signature of **document extraction** — these are the values
scraped off the invoice PDF, kept as-received for audit, separate from the resolved entity. The
`IMPORT_INVOICE` command feeds it. **Derived**; the extraction reading is **Inferred** but strongly
supported by `ExpenseRecoveryItemMapping.JSONConfigText`/`InvoiceLineItemName` doing the same job
one level down.

### `LandlordInvoiceItem` — 28 fields

```
LandlordInvoiceID(Text) ⚠ weak FK, SequenceNumber(Number)
LineItemDescription(Text), LineItemAmount(Currency), ItemDate(Date)
TaxAmount(Currency), TaxRate(Percentage), TotalAmount(Currency)
AmountNotAllocated(Currency), LinkAmountAllocated(Text)
CodeExpenseGroupID / CodeExpenseTypeID / CodeExpenseCategoryID
RemitMessage(Text), Comments(Text)
── the seven PayTrans* mirror fields ──
PayTransCategory(Text)        PayTransEffectiveDate(Text)   PayTransExpenseGroup(Text)
PayTransExpenseType(Text)     PayTransIsReceivable(Text)    PayTransTotalAmount(Text)
PayTransVendor(Text)
```

The seven `PayTrans*` fields are **denormalised copies of the matched payment transaction's key
attributes, all typed `Text`** — including `PayTransTotalAmount(Text)`, a money value stored as
text, and `PayTransEffectiveDate(Text)`, a date stored as text. They exist so a reconciliation grid
can render invoice line and payment side by side in one row. **Observed.** They are a §4.4 hazard
and a denormalisation ASG Edge+ should replace with a join.

### `LinkLandlordInvPaymentTxn` — the match itself

```
LandlordInvoiceItemID(Text) ⟷ PaymentTransactionID(Payment Transaction ID)
AllocationAmount(Currency)     — how much of the payment settles this line
AllocationDate(Date)
VarianceAmount(Currency)       — the difference
VarianceReason(Text)           — why
ReconciliationStatus(Text)
Notes, Created/Modified, ProjectEntityID
```

**This is the best-designed object in the module.** It is a many-to-many allocation carrying the
variance and its explanation on the join. One payment can settle several invoice lines; one invoice
line can be settled by several payments; every discrepancy is recorded with a reason.
`PaymentTransaction.IsInvoiceReconciled(Boolean)` is the resulting flag. **Observed.**

ASG Edge+ should copy this shape verbatim — and extend it to the receipt side, which currently
lacks an equivalent (§3).

### `InvoiceIssue` / `InvoiceItem` — the outbound side

`InvoiceIssue` (23) is a **batch**: `BatchNumber`, `BatchDate`, `InvoiceNumber`, `InvoiceDate`,
`ReceivedDate`, `PaidDate`, `InvoiceAmount`, `TaxAmount1..2`, `TotalAmount`,
`CodeInvoiceStatusID`, `IssueID(Text)`. `InvoiceItem` (18) is its line: `GLNumber(Text)`,
`SubAccount(Text)`, `Quantity`, `UnitCost`, `InvoiceAmount`, `TaxAmount1..2`, `TotalAmount`.

Both sit under the **Specialized Forms** top group, not Contract — they belong to the issue/service
side of the product, not the lease. **Observed.** They are the only place `GLNumber` appears as a
plain field rather than as a numbered account slot.

---

## 5. The GL export contract

This is a hard integration contract, and it is fully enumerable. **Observed.**

### Where the account numbers are defined: `CodeExpenseType`

`CodeExpenseType` (31 fields) is a code table that carries **20 GL account slots** and **three
accounting-treatment bindings**:

```
── AP export accounts ──
APExportBaseNumber, APExportPrepaidNumber, APExportTax1..4Number          (6 slots)
── accrual accounts, by accrual purpose ──
ExpAccrualAcct1..4Number             (expense accrual)                    (4 slots)
PercentRentAccrualAcct1..4Number     (percentage rent accrual)            (4 slots)
RETaxAccrualAcct1..4Number           (real-estate tax accrual)            (4 slots)
── accounting treatment ──
CodeASC842ScheduleID(Dropdown (ASC 842 Schedule Type))
CodeIFRS16ScheduleID(Dropdown (IFRS 16 Schedule Type))
CodeSLScheduleID(Dropdown (Straight Line Schedule Type))
── taxonomy ──
CodeExpenseCategoryID, ParentCodeExpenseGroupID, ParentID(Expense Group Code)
ShortName, LongDescription, ActualLongName, Inactive
```

**Choosing an expense type chooses both the GL coding and the lease-accounting treatment.** That is
the single most load-bearing fact about the classification system, and it is why
`CodeExpenseTypeID` appears on `ExpenseSetup`, `PaymentTransaction`, `AccrualTransaction`,
`PercentageRent`, `UseBasedRent`, `ExpenseRecovery`, `ExpenseAccrualSetup`, `LandlordInvoiceItem`,
`VariableRentOffset` and `VirtualExpenseForecastPeriod`. Ten objects, one classification.

`CodeSLSchedule` (24 fields) similarly carries `ExportAcct1..20Number` and
`DontAmortizeAssetValue(Boolean)` — 20 more slots for the straight-line side, mirrored on
`SLPeriod` as `ExportAcct1..20Number` plus `SLExportAcct1..3Number`.

### Where they land: `PaymentTransaction` and `AccrualTransaction`

Both carry a **snapshot** of the account numbers on every row:

| Slot family | `PaymentTransaction` | `AccrualTransaction` | `CodeExpenseType` |
|---|:---:|:---:|:---:|
| `AccountNumber1..8` | ✓ | ✓ | — |
| `APExportBaseNumber` | ✓ | ✓ | ✓ |
| `APExportPrepaidNumber` | ✓ | ✓ | ✓ |
| `APExportTax1..4Number` | ✓ | — | ✓ |
| `ExpAccrualAcct1..4Number` | ✓ | ✓ | ✓ |
| `PercentRentAccrualAcct1..4Number` | ✓ | ✓ | ✓ |
| `RETaxAccrualAcct1..4Number` | ✓ | ✓ | ✓ |

`AccountNumber1..8` exists on the transactions but **not** on `CodeExpenseType`. Its likely source
is `Organization` — `docs/data-fields/` shows `Organization` carrying `Account Number #1–8`
(recorded in [009](../../admin/009-related-fields-and-data-model.md)'s Related Fields walkthrough).
So the eight-segment account string comes from the **org**, and the base/tax/accrual accounts come
from the **expense type**. **Inferred**, and open question 2 — it is the core of any GL export.

`docs/data-fields/payment-transaction.md` reads the eight slots as split coding: *"up to eight
parallel 'Account Number #N' fields for split GL coding … Lucernex models multi-line allocation as
fixed parallel columns rather than a normalized child table."* **Observed** statement, but note it
conflicts with the eight-segments-of-one-account reading. Both are plausible; resolving it is part
of open question 2.

### Export batching

```
ExportBatchNumber(Text)   — set when the row leaves for AP
CheckNumber(Text)         — set when AP settles it
CheckDate(Date)
CheckAmount(Currency)
CodeCheckCurrencyTypeID   — the check may be in a different currency than the transaction
```

`CodeCheckCurrencyTypeID` being distinct from `CodeCurrencyTypeID` means **settlement currency can
differ from transaction currency** — an FX exposure the schema acknowledges but carries no rate
field for. `SLPeriod` does carry `ConversionRateAverage`, `ConversionRateMonthEnd`, `FXGainLoss`
and a `*Translated` twin for every monetary field; `PaymentTransaction` carries none of that.
**Observed asymmetry** — open question 5.

### `PaymentTransactionFullImport`

A 118-field, field-for-field mirror of `PaymentTransaction` with **no Postgres table**. An import
staging buffer for bulk payment loads. **Observed** (the field lists are identical; the PG TABLE
cell is empty). Its existence tells ASG Edge+ that bulk payment import is a first-class requirement,
not an afterthought.

---

## 6. Typing hazards on the payment path (Constitution §4.4)

Every item below is **Observed** in `_lucernex_objects_summary.txt`.

| Field | Declared type | Should be | Why it matters |
|---|---|---|---|
| `PaymentTransaction.AmountInvoiced` | **`Text`** | `BigDecimal` | A money field stored as text, sitting next to `InvoiceAmount(Currency)` |
| `PaymentTransaction.AmountReceived` | **`Text`** | `BigDecimal` | Same |
| `LandlordInvoiceItem.PayTransTotalAmount` | **`Text`** | `BigDecimal` | Denormalised money-as-text on the reconciliation grid |
| `LandlordInvoiceItem.LinkAmountAllocated` | **`Text`** | `BigDecimal` | Allocation amount as text |
| `LandlordInvoiceItem.PayTransEffectiveDate` | **`Text`** | `LocalDate` | Date as text |
| `LandlordInvoiceItem.PayTransIsReceivable` | **`Text`** | `boolean` | Boolean as text |
| `PaymentTransaction.ExpenseRecoveryID` | **`Text`** | FK | Weak FK on the recovery settlement path |
| `PaymentTransaction.ScheduledOffsetID` | **`Text`** | FK | Weak FK on the offset path |
| `LandlordInvoiceItem.LandlordInvoiceID` | **`Text`** | FK | Weak FK — invoice line to invoice header |
| `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID` | **`Text`** | FK | Weak FK on the match table |
| `AccrualTransaction.ExpenseAccrualSetupID` | **`Text`** | FK | Weak FK |
| **All 20 GL account slots** | `Text` | `Text` — correct | GL account codes are legitimately strings; keep them strings |
| `PaymentTransaction.BankAccountNumber` / `BankRoutingNumber` | `Text` | encrypted `Text` | Correctly typed, but this is **PII/PCI-adjacent data stored on a transaction row** |
| `sales.GrossSalesAmount` and every landed column | PG `TEXT` | `NUMERIC` | The entire landed schema is untyped — see [`data-model.md` §5](data-model.md#5-postgres-reality-every-column-is-text) |

**`AmountInvoiced` and `AmountReceived` are the sharpest single instances**: two money fields on the
platform's central ledger, typed `Text`, adjacent to correctly-typed `Currency` siblings. Any
migration must parse them defensively and reconcile them against `InvoiceAmount` and
`PaymentReceipt.ReceivedAmount`.

---

## 7. The hold / suspend surface

| Flag | On | Effect |
|---|---|---|
| `HoldFlag` | `ExpenseSetup` | Suspend the clause |
| `HoldFlag` | `ExpenseSchedule` | Suspend one period step |
| `HoldFlag` | `ExpenseAccrualSetup` | Suspend accrual |
| `HoldFlag` | `PaymentTransaction` | Suspend one payment from processing/export |
| `HoldFlag` | `AccrualTransaction` | Suspend one accrual posting |
| `SetExpHoldFlag` | `AlternateRentSchedule` | **Sets** the expense hold when alternate rent applies |
| `SetPRHoldFlag` | `AlternateRentSchedule` | **Sets** the percentage-rent hold |
| `SuspendSL` | `AlternateRentSchedule` | Suspends straight-line accounting |
| `HoldAmountInSchedLiability` | `Covenant` | Excludes an amount from the ASC 842 liability |
| `ReadyForPaymentFlag` | `ExpenseSetup`, `ExpenseSchedule` | Positive gate (must be on) |
| `IncludeTermForAccruals` | `ContractTerm` | Whether an option term is accrued |
| `IncludeInPlanForecast` | `ExpenseSetup` | Whether the clause appears in forecasting |
| `IsIncludeInRollForwardReport` | `SLSummary` | Disclosure inclusion |

Two shapes here: **negative gates** (`HoldFlag`, `Suspend*`) and **positive gates**
(`ReadyForPayment*`, `Include*`). Both are needed. **Observed.**

---

## Open questions

Ranked by impact.

1. **How is a `PaymentReceipt` matched to the `PaymentTransaction`s it settles?** There is no FK and
   no link table. Only `AmountAllocated`/`AmountNotAllocated` on each side and the
   `RECONCILE_RECEIPT` command. Open a receipt in the UI and see what the reconcile screen joins on.
   *This is a genuine schema gap — ASG Edge+ should add an explicit allocation table.*
2. **Where do `AccountNumber1..8` come from, and are they eight segments of one account or eight
   split-coding lines?** `docs/data-fields/payment-transaction.md` says split coding; `Organization`
   also carries `Account Number #1–8`, suggesting segments. Read one posted transaction's eight
   values against its organization's eight. *This is the core of the GL export.*
3. **Precedence between `ExpenseSchedule.TaxAmount1..4` and `CalculatedTaxAmount1..4`.** Which one
   reaches `PaymentTransaction.TaxAmount1..4`?
4. **What is the base date for the first aging ladder (`AgingAmountForMonth1..3`)?** Invoice date or
   effective date? The second ladder is explicitly due-date-based.
5. **Is there any FX rate on the payment path?** `CodeCheckCurrencyTypeID` differs from
   `CodeCurrencyTypeID` but no rate or gain/loss field exists on `PaymentTransaction`, while
   `SLPeriod` has a full translation apparatus. Confirm whether cross-currency settlement is
   actually supported or merely representable.
6. **Does `DELETE_PAYMENTS` refuse rows carrying `ExportBatchNumber` or `CheckNumber`?**
   Determines whether "exported" is a hard immutability boundary.
7. **What are the members of `Dropdown (Source Entity Code)`?** The complete list of generators that
   can write to the ledger.
8. **Are `ExpenseAllocation` (by `OrganizationID`, `AllocationPercentage`) and
   `ExpenseVendorAllocation` (by `VendorID`, `PaymentPercentage`) applied at generation time
   (producing N transactions) or at export time (producing N GL lines from one transaction)?**
   Changes the cardinality of the ledger.
