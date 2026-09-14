# PaymentTransactionFullImport

*118 fields · module: Lease Accounting & Payments · Postgres: `none exported`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 118 declared fields, filed under Lease Accounting & Payments, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 118 |
| Catalogued fields | not in the catalogue |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 13 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-124](../rules/CON-R-124.md) | Bulk payments are imported: PaymentTransactionFullImport mirrors PaymentTransaction's 118 fields with no backing table of its own. | Observed |
| [TAX-R-010](../rules/TAX-R-010.md) | Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit in this family. | Observed |

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AlternateRentScheduleID` |  | Alternate Rent Schedule ID | — |  | [AlternateRentSchedule](AlternateRentSchedule.md) |
| `AppliedToPayTranID` |  | Payment Transaction ID | — |  | [PaymentTransaction](PaymentTransaction.md) |
| `AssetID` |  | Equipment ID | — |  | [Asset](Asset.md) |
| `AssociatedDocumentID` |  | Document ID | — |  | [Document](Document.md) |
| `ContractID` |  | Contract ID | — |  | [Contract](Contract.md) |
| `ExpenseSetupID` |  | Expense Setup ID | — |  | [ExpenseSetup](ExpenseSetup.md) |
| `FolderID` |  | Folder ID | — |  | [Folder](Folder.md) |
| `OrganizationID` |  | Organization ID | — |  | [Organization](Organization.md) |
| `PercentageRentID` |  | Percentage Rent ID | — |  | [PercentageRent](PercentageRent.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `PropertyTaxBillID` |  | Property Tax Bill ID | — |  | [PropertyTaxBill](PropertyTaxBill.md) |
| `VendorID` |  | Employer ID | — |  | [Employer](Employer.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` |  | Entity | — |  |  |
| `DocumentIDList` |  | Document List | — |  |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeApprovalStatusID` |  | Dropdown (Approval Status Code) | — |  | Approval Status Code |
| `CodeCheckCurrencyTypeID` |  | Dropdown (Currency Type Code) | — |  | Currency Type Code |
| `CodeCurrencyTypeID` |  | Dropdown (Currency Type Code) | — |  | Currency Type Code |
| `CodeExpenseCategoryID` |  | Dropdown (Expense Category Code) | — |  | Expense Category Code |
| `CodeExpenseGroupID` |  | Dropdown (Expense Group Code) | — |  | Expense Group Code |
| `CodeExpenseTypeID` |  | Dropdown (Expense Type Code) | — |  | Expense Type Code |
| `CodePaymentMethodID` |  | Dropdown (Payment Method Code) | — |  | Payment Method Code |
| `CodeSourceEntityID` |  | Dropdown (Source Entity Code) | — |  | Source Entity Code |

### Money (25)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AgingAmountForMonth1` |  | Currency | — |  |  |
| `AgingAmountForMonth2` |  | Currency | — |  |  |
| `AgingAmountForMonth3` |  | Currency | — |  |  |
| `AgingAmountRemainder` |  | Currency | — |  |  |
| `AmountAllocated` |  | Currency | — |  |  |
| `AmountNotAllocated` |  | Currency | — |  |  |
| `CheckAmount` |  | Currency | — |  |  |
| `ClientAmount1` |  | Currency | — |  |  |
| `ClientAmount2` |  | Currency | — |  |  |
| `ClientAmount3` |  | Currency | — |  |  |
| `DueDateAgingAmountForMonth1` |  | Currency | — |  |  |
| `DueDateAgingAmountForMonth2` |  | Currency | — |  |  |
| `DueDateAgingAmountForMonth3` |  | Currency | — |  |  |
| `DueDateAgingAmountRemainder` |  | Currency | — |  |  |
| `FreightAmount` |  | Currency | — |  |  |
| `InvoiceAmount` |  | Currency | — |  |  |
| `InvoiceAmountAllocated` |  | Currency | — |  |  |
| `InvoiceAmountNotAllocated` |  | Currency | — |  |  |
| `MiscAmount` |  | Currency | — |  |  |
| `PreAltRentInvoiceAmount` |  | Currency | — |  |  |
| `TaxAmount1` |  | Currency | — |  |  |
| `TaxAmount2` |  | Currency | — |  |  |
| `TaxAmount3` |  | Currency | — |  |  |
| `TaxAmount4` |  | Currency | — |  |  |
| `TotalAmount` |  | Currency | — |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PaymentTransactionID` |  | Number | — |  |  |

### Dates & timestamps (12)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillingDate` |  | Date | — |  |  |
| `CheckDate` |  | Date | — |  |  |
| `ClientDate1` |  | Date | — |  |  |
| `ClientDate2` |  | Date | — |  |  |
| `ClientDate3` |  | Date | — |  |  |
| `CoverageBeginDate` |  | Date | — |  |  |
| `CoverageEndDate` |  | Date | — |  |  |
| `DueDate` |  | Date | — |  |  |
| `EffectiveDate` |  | Date | — |  |  |
| `InvoiceDate` |  | Date | — |  |  |
| `LastApprovalChangeDate` |  | Date | — |  |  |
| `PostingDate` |  | Date | — |  |  |

### Flags (10)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ConfirmedFlag` |  | Boolean | — |  |  |
| `CreditFlag` |  | Boolean | — |  |  |
| `HoldFlag` |  | Boolean | — |  |  |
| `InAlternateRent` |  | Boolean | — |  |  |
| `IsInvoiceReconciled` |  | Boolean | — |  |  |
| `IsReceivable` |  | Boolean | — |  |  |
| `OneTimeFlag` |  | Boolean | — |  |  |
| `PrepaidFlag` |  | Boolean | — |  |  |
| `ProcessedFlag` |  | Boolean | — |  |  |
| `TaxesIncludedFlag` |  | Boolean | — |  |  |

### Text & notes (45)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `APExportBaseNumber` |  | Text | — |  |  |
| `APExportPrepaidNumber` |  | Text | — |  |  |
| `APExportTax1Number` |  | Text | — |  |  |
| `APExportTax2Number` |  | Text | — |  |  |
| `APExportTax3Number` |  | Text | — |  |  |
| `APExportTax4Number` |  | Text | — |  |  |
| `AccountNumber1` |  | Text | — |  |  |
| `AccountNumber2` |  | Text | — |  |  |
| `AccountNumber3` |  | Text | — |  |  |
| `AccountNumber4` |  | Text | — |  |  |
| `AccountNumber5` |  | Text | — |  |  |
| `AccountNumber6` |  | Text | — |  |  |
| `AccountNumber7` |  | Text | — |  |  |
| `AccountNumber8` |  | Text | — |  |  |
| `AmountInvoiced` |  | Text | — |  |  |
| `AmountReceived` |  | Text | — |  |  |
| `BankAccountNumber` |  | Text | — |  |  |
| `BankRoutingNumber` |  | Text | — |  |  |
| `BaseName` |  | Text | — |  |  |
| `CheckNumber` |  | Text | — |  |  |
| `ClientText1` |  | Text | — |  |  |
| `ClientText2` |  | Text | — |  |  |
| `ClientText3` |  | Text | — |  |  |
| `Description` |  | Text | — |  |  |
| `ExpAccrualAcct1Number` |  | Text | — |  |  |
| `ExpAccrualAcct2Number` |  | Text | — |  |  |
| `ExpAccrualAcct3Number` |  | Text | — |  |  |
| `ExpAccrualAcct4Number` |  | Text | — |  |  |
| `ExpenseRecoveryID` |  | Text | — |  |  |
| `ExportBatchNumber` |  | Text | — |  |  |
| `InternalRefNumber` |  | Text | — |  |  |
| `InvoiceNumber` |  | Text | — |  |  |
| `Notes` |  | Text | — |  |  |
| `PercentRentAccrualAcct1Number` |  | Text | — |  |  |
| `PercentRentAccrualAcct2Number` |  | Text | — |  |  |
| `PercentRentAccrualAcct3Number` |  | Text | — |  |  |
| `PercentRentAccrualAcct4Number` |  | Text | — |  |  |
| `RETaxAccrualAcct1Number` |  | Text | — |  |  |
| `RETaxAccrualAcct2Number` |  | Text | — |  |  |
| `RETaxAccrualAcct3Number` |  | Text | — |  |  |
| `RETaxAccrualAcct4Number` |  | Text | — |  |  |
| `RemitMessage` |  | Text | — |  |  |
| `ScheduledOffsetID` |  | Text | — |  |  |
| `SourceEntityTable` |  | Text | — |  |  |
| `VendorRefNumber` |  | Text | — |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` |  | Text | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
