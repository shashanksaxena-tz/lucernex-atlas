# Bid Package Ancillary Tables

These 6 tables (21 fields, all Global) are the line-item and alternate/breakout detail underneath the two large standalone bid entities, [BidPackage](bid-package.md) (53 fields) and [BidPackageTemplate](bid-package-template.md) (31 fields). Each pairs a 'definition' table (Breakout, Alternate) with a matching 'Value' table holding the bidder-submitted number against it — the same header/line-item pattern seen throughout the catalog, just at a smaller scale for the competitive-bid workflow specifically.

**Entities in this file:** 6 &nbsp;·&nbsp; **Total fields:** 21 (Global: 21, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `BidPackageBreakoutValue` | 5 (5/0) | The dollar value a bidder submitted for one BidPackageBreakout line item. |
| `BidPackageAlternate` | 4 (4/0) | An alternate (optional add/deduct) bid line offered within a BidPackage, with an accepted flag. |
| `BidPackageAlternateValue` | 3 (3/0) | The dollar value a bidder submitted for one BidPackageAlternate line. |
| `BidPackageBreakout` | 3 (3/0) | A cost breakout line item within a BidPackage tied to a specific budget line. |
| `BidPackageTemplateAlternate` | 3 (3/0) | The template-defined alternate line pre-configured on a BidPackageTemplate before a specific bid is created. |
| `BidPackageTemplateBreakout` | 3 (3/0) | The template-defined breakout line pre-configured on a BidPackageTemplate. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| BidPackageBreakoutValue | Bid Package Breakout | `BidPackageBreakoutID` | `sTYPE_BID_PACKAGE_BREAKOUT` | Global | No | No |  | Specialized Forms / Bid Package Breakout Value |
| BidPackageBreakoutValue | Breakout Value | `Value` | `sTYPE_MONEY` | Global | Yes | No |  | Specialized Forms / Bid Package Breakout Value |
| BidPackageBreakoutValue | Budget Column | `BudgetColumnID` | `sTYPE_BUDGET_COLUMN` | Global | Yes | No |  | Specialized Forms / Bid Package Breakout Value |
| BidPackageBreakoutValue | Budget Line Item | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | Yes | No |  | Specialized Forms / Bid Package Breakout Value |
| BidPackageBreakoutValue | Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package Breakout Value |
| BidPackageAlternate | Accepted? | `Accepted` | `sTYPE_BOOLEAN` | Global | No | No |  | Specialized Forms / Bid Package Alternate |
| BidPackageAlternate | Bid Package | `BidPackageID` | `sTYPE_BID_PACKAGE` | Global | Yes | No |  | Specialized Forms / Bid Package Alternate |
| BidPackageAlternate | Budget Line Item | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | Yes | No |  | Specialized Forms / Bid Package Alternate |
| BidPackageAlternate | Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package Alternate |
| BidPackageAlternateValue | Alternate Value | `AltValue` | `sTYPE_MONEY` | Global | Yes | No |  | Specialized Forms / Bid Package Alternate Value |
| BidPackageAlternateValue | Bid Package Alternate | `BidPackageAlternateID` | `sTYPE_BID_PACKAGE_ALTERNATE` | Global | Yes | No |  | Specialized Forms / Bid Package Alternate Value |
| BidPackageAlternateValue | Budget Column | `BudgetColumnID` | `sTYPE_BUDGET_COLUMN` | Global | Yes | No |  | Specialized Forms / Bid Package Alternate Value |
| BidPackageBreakout | Bid Package | `BidPackageID` | `sTYPE_BID_PACKAGE` | Global | Yes | No |  | Specialized Forms / Bid Package Breakout |
| BidPackageBreakout | Budget Line Item | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | Yes | No |  | Specialized Forms / Bid Package Breakout |
| BidPackageBreakout | Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package Breakout |
| BidPackageTemplateAlternate | Bid Package Template | `BidPackageTemplateID` | `sTYPE_BID_PACKAGE_TEMPLATE` | Global | Yes | No |  | Specialized Forms / Bid Package Template Alternate |
| BidPackageTemplateAlternate | Budget Line Item | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | Yes | No |  | Specialized Forms / Bid Package Template Alternate |
| BidPackageTemplateAlternate | Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package Template Alternate |
| BidPackageTemplateBreakout | Bid Package Template | `BidPackageTemplateID` | `sTYPE_BID_PACKAGE_TEMPLATE` | Global | Yes | No |  | Specialized Forms / Bid Package Template Breakout |
| BidPackageTemplateBreakout | Budget Line Item | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | Yes | No |  | Specialized Forms / Bid Package Template Breakout |
| BidPackageTemplateBreakout | Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Bid Package Template Breakout |
