# Sales — Data Fields

Reported retail sales figures for a location, feeding percentage-rent calculations — currency type, fiscal period/year, and a client-assigned sales ID for reconciling against a tenant's own sales report. 27 Global fields under Contract.

**Table Association:** `Sales` &nbsp;·&nbsp; **Total fields:** 27 (Global: 27, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Client Sales ID | `ClientSalesID` | `sTYPE_TEXT` | Global | No | No |  | Contract / Sales |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Sales |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Sales |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales |
| Fiscal Period | `SalesPeriod` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales |
| Fiscal Year | `SalesYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Sales |
| Gross Sales Amount | `GrossSalesAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Matching Calendar Month | `MatchingCalendarMonthText` | `sTYPE_TEXT` | Global | No | No |  | Contract / Sales |
| Matching Calendar Month / Year | `MatchingCalendarMonthYearText` | `sTYPE_TEXT` | Global | No | No |  | Contract / Sales |
| Matching Calendar Year | `MatchingCalendarYear` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Sales |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Sales |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Sales |
| Net Sales Amount | `NetSalesAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Posting Date | `PostingDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales |
| Sales Adjustment #1 | `SalesAdjustment1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Sales Adjustment #2 | `SalesAdjustment2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Sales Adjustment #3 | `SalesAdjustment3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Sales Adjustment #4 | `SalesAdjustment4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Sales Adjustment #5 | `SalesAdjustment5` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Sales Adjustment #6 | `SalesAdjustment6` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales |
| Sales Category | `CodeSalesCategoryID` | `sCODE_SALES_CATEGORY` | Global | No | No |  | Contract / Sales |
| Sales ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Sales |
| Sales Group | `CodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Contract / Sales |
| Sales RecID | `SalesID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Sales |
| Sales Type | `CodeSalesTypeID` | `sCODE_SALES_TYPE` | Global | No | No |  | Contract / Sales |
| Unit Sales Count | `UnitSalesCount` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Sales |
| Unit Sales Type | `CodeUnitSalesTypeID` | `sCODE_UNIT_SALES_TYPE` | Global | No | No |  | Contract / Sales |
