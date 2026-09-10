# PageLayoutField — Data Fields

One field's placement configuration within a page layout — accessor name, display label, and up to two Display Option slots for conditional visibility, the join between a Data Field and a specific PageLayout. 27 Global fields under Statics; central to the PAGE-LAYOUTS-01 domain as the record that actually maps a data field onto a rendered screen position.

**Table Association:** `PageLayoutField` &nbsp;·&nbsp; **Total fields:** 27 (Global: 27, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Page Layout Field Accessor Name | `AccessorName` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Budget View | `BudgetViewID` | `sTYPE_BUDGET_VIEW` | Global | No | No |  | Statics / Hidden |
| Page Layout Field ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Field Display Label | `DisplayLabel` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Display Option #1 | `DisplayOption1` | `sTYPE_NUMBER` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Field Display Option #2 | `DisplayOption2` | `sTYPE_NUMBER` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Field Display Option JSON | `DisplayOptionJSON` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Edit Column Position | `EditColumnPosition` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Edit Field Height | `EditFieldHeight` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Edit Field Width | `EditFieldWidth` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Edit Row Position | `EditRowPosition` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Field Context | `FieldContext` | `sTYPE_TEXT` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Header Column Position | `HeaderColumnPosition` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Is In Edit Layout? | `IsInEditLayout` | `sTYPE_BOOLEAN` | Global | No | No |  | Statics / Hidden |
| Page Layout Field JSON Config Text | `JSONConfigText` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Label CSS Style | `LabelCSSStyle` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Mobile Row Position | `MobileRowPosition` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Page Layout | `PageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | Yes | No |  | Statics / Hidden |
| Page Layout Field RecID | `PageLayoutFieldID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Report Group Available Field | `ReportGroupAvailableFieldID` | `sTYPE_REPORT_GROUP_AVAILABLE_FIELD` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Static Text | `StaticText` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Sub Page Layout | `SubPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Statics / Hidden |
| Page Layout Field Value CSS Style | `ValueCSSStyle` | `sTYPE_TEXTAREA` | Global | No | No |  | Statics / Hidden |
| Page Layout Field View Column Position | `ViewColumnPosition` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field View Field Height | `ViewFieldHeight` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field View Field Width | `ViewFieldWidth` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
| Page Layout Field View Row Position | `ViewRowPosition` | `sTYPE_NUMBER` | Global | No | No |  | Statics / Hidden |
