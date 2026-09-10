# Data Fields — Full Field-Level Reference

This is the authoritative, field-by-field companion to [005-manage-data-fields.md](../admin/005-manage-data-fields.md). That document describes the Manage Data Fields screen narratively (24 top-level groups, dominant table associations, representative examples); this folder tabulates **every one of the 6,158 leaf fields** captured in `data-fields-global-tree-rows.json` (5,953 Global) and `data-fields-firm-tree-rows.json` (205 Firm) so every field is individually inspectable and exportable, not just summarized.

## How this is organized

- **122 entities** (Lucernex `Table Association` values) with 15 or more fields each get their own file — these cover 5486 of 6,158 fields (89%).
- The remaining **92 entities**, each with fewer than 15 fields (672 fields, 11%), are grouped into **8 thematic files** by naming pattern and function (join/`Link*` tables, master code tables, bid-package ancillary tables, workflow/notification ancillary tables, audit/history tables, demographics/site-selection reference tables, budget ancillary tables, and a miscellaneous-small-entities catch-all). Grouping is explained in each bucket file's intro.
- [`INDEX.md`](INDEX.md) (this file) has **one row per distinct Table Association value found in the raw data — all 214 of them** — with field counts and a plain-language explanation, linking to whichever file (standalone or bucket) holds that entity's fields.
- [`all-fields.csv`](all-fields.csv) is every one of the 6,158 fields as one flat, spreadsheet-ready table (`Entity, Label, InternalName, FieldType, Scope, Required, ReadOnly, Default`) — built for the ASG Edge+ vs. Lucernex parity comparison.

## Data-quality notes and reconciliation

- **Row-count reconciliation.** 005 reports 6,297 Global and 549 Firm total hierarchy rows (including the 24 top-level group rows and 320 subgroup rows in *each* scope). Subtracting the non-leaf rows (24 + 320 = 344 per scope) leaves 5953 Global and 205 Firm leaf fields — exactly matching 005's validated leaf-field counts (5,953 / 205) and this folder's 6158-row total.
- **No missing top-level group.** All 24 top-level groups named in 005 are present in both raw JSON captures with the expected leaf counts under them; there is no group-level gap requiring a re-crawl.
- **214 distinct Table Association values** were found across both scopes (Global and Firm leaves combined) — substantially more than the handful named in 005's 'dominant associations' lists, because 005 only called out the top 8 per scope.
- **005's two open questions about Firm-scope naming are now answered from the raw data.** Question 7 ('which three Firm fields do not use the `Firm_` prefix') — they are `zFirm_LeaseSquareFootage` (table `Contract`), `math_Test_0` (table `Allowance`, display label literally "Test"), and `EDGE_ASGCenterID` (table `Location`) — the last one's `EDGE_` prefix is a strong signal it was pushed into Lucernex from an external ASG Edge+ era integration rather than authored natively in Firm Fields. Question 8 ('which two Firm fields have the `TBD` default') — `Firm_SalesReportSignatureName` and `Firm_SalesReportSignatureTitle`, both on `ProjectEntity`.
- **448 distinct Field Type codes** were found (005 only listed the 12 most frequent per scope). The full legend is below.

## Methodology and confidence caveats

Each entity's explanation below is grounded in that entity's actual field labels, group/subgroup placement, and field-type mix (all inspected directly from the raw JSON) plus general commercial real-estate/lease-administration domain knowledge — it is not copied from any Lucernex vendor documentation, which was not available for this exercise. Entities are covered at graduated depth: the largest ~34 (which together account for most of the fields) get multi-sentence explanations; the remaining 88 standalone entities get 2-3 sentence explanations; the 92 small, bucketed entities get one sentence each. The **field type legend** below is similarly inferred from naming convention where not already documented in 005 — flagged inline wherever it is a naming-convention inference rather than a directly observed fact.

## Field type legend

All 448 distinct `Form Field Type` codes found across both scopes, most frequent first. Codes already explained by name — plain data types, computed/math-operation fields, and `sTYPE_<Entity>` / `sCODE_<Name>` lookups — are described directly; where the mapping is inferred purely from the code's naming convention rather than confirmed against vendor documentation, the description says so explicitly.

| Code | Global | Firm | Total | Description |
|---|---:|---:|---:|---|
| `sTYPE_TEXT` | 961 | 83 | 1044 | Free-text input. |
| `sTYPE_MONEY` | 891 | 8 | 899 | Currency amount. |
| `sTYPE_DATE` | 365 | 12 | 377 | Date picker. |
| `sTYPE_NUMBER` | 336 | 12 | 348 | Numeric input. |
| `sTYPE_UNFORMATTED_NUMBER` | 279 | 0 | 279 | Numeric input with no thousands/decimal formatting (often an internal ID or count). |
| `sTYPE_MEMBER` | 261 | 1 | 262 | Lookup reference to an internal Member (Lucernex user) record. |
| `sTYPE_MONEY_MATH_OPERATION` | 258 | 4 | 262 | System-calculated currency amount (computed, not directly entered). |
| `sTYPE_TIME` | 232 | 0 | 232 | Date/time-stamp value (despite the name, typically a full timestamp such as Created/Modified date). |
| `sTYPE_BOOLEAN` | 229 | 0 | 229 | True/false toggle. |
| `sTYPE_PERCENTAGE` | 179 | 9 | 188 | Percentage input. |
| `sTYPE_TEXTAREA` | 158 | 8 | 166 | Multi-line free-text input. |
| `sTYPE_CHECKBOX` | 153 | 2 | 155 | Checkbox (true/false). |
| `sTYPE_PERCENT_MATH_OPERATION` | 134 | 0 | 134 | System-calculated percentage (computed, not directly entered). |
| `sTYPE_CONTRACT` | 62 | 0 | 62 | Lookup reference to a Contract (lease) record. |
| `sTYPE_SUBMITBUTTON` | 62 | 0 | 62 | Form action button that triggers a server-side process — not a stored data value. |
| `sTYPE_CUSTOM_CODE_FIELD` | 1 | 54 | 55 | Dropdown bound to a tenant-defined Custom Code field/list (see Manage Custom Lists, 006). |
| `sTYPE_AREA` | 54 | 0 | 54 | Numeric building/land area measurement (typically square footage) — a plain measurement field, not an entity lookup despite the generic sTYPE_ name. |
| `sTYPE_PAGE_LAYOUT` | 46 | 0 | 46 | Lookup reference to a PageLayout record. |
| `sCODE_CURRENCY_TYPE` | 37 | 0 | 37 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_NUMBER_FRACTION6DIGITS` | 34 | 0 | 34 | Numeric input fixed to 6 decimal places. |
| `sTYPE_PERSON` | 31 | 0 | 31 | Lookup reference to a Person (contact) record. |
| `sTYPE_EMPLOYER` | 26 | 0 | 26 | Lookup reference to an Employer (vendor/landlord/tenant company) record. |
| `sCODE_JOB_TITLE` | 24 | 0 | 24 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_DROPDOWN_YEAR` | 23 | 0 | 23 | Year selected from a dropdown list. |
| `sTYPE_MATH_OPERATION` | 22 | 1 | 23 | System-calculated numeric value (computed, not directly entered). |
| `sCODE_EXPENSE_GROUP` | 20 | 0 | 20 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BUILDING_AREA_UNIT` | 18 | 0 | 18 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_EXPENSE_TYPE` | 18 | 0 | 18 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_PROJECT_ENTITY` | 18 | 0 | 18 | Lookup reference to a ProjectEntity (capital project) record. |
| `sTYPE_BUDGET_COLUMN_TYPE` | 16 | 0 | 16 | Lookup reference to a BudgetColumnType record. |
| `sTYPE_DOCUMENT` | 16 | 0 | 16 | Lookup reference to a Document record. |
| `sCODE_EXCHANGE_RATE_TYPE` | 15 | 0 | 15 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_COVENANT` | 15 | 0 | 15 | Lookup reference to a Covenant record. |
| `sTYPE_STATE_PROVINCE` | 15 | 0 | 15 | State/Province selector. |
| `sTYPE_MONTH_AND_DAY` | 14 | 0 | 14 | Month-and-day selector (no year). |
| `sTYPE_PROGRAM` | 14 | 0 | 14 | Lookup reference to a Program record. |
| `sCODE_USER_CLASS` | 13 | 0 | 13 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_CONTRACT_AMENDMENT` | 13 | 0 | 13 | Lookup reference to a ContractAmendment record. |
| `sTYPE_VENDOR` | 13 | 0 | 13 | Lookup reference to a Vendor record. |
| `sCODE_SALES_GROUP` | 12 | 0 | 12 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_ISSUE` | 12 | 0 | 12 | Lookup reference to an Issue record. |
| `sTYPE_POSTALCODE` | 12 | 0 | 12 | Postal/ZIP code input. |
| `sTYPE_TASK` | 12 | 0 | 12 | Lookup reference to a Task (schedule) record. |
| `sTYPE_YES_NO_RADIO` | 11 | 0 | 11 | Yes/No radio button pair. |
| `sCODE_MONTH_FREQUENCY` | 10 | 0 | 10 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_BUDGET_LINE_ITEM` | 10 | 0 | 10 | Lookup reference to a BudgetLineItem record. |
| `sTYPE_JURISDICTION` | 10 | 0 | 10 | Lookup reference to a Jurisdiction record. |
| `sTYPE_MIXEDENTITY` | 10 | 0 | 10 | Lookup reference that can resolve to more than one entity type depending on context. |
| `sCODE_MARKET_AREA` | 9 | 0 | 9 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_COUNTRY` | 9 | 0 | 9 | Country selector. |
| `sTYPE_DATE_MATH_OPERATION` | 9 | 0 | 9 | System-calculated date (computed, not directly entered). |
| `sTYPE_ENTITY_NAME` | 9 | 0 | 9 | Read-only display of a linked entity's name. |
| `sTYPE_EXPENSE_SETUP` | 9 | 0 | 9 | Lookup reference to an ExpenseSetup record. |
| `sTYPE_NUMBER_FRACTION2DIGITS` | 7 | 2 | 9 | Numeric input fixed to 2 decimal places. |
| `sTYPE_PERIOD_YEAR` | 9 | 0 | 9 | Accounting period/year selector. |
| `sTYPE_REGION` | 9 | 0 | 9 | Lookup reference to a Region record. |
| `sTYPE_REPORT_GROUP_DATA` | 9 | 0 | 9 | Lookup reference to a ReportGroupData (field-catalog group) record. |
| `sCODE_EXPENSE_CATEGORY` | 8 | 0 | 8 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RESPONSIBLE_PARTY` | 8 | 0 | 8 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_PARCEL` | 8 | 0 | 8 | Lookup reference to a Parcel record. |
| `sCODE_CONDITION` | 7 | 0 | 7 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_JOB_FUNCTION` | 7 | 0 | 7 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_DOCUMENT_LIST` | 7 | 0 | 7 | Multi-select list of Document records. |
| `sTYPE_FACILITY` | 7 | 0 | 7 | Lookup reference to a Facility record. |
| `sTYPE_NUMBER_FRACTION0DIGITS` | 7 | 0 | 7 | Numeric input fixed to 0 decimal places. |
| `sTYPE_ORGANIZATION` | 7 | 0 | 7 | Lookup reference to an Organization record. |
| `sCODE_ASSET_CATEGORY` | 6 | 0 | 6 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FREQUENCY` | 6 | 0 | 6 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_BUDGET_COLUMN` | 6 | 0 | 6 | Lookup reference to a BudgetColumn record. |
| `sTYPE_BUDGET_VIEW` | 6 | 0 | 6 | Lookup reference to a BudgetView record. |
| `sTYPE_CLIENT_LISTS` | 0 | 6 | 6 | Dropdown bound to a tenant-defined Client (Custom) Drop Down list (see Firm & Client Drop Downs, 007). |
| `sTYPE_DATE_RANGE` | 6 | 0 | 6 | Date range (begin/end) picker. |
| `sTYPE_EQUIPMENT` | 6 | 0 | 6 | Lookup reference to an equipment/Asset record. |
| `sTYPE_MONTH` | 6 | 0 | 6 | Month selector. |
| `sTYPE_TIMEZONE` | 6 | 0 | 6 | Time zone selector. |
| `sCODE_ACCOUNTING_METHOD` | 5 | 0 | 5 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASC842_SCHEDULE` | 5 | 0 | 5 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_IFRS16_SCHEDULE` | 5 | 0 | 5 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PROJECT_TYPE` | 5 | 0 | 5 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SQLTABLE` | 5 | 0 | 5 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_USAGE_GROUP` | 5 | 0 | 5 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_USAGE_UNIT_TYPE` | 5 | 0 | 5 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_BUDGET_TEMPLATE` | 5 | 0 | 5 | Lookup reference to a Budget Template record. |
| `sTYPE_CONTRACT_TERM` | 5 | 0 | 5 | Lookup reference to a ContractTerm record. |
| `sTYPE_FOLDER` | 5 | 0 | 5 | Lookup reference to a Folder record. |
| `sTYPE_PASS_FAIL` | 5 | 0 | 5 | Pass/Fail radio button pair. |
| `sTYPE_QUARTERS_YEAR` | 5 | 0 | 5 | Calendar quarter/year period selector. |
| `sTYPE_SCENARIO` | 5 | 0 | 5 | Lookup reference to a Scenario record. |
| `sTYPE_TASK_CREATION_METHOD` | 5 | 0 | 5 | Selector for how a Task is auto-generated. |
| `sTYPE_WORK_FLOW_TEMPLATE_STEP` | 5 | 0 | 5 | Lookup reference to a WorkFlowTemplateStep record. |
| `sCODE_MARKET_TYPE` | 4 | 0 | 4 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PRIORITY` | 4 | 0 | 4 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PRORATION_METHOD` | 4 | 0 | 4 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SL_SCHEDULE` | 4 | 0 | 4 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TIME_UNIT` | 4 | 0 | 4 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_BID_PACKAGE` | 4 | 0 | 4 | Lookup reference to a BidPackage record. |
| `sTYPE_BROKER` | 4 | 0 | 4 | Lookup reference to a broker contact record. |
| `sTYPE_COMPLEX` | 4 | 0 | 4 | Lookup reference to a Complex (multi-building property) record. |
| `sTYPE_FISCAL_YEAR` | 4 | 0 | 4 | Fiscal year selector. |
| `sTYPE_LAWYER` | 4 | 0 | 4 | Lookup reference to an attorney contact record. |
| `sTYPE_LOCATION` | 4 | 0 | 4 | Lookup reference to a Location record. |
| `sTYPE_PROTOTYPE` | 4 | 0 | 4 | Lookup reference to a Prototype (standard design) record. |
| `sTYPE_RE_TRANSACTION` | 4 | 0 | 4 | Lookup reference to a RETransaction record. |
| `sCODE_AREA` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BUDGET_COLUMN_STATUS` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CONSTRUCTION_TYPE` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CONTACT_TYPE` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CONTRACT_USE` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DISTRIBUTION_CENTER` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FREQUENCY_UNIT` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LAND_AREA_UNIT` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LAST_ACTION_STATUS` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_MAINTENANCE_REMEDY` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PR_FREQUENCY` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_REGION` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TASK_STATUS` | 3 | 0 | 3 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_BID_PACKAGE_TEMPLATE` | 3 | 0 | 3 | Lookup reference to a BidPackageTemplate record. |
| `sTYPE_CUSTOM_CODE_TABLE_REF` | 3 | 0 | 3 | Reference to a tenant-defined Custom Code table (see 006). |
| `sTYPE_DATE_DAYS_MATH_OPERATION` | 3 | 0 | 3 | System-calculated date offset by a number of days. |
| `sTYPE_EXPENSE_ACCRUAL_SETUP` | 3 | 0 | 3 | Lookup reference to an ExpenseAccrualSetup record. |
| `sTYPE_FIRM` | 3 | 0 | 3 | Lookup reference to the tenant Firm configuration record. |
| `sTYPE_FIRM_LOGO` | 0 | 3 | 3 | Firm logo image upload. |
| `sTYPE_FORM_PAGE_LAYOUT` | 3 | 0 | 3 | Lookup reference to a form-type PageLayout record. |
| `sTYPE_HOLIDAY_SCHEDULE` | 3 | 0 | 3 | Lookup reference to a HolidaySchedule record. |
| `sTYPE_KEY_DATE` | 3 | 0 | 3 | Lookup reference to a KeyDate record. |
| `sTYPE_MONTHS_YEAR` | 3 | 0 | 3 | Calendar month/year period selector. |
| `sTYPE_PAYMENT_TRANSACTION` | 3 | 0 | 3 | Lookup reference to a PaymentTransaction record. |
| `sTYPE_PHOTO` | 3 | 0 | 3 | Image/photo upload. |
| `sTYPE_PROCESS_TIMELINE` | 3 | 0 | 3 | Lookup reference to a ProcessTimeline record. |
| `sTYPE_REPORT_GROUP_AVAILABLE_FIELD` | 3 | 0 | 3 | Lookup reference to a ReportGroupAvailableField (data-field catalog) record. |
| `sTYPE_ROOT_REGION` | 3 | 0 | 3 | Lookup reference to a top-level Region record. |
| `sTYPE_SUBREGION` | 3 | 0 | 3 | Lookup reference to a child Region record. |
| `sTYPE_WORK_FLOW_TEMPLATE` | 3 | 0 | 3 | Lookup reference to a WorkFlowTemplate record. |
| `sTYPE_WORK_FLOW_TEMPLATE_STEP_ACTION` | 3 | 0 | 3 | Lookup reference to a WorkFlowTemplateStepAction record. |
| `sCODE_ACCOUNTING_ADJUSTMENT_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ACCRUAL_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_APPROVAL_STATUS` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_APPROVAL_STATUS_EXPRECOVERY` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_GROUP` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BUILDING_CLASS` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COVENANT_CATEGORY` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COVENANT_GROUP` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COVENANT_STATUS` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COVENANT_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CPI_INDEX` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DEAL_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LOCK_OUT_REASON` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PAYMENT_METHOD` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PERCENTAGE_RENT_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PROJECT_PHASE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RECOVERY_GROUP` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RECOVERY_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SALES_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SCENARIO_DEAL_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SECURITY_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TERM_STATUS` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TERM_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_USE_RENT_MODEL_TYPE` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_WORK_FLOW_STATUS` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ZONING` | 2 | 0 | 2 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_ASSET` | 2 | 0 | 2 | Lookup reference to an Asset record. |
| `sTYPE_CODE_CONTACT_TYPE_LIST` | 2 | 0 | 2 | Multi-select list of contact-type code values. |
| `sTYPE_COUNTRY_ONLY` | 2 | 0 | 2 | Country selector (no state/province paired field). |
| `sTYPE_CURRENT_DATE` | 2 | 0 | 2 | Read-only, auto-populated with today's date. |
| `sTYPE_DMA` | 2 | 0 | 2 | Lookup reference to a DMA (Designated Market Area) record. |
| `sTYPE_DROPDOWN_PERIOD` | 2 | 0 | 2 | Accounting period selected from a dropdown list. |
| `sTYPE_EXPENSE_RECOVERY` | 2 | 0 | 2 | Lookup reference to an ExpenseRecovery record. |
| `sTYPE_EXPENSE_SCHEDULE` | 2 | 0 | 2 | Lookup reference to an ExpenseSchedule record. |
| `sTYPE_LINK_REGION_MARKET` | 2 | 0 | 2 | Lookup reference to a LinkRegionMarket record. |
| `sTYPE_MINISCHEDULE` | 2 | 0 | 2 | Compact inline schedule/grid widget. |
| `sTYPE_NULL_CHECKBOX` | 2 | 0 | 2 | Three-state checkbox (true/false/unset). |
| `sTYPE_OPERATING_STATUS` | 2 | 0 | 2 | Operating-status selector (active/inactive-style). |
| `sTYPE_OWNER` | 2 | 0 | 2 | Lookup reference to a property owner contact record. |
| `sTYPE_PASSWORD` | 2 | 0 | 2 | Masked password input. |
| `sTYPE_PERCENT_OR_AMOUNT` | 2 | 0 | 2 | Toggle field accepting either a percentage or a flat amount. |
| `sTYPE_PE_MEMBER` | 2 | 0 | 2 | Lookup reference to a Member in a ProjectEntity team-assignment role. |
| `sTYPE_PORTFOLIO` | 2 | 0 | 2 | Lookup reference to a portfolio-level ProjectEntity record. |
| `sTYPE_PORTFOLIO_LIST` | 2 | 0 | 2 | Multi-select list of portfolio-level ProjectEntity records. |
| `sTYPE_PROJECT_MANAGER` | 2 | 0 | 2 | Lookup reference to a project manager (Member) record. |
| `sTYPE_PROPERTY_TAX_ASSESSMENT` | 2 | 0 | 2 | Lookup reference to a PropertyTaxAssessment record. |
| `sTYPE_PROPERTY_TAX_BILL` | 2 | 0 | 2 | Lookup reference to a PropertyTaxBill record. |
| `sTYPE_PURCHASE_ORDER` | 2 | 0 | 2 | Lookup reference to a PurchaseOrder record. |
| `sTYPE_SCHEDULED_OFFSET` | 2 | 0 | 2 | Lookup reference to a ScheduledOffset record. |
| `sTYPE_SL_SUMMARY` | 2 | 0 | 2 | Lookup reference to an SLSummary record. |
| `sTYPE_TASK_TEMPLATE` | 2 | 0 | 2 | Lookup reference to a Task Template record. |
| `sTYPE_VALUES_PROVIDER` | 2 | 0 | 2 | Configuration hook supplying a dynamic list of values to another field. |
| `sTYPE_WORK_FLOW_STEP` | 2 | 0 | 2 | Lookup reference to a WorkFlowStep record. |
| `sCODE_ADJUSTMENT_METHOD` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_AGREEMENT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ALLOWANCE_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ALLOWANCE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ALT_RENT_MATH` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_AMENDMENT_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_AMENDMENT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ANALYTICS_ROLE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_APPROVAL_STATUS_MEMBER_EQUIPMENT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_APPROVAL_STATUS_MEMBER_RE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_CLASS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_DEPARTMENT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_OPERATION_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_PRODUCT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_SUSPENSION_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ASSET_TYPE_TEST` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BASE_YEAR_AMOUNT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BID_GRACE_PERIOD_TIME_UNIT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BID_PACKAGE_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BUDGET_CHANGE_REASON` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_BUDGET_VALUE_UNITS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CALCULATION_METHOD` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CAP_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CLASSIFICATION` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COMPETITOR_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COMPLEX_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COMPLEX_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CONTRACT_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CONTRACT_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CONTRACT_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CONTRACT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COVENANT_TEMPLATE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_COVERAGE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CO_TENANCY_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CO_TENANCY_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_CSI` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DAY_OF_WEEK` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DECISION_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DEMOGRAPHIC_RESULTS_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DENOMINATOR` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DISTANCE_UNIT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DOCUMENT_ACTION` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DOCUMENT_CONVERT_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_DOCUMENT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ESCALATION_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ESCALATION_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ESCALATION_PAYMENT_METHOD` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ESCALATION_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_EVALUATION_RATING` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_EXCLUSION_CAP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_EXPENSE_ACCT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_EXP_REC_BASED_ON` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FACILITY_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FACILITY_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FACILITY_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FACILITY_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FACILITY_USE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FINANCIAL_ADJUSTMENT_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FOLDER_TEMPLATE_ACTION` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_FUNDING_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_GUARANTEE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_HOLDING_INTEREST` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INDEX_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INDEX_SOURCE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INDEX_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INSPECTION_PERIOD_START` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INSPECTION_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INSURANCE_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INSURANCE_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INSURANCE_POLICY_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INSURANCE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_INVOICE_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ISSUE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_KEY_DATE_ACTION` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_KEY_DATE_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_KEY_DATE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LEASE_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LEASE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LOCATION_ACCESS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LOCATION_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LOCATION_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LOCATION_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LOCATION_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_LOCATION_USE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_MARKET_DEMOGRAPHICS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_MASTER_EMPLOYER_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_MEASUREMENT_UNIT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_MEMBER_ACTION` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_OFFSET_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_OFFSET_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ORG_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ORG_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_ORG_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_ACCESS_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_ACCESS_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_ACCESS_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARCEL_USE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARKING_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARKING_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARTY_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PARTY_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PASS_THROUGH_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PLAN_FORECAST_BASED_ON` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PLAN_FORECAST_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PROBLEM` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PROPERTY_PRIMARY_USE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PROPERTY_TAX_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PROPERTY_TAX_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PROPERTY_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PRO_FORMA_BUDGET_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_PRO_RATA_SHARE_METHOD` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RECEIPT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RECOVERY_ITEM_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RECOVERY_ITEM_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RECOVERY_SECTION` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RESPONSE_TIME` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RESPONSIBILITY_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RESPONSIBILITY_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RESPONSIBLE_PARTY_SYSTEM` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RESULTS_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_RE_TRANSACTION_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SALES_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SCENARIO_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SCHEDULE_CREATION_REASON` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SECURITY_DEPOSIT_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SECURITY_DEPOSIT_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SECURITY_DEPOSIT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SECURITY_PRIVILEGE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SITE_RATING` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SLOT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SOURCE_ENTITY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SPACE_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SPACE_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SPACE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SPACE_USE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SRQ_SOURCE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SRQ_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_SRQ_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_STORE_PHASE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_STORE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TASK_LEAD_LAG_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TAX_APPEAL_RESULT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TAX_APPEAL_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TAX_PAID_TO` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TAX_REFUND_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TAX_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TENANT_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TENANT_GROUP` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TENANT_STATUS` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TENANT_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_TENANT_USE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_THIRD_PARTY_VENDOR` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_UNIT_SALES_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_USAGE_CATEGORY` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_USAGE_TYPE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_VENDOR_GRADE` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sCODE_WEIGHT_UNIT` | 1 | 0 | 1 | Dropdown selection from a fixed platform master/reference code list (see Firm & Client Drop Downs, 007) — inferred from naming. |
| `sTYPE_ACREAGE` | 1 | 0 | 1 | Land area input in acres. |
| `sTYPE_ACTION_RUN_REPORT` | 1 | 0 | 1 | Action button that runs a report — not a stored data value. |
| `sTYPE_ACTIVEINACTIVE_PROJECT` | 1 | 0 | 1 | ProjectEntity lookup restricted by active/inactive status. |
| `sTYPE_ALLMONTHS` | 1 | 0 | 1 | Grid widget for entering a value per calendar month. |
| `sTYPE_ALLOWANCE` | 1 | 0 | 1 | Lookup reference to an Allowance record. |
| `sTYPE_ALLPERIODS` | 1 | 0 | 1 | Grid widget for entering a value per accounting period. |
| `sTYPE_ALLQUARTERS` | 1 | 0 | 1 | Grid widget for entering a value per calendar quarter. |
| `sTYPE_ALL_FORMFIELDS` | 1 | 0 | 1 | Meta-selector listing every field on the current form (layout-configuration use). |
| `sTYPE_ALTERNATE_RENT_SCHEDULE` | 1 | 0 | 1 | Lookup reference to an AlternateRentSchedule record. |
| `sTYPE_ANNUAL_VARIANCE` | 1 | 0 | 1 | Computed year-over-year variance value. |
| `sTYPE_BIDDER_BUDGET` | 1 | 0 | 1 | Lookup reference to a bidder's submitted budget detail. |
| `sTYPE_BIDDER_ISSUE` | 1 | 0 | 1 | Lookup reference to a BidderIssue record. |
| `sTYPE_BIDDER_LAYOUT` | 1 | 0 | 1 | Lookup reference to a bidder-facing page layout. |
| `sTYPE_BID_PACKAGE_ALTERNATE` | 1 | 0 | 1 | Lookup reference to a BidPackageAlternate record. |
| `sTYPE_BID_PACKAGE_BREAKOUT` | 1 | 0 | 1 | Lookup reference to a BidPackageBreakout record. |
| `sTYPE_BLANK_ROW` | 1 | 0 | 1 | Form-layout spacer row — not a stored data value. |
| `sTYPE_BLANK_SPACE` | 1 | 0 | 1 | Form-layout spacer element — not a stored data value. |
| `sTYPE_BUDGET_COLUMN_ITEM_COMMENT` | 1 | 0 | 1 | Free-text comment attached to a BudgetColumnItemValue grid cell. |
| `sTYPE_BUDGET_COLUMN_ITEM_VALUE` | 1 | 0 | 1 | Lookup reference to a BudgetColumnItemValue (budget grid cell) record. |
| `sTYPE_BUDGET_COLUMN_TOTAL` | 1 | 0 | 1 | System-calculated total across a BudgetColumn's line items (computed, not directly entered). |
| `sTYPE_BUDGET_INDEX` | 1 | 0 | 1 | Lookup reference to a BudgetIndex record. |
| `sTYPE_BUDGET_OPTION` | 1 | 0 | 1 | Lookup reference to a BudgetOption record. |
| `sTYPE_CAPITALPROGRAM` | 1 | 0 | 1 | Lookup reference to a capital Program record. |
| `sTYPE_CITY` | 1 | 0 | 1 | City name input. |
| `sTYPE_CODE_ASSET_CATEGORY_LIST` | 1 | 0 | 1 | Multi-select list of CodeAssetCategory values. |
| `sTYPE_COMPANY_TYPE` | 1 | 0 | 1 | Company-type selector. |
| `sTYPE_COMPARISONLIST` | 1 | 0 | 1 | Multi-select list used to build a comparison report. |
| `sTYPE_COMP_ASSUMPTIONS` | 1 | 0 | 1 | Assumptions block for a comparison analysis. |
| `sTYPE_COMP_EXPENSE_GROUP` | 1 | 0 | 1 | Expense-group selector scoped to a comparison analysis. |
| `sTYPE_DATEPATTERN` | 1 | 0 | 1 | Format-pattern selector governing how a related date field displays. |
| `sTYPE_DEVELOPMENT_PLAN` | 1 | 0 | 1 | Lookup reference to a DevelopmentPlan record. |
| `sTYPE_DOCUMENT_SLIDESHOW` | 1 | 0 | 1 | Slideshow viewer widget for a set of Document image attachments. |
| `sTYPE_DOCUMENT_VIEWLINK` | 1 | 0 | 1 | Read-only link that opens a Document for viewing. |
| `sTYPE_EMAIL_RECEIVED_LOG` | 1 | 0 | 1 | Lookup reference to an EMailReceivedLog record. |
| `sTYPE_EMP_JOB_FUNCTION_LIST` | 1 | 0 | 1 | Multi-select list of job functions available to an Employer. |
| `sTYPE_EMP_JOB_TITLE_LIST` | 1 | 0 | 1 | Multi-select list of job titles available to an Employer. |
| `sTYPE_EMP_USER_CLASS_LIST` | 1 | 0 | 1 | Multi-select list of security user classes available to an Employer. |
| `sTYPE_ENTITY_EMAIL` | 1 | 0 | 1 | Email address linked to an entity record. |
| `sTYPE_ENTITY_TEMPLATE` | 1 | 0 | 1 | Lookup reference to an Entity Template record. |
| `sTYPE_EQUIPMENT_CONTRACT` | 1 | 0 | 1 | Lookup reference to an equipment-financing Contract record. |
| `sTYPE_ESCALATION_INDEX` | 1 | 0 | 1 | Lookup reference to an EscalationIndex record. |
| `sTYPE_EXPACCRUAL_FORECAST_TABLE` | 1 | 0 | 1 | Lookup reference to an expense-accrual forecast period record. |
| `sTYPE_EXPENSE_ACCRUAL_SCHEDULE` | 1 | 0 | 1 | Lookup reference to an ExpenseAccrualSchedule record. |
| `sTYPE_EXPENSE_ESCALTION_TYPE` | 1 | 0 | 1 | Lookup reference to an ExpenseEscalation type/record. |
| `sTYPE_EXPENSE_FORECAST_TABLE` | 1 | 0 | 1 | Lookup reference to an expense forecast period record. |
| `sTYPE_EXPENSE_RECOVERY_ITEM` | 1 | 0 | 1 | Lookup reference to an ExpenseRecoveryItem record. |
| `sTYPE_FINANCIALMODEL` | 1 | 0 | 1 | Lookup reference to a financial model configuration. |
| `sTYPE_FOLDER_TEMPLATE` | 1 | 0 | 1 | Lookup reference to a Folder Template record. |
| `sTYPE_FULL_FOLDER_LIST` | 1 | 0 | 1 | Multi-select list of Folder records (full hierarchy). |
| `sTYPE_GLOBAL_PROPERTY_SECTION` | 1 | 0 | 1 | Selector over GlobalProperty configuration sections. |
| `sTYPE_INVOICE_ISSUE` | 1 | 0 | 1 | Lookup reference to an InvoiceIssue record. |
| `sTYPE_ISSUE_DATE_FILTER` | 1 | 0 | 1 | Date filter scoped to Issue records. |
| `sTYPE_ISSUE_DATE_RANGE` | 1 | 0 | 1 | Date-range filter scoped to Issue records. |
| `sTYPE_ISSUE_RESPONSE` | 1 | 0 | 1 | Lookup reference to an IssueResponse record. |
| `sTYPE_JAVASCRIPT` | 1 | 0 | 1 | Embedded script hook — not a stored data value. |
| `sTYPE_JAVASCRIPT_FIELD` | 1 | 0 | 1 | Field-level scripted value/behavior hook (see Value Javascript in 005) — not a stored data value. |
| `sTYPE_LANDLORD` | 1 | 0 | 1 | Lookup reference to a landlord contact record. |
| `sTYPE_LANDLORD_INVOICE` | 1 | 0 | 1 | Lookup reference to a LandlordInvoice record. |
| `sTYPE_LANDLORD_INVOICE_ITEM` | 1 | 0 | 1 | Lookup reference to a LandlordInvoiceItem record. |
| `sTYPE_LAND_PURCHASE_SUMMARY` | 1 | 0 | 1 | Lookup reference to a LandPurchaseSummary record. |
| `sTYPE_LANGUAGE` | 1 | 0 | 1 | Language selector. |
| `sTYPE_MANYTOMANY_LIST` | 1 | 0 | 1 | Generic many-to-many multi-select list. |
| `sTYPE_MONTHS_WITH_DATA` | 1 | 0 | 1 | Month selector restricted to months that have recorded data. |
| `sTYPE_NOTIFY_TEMPLATE` | 1 | 0 | 1 | Lookup reference to a NotifyTemplate record. |
| `sTYPE_NUMBERPATTERN` | 1 | 0 | 1 | Format-pattern selector governing how a related number field displays. |
| `sTYPE_NUMBER_FRACTION5DIGITS` | 1 | 0 | 1 | Numeric input fixed to 5 decimal places. |
| `sTYPE_ONETOMANY_LIST` | 1 | 0 | 1 | Generic one-to-many multi-select list. |
| `sTYPE_PAGEBREAK` | 1 | 0 | 1 | Form-layout page-break control — not a stored data value. |
| `sTYPE_PAGE_LAYOUT_FILTER` | 1 | 0 | 1 | Lookup reference to a PageLayoutFilter record. |
| `sTYPE_PART` | 1 | 0 | 1 | Lookup reference to a Part record. |
| `sTYPE_PART_PACKAGE` | 1 | 0 | 1 | Lookup reference to a PartPackage record. |
| `sTYPE_PAYMENT_RECEIPT` | 1 | 0 | 1 | Lookup reference to a PaymentReceipt record. |
| `sTYPE_PERCENTAGE_2DIGITS` | 1 | 0 | 1 | Percentage input fixed to 2 decimal places. |
| `sTYPE_PERCENTAGE_RENT` | 1 | 0 | 1 | Lookup reference to a PercentageRent record. |
| `sTYPE_PE_CONTACTEMPLOYER_LIST` | 1 | 0 | 1 | Multi-select list of ProjectEntity contact/employer records. |
| `sTYPE_PHONE` | 1 | 0 | 1 | Phone number input. |
| `sTYPE_PROCESS_TIMELINE_TEMPLATE` | 1 | 0 | 1 | Lookup reference to a ProcessTimelineTemplate record. |
| `sTYPE_PROPERTY_MANAGER` | 1 | 0 | 1 | Lookup reference to a property manager contact record. |
| `sTYPE_PROPERTY_TAX_APPEAL` | 1 | 0 | 1 | Lookup reference to a PropertyTaxAppeal record. |
| `sTYPE_PROPERTY_TAX_SUMMARY` | 1 | 0 | 1 | Lookup reference to a PropertyTaxSummary record. |
| `sTYPE_QUARTER_VARIANCE` | 1 | 0 | 1 | Computed quarter-over-quarter variance value. |
| `sTYPE_RECALC_NOTES` | 1 | 0 | 1 | Lookup reference to a RecalcOverrideNotes record. |
| `sTYPE_RESPONSIBILITY` | 1 | 0 | 1 | Lookup reference to a Responsibility record. |
| `sTYPE_RETRAN_CONTACT` | 1 | 0 | 1 | Lookup reference to a ReTransScenContact record. |
| `sTYPE_SALES_EXCLUSION_CAP` | 1 | 0 | 1 | Lookup reference to a SalesExclusionCap record. |
| `sTYPE_SECURITY_LEVEL` | 1 | 0 | 1 | Security access-level selector. |
| `sTYPE_SEMIANNUAL_VARIANCE` | 1 | 0 | 1 | Computed half-year-over-half-year variance value. |
| `sTYPE_SERVICE_REQUEST` | 1 | 0 | 1 | Lookup reference to a ServiceRequest record. |
| `sTYPE_SPACE` | 1 | 0 | 1 | Lookup reference to a Space record. |
| `sTYPE_STATE_PROVINCE_LIST` | 1 | 0 | 1 | Multi-select list of State/Province values. |
| `sTYPE_STATICTEXT_LABEL` | 1 | 0 | 1 | Static display label — not a stored data value. |
| `sTYPE_SUB_EDITFORM` | 1 | 0 | 1 | Embedded child-record edit form — not itself a stored data value. |
| `sTYPE_TIME_MATH_OPERATION` | 1 | 0 | 1 | System-calculated time value. |
| `sTYPE_TOTAL_MATH_OPERATION` | 1 | 0 | 1 | System-calculated running/aggregate total. |
| `sTYPE_WORK_FLOW` | 1 | 0 | 1 | Lookup reference to a WorkFlow (running instance) record. |
| `sTYPE_WORK_FLOW_APPROVER_LIST` | 1 | 0 | 1 | Multi-select list of workflow approvers. |
| `sTYPE_YEARS` | 1 | 0 | 1 | Year selector. |
| `sTYPE_YEARS_WITH_DATA` | 1 | 0 | 1 | Year selector restricted to years that have recorded data. |
| `sTYPE_YMAP` | 1 | 0 | 1 | Year-keyed map/grid widget for entering per-year values. |

## All entities (one row per Table Association)

Sorted by total field count, largest first. **Detail file** links to the entity's own file for standalone entities (≥15 fields), or to the shared bucket file for the 92 small entities — the bucket name is noted in parentheses.

| Entity | Total | Global | Firm | Detail file | What it is and why it has this many fields |
|---|---:|---:|---:|---|---|
| `ExpenseRecovery` | 567 | 558 | 9 | [ExpenseRecovery](expense-recovery.md) | The CAM/OpEx recovery engine for a lease — one record per recoverable expense category (CAM, taxes, insurance, HVAC, etc.) per contract per year, carrying the base year, cap formula (percent or dollar, per-period or cumulative), pro rata share method, gross-up rules, and admin fee. It is by far the largest entity in the catalog (567 fields, 92% Global) because commercial CAM reconciliation is one of the most negotiated and variably-structured terms in a lease — every landlord uses a different combination of caps, exclusions, base-year stops, and gross-up methodologies, and Lucernex models each variant as its own field rather than a generic formula, which is why nearly half the fields are `MONEY_MATH_OPERATION`/`PERCENT_MATH_OPERATION` computed values. |
| `Contract` | 402 | 255 | 147 | [Contract](contract.md) | The lease/contract header record itself — the central entity the rest of the schema hangs off of. It mixes core lease terms (dates, base rent, discount rate, renewal options) with dozens of Boolean 'in lease?' flags (Automatic Renewal In Lease?, Bargain Renewal In Lease?) that record whether a clause exists versus whether it has been exercised, plus `SUBMITBUTTON` fields that are workflow triggers rather than data. At 402 fields (255 Global + 147 Firm) it is also the entity this tenant has customized the most — 147 of the 205 total Firm-scope fields attach here, confirming Contract is where ASG has extended Lucernex's base model with tenant-specific CAM, co-tenancy, and delivery-requirement fields. |
| `LeaseInfo` | 218 | 218 | 0 | [LeaseInfo](lease-info.md) | A negotiation-history snapshot living under the Pro Forma Lease group — it captures the same handful of deal terms (abatement, rent, TI allowance) at multiple negotiation checkpoints (Broker Recommended, Landlord Asking, Final Terms), each as its own field triple. All 218 fields are Global with none in Firm scope, meaning this negotiation-tracking structure is a fixed platform feature ASG has not customized. It exists to preserve what was offered versus what was countered versus what was ultimately agreed, which is otherwise lost once a lease is executed and only the final terms remain on Contract. |
| `ProjectEntity` | 170 | 165 | 5 | [ProjectEntity](project-entity.md) | The generic 'project' record used for capital projects, store rollouts, and portfolio initiatives — distinct from Contract, it tracks phase-gate status (Design, Construction, Possession, Operations) via parallel status/date pairs and milestone pointers, plus `SUBMITBUTTON` action fields for phase transitions. It spans four top-level groups (Milestones, Schedule, Statics, Summary Information), which is unusual and reflects that a 'project' is a cross-cutting concept touched by scheduling, milestone tracking, and portfolio reporting rather than owned by a single functional group. 170 fields. |
| `SLSummary` | 135 | 135 | 0 | [SLSummary](sl-summary.md) | Straight-line rent summary — one record per contract holding forward-looking cash and interest expense projected out fiscal-year by fiscal-year (Current, Beyond Fifth, Beyond Sixth) and quarter by quarter within the current year, used for ASC 842/IFRS 16 disclosure schedules. All 135 fields are Global `MONEY` values; this is a reporting rollup table, not a transactional one, which is why there are no Boolean flags or codes — every field is a pre-calculated dollar amount for a specific future period. |
| `Asset` | 126 | 126 | 0 | [Asset](asset.md) | The fixed-asset/ROU-asset record tied to a lease or equipment contract — accounting begin/end dates, discount rate overrides, depreciation dates, sale price, and current payment amounts. 126 fields, entirely Global, spanning Equipment/Assets, Statics, and Summary Information, reflecting that an Asset is simultaneously an accounting construct (depreciation, discount rate), a physical-equipment record, and a portfolio summary line. |
| `PaymentTransaction` | 118 | 118 | 0 | [PaymentTransaction](payment-transaction.md) | Individual rent/expense payment or receipt records against a contract — up to eight parallel 'Account Number #N' fields for split GL coding, allocation amounts, and payment dates. 118 fields, all Global. The repeated-numbered-field pattern (Account Number #1 through #8) is common across the financial entities in this catalog and indicates Lucernex models multi-line allocation as fixed parallel columns rather than a normalized child table exposed to this catalog. |
| `ExpenseSetup` | 105 | 103 | 2 | [ExpenseSetup](expense-setup.md) | The recurring-expense billing configuration for a contract (insurance, taxes, CAM billed directly rather than through recovery) — coverage period begin markers for every possible billing frequency (Annual, Q1-Q4, both Semi-Annual halves) so the same setup record can support annual, quarterly, or semi-annual billing without changing schema. 105 fields split 103 Global / 2 Firm, and it appears under both the Contract group and the Wizard group — meaning this configuration also drives a guided lease-setup wizard flow, not just the standing contract record. |
| `ContractFinancialTest` | 92 | 92 | 0 | [ContractFinancialTest](contract-financial-test.md) | The ASC 842 / IFRS 16 lease-classification and present-value calculation record for a contract — initial asset and liability balances, PV of financial terms before and after adjustments, and the aggregate lease value under each standard. 92 Global fields; the near-identical field pairs prefixed 'ASC 842' and (by pattern) 'IFRS 16' show Lucernex runs the same lease-accounting calculation twice per contract, once under each standard, so a tenant reporting under only one standard still carries both sets of fields. |
| `Facility` | 89 | 88 | 1 | [Facility](facility.md) | The physical property/building record — address fields (Street Address #1-3, City, State, Postal Code, Jurisdiction) plus facility-level dates and area figures. 89 fields (88 Global, 1 Firm) under its own top-level Facility group; this is the most 'plain real estate' entity in the catalog, closer to a CRM property record than a financial one, which is reflected in the dominance of `TEXT` and `DATE` field types over `MONEY`. |
| `Program` | 85 | 85 | 0 | [Program](program.md) | A capital/rollout program header — the container above ProjectEntity for a slate of related capital projects, carrying its own page-layout assignments (Cap Project Setup Page Layout, Cap Project Map Setup Layout) and exchange-rate-type overrides per cost category (Asset Amortization, Asset Balance, Cash Expenses) with matching '(Translation)' fields for multi-currency portfolios. 85 Global fields under Program Summary Information; the page-layout fields here are notable because they mean a Program's own metadata determines which page layout its child projects render with, tying this entity directly into the PAGE-LAYOUTS-01 configuration domain. |
| `Member` | 78 | 78 | 0 | [Member](member.md) | The internal user/employee account record for Lucernex itself (not a lease party) — login and access-control fields (Accept EULA?, Always Spell Check?, Color Scheme) alongside org fields (Code Job Function, Code Analytics Role) and billing rates. 78 Global fields under Company Items; this is user-account metadata rather than lease data, included in the catalog because Member records are referenced everywhere else (Created By, Modified By, approvers, assignees) via `sTYPE_MEMBER` lookup fields. |
| `SLPeriod` | 78 | 78 | 0 | [SLPeriod](sl-period.md) | Period-level straight-line rent detail underlying SLSummary — one record per accounting period per contract carrying asset/liability balance, amortization expense, and both the current-currency and '- Translated' value pair for every monetary field, plus 12-Month Forward Change figures used for disclosure roll-forwards. 78 Global fields; where SLSummary is the fiscal-year rollup, SLPeriod is the period-by-period ledger that rollup is built from. |
| `SiteSurvey` | 78 | 78 | 0 | [SiteSurvey](site-survey.md) | Site-selection/demographic evaluation data for a candidate location — household income and count at 1/3/5-mile radii, median age, and condition-code ratings, used during real estate site selection before a lease is signed. 78 Global fields under its own Site Survey group; the repeated '-1 Mile/-3 Miles/-5 Miles' field triples show Lucernex bakes fixed trade-area radii into the schema rather than storing a single configurable radius. |
| `Parcel` | 74 | 74 | 0 | [Parcel](parcel.md) | The land-parcel record, distinct from Facility (building) and Location (site) — address fields plus parcel-specific attributes like Demographic DMA linkage, used primarily for ground-lease and land-purchase scenarios and as the anchor for the large PropertyTax* family (Assessment, Bill, Summary, Appeal, ParcelAccess). 74 Global fields under its own Parcel group. |
| `Employer` | 71 | 66 | 5 | [Employer](employer.md) | The vendor/landlord/tenant company record — banking details (Bank Account Number, Bank Routing Number), AP vendor number, and document-access permission flags (Allow Employees Upload/Download access to Employer Documents). 71 fields (66 Global, 5 Firm) under Company Items; this is the counterparty master record referenced by Contract, PaymentTransaction, and most financial entities whenever a payee or lessor needs to be identified. |
| `Scenario` | 70 | 70 | 0 | [Scenario](scenario.md) | A deal/transaction scenario under RE Transaction — comparative what-if terms (Broker Commission, Capital Required, Annual Total Rent) for a prospective site or renewal being evaluated before commitment, plus site demographic fields (Average HH Income, Block) inherited from the site-selection process. 70 Global fields; Scenario sits upstream of Contract in the deal lifecycle, modeling terms under negotiation rather than terms in force. |
| `VirtualSalesPeriod` | 66 | 66 | 0 | [VirtualSalesPeriod](virtual-sales-period.md) | A computed (non-stored, 'Virtual') period record projecting percentage-rent breakpoints and sales-based rent obligations forward — up to eight numbered Breakpoint Amount/Rate slots per period. 66 Global fields under Contract; 'Virtual' entities in this catalog are calculated projections generated at read-time rather than persisted transactional rows, which is why none of them appear in Firm scope (a tenant cannot customize a calculation the platform generates). |
| `VirtualUsagePeriod` | 66 | 66 | 0 | [VirtualUsagePeriod](virtual-usage-period.md) | The usage-based-rent counterpart to VirtualSalesPeriod — projects breakpoint cost tiers (with 6-decimal-precision `NUMBER_FRACTION6DIGITS` fields for unit-cost rates) period by period for contracts billed on usage/consumption rather than sales volume. 66 Global fields under Contract. |
| `Location` | 66 | 61 | 5 | [Location](location.md) | A general site/location record — address and geocoding fields (Latitude, Longitude) plus percentage-based site metrics — used as a lighter-weight alternative to Facility for sites that are tracked before or without a full facility record. 66 fields (61 Global, 5 Firm) under its own Location group. |
| `WorkFlowTemplateStep` | 59 | 59 | 0 | [WorkFlowTemplateStep](work-flow-template-step.md) | One approval step within a reusable workflow template — approver/assignee configuration exposed as four parallel list-type fields per role (Approver Job Title List, Approver Member List, Approver Type, Approver User Class List) so a single step can route to a named person, a job title, a user class, or a mix. 59 Global fields under Company Items; this is template design-time metadata, distinct from WorkFlowStep which is the runtime instance of a step actually executing against a real contract or task. |
| `AccrualTransaction` | 54 | 54 | 0 | [AccrualTransaction](accrual-transaction.md) | An individual expense-accrual posting tied to a contract, carrying up to eight parallel Account Number fields for GL split coding, matching the same allocation pattern seen in PaymentTransaction. 54 Global fields under Contract. |
| `BidPackage` | 53 | 53 | 0 | [BidPackage](bid-package.md) | The competitive-bid solicitation record for a capital project — ranked bidder results (1st Place Bidder Name/Amount, and by pattern 2nd/3rd) plus its own page-layout assignment (Bid Award and Cancellation Layout) and approval-status/date fields for the award decision. 53 Global fields under Specialized Forms; it anchors a large ancillary family (BidPackageTemplate, BidderIssue, BidPackageAlternate/Breakout and their Value variants) that model the line items and alternates within a single bid. |
| `WorkFlowStep` | 53 | 53 | 0 | [WorkFlowStep](work-flow-step.md) | The runtime instance of one workflow step executing against a real record — computed alert/warn/due dates for approvers and assignees, checkout tracking (CheckedOutByMemberID), and a pointer back to the WorkFlowTemplateStep it was instantiated from. 53 Global fields spanning Statics and Workflow groups. |
| `ExpenseSchedule` | 51 | 51 | 0 | [ExpenseSchedule](expense-schedule.md) | The recurring expense-billing schedule generated from an ExpenseSetup — per-period billed amounts, adjustment method and type (for escalating charges), and tax amount fields (Calculated Tax Amount #1-3+) for jurisdictions with multiple tax components. 51 Global fields under Contract and Summary Information. |
| `ExpenseRecoveryItem` | 46 | 46 | 0 | [ExpenseRecoveryItem](expense-recovery-item.md) | The line-item detail underneath ExpenseRecovery — one record per actual-vs-budget variance calculation (A-B, A-P, B-P Variance Amount/Percent), admin fee, and approved pro rata share, used during CAM reconciliation to compare what a tenant was billed against what was approved. 46 Global fields under Contract; naming convention (A=Actual, B=Budget, P=Prior, based on context) mirrors standard CAM reconciliation worksheet columns. |
| `ProFormaBudget` | 46 | 46 | 0 | [ProFormaBudget](pro-forma-budget.md) | The financial feasibility analysis for a prospective deal or capital project — IRR, NPV, and Payback Period alongside a Finance Committee Approval flag, gating whether a deal proceeds. 46 Global fields under Summary Information, dominated by `MONEY` fields (36 of 46) since this is fundamentally a discounted-cash-flow worksheet. |
| `Complex` | 45 | 45 | 0 | [Complex](complex.md) | A multi-building property complex/campus record sitting above Facility in the property hierarchy — complex-level classification and status fields plus a linked Person (likely site or leasing contact). 45 Global fields under its own Complex group. |
| `Covenant` | 45 | 38 | 7 | [Covenant](covenant.md) | A lease covenant/compliance obligation (financial ratio tests, use restrictions, exclusivity clauses) tied to a Contract — covenant amount/area, category, and an associated document reference for the underlying clause. 45 fields (38 Global, 7 Firm) spanning Contract and Wizard groups, and one of the entities the user named as expected — the Firm extension here likely reflects tenant-specific covenant categories not in the base platform list. |
| `PercentageRent` | 44 | 41 | 3 | [PercentageRent](percentage-rent.md) | The percentage/sales-based rent clause on a retail lease — cap amount/frequency, audit-right flag, and billing frequency, linked to Covenant for cross-referencing compliance obligations tied to the same clause. 44 fields (41 Global, 3 Firm) under Contract; it is the clause-level configuration that VirtualSalesPeriod and PercentageRentBreakpoint project forward from. |
| `PageLayout` | 42 | 42 | 0 | [PageLayout](page-layout.md) | Platform metadata describing a configured page layout itself — creator/run tracking, edit/create permission flags, and a Budget Column Type association. 42 Global fields under Statics; this is the Manage Page Layouts feature's own field catalog entry, directly relevant to the PAGE-LAYOUTS-01 epic since it defines what metadata exists about a layout record versus what the layout renders. |
| `KeyDate` | 41 | 31 | 10 | [KeyDate](key-date.md) | A tracked deadline/notice date tied to a Contract, Contract Term, or Covenant — action date/period (with a configurable period unit: days, months, etc.), earliest notice date, and coverage period bounds, used to drive renewal, termination, and compliance-notice alerts. 41 fields (31 Global, 10 Firm) under Contract; one of the entities the user specifically flagged, and its 10 Firm fields suggest ASG tracks additional tenant-specific deadline types beyond the base platform set. |
| `Tenant` | 41 | 41 | 0 | [Tenant](tenant.md) | The sub-tenant/occupant record under a Facility (for landlords or sub-lease scenarios) — headcount capacity fields (Capacity #1-4, calcTotalHeadcount) and a Contract linkage. 41 Global fields under Facility. |
| `PropertyTaxAppeal` | 40 | 40 | 0 | [PropertyTaxAppeal](property-tax-appeal.md) | A property-tax assessment appeal filed against a Parcel — filing date, appraisal fee, attorney fee, and the resulting assessment reduction, anchoring a sub-family (PropertyTaxAppealAward) for tracking the appeal's financial outcome. 40 Global fields under Parcel. |
| `WorkFlowTemplateStepAction` | 39 | 39 | 0 | [WorkFlowTemplateStepAction](work-flow-template-step-action.md) | The button/action definition available at a workflow template step (Approve, Reject, Send Back) — Boolean flags controlling what the action does to the workflow (Should Close Work Flow?, Should Move to Next Step, Should Restart the Step?) plus finance-specific behavior like FIFO pay-app validation and auto-copy of amounts. 39 Global fields under Company Items and Statics. |
| `PercentageRentBreakpoint` | 39 | 39 | 0 | [PercentageRentBreakpoint](percentage-rent-breakpoint.md) | The natural-breakpoint configuration for a percentage-rent clause — up to eight numbered Breakpoint Amount/Count slots defining the sales tiers at which the percentage rate changes. 39 Global fields under Contract, the static configuration that VirtualPercentageRentPeriod projects forward period by period. |
| `Person` | 37 | 37 | 0 | [Person](person.md) | An individual contact record (broker, attorney, property manager) distinct from Employer (the company) and Member (internal user) — billing rates, multiple email/phone slots, and job-title code linkage. 37 Global fields under Company Items. |
| `VirtualPercentageRentPeriod` | 37 | 37 | 0 | [VirtualPercentageRentPeriod](virtual-percentage-rent-period.md) | The computed period-by-period projection of PercentageRentBreakpoint tiers, following the same Virtual-entity pattern as VirtualSalesPeriod. 37 Global fields under Contract. |
| `Task` | 37 | 37 | 0 | [Task](task.md) | A schedule/project task record — baseline vs. actual dates and durations, lead/lag days, and resource unit tracking, the core row of the project-scheduling module (paired with TaskPredecessor for dependency chains). 37 Global fields under Schedule and Statics. |
| `BudgetColumnType` | 34 | 34 | 0 | [BudgetColumnType](budget-column-type.md) | The template defining what a Budget Column represents (multi-select allowed, one-instance-only, editable) — configuration metadata one level above the individual BudgetColumn records. 34 Global fields under Budget and Statics. |
| `LandPurchaseSummary` | 34 | 34 | 0 | [LandPurchaseSummary](land-purchase-summary.md) | The land-acquisition deal record for ground purchases — asking price, acreage, and commencement date, anchoring the Purchase Management group alongside Ownership and DevelopmentPlan. 34 Global fields. |
| `Responsibility` | 33 | 33 | 0 | [Responsibility](responsibility.md) | Defines which party (landlord/tenant) is responsible for a cost category on a lease, with cap amount/percent limits — the allocation-of-obligation record that ExpenseRecovery and FinancialAdjustment calculations reference. 33 Global fields under Contract and Wizard. |
| `LinkReTransScenContact` | 32 | 32 | 0 | [LinkReTransScenContact](link-re-trans-scen-contact.md) | A join record linking a real-estate transaction Scenario to a contact (broker, attorney) with contact-type classification and email. 32 Global fields under RE Transaction — despite the Link-style name, at 32 fields it is treated as standalone rather than folded into the small Link bucket. |
| `LandlordInvoice` | 31 | 31 | 0 | [LandlordInvoice](landlord-invoice.md) | An invoice received from a landlord for billing outside the standard recovery/rent cycle — coverage period and allocation-status amounts, anchoring LandlordInvoiceItem as its line-item detail. 31 Global fields under Contract. |
| `PropertyTaxBill` | 31 | 31 | 0 | [PropertyTaxBill](property-tax-bill.md) | A property tax bill issued against a Parcel — discount amount/date/rate for early-payment discounts, feeding into PropertyTaxSummary. 31 Global fields under Parcel. |
| `PropertyTaxSummary` | 31 | 31 | 0 | [PropertyTaxSummary](property-tax-summary.md) | The rollup of assessment amount/percent and billing frequency for a Parcel's property tax obligation across bills and appeals. 31 Global fields under Parcel. |
| `BidPackageTemplate` | 31 | 31 | 0 | [BidPackageTemplate](bid-package-template.md) | A reusable bid solicitation template — pre-assigns the page layouts used at each stage of a bid (Award, Invitation) and default budget view/column types, so a new BidPackage doesn't need each layout chosen manually. 31 Global fields under Specialized Forms. |
| `ExpenseAccrualSchedule` | 30 | 30 | 0 | [ExpenseAccrualSchedule](expense-accrual-schedule.md) | The generated period-by-period accrual schedule from an ExpenseAccrualSetup — accrual rate and annual amount per begin period/year. 30 Global fields under Contract. |
| `ExpenseAccrualSetup` | 30 | 30 | 0 | [ExpenseAccrualSetup](expense-accrual-setup.md) | The configuration for accruing an expense ahead of its billing (common for property tax and insurance accrued monthly against an annual bill) — accrual message, area-unit basis, and begin period. 30 Global fields under Contract. |
| `UseBasedRentBreakpoint` | 30 | 30 | 0 | [UseBasedRentBreakpoint](use-based-rent-breakpoint.md) | The tiered-cost-per-unit configuration for usage-based rent, mirroring PercentageRentBreakpoint's structure but keyed to consumption cost rather than sales. 30 Global fields under Contract. |
| `ProcessTimeline` | 30 | 30 | 0 | [ProcessTimeline](process-timeline.md) | A generic milestone/phase timeline attached to a Location or ProjectEntity — actual vs. baseline vs. original end dates and duration, spanning the Location and Milestones groups since timelines apply to both site selection and construction phases. 30 Global fields. |
| `DevelopmentSlot` | 30 | 30 | 0 | [DevelopmentSlot](development-slot.md) | A build-out slot within a development pipeline plan — assigned broker/project, current revenue weeks, and duration, feeding ProgramRevenueWeeks reporting. 30 Global fields under RE Planner. |
| `RETransaction` | 30 | 30 | 0 | [RETransaction](re-transaction.md) | The formal real-estate transaction record once a Scenario converts into an active deal — approved capital budget, deal schedule, and begin date. 30 Global fields under RE Transaction; sits between Scenario (evaluation) and Contract (executed lease) in the deal lifecycle. |
| `ServiceRequest` | 30 | 30 | 0 | [ServiceRequest](service-request.md) | A facilities service/maintenance ticket tied to an Asset or Contract — approval date/party, asset group/type, anchoring WorkOrder as the dispatched work resulting from the request. 30 Global fields under Specialized Forms. |
| `ContractTerm` | 29 | 26 | 3 | [ContractTerm](contract-term.md) | One renewal/extension term option on a lease — average rent per area unit and area-unit basis, linked to Amendment and Covenant, appearing under both Contract and Wizard (the guided lease-entry flow). 29 fields (26 Global, 3 Firm). |
| `CodeExpenseType` | 29 | 29 | 0 | [CodeExpenseType](code-expense-type.md) | Master expense-category configuration — AP export account/tax numbers for up to several slots, defining how each expense type maps to the general ledger on export. 29 Global fields under Contract, despite the 'Code' prefix this is a substantial configuration table rather than a small reference list, so it is kept standalone rather than folded into the small Code/Reference bucket. |
| `WorkOrder` | 29 | 29 | 0 | [WorkOrder](work-order.md) | The dispatched maintenance work order resulting from a ServiceRequest — actual completion date, cost, labor hours, and vendor assignment. 29 Global fields under Specialized Forms. |
| `LandlordInvoiceItem` | 28 | 28 | 0 | [LandlordInvoiceItem](landlord-invoice-item.md) | Line-item detail under a LandlordInvoice — allocated vs. unallocated amount and comments per line. 28 Global fields under Contract. |
| `ReTransScenContact` | 28 | 28 | 0 | [ReTransScenContact](re-trans-scen-contact.md) | Contact record specific to a real-estate transaction scenario (distinct from LinkReTransScenContact, the join-style variant) — contact type, employer name, email. 28 Global fields under RE Transaction. |
| `CostTrackingTemplate` | 27 | 27 | 0 | [CostTrackingTemplate](cost-tracking-template.md) | A reusable cost-tracking configuration for capital projects — which budget column represents 'Approved Change Order' and how variance is calculated, applied across ProjectEntity records. 27 Global fields under Company Items. |
| `ReportGroupAvailableField` | 27 | 27 | 0 | [ReportGroupAvailableField](report-group-available-field.md) | Metadata about the Data Fields catalog itself — API table name, dropdown table name, field type and definition — meaning this entity is Lucernex describing its own field-metadata system, the same system this documentation set is built from. 27 Global fields under Company Items, directly relevant to understanding how Manage Data Fields (005) is implemented. |
| `ExpenseEscalation` | 27 | 27 | 0 | [ExpenseEscalation](expense-escalation.md) | An automatic escalation clause on a recoverable expense — base amount/year, cap amount/percentage, and begin date, distinct from CPI-indexed escalation (see the small CPI entity). 27 Global fields under Contract. |
| `Sales` | 27 | 27 | 0 | [Sales](sales.md) | Reported retail sales figures for a location, feeding percentage-rent calculations — currency type, fiscal period/year, and a client-assigned sales ID for reconciling against a tenant's own sales report. 27 Global fields under Contract. |
| `PageLayoutField` | 27 | 27 | 0 | [PageLayoutField](page-layout-field.md) | One field's placement configuration within a page layout — accessor name, display label, and up to two Display Option slots for conditional visibility, the join between a Data Field and a specific PageLayout. 27 Global fields under Statics; central to the PAGE-LAYOUTS-01 domain as the record that actually maps a data field onto a rendered screen position. |
| `CoTenancy` | 26 | 26 | 0 | [CoTenancy](co-tenancy.md) | A co-tenancy clause (rent reduction if an anchor tenant vacates) — anchor name, co-tenancy amount/area, and begin date, one of the seven Firm-editable Contract subgroups per 005. 26 Global fields under Contract. |
| `Insurance` | 26 | 26 | 0 | [Insurance](insurance.md) | Required insurance coverage terms on a lease — certificate received/request dates, required flag, and whether the agent is also the named insured. 26 Global fields under Contract, anchoring VendorInsurance as the actual policy-level detail. |
| `Space` | 26 | 26 | 0 | [Space](space.md) | A leasable space/suite record within a Facility — area unit and Contract linkage, more granular than Facility itself for multi-tenant buildings. 26 Global fields under Facility. |
| `BudgetLineItem` | 25 | 25 | 0 | [BudgetLineItem](budget-line-item.md) | One line item within a budget template — alert threshold, category code, and template linkage; the line-item layer beneath BudgetColumn/BudgetColumnType. 25 Global fields under Budget. |
| `WorkFlowTemplate` | 25 | 25 | 0 | [WorkFlowTemplate](work-flow-template.md) | The top-level workflow definition (the container for WorkFlowTemplateStep records) — active layout, associated task, and auto-assignment rules for the initiator. 25 Global fields under Company Items. |
| `SecurityDeposit` | 25 | 24 | 1 | [SecurityDeposit](security-deposit.md) | Security/damage deposit tracking on a lease — deposit amount, account number, and Covenant linkage for deposits tied to compliance conditions. 25 fields (24 Global, 1 Firm) under Contract. |
| `Competitor` | 25 | 25 | 0 | [Competitor](competitor.md) | A competing retailer/property tracked for market analysis — name, type, and building area unit, used in site-selection and demographic comparison work. 25 Global fields under Summary Information. |
| `Firm` | 24 | 23 | 1 | [Firm](firm.md) | The tenant-company configuration record — one row per Lucernex client firm, holding default page-layout assignments per module (Facility Setup Page, Equipment Contract Setup Page) and default folder security. 24 fields (23 Global, 1 Firm) spanning Company Items, Statics, and Summary Information; this is the master firm-level settings record, not to be confused with the 'Firm' scope of this whole catalog. |
| `AlternateRentSchedule` | 24 | 24 | 0 | [AlternateRentSchedule](alternate-rent-schedule.md) | An alternate/contingency rent calculation method available on a contract — alt rent math formula selection and begin date. 24 Global fields under Contract. |
| `PropertyTaxAssessment` | 24 | 24 | 0 | [PropertyTaxAssessment](property-tax-assessment.md) | The underlying assessed value detail for a Parcel — land, improvements, and adjustment components of the total assessment, feeding PropertyTaxBill and PropertyTaxSummary. 24 Global fields under Parcel. |
| `LinkMemberProjectEntity` | 24 | 24 | 0 | [LinkMemberProjectEntity](link-member-project-entity.md) | A join record linking an internal Member to a ProjectEntity in an org-chart role — manager name/title and job function, despite the Link-style name it carries enough project-team detail (24 fields) to warrant standalone treatment. 24 Global fields spanning Statics and Summary Information. |
| `SalesExclusionCap` | 22 | 22 | 0 | [SalesExclusionCap](sales-exclusion-cap.md) | A cap limiting how much sales can be excluded from percentage-rent calculation (e.g., online/catalog sales exclusions) — cap amount/percent and begin date. 22 Global fields under Contract. |
| `UseBasedRent` | 22 | 22 | 0 | [UseBasedRent](use-based-rent.md) | The usage-based rent clause header (e.g., per-unit, per-transaction rent) — billing frequency and currency type, the clause-level record UseBasedRentBreakpoint and VirtualUseBasedRentPeriod project from. 22 Global fields under Contract. |
| `VirtualUseBasedRentPeriod` | 22 | 22 | 0 | [VirtualUseBasedRentPeriod](virtual-use-based-rent-period.md) | The computed period projection of UseBasedRentBreakpoint tiers, following the same Virtual-entity calculation pattern. 22 Global fields under Contract. |
| `Document` | 22 | 22 | 0 | [Document](document.md) | The document/file metadata record used across the platform — author, checkout status (Checked Out By Member, Checked Out Date) for document locking during edits. 22 Global fields under Documents. |
| `InvoiceIssue` | 22 | 22 | 0 | [InvoiceIssue](invoice-issue.md) | An invoice batch header for accounts-payable processing — batch date/number and currency type, anchoring InvoiceItem as line-level detail. 22 Global fields under Specialized Forms. |
| `Allowance` | 21 | 17 | 4 | [Allowance](allowance.md) | A tenant-improvement or other landlord allowance on a lease — allowance type/group classification and begin date. 21 fields (17 Global, 4 Firm) under Contract; one of the entities the user specifically named, and its Firm extension (Firm_AllowCostPSF per 005's representative examples) shows ASG tracks a cost-per-square-foot calculation the base platform doesn't. |
| `CodeASC842Schedule` | 21 | 21 | 0 | [CodeASC842Schedule](code-asc842-schedule.md) | A reusable amortization-schedule template for ASC 842 reporting — 'Don't Amortize Asset Value' flag plus a large block of numbered GL Export Account slots for mapping schedule output to different ledger accounts. 21 Global fields under Contract. |
| `CodeIFRS16Schedule` | 21 | 21 | 0 | [CodeIFRS16Schedule](code-ifrs16-schedule.md) | The IFRS 16 counterpart to CodeASC842Schedule, structurally identical (same export-account slot pattern) but for the international standard. 21 Global fields under Contract. |
| `CodeSLSchedule` | 21 | 21 | 0 | [CodeSLSchedule](code-sl-schedule.md) | The pre-ASC-842/pre-IFRS-16 straight-line schedule template, structurally identical to the two standard-specific schedules — Lucernex evidently kept the legacy SL schedule type alongside both new-standard schedule types rather than replacing it. 21 Global fields under Contract. |
| `FacilityExpense` | 21 | 21 | 0 | [FacilityExpense](facility-expense.md) | A non-recovered operating expense tracked directly against a Facility rather than through a Contract's ExpenseRecovery — actual vs. budgeted amount and description. 21 Global fields under Facility. |
| `BudgetColumn` | 20 | 20 | 0 | [BudgetColumn](budget-column.md) | One column within a capital project budget (e.g., 'Original Budget', 'Approved Change Orders') — status, type, and an 'Allow UI Edit?' flag, the representative example walked through in 005's own documentation. 20 Global fields under Budget. |
| `BudgetColumnItemValue` | 20 | 20 | 0 | [BudgetColumnItemValue](budget-column-item-value.md) | The actual dollar value at the intersection of a BudgetLineItem and a BudgetColumn — the individual cell in the budget grid. 20 fields under Budget and Statics. |
| `EmployerSite` | 20 | 20 | 0 | [EmployerSite](employer-site.md) | A specific site/location belonging to an Employer (useful when a vendor has multiple branch offices) — business unit and currency type per site. 20 Global fields under Company Items. |
| `UserClassSecurity` | 20 | 20 | 0 | [UserClassSecurity](user-class-security.md) | A named security role/permission class — dashboard component visibility and group hierarchy, referenced by WorkFlowTemplateStep's 'Assignee User Class List' fields. 20 Global fields under Company Items. |
| `VirtualExpenseForecastPeriod` | 20 | 20 | 0 | [VirtualExpenseForecastPeriod](virtual-expense-forecast-period.md) | A forward-looking forecast of recoverable expense by calendar month/year and expense category, computed rather than stored. 20 Global fields under Contract. |
| `PaymentReceipt` | 20 | 20 | 0 | [PaymentReceipt](payment-receipt.md) | Money received from a tenant/payer (the inverse of PaymentTransaction) — allocated/unallocated amount and bank account/routing number for the depositing account. 20 Global fields under Contract. |
| `BidderIssue` | 20 | 20 | 0 | [BidderIssue](bidder-issue.md) | One bidder's response to a BidPackage — conditioned bid amount and allow-conditioning flag, letting a bidder submit a qualified rather than firm bid. 20 Global fields under Specialized Forms. |
| `WorkFlow` | 20 | 20 | 0 | [WorkFlow](work-flow.md) | The active workflow instance running against a real trigger object (Trigger CodeSQLTable, Trigger Object) — the runtime record one level above WorkFlowStep. 20 Global fields under Statics and Workflow. |
| `ContractAmendment` | 19 | 17 | 2 | [ContractAmendment](contract-amendment.md) | A formal amendment/modification to an executed lease — amendment group/number/type classification and base-amount change. 19 fields (17 Global, 2 Firm) under Contract. |
| `VariableRentOffset` | 19 | 19 | 0 | [VariableRentOffset](variable-rent-offset.md) | A rent offset tied to a variable expense group/type (rent that adjusts based on a specific expense category rather than CPI or sales). 19 Global fields under Contract. |
| `VirtualPRAccrualPeriod` | 19 | 19 | 0 | [VirtualPRAccrualPeriod](virtual-pr-accrual-period.md) | The computed period projection of percentage-rent accrual, showing this-period, prior-periods, and total accrual amounts. 19 Global fields under Contract. |
| `ParcelAccess` | 19 | 19 | 0 | [ParcelAccess](parcel-access.md) | An access easement or right-of-way record on a Parcel — effective/expire date and associated document. 19 Global fields under Parcel. |
| `PurchaseOrder` | 19 | 19 | 0 | [PurchaseOrder](purchase-order.md) | A capital-project purchase order — approved change order amount and estimate amount, tied into the ChangeOrder/CostTrackingTemplate variance-tracking chain. 19 Global fields under Specialized Forms. |
| `WorkFlowStepApprover` | 19 | 19 | 0 | [WorkFlowStepApprover](work-flow-step-approver.md) | One named approver's action on a running WorkFlowStep — action comment, action taken, and has-approved flag, the audit trail of an individual approval decision. 19 Global fields under Workflow. |
| `AcctingAssumptionAdjust` | 18 | 18 | 0 | [AcctingAssumptionAdjust](accting-assumption-adjust.md) | A manual adjustment to lease-accounting assumptions used in ASC 842/IFRS 16 calculations — adjustment percent and annual amount, letting an accountant override a calculated assumption. 18 Global fields under Contract. |
| `FinancialAdjustment` | 18 | 18 | 0 | [FinancialAdjustment](financial-adjustment.md) | A manual dollar adjustment to an Asset's or Contract's financial position — accounting adjustment type and amount. 18 Global fields under Contract. |
| `SalesExclusion` | 18 | 18 | 0 | [SalesExclusion](sales-exclusion.md) | An individual excluded sales category feeding into a SalesExclusionCap total. 18 Global fields under Contract. |
| `ScheduledOffset` | 18 | 18 | 0 | [ScheduledOffset](scheduled-offset.md) | A pre-scheduled (as opposed to variable) rent offset — cap amount per month/percent and allocation tracking. 18 Global fields under Contract. |
| `Parking` | 18 | 18 | 0 | [Parking](parking.md) | Parking-facility detail under a Facility record — currency type and description for parking-related costs/revenue. 18 Global fields under Facility. |
| `Organization` | 17 | 17 | 0 | [Organization](organization.md) | A broader organizational entity (parent company, franchise group) above Employer — up to several numbered Account Number slots mirroring the financial entities' split-coding pattern. 17 Global fields under Company Items. |
| `TemplateAudit` | 17 | 17 | 0 | [TemplateAudit](template-audit.md) | An audit trail of when a BudgetTemplate/EntityTemplate/FolderTemplate was applied to a new project — applied date and whether folder structure was copied. 17 Global fields under Company Items. |
| `PropertyTaxAppealAward` | 17 | 17 | 0 | [PropertyTaxAppealAward](property-tax-appeal-award.md) | The financial outcome of a PropertyTaxAppeal — actual/estimated award date and award/award-fee amount. 17 Global fields under Parcel. |
| `InvoiceItem` | 17 | 17 | 0 | [InvoiceItem](invoice-item.md) | Line-item detail under an InvoiceIssue batch — GL number and invoice amount per line. 17 Global fields under Specialized Forms. |
| `VirtualTemplateBudgetOption` | 16 | 16 | 0 | [VirtualTemplateBudgetOption](virtual-template-budget-option.md) | Read-only projection of a budget template's metadata (name, description, notes, and Cap Program/Cap Project applicability flags) surfaced for selection during project setup, distinct from the persisted BudgetLineItem/BudgetColumn records it configures. 16 Global fields under Company Items. |
| `VirtualTemplateBudget` | 16 | 16 | 0 | [VirtualTemplateBudget](virtual-template-budget.md) | Near-identical structure to VirtualTemplateBudgetOption; the two likely back two different UI pickers (a single-select field vs. an option list) over the same underlying budget template metadata. 16 Global fields under Company Items. |
| `DiscountRate` | 16 | 16 | 0 | [DiscountRate](discount-rate.md) | A named discount-rate configuration (by country and accounting method) used in NPV/present-value calculations across ContractFinancialTest and ProFormaBudget. 16 Global fields under Company Items. |
| `FiscalPeriod` | 16 | 16 | 0 | [FiscalPeriod](fiscal-period.md) | The fiscal calendar definition — begin/end date and days-in-period per named fiscal period, the calendar backbone that SLPeriod, ExpenseSchedule, and Sales fiscal-period fields reference. 16 Global fields under Company Items. |
| `Part` | 16 | 16 | 0 | [Part](part.md) | An equipment/maintenance parts-catalog record — cost, manufacturer, and model number, supporting the Equipment/Assets maintenance workflow. 16 Global fields under Company Items. |
| `Folder` | 16 | 16 | 0 | [Folder](folder.md) | A document-management folder — downloadable flag and folder-template linkage, the container Document records live in. 16 Global fields under Documents. |
| `PageLayoutFilter` | 16 | 16 | 0 | [PageLayoutFilter](page-layout-filter.md) | A conditional display rule on a page layout field — up to two Criteria Type/Value slots and a column sort order, refining what PageLayoutField only partially configures. 16 Global fields under Statics. |
| `VirtualTemplateFolder` | 15 | 15 | 0 | [VirtualTemplateFolder](virtual-template-folder.md) | Read-only projection of FolderTemplate metadata (name, description, Cap Program/Cap Project applicability), the folder-template counterpart to VirtualTemplateBudget. 15 Global fields under Company Items. |
| `VirtualTemplateSchedule` | 15 | 15 | 0 | [VirtualTemplateSchedule](virtual-template-schedule.md) | Read-only projection of a schedule-template's metadata, completing the Virtual*Template trio alongside VirtualTemplateBudget and VirtualTemplateFolder. 15 Global fields under Company Items. |
| `VendorInsurance` | 15 | 15 | 0 | [VendorInsurance](vendor-insurance.md) | The actual insurance policy detail for a vendor/employer (as opposed to Insurance, which is the lease's required-coverage terms) — aggregate occurrence amount and policy type/dates. 15 Global fields under Company Items. |
| `ExpenseVendorAllocation` | 15 | 15 | 0 | [ExpenseVendorAllocation](expense-vendor-allocation.md) | Allocation of a recoverable expense to a specific paying vendor — AP vendor number and begin/end date. 15 Global fields under Contract. |
| `VirtualPRPAggregate` | 15 | 15 | 0 | [VirtualPRPAggregate](virtual-prp-aggregate.md) | An aggregated percentage-rent obligation projection across a contract's full term — current offset amount and current percentage rent obligation/paid. 15 Global fields under Contract. |
| `Prototype` | 15 | 15 | 0 | [Prototype](prototype.md) | A standardized store/facility design template used for rollout programs — approved flag, average project cost/duration, and default construction type/distribution center. 15 Global fields under its own Prototype group. |
| `ChangeOrder` | 15 | 15 | 0 | [ChangeOrder](change-order.md) | A cost change against an active capital project — approved amount, sequence number, and cost-tracking-variance linkage back to CostTrackingTemplate. 15 Global fields under Specialized Forms. |
| `AuditColumn` | 14 | 14 | 0 | [Audit & History Tables](audit-history-tables.md) | Metadata defining which columns on a table are tracked for audit history — accessor name and audit action per tracked field. |
| `ExpenseAllocation` | 14 | 14 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Splits one recoverable expense across multiple contracts/entities by percentage — the allocation record for shared-building expenses. |
| `PropertyTaxDetail` | 14 | 14 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Free-form notes detail attached to a Parcel's property tax record. |
| `ProgramRevenueWeeks` | 14 | 14 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Weekly revenue-target tracking (filled/unfilled targets and weeks) for a development Program, feeding DevelopmentSlot planning. |
| `TaskPredecessor` | 14 | 14 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Defines a dependency between two Task records, with actual lead/lag days — the scheduling-network edge beneath Task. |
| `PayApp` | 14 | 14 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | An AIA-style payment application against a construction contract — invoice retainage and cost-tracking variance. |
| `EMailReceivedLog` | 14 | 14 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A logged inbound email tied to a record — arrival date and body, the source EMailReceivedLog rows LinkEMailReceivedLogDocument attaches Documents to. |
| `CustomCodeField` | 13 | 13 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | Meta-definition of a tenant-created custom code/dropdown field — the schema record behind Manage Custom Lists (see 006). |
| `AllowanceTransaction` | 13 | 13 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | An individual draw/payment transaction against an Allowance — due date and linkage back to the Allowance and Contract. |
| `VirtualExpAccrualForecastPeriod` | 13 | 13 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A computed forward forecast of an expense accrual by period, referencing the ExpenseAccrualSchedule/Setup it projects from. |
| `LinkLandlordInvPaymentTxn` | 13 | 13 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a LandlordInvoiceItem to the PaymentTransaction that paid it — allocation amount and date. |
| `Usage` | 13 | 13 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A recorded consumption/usage reading against a contract on a given posting date, feeding usage-based rent calculations. |
| `VirtualUBRPAggregate` | 13 | 13 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | An aggregated projection of use-based-rent obligation across a contract term, the use-based-rent counterpart to VirtualPRPAggregate. |
| `AssetHistory` | 13 | 13 | 0 | [Audit & History Tables](audit-history-tables.md) | A point-in-time snapshot of an Asset's financial state, letting the platform show what an asset's values were before a later recalculation. |
| `Question` | 13 | 13 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A question posted during a bid Q&A process, with published/private visibility flags — the counterpart IssueResponse replies to. |
| `LinkProjectEntityContact` | 13 | 13 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a ProjectEntity to a contact person with a contact-type classification. |
| `BudgetOption` | 12 | 12 | 0 | [Budget Ancillary Tables](budget-ancillary-tables.md) | A selectable alternative version of a budget-column entity type. |
| `HolidayDate` | 12 | 12 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | One calendar date within a HolidaySchedule. |
| `EscalationIndex` | 12 | 12 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A named index value series (e.g., a specific published CPI series) used to drive ExpenseEscalation calculations. |
| `NotifyTemplate` | 12 | 12 | 0 | [Workflow & Notification Ancillary Tables](workflow-notification-ancillary-tables.md) | A reusable email/dashboard notification template — trigger table, message body, and channel enablement flags. |
| `BudgetView` | 11 | 11 | 0 | [Budget Ancillary Tables](budget-ancillary-tables.md) | A named saved view/filter over the budget grid. |
| `MemberAudit` | 11 | 11 | 0 | [Audit & History Tables](audit-history-tables.md) | Login/session audit trail for internal Members — action name, audit date, and impersonation tracking for support access. |
| `StateProvinceCountry` | 11 | 11 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Master geography reference with ISO Alpha-2/3 country codes, backing every address field across Facility, Location, and Parcel. |
| `Party` | 11 | 11 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A generic company/contact reference tied to a Contract, used where the role doesn't fit Employer or Person specifically. |
| `LinkReceiptTransaction` | 11 | 11 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a PaymentReceipt to the transaction(s) it was allocated against. |
| `LinkSchedOffsetExpGrpType` | 11 | 11 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a ScheduledOffset to the expense group/type it applies to. |
| `DemographicResults` | 11 | 11 | 0 | [Demographics & Site-Selection Reference Tables](demographics-market-tables.md) | A saved demographic analysis output for a site — name, description, and an attached results document. |
| `MapClientSchedule` | 11 | 11 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Links a RETransaction/schedule to auto-push forecast behavior and percent-complete tracking. |
| `IssueResponse` | 11 | 11 | 0 | [Workflow & Notification Ancillary Tables](workflow-notification-ancillary-tables.md) | A reply/answer posted against a bidder Issue (Q&A) during a bid process. |
| `ProcessTimelineTemplate` | 10 | 10 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A reusable milestone/phase template that ProcessTimeline instances are created from, with default phase-status labels. |
| `DemographicReport` | 10 | 10 | 0 | [Demographics & Site-Selection Reference Tables](demographics-market-tables.md) | A demographic report definition tied to a market area, the report-level wrapper around DemographicResults/DemographicFact data. |
| `DemographicFact` | 10 | 10 | 0 | [Demographics & Site-Selection Reference Tables](demographics-market-tables.md) | One data point within a demographic report, with an ordering sequence for display. |
| `Jurisdiction` | 10 | 10 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A tax/legal jurisdiction reference record, referenced by Facility, Parcel, and Location address blocks. |
| `WorkFlowStepAssignee` | 10 | 10 | 0 | [Workflow & Notification Ancillary Tables](workflow-notification-ancillary-tables.md) | One assignee's notification/acknowledgment status on a running WorkFlowStep, parallel to WorkFlowStepApprover for the assignee (rather than approver) role. |
| `CPI` | 9 | 9 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A recorded Consumer Price Index value at a point in time, tied to a Contract, feeding CPI-indexed rent escalation. |
| `Ownership` | 9 | 9 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Records a funding/ownership percentage and type for an entity in a land purchase, supporting multi-party purchases. |
| `WorkFlowTemplateStepMember` | 9 | 9 | 0 | [Workflow & Notification Ancillary Tables](workflow-notification-ancillary-tables.md) | Template-time configuration of which specific Member (or ad-hoc member) fills a WorkFlowTemplateStep role, including org-chart-level targeting. |
| `ExchangeRate` | 8 | 8 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A currency exchange rate captured at a point in time for a Contract, supporting multi-currency financial calculations. |
| `HolidaySchedule` | 8 | 8 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A named calendar of holidays (the header record for HolidayDate), used in schedule/task date calculations. |
| `LinkLandPurchaseInspection` | 8 | 8 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a LandPurchaseSummary to a due-diligence inspection — type, duration, and scheduled date. |
| `LinkRegionManager` | 8 | 8 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table assigning a Member as manager of a Region, with a manager flag and operating-status inheritance. |
| `Region` | 8 | 8 | 0 | [Demographics & Site-Selection Reference Tables](demographics-market-tables.md) | A geographic region in the portfolio hierarchy — parent/previous region linkage and operating status, referenced by LinkRegionManager and LinkRegionMarket. |
| `ComparisonItem` | 8 | 8 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | One line in a competitive/market comparison analysis, with a computed value and expense-group total. |
| `BudgetIndexValue` | 7 | 7 | 0 | [Budget Ancillary Tables](budget-ancillary-tables.md) | One escalation percentage within a BudgetIndex series, tied to a budget column type. |
| `PartPackageItem` | 7 | 7 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | One part within a PartPackage kit. |
| `LinkTaskByCodeMember` | 7 | 7 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table assigning a Task to a Member by job title/org-chart level rather than by name. |
| `LinkRegionMarket` | 7 | 7 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a Region to a market area and its assigned market manager. |
| `DMA` | 7 | 7 | 0 | [Demographics & Site-Selection Reference Tables](demographics-market-tables.md) | A Designated Market Area (a standard US media-market geography) reference record, used for site-selection demographic comparison. |
| `BudgetIndex` | 6 | 6 | 0 | [Budget Ancillary Tables](budget-ancillary-tables.md) | A named escalation index (e.g., a cost inflation index) applied to capital budgets, the header record for BudgetIndexValue. |
| `PartPackage` | 6 | 6 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A named kit/bundle of parts, the header record above PartPackageItem. |
| `RecalcOverrideNotes` | 6 | 6 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A free-text note explaining why a financial recalculation was manually overridden — an audit-style justification field. |
| `DemographicStudyArea` | 6 | 6 | 0 | [Demographics & Site-Selection Reference Tables](demographics-market-tables.md) | The trade-area definition used for a demographic study — radius in miles or drive time in minutes, an alternative to SiteSurvey's fixed 1/3/5-mile bands. |
| `DocumentAudit` | 6 | 6 | 0 | [Audit & History Tables](audit-history-tables.md) | Audit trail of actions taken on a Document (view, edit, delete) — action, actor, and date. |
| `DevelopmentPlan` | 6 | 6 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A named development pipeline plan under RE Planner, the header record above DevelopmentSlot. |
| `NotifyTemplateMember` | 6 | 6 | 0 | [Workflow & Notification Ancillary Tables](workflow-notification-ancillary-tables.md) | The recipient list for a NotifyTemplate, targetable by member, job title, or org-chart level. |
| `Project` | 6 | 6 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A lightweight project identity record (ID, RecID, UUID) distinct from the richer ProjectEntity, likely used for cross-system reference linking. |
| `ReportGroupData` | 5 | 5 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Platform metadata for a top-level or subgroup node in this very Data Fields hierarchy — parent group name and firm scoping. |
| `ExpenseRecoveryItemMapping` | 5 | 5 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Maps an ExpenseRecoveryItem to an external invoice line item name and a JSON configuration blob, likely supporting invoice-import matching. |
| `LinkTaskMember` | 5 | 5 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table assigning a specific Member to a specific Task on a ProjectEntity. |
| `BidPackageBreakoutValue` | 5 | 5 | 0 | [Bid Package Ancillary Tables](bid-package-ancillary-tables.md) | The dollar value a bidder submitted for one BidPackageBreakout line item. |
| `CustomCodeTable` | 5 | 5 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | Meta-definition of a tenant-created custom code table, including a self-referencing parent-table link for hierarchical code lists. |
| `LinkProjectEntityVendor` | 4 | 4 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a ProjectEntity (portfolio) to an approved Vendor. |
| `BidPackageAlternate` | 4 | 4 | 0 | [Bid Package Ancillary Tables](bid-package-ancillary-tables.md) | An alternate (optional add/deduct) bid line offered within a BidPackage, with an accepted flag. |
| `Issue` | 4 | 4 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A bid-package issue/question thread header — date range and type, the object Question and IssueResponse attach to. |
| `LinkBudgetViewBLI` | 4 | 4 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table associating a BudgetLineItem with a BudgetView. |
| `InformationOverlay` | 4 | 4 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Configuration for an in-app guided-tour/tooltip overlay — tour name, field name list, and expiration date. |
| `GlobalProperty` | 4 | 4 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A generic firm-scoped key/value configuration setting, organized by property section — a low-level settings-store table. |
| `LinkEMailReceivedLogDocument` | 4 | 4 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a received email log entry to a saved Document (e.g., an email attachment filed to the record). |
| `LinkSecurity` | 3 | 3 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table applying a security setting to a Folder for a given user class. |
| `CodeAssetCategory` | 3 | 3 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | Master asset-category reference record — GL number and sub-account mapping for a category of equipment/assets. |
| `BidPackageAlternateValue` | 3 | 3 | 0 | [Bid Package Ancillary Tables](bid-package-ancillary-tables.md) | The dollar value a bidder submitted for one BidPackageAlternate line. |
| `BidPackageBreakout` | 3 | 3 | 0 | [Bid Package Ancillary Tables](bid-package-ancillary-tables.md) | A cost breakout line item within a BidPackage tied to a specific budget line. |
| `BidPackageTemplateAlternate` | 3 | 3 | 0 | [Bid Package Ancillary Tables](bid-package-ancillary-tables.md) | The template-defined alternate line pre-configured on a BidPackageTemplate before a specific bid is created. |
| `BidPackageTemplateBreakout` | 3 | 3 | 0 | [Bid Package Ancillary Tables](bid-package-ancillary-tables.md) | The template-defined breakout line pre-configured on a BidPackageTemplate. |
| `MapClientBudget` | 3 | 3 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | Links a ProjectEntity to its budget with a last-reviewed-date stamp. |
| `ComparisonReport` | 3 | 3 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A saved competitive-comparison report with its own assigned page layout. |
| `Site` | 3 | 3 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A minimal site-identity stub (ID, RecID, UUID only) used for cross-system reference rather than data capture. |
| `CodeProblem` | 2 | 2 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | Master maintenance-problem-type reference record with a remedy note, linked to an asset category. |
| `CodeBudgetColumnStatus` | 2 | 2 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | Master reference record for budget-column status values, including a locked flag. |
| `LinkPEMemberCodeJobTitle` | 2 | 2 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a ProjectEntity member assignment to a job-title code — internal ID-only fields with no exposed labels. |
| `LinkEmpAvailableJobFunction` | 2 | 2 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table controlling which job functions are available/selectable for a given Employer. |
| `LinkEmpAvailableJobTitle` | 2 | 2 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table controlling which job titles are available/selectable for a given Employer. |
| `LinkEmpAvailableUserClass` | 2 | 2 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table controlling which security user classes are available/selectable for a given Employer. |
| `CodeSalesType` | 2 | 2 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | Master reference record for sales-type classification, with a flag to omit a type from sales-group totals. |
| `CodeResponsibleParty` | 1 | 1 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | A single-field master value for the responsible-party code list used on Responsibility records. |
| `CodeSalesGroup` | 1 | 1 | 0 | [Code, Custom List & Reference Definition Tables](code-reference-tables.md) | A single-field master value letting one sales group alias to another for reporting rollups. |
| `CommitteePackage` | 1 | 1 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A single-field stub representing a committee-review package record (see LinkCommPkgTemplDocContent). |
| `EntityTemplate` | 1 | 1 | 0 | [Small / Miscellaneous Entities](small-miscellaneous-entities.md) | A single-field stub representing a reusable entity-setup template, referenced by TemplateAudit. |
| `LeaseAudit` | 1 | 1 | 0 | [Audit & History Tables](audit-history-tables.md) | A single-field audit-trail stub for lease-level changes; likely a placeholder or minimally-used table relative to the richer Contract audit trail. |
| `LinkBudgetIndexBLI` | 1 | 1 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table associating a BudgetLineItem with a BudgetIndex escalator — a single internal RecID field only. |
| `LinkCommPkgTemplDocContent` | 1 | 1 | 0 | [Link & Relationship Tables](link-relationship-tables.md) | Join table linking a committee-package template to its document content — a single internal RecID field only. |
| `Notify` | 1 | 1 | 0 | [Workflow & Notification Ancillary Tables](workflow-notification-ancillary-tables.md) | A single-field stub representing an individual fired notification instance. |
