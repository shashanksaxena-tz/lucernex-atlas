# PLT-R-015 — `TemplateAudit` names four template kinds; this module owns one

*Platform & Tenancy · Observed*

**A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | A Budget, Entity, Folder, or Task template is applied to a `ProjectEntity` |
| What it reads | `TemplateAudit.BudgetEntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID`, `EntityTemplateID` |
| What it writes | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here |

## What it constrains

[ProjectEntity](../entities/ProjectEntity.md), [TemplateAudit](../entities/TemplateAudit.md), [EntityTemplate](../entities/EntityTemplate.md)

Columns named: `TemplateAudit.BudgetEntityTemplateID`

## Confidence

Observed field list; Derived scope conclusion

---

Source: `docs/modules/platform-tenancy/rules.md`
