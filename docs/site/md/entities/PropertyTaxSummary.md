# PropertyTaxSummary

*32 fields · module: Property Tax · Postgres: `property_tax_summary`*

The rollup of assessment amount/percent and billing frequency for a Parcel's property tax obligation across bills and appeals. 31 Global fields under Parcel.

Source: `data-fields/property-tax-summary.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ParcelID` | Parcel | Parcel ID | Global | yes | [Parcel](Parcel.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `TaxAuthorityID` | Tax Authority | Employer ID | Global |  | [Employer](Employer.md) |
| `VendorID` | Vendor | Employer ID | Global |  | [Employer](Employer.md) |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBillingFrequencyID` | Billing Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodePaymentFrequencyID` | Payment Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodePropertyTaxTypeID` | Property Tax Type | Dropdown (Property Tax Type Code) | Global |  | Property Tax Type Code |
| `CodeRecoveryGroupID` | Recovery Group | Dropdown (Recovery Group Code) | Global |  | Recovery Group Code |
| `CodeRecoveryTypeID` | Recovery Type | Dropdown (Recovery Type Code) | Global |  | Recovery Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssessmentAmount` | Assessment Amount | Currency | Global |  |  |
| `EstimatedAccrualAmount` | Estimated Accrual Amount | Currency | Global |  |  |
| `NetTaxAmount` | Net Tax Amount | Currency | Global |  |  |

### Rates & percentages (5)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssessmentPercent` | Assessment Percent | Percentage | Global |  |  |
| `MillRate` | Mill Rate | Percentage | Global |  |  |
| `NetTaxPercent` | Net Tax Percent | Percentage | Global |  |  |
| `RatePer` | Rate Per | Percentage | Global |  |  |
| `TaxRatePer` | Tax Rate Per | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PropertyTaxSummaryID` | Property Tax Summary RecID | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TicklerDate` | Tickler Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `RightToAppeal` | Right To Appeal? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `TaxAccountNumber` | Tax Account Number | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Property Tax Summary ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `PropertyTaxSummaryID` |
