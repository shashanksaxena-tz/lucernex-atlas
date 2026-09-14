# Organization

*17 fields · module: Platform & Tenancy · Postgres: `organization`*

A broader organizational entity (parent company, franchise group) above Employer — up to several numbered Account Number slots mirroring the financial entities' split-coding pattern. 17 Global fields under Company Items.

Source: `data-fields/organization.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 17 |
| Fields with a vendor definition | 17 of 17 inventoried |
| Physical tables | `organization` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 17 (17 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 8 keys from 8 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in organization

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 17 fields carry a vendor definition

**Observed.** 17 of this record's 17 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-111](../rules/CON-R-111.md) | Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved. | Inferred |

## Fields

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeOrganizationCategoryID` | Organization Category | Select the organization category from this field. Categories are the third level of organization in Lx. Categories are the children of types, and grandchildren of Groups. Groups, types, and categories are used to simplify reporting. | Dropdown (Org Category Code) | Global |  | `organization.CodeOrganizationCategoryID · TEXT` | Org Category Code |
| `CodeOrganizationGroupID` | Organization Group | Select the organization group from this field. Groups are the first level of organization in Lx. Groups are the parents of types, and grandparents of Categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Org Group Code) | Global |  | `organization.CodeOrganizationGroupID · TEXT` | Org Group Code |
| `CodeOrganizationTypeID` | Organization Type | Select the organization type from this field. Types are the second level of organization in Lx. Types are the children of groups, and parents of Categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Org Type Code) | Global |  | `organization.CodeOrganizationTypeID · TEXT` | Org Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `OrganizationID` | Organization RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `organization.OrganizationID · VARCHAR(64) NOT NULL` |  |

### Text & notes (10)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccountNumber1` | Account Number #1 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber1 · TEXT` |  |
| `AccountNumber2` | Account Number #2 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber2 · TEXT` |  |
| `AccountNumber3` | Account Number #3 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber3 · TEXT` |  |
| `AccountNumber4` | Account Number #4 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber4 · TEXT` |  |
| `AccountNumber5` | Account Number #5 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber5 · TEXT` |  |
| `AccountNumber6` | Account Number #6 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber6 · TEXT` |  |
| `AccountNumber7` | Account Number #7 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber7 · TEXT` |  |
| `AccountNumber8` | Account Number #8 | Enter an account number associated with the organization in this field. | Text | Global |  | `organization.AccountNumber8 · TEXT` |  |
| `OrganizationName` | Organization Name | Enter the organization name in this field. | Text | Global | yes | `organization.OrganizationName · TEXT` |  |
| `PortfolioIDList` | Portfolio Access | This field contains a list of the portfolios that are associated with a given organization. It is used to filter organization records based on the current porfolio. | Text | Global |  | `organization.PortfolioIDList · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Organization ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `organization.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `organization.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `organization.ModifiedDate · TEXT` |  |

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
