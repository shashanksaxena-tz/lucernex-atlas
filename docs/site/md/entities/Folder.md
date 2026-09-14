# Folder

*16 fields · module: Documents, Folders & Correspondence · Postgres: `folder`*

A document-management folder — downloadable flag and folder-template linkage, the container Document records live in. 16 Global fields under Documents.

Source: `data-fields/folder.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Fields with a vendor definition | 15 of 16 inventoried |
| Physical tables | `folder` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 7 keys from 7 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in folder

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 15 fields carry a vendor definition

**Observed.** 15 of this record's 16 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 2; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-004](../rules/DOC-R-004.md) | Input: `Folder.ParentFolderID`, `Required = No`. Effect: Unlike `Document` (`DOC-R-001`), a `Folder` need not have a parent — the folder tree has genuine roots. | Observed |
| [DOC-R-005](../rules/DOC-R-005.md) | Input: `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent `PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/ `.IsLatestVersion` both being present. | Derived |
| [DOC-R-011](../rules/DOC-R-011.md) | Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather than living in a separate email-attachment | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `folder.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SubscriptionCodeJobTitleIDList` | Subscriber Job Titles | This field gets a list of the job titles that are subscribed to this folder. | Dropdown (Job Title Code) | Global |  | `folder.SubscriptionCodeJobTitleIDList · TEXT` | Job Title Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FolderID` | Folder RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `folder.FolderID · VARCHAR(64) NOT NULL` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsFolderDownloadableByMember` | Downloadable | If the value of this field is true, the user has download access to this folder. | Boolean | Global |  | `folder.IsFolderDownloadableByMember · TEXT` |  |
| `IsFolderReadableByMember` | Readable | If the value of this field is true, the user has view access to this folder. | Boolean | Global |  | `folder.IsFolderReadableByMember · TEXT` |  |
| `IsFolderUploadOnlyByMember` | Uploadable Only | If the value of this field is true, the user has upload only access to this folder. | Boolean | Global |  | `folder.IsFolderUploadOnlyByMember · TEXT` |  |
| `IsFolderUploadableByMember` | Uploadable | If this field is true, the member has full permissions to the folder. | Boolean | Global |  | `folder.IsFolderUploadableByMember · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `folder.Description · TEXT` |  |
| `FolderName` | Name | Enter the folder name in this field. | Text | Global | yes | `folder.FolderName · TEXT` |  |
| `FolderTemplateName` | Folder Template Name | This field displays the name of the folder template applied to the entity. | Text | Global |  | `folder.FolderTemplateName · TEXT` |  |
| `ParentFolderID` | Parent Folder | The ID of the parent folder. | Text | Global |  | `folder.ParentFolderID · TEXT` |  |
| `PreviousFolderID` | Previous Folder | This field is used to determine the order of folders. | Text | Global |  | `folder.PreviousFolderID · TEXT` |  |
| `SubFolderPath` | Path Name | This field determines the folder path of a given document (e.g. "\Folder 1\Folder 2"). | Text | Global |  | `folder.SubFolderPath · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Folder ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `folder.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `folder.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `folder.ModifiedDate · TEXT` |  |

## What points here (7 keys)

| Record type | Via column |
|---|---|
| [ContractFinancialTest](ContractFinancialTest.md) | `FolderID` |
| [Covenant](Covenant.md) | `FolderID` |
| [FacilityExpense](FacilityExpense.md) | `FolderID` |
| [LandlordInvoice](LandlordInvoice.md) | `FolderID` |
| [ParcelAccess](ParcelAccess.md) | `FolderID` |
| [PaymentTransaction](PaymentTransaction.md) | `FolderID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `FolderID` |
