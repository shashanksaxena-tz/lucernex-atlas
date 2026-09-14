# DOC-R-004 — A Folder's parent is optional; root folders exist

*Documents, Folders & Correspondence · Observed*

**Input: `Folder.ParentFolderID`, `Required = No`. Effect: Unlike `Document` (`DOC-R-001`), a `Folder` need not have a parent — the folder tree has genuine roots.**

Input: `Folder.ParentFolderID`, `Required = No`. Effect: Unlike `Document` (`DOC-R-001`), a `Folder` need not have a parent — the folder tree has genuine roots. Confidence: Observed (`../../data-fields/folder.md`).

## What it constrains

[Folder](../entities/Folder.md), [Document](../entities/Document.md)

Columns named: `Folder.ParentFolderID`

## Rules it cites

[DOC-R-001](DOC-R-001.md)

## Confidence

Observed (`../../data-fields/folder.md`)

---

Source: `docs/modules/documents-folders/rules.md`
