---
title: StateProvinceCountry
tags: [entity, platform-tenancy, reference-data]
evidence: Observed
---

**`state_province_country` · 11 fields · [[module-platform-tenancy]]**

Master geography with ISO Alpha-2/3 codes, behind every address in the product. Fifth in in-degree:
**22 objects, 26 columns**.

Its FK type is named **`Country, State, County ID`** — one of the four type names that lie about their
target. Alongside it, `County ID` (17 columns) resolves to [[Jurisdiction]], not to this. See
[[type-system]].

Two of the seven [[DiscountRate]] lookup dimensions are Country and State/Province, so geography is
load-bearing in the accounting engine, not just in addresses.
