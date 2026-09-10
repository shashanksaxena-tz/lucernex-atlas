# AccrualTransaction — Data Fields

An individual expense-accrual posting tied to a contract, carrying up to eight parallel Account Number fields for GL split coding, matching the same allocation pattern seen in PaymentTransaction. 54 Global fields under Contract.

**Table Association:** `AccrualTransaction` &nbsp;·&nbsp; **Total fields:** 54 (Global: 54, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| AP Export Base Number | `APExportBaseNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| AP Export Prepaid Number | `APExportPrepaidNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #1 | `AccountNumber1` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #2 | `AccountNumber2` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #3 | `AccountNumber3` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #4 | `AccountNumber4` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #5 | `AccountNumber5` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #6 | `AccountNumber6` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #7 | `AccountNumber7` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Account Number #8 | `AccountNumber8` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Accrual Message | `AccrualMessage` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Accrual Transaction ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Accrual Transaction |
| Accrual Transaction RecID | `AccrualTransactionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Accrual Transaction |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Accrual Transaction |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Accrual Transaction |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Accrual Transaction |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Accrual Transaction |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Exp Accrual Acct #1 Number | `ExpAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Exp Accrual Acct #2 Number | `ExpAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Exp Accrual Acct #3 Number | `ExpAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Exp Accrual Acct #4 Number | `ExpAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Expense Accrual Setup | `ExpenseAccrualSetupID` | `sTYPE_EXPENSE_ACCRUAL_SETUP` | Global | No | No |  | Contract / Accrual Transaction |
| Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Accrual Transaction |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Accrual Transaction |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Accrual Transaction |
| Hold? | `HoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Accrual Transaction |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Accrual Transaction |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Accrual Transaction |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Accrual Transaction |
| Organization | `OrganizationID` | `sTYPE_ORGANIZATION` | Global | No | No |  | Contract / Accrual Transaction |
| Percent Rent Accrual Acct #1 | `PercentRentAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Percent Rent Accrual Acct #2 | `PercentRentAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Percent Rent Accrual Acct #3 | `PercentRentAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Percent Rent Accrual Acct #4 | `PercentRentAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Period Amount | `PeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accrual Transaction |
| Period Begin Date | `PeriodBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Accrual Transaction |
| Period End Date | `PeriodEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Accrual Transaction |
| Period Number | `PeriodNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Accrual Transaction |
| Period Year | `PeriodYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Accrual Transaction |
| Posting Date | `PostingDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Accrual Transaction |
| Processed? | `ProcessedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Accrual Transaction |
| RE Tax Accrual Acct #1 | `RETaxAccrualAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| RE Tax Accrual Acct #2 | `RETaxAccrualAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| RE Tax Accrual Acct #3 | `RETaxAccrualAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| RE Tax Accrual Acct #4 | `RETaxAccrualAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Accrual Transaction |
| Source Entity Table | `SourceEntityTable` | `sTYPE_TEXT` | Global | No | No |  | Contract / Accrual Transaction |
| Tax Amount #1 | `TaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accrual Transaction |
| Tax Amount #2 | `TaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accrual Transaction |
| Tax Amount #3 | `TaxAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accrual Transaction |
| Tax Amount #4 | `TaxAmount4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accrual Transaction |
| Taxes Included In Amount? | `TaxesIncludedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Accrual Transaction |
| Total Amount | `TotalAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accrual Transaction |
