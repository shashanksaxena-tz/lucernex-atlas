# Variable Rent (Percentage / Use-Based) & Sales

*In scope for the rebuild*

Retail turnover rent: reported sales and usage, breakpoints, exclusions and caps, and the virtual period projections that price them.

|  | Count |
|---|---|
| Record types | 17 |
| Fields | 472 |
| Keys in | 2 |
| Keys out | 44 |
| Rules | 0 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [VirtualSalesPeriod](../entities/VirtualSalesPeriod.md) | `—` | 66 | 0 |
| [VirtualUsagePeriod](../entities/VirtualUsagePeriod.md) | `virtual_usage_period` | 66 | 0 |
| [PercentageRent](../entities/PercentageRent.md) | `percentage_rent` | 45 | 2 |
| [PercentageRentBreakpoint](../entities/PercentageRentBreakpoint.md) | `percentage_rent_breakpoint` | 40 | 0 |
| [VirtualPercentageRentPeriod](../entities/VirtualPercentageRentPeriod.md) | `virtual_percentage_rent_period` | 38 | 0 |
| [UseBasedRentBreakpoint](../entities/UseBasedRentBreakpoint.md) | `use_based_rent_breakpoint` | 31 | 0 |
| [Sales](../entities/Sales.md) | `sales` | 28 | 0 |
| [SalesExclusionCap](../entities/SalesExclusionCap.md) | `sales_exclusion_cap` | 23 | 1 |
| [UseBasedRent](../entities/UseBasedRent.md) | `use_based_rent` | 23 | 0 |
| [VirtualUseBasedRentPeriod](../entities/VirtualUseBasedRentPeriod.md) | `virtual_use_based_rent_period` | 23 | 0 |
| [VirtualPRAccrualPeriod](../entities/VirtualPRAccrualPeriod.md) | `virtual_pr_accrual_period` | 20 | 0 |
| [SalesExclusion](../entities/SalesExclusion.md) | `sales_exclusion` | 19 | 0 |
| [VirtualPRPAggregate](../entities/VirtualPRPAggregate.md) | `virtual_p_r_p_aggregate` | 16 | 0 |
| [Usage](../entities/Usage.md) | `usage` | 14 | 0 |
| [VirtualUBRPAggregate](../entities/VirtualUBRPAggregate.md) | `virtual_u_b_r_p_aggregate` | 14 | 0 |
| [CodeSalesGroup](../entities/CodeSalesGroup.md) | `code_sales_group` | 3 | 0 |
| [CodeSalesType](../entities/CodeSalesType.md) | `code_sales_type` | 3 | 0 |
