# DOC-R-001 — A Document must belong to exactly one Folder

*Documents, Folders & Correspondence · Observed*

**Trigger: Document create/save. Input: `Document.ParentFolderID`, `Required = Yes`.**

Trigger: Document create/save. Input: `Document.ParentFolderID`, `Required = Yes`. Effect: Save is blocked without a parent folder. Confidence: Observed (`../../data-fields/document.md`).

## What it constrains

[Document](../entities/Document.md)

Columns named: `Document.ParentFolderID`

## Confidence

Observed (`../../data-fields/document.md`)

---

Source: `docs/modules/documents-folders/rules.md`
