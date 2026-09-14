---
title: Layouts are built on computed projections, not only on tables
tags: [finding, layouts, data-model]
evidence: Observed
---

Four [[page-layout-concept|layouts]] name a [[virtual-projection|`Virtual*`]] object as their primary
table — **and two of them are top-level Summary Pages**:

| PLID | Layout | Mode | Primary table |
|---:|---|---|---|
| 98921 | ASG Breakpoint Schedule | **SEP** | [[VirtualPercentageRentPeriod]] |
| 98934 | ASG Percent Rent Schedule | **SEP** | [[VirtualPercentageRentPeriod]] |
| 98908 | ASG Contract Payment Details - Breakpoints | LIST | [[VirtualPercentageRentPeriod]] |
| 98920 | ASG Contract Percent Rent - Schedule | LIST | [[VirtualSalesPeriod]] |

The corpus had recorded that the 13 `Virtual*` objects have **no primary key and not one audit
column** — computed projections, internal machinery. **Two of them turn out to be the primary table of
user-facing screens.**

> **The layout engine must be able to target a read model or computed projection, not just an entity
> table.**

A rebuild that only permits layouts over persisted entities **cannot reproduce the percentage-rent
breakpoint and sales-period schedule screens at all**.

It also means those screens are **inherently read-only** — there is no key to write back to — which a
layout engine has to **model explicitly** rather than discover at runtime. Whether the builder in fact
renders them as display-only is [[q-bbw-11-virtual-layout-writable]].

### The related oddity

`ASG ASC 842 Schedule` (98859) and `ASG SL Summary` (98873) declare **the same primary table**,
`Straight-Line Schedule`. Two screens, one underlying object, two layouts — so
[[one-engine-three-standards|the standard is a layout distinction here, not a data one]]. Which of
[[SLSummary]] / [[SLPeriod]] / `CodeSLSchedule` that table actually is remains
[[q-bbw-10-straight-line-table]].
