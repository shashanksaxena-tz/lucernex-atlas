# PropertyTaxSummary

*32 fields · module: Property Tax · Postgres: `property_tax_summary`*

The rollup of assessment amount/percent and billing frequency for a Parcel's property tax obligation across bills and appeals. 31 Global fields under Parcel.

Source: `data-fields/property-tax-summary.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Fields with a vendor definition | 31 of 32 inventoried |
| Physical tables | `property_tax_summary` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in property_tax_summary

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 31 fields carry a vendor definition

**Observed.** 31 of this record's 32 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 31 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 2 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-014](../rules/FAC-R-014.md) | Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: | Observed |
| [TAX-R-006](../rules/TAX-R-006.md) | Input: `ParcelID` on all six objects, `Required = Yes` on each. Effect: Every level is independently queryable by Parcel without walking the roll-up chain to `PropertyTaxSummary`; | Observed |
| [TAX-R-008](../rules/TAX-R-008.md) | Input: `PropertyTaxSummary.CodeExpenseGroupID`/`.CodeExpenseTypeID`, `PropertyTaxAppeal.CodeExpenseGroupID`/`.CodeExpenseTypeID`. Effect: Selecting an expense type/group on a property-tax record is a GL-routing decision, identical in mechan | Observed |
| [TAX-R-009](../rules/TAX-R-009.md) | Input: `PropertyTaxSummary.CodeRecoveryGroupID`/`.CodeRecoveryTypeID`. Effect: Ties this module directly into the CAM/expense-recovery engine (`../accounting/README.md`'s "out of scope but adjacent" list) — a tax summary is not just billed, | Observed |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ParcelID` | Parcel | The parcel ID of the parcel record that this property tax summary record is associated with. | Parcel ID | Global | yes | `property_tax_summary.ParcelID · TEXT` | [Parcel](Parcel.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `property_tax_summary.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `TaxAuthorityID` | Tax Authority | Select the tax authority from this field. | Employer ID | Global |  | `property_tax_summary.TaxAuthorityID · TEXT` | [Employer](Employer.md) |
| `VendorID` | Vendor | The ID of the vendor associated with this property tax. | Employer ID | Global |  | `property_tax_summary.VendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | The Payment Frequency field controls how often you can generate rent or generate payments. Select the payment frequency from this field. | Dropdown (Frequency Code) | Global |  | `property_tax_summary.CodeBillingFrequencyID · TEXT` | Frequency Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `property_tax_summary.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExpenseGroupID` | Expense Group | The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `property_tax_summary.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `property_tax_summary.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodePaymentFrequencyID` | Payment Frequency | Select how often you pay this tax from this field. | Dropdown (Frequency Code) | Global |  | `property_tax_summary.CodePaymentFrequencyID · TEXT` | Frequency Code |
| `CodePropertyTaxTypeID` | Property Tax Type | Select the type of tax from this field. Common examples include county, city, and state. | Dropdown (Property Tax Type Code) | Global |  | `property_tax_summary.CodePropertyTaxTypeID · TEXT` | Property Tax Type Code |
| `CodeRecoveryGroupID` | Recovery Group | Select the recovery group this tax should be associated with from this field. The recovery group and type you select will allow you to pull your property taxes into your expense recoveries. | Dropdown (Recovery Group Code) | Global |  | `property_tax_summary.CodeRecoveryGroupID · TEXT` | Recovery Group Code |
| `CodeRecoveryTypeID` | Recovery Type | Select the recovery type this tax should be associated with from this field. The recovery group and type you select will allow you to pull your property taxes into your expense recoveries. | Dropdown (Recovery Type Code) | Global |  | `property_tax_summary.CodeRecoveryTypeID · TEXT` | Recovery Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssessmentAmount` | Assessment Amount | The assessment amount. | Currency | Global |  | `property_tax_summary.AssessmentAmount · TEXT` |  |
| `EstimatedAccrualAmount` | Estimated Accrual Amount | The estimated accrual amount. | Currency | Global |  | `property_tax_summary.EstimatedAccrualAmount · TEXT` |  |
| `NetTaxAmount` | Net Tax Amount | The net tax amount. | Currency | Global |  | `property_tax_summary.NetTaxAmount · TEXT` |  |

### Rates & percentages (5)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssessmentPercent` | Assessment Percent | The assessment percentage. | Percentage | Global |  | `property_tax_summary.AssessmentPercent · TEXT` |  |
| `MillRate` | Mill Rate | The mill rate. | Percentage | Global |  | `property_tax_summary.MillRate · TEXT` |  |
| `NetTaxPercent` | Net Tax Percent | The net tax percentage. | Percentage | Global |  | `property_tax_summary.NetTaxPercent · TEXT` |  |
| `RatePer` | Rate Per | This field is not implemented. | Percentage | Global |  | `property_tax_summary.RatePer · TEXT` |  |
| `TaxRatePer` | Tax Rate Per | This field is not implemented. | Percentage | Global |  | `property_tax_summary.TaxRatePer · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PropertyTaxSummaryID` | Property Tax Summary RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `property_tax_summary.PropertyTaxSummaryID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TicklerDate` | Tickler Date | A Tickler Date is used in reporting to give notice that the expiration date is approaching. If your company uses tickler dates, enter the date in this field. There is no associated functionality with this field. | Date | Global |  | `property_tax_summary.TicklerDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `RightToAppeal` | Right To Appeal? | This flag indicates whether you have the right to appeal the property tax. | Boolean | Global |  | `property_tax_summary.RightToAppeal · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `property_tax_summary.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `property_tax_summary.Notes · TEXT` |  |
| `TaxAccountNumber` | Tax Account Number | Enter your tax account number in this field. | Text | Global |  | `property_tax_summary.TaxAccountNumber · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Summary ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `property_tax_summary.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `property_tax_summary.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `property_tax_summary.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `property_tax_summary.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `property_tax_summary.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `property_tax_summary.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `PropertyTaxSummaryID` |
