# ReportGroupAvailableField — Data Fields

Metadata about the Data Fields catalog itself — API table name, dropdown table name, field type and definition — meaning this entity is Lucernex describing its own field-metadata system, the same system this documentation set is built from. 27 Global fields under Company Items, directly relevant to understanding how Manage Data Fields (005) is implemented.

**Table Association:** `ReportGroupAvailableField` &nbsp;·&nbsp; **Total fields:** 27 (Global: 27, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Api Table Name | `ApiTableName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Default Value | `DefaultValue` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Definition | `Definition` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Data Fields |
| Dropdown Table Name | `DropdownTableName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Field Name | `AccessorName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Field Type | `FormFieldType` | `sTYPE_ALL_FORMFIELDS` | Global | Yes | No |  | Company Items / Data Fields |
| FieldText | `FieldText` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| FirmID | `FirmID` | `sTYPE_FIRM` | Global | No | No |  | Company Items / Data Fields |
| Global Definition | `GlobalDefinition` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Data Fields |
| Hierarchy Name | `HierarchyName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Is Functional? | `IsFunctional` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Data Fields |
| Is Global Field? | `IsGlobal` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Data Fields |
| Is ReadOnly? | `IsReadOnly` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Data Fields |
| Is Required? | `IsRequired` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Data Fields |
| Is UDF Field? | `IsClientExtensionField` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Data Fields |
| Label | `DefaultLabel` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Data Fields |
| Maximum Length | `MaxLength` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Data Fields |
| Parent Report Group | `ParentReportGroupDataID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Company Items / Data Fields |
| RGAF Created Date | `CreatedDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Data Fields |
| RGAF Modified Date | `ModifiedDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Data Fields |
| Report Field Label | `UILabel` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Report Group | `ReportGroupDataID` | `sTYPE_REPORT_GROUP_DATA` | Global | Yes | No |  | Company Items / Data Fields |
| Script Name | `ScriptName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Table Detail | `TableName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Table Name | `CodeSQLTableID` | `sCODE_SQLTABLE` | Global | Yes | No |  | Company Items / Data Fields |
| Version Added | `VersionAdded` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
| Version Modified | `VersionModified` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Data Fields |
