# PageLayoutFilter — Data Fields

A conditional display rule on a page layout field — up to two Criteria Type/Value slots and a column sort order, refining what PageLayoutField only partially configures. 16 Global fields under Statics.

**Table Association:** `PageLayoutFilter` &nbsp;·&nbsp; **Total fields:** 16 (Global: 16, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Page Layout Filter Accessor Name | `AccessorName` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Filter Column Order By | `ColumnOrderBy` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Criteria Type #1 | `CriteriaType1` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Criteria Type #2 | `CriteriaType2` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Criteria Value #1 | `CriteriaValue1` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Criteria Value #2 | `CriteriaValue2` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Extended Group Filter | `ExtendedGroupFilterID` | `sTYPE_PAGE_LAYOUT_FILTER` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Field Context | `FieldContext` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Is List Filter? | `IsListFilter` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Filter Page Layout | `PageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Filter RecID | `PageLayoutFilterID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Report Group Available Field | `ReportGroupAvailableFieldID` | `sTYPE_REPORT_GROUP_AVAILABLE_FIELD` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Filter Row Order By | `RowOrderBy` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Show Label? | `ShowLabel` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Filter Show Subtotal? | `ShowSubtotal` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
