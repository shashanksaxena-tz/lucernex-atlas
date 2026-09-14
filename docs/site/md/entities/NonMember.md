# NonMember

*37 fields · module: People & Parties · Postgres: `non_member`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 37 declared fields, filed under People & Parties, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 36 of its 37 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Fields with a vendor definition | 36 of 37 inventoried |
| Physical tables | `non_member` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | firm_global |
| Rules that name it | 3 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in non_member

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 36 fields carry a vendor definition

**Observed.** 36 of this record's 37 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 8 fields marked required

**Observed.** The inventory marks 8 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-001](../rules/PPL-R-001.md) | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields | Derived |
| [PPL-R-002](../rules/PPL-R-002.md) | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-003](../rules/PPL-R-003.md) | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1 | Inferred |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EmployerID` | Employer | Select the person's employer from this field. Employers are third party companies that are involved in your lifecycle process. They can be companies you pay also known as vendors or companies that are part of projects such as architects or general contractors. | Employer ID | — | yes | `non_member.EmployerID · TEXT` | [Employer](Employer.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | — |  | `non_member.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | — |  | `non_member.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeContactTypeIDList` | Contact Type List | Select the contact type this person should have using the multi-select field. | Dropdown (Contact Type Code) | — | yes | `non_member.CodeContactTypeIDList · TEXT` | Contact Type Code |
| `CodeJobFunctionID` | Job Function | Select this person's job function from this field. A job function is a broad category. Think of a job function as a person's department. | Dropdown (Job Function Code) | — | yes | `non_member.CodeJobFunctionID · TEXT` | Job Function Code |
| `CodeJobTitleID` | Job Title | Select this person's job title from this field. A job title is more specific to the person than the job function. | Dropdown (Job Title Code) | — |  | `non_member.CodeJobTitleID · TEXT` | Job Title Code |
| `CodeJobTitleIDList` | Job Titles |  | Dropdown (Job Title Code) | — |  | `non_member.CodeJobTitleIDList · TEXT` | Job Title Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillRate1` | Billing Rate #1 | Enter the person's primary billing rate in this field. | Currency | — |  | `non_member.BillRate1 · TEXT` |  |
| `BillRate2` | Billing Rate #2 | Enter the person's secondary billing rate in this field. | Currency | — |  | `non_member.BillRate2 · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PersonID` | Person RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | `non_member.PersonID · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | This flag indicates whether the non-member is active or inactive. | Boolean | — | yes | `non_member.Inactive · TEXT` |  |
| `UseEmployerAddress` | Use Employer Address | If you want to use the address of the employer for this member record, select this check box. | Boolean | — | yes | `non_member.UseEmployerAddress · TEXT` |  |

### Text & notes (22)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `City` |  | The city associated with this record. | Text | — |  | `non_member.City · TEXT` |  |
| `CountryID` | Country | Select the person's country from this field. | Text | — |  | `non_member.CountryID · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | — |  | `non_member.Description · TEXT` |  |
| `Designations` |  | The designation of the non-member from the Person table. | Text | — |  | `non_member.Designations · TEXT` |  |
| `EMail1` | Email #1 | Enter the person's primary email address. | Text | — |  | `non_member.EMail1 · TEXT` |  |
| `EMail2` | Email #2 | Enter the person's secondary email address. | Text | — |  | `non_member.EMail2 · TEXT` |  |
| `Fax` |  | Enter the person's fax number in this field. | Text | — |  | `non_member.Fax · TEXT` |  |
| `FirstName` | First Name | Enter the person's first name in this field. | Text | — | yes | `non_member.FirstName · TEXT` |  |
| `LastName` | Last Name | Enter the person's last name in this field. | Text | — | yes | `non_member.LastName · TEXT` |  |
| `MiddleName` | Middle Name | Enter the person's middle name in this field. | Text | — |  | `non_member.MiddleName · TEXT` |  |
| `MobileNumber` | Mobile Number | Enter the person's mobile phone number in this field. | Text | — |  | `non_member.MobileNumber · TEXT` |  |
| `Phone` |  | Enter the person's phone number in this field. | Text | — |  | `non_member.Phone · TEXT` |  |
| `PhoneExtension` | Phone Extension | Enter the person's phone extenstion in this field. | Text | — |  | `non_member.PhoneExtension · TEXT` |  |
| `PostalCode` | Postal Code | Enter the person's postal code in this field. | Text | — |  | `non_member.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | — |  | `non_member.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | — |  | `non_member.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | — |  | `non_member.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | — |  | `non_member.StreetAddress4 · TEXT` |  |
| `Suffix` |  | Enter the person's suffix if the person has one. | Text | — |  | `non_member.Suffix · TEXT` |  |
| `Title` |  | Enter the person's title in this field. | Text | — |  | `non_member.Title · TEXT` |  |
| `WebSite` | Website | Enter the person's website in this field. | Text | — |  | `non_member.WebSite · TEXT` |  |
| `WirelessEMail` | Wireless Email | Enter the person's wireless email in this field. | Text | — |  | `non_member.WirelessEMail · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Person ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | — | yes | `non_member.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `non_member.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `non_member.ModifiedDate · TEXT` |  |
