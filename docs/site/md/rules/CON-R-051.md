# CON-R-051 — Step 1 — gross sales for the sales period (``)

*Contracts & Leases · Observed*

**Sales are reported: GrossSalesPeriodAmount sums Sales.GrossSalesAmount over the sales period; GrossSalesPeriodCount does the same for unit counts.**

Sales are reported: GrossSalesPeriodAmount sums Sales.GrossSalesAmount over the sales period; GrossSalesPeriodCount does the same for unit counts.

``` GrossSalesPeriodAmount = Σ Sales.GrossSalesAmount for periods in [PeriodBeginDate, PeriodEndDate] GrossSalesPeriodCount = Σ Sales.UnitSalesCount ``` `Sales` carries `SalesAdjustment1..6(Currency)` and its own `NetSalesAmount`, so a reported sales row can already be net of tenant-side adjustments before exclusions are applied. Observed; the precedence between `Sales.NetSalesAmount` and the exclusion engine is an open question.

## What it constrains

[Sales](../entities/Sales.md)

Columns named: `Sales.NetSalesAmount`

---

Source: `docs/modules/contracts/percentage-rent.md`
