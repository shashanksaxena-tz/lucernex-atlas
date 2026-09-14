# Document

*23 fields · module: Documents, Folders & Correspondence · Postgres: `document`*

The document/file metadata record used across the platform — author, checkout status (Checked Out By Member, Checked Out Date) for document locking during edits. 22 Global fields under Documents.

Source: `data-fields/document.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Catalogued fields | 22 (22 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 10 keys from 10 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CheckedOutByMemberID` | Checked Out By Member | Member ID | Global |  | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AuthoredByPersonID` | Author | Contact | Global |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeDocumentConvertStatusID` | Conversion Status | Dropdown (Document Convert Status Code) | Global | yes | Document Convert Status Code |
| `CodeDocumentTypeID` | Document Type | Dropdown (Document Type Code) | Global | yes | Document Type Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentID` | Document RecID | Number | Global |  |  |
| `FileSize` | File Size | Number | Global |  |  |
| `Version` |  | Number | Global | yes |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CheckedOutDate` | Checked Out Date | Date | Global |  |  |
| `FileCreatedDate` | File Created Date | Time | Global | yes |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HasMarkups` | Has Markups? | Boolean | Global |  |  |
| `IsCheckedOut` | Is Checked Out? | Boolean | Global |  |  |
| `IsLatestVersion` | Is Latest Version? | Boolean | Global |  |  |
| `ReadyForRelease` | Released? | Boolean | Global | yes |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AuthorName` | Author Name | Text | Global |  |  |
| `BaseName` | File Name | Text | Global | yes |  |
| `Description` |  | Text | Global |  |  |
| `DownloadLink` | Download Link | Text | Global |  |  |
| `ParentFolderID` | Parent Folder | Text | Global | yes |  |
| `ParentFolderName` | Parent Folder Name | Text | Global |  |  |
| `SubFolderPath` | Folder | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

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
