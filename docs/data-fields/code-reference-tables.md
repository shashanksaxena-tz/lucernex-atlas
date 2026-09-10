# Code, Custom List & Reference Definition Tables

These 8 tables (29 fields, all Global) are either the meta-schema behind tenant-defined custom lists (`CustomCodeField`, `CustomCodeTable` — see [006-manage-custom-lists.md](../admin/006-manage-custom-lists.md)) or small master/reference code tables (`Code*`) that back a single dropdown elsewhere in the schema. They are grouped together because each individually holds only 1-13 fields — the code table itself is usually just an ID, a name, and one or two behavior flags; the volume lives in the *values* of the list, not its own field catalog.

**Entities in this file:** 8 &nbsp;·&nbsp; **Total fields:** 29 (Global: 29, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `CustomCodeField` | 13 (13/0) | Meta-definition of a tenant-created custom code/dropdown field — the schema record behind Manage Custom Lists (see 006). |
| `CustomCodeTable` | 5 (5/0) | Meta-definition of a tenant-created custom code table, including a self-referencing parent-table link for hierarchical code lists. |
| `CodeAssetCategory` | 3 (3/0) | Master asset-category reference record — GL number and sub-account mapping for a category of equipment/assets. |
| `CodeProblem` | 2 (2/0) | Master maintenance-problem-type reference record with a remedy note, linked to an asset category. |
| `CodeBudgetColumnStatus` | 2 (2/0) | Master reference record for budget-column status values, including a locked flag. |
| `CodeSalesType` | 2 (2/0) | Master reference record for sales-type classification, with a flag to omit a type from sales-group totals. |
| `CodeResponsibleParty` | 1 (1/0) | A single-field master value for the responsible-party code list used on Responsibility records. |
| `CodeSalesGroup` | 1 (1/0) | A single-field master value letting one sales group alias to another for reporting rollups. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| CustomCodeField | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Custom Code Field ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Custom Code Field RecID | `CustomCodeFieldID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Field Name | `CustomCodeFieldName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Inactive | `Inactive` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Parent Custom Code Field | `ParentCustomCodeFieldID` | `sTYPE_CUSTOM_CODE_FIELD` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Parent Custom Code Table | `ParentCustomCodeTableID` | `sTYPE_CUSTOM_CODE_TABLE_REF` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Custom Code Fields |
| CustomCodeField | Table Name | `CustomCodeTableID` | `sTYPE_CUSTOM_CODE_TABLE_REF` | Global | Yes | No |  | Company Items / Custom Code Fields |
| CustomCodeTable | Custom Code Table ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| CustomCodeTable | Custom Code Table Name | `CustomCodeTableName` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| CustomCodeTable | Custom Code Table RecID | `CustomCodeTableID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| CustomCodeTable | Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| CustomCodeTable | Parent Custom Code Table | `ParentCustomCodeTableID` | `sTYPE_CUSTOM_CODE_TABLE_REF` | Global | No | No |  | Statics / Hidden |
| CodeAssetCategory | DNE Amount | `DNEAmount` | `sTYPE_MONEY` | Global | No | No |  | Equipment/Assets / Maintenance Category |
| CodeAssetCategory | GL Number | `GLNumber` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / Maintenance Category |
| CodeAssetCategory | Sub Account | `SubAccount` | `sTYPE_TEXT` | Global | No | No |  | Equipment/Assets / Maintenance Category |
| CodeProblem | Problem Remedy Note | `RemedyNote` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Service Request |
| CodeProblem | ParentCodeAssetCategoryID | `ParentCodeAssetCategoryID` | `sCODE_ASSET_CATEGORY` | Global | Yes | No |  | Statics / Hidden |
| CodeBudgetColumnStatus | BudgetColumnTypeID | `BudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Statics / Hidden |
| CodeBudgetColumnStatus | IsBudgetColumnLocked | `IsBudgetColumnLocked` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| CodeSalesType | Group | `ParentCodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | Yes | No |  | Statics / Hidden |
| CodeSalesType | Omit From Sales Group Total | `OmitFromSalesGroupTotal` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| CodeResponsibleParty | Responsible Party Value | `CodeResponsiblePartySystemID` | `sCODE_RESPONSIBLE_PARTY_SYSTEM` | Global | No | No |  | Contract / Responsibility System Value |
| CodeSalesGroup | Alias For Sales Group | `AliasForCodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Statics / Hidden |
