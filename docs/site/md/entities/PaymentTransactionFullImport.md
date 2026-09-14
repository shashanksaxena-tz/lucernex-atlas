# PaymentTransactionFullImport

*118 fields · module: Lease Accounting & Payments · Postgres: `none exported`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 118 declared fields, filed under Lease Accounting & Payments, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 113 of its 118 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 118 |
| Fields with a vendor definition | 113 of 118 inventoried |
| Physical tables | — |
| Replication database | — |
| Catalogued fields | not in the catalogue |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 13 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 113 fields carry a vendor definition

**Observed.** 113 of this record's 118 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### 118 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 118 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-124](../rules/CON-R-124.md) | Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own. | Observed |
| [TAX-R-010](../rules/TAX-R-010.md) | Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit in this family. | Observed |

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AlternateRentScheduleID` | Alternate Rent Schedule | The alternate rent schedule ID associated with the payment transaction. | Alternate Rent Schedule ID | — |  | not extracted | [AlternateRentSchedule](AlternateRentSchedule.md) |
| `AppliedToPayTranID` | Applied to Transaction | The payment transaction ID created when you apply a scheduled offset. | Payment Transaction ID | — |  | not extracted | [PaymentTransaction](PaymentTransaction.md) |
| `AssetID` | Equipment | The associated asset record ID. | Equipment ID | — |  | not extracted | [Asset](Asset.md) |
| `AssociatedDocumentID` | Associated Document | The ID of a document associated with this record. | Document ID | — |  | not extracted | [Document](Document.md) |
| `ContractID` |  | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | — |  | not extracted | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | The ExpenseSetupID field is used to associate a payment transaction with an expense setup record. | Expense Setup ID | — |  | not extracted | [ExpenseSetup](ExpenseSetup.md) |
| `FolderID` | Folder | The folder ID when you save a transaction to your documents. | Folder ID | — |  | not extracted | [Folder](Folder.md) |
| `OrganizationID` | Organization | Select the organization from which this payment should be debited from this field. | Organization ID | — |  | not extracted | [Organization](Organization.md) |
| `PercentageRentID` | Percentage Rent | The percentage rent record ID that the payment transaction is associated with. | Percentage Rent ID | — |  | not extracted | [PercentageRent](PercentageRent.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | not extracted | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxBillID` | Property Tax Bill | The ID of the property bill record associated with the transaction. This field is used in the Parcel module. | Property Tax Bill ID | — |  | not extracted | [PropertyTaxBill](PropertyTaxBill.md) |
| `VendorID` | Vendor | Select the vendor that this payment should be paid to from this field. | Employer ID | — |  | not extracted | [Employer](Employer.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | This is a reporting field that returns data about the asset associated with the entity. | Entity | — |  | not extracted |  |
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents a record. | Document List | — |  | not extracted |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeApprovalStatusID` | Approval Status | This field populates with the approval status of the transaction. A transaction must be approved from the Contract > Details > Summary page or the Equipment Contract > Details > Summary page. | Dropdown (Approval Status Code) | — |  | not extracted | Approval Status Code |
| `CodeCheckCurrencyTypeID` | Check Currency Type | Select the currency in which the check was written from the field. | Dropdown (Currency Type Code) | — |  | not extracted | Currency Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | — |  | not extracted | Currency Type Code |
| `CodeExpenseCategoryID` | Expense Category | The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the grandchildren of groups. | Dropdown (Expense Category Code) | — |  | not extracted | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | — |  | not extracted | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | — |  | not extracted | Expense Type Code |
| `CodePaymentMethodID` | Payment Method | Select the payment method from this field. | Dropdown (Payment Method Code) | — |  | not extracted | Payment Method Code |
| `CodeSourceEntityID` | Source Entity | This field is no longer used. | Dropdown (Source Entity Code) | — |  | not extracted | Source Entity Code |

### Money (25)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AgingAmountForMonth1` | Total Amount (0-30 days) | The total amount of the transaction if the effective date of the transaction was within the last 30 days. | Currency | — |  | not extracted |  |
| `AgingAmountForMonth2` | Total Amount (31-60 days) | The total amount of the transaction if the effective date of the transaction was within the last 60 days. | Currency | — |  | not extracted |  |
| `AgingAmountForMonth3` | Total Amount (61-90 days) | The total amount of the transaction if the effective date of the transaction was within the last 90 days. | Currency | — |  | not extracted |  |
| `AgingAmountRemainder` | Total Amount (over 90 days) | The total amount of the transaction if the effective date of the transaction was beyond the last 90 days. | Currency | — |  | not extracted |  |
| `AmountAllocated` | Amount Allocated | This field automatically calculates the amount that has been applied to transactions so far. | Currency | — |  | not extracted |  |
| `AmountNotAllocated` | Amount Not Allocated | This field automatically calculates the remaining balance of the received transaction. | Currency | — |  | not extracted |  |
| `CheckAmount` | Check Amount | Enter the check amount in this field. | Currency | — |  | not extracted |  |
| `ClientAmount1` | Client Amount #1 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Currency | — |  | not extracted |  |
| `ClientAmount2` | Client Amount #2 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Currency | — |  | not extracted |  |
| `ClientAmount3` | Client Amount #3 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Currency | — |  | not extracted |  |
| `DueDateAgingAmountForMonth1` | Total Amount (Due Date 0-30 days) | The total amount of the transaction if the due date or end date of the transaction was within the last 30 days. | Currency | — |  | not extracted |  |
| `DueDateAgingAmountForMonth2` | Total Amount (Due Date 31-60 days) | The total amount of the transaction if the due date or end date of the transaction was within the last 60 days. | Currency | — |  | not extracted |  |
| `DueDateAgingAmountForMonth3` | Total Amount (Due Date 61-90 days) | The total amount of the transaction if the due date or end date of the transaction was within the last 90 days. | Currency | — |  | not extracted |  |
| `DueDateAgingAmountRemainder` | Total Amount (Due Date over 90 days) | The total amount of the transaction if the due date or end date of the transaction was beyond the last 90 days. | Currency | — |  | not extracted |  |
| `FreightAmount` | Freight Amount | Enter any freight amounts that should be included in the transaction total in this field. | Currency | — |  | not extracted |  |
| `InvoiceAmount` | Invoice Amount | Enter the base amount of your invoice without taxes, freight, or miscellaneous costs. | Currency | — |  | not extracted |  |
| `InvoiceAmountAllocated` | Invoice Amount Allocated |  | Currency | — |  | not extracted |  |
| `InvoiceAmountNotAllocated` | Invoice Amount Not Allocated |  | Currency | — |  | not extracted |  |
| `MiscAmount` | Misc Amount | Enter any other amounts that should be included in the transaction total in this field. | Currency | — |  | not extracted |  |
| `PreAltRentInvoiceAmount` | Pre-Alternate Rent Invoice Amount | The amount that would be paid prior to applying the alternate rent amount. | Currency | — |  | not extracted |  |
| `TaxAmount1` | Tax Amount #1 | Enter the primary tax amount in currency in this field. | Currency | — |  | not extracted |  |
| `TaxAmount2` | Tax Amount #2 | Enter the secondary tax amount in currency in this field. | Currency | — |  | not extracted |  |
| `TaxAmount3` | Tax Amount #3 | Enter the third tax amount in currency in this field. | Currency | — |  | not extracted |  |
| `TaxAmount4` | Tax Amount #4 | Enter the fourth tax amount in currency in this field. | Currency | — |  | not extracted |  |
| `TotalAmount` | Total Amount | This field will only be editable if the Taxes Included in Amount? flag is selected. The total amount is the base amount plus any taxes, freight amounts, or miscellaneous costs. | Currency | — |  | not extracted |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PaymentTransactionID` | Payment Transaction RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | not extracted |  |

### Dates & timestamps (12)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillingDate` | Billing Date | The billing date. | Date | — |  | not extracted |  |
| `CheckDate` | Check Date | Enter the check date in this field. | Date | — |  | not extracted |  |
| `ClientDate1` | Client Date #1 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Date | — |  | not extracted |  |
| `ClientDate2` | Client Date #2 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Date | — |  | not extracted |  |
| `ClientDate3` | Client Date #3 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Date | — |  | not extracted |  |
| `CoverageBeginDate` | Coverage Begin Date | This field will pre-populate with your payment begin date. | Date | — |  | not extracted |  |
| `CoverageEndDate` | Coverage End Date | This field will pre-populate with your payment end date. | Date | — |  | not extracted |  |
| `DueDate` | Due Date | Enter the date the payment is due in this field. | Date | — |  | not extracted |  |
| `EffectiveDate` | Effective Date | Enter the effective date of the transaction in this field. | Date | — |  | not extracted |  |
| `InvoiceDate` | Invoice Date | Enter the invoice date in this field. | Date | — |  | not extracted |  |
| `LastApprovalChangeDate` | Last Approval Change Date | The date when the Approval Status field changed from Approved to Review. | Date | — |  | not extracted |  |
| `PostingDate` | Posting Date | Enter the date the transaction going to be sent to the accounting system in this field. | Date | — |  | not extracted |  |

### Flags (10)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ConfirmedFlag` | Confirmed? | This is an information-only flag. | Boolean | — |  | not extracted |  |
| `CreditFlag` | Credit? | If this transaction is a credit item, select this check box. | Boolean | — |  | not extracted |  |
| `HoldFlag` | Hold? | If this transaction should be marked with a hold flag, select this check box. | Boolean | — |  | not extracted |  |
| `InAlternateRent` | In Alternate Rent? | This field returns as true if this payment transaction has a reference to an Alternate Rent Expense Schedule ID. | Boolean | — |  | not extracted |  |
| `IsInvoiceReconciled` | Is Invoice Reconciled? |  | Boolean | — |  | not extracted |  |
| `IsReceivable` | Is Receivable? | If this transaction is an accounts receivable item, select this check box. These items are also known as income items. | Boolean | — |  | not extracted |  |
| `OneTimeFlag` | One Time? | This flag indicates whether a transaction is a one-time expense or if it is a recurring expense. The one-time expense flag is not editable. | Boolean | — |  | not extracted |  |
| `PrepaidFlag` | Prepaid? | This is an information-only flag. | Boolean | — |  | not extracted |  |
| `ProcessedFlag` | Processed? | Once the transaction has been processed, select this check box. After you save changes, you cannot make any further changes. Do not select the Processed Flag check box unless you are certain you do not want to make any further changes. | Boolean | — |  | not extracted |  |
| `TaxesIncludedFlag` | Taxes Included In Amount? | Select this check box if taxes are included in the value you entered in the Base Amount field. The system will then subtract the tax amounts from the base amount, and the Total Amount field becomes editable. If you need to make changes to the value in the Total Amount field, you may now do so. | Boolean | — |  | not extracted |  |

### Text & notes (45)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `APExportBaseNumber` | AP Export Base Number | The account number for your expenses. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `APExportPrepaidNumber` | AP Export Prepaid Number | The account number for your prepaid expenses (if applicable). The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `APExportTax1Number` | AP Export Tax #1 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `APExportTax2Number` | AP Export Tax #2 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `APExportTax3Number` | AP Export Tax #3 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `APExportTax4Number` | AP Export Tax #4 | This field contains an account number for your accounts payable export taxes. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `AccountNumber1` | Account Number #1 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AccountNumber2` | Account Number #2 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AccountNumber3` | Account Number #3 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AccountNumber4` | Account Number #4 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AccountNumber5` | Account Number #5 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AccountNumber6` | Account Number #6 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AccountNumber7` | Account Number #7 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AccountNumber8` | Account Number #8 | This field contains an account number associated with the organization. You can edit these account numbers at the organization-level. | Text | — |  | not extracted |  |
| `AmountInvoiced` | Amount Invoiced |  | Text | — |  | not extracted |  |
| `AmountReceived` | Amount Received | This field automatically calculates the amount received by totalling the value of any receipts which have been reconciled against this transaction. | Text | — |  | not extracted |  |
| `BankAccountNumber` | Bank Account Number | Enter the bank account number in this field. Changing this value will change the approval status to Review. | Text | — |  | not extracted |  |
| `BankRoutingNumber` | Bank Routing Number | Enter the bank routing number in this field. Changing this value will change the approval status to Review. | Text | — |  | not extracted |  |
| `BaseName` | File Name | This field displays the file name of the file attached to the record. | Text | — |  | not extracted |  |
| `CheckNumber` | Check Number | Enter the payment/check reference number in this field. | Text | — |  | not extracted |  |
| `ClientText1` | Client Text #1 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Text | — |  | not extracted |  |
| `ClientText2` | Client Text #2 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Text | — |  | not extracted |  |
| `ClientText3` | Client Text #3 | This field is reserved for client use, since clients cannot add custom fields to the PaymentTransaction database table. | Text | — |  | not extracted |  |
| `Description` |  | Write a description of the record. | Text | — |  | not extracted |  |
| `ExpAccrualAcct1Number` | Expense Accrual Acct #1 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `ExpAccrualAcct2Number` | Expense Accrual Acct #2 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `ExpAccrualAcct3Number` | Expense Accrual Acct #3 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `ExpAccrualAcct4Number` | Expense Accrual Acct #4 | This field contains an account number for your expense accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `ExpenseRecoveryID` | Expense Recovery | The expense recovery record ID associated with the transaction. | Text | — |  | not extracted |  |
| `ExportBatchNumber` | Export Batch Number | The payment transaction batch number. This field is primarily used in integrations. | Text | — |  | not extracted |  |
| `InternalRefNumber` | Internal Reference Number | Enter the internal reference number, if you have one, in this field. | Text | — |  | not extracted |  |
| `InvoiceNumber` | Invoice Number | Enter the invoice number in this field. | Text | — |  | not extracted |  |
| `Notes` |  | Add any notes about the record. | Text | — |  | not extracted |  |
| `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | This field contains an account number for your percent rent accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level. | Text | — |  | not extracted |  |
| `RemitMessage` | Remit Message | Enter a remittance message in this field. This is the message that will appear on the memo line of a check. | Text | — |  | not extracted |  |
| `ScheduledOffsetID` | Scheduled Offset | The ID of the schedule offset record associated with the transaction. | Text | — |  | not extracted |  |
| `SourceEntityTable` | Source Entity Table | The record type used to generate the transaction so that a unique identifier can be created for the batch. For example, transactions generated by the Generate Rent action begin with the code RNT. | Text | — |  | not extracted |  |
| `VendorRefNumber` | Client Reference Number | This field is only editable when you create a one-time transaction. Enter the vendor reference number in this field. | Text | — |  | not extracted |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Payment Transaction ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | — | yes | not extracted |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | not extracted | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | not extracted |  |
