# PaymentTransaction

*118 fields · module: Lease Accounting & Payments · Postgres: `payment_transaction`*

Individual rent/expense payment or receipt records against a contract — up to eight parallel 'Account Number #N' fields for split GL coding, allocation amounts, and payment dates. 118 fields, all Global. The repeated-numbered-field pattern (Account Number #1 through #8) is common across the financial entities in this catalog and indicates Lx models multi-line allocation as fixed parallel columns rather than a normalized child table exposed to this catalog.

Source: `data-fields/payment-transaction.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 118 |
| Fields with a vendor definition | 113 of 118 inventoried |
| Physical tables | `payment_transaction` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 118 (118 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 4 keys from 4 record types |
| Points at | 13 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 15 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in payment_transaction

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 113 fields carry a vendor definition

**Observed.** 113 of this record's 118 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 1 field marked required

**Observed.** The inventory marks 1 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AlternateRentScheduleID` | Alternate Rent Schedule | The alternate rent schedule ID associated with the payment transaction. | Alternate Rent Schedule ID | Global |  | `payment_transaction.AlternateRentScheduleID · TEXT` | [AlternateRentSchedule](AlternateRentSchedule.md) |
| `AppliedToPayTranID` | Applied to Transaction | The payment transaction ID created when you apply a scheduled offset. | Payment Transaction ID | Global |  | `payment_transaction.AppliedToPayTranID · TEXT` | [PaymentTransaction](PaymentTransaction.md) |
| `AssetID` | Equipment | The associated asset record ID. | Equipment ID | Global |  | `payment_transaction.AssetID · TEXT` | [Asset](Asset.md) |
| `AssociatedDocumentID` | Associated Document | The ID of a document associated with this record. | Document ID | Global |  | `payment_transaction.AssociatedDocumentID · TEXT` | [Document](Document.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `payment_transaction.ContractID · TEXT` | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | The ExpenseSetupID field is used to associate a payment transaction with an expense setup record. | Expense Setup ID | Global |  | `payment_transaction.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |
| `FolderID` | Folder | The folder ID when you save a transaction to your documents. | Folder ID | Global |  | `payment_transaction.FolderID · TEXT` | [Folder](Folder.md) |
| `OrganizationID` | Organization | Select the organization from which this payment should be debited from this field. | Organization ID | Global |  | `payment_transaction.OrganizationID · TEXT` | [Organization](Organization.md) |
| `PercentageRentID` | Percentage Rent | The percentage rent record ID that the payment transaction is associated with. | Percentage Rent ID | Global |  | `payment_transaction.PercentageRentID · TEXT` | [PercentageRent](PercentageRent.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `payment_transaction.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxBillID` | Property Tax Bill | The ID of the property bill record associated with the transaction. This field is used in the Parcel module. | Property Tax Bill ID | Global |  | `payment_transaction.PropertyTaxBillID · TEXT` | [PropertyTaxBill](PropertyTaxBill.md) |
| `VendorID` | Vendor | Select the vendor that this payment should be paid to from this field. | Employer ID | Global |  | `payment_transaction.VendorID · TEXT` | [Employer](Employer.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | This is a reporting field that returns data about the asset associated with the entity. | Entity | Global |  | `payment_transaction.AssetAssociatedProjectEntityID · TEXT` |  |
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents a record. | Document List | Global |  | `payment_transaction.DocumentIDList · TEXT` |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeApprovalStatusID` | Approval Status | This field populates with the approval status of the transaction. A transaction must be approved from the Contract > Details > Summary page or the Equipment Contract > Details > Summary page. | Dropdown (Approval Status Code) | Global |  | `payment_transaction.CodeApprovalStatusID · TEXT` | Approval Status Code |
| `CodeCheckCurrencyTypeID` | Check Currency Type | Select the currency in which the check was written from the field. | Dropdown (Currency Type Code) | Global |  | `payment_transaction.CodeCheckCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `payment_transaction.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExpenseCategoryID` | Expense Category | The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the grandchildren of groups. | Dropdown (Expense Category Code) | Global |  | `payment_transaction.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `payment_transaction.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `payment_transaction.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodePaymentMethodID` | Payment Method | Select the payment method from this field. | Dropdown (Payment Method Code) | Global |  | `payment_transaction.CodePaymentMethodID · TEXT` | Payment Method Code |
| `CodeSourceEntityID` | Source Entity | This field is no longer used. | Dropdown (Source Entity Code) | Global |  | `payment_transaction.CodeSourceEntityID · TEXT` | Source Entity Code |

### Money (25)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AgingAmountForMonth1` | Total Amount (0-30 days) | The total amount of the transaction if the effective date of the transaction was within the last 30 days. | Currency | Global |  | `payment_transaction.AgingAmountForMonth1 · TEXT` |  |
| `AgingAmountForMonth2` | Total Amount (31-60 days) | The total amount of the transaction if the effective date of the transaction was within the last 60 days. | Currency | Global |  | `payment_transaction.AgingAmountForMonth2 · TEXT` |  |
| `AgingAmountForMonth3` | Total Amount (61-90 days) | The total amount of the transaction if the effective date of the transaction was within the last 90 days. | Currency | Global |  | `payment_transaction.AgingAmountForMonth3 · TEXT` |  |
| `AgingAmountRemainder` | Total Amount (over 90 days) | The total amount of the transaction if the effective date of the transaction was beyond the last 90 days. | Currency | Global |  | `payment_transaction.AgingAmountRemainder · TEXT` |  |
| `AmountAllocated` | Amount Allocated | This field automatically calculates the amount that has been applied to transactions so far. | Currency | Global |  | `payment_transaction.AmountAllocated · TEXT` |  |
| `AmountNotAllocated` | Amount Not Allocated | This field automatically calculates the remaining balance of the received transaction. | Currency | Global |  | `payment_transaction.AmountNotAllocated · TEXT` |  |
| `CheckAmount` | Check Amount | Enter the check amount in this field. | Currency | Global |  | `payment_transaction.CheckAmount · TEXT` |  |
| `ClientAmount1` | Client Amount #1 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Currency | Global |  | `payment_transaction.ClientAmount1 · TEXT` |  |
| `ClientAmount2` | Client Amount #2 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Currency | Global |  | `payment_transaction.ClientAmount2 · TEXT` |  |
| `ClientAmount3` | Client Amount #3 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Currency | Global |  | `payment_transaction.ClientAmount3 · TEXT` |  |
| `DueDateAgingAmountForMonth1` | Total Amount (Due Date 0-30 days) | The total amount of the transaction if the due date or end date of the transaction was within the last 30 days. | Currency | Global |  | `payment_transaction.DueDateAgingAmountForMonth1 · TEXT` |  |
| `DueDateAgingAmountForMonth2` | Total Amount (Due Date 31-60 days) | The total amount of the transaction if the due date or end date of the transaction was within the last 60 days. | Currency | Global |  | `payment_transaction.DueDateAgingAmountForMonth2 · TEXT` |  |
| `DueDateAgingAmountForMonth3` | Total Amount (Due Date 61-90 days) | The total amount of the transaction if the due date or end date of the transaction was within the last 90 days. | Currency | Global |  | `payment_transaction.DueDateAgingAmountForMonth3 · TEXT` |  |
| `DueDateAgingAmountRemainder` | Total Amount (Due Date over 90 days) | The total amount of the transaction if the due date or end date of the transaction was beyond the last 90 days. | Currency | Global |  | `payment_transaction.DueDateAgingAmountRemainder · TEXT` |  |
| `FreightAmount` | Freight Amount | Enter any freight amounts that should be included in the transaction total in this field. | Currency | Global |  | `payment_transaction.FreightAmount · TEXT` |  |
| `InvoiceAmount` | Invoice Amount | Enter the base amount of your invoice without taxes, freight, or miscellaneous costs. | Currency | Global |  | `payment_transaction.InvoiceAmount · TEXT` |  |
| `InvoiceAmountAllocated` | Invoice Amount Allocated |  | Currency | Global |  | `payment_transaction.InvoiceAmountAllocated · TEXT` |  |
| `InvoiceAmountNotAllocated` | Invoice Amount Not Allocated |  | Currency | Global |  | `payment_transaction.InvoiceAmountNotAllocated · TEXT` |  |
| `MiscAmount` | Misc Amount | Enter any other amounts that should be included in the transaction total in this field. | Currency | Global |  | `payment_transaction.MiscAmount · TEXT` |  |
| `PreAltRentInvoiceAmount` | Pre-Alternate Rent Invoice Amount | The amount that would be paid prior to applying the alternate rent amount. | Currency | Global |  | `payment_transaction.PreAltRentInvoiceAmount · TEXT` |  |
| `TaxAmount1` | Tax Amount #1 | Enter the primary tax amount in currency in this field. | Currency | Global |  | `payment_transaction.TaxAmount1 · TEXT` |  |
| `TaxAmount2` | Tax Amount #2 | Enter the secondary tax amount in currency in this field. | Currency | Global |  | `payment_transaction.TaxAmount2 · TEXT` |  |
| `TaxAmount3` | Tax Amount #3 | Enter the third tax amount in currency in this field. | Currency | Global |  | `payment_transaction.TaxAmount3 · TEXT` |  |
| `TaxAmount4` | Tax Amount #4 | Enter the fourth tax amount in currency in this field. | Currency | Global |  | `payment_transaction.TaxAmount4 · TEXT` |  |
| `TotalAmount` | Total Amount | This field will only be editable if the Taxes Included in Amount? flag is selected. The total amount is the base amount plus any taxes, freight amounts, or miscellaneous costs. | Currency | Global |  | `payment_transaction.TotalAmount · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PaymentTransactionID` | Payment Transaction RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `payment_transaction.PaymentTransactionID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (12)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillingDate` | Billing Date | The billing date. | Date | Global |  | `payment_transaction.BillingDate · TEXT` |  |
| `CheckDate` | Check Date | Enter the check date in this field. | Date | Global |  | `payment_transaction.CheckDate · TEXT` |  |
| `ClientDate1` | Client Date #1 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Date | Global |  | `payment_transaction.ClientDate1 · TEXT` |  |
| `ClientDate2` | Client Date #2 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Date | Global |  | `payment_transaction.ClientDate2 · TEXT` |  |
| `ClientDate3` | Client Date #3 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Date | Global |  | `payment_transaction.ClientDate3 · TEXT` |  |
| `CoverageBeginDate` | Coverage Begin Date | This field will pre-populate with your payment begin date. | Date | Global |  | `payment_transaction.CoverageBeginDate · TEXT` |  |
| `CoverageEndDate` | Coverage End Date | This field will pre-populate with your payment end date. | Date | Global |  | `payment_transaction.CoverageEndDate · TEXT` |  |
| `DueDate` | Due Date | Enter the date the payment is due in this field. | Date | Global |  | `payment_transaction.DueDate · TEXT` |  |
| `EffectiveDate` | Effective Date | Enter the effective date of the transaction in this field. | Date | Global |  | `payment_transaction.EffectiveDate · TEXT` |  |
| `InvoiceDate` | Invoice Date | Enter the invoice date in this field. | Date | Global |  | `payment_transaction.InvoiceDate · TEXT` |  |
| `LastApprovalChangeDate` | Last Approval Change Date | The date when the Approval Status field changed from Approved to Review. | Date | Global |  | `payment_transaction.LastApprovalChangeDate · TEXT` |  |
| `PostingDate` | Posting Date | Enter the date the transaction going to be sent to the accounting system in this field. | Date | Global |  | `payment_transaction.PostingDate · TEXT` |  |

### Flags (10)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ConfirmedFlag` | Confirmed? | This is an information-only flag. | Boolean | Global |  | `payment_transaction.ConfirmedFlag · TEXT` |  |
| `CreditFlag` | Credit? | If this transaction is a credit item, select this check box. | Boolean | Global |  | `payment_transaction.CreditFlag · TEXT` |  |
| `HoldFlag` | Hold? | If this transaction should be marked with a hold flag, select this check box. | Boolean | Global |  | `payment_transaction.HoldFlag · TEXT` |  |
| `InAlternateRent` | In Alternate Rent? | This field returns as true if this payment transaction has a reference to an Alternate Rent Expense Schedule ID. | Boolean | Global |  | `payment_transaction.InAlternateRent · TEXT` |  |
| `IsInvoiceReconciled` | Is Invoice Reconciled? |  | Boolean | Global |  | `payment_transaction.IsInvoiceReconciled · TEXT` |  |
| `IsReceivable` | Is Receivable? | If this transaction is an accounts receivable item, select this check box. These items are also known as income items. | Boolean | Global |  | `payment_transaction.IsReceivable · TEXT` |  |
| `OneTimeFlag` | One Time? | This flag indicates whether a transaction is a one-time expense or if it is a recurring expense. The one-time expense flag is not editable. | Boolean | Global |  | `payment_transaction.OneTimeFlag · TEXT` |  |
| `PrepaidFlag` | Prepaid? | This is an information-only flag. | Boolean | Global |  | `payment_transaction.PrepaidFlag · TEXT` |  |
| `ProcessedFlag` | Processed? | Once the transaction has been processed, select this check box. After you save changes, you cannot make any further changes. Do not select the Processed Flag check box unless you are certain you do not want to make any further changes. | Boolean | Global |  | `payment_transaction.ProcessedFlag · TEXT` |  |
| `TaxesIncludedFlag` | Taxes Included In Amount? | Select this check box if taxes are included in the value you entered in the Base Amount field. The system will then subtract the tax amounts from the base amount, and the Total Amount field becomes editable. If you need to make changes to the value in the Total Amount field, you may now do so. | Boolean | Global |  | `payment_transaction.TaxesIncludedFlag · TEXT` |  |

### Text & notes (45)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `APExportBaseNumber` | AP Export Base Number | The account number for your expenses. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.APExportBaseNumber · TEXT` |  |
| `APExportPrepaidNumber` | AP Export Prepaid Number | The account number for your prepaid expenses (if applicable). The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.APExportPrepaidNumber · TEXT` |  |
| `APExportTax1Number` | AP Export Tax #1 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.APExportTax1Number · TEXT` |  |
| `APExportTax2Number` | AP Export Tax #2 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.APExportTax2Number · TEXT` |  |
| `APExportTax3Number` | AP Export Tax #3 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.APExportTax3Number · TEXT` |  |
| `APExportTax4Number` | AP Export Tax #4 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.APExportTax4Number · TEXT` |  |
| `AccountNumber1` | Account Number #1 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber1 · TEXT` |  |
| `AccountNumber2` | Account Number #2 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber2 · TEXT` |  |
| `AccountNumber3` | Account Number #3 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber3 · TEXT` |  |
| `AccountNumber4` | Account Number #4 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber4 · TEXT` |  |
| `AccountNumber5` | Account Number #5 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber5 · TEXT` |  |
| `AccountNumber6` | Account Number #6 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber6 · TEXT` |  |
| `AccountNumber7` | Account Number #7 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber7 · TEXT` |  |
| `AccountNumber8` | Account Number #8 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | Global |  | `payment_transaction.AccountNumber8 · TEXT` |  |
| `AmountInvoiced` | Amount Invoiced |  | Text | Global |  | `payment_transaction.AmountInvoiced · TEXT` |  |
| `AmountReceived` | Amount Received | This field automatically calculates the amount received by totalling the value of any receipts which have been reconciled against this transaction. | Text | Global |  | `payment_transaction.AmountReceived · TEXT` |  |
| `BankAccountNumber` | Bank Account Number | Enter the bank account number in this field. Changing this value will change the approval status to Review. | Text | Global |  | `payment_transaction.BankAccountNumber · TEXT` |  |
| `BankRoutingNumber` | Bank Routing Number | Enter the bank routing number in this field. Changing this value will change the approval status to Review. | Text | Global |  | `payment_transaction.BankRoutingNumber · TEXT` |  |
| `BaseName` | File Name | This field displays the file name of the file attached to the record. | Text | Global |  | `payment_transaction.BaseName · TEXT` |  |
| `CheckNumber` | Check Number | Enter the payment/check reference number in this field. | Text | Global |  | `payment_transaction.CheckNumber · TEXT` |  |
| `ClientText1` | Client Text #1 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Text | Global |  | `payment_transaction.ClientText1 · TEXT` |  |
| `ClientText2` | Client Text #2 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Text | Global |  | `payment_transaction.ClientText2 · TEXT` |  |
| `ClientText3` | Client Text #3 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Text | Global |  | `payment_transaction.ClientText3 · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `payment_transaction.Description · TEXT` |  |
| `ExpAccrualAcct1Number` | Expense Accrual Acct #1 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.ExpAccrualAcct1Number · TEXT` |  |
| `ExpAccrualAcct2Number` | Expense Accrual Acct #2 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.ExpAccrualAcct2Number · TEXT` |  |
| `ExpAccrualAcct3Number` | Expense Accrual Acct #3 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.ExpAccrualAcct3Number · TEXT` |  |
| `ExpAccrualAcct4Number` | Expense Accrual Acct #4 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.ExpAccrualAcct4Number · TEXT` |  |
| `ExpenseRecoveryID` | Expense Recovery | The expense recovery record ID associated with the transaction. | Text | Global |  | `payment_transaction.ExpenseRecoveryID · TEXT` |  |
| `ExportBatchNumber` | Export Batch Number | The payment transaction batch number. This field is primarily used in integrations. | Text | Global |  | `payment_transaction.ExportBatchNumber · TEXT` |  |
| `InternalRefNumber` | Internal Reference Number | Enter the internal reference number, if you have one, in this field. | Text | Global |  | `payment_transaction.InternalRefNumber · TEXT` |  |
| `InvoiceNumber` | Invoice Number | Enter the invoice number in this field. | Text | Global |  | `payment_transaction.InvoiceNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `payment_transaction.Notes · TEXT` |  |
| `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.PercentRentAccrualAcct1Number · TEXT` |  |
| `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.PercentRentAccrualAcct2Number · TEXT` |  |
| `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.PercentRentAccrualAcct3Number · TEXT` |  |
| `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.PercentRentAccrualAcct4Number · TEXT` |  |
| `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.RETaxAccrualAcct1Number · TEXT` |  |
| `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.RETaxAccrualAcct2Number · TEXT` |  |
| `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.RETaxAccrualAcct3Number · TEXT` |  |
| `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | Global |  | `payment_transaction.RETaxAccrualAcct4Number · TEXT` |  |
| `RemitMessage` | Remit Message | Enter a remittance message in this field. This is the message that will appear on the memo line of a check. | Text | Global |  | `payment_transaction.RemitMessage · TEXT` |  |
| `ScheduledOffsetID` | Scheduled Offset | The ID of the schedule offset record associated with the transaction. | Text | Global |  | `payment_transaction.ScheduledOffsetID · TEXT` |  |
| `SourceEntityTable` | Source Entity Table | The record type used to generate the transaction so that a unique identifier can be created for the batch. For example, transactions generated by the Generate Rent action begin with the code RNT. | Text | Global |  | `payment_transaction.SourceEntityTable · TEXT` |  |
| `VendorRefNumber` | Client Reference Number | This field is only editable when you create a one-time transaction. Enter the vendor reference number in this field. | Text | Global |  | `payment_transaction.VendorRefNumber · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Payment Transaction ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `payment_transaction.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `payment_transaction.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `payment_transaction.ModifiedDate · TEXT` |  |

## What points here (4 keys)

| Record type | Via column |
|---|---|
| [LinkLandlordInvPaymentTxn](LinkLandlordInvPaymentTxn.md) | `PaymentTransactionID` |
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `PaymentTransactionID` |
| [PaymentTransaction](PaymentTransaction.md) | `AppliedToPayTranID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `AppliedToPayTranID` |
