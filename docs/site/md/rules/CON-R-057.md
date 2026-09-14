# CON-R-057 — 5. Percentage rent

*Contracts & Leases · Derived*

**Sales periods roll into a rent period: PRPSalesAmount sums NetSalesPeriodAmount over every sales period inside the billing bucket.**

Sales periods roll into a rent period: PRPSalesAmount sums NetSalesPeriodAmount over every sales period inside the billing bucket.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Sales periods roll into a rent period |
| Stated as | Net sales per sales period, `BillingBucket{Begin,End}Date` |
| Stated as | `PRPSalesAmount = Σ NetSalesPeriodAmount` inside the billing bucket |
| Stated as | Rent-period sales |
| Stated as | Derived |

---

Source: `docs/modules/contracts/rules.md`
