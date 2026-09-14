# Document

*23 fields · module: Documents, Folders & Correspondence · Postgres: `document`*

The document/file metadata record used across the platform — author, checkout status (Checked Out By Member, Checked Out Date) for document locking during edits. 22 Global fields under Documents.

Source: `data-fields/document.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Fields with a vendor definition | 22 of 23 inventoried |
| Physical tables | `document` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 22 (22 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 10 keys from 10 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in document

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 22 fields carry a vendor definition

**Observed.** 22 of this record's 23 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 22 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 7 are marked required.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [DOC-R-001](../rules/DOC-R-001.md) | Trigger: Document create/save. Input: `Document.ParentFolderID`, `Required = Yes`. | Observed |
| [DOC-R-002](../rules/DOC-R-002.md) | Input: `Document.CodeDocumentTypeID`, `.CodeDocumentConvertStatusID`, both `Required = Yes`. Confidence: Observed (`../../data-fields/document.md`). | Observed |
| [DOC-R-003](../rules/DOC-R-003.md) | Input: `Document.ReadyForRelease`, `Required = Yes`, distinct from `IsCheckedOut`/ `CheckedOutByMemberID`/`CheckedOutDate`. Effect: Every document row must explicitly state whether it counts as released, as a separate fact from whether it i | Observed |
| [DOC-R-004](../rules/DOC-R-004.md) | Input: `Folder.ParentFolderID`, `Required = No`. Effect: Unlike `Document` (`DOC-R-001`), a `Folder` need not have a parent — the folder tree has genuine roots. | Observed |
| [DOC-R-005](../rules/DOC-R-005.md) | Input: `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent `PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/ `.IsLatestVersion` both being present. | Derived |
| [DOC-R-010](../rules/DOC-R-010.md) | Input: `DocumentMarkup`'s only field is `ProjectEntityID`; `Document.HasMarkups` is a boolean flag with no visible source of truth for what the markup actually is. | Observed |
| [DOC-R-011](../rules/DOC-R-011.md) | Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather than living in a separate email-attachment | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CheckedOutByMemberID` | Checked Out By Member | This field displays the name of the member who checked out the file. | Member ID | Global |  | `document.CheckedOutByMemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `document.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AuthoredByPersonID` | Author | Select the author of the document from this field. | Contact | Global |  | `document.AuthoredByPersonID · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeDocumentConvertStatusID` | Conversion Status | This field displays the status of the OCR conversion of your document. A document with a status of Waiting is currently in the queue to be converted. When the system begins to convert the file, the status will change to Converting. Finally, when the conversion is complete, the OCR status will be Converted. This means the PDF is converted and ready to search. | Dropdown (Document Convert Status Code) | Global | yes | `document.CodeDocumentConvertStatusID · TEXT` | Document Convert Status Code |
| `CodeDocumentTypeID` | Document Type | Select the document type from the document type field. | Dropdown (Document Type Code) | Global | yes | `document.CodeDocumentTypeID · TEXT` | Document Type Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentID` | Document RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `document.DocumentID · VARCHAR(64) NOT NULL` |  |
| `FileSize` | File Size | This field displays the size of the document file. | Number | Global |  | `document.FileSize · TEXT` |  |
| `Version` |  | The version number of the document. | Number | Global | yes | `document.Version · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CheckedOutDate` | Checked Out Date | This field displays the date the member checked out the file. | Date | Global |  | `document.CheckedOutDate · TEXT` |  |
| `FileCreatedDate` | File Created Date | The date the document was uploaded to Lx. | Time | Global | yes | `document.FileCreatedDate · TEXT` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HasMarkups` | Has Markups? | This flag indicates whether a document has markups from the Lx document viewer. | Boolean | Global |  | `document.HasMarkups · TEXT` |  |
| `IsCheckedOut` | Is Checked Out? | This flag indicates whether the document has been checked out or not. If a document is flagged as checked out, you will not be able to make changes or upload a new version of the document. | Boolean | Global |  | `document.IsCheckedOut · TEXT` |  |
| `IsLatestVersion` | Is Latest Version? | This flag indicates whether the version you are viewing is the latest version of the document. | Boolean | Global |  | `document.IsLatestVersion · TEXT` |  |
| `ReadyForRelease` | Released? | Select the Release Document Immediately check box to make this document immediately available to everyone. If you do not select the Release Document Immediately check box, the document version will only be visible to you. You can make the version visible to others by following the View Revision History procedures in the Online Help. | Boolean | Global | yes | `document.ReadyForRelease · TEXT` |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AuthorName` | Author Name | Enter the name of the author of this document. | Text | Global |  | `document.AuthorName · TEXT` |  |
| `BaseName` | File Name | This field displays the file name of the file attached to the record. | Text | Global | yes | `document.BaseName · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `document.Description · TEXT` |  |
| `DownloadLink` | Download Link | When added to a report, this field allows you to download documents individually or in bulk. | Text | Global |  | `document.DownloadLink · TEXT` |  |
| `ParentFolderID` | Parent Folder | The folder ID of this folder's parent folder. | Text | Global | yes | `document.ParentFolderID · TEXT` |  |
| `ParentFolderName` | Parent Folder Name | This field displays the parent folder name of the document. | Text | Global |  | `document.ParentFolderName · TEXT` |  |
| `SubFolderPath` | Folder | The folder path for this document. For example: "\Folder 1 Name\Folder 2 Name\". | Text | Global |  | `document.SubFolderPath · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `document.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `document.ModifiedDate · TEXT` |  |

## What points here (10 keys)

| Record type | Via column |
|---|---|
| [ContractFinancialTest](ContractFinancialTest.md) | `AssociatedDocumentID` |
| [Covenant](Covenant.md) | `AssociatedDocumentID` |
| [DemographicResults](DemographicResults.md) | `DocumentID` |
| [ExpenseRecoveryItemMapping](ExpenseRecoveryItemMapping.md) | `DocumentID` |
| [FacilityExpense](FacilityExpense.md) | `AssociatedDocumentID` |
| [LandlordInvoice](LandlordInvoice.md) | `AssociatedDocumentID` |
| [LinkEMailReceivedLogDocument](LinkEMailReceivedLogDocument.md) | `DocumentID` |
| [ParcelAccess](ParcelAccess.md) | `AssociatedDocumentID` |
| [PaymentTransaction](PaymentTransaction.md) | `AssociatedDocumentID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `AssociatedDocumentID` |
