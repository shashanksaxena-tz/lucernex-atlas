# Documents, Folders & Correspondence — rules

`DOC-R-001` through `DOC-R-011`. Every rule below is derived from the FK graph
([`data-model.md`](data-model.md)) or the Data Fields `Required` column; none is derived from a live
screen capture of this module (no Documents/Binders/Correspondence screen has been opened — see
Open Questions in [`README.md`](README.md)), so confidence tops out at **Derived** except where
noted. Evidence discipline per [`../../CONVENTIONS.md`](../../CONVENTIONS.md).

---

### DOC-R-001 — A Document must belong to exactly one Folder
**Trigger:** Document create/save. **Input:** `Document.ParentFolderID`, `Required = Yes`.
**Effect:** Save is blocked without a parent folder. **Confidence:** Observed
([`../../data-fields/document.md`](../../data-fields/document.md)).

### DOC-R-002 — A Document must declare a Document Type and a Conversion Status
**Input:** `Document.CodeDocumentTypeID`, `.CodeDocumentConvertStatusID`, both `Required = Yes`.
**Confidence:** Observed ([`../../data-fields/document.md`](../../data-fields/document.md)).

### DOC-R-003 — A Document carries an explicit release gate, independent of its checkout lock
**Input:** `Document.ReadyForRelease`, `Required = Yes`, distinct from `IsCheckedOut`/
`CheckedOutByMemberID`/`CheckedOutDate`. **Effect:** Every document row must explicitly state
whether it counts as released, as a separate fact from whether it is currently locked for editing.
**Confidence:** Observed ([`../../data-fields/document.md`](../../data-fields/document.md)); what
gates the transition (who may set it, whether it can be un-set) is Inferred/unconfirmed.

### DOC-R-004 — A Folder's parent is optional; root folders exist
**Input:** `Folder.ParentFolderID`, `Required = No`. **Effect:** Unlike `Document` (`DOC-R-001`), a
`Folder` need not have a parent — the folder tree has genuine roots. **Confidence:** Observed
([`../../data-fields/folder.md`](../../data-fields/folder.md)).

### DOC-R-005 — A Folder's own history is modelled with an explicit self-reference; a Document's is not
**Input:** `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent
`PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/
`.IsLatestVersion` both being present. **Effect:** The schema is internally inconsistent about
whether "history of a record" is an explicit link or an implicit one, in the same module.
**Confidence:** Derived, exhaustive field-list comparison —
[`data-model.md`](data-model.md#23-document-versioning-has-no-explicit-lineage-column).

### DOC-R-006 — Per-folder security is independent of ProjectEntity scoping
**Input:** `FolderSecurity` carries no `ProjectEntityID` — only `FolderID`, `CodeUserClassID`, and
`CodeFolderSecurityTypeID`. **Effect:** Folder-level access control is scoped entirely through the
folder it secures, not separately to any entity. **Confidence:** Observed, exhaustive field-list
read.

### DOC-R-007 — A folder template's real metadata lives on VirtualTemplateFolder, not FolderTemplate
**Input:** `FolderTemplate` has one field (`ProjectEntityID`); `VirtualTemplateFolder` carries
`TemplateName`, `Description`, `Notes`, and 11 `IsValidFor*` flags. **Effect:** Any rebuild reading
"what is a folder template" from `FolderTemplate` alone will find almost nothing; the authoritative
shape is `VirtualTemplateFolder`'s. **Confidence:** Observed, field-list comparison —
[`data-model.md`](data-model.md#22-foldertemplate-is-a-stub-virtualtemplatefolder-carries-the-real-metadata).

### DOC-R-008 — A folder template declares which of the eleven `ProjectEntity` subtypes it may attach to
**Input:** The 11 `IsValidFor*` booleans on `VirtualTemplateFolder`, matching the enumeration in
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §1.4. **Effect:** The
same attachability-matrix mechanism used for Forms/Issue types applies to folder templates.
**Confidence:** Observed, field-list match.

### DOC-R-009 — Applying a template stamps folder, budget, and task templates in one audit event
**Input:** `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`,
`.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row,
plus `CopyFolderStructure` (boolean) and `AppliedDate`. **Effect:** A single audit row can record
that folder, budget, and task templates were all applied together to a newly-created entity.
**Confidence:** Observed, field list + [`../../mindmap/edges.json`](../../mindmap/edges.json)
resolution of all four to `EntityTemplate` (`platform-tenancy`).

### DOC-R-010 — DocumentMarkup does not persist markup content in this schema
**Input:** `DocumentMarkup`'s only field is `ProjectEntityID`; `Document.HasMarkups` is a boolean
flag with no visible source of truth for what the markup actually is. **Effect:** A rebuild cannot
port markup annotation data from this schema — it is not captured here, by either genuine product
architecture (stored elsewhere) or export limitation. **Confidence:** Observed (field absence,
exhaustive); the explanation for the absence is unresolved — see
[`data-model.md`](data-model.md#21-documentmarkup-does-not-capture-markup-content).

### DOC-R-011 — An email's attachments are promoted into ordinary Document/Folder records
**Input:** `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. **Effect:** A received
email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy,
rather than living in a separate email-attachment store. **Confidence:** Observed, field list +
internal edge resolution ([`data-model.md`](data-model.md#6-cross-module-edges)). No equivalent link
exists for `EMailSentLog`, which carries no substantive fields at all — see `data-model.md` §5.
