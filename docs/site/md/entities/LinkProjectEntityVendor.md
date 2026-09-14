# LinkProjectEntityVendor

*4 fields · module: People & Parties · Postgres: `link_project_entity_vendor`*

Join table linking a ProjectEntity (portfolio) to an approved Vendor.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 4 |
| Fields with a vendor definition | 4 of 4 inventoried |
| Physical tables | `link_project_entity_vendor` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 4 (4 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_project_entity_vendor

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 4 fields carry a vendor definition

**Observed.** 4 of this record's 4 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 4 comparable

**Observed.** Over the 4 fields both captures contain, they agree on 3. The exceptions are ProjectEntityID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-006](../rules/PPL-R-006.md) | Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` | Porfolio | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity ID | Global | yes | `link_project_entity_vendor.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | The vendor ID associated with the record. | Employer ID | Global | yes | `link_project_entity_vendor.VendorID · TEXT` | [Employer](Employer.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkProjectEntityVendorID` | Link Portfolio Vendor RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `link_project_entity_vendor.LinkProjectEntityVendorID · VARCHAR(64) NOT NULL` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Link Portfolio Vendor ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `link_project_entity_vendor.BOMapClientRecordID · TEXT` |  |
