# Budget Ancillary Tables

These 4 tables (36 fields, all Global) round out the capital-budgeting model beneath the standalone [BudgetColumn](budgetcolumn.md), [BudgetColumnType](budgetcolumntype.md), and [BudgetLineItem](budgetlineitem.md) entities — saved grid views (`BudgetView`), selectable column alternatives (`BudgetOption`), and cost-escalation indexing (`BudgetIndex`/`BudgetIndexValue`).

**Entities in this file:** 4 &nbsp;·&nbsp; **Total fields:** 36 (Global: 36, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `BudgetOption` | 12 (12/0) | A selectable alternative version of a budget-column entity type. |
| `BudgetView` | 11 (11/0) | A named saved view/filter over the budget grid. |
| `BudgetIndexValue` | 7 (7/0) | One escalation percentage within a BudgetIndex series, tied to a budget column type. |
| `BudgetIndex` | 6 (6/0) | A named escalation index (e.g., a cost inflation index) applied to capital budgets, the header record for BudgetIndexValue. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| BudgetOption | Bot Entity Type | `BotEntityType` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Option |
| BudgetOption | Budget Column | `BudgetColumnID` | `sTYPE_BUDGET_COLUMN` | Global | Yes | No |  | Budget / Budget Option |
| BudgetOption | Budget Option ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Option |
| BudgetOption | Budget Option Name | `BudgetOptionName` | `sTYPE_TEXT` | Global | No | No |  | Budget / Budget Option |
| BudgetOption | Budget Option RecID | `BudgetOptionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Option |
| BudgetOption | Budget Option Template | `BudgetOptionTemplateID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Budget / Budget Option |
| BudgetOption | Budget Option Template PEID | `BudgetOptionTemplatePEID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Option |
| BudgetOption | Created By Member | `CreatedByMemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Budget / Budget Option |
| BudgetOption | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Option |
| BudgetOption | Initialized From Budget Column | `InitializedFromBudgetColumnID` | `sTYPE_BUDGET_COLUMN` | Global | No | No |  | Budget / Budget Option |
| BudgetOption | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Option |
| BudgetOption | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Option |
| BudgetView | Budget View ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget View |
| BudgetView | Budget View Name | `BudgetViewName` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget View |
| BudgetView | Budget View RecID | `BudgetViewID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget View |
| BudgetView | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget View |
| BudgetView | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget View |
| BudgetView | Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Budget / Budget View |
| BudgetView | Is Budget View Edit Controller? | `isEditController` | `sTYPE_BOOLEAN` | Global | No | No |  | Budget / Budget View |
| BudgetView | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget View |
| BudgetView | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget View |
| BudgetView | ProjectEntityID | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | No | No |  | Budget / Budget View |
| BudgetView | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget View |
| BudgetIndexValue | Budget Column Type | `BudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | Yes | No |  | Budget / Budget Index Value |
| BudgetIndexValue | Budget Index | `BudgetIndexID` | `sTYPE_BUDGET_INDEX` | Global | Yes | No |  | Budget / Budget Index Value |
| BudgetIndexValue | Budget Index Value ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Index Value |
| BudgetIndexValue | Budget Index Value RecID | `BudgetIndexValueID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Index Value |
| BudgetIndexValue | Index Value Percent | `IndexValuePercent` | `sTYPE_PERCENTAGE` | Global | Yes | No |  | Budget / Budget Index Value |
| BudgetIndexValue | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Index Value |
| BudgetIndexValue | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Index Value |
| BudgetIndex | Budget Index ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Index |
| BudgetIndex | Budget Index Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Budget / Budget Index |
| BudgetIndex | Budget Index Name | `BudgetIndexName` | `sTYPE_TEXT` | Global | Yes | No |  | Budget / Budget Index |
| BudgetIndex | Budget Index RecID | `BudgetIndexID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Budget / Budget Index |
| BudgetIndex | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Budget / Budget Index |
| BudgetIndex | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Budget / Budget Index |
