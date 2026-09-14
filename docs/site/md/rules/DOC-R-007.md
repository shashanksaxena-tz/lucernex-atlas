# DOC-R-007 — A folder template's real metadata lives on VirtualTemplateFolder, not FolderTemplate

*Documents, Folders & Correspondence · Observed*

**Input: `FolderTemplate` has one field (`ProjectEntityID`); `VirtualTemplateFolder` carries `TemplateName`, `Description`, `Notes`, and 11 `IsValidFor*` flags.**

Input: `FolderTemplate` has one field (`ProjectEntityID`); `VirtualTemplateFolder` carries `TemplateName`, `Description`, `Notes`, and 11 `IsValidFor*` flags. Effect: Any rebuild reading "what is a folder template" from `FolderTemplate` alone will find almost nothing; the authoritative shape is `VirtualTemplateFolder`'s. Confidence: Observed, field-list comparison — `data-model.md`.

## The wording it rests on

> what is a folder template

## What it constrains

[FolderTemplate](../entities/FolderTemplate.md), [VirtualTemplateFolder](../entities/VirtualTemplateFolder.md)

## Confidence

Observed, field-list comparison — `data-model.md`

---

Source: `docs/modules/documents-folders/rules.md`
