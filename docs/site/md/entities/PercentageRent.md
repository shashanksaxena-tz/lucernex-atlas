# PercentageRent

*45 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `percentage_rent`*

The percentage/sales-based rent clause on a retail lease — cap amount/frequency, audit-right flag, and billing frequency, linked to Covenant for cross-referencing compliance obligations tied to the same clause. 44 fields (41 Global, 3 Firm) under Contract; it is the clause-level configuration that VirtualSalesPeriod and PercentageRentBreakpoint project forward from.

Source: `data-fields/percentage-rent.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 45 |
| Catalogued fields | 44 (41 global, 3 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### 3 tenant custom columns

**Observed.** This record carries 3 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 3 catalogued Firm-scope fields

**Observed.** Of 44 catalogued fields on this record, 3 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-063](../rules/CON-R-063.md) | Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue. | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `RentYearStartMonth` | Rent Year Start Month | Dropdown | Global |  |  |

### Coded values (drop-downs) (10)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeCapFrequencyID` | Cap Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodePercentageRentTypeID` | Percentage Rent Type | Dropdown (Percentage Rent Type Code) | Global |  | Percentage Rent Type Code |
| `CodeProrationMethodID` | Proration Method | Dropdown (Proration Method Code) | Global |  | Proration Method Code |
| `CodeReportingFrequencyID` | Reporting Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |
| `CodeStoreTypeID` | Store Type | Dropdown (Store Type Code) | Global |  | Store Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapAmount` | Cap Amount | Currency | Global |  |  |
| `FloorAmount` | Floor Amount | Currency | Global |  |  |
| `OffsetAmount` | Offset Amount | Currency | Global |  |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AnnualPaymentDueDays` | Last Payment Due Offset Days | Number | Global |  |  |
| `AnnualReportDueDays` | Annual Report Due Days | Number | Global |  |  |
| `PercentageRentID` | Percentage Rent RecID | Number | Global |  |  |
| `PeriodPaymentDueDays` | Period Payment Due Offset Days | Number | Global |  |  |
| `PeriodReportDueDays` | Period Report Due Days | Number | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `DueDate` | Due Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `SalesYearEndDate` | Sales Year End Date | Date | Global |  |  |

### Flags (10)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AnnualizeRent` | Annualize Rent | Boolean | Global |  |  |
| `AuditRightFlag` | Audit Right? | Boolean | Global |  |  |
| `CumulativeFlag` | Cumulative? | Boolean | Global |  |  |
| `ExtFinalPeriodToLeaseExpDt` | Extend Final Period to Lease Expiration Date | Boolean | Global |  |  |
| `Firm_CertifiedSales` | Certified Sales | Boolean | Firm |  |  |
| `IsMidMonth` | Is Mid Month? | Boolean | Global |  |  |
| `IsPartialTerm` | Is Partial Term? | Boolean | Global |  |  |
| `NaturalBreakpointFlag` | Natural Breakpoint? | Boolean | Global |  |  |
| `UseCountBasedRate` | Use Count Based Rate? | Boolean | Global |  |  |
| `UseTrailing12MonthSales` | Use Trailing #12 Month Sales? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `Firm_PercentRentDocument` | Document | Text | Firm |  |  |
| `Firm_PercentRentPage` | Page | Text | Firm |  |  |
| `Notes` |  | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Percentage Rent ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [PaymentTransaction](PaymentTransaction.md) | `PercentageRentID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `PercentageRentID` |
