# LinkEMailReceivedLogDocument

*5 fields · module: Documents, Folders & Correspondence · Postgres: `link_e_mail_received_log_document`*

Join table linking a received email log entry to a saved Document (e.g., an email attachment filed to the record).

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 5 |
| Fields with a vendor definition | 4 of 5 inventoried |
| Physical tables | `link_e_mail_received_log_document` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 4 (4 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_e_mail_received_log_document

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 4 fields carry a vendor definition

**Observed.** 4 of this record's 5 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 4 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 2 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-011](../rules/DOC-R-011.md) | Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather than living in a separate email-attachment | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentID` | Document | The ID of the file. | Document ID | Global |  | `link_e_mail_received_log_document.DocumentID · TEXT` | [Document](Document.md) |
| `EMailReceivedLogID` | E Mail Rcvd Log | The ID of the email log. | Email Received Log Record ID | Global | yes | `link_e_mail_received_log_document.EMailReceivedLogID · TEXT` | [EMailReceivedLog](EMailReceivedLog.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `link_e_mail_received_log_document.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkEMailReceivedLogDocumentID` | E-Mail Rcvd Doc RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `link_e_mail_received_log_document.LinkEMailReceivedLogDocumentID · VARCHAR(64) NOT NULL` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | E-Mail Rcvd Doc ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `link_e_mail_received_log_document.BOMapClientRecordID · TEXT` |  |
