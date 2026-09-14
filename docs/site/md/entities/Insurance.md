# Insurance

*27 fields · module: Contracts & Leases · Postgres: `insurance`*

Required insurance coverage terms on a lease — certificate received/request dates, required flag, and whether the agent is also the named insured. 26 Global fields under Contract, anchoring VendorInsurance as the actual policy-level detail.

Source: `data-fields/insurance.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Fields with a vendor definition | 26 of 27 inventoried |
| Physical tables | `insurance` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 26 (26 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in insurance

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 26 fields carry a vendor definition

**Observed.** 26 of this record's 27 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `insurance.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `insurance.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `insurance.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `insurance.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContactID` | Contact | Select the contact associated with the policy from this field. | Contact | Global |  | `insurance.ContactID · TEXT` |  |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `insurance.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeInsuranceCategoryID` | Insurance Category | The insurance category is the third level of categorization for insurance records. Categories are the children of types, and the grandchildren of groups. | Dropdown (Insurance Category Code) | Global |  | `insurance.CodeInsuranceCategoryID · TEXT` | Insurance Category Code |
| `CodeInsuranceGroupID` | Insurance Group | The insurance group is the first level of categorization for insurance records. Groups are the parents of types, and the grandparents of categories. | Dropdown (Insurance Group Code) | Global |  | `insurance.CodeInsuranceGroupID · TEXT` | Insurance Group Code |
| `CodeInsuranceTypeID` | Insurance Type | The insurance type is the second level of categorization for insurance records. Types are the children of groups, and the parents of categories. | Dropdown (Insurance Type Code) | Global |  | `insurance.CodeInsuranceTypeID · TEXT` | Insurance Type Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CoverageAmount` | Coverage Amount | Enter the total amount of coverage in this field. | Currency | Global |  | `insurance.CoverageAmount · TEXT` |  |
| `SingleOccuranceAmount` | Single Occurance Amount | Enter the single occurrence coverage amount in this field. | Currency | Global |  | `insurance.SingleOccuranceAmount · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `InsuranceID` | Insurance RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `insurance.InsuranceID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `insurance.BeginDate · TEXT` |  |
| `CertificateReceivedDate` | Certificate Received Date | Enter the date the insurance certificate was received in this field. | Date | Global |  | `insurance.CertificateReceivedDate · TEXT` |  |
| `CertificateRequestDate` | Certificate Request Date | Enter the date the insurance certificate was requested in this field. | Date | Global |  | `insurance.CertificateRequestDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `insurance.EndDate · TEXT` |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AgentAlsoNamedInsuredFlag` | Agent Also Named Insured? | Select this check box if a third party agent is the policy-holder for the lease. | Boolean | Global |  | `insurance.AgentAlsoNamedInsuredFlag · TEXT` |  |
| `CertificateRequiredFlag` | Certificate Required? | Select this check box if you are required to submit proof of insurance. | Boolean | Global |  | `insurance.CertificateRequiredFlag · TEXT` |  |
| `LandlordAlsoNamedInsuredFlag` | Landlord Also Named Insured? | Select this check box if the landlord is the policy-holder for the lease. | Boolean | Global |  | `insurance.LandlordAlsoNamedInsuredFlag · TEXT` |  |
| `PolicyRequiredFlag` | Policy Required? | Select this check box if an insurance policy is required in the lease. | Boolean | Global |  | `insurance.PolicyRequiredFlag · TEXT` |  |
| `SelfInsuredFlag` | Self Insured? | Select this check box if you are the policy-holder for the lease. | Boolean | Global |  | `insurance.SelfInsuredFlag · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `insurance.Notes · TEXT` |  |
| `PolicyNumber` | Policy Number | Enter the policy number in this field. | Text | Global |  | `insurance.PolicyNumber · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `insurance.Section · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Insurance ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `insurance.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `insurance.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `insurance.ModifiedDate · TEXT` |  |
