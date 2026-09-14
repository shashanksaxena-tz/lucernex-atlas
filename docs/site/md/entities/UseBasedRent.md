# UseBasedRent

*23 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `use_based_rent`*

The usage-based rent clause header (e.g., per-unit, per-transaction rent) — billing frequency and currency type, the clause-level record UseBasedRentBreakpoint and VirtualUseBasedRentPeriod project from. 22 Global fields under Contract.

Source: `data-fields/use-based-rent.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Fields with a vendor definition | 22 of 23 inventoried |
| Physical tables | `use_based_rent` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 22 (22 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in use_based_rent

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 22 fields carry a vendor definition

**Observed.** 22 of this record's 23 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 22 comparable

**Observed.** Over the 22 fields both captures contain, they agree on 21. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `use_based_rent.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `use_based_rent.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `use_based_rent.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `use_based_rent.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `RentYearStartMonth` | Rent Year Start Month | Select the start month of the rent year from this field. | Dropdown | Global |  | `use_based_rent.RentYearStartMonth · TEXT` |  |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | The Payment Frequency field controls how often you can generate rent or generate payments. Select the payment frequency from this field. | Dropdown (Frequency Code) | Global |  | `use_based_rent.CodeBillingFrequencyID · TEXT` | Frequency Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `use_based_rent.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `use_based_rent.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `use_based_rent.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodeReportingFrequencyID` | Reporting Frequency | Select the reporting frequency for this record. | Dropdown (Frequency Code) | Global |  | `use_based_rent.CodeReportingFrequencyID · TEXT` | Frequency Code |
| `CodeUsageGroupID` | Usage Group | Select the usage group from this field. A Usage Group will be used with one and only one Model Type. The model type of a usage group will impact how your use based rent is calculated. | Dropdown (Usage Group Code) | Global |  | `use_based_rent.CodeUsageGroupID · TEXT` | Usage Group Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | This field can be used to create custom unit types for count-based usage groups. | Dropdown (Usage Unit Type Code) | Global |  | `use_based_rent.CodeUsageUnitTypeID · TEXT` | Usage Unit Type Code |
| `CodeUseRentModelTypeID` | Model Type | The Model Type field allows you to select the model type to associate with a usage group. A Usage Group will be used with one and only one Model Type. If you have use-based rent that involves both model types, then create different usage groups for each model type. When you select the Count Based model type, the rent will be calculated as the Unit Resource Rent Rate * the Number of Units Used by the Lessee. When you select the Share Based model type, the rent will be calculated as the Shared Resource Rent Rate * the Lessee Share. | Dropdown (Use Rent Model Type Code) | Global | yes | `use_based_rent.CodeUseRentModelTypeID · TEXT` | Use Rent Model Type Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodPaymentDueDays` | Period Payment Due Days | Enter the payment due date in this field. | Number | Global |  | `use_based_rent.PeriodPaymentDueDays · TEXT` |  |
| `PeriodReportDueDays` | Period Report Due Days | Enter the reporting due date in this field. | Number | Global |  | `use_based_rent.PeriodReportDueDays · TEXT` |  |
| `UseBasedRentID` | Use Based Rent RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `use_based_rent.UseBasedRentID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `use_based_rent.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `use_based_rent.EndDate · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `use_based_rent.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `use_based_rent.Notes · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Use Based Rent ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `use_based_rent.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `use_based_rent.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `use_based_rent.ModifiedDate · TEXT` |  |
