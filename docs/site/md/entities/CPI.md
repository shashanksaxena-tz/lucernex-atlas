# CPI

*10 fields · module: Lease Accounting & Payments · Postgres: `c_p_i`*

A recorded Consumer Price Index value at a point in time, tied to a Contract, feeding CPI-indexed rent escalation.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Fields with a vendor definition | 9 of 10 inventoried |
| Physical tables | `c_p_i` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 9 (9 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in c_p_i

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 9 fields carry a vendor definition

**Observed.** 9 of this record's 10 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 9 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `c_p_i.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `c_p_i.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCPIIndexID` | CPI Index | The CPI Index field contains a list of CPI indexes that have been loaded into Lx in one of three ways: globally via API, manually at the firm-level, or manually at the contract-level. If you have added a contract-level CPI index, the index will be labled "Contract Specific" in the CPI Index field. | Dropdown (CPI Index Code) | Global |  | `c_p_i.CodeCPIIndexID · TEXT` | CPI Index Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CPI` | CPI Value | The CPI Value field is where you will enter the value of the CPI index. | 5-Digit Number | Global | yes | `c_p_i.CPI · TEXT` |  |
| `CPIID` | CPI RecID | The CPI ID / CPI Rec ID is the index name. For example, the global-level US All Urban Consumers (Current Series) CPI index has a CPI ID of BLS_CUUR0000SA0. | Number | Global |  | `c_p_i.CPIID · VARCHAR(64) NOT NULL` |  |
| `Month` |  | The Month field is where you will enter the two-digit month for the CPI index value. For example, enter February as 02. | Number | Global | yes | `c_p_i.Month · TEXT` |  |
| `Year` |  | The Year field is where you will enter the year for the CPI index value. | Number | Global | yes | `c_p_i.Year · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PublishedDate` | Published Date | The Published Date field is where you will enter the publication date of the CPI Index. It is our best practice recommendation that you include the publication date of the CPI index. In rare cases, the government may make changes to CPI index values for a prior month or year. However, as an auditing practice, we take the policy of retaining the old CPI index value in the system. By including the publication date of the CPI index, the system will know which CPI value to use the more recent one if there are multiple records in the system for a particular month or year. | Date | Global |  | `c_p_i.PublishedDate · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `c_p_i.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `c_p_i.ModifiedDate · TEXT` |  |
