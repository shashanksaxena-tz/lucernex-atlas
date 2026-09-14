# DOC-R-009 — Applying a template stamps folder, budget, and task templates in one audit event

*Documents, Folders & Correspondence · Observed*

**Input: `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`, `.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row, plus `CopyFolderStructure` (boolean) and `AppliedDate`. Effect: A single audit row can record that folder, budget, and task….**

Input: `FolderTemplateAudit.EntityTemplateID`, `.FolderEntityTemplateID`, `.BudgetEntityTemplateID`, `.TaskEntityTemplateID` — four `Template ID`-typed columns on one row, plus `CopyFolderStructure` (boolean) and `AppliedDate`. Effect: A single audit row can record that folder, budget, and task templates were all applied together to a newly-created entity. Confidence: Observed, field list + `../../mindmap/edges.json` resolution of all four to `EntityTemplate` (`platform-tenancy`).

## What it constrains

[FolderTemplateAudit](../entities/FolderTemplateAudit.md), [EntityTemplate](../entities/EntityTemplate.md)

Columns named: `FolderTemplateAudit.EntityTemplateID`

## Confidence

Observed, field list + `../../mindmap/edges.json` resolution of all four to `EntityTemplate` (`platform-tenancy`)

---

Source: `docs/modules/documents-folders/rules.md`
