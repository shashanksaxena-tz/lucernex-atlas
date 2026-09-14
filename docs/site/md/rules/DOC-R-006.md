# DOC-R-006 — Per-folder security is independent of ProjectEntity scoping

*Documents, Folders & Correspondence · Observed*

**Input: `FolderSecurity` carries no `ProjectEntityID` — only `FolderID`, `CodeUserClassID`, and `CodeFolderSecurityTypeID`. Effect: Folder-level access control is scoped entirely through the folder it secures, not separately to any entity.**

Input: `FolderSecurity` carries no `ProjectEntityID` — only `FolderID`, `CodeUserClassID`, and `CodeFolderSecurityTypeID`. Effect: Folder-level access control is scoped entirely through the folder it secures, not separately to any entity. Confidence: Observed, exhaustive field-list read.

## What it constrains

[FolderSecurity](../entities/FolderSecurity.md)

## Confidence

Observed, exhaustive field-list read

---

Source: `docs/modules/documents-folders/rules.md`
