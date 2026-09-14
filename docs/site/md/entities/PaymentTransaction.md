# PaymentTransaction

*118 fields · module: Lease Accounting & Payments · Postgres: `payment_transaction`*

Individual rent/expense payment or receipt records against a contract — up to eight parallel 'Account Number #N' fields for split GL coding, allocation amounts, and payment dates. 118 fields, all Global. The repeated-numbered-field pattern (Account Number #1 through #8) is common across the financial entities in this catalog and indicates Lx models multi-line allocation as fixed parallel columns rather than a normalized child table exposed to this catalog.

Source: `data-fields/payment-transaction.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 118 |
| Catalogued fields | 118 (118 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 4 keys from 4 record types |
| Points at | 13 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 15 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-019](../rules/CON-R-019.md) | Determining payable vs receivable: direction is carried on ExpenseSetup.IsReceivable and PaymentTransaction.IsReceivable, not on the contract, so one contract can be both. | Observed |
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [CON-R-063](../rules/CON-R-063.md) | Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue. | Derived |
| [CON-R-072](../rules/CON-R-072.md) | A payment is generated under alternate rent: PreAltRentInvoiceAmount records what would have been invoiced without the concession. | Observed |
| [CON-R-111](../rules/CON-R-111.md) | Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved. | Inferred |
| [CON-R-117](../rules/CON-R-117.md) | A payment is fully matched: PaymentTransaction.IsInvoiceReconciled is set when the three-way match completes. | Observed |
| [CON-R-118](../rules/CON-R-118.md) | Money is received: there is no FK or link table from PaymentReceipt to PaymentTransaction — only allocated/unallocated totals on each side. | Observed |
| [CON-R-124](../rules/CON-R-124.md) | Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own. | Observed |
| [CON-R-125](../rules/CON-R-125.md) | Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer. | Observed |
| [CON-R-132](../rules/CON-R-132.md) | Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |
| [LAY-R-120](../rules/LAY-R-120.md) | A single `PageLayoutID` can carry both a detail Edit Layout and a grid List Layout, as two orthogonal facets of one record. Proven on `ASG Contract Payments` (96214, `PaymentTransaction`). | Observed |
| [PPL-R-004](../rules/PPL-R-004.md) | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema | Observed |
| [TAX-R-010](../rules/TAX-R-010.md) | Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit in this family. | Observed |

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AlternateRentScheduleID` | Alternate Rent Schedule | Alternate Rent Schedule ID | Global |  | [AlternateRentSchedule](AlternateRentSchedule.md) |
| `AppliedToPayTranID` | Applied to Transaction | Payment Transaction ID | Global |  | [PaymentTransaction](PaymentTransaction.md) |
| `AssetID` | Equipment | Equipment ID | Global |  | [Asset](Asset.md) |
| `AssociatedDocumentID` | Associated Document | Document ID | Global |  | [Document](Document.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | Expense Setup ID | Global |  | [ExpenseSetup](ExpenseSetup.md) |
| `FolderID` | Folder | Folder ID | Global |  | [Folder](Folder.md) |
| `OrganizationID` | Organization | Organization ID | Global |  | [Organization](Organization.md) |
| `PercentageRentID` | Percentage Rent | Percentage Rent ID | Global |  | [PercentageRent](PercentageRent.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxBillID` | Property Tax Bill | Property Tax Bill ID | Global |  | [PropertyTaxBill](PropertyTaxBill.md) |
| `VendorID` | Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | Entity | Global |  |  |
| `DocumentIDList` | Documents | Document List | Global |  |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeApprovalStatusID` | Approval Status | Dropdown (Approval Status Code) | Global |  | Approval Status Code |
| `CodeCheckCurrencyTypeID` | Check Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | Global |  | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodePaymentMethodID` | Payment Method | Dropdown (Payment Method Code) | Global |  | Payment Method Code |
| `CodeSourceEntityID` | Source Entity | Dropdown (Source Entity Code) | Global |  | Source Entity Code |

### Money (25)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AgingAmountForMonth1` | Total Amount (0-30 days) | Currency | Global |  |  |
| `AgingAmountForMonth2` | Total Amount (31-60 days) | Currency | Global |  |  |
| `AgingAmountForMonth3` | Total Amount (61-90 days) | Currency | Global |  |  |
| `AgingAmountRemainder` | Total Amount (over 90 days) | Currency | Global |  |  |
| `AmountAllocated` | Amount Allocated | Currency | Global |  |  |
| `AmountNotAllocated` | Amount Not Allocated | Currency | Global |  |  |
| `CheckAmount` | Check Amount | Currency | Global |  |  |
| `ClientAmount1` | Client Amount #1 | Currency | Global |  |  |
| `ClientAmount2` | Client Amount #2 | Currency | Global |  |  |
| `ClientAmount3` | Client Amount #3 | Currency | Global |  |  |
| `DueDateAgingAmountForMonth1` | Total Amount (Due Date 0-30 days) | Currency | Global |  |  |
| `DueDateAgingAmountForMonth2` | Total Amount (Due Date 31-60 days) | Currency | Global |  |  |
| `DueDateAgingAmountForMonth3` | Total Amount (Due Date 61-90 days) | Currency | Global |  |  |
| `DueDateAgingAmountRemainder` | Total Amount (Due Date over 90 days) | Currency | Global |  |  |
| `FreightAmount` | Freight Amount | Currency | Global |  |  |
| `InvoiceAmount` | Invoice Amount | Currency | Global |  |  |
| `InvoiceAmountAllocated` | Invoice Amount Allocated | Currency | Global |  |  |
| `InvoiceAmountNotAllocated` | Invoice Amount Not Allocated | Currency | Global |  |  |
| `MiscAmount` | Misc Amount | Currency | Global |  |  |
| `PreAltRentInvoiceAmount` | Pre-Alternate Rent Invoice Amount | Currency | Global |  |  |
| `TaxAmount1` | Tax Amount #1 | Currency | Global |  |  |
| `TaxAmount2` | Tax Amount #2 | Currency | Global |  |  |
| `TaxAmount3` | Tax Amount #3 | Currency | Global |  |  |
| `TaxAmount4` | Tax Amount #4 | Currency | Global |  |  |
| `TotalAmount` | Total Amount | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PaymentTransactionID` | Payment Transaction RecID | Number | Global |  |  |

### Dates & timestamps (12)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillingDate` | Billing Date | Date | Global |  |  |
| `CheckDate` | Check Date | Date | Global |  |  |
| `ClientDate1` | Client Date #1 | Date | Global |  |  |
| `ClientDate2` | Client Date #2 | Date | Global |  |  |
| `ClientDate3` | Client Date #3 | Date | Global |  |  |
| `CoverageBeginDate` | Coverage Begin Date | Date | Global |  |  |
| `CoverageEndDate` | Coverage End Date | Date | Global |  |  |
| `DueDate` | Due Date | Date | Global |  |  |
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `InvoiceDate` | Invoice Date | Date | Global |  |  |
| `LastApprovalChangeDate` | Last Approval Change Date | Date | Global |  |  |
| `PostingDate` | Posting Date | Date | Global |  |  |

### Flags (10)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ConfirmedFlag` | Confirmed? | Boolean | Global |  |  |
| `CreditFlag` | Credit? | Boolean | Global |  |  |
| `HoldFlag` | Hold? | Boolean | Global |  |  |
| `InAlternateRent` | In Alternate Rent? | Boolean | Global |  |  |
| `IsInvoiceReconciled` | Is Invoice Reconciled? | Boolean | Global |  |  |
| `IsReceivable` | Is Receivable? | Boolean | Global |  |  |
| `OneTimeFlag` | One Time? | Boolean | Global |  |  |
| `PrepaidFlag` | Prepaid? | Boolean | Global |  |  |
| `ProcessedFlag` | Processed? | Boolean | Global |  |  |
| `TaxesIncludedFlag` | Taxes Included In Amount? | Boolean | Global |  |  |

### Text & notes (45)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `APExportBaseNumber` | AP Export Base Number | Text | Global |  |  |
| `APExportPrepaidNumber` | AP Export Prepaid Number | Text | Global |  |  |
| `APExportTax1Number` | AP Export Tax #1 | Text | Global |  |  |
| `APExportTax2Number` | AP Export Tax #2 | Text | Global |  |  |
| `APExportTax3Number` | AP Export Tax #3 | Text | Global |  |  |
| `APExportTax4Number` | AP Export Tax #4 | Text | Global |  |  |
| `AccountNumber1` | Account Number #1 | Text | Global |  |  |
| `AccountNumber2` | Account Number #2 | Text | Global |  |  |
| `AccountNumber3` | Account Number #3 | Text | Global |  |  |
| `AccountNumber4` | Account Number #4 | Text | Global |  |  |
| `AccountNumber5` | Account Number #5 | Text | Global |  |  |
| `AccountNumber6` | Account Number #6 | Text | Global |  |  |
| `AccountNumber7` | Account Number #7 | Text | Global |  |  |
| `AccountNumber8` | Account Number #8 | Text | Global |  |  |
| `AmountInvoiced` | Amount Invoiced | Text | Global |  |  |
| `AmountReceived` | Amount Received | Text | Global |  |  |
| `BankAccountNumber` | Bank Account Number | Text | Global |  |  |
| `BankRoutingNumber` | Bank Routing Number | Text | Global |  |  |
| `BaseName` | File Name | Text | Global |  |  |
| `CheckNumber` | Check Number | Text | Global |  |  |
| `ClientText1` | Client Text #1 | Text | Global |  |  |
| `ClientText2` | Client Text #2 | Text | Global |  |  |
| `ClientText3` | Client Text #3 | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `ExpAccrualAcct1Number` | Expense Accrual Acct #1 | Text | Global |  |  |
| `ExpAccrualAcct2Number` | Expense Accrual Acct #2 | Text | Global |  |  |
| `ExpAccrualAcct3Number` | Expense Accrual Acct #3 | Text | Global |  |  |
| `ExpAccrualAcct4Number` | Expense Accrual Acct #4 | Text | Global |  |  |
| `ExpenseRecoveryID` | Expense Recovery | Text | Global |  |  |
| `ExportBatchNumber` | Export Batch Number | Text | Global |  |  |
| `InternalRefNumber` | Internal Reference Number | Text | Global |  |  |
| `InvoiceNumber` | Invoice Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | Text | Global |  |  |
| `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | Text | Global |  |  |
| `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | Text | Global |  |  |
| `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | Text | Global |  |  |
| `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | Text | Global |  |  |
| `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | Text | Global |  |  |
| `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | Text | Global |  |  |
| `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | Text | Global |  |  |
| `RemitMessage` | Remit Message | Text | Global |  |  |
| `ScheduledOffsetID` | Scheduled Offset | Text | Global |  |  |
| `SourceEntityTable` | Source Entity Table | Text | Global |  |  |
| `VendorRefNumber` | Client Reference Number | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Payment Transaction ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (4 keys)

| Record type | Via column |
|---|---|
| [LinkLandlordInvPaymentTxn](LinkLandlordInvPaymentTxn.md) | `PaymentTransactionID` |
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `PaymentTransactionID` |
| [PaymentTransaction](PaymentTransaction.md) | `AppliedToPayTranID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `AppliedToPayTranID` |
