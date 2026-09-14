# Rent & Payments

Money that actually moves: generated rent, payment transactions against a lease, and the invoice records that carry them. Everything here hangs off the payment record - the lease itself never holds a vendor or a payment.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Accounts payable and the lease administrators who reconcile what was billed against what the lease says.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

Payment Info on the contract, and the invoice list layouts.

## Generate Rent output

*Observed · capability · source: `docs/modules/contracts/rent-generation.md`*

Generate Rent writes payment/charge transactions - this tenant holds 11,426 of them. The existing output was read instead of pressing the button on a shared tenant. Overwrite-versus-duplicate behaviour and batch-number storage remain open, needing a disposable lease.

## Payee on the payment

*Observed · capability · source: `docs/modules/workflow/`*

The payee lives on the payment, typed as Employer. Payment history also enters through a workflow step ('Import Payment History/Sales'), so payments arrive both by button and by process.

## Line-item invoices

*Observed · capability · source: `View Object Model, Math field list`*

Invoices are line-item records, and their totals are the only formulas outside the recovery grid and the accounting tests - invoicing computes its totals, it does not store them pre-summed.

## Allowances & offsets

*Derived · capability · source: `data-fields/allowance.md, scheduled-offset.md, variable-rent-offset.md`*

Tenant improvement and other allowances, offset against rent: the Allowance, Scheduled Offset and Variable Rent Offset records are tabulated field-by-field in the corpus. The posting and offsetting behavior - when an offset fires, what it nets against - is not yet written up as analysis. ASG Edge+ BRD-22.

## Accrual management

*Derived · capability · source: `data-fields/accrual-transaction.md, expense-accrual-setup.md`*

Expense accruals: Accrual Transaction, Expense Accrual Setup and the virtual PR accrual period records are tabulated. Accrual runs, reversals and period-close behavior are not yet analyzed. ASG Edge+ BRD-23.

## Rules (16)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### 2 Contract identity — [CON-R-019](../rules/CON-R-019.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Determining payable vs receivable: direction is carried on ExpenseSetup.IsReceivable and PaymentTransaction.IsReceivable, not on the contract, so one contract can be both.**

|  |  |
|---|---|
| Stated as | Determining payable vs receivable |
| Stated as | `ExpenseSetup.IsReceivable`, `PaymentTransaction.IsReceivable` |
| Stated as | Direction is carried per-clause and per-transaction, not on the contract. One contract may be both |
| Stated as | Money direction |
| Stated as | Observed |

### 2 Contract identity — [CON-R-020](../rules/CON-R-020.md)

*Derived · rule · source: `docs/modules/contracts/rules.md`*

**Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposit.PartyID.**

|  |  |
|---|---|
| Stated as | Resolving a contract's vendors |
| Stated as | `PaymentTransaction.VendorID`, `ExpenseSetup.VendorID`, `ExpenseVendorAllocation.VendorID`, `ScheduledOffset.VendorID`, `LandlordInvoice.EmployerID`, `SecurityDeposit.PartyID` |
| Stated as | `Contract` has no vendor FK; the set is derived from children |
| Stated as | Derived vendor set |
| Stated as | Observed |

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

### 6 Alternate rent and — [CON-R-072](../rules/CON-R-072.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A payment is generated under alternate rent: PreAltRentInvoiceAmount records what would have been invoiced without the concession.**

|  |  |
|---|---|
| Stated as | A payment is generated under alternate rent |
| Stated as | `PaymentTransaction.InAlternateRent`, `.AlternateRentScheduleID`, `.PreAltRentInvoiceAmount` |
| Stated as | Records what would have been invoiced without the concession |
| Stated as | Concession audit trail |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-111](../rules/CON-R-111.md)

*Inferred · rule · source: `docs/modules/contracts/rules.md`*

**Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved.**

|  |  |
|---|---|
| Stated as | Eight-segment coding is applied |
| Stated as | `AccountNumber1..8` |
| Stated as | Present on `PaymentTransaction` and `AccrualTransaction`, absent from `CodeExpenseType`; `Organization` carries `Account Number #1–8`. Whether these are 8 segments of one account or 8 split-coding lines is unresolved |
| Stated as | Account string |
| Stated as | Inferred — unresolved |

### 9 Payment lifecycle — [CON-R-115](../rules/CON-R-115.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**An invoice line is matched to a payment: LinkLandlordInvPaymentTxn allocates AllocationAmount/AllocationDate between LandlordInvoiceItemID and PaymentTransactionID.**

|  |  |
|---|---|
| Stated as | An invoice line is matched to a payment |
| Stated as | `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`, `.PaymentTransactionID`, `.AllocationAmount`, `.AllocationDate` |
| Stated as | Many-to-many allocation |
| Stated as | Match |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-117](../rules/CON-R-117.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**A payment is fully matched: PaymentTransaction.IsInvoiceReconciled is set when the three-way match completes.**

|  |  |
|---|---|
| Stated as | A payment is fully matched |
| Stated as | `PaymentTransaction.IsInvoiceReconciled` |
| Stated as | Set when the three-way match completes |
| Stated as | Reconciled flag |
| Stated as | Observed |

### 9 Payment lifecycle — [CON-R-118](../rules/CON-R-118.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side.**

|  |  |
|---|---|
| Stated as | Money is received |
| Stated as | `PaymentReceipt.ReceivedAmount`, `.AmountAllocated`, `.AmountNotAllocated`, `RECONCILE_RECEIPT` |
| Stated as | There is no FK or link table from `PaymentReceipt` to `PaymentTransaction` — only allocated/unallocated totals on each side |
| Stated as | Receipt allocation |
| Stated as | Observed (by absence) — schema gap |

### 9 Payment lifecycle — [CON-R-124](../rules/CON-R-124.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own.**

|  |  |
|---|---|
| Stated as | Bulk payments are imported |
| Stated as | `PaymentTransactionFullImport` (118 fields, no PG table) |
| Stated as | A field-for-field staging mirror of `PaymentTransaction` |
| Stated as | Import buffer |
| Stated as | Observed |

### 10 Suppression and — [CON-R-125](../rules/CON-R-125.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer.**

|  |  |
|---|---|
| Stated as | Any generation or posting |
| Stated as | `HoldFlag` on `ExpenseSetup`, `ExpenseSchedule`, `ExpenseAccrualSetup`, `PaymentTransaction`, `AccrualTransaction` |
| Stated as | Negative gate at every layer |
| Stated as | Suppression |
| Stated as | Observed |

### 11 Typing and — [CON-R-132](../rules/CON-R-132.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount.**

|  |  |
|---|---|
| Stated as | Migrating `PaymentTransaction` |
| Stated as | `AmountInvoiced(Text)`, `AmountReceived(Text)` |
| Stated as | Two money fields on the central ledger are declared `Text` while their siblings are `Currency` |
| Stated as | Parse to `BigDecimal`; reconcile against `InvoiceAmount` and `PaymentReceipt.ReceivedAmount` |
| Stated as | Observed |

### 11 Typing and — [CON-R-134](../rules/CON-R-134.md)

*Observed · rule · source: `docs/modules/contracts/rules.md`*

**Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy.**

|  |  |
|---|---|
| Stated as | Migrating any parent-child edge |
| Stated as | Seven `Text`-typed FKs (`PaymentTransaction.ExpenseRecoveryID`, `.ScheduledOffsetID`, `ExpenseSchedule.Previous/NextExpenseScheduleID`, `ExpenseAccrualSchedule.ExpenseAccrualSetupID`, `AccrualTransaction.ExpenseAccrualSetupID`, `ExpenseRecoveryItem.ExpenseRecoveryID`, `LandlordInvoiceItem.LandlordInvoiceID`, `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`) |
| Stated as | Declared `Text` rather than a typed FK, though the target's FK type exists elsewhere |
| Stated as | Model as real FKs; define an orphan-handling policy |
| Stated as | Observed |

### C The Edit List — [LAY-R-120](../rules/LAY-R-120.md)

*Observed · rule · source: `docs/modules/layouts-and-forms/rules.md`*

**A single `PageLayoutID` can carry both a detail Edit Layout and a grid List Layout, as two orthogonal facets of one record. Proven on `ASG Contract Payments` (96214, `PaymentTransaction`).**

|  |  |
|---|---|
| Stated as | A single `PageLayoutID` can carry both a detail Edit Layout and a grid List Layout, as two orthogonal facets of one record. Proven on `ASG Contract Payments` (96214, `PaymentTransaction`). |
| Stated as | Observed |
| Stated as | 008 |

### Employer is one — [PPL-R-004](../rules/PPL-R-004.md)

*Observed · rule · source: `docs/modules/people-parties/rules.md`*

**No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema.**

|  |  |
|---|---|
| When it fires | Any process that treats Vendor, Landlord, or Tenant-as-counterparty as separate entities |
| What it reads | `PaymentTransaction.VendorID` (type `Employer ID`), `LinkProjectEntityContact. Landlord_EmployerID`, `Employer.Is*Vendor` flags |
| The test | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema |
| What it writes | All three business roles resolve to one `Employer` row. A rebuild should not create separate entities that then require manual synchronisation |

### Only PropertyTaxBill — [TAX-R-010](../rules/TAX-R-010.md)

*Observed · rule · source: `docs/modules/property-tax/rules.md`*

**Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit in this family.**
