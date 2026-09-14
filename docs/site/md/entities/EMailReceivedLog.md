# EMailReceivedLog

*15 fields · module: Documents, Folders & Correspondence · Postgres: `e_mail_received_log`*

A logged inbound email tied to a record — arrival date and body, the source EMailReceivedLog rows LinkEMailReceivedLogDocument attaches Documents to.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 15 |
| Fields with a vendor definition | 14 of 15 inventoried |
| Physical tables | `e_mail_received_log` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 14 (14 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in e_mail_received_log

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 14 fields carry a vendor definition

**Observed.** 14 of this record's 15 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `e_mail_received_log.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EMailReceivedLogID` | E-Mail Rcvd RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `e_mail_received_log.EMailReceivedLogID · VARCHAR(64) NOT NULL` |  |
| `NumberOfAttachments` | Number Of Attachments | This field displays the number of attachments attached to an email sent to the email log of an entity. | Number | Global | yes | `e_mail_received_log.NumberOfAttachments · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ArrivalDate` | Arrival Date | The arrival date of an email sent to the email log of an entity. | Date | Global |  | `e_mail_received_log.ArrivalDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsCritical` | Is Critical? | This flag is set to true if the email sender flagged the email as important. | Boolean | Global |  | `e_mail_received_log.IsCritical · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Body` |  | The body of an email sent to the email log of an entity. | Text | Global |  | `e_mail_received_log.Body · TEXT` |  |
| `MailServiceEventID` | Mail Service Event ID | The mail service event ID of an email sent to the email log of an entity. | Text | Global | yes | `e_mail_received_log.MailServiceEventID · TEXT` |  |
| `Sender` |  | The email address of the sender of an email sent to the email log of an entity. | Text | Global |  | `e_mail_received_log.Sender · TEXT` |  |
| `Subject` |  | The subject of an email sent to the email log of an entity. | Text | Global |  | `e_mail_received_log.Subject · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | E-Mail Rcvd ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `e_mail_received_log.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `e_mail_received_log.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `e_mail_received_log.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `e_mail_received_log.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `e_mail_received_log.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `e_mail_received_log.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [LinkEMailReceivedLogDocument](LinkEMailReceivedLogDocument.md) | `EMailReceivedLogID` |
