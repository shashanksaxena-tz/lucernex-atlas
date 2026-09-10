# ProFormaBudget — Data Fields

The financial feasibility analysis for a prospective deal or capital project — IRR, NPV, and Payback Period alongside a Finance Committee Approval flag, gating whether a deal proceeds. 46 Global fields under Summary Information, dominated by `MONEY` fields (36 of 46) since this is fundamentally a discounted-cash-flow worksheet.

**Table Association:** `ProFormaBudget` &nbsp;·&nbsp; **Total fields:** 46 (Global: 46, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Date Of Financials | `DateOfFinancials` | `sTYPE_DATE` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Finance Committee Approval | `CodeProFormaBudgetStatusID` | `sCODE_PRO_FORMA_BUDGET_STATUS` | Global | No | No |  | Summary Information / Pro Forma Budget |
| IRR | `IRR` | `sTYPE_PERCENTAGE` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / Pro Forma Budget |
| NPV | `NPV` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Notes Financials | `NotesFinancials` | `sTYPE_TEXTAREA` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Payback Period | `PaybackPeriod` | `sTYPE_NUMBER_FRACTION2DIGITS` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Pro Forma Budget ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / Pro Forma Budget |
| Pro Forma Budget RecID | `ProFormaBudgetID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Capital Beyond Fifth Year | `ProjectedCostCapitalBeyond` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Capital Fifth Year | `ProjectedCostCapitalFifthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Capital Fourth Year | `ProjectedCostCapitalFourthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Capital Next Year | `ProjectedCostCapitalNextYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Capital PriorYear | `ProjectedCostCapitalPriorYear` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Capital Third Year | `ProjectedCostCapitalThirdYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Capital This Year | `ProjectedCostCapitalThisYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Operating Beyond Fifth Year | `ProjectedCostOperatingBeyond` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Operating Current Year | `ProjectedCostOperatingThisYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Operating Fifth Year | `ProjectedCostOperatingFifthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Operating Fourth Year | `ProjectedCostOperatingFourthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Operating Next Year | `ProjectedCostOperatingNextYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Operating Prior Year | `ProjectedCostOperatingPriorYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Cost Operating Third Year | `ProjectedCostOperatingThirdYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Margin Beyond Fifth Year | `ProjectedMarginBeyond` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Margin Fifth Year | `ProjectedMarginFifthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Margin Fourth Year | `ProjectedMarginFourthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Margin Next Year | `ProjectedMarginNextYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Margin Prior Year | `ProjectedMarginPriorYear` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Margin Third Year | `ProjectedMarginThirdYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Margin This Year | `ProjectedMarginThisYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Property Taxes Beyond Fifth Year | `ProjectedPropTaxesBeyond` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Property Taxes Fifth Year | `ProjectedPropTaxesFifthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Property Taxes Fourth Year | `ProjectedPropTaxesFourthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Property Taxes Next Year | `ProjectedPropTaxesNextYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Property Taxes PriorYear | `ProjectedPropTaxesPriorYear` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Property Taxes Third Year | `ProjectedPropTaxesThirdYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Property Taxes This Year | `ProjectedPropTaxesThisYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Sales Beyond Fifth Year | `ProjectedSalesBeyond` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Sales Fifth Year | `ProjectedSalesFifthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Sales Fourth Year | `ProjectedSalesFourthYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Sales Next Year | `ProjectedSalesNextYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Sales Prior Year | `ProjectedSalesPriorYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Sales Third Year | `ProjectedSalesThirdYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| Projected Sales This Year | `ProjectedSalesThisYr` | `sTYPE_MONEY` | Global | No | No |  | Summary Information / Pro Forma Budget |
| ROI | `ROI` | `sTYPE_PERCENTAGE` | Global | No | No |  | Summary Information / Pro Forma Budget |
