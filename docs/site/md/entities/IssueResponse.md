# IssueResponse

*11 fields · module: Capital Projects & Scheduling · Postgres: `issue_response`*

A reply/answer posted against a bidder Issue (Q&A) during a bid process.

Source: `data-fields/workflow-notification-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 11 |
| Fields with a vendor definition | 0 of 11 inventoried |
| Physical tables | `issue_response` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 11 (11 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in issue_response

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required-ness: the captures agree

**Observed.** Over the 11 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 4 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` | ProjectEntity ID |  | Entity ID | Global | yes | `issue_response.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IssueResponseID` | Issue Response ID |  | Number | Global |  | `issue_response.IssueResponseID · VARCHAR(64) NOT NULL` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Body` |  |  | Text | Global |  | `issue_response.Body · TEXT` |  |
| `IssueID` | Issue ID |  | Text | Global | yes | `issue_response.IssueID · TEXT` |  |
| `SequenceNumber` | Sequence Number |  | Text | Global | yes | `issue_response.SequenceNumber · TEXT` |  |
| `Subject` |  |  | Text | Global | yes | `issue_response.Subject · TEXT` |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By |  | Member ID | Global |  | `issue_response.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date |  | Time | Global |  | `issue_response.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `issue_response.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `issue_response.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number |  | Number | Global |  | `issue_response.RevNumber · TEXT` |  |
