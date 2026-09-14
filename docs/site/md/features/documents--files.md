# Documents & Files

Documents and binders: every record root in the product shows Documents and Binders tabs. The documents half is a real record family; the binders half is not backed by any single record the census can name with confidence.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Everyone. Documents hang off records, and the folder tree is how they are found.

## Documents everywhere

*Observed · capability · source: `docs/modules/documents-folders/README.md`*

Document check-in and versioning attach to every record root through the entity supertype. Four of the ten document records are near-empty stubs - markup content and outbound correspondence are not recoverable from this schema.

## Binders = CommitteePkg

*Derived · capability · source: `docs/data-model/reading-the-census.md`*

Binders: the committee-package record is the best candidate - a dedicated screen routes to it from every record root, and both field inventories list the record, though they name different single fields for it, so neither shows the real table. The earlier 'no record backs binders' claim was withdrawn.

## Open questions (13)

*Inferred · group*

13 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### What object if any

*Inferred · question · source: `docs/modules/documents-folders/README.md`*

What object, if any, actually backs "Binders"/"Committee Packages"? The single biggest gap in this module. Nobody has confirmed this. Recorded in modules/documents-folders/README.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### Where does markup

*Inferred · question · source: `docs/modules/documents-folders/README.md`*

Where does markup annotation content actually live, if not in DocumentMarkup?. Nobody has confirmed this. Recorded in modules/documents-folders/README.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### How are successive

*Inferred · question · source: `docs/modules/documents-folders/README.md`*

How are successive versions of the same logical document actually grouped, given no explicit FK exists for it?. Nobody has confirmed this. Recorded in modules/documents-folders/README.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### Is outbound

*Inferred · question · source: `docs/modules/documents-folders/README.md`*

Is outbound correspondence tracking a genuine product gap or an export artefact?. Nobody has confirmed this. Recorded in modules/documents-folders/README.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### What does

*Inferred · question · source: `docs/modules/documents-folders/README.md`*

What does FolderTemplateAudit.CodeFolderActionIDList actually record?. Nobody has confirmed this. Recorded in modules/documents-folders/README.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### What object if any

*Inferred · question · source: `docs/modules/documents-folders/asg-edgeplus-mapping.md`*

What object, if any, actually backs "Binders"/"Committee Packages" in Lx? Blocks whether ASG Edge+ has anything at all to model against. Nobody has confirmed this. Recorded in modules/documents-folders/asg-edgeplus-mapping.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### Where does markup

*Inferred · question · source: `docs/modules/documents-folders/asg-edgeplus-mapping.md`*

Where does markup annotation content actually live in the live product, if not in DocumentMarkup?. Nobody has confirmed this. Recorded in modules/documents-folders/asg-edgeplus-mapping.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### How are successive

*Inferred · question · source: `docs/modules/documents-folders/asg-edgeplus-mapping.md`*

How are successive versions of the same logical document actually grouped in Lx's live behaviour, independent of the missing FK?. Nobody has confirmed this. Recorded in modules/documents-folders/asg-edgeplus-mapping.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### Is outbound

*Inferred · question · source: `docs/modules/documents-folders/asg-edgeplus-mapping.md`*

Is outbound correspondence tracking a genuine Lx product gap, or an artefact of this export?. Nobody has confirmed this. Recorded in modules/documents-folders/asg-edgeplus-mapping.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### What object if any

*Inferred · question · source: `docs/modules/documents-folders/data-model.md`*

What object, if any, actually backs the "Binders" / "Committee Packages" feature? The single biggest gap in this module — a universally-navigable feature with no discoverable schema object. Opening /en/CommitteeDocuments/PECommPkg.jsp directly is the only way this pass could not resolve it further. Nobody has confirmed this. Recorded in modules/documents-folders/data-model.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### Where does markup

*Inferred · question · source: `docs/modules/documents-folders/data-model.md`*

Where does markup annotation content actually live, if not in DocumentMarkup? Determines whether ASG Edge+'s markup feature (if built) needs its own new data model from scratch (almost certainly yes) or can port anything from Lx. Nobody has confirmed this. Recorded in modules/documents-folders/data-model.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### Is outbound

*Inferred · question · source: `docs/modules/documents-folders/data-model.md`*

Is outbound correspondence tracking a genuine product gap, or an export artefact? If genuine, ASG Edge+ needs to decide whether sent-mail tracking is in scope at all, since Lx offers no model to draw from. Nobody has confirmed this. Recorded in modules/documents-folders/data-model.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

### What does

*Inferred · question · source: `docs/modules/documents-folders/data-model.md`*

What does CodeFolderActionIDList on FolderTemplateAudit actually record — which folder actions (create/copy/skip?) were taken when the template was applied?. Nobody has confirmed this. Recorded in modules/documents-folders/data-model.md, under the Documents, Folders & Correspondence area. Until it is settled, anything built on the assumption is a guess.

## Rules (11)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### A Document must — [DOC-R-001](../rules/DOC-R-001.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Trigger: Document create/save. Input: `Document.ParentFolderID`, `Required = Yes`.**

### A Document must — [DOC-R-002](../rules/DOC-R-002.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `Document.CodeDocumentTypeID`, `.CodeDocumentConvertStatusID`, both `Required = Yes`. Confidence: Observed (`../../data-fields/document.md`).**

### A Document carries — [DOC-R-003](../rules/DOC-R-003.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `Document.ReadyForRelease`, `Required = Yes`, distinct from `IsCheckedOut`/ `CheckedOutByMemberID`/`CheckedOutDate`. Effect: Every document row must explicitly state whether it counts as released, as a separate fact from whether it is currently locked for editing.**

### A Folder s parent is — [DOC-R-004](../rules/DOC-R-004.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `Folder.ParentFolderID`, `Required = No`. Effect: Unlike `Document` (`DOC-R-001`), a `Folder` need not have a parent — the folder tree has genuine roots.**

### A Folder s own — [DOC-R-005](../rules/DOC-R-005.md)

*Derived · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent `PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/ `.IsLatestVersion` both being present.**

### Per folder security — [DOC-R-006](../rules/DOC-R-006.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `FolderSecurity` carries no `ProjectEntityID` — only `FolderID`, `CodeUserClassID`, and `CodeFolderSecurityTypeID`. Effect: Folder-level access control is scoped entirely through the folder it secures, not separately to any entity.**

### A folder template s — [DOC-R-007](../rules/DOC-R-007.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `FolderTemplate` has one field (`ProjectEntityID`); `VirtualTemplateFolder` carries `TemplateName`, `Description`, `Notes`, and 11 `IsValidFor*` flags.**

### A folder template — [DOC-R-008](../rules/DOC-R-008.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: The 11 `IsValidFor*` booleans on `VirtualTemplateFolder`, matching the enumeration in `../../data-model/project-entity.md` §1.4. Effect: The same attachability-matrix mechanism used for Forms/Issue types applies to folder templates.**

### Applying a template — [DOC-R-009](../rules/DOC-R-009.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`, `.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row, plus `CopyFolderStructure` (boolean) and `AppliedDate`. Effect: A single audit row can record that folder, budget, and task….**

### DocumentMarkup does — [DOC-R-010](../rules/DOC-R-010.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `DocumentMarkup`'s only field is `ProjectEntityID`; `Document.HasMarkups` is a boolean flag with no visible source of truth for what the markup actually is.**

### An email s — [DOC-R-011](../rules/DOC-R-011.md)

*Observed · rule · source: `docs/modules/documents-folders/rules.md`*

**Input: `LinkEMailReceivedLogDocument.DocumentID` + `.EMailReceivedLogID`. Effect: A received email's attachments become standard `Document` rows, filed under the ordinary `Folder` hierarchy, rather than living in a separate email-attachment store.**
