# LinkReTransScenContact

*33 fields · module: Portfolio & Real-Estate Transactions · Postgres: `link_re_trans_scen_contact`*

A join record linking a real-estate transaction Scenario to a contact (broker, attorney) with contact-type classification and email. 32 Global fields under RE Transaction — despite the Link-style name, at 32 fields it is treated as standalone rather than folded into the small Link bucket.

Source: `data-fields/link-re-trans-scen-contact.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 33 |
| Fields with a vendor definition | 0 of 33 inventoried |
| Physical tables | `link_re_trans_scen_contact` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 32 (32 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_re_trans_scen_contact

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 1 field marked required

**Observed.** The inventory marks 1 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `JurisdictionID` | Jurisdiction |  | County ID | Global |  | `link_re_trans_scen_contact.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `link_re_trans_scen_contact.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `RETransactionID` | RE Transaction |  | RE Transaction ID | Global |  | `link_re_trans_scen_contact.RETransactionID · TEXT` | [RETransaction](RETransaction.md) |
| `ReTransScenContactID` | RE Transaction Contact |  | RE Transaction Contact ID | Global |  | `link_re_trans_scen_contact.ReTransScenContactID · TEXT` | [ReTransScenContact](ReTransScenContact.md) |
| `ScenarioID` | Scenario |  | Scenario ID | Global |  | `link_re_trans_scen_contact.ScenarioID · TEXT` | [Scenario](Scenario.md) |
| `StateProvinceCountryID` | State Province Country |  | Country, State, County ID | Global |  | `link_re_trans_scen_contact.StateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PersonID` | Company Contact |  | Contact | Global |  | `link_re_trans_scen_contact.PersonID · TEXT` |  |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeContactTypeIDList` | Contact Type |  | Dropdown (Contact Type Code) | Global |  | `link_re_trans_scen_contact.CodeContactTypeIDList · TEXT` | Contact Type Code |
| `CodeJobTitleID` | Job Title |  | Dropdown (Job Title Code) | Global |  | `link_re_trans_scen_contact.CodeJobTitleID · TEXT` | Job Title Code |
| `ICodeJobFunctionID` | Job Function |  | Dropdown (Job Function Code) | Global |  | `link_re_trans_scen_contact.ICodeJobFunctionID · TEXT` | Job Function Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkReTransScenContactID` | RE Transaction Scenario Contact RecID |  | Number | Global |  | `link_re_trans_scen_contact.LinkReTransScenContactID · VARCHAR(64) NOT NULL` |  |

### Text & notes (17)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `City` |  |  | Text | Global |  | `link_re_trans_scen_contact.City · TEXT` |  |
| `EMail1` | E Mail #1 |  | Text | Global |  | `link_re_trans_scen_contact.EMail1 · TEXT` |  |
| `EmployerName` | Employer Name |  | Text | Global |  | `link_re_trans_scen_contact.EmployerName · TEXT` |  |
| `FirstName` | First Name |  | Text | Global |  | `link_re_trans_scen_contact.FirstName · TEXT` |  |
| `LastName` | Last Name |  | Text | Global |  | `link_re_trans_scen_contact.LastName · TEXT` |  |
| `MiddleName` | Middle Name |  | Text | Global |  | `link_re_trans_scen_contact.MiddleName · TEXT` |  |
| `MobileNumber` | Mobile Number |  | Text | Global |  | `link_re_trans_scen_contact.MobileNumber · TEXT` |  |
| `NameFirstLast` | Name (First Last) |  | Text | Global |  | `link_re_trans_scen_contact.NameFirstLast · TEXT` |  |
| `NameLastFirst` | Name (Last First) |  | Text | Global |  | `link_re_trans_scen_contact.NameLastFirst · TEXT` |  |
| `Phone` |  |  | Text | Global |  | `link_re_trans_scen_contact.Phone · TEXT` |  |
| `PostalCode` | Postal Code |  | Text | Global |  | `link_re_trans_scen_contact.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 |  | Text | Global |  | `link_re_trans_scen_contact.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 |  | Text | Global |  | `link_re_trans_scen_contact.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 |  | Text | Global |  | `link_re_trans_scen_contact.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 |  | Text | Global |  | `link_re_trans_scen_contact.StreetAddress4 · TEXT` |  |
| `Suffix` |  |  | Text | Global |  | `link_re_trans_scen_contact.Suffix · TEXT` |  |
| `Title` |  |  | Text | Global |  | `link_re_trans_scen_contact.Title · TEXT` |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | RE Transaction Scenario Contact ClientID |  | Text | Global | yes | `link_re_trans_scen_contact.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By |  | Member ID | Global |  | `link_re_trans_scen_contact.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date |  | Time | Global |  | `link_re_trans_scen_contact.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `link_re_trans_scen_contact.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `link_re_trans_scen_contact.ModifiedDate · TEXT` |  |
