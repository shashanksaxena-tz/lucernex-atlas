# TemplateAudit — Data Fields

An audit trail of when a BudgetTemplate/EntityTemplate/FolderTemplate was applied to a new project — applied date and whether folder structure was copied. 17 Global fields under Company Items.

**Table Association:** `TemplateAudit` &nbsp;·&nbsp; **Total fields:** 17 (Global: 17, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Applied Date | `AppliedDate` | `sTYPE_TIME` | Global | Yes | No |  | Company Items / Template Audit |
| Budget Template | `BudgetEntityTemplateID` | `sTYPE_BUDGET_TEMPLATE` | Global | No | No |  | Company Items / Template Audit |
| Copy Folder Structure? | `CopyFolderStructure` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Template Audit |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Template Audit |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Template Audit |
| Entity Template | `EntityTemplateID` | `sTYPE_ENTITY_TEMPLATE` | Global | Yes | No |  | Company Items / Template Audit |
| Entity Template Type | `EntityTemplateTypeName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Template Audit |
| Folder Template | `FolderEntityTemplateID` | `sTYPE_FOLDER_TEMPLATE` | Global | No | No |  | Company Items / Template Audit |
| Folder Template Action List | `CodeFolderActionIDList` | `sCODE_FOLDER_TEMPLATE_ACTION` | Global | No | No |  | Company Items / Template Audit |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Template Audit |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Template Audit |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Template Audit |
| Schedule End Date | `ScheduleEndDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Template Audit |
| Schedule Start Date | `ScheduleStartDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Template Audit |
| Task Template | `TaskEntityTemplateID` | `sTYPE_TASK_TEMPLATE` | Global | No | No |  | Company Items / Template Audit |
| Template Audit ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Template Audit |
| Template Audit RecID | `TemplateAuditID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Template Audit |
