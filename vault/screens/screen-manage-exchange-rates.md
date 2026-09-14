---
title: "Manage Exchange Rates"
tags: [screen, administration,reference-data,accounting]
evidence: Observed
---

`/en/admin/ManageCurrencyRates.jsp`

![Empty — and [[Program]] carries fourteen FX rate-type selectors that read from here.](../assets/screenshots/bbw-admin/24-manage-exchange-rates.jpg)
`docs/assets/screenshots/bbw-admin/24-manage-exchange-rates.jpg` · `af-admin/25-manage-exchange-rates.jpg`

**Zero rows.** One of the [[feature-reference-data|four of five reference tables that are empty]].

Less alarming than [[screen-manage-discount-rates|the discount-rate table]] — both tenants are
single-currency US operations, and 166 currency types being *offered* in the
[[screen-contract-wizard|contract wizard]] is not evidence any are used.

But [[Program]] carries **14 FX rate-type selectors**, so the capability is configured for in the data
model and unpopulated in the data. Worth a decision rather than an assumption if ASG Edge+ has
multi-currency clients.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
