# DOC-R-005 — A Folder's own history is modelled with an explicit self-reference; a Document's is not

*Documents, Folders & Correspondence · Derived*

**Input: `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent `PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/ `.IsLatestVersion` both being present.**

Input: `Folder.PreviousFolderID` (typed `Folder`, self-referencing) exists; no equivalent `PriorVersionDocumentID`-style column exists on `Document` despite `Document.Version`/ `.IsLatestVersion` both being present. Effect: The schema is internally inconsistent about whether "history of a record" is an explicit link or an implicit one, in the same module. Confidence: Derived, exhaustive field-list comparison — `data-model.md`.

## What it constrains

[Folder](../entities/Folder.md), [Document](../entities/Document.md)

Columns named: `Folder.PreviousFolderID`, `Document.Version`

## Confidence

Derived, exhaustive field-list comparison — `data-model.md`

---

Source: `docs/modules/documents-folders/rules.md`
