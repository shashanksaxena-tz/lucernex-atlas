# PercentageRent

*45 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `percentage_rent`*

The percentage/sales-based rent clause on a retail lease — cap amount/frequency, audit-right flag, and billing frequency, linked to Covenant for cross-referencing compliance obligations tied to the same clause. 44 fields (41 Global, 3 Firm) under Contract; it is the clause-level configuration that VirtualSalesPeriod and PercentageRentBreakpoint project forward from.

Source: `data-fields/percentage-rent.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 45 |
| Fields with a vendor definition | 37 of 47 inventoried |
| Physical tables | `percentage_rent` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in percentage_rent

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 37 fields carry a vendor definition

**Observed.** 37 of this record's 47 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 44 comparable

**Observed.** Over the 44 fields both captures contain, they agree on 43. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-063](../rules/CON-R-063.md) | Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue. | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `percentage_rent.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `percentage_rent.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `percentage_rent.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `percentage_rent.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `RentYearStartMonth` | Rent Year Start Month | Select the start month of the rent year from this field. | Dropdown | Global |  | `percentage_rent.RentYearStartMonth · TEXT` |  |

### Coded values (drop-downs) (10)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | The Payment Frequency field controls how often you can generate rent or generate payments. Select the payment frequency from this field. | Dropdown (Frequency Code) | Global |  | `percentage_rent.CodeBillingFrequencyID · TEXT` | Frequency Code |
| `CodeCapFrequencyID` | Cap Frequency | Select the frequency that the cap should be applied from this field. For example, if you had a max cap of $100,000.00, the cap frequency could determine whether that cap is applied monthly, quarterly, or annually. If no cap frequency is specified, the cap amount is assumed to be the amount that applies for each percentage rent payment period. So, for example, if percentage rent is paid monthly and a $500 cap is specified, the system assumes that the cap is applied monthly if the frequency is not set. | Dropdown (Frequency Code) | Global |  | `percentage_rent.CodeCapFrequencyID · TEXT` | Frequency Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `percentage_rent.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `percentage_rent.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `percentage_rent.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodePercentageRentTypeID` | Percentage Rent Type | Select the percentage rent calculation method from this field. For more information about the available calculation methods, please see the Lx Online Help. | Dropdown (Percentage Rent Type Code) | Global |  | `percentage_rent.CodePercentageRentTypeID · TEXT` | Percentage Rent Type Code |
| `CodeProrationMethodID` | Proration Method |  | Dropdown (Proration Method Code) | Global |  | `percentage_rent.CodeProrationMethodID · TEXT` | Proration Method Code |
| `CodeReportingFrequencyID` | Reporting Frequency | Select the reporting frequency for this record. | Dropdown (Frequency Code) | Global |  | `percentage_rent.CodeReportingFrequencyID · TEXT` | Frequency Code |
| `CodeSalesGroupID` | Sales Group | Select the sales group that this percentage rent record will be associated with from this field. | Dropdown (Sales Group) | Global |  | `percentage_rent.CodeSalesGroupID · TEXT` | Sales Group |
| `CodeStoreTypeID` | Store Type | Select the store type from this field. | Dropdown (Store Type Code) | Global |  | `percentage_rent.CodeStoreTypeID · TEXT` | Store Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapAmount` | Cap Amount | Enter the maximum payment allowed in this field. | Currency | Global |  | `percentage_rent.CapAmount · TEXT` |  |
| `FloorAmount` | Floor Amount | Enter the minimum payment required in this field. | Currency | Global |  | `percentage_rent.FloorAmount · TEXT` |  |
| `OffsetAmount` | Offset Amount | The percentage rent offset amount. This field does not impact any calculations. | Currency | Global |  | `percentage_rent.OffsetAmount · TEXT` |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AnnualPaymentDueDays` | Last Payment Due Offset Days | Enter the annual payment due date in this field. | Number | Global |  | `percentage_rent.AnnualPaymentDueDays · TEXT` |  |
| `AnnualReportDueDays` | Annual Report Due Days | Enter the annual reporting due date in this field. | Number | Global |  | `percentage_rent.AnnualReportDueDays · TEXT` |  |
| `PercentageRentID` | Percentage Rent RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `percentage_rent.PercentageRentID · VARCHAR(64) NOT NULL` |  |
| `PeriodPaymentDueDays` | Period Payment Due Offset Days | Enter the period payment due date in this field. | Number | Global |  | `percentage_rent.PeriodPaymentDueDays · TEXT` |  |
| `PeriodReportDueDays` | Period Report Due Days | Enter the period reporting due date in this field. | Number | Global |  | `percentage_rent.PeriodReportDueDays · TEXT` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `percentage_rent.BeginDate · TEXT` |  |
| `DueDate` | Due Date | Enter the due date for the rent schedule in this field. This field does not impact any calculations. | Date | Global |  | `percentage_rent.DueDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `percentage_rent.EndDate · TEXT` |  |
| `SalesYearEndDate` | Sales Year End Date | The end date of the sales year. | Date | Global |  | `percentage_rent.SalesYearEndDate · TEXT` |  |

### Flags (10)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AnnualizeRent` | Annualize Rent |  | Boolean | Global |  | `percentage_rent.AnnualizeRent · TEXT` |  |
| `AuditRightFlag` | Audit Right? | Select this check box if your landlord has the right to audit your percentage rent. | Boolean | Global |  | `percentage_rent.AuditRightFlag · TEXT` |  |
| `CumulativeFlag` | Cumulative? | This flag indicates whether the percentage rent is cumulative or not. This flag does not have any associated functionality. | Boolean | Global |  | `percentage_rent.CumulativeFlag · TEXT` |  |
| `ExtFinalPeriodToLeaseExpDt` | Extend Final Period to Lease Expiration Date |  | Boolean | Global |  | `percentage_rent.ExtFinalPeriodToLeaseExpDt · TEXT` |  |
| `Firm_CertifiedSales` | Certified Sales |  | Boolean | Firm |  | `percentage_rent.Firm_CertifiedSales · TEXT` |  |
| `IsMidMonth` | Is Mid Month? |  | Boolean | Global |  | `percentage_rent.IsMidMonth · TEXT` |  |
| `IsPartialTerm` | Is Partial Term? | Select this check box if the term length is greater than 12 months but less than 2 years. For example, a 15-month term. | Boolean | Global |  | `percentage_rent.IsPartialTerm · TEXT` |  |
| `NaturalBreakpointFlag` | Natural Breakpoint? | Select the appropriate option button for one of three percentage rent breakpoint types: Natural Breakpoint, Artificial Breakpoint, or Count Based Rate. For more information about these breakpoint types, please see the Lx Online Help. | Boolean | Global |  | `percentage_rent.NaturalBreakpointFlag · TEXT` |  |
| `UseCountBasedRate` | Use Count Based Rate? | This setting causes count-based rates to be used in calculating breakpoint rates. | Boolean | Global |  | `percentage_rent.UseCountBasedRate · TEXT` |  |
| `UseTrailing12MonthSales` | Use Trailing #12 Month Sales? | Select this check box if you want to use a full 12 months of sales and your annual breakpoint to calculate the prorated amount due, even if the full 12 months is not within the same fiscal year. | Boolean | Global |  | `percentage_rent.UseTrailing12MonthSales · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `percentage_rent.Description · TEXT` |  |
| `Firm_PercentRentDocument` | Document |  | Text | Firm |  | `percentage_rent.Firm_PercentRentDocument · TEXT` |  |
| `Firm_PercentRentPage` | Page |  | Text | Firm |  | `percentage_rent.Firm_PercentRentPage · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `percentage_rent.Notes · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `percentage_rent.Section · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Percentage Rent ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `percentage_rent.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `percentage_rent.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `percentage_rent.ModifiedDate · TEXT` |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [PaymentTransaction](PaymentTransaction.md) | `PercentageRentID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `PercentageRentID` |
