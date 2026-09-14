---
title: "The six budget and bidding tools"
tags: [screen, administration,out-of-scope]
evidence: Observed
---

`/en/budget/* · /en/admin/BidPackageTemplate.jsp`

![Budget templates — one of six tools in an area ruled out of scope by decision.](../assets/screenshots/bbw-admin/19-manage-budget-templates.jpg)
`docs/assets/screenshots/bbw-admin/19-manage-budget-templates.jpg`

**Out of scope by decision (2026-09-10).** Six admin tools, and **27 objects** retained in the census
and the [[foreign-key-graph]] purely so the model stays whole.

| Tool | Route |
|---|---|
| Manage Budget Templates | `/en/budget/BudgetTemplateEdit.jsp` |
| Manage Budget Views | `/en/budget/BudgetLayoutView.jsp` |
| Manage Budget Types | `/en/budget/BudgetColumnTypeEdit.jsp` |
| Manage Budget Summary Page | `/en/budget/BudgetSummaryEdit.jsp` |
| Manage Budget Index Variables | `/en/budget/BudgetIndexEdit.jsp` |
| Manage Bid Package Templates | `/en/admin/BidPackageTemplate.jsp` |

**The boundary is porous in one direction and not the other**: only **13** FK columns cross from
in-scope objects into Budget/Bid/Cost — nine of them the same `BudgetTemplateID` column — while **71**
point the other way. So cutting the area loses little and keeping it costs little.

Two retired rule ids belong to this area and **must not be reused**: `RPT-R-034` and `RPT-R-035`.

Compare [[finding-punch-list-out-of-scope]], which is a different out-of-scope argument — assigned to a
separate product rather than deferred.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
