# Budgeting, Cost Tracking & Bidding — OUT OF SCOPE

*Out of scope by decision*

Deliberately excluded by user decision (2026-09-10). The budget model, bid packages and cost-tracking templates. Retained in objects.json / edges.json and object-catalog.md for census and FK-graph completeness only.

|  | Count |
|---|---|
| Record types | 27 |
| Fields | 546 |
| Keys in | 13 |
| Keys out | 71 |
| Rules | 0 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [BudgetOptionTemplate](../entities/BudgetOptionTemplate.md) | `—` | 107 | 0 |
| [BidPackage](../entities/BidPackage.md) | `bid_package` | 48 | 0 |
| [ProFormaBudget](../entities/ProFormaBudget.md) | `pro_forma_budget` | 47 | 0 |
| [BidPackageTemplate](../entities/BidPackageTemplate.md) | `bid_package_template` | 32 | 1 |
| [BudgetColumnType](../entities/BudgetColumnType.md) | `budget_column_type` | 31 | 16 |
| [CostTrackingTemplate](../entities/CostTrackingTemplate.md) | `cost_tracking_template` | 28 | 0 |
| [BudgetLineGroup](../entities/BudgetLineGroup.md) | `budget_line_group` | 26 | 0 |
| [BudgetLineItem](../entities/BudgetLineItem.md) | `budget_line_item` | 26 | 0 |
| [BudgetLineLeaf](../entities/BudgetLineLeaf.md) | `budget_line_leaf` | 26 | 0 |
| [BidderIssue](../entities/BidderIssue.md) | `bidder_issue` | 21 | 0 |
| [BudgetColumn](../entities/BudgetColumn.md) | `budget_column` | 21 | 0 |
| [BudgetColumnItemValue](../entities/BudgetColumnItemValue.md) | `—` | 19 | 0 |
| [BudgetTemplateAudit](../entities/BudgetTemplateAudit.md) | `budget_template_audit` | 18 | 0 |
| [VirtualTemplateBudget](../entities/VirtualTemplateBudget.md) | `virtual_template_budget` | 17 | 0 |
| [VirtualTemplateBudgetOption](../entities/VirtualTemplateBudgetOption.md) | `virtual_template_budget_option` | 17 | 0 |
| [BudgetOption](../entities/BudgetOption.md) | `budget_option` | 13 | 0 |
| [BudgetView](../entities/BudgetView.md) | `budget_view` | 10 | 4 |
| [BudgetIndexValue](../entities/BudgetIndexValue.md) | `budget_index_value` | 8 | 0 |
| [BidPackageBreakoutValue](../entities/BidPackageBreakoutValue.md) | `bid_package_breakout_value` | 6 | 0 |
| [BudgetIndex](../entities/BudgetIndex.md) | `budget_index` | 6 | 1 |
| [BidPackageAlternate](../entities/BidPackageAlternate.md) | `bid_package_alternate` | 5 | 0 |
| [BidPackageAlternateValue](../entities/BidPackageAlternateValue.md) | `bid_package_alternate_value` | 4 | 0 |
| [BidPackageBreakout](../entities/BidPackageBreakout.md) | `—` | 4 | 0 |
| [CodeBudgetColumnStatus](../entities/CodeBudgetColumnStatus.md) | `code_budget_column_status` | 3 | 0 |
| [BudgetTemplate](../entities/BudgetTemplate.md) | `budget_template` | 1 | 14 |
| [LinkBudgetIndexBLI](../entities/LinkBudgetIndexBLI.md) | `link_budget_index_b_l_i` | 1 | 0 |
| [LinkBudgetViewBLI](../entities/LinkBudgetViewBLI.md) | `link_budget_view_b_l_i` | 1 | 0 |
