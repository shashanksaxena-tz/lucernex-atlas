---
title: "Q-BBW-10 — Which object is 'Straight-Line Schedule'?"
tags: [open-question, accounting, data-model]
evidence: Derived
status: open
---

**24 of the 30 primary tables behind the 93 layouts resolve to a catalog object by name.** Of the six
that do not, five are settled:

| Layout's primary table | Resolves to |
|---|---|
| `Portfolio` | [[Program]] — display alias |
| `Entity` | [[ProjectEntity]] — display alias |
| `Percentage Rent Period` | [[VirtualPercentageRentPeriod]] — confirmed by physical name |
| `Sales Period` | [[VirtualSalesPeriod]] — confirmed by physical name |
| `Comparison Report Item` | `ComparisonItem` *(Inferred, and only on the abandoned `zdelete` layout)* |
| **`Straight-Line Schedule`** | **ambiguous across three candidates** |

The three candidates are [[SLSummary]], [[SLPeriod]] and `CodeSLSchedule`, and **none is an exact
match**.

It matters because **two layouts declare it** — `ASG ASC 842 Schedule` (98859) and `ASG SL Summary`
(98873), the same primary table under two different screens. See
[[finding-layouts-over-projections]].

### How to settle it

A `ShowObjectDetails.jsp` pass, or read the two layouts' placed fields and see which object's columns
they name.
