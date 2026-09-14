# ReTransScenContact

*28 fields · module: Portfolio & Real-Estate Transactions · Postgres: `re_trans_scen_contact`*

Contact record specific to a real-estate transaction scenario (distinct from LinkReTransScenContact, the join-style variant) — contact type, employer name, email. 28 Global fields under RE Transaction.

Source: `data-fields/re-trans-scen-contact.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Fields with a vendor definition | 25 of 28 inventoried |
| Physical tables | `re_trans_scen_contact` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 28 (28 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 4 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in re_trans_scen_contact

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 25 fields carry a vendor definition

**Observed.** 25 of this record's 28 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 28 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | Global |  | `re_trans_scen_contact.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `StateProvinceCountryID` | State Province Country | Select the state or province from this field. | Country, State, County ID | Global |  | `re_trans_scen_contact.StateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeContactTypeID` | Contact Type | Select the type of contact from the list. | Dropdown (Contact Type Code) | Global |  | `re_trans_scen_contact.CodeContactTypeID · TEXT` | Contact Type Code |
| `CodeJobFunctionID` | Job Function | Select this person's job function from this field. A job function is a broad category. Think of a job function as a person's department. | Dropdown (Job Function Code) | Global |  | `re_trans_scen_contact.CodeJobFunctionID · TEXT` | Job Function Code |
| `CodeJobTitleID` | Job Title | Select this person's job title from this field. A job title is more specific to the person than the job function. | Dropdown (Job Title Code) | Global |  | `re_trans_scen_contact.CodeJobTitleID · TEXT` | Job Title Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ReTransScenContactID` | RE Trans Scen Contact ID |  | Number | Global |  | `re_trans_scen_contact.ReTransScenContactID · VARCHAR(64) NOT NULL` |  |

### Text & notes (18)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `City` |  | Select the city of this contact. | Text | Global |  | `re_trans_scen_contact.City · TEXT` |  |
| `EMail1` | E Mail #1 | Enter the person's primary email address. | Text | Global |  | `re_trans_scen_contact.EMail1 · TEXT` |  |
| `EmployerName` | Employer Name | Enter the name of the person's employer. | Text | Global | yes | `re_trans_scen_contact.EmployerName · TEXT` |  |
| `FirstName` | First Name | Enter the person's first name in this field. | Text | Global | yes | `re_trans_scen_contact.FirstName · TEXT` |  |
| `LastName` | Last Name | Enter the person's last name in this field. | Text | Global | yes | `re_trans_scen_contact.LastName · TEXT` |  |
| `MiddleName` | Middle Name | Enter the person's middle name in this field. | Text | Global |  | `re_trans_scen_contact.MiddleName · TEXT` |  |
| `MobileNumber` | Mobile Number | Enter the person's mobile phone number in this field. | Text | Global |  | `re_trans_scen_contact.MobileNumber · TEXT` |  |
| `NameFirstLast` | Name (First Last) |  | Text | Global |  | `re_trans_scen_contact.NameFirstLast · TEXT` |  |
| `NameLastFirst` | Name (Last First) |  | Text | Global |  | `re_trans_scen_contact.NameLastFirst · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `re_trans_scen_contact.Notes · TEXT` |  |
| `Phone` |  | Enter the person's phone number in this field. | Text | Global |  | `re_trans_scen_contact.Phone · TEXT` |  |
| `PostalCode` | Postal Code | Enter the person's postal code in this field. | Text | Global |  | `re_trans_scen_contact.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `re_trans_scen_contact.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `re_trans_scen_contact.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `re_trans_scen_contact.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `re_trans_scen_contact.StreetAddress4 · TEXT` |  |
| `Suffix` |  | Enter the person's suffix if the person has one. | Text | Global |  | `re_trans_scen_contact.Suffix · TEXT` |  |
| `Title` |  | Enter the person's title in this field. | Text | Global |  | `re_trans_scen_contact.Title · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `re_trans_scen_contact.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `re_trans_scen_contact.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `re_trans_scen_contact.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `re_trans_scen_contact.ModifiedDate · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [LinkReTransScenContact](LinkReTransScenContact.md) | `ReTransScenContactID` |
