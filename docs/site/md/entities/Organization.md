# Organization

*17 fields · module: Platform & Tenancy · Postgres: `organization`*

A broader organizational entity (parent company, franchise group) above Employer — up to several numbered Account Number slots mirroring the financial entities' split-coding pattern. 17 Global fields under Company Items.

Source: `data-fields/organization.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 17 |
| Catalogued fields | 17 (17 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 8 keys from 8 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-111](../rules/CON-R-111.md) | Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved. | Inferred |

## Fields

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeOrganizationCategoryID` | Organization Category | Dropdown (Org Category Code) | Global |  | Org Category Code |
| `CodeOrganizationGroupID` | Organization Group | Dropdown (Org Group Code) | Global |  | Org Group Code |
| `CodeOrganizationTypeID` | Organization Type | Dropdown (Org Type Code) | Global |  | Org Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `OrganizationID` | Organization RecID | Number | Global |  |  |

### Text & notes (10)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccountNumber1` | Account Number #1 | Text | Global |  |  |
| `AccountNumber2` | Account Number #2 | Text | Global |  |  |
| `AccountNumber3` | Account Number #3 | Text | Global |  |  |
| `AccountNumber4` | Account Number #4 | Text | Global |  |  |
| `AccountNumber5` | Account Number #5 | Text | Global |  |  |
| `AccountNumber6` | Account Number #6 | Text | Global |  |  |
| `AccountNumber7` | Account Number #7 | Text | Global |  |  |
| `AccountNumber8` | Account Number #8 | Text | Global |  |  |
| `OrganizationName` | Organization Name | Text | Global | yes |  |
| `PortfolioIDList` | Portfolio Access | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Organization ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (8 keys)

| Record type | Via column |
|---|---|
| [AccrualTransaction](AccrualTransaction.md) | `OrganizationID` |
| [Contract](Contract.md) | `OrganizationID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `OrganizationID` |
| [Location](Location.md) | `OrganizationID` |
| [Parcel](Parcel.md) | `OrganizationID` |
| [PaymentTransaction](PaymentTransaction.md) | `OrganizationID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `OrganizationID` |
| [Tenant](Tenant.md) | `OrganizationID` |
