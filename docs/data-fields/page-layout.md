# PageLayout — Data Fields

Platform metadata describing a configured page layout itself — creator/run tracking, edit/create permission flags, and a Budget Column Type association. 42 Global fields under Statics; this is the Manage Page Layouts feature's own field catalog entry, directly relevant to the PAGE-LAYOUTS-01 epic since it defines what metadata exists about a layout record versus what the layout renders.

**Table Association:** `PageLayout` &nbsp;·&nbsp; **Total fields:** 42 (Global: 42, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Statics / Hidden |
| Firm | `FirmID` | `sTYPE_FIRM` | Global | No | No |  | Statics / Hidden |
| Last Run By | `LastRunBy` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| Last Run Date | `LastRunDate` | `sTYPE_TIME` | Global | No | No |  | Statics / Hidden |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Statics / Hidden |
| Page Layout Allow Edit? | `AllowEdit` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Allow User Create? | `AllowUserCreate` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Budget Column Type | `BudgetColumnTypeID` | `sTYPE_BUDGET_COLUMN_TYPE` | Global | No | No |  | Statics / Hidden |
| Page Layout Client List RGD | `ClientListRGDID` | `sTYPE_REPORT_GROUP_DATA` | Global | No | No |  | Statics / Hidden |
| Page Layout ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Computed Sequence Number | `ComputedSequenceNumber` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Created By Member | `CreatedByMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Statics / Hidden |
| Page Layout Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Entity Selection Filter | `EntitySelectionFilter` | `sTYPE_NUMBER` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Equivalent PL Types | `EquivalentPLTypes` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Hierarchy Name | `HierarchyName` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Is Budget Impacting? | `IsBudgetImpacting` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Is Dashboard Report? | `IsDashboardReport` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Is Global Report? | `IsGlobalReport` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Is Menu Link? | `IsMenuLink` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Is Ordered? | `IsOrdered` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Is Report? | `IsReport` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Is SEP/List Layout? | `IsSEPOrListLayout` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Issue Type | `CodeIssueTypeID` | `sCODE_ISSUE_TYPE` | Global | No | No |  | Statics / Hidden |
| Page Layout JSON Config Text | `JSONConfigText` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Name | `PageLayoutName` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Order Record Name | `OrderRecordName` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Order Record Type | `OrderRecordType` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Output Type | `OutputType` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Owned By Member | `OwnedByMemberID` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Parent Page Layout | `ParentPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Statics / Hidden |
| Page Layout ParentID | `ParentID` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Previous Page Layout | `PreviousPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Statics / Hidden |
| Page Layout PreviousID | `PreviousID` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Primary Code SQL Table | `PrimaryCodeSQLTableID` | `sCODE_SQLTABLE` | Global | No | No |  | Statics / Hidden |
| Page Layout RecID | `PageLayoutID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Run Mode Filters | `RunModeFilters` | `sTYPE_NUMBER` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Type | `PageLayoutType` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout URL | `URL` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
