# Documents, Folders & Correspondence

*In scope for the rebuild*

Document storage with a templated folder tree and per-folder security, plus the inbound/outbound e-mail log.

Stated up front. Ten objects, 99 fields — the smallest field count of any in-scope module — and the count itself is the finding: four of the ten objects are 1-to-3-field stubs. DocumentMarkup and EMailSentLog carry exactly one field each (ProjectEntityID); FolderTemplate carries one field too; FolderSecurity carries three. The substantive content sits in Document (23 fields), FolderTemplateAudit (18), Folder (16), VirtualTemplateFolder (16), and EMailReceivedLog (15). This module is universal in reach — every ProjectEntity root carries a Documents tab (document/Index.jsp, per 003) and a Binders tab (CommitteeDocuments/PECommPkg.jsp) — but two of its most-asked-about capabilities turn out to have no substantive backing in the schema export available to this pass: markup content (DocumentMarkup is a stub; only a boolean flag on Document survives) and Binders themselves, which route to a JSP internally named "Committee Packages" but correspond to no object anywhere in the 223-object census — not Binder, not Committee, not anything close. Meanwhile the live tenant holds 11,905 documents (../../data-model/graphql-api.md), the largest single collection in the product, so this is not a lightly-used corner of the schema — it is a heavily-used feature whose full data model this pass could not fully recover.

|  | Count |
|---|---|
| Record types | 10 |
| Fields | 99 |
| Keys in | 16 |
| Keys out | 20 |
| Rules | 11 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Document](../entities/Document.md) | `document` | 23 | 10 |
| [FolderTemplateAudit](../entities/FolderTemplateAudit.md) | `folder_template_audit` | 18 | 0 |
| [Folder](../entities/Folder.md) | `folder` | 16 | 7 |
| [VirtualTemplateFolder](../entities/VirtualTemplateFolder.md) | `virtual_template_folder` | 16 | 0 |
| [EMailReceivedLog](../entities/EMailReceivedLog.md) | `e_mail_received_log` | 15 | 1 |
| [LinkEMailReceivedLogDocument](../entities/LinkEMailReceivedLogDocument.md) | `link_e_mail_received_log_document` | 5 | 0 |
| [FolderSecurity](../entities/FolderSecurity.md) | `folder_security` | 3 | 0 |
| [DocumentMarkup](../entities/DocumentMarkup.md) | `document_markup` | 1 | 0 |
| [EMailSentLog](../entities/EMailSentLog.md) | `e_mail_sent_log` | 1 | 0 |
| [FolderTemplate](../entities/FolderTemplate.md) | `folder_template` | 1 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [DOC-R-001](../rules/DOC-R-001.md) | A Document must belong to exactly one Folder | Trigger: Document create/save. Input: `Document.ParentFolderID`, `Required = Yes`. | Observed |
| [DOC-R-002](../rules/DOC-R-002.md) | A Document must declare a Document Type and a Conversion Status | Input: `Document.CodeDocumentTypeID`, `.CodeDocumentConvertStatusID`, both `Required = Yes`. Confidence: Observed (`../../data-fields/document.md`). | Observed |
| [DOC-R-003](../rules/DOC-R-003.md) | A Document carries an explicit release gate, independent of its checkout lock | Input: `Document.ReadyForRelease`, `Required = Yes`, distinct from `IsCheckedOut`/ `CheckedOutByMemberID`/`CheckedOutDate`. Effect: Every document row must explicitly state whether it counts as releas | Observed |
| [DOC-R-004](../rules/DOC-R-004.md) | A Folder's parent is optional; root folders exist | Input: `Folder.ParentFolderID`, `Required = No`. Effect: Unlike `Document` (`DOC-R-001`), a `Folder` need not have a parent — the folder tree has genuine roots. | Observed |
| [DOC-R-005](../rules/DOC-R-005.md) | A Folder's own history is modelled with an explicit self-reference; a Document's is not | Input: `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent `PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/ `.IsLatestVersion` both | Derived |
| [DOC-R-006](../rules/DOC-R-006.md) | Per-folder security is independent of ProjectEntity scoping | Input: `FolderSecurity` carries no `ProjectEntityID` — only `FolderID`, `CodeUserClassID`, and `CodeFolderSecurityTypeID`. Effect: Folder-level access control is scoped entirely through the folder it  | Observed |
| [DOC-R-007](../rules/DOC-R-007.md) | A folder template's real metadata lives on VirtualTemplateFolder, not FolderTemplate | Input: `FolderTemplate` has one field (`ProjectEntityID`); `VirtualTemplateFolder` carries `TemplateName`, `Description`, `Notes`, and 11 `IsValidFor*` flags. | Observed |
| [DOC-R-008](../rules/DOC-R-008.md) | A folder template declares which of the eleven `ProjectEntity` subtypes it may attach to | Input: The 11 `IsValidFor*` booleans on `VirtualTemplateFolder`, matching the enumeration in `../../data-model/project-entity.md` §1.4. Effect: The same attachability-matrix mechanism used for Forms/I | Observed |
| [DOC-R-009](../rules/DOC-R-009.md) | Applying a template stamps folder, budget, and task templates in one audit event | Input: `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`, `.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row, plus `CopyFolderStructure` ( | Observed |
| [DOC-R-010](../rules/DOC-R-010.md) | DocumentMarkup does not persist markup content in this schema | Input: `DocumentMarkup`'s only field is `ProjectEntityID`; `Document.HasMarkups` is a boolean flag with no visible source of truth for what the markup actually is. | Observed |
| [DOC-R-011](../rules/DOC-R-011.md) | An email's attachments are promoted into ordinary Document/Folder records | Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather th | Observed |
