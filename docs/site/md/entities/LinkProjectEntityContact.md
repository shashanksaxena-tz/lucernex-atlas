# LinkProjectEntityContact

*12 fields · module: People & Parties · Postgres: `link_project_entity_contact`*

Join table linking a ProjectEntity to a contact person with a contact-type classification.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 12 |
| Fields with a vendor definition | 12 of 12 inventoried |
| Physical tables | `link_project_entity_contact` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_project_entity_contact

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 12 fields carry a vendor definition

**Observed.** 12 of this record's 12 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 4; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-002](../rules/PPL-R-002.md) | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-005](../rules/PPL-R-005.md) | Both `CompanyID` and `ContactID` are independently nullable | Derived |
| [PPL-R-006](../rules/PPL-R-006.md) | Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EmployerID` | Employer | The employer of the contact. | Employer ID | Global |  | `link_project_entity_contact.EmployerID · TEXT` | [Employer](Employer.md) |
| `Landlord_EmployerID` | Landlord (Employer) | This field determines the landlord employer contact associated with this project. | Employer ID | Global |  | `link_project_entity_contact.Landlord_EmployerID · TEXT` | [Employer](Employer.md) |
| `ProjectEntityID` | Entity | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity ID | Global | yes | `link_project_entity_contact.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Landlord_PersonID` | Landlord (Person) | This field determines the landlord contact associated with this project. | Contact | Global |  | `link_project_entity_contact.Landlord_PersonID · TEXT` |  |
| `PersonID` | Person | The ID of the person record. | Contact | Global |  | `link_project_entity_contact.PersonID · TEXT` |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeContactTypeID` | Contact Type | The contact type of the contact. | Dropdown (Contact Type Code) | Global | yes | `link_project_entity_contact.CodeContactTypeID · TEXT` | Contact Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Rating` |  | The rating of the contact entered on the Edit Contacts page. | Number | Global |  | `link_project_entity_contact.Rating · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` |  | If the value of the field is true, this contact has been marked inactive on the Edit Contacts page. | Boolean | Global | yes | not extracted |  |
| `IsPrimary` | Is Primary? | If the value of the field is true, this contact has been marked as a primary contact on the Edit Contacts page. | Boolean | Global | yes | `link_project_entity_contact.IsPrimary · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `link_project_entity_contact.Notes · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `link_project_entity_contact.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `link_project_entity_contact.ModifiedDate · TEXT` |  |
