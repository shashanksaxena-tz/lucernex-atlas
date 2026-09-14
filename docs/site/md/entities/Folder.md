# Folder

*16 fields · module: Documents, Folders & Correspondence · Postgres: `folder`*

A document-management folder — downloadable flag and folder-template linkage, the container Document records live in. 16 Global fields under Documents.

Source: `data-fields/folder.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | 16 (16 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 7 keys from 7 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-004](../rules/DOC-R-004.md) | Input: `Folder.ParentFolderID`, `Required = No`. Effect: Unlike `Document` (`DOC-R-001`), a `Folder` need not have a parent — the folder tree has genuine roots. | Observed |
| [DOC-R-005](../rules/DOC-R-005.md) | Input: `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent `PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/ `.IsLatestVersion` both being present. | Derived |
| [DOC-R-011](../rules/DOC-R-011.md) | Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather than living in a separate email-attachment | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SubscriptionCodeJobTitleIDList` | Subscriber Job Titles | Dropdown (Job Title Code) | Global |  | Job Title Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FolderID` | Folder RecID | Number | Global |  |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsFolderDownloadableByMember` | Downloadable | Boolean | Global |  |  |
| `IsFolderReadableByMember` | Readable | Boolean | Global |  |  |
| `IsFolderUploadOnlyByMember` | Uploadable Only | Boolean | Global |  |  |
| `IsFolderUploadableByMember` | Uploadable | Boolean | Global |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `FolderName` | Name | Text | Global | yes |  |
| `FolderTemplateName` | Folder Template Name | Text | Global |  |  |
| `ParentFolderID` | Parent Folder | Text | Global |  |  |
| `PreviousFolderID` | Previous Folder | Text | Global |  |  |
| `SubFolderPath` | Path Name | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Folder ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

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
