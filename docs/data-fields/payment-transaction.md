# PaymentTransaction — Data Fields

Individual rent/expense payment or receipt records against a contract — up to eight parallel 'Account Number #N' fields for split GL coding, allocation amounts, and payment dates. 118 fields, all Global. The repeated-numbered-field pattern (Account Number #1 through #8) is common across the financial entities in this catalog and indicates Lucernex models multi-line allocation as fixed parallel columns rather than a normalized child table exposed to this catalog.

**Table Association:** `PaymentTransaction` &nbsp;·&nbsp; **Total fields:** 118 (Global: 118, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| AP Export Base Number | `APExportBaseNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| AP Export Prepaid Number | `APExportPrepaidNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| AP Export Tax #1 | `APExportTax1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| AP Export Tax #2 | `APExportTax2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| AP Export Tax #3 | `APExportTax3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| AP Export Tax #4 | `APExportTax4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #1 | `AccountNumber1` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #2 | `AccountNumber2` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #3 | `AccountNumber3` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #4 | `AccountNumber4` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #5 | `AccountNumber5` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #6 | `AccountNumber6` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #7 | `AccountNumber7` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Account Number #8 | `AccountNumber8` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Alternate Rent Schedule | `AlternateRentScheduleID` | `sTYPE_ALTERNATE_RENT_SCHEDULE` | Global | No | No |  | Contract / Payment Transaction |
| Amount Allocated | `AmountAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Amount Invoiced | `AmountInvoiced` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Amount Not Allocated | `AmountNotAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Amount Received | `AmountReceived` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Applied to Transaction | `AppliedToPayTranID` | `sTYPE_PAYMENT_TRANSACTION` | Global | No | No |  | Contract / Payment Transaction |
| Approval Status | `CodeApprovalStatusID` | `sCODE_APPROVAL_STATUS` | Global | No | No |  | Contract / Payment Transaction |
| Associated Document | `AssociatedDocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Payment Transaction |
| Bank Account Number | `BankAccountNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Bank Routing Number | `BankRoutingNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Billing Date | `BillingDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Check Amount | `CheckAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Check Currency Type | `CodeCheckCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Payment Transaction |
| Check Date | `CheckDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Check Number | `CheckNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Client Amount #1 | `ClientAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Client Amount #2 | `ClientAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Client Amount #3 | `ClientAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Client Date #1 | `ClientDate1` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Client Date #2 | `ClientDate2` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Client Date #3 | `ClientDate3` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Client Reference Number | `VendorRefNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Client Text #1 | `ClientText1` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Payment Transaction |
| Client Text #2 | `ClientText2` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Payment Transaction |
| Client Text #3 | `ClientText3` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Payment Transaction |
| Confirmed? | `ConfirmedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Payment Transaction |
| Coverage Begin Date | `CoverageBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Coverage End Date | `CoverageEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Credit? | `CreditFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Payment Transaction |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Documents | `DocumentIDList` | `sTYPE_DOCUMENT_LIST` | Global | No | No |  | Contract / Payment Transaction |
| Due Date | `DueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Equipment | `AssetID` | `sTYPE_EQUIPMENT` | Global | No | No |  | Contract / Payment Transaction |
| Equipment Associated Entity | `AssetAssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Contract / Payment Transaction |
| Expense Accrual Acct #1 | `ExpAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Expense Accrual Acct #2 | `ExpAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Expense Accrual Acct #3 | `ExpAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Expense Accrual Acct #4 | `ExpAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Payment Transaction |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Payment Transaction |
| Expense Recovery | `ExpenseRecoveryID` | `sTYPE_EXPENSE_RECOVERY` | Global | No | No |  | Contract / Payment Transaction |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | No | No |  | Contract / Payment Transaction |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Payment Transaction |
| Export Batch Number | `ExportBatchNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| File Name | `BaseName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Folder | `FolderID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Payment Transaction |
| Freight Amount | `FreightAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Hold? | `HoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| In Alternate Rent? | `InAlternateRent` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Payment Transaction |
| Internal Reference Number | `InternalRefNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Invoice Amount | `InvoiceAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Invoice Amount Allocated | `InvoiceAmountAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Invoice Amount Not Allocated | `InvoiceAmountNotAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Invoice Date | `InvoiceDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Invoice Number | `InvoiceNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Is Invoice Reconciled? | `IsInvoiceReconciled` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Payment Transaction |
| Is Receivable? | `IsReceivable` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| Last Approval Change Date | `LastApprovalChangeDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Misc Amount | `MiscAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Payment Transaction |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Payment Transaction |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Payment Transaction |
| One Time? | `OneTimeFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| Organization | `OrganizationID` | `sTYPE_ORGANIZATION` | Global | No | No |  | Contract / Payment Transaction |
| Payment Method | `CodePaymentMethodID` | `sCODE_PAYMENT_METHOD` | Global | No | No |  | Contract / Payment Transaction |
| Payment Transaction ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Payment Transaction |
| Payment Transaction RecID | `PaymentTransactionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Payment Transaction |
| Percent Rent Accrual Acct #1 | `PercentRentAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Percent Rent Accrual Acct #2 | `PercentRentAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Percent Rent Accrual Acct #3 | `PercentRentAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Percent Rent Accrual Acct #4 | `PercentRentAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Percentage Rent | `PercentageRentID` | `sTYPE_PERCENTAGE_RENT` | Global | No | No |  | Contract / Payment Transaction |
| Posting Date | `PostingDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Payment Transaction |
| Pre-Alternate Rent Invoice Amount | `PreAltRentInvoiceAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Prepaid? | `PrepaidFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| Processed? | `ProcessedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| Property Tax Bill | `PropertyTaxBillID` | `sTYPE_PROPERTY_TAX_BILL` | Global | No | No |  | Contract / Payment Transaction |
| RE Tax Accrual Acct #1 | `RETaxAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| RE Tax Accrual Acct #2 | `RETaxAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| RE Tax Accrual Acct #3 | `RETaxAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| RE Tax Accrual Acct #4 | `RETaxAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Remit Message | `RemitMessage` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Scheduled Offset | `ScheduledOffsetID` | `sTYPE_SCHEDULED_OFFSET` | Global | No | No |  | Contract / Payment Transaction |
| Source Entity | `CodeSourceEntityID` | `sCODE_SOURCE_ENTITY` | Global | No | No |  | Contract / Payment Transaction |
| Source Entity Table | `SourceEntityTable` | `sTYPE_TEXT` | Global | No | No |  | Contract / Payment Transaction |
| Tax Amount #1 | `TaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Tax Amount #2 | `TaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Tax Amount #3 | `TaxAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Tax Amount #4 | `TaxAmount4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Taxes Included In Amount? | `TaxesIncludedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount | `TotalAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (0-30 days) | `AgingAmountForMonth1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (31-60 days) | `AgingAmountForMonth2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (61-90 days) | `AgingAmountForMonth3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (Due Date 0-30 days) | `DueDateAgingAmountForMonth1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (Due Date 31-60 days) | `DueDateAgingAmountForMonth2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (Due Date 61-90 days) | `DueDateAgingAmountForMonth3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (Due Date over 90 days) | `DueDateAgingAmountRemainder` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Total Amount (over 90 days) | `AgingAmountRemainder` | `sTYPE_MONEY` | Global | No | No |  | Contract / Payment Transaction |
| Vendor | `VendorID` | `sTYPE_VENDOR` | Global | No | No |  | Contract / Payment Transaction |
| Effective End Date | `EffectiveEndDate` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
