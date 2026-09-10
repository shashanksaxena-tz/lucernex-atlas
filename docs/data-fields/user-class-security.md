# UserClassSecurity — Data Fields

A named security role/permission class — dashboard component visibility and group hierarchy, referenced by WorkFlowTemplateStep's 'Assignee User Class List' fields. 20 Global fields under Company Items.

**Table Association:** `UserClassSecurity` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Budget Column Type | `BudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Company Items / Security |
| Dashboard Component Title | `DashboardComponentTitle` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Security |
| Group Hierarchy | `GroupHierarchyNoPrefix` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Security |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Security |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Security |
| Name With Full Hierarchy | `GroupHierarchy` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Security |
| Page Layout | `PageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Security |
| Parent Group Name | `ParentGroupName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Security |
| Parent Report Group | `RootReportGroupDataID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Company Items / Security |
| Report Group | `SubReportGroupDataID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Company Items / Security |
| Report Group Available Field | `ReportGroupAvailableFieldID` | `sTYPE_REPORT_GROUP_AVAILABLE_FIELD` | Global | No | No |  | Company Items / Security |
| Report Group Data | `ReportGroupDataID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Company Items / Security |
| Security Level | `SecurityLevelName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Security |
| Security Object Name | `SecurityObjectNameText` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Security |
| Security Privilege | `CodeSecurityPrivilegeID` | `sCODE_SECURITY_PRIVILEGE` | Global | No | No |  | Company Items / Security |
| Security Type | `SecurityType` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Security |
| SecurityLevelByteValue | `SecurityLevelByteValue` | `sTYPE_SECURITY_LEVEL` | Global | No | No |  | Company Items / Security |
| User Class | `CodeUserClassID` | `sCODE_USER_CLASS` | Global | Yes | No |  | Company Items / Security |
| User Class Security ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Security |
| User Class Security RecID | `UserClassSecurityID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Security |
