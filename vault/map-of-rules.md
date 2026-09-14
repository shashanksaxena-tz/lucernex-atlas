---
title: Map of rules
tags: [moc, rules]
---

# The numbered business rules

**469 rules defined across 13 registers.** They are numbered so any note can cite one. The **115 most
load-bearing have their own page**; the rest live in the module registers, which link to
[`docs/modules/*/rules.md`](../docs/INDEX.md).

| Register | Range | Defined |
|---|---|---:|
| [[rules-contracts]] | `CON-R-001…161` | **161** |
| [[rules-layouts-and-forms]] | `LAY-R-001…018`, `101…202` | 88 |
| [[rules-workflow]] | `WF-R-001…062` + 7 suffixed | 69 |
| [[rules-accounting]] | `ACC-R-001…062` | 62 |
| [[rules-reporting]] | `RPT-R-001…077` *(gaps)* | 49 |
| [[rules-facilities-locations]] | `FAC-R-001…020` | 20 |
| [[rules-platform-tenancy]] | `PLT-R-001…016` | 16 |
| [[rules-assets-equipment]] | `AST-R-001…016` | 16 |
| [[rules-portfolio-transactions]] | `POR-R-001…016` | 16 |
| [[rules-projects-capital]] | `PRJ-R-001…014` | 14 |
| [[rules-people-parties]] | `PPL-R-001…013` | 13 |
| [[rules-property-tax]] | `TAX-R-001…012` | 12 |
| [[rules-documents-folders]] | `DOC-R-001…011` | 11 |

## Before citing anything

- **`RPT-R-034` and `RPT-R-035` are retired and must not be reused.**
- **`RPT-R-070`…`077` are ASG Edge+ requirements, not Lx observations.**
- **There is no `LAY-R-100`** — that string is a section heading.
- **[[rules-workflow]]'s own header undercounts itself**: it says 67, and 69 are defined.
- Three modules cite rules they do not own; do not double-count
  ([[rule-LAY-R-106]], [[rule-FAC-R-014]], [[rule-ACC-R-056]]).

## The ten most consequential

[[rule-ACC-R-011]] — classification polarity is **inverted** ·
[[rule-ACC-R-033]] — a formula that **does not exist** ·
[[rule-CON-R-058]] — percentage-rent tiering, **Inferred**, the module's own stated biggest risk ·
[[rule-CON-R-131]] — **every landed column is `TEXT`** ·
[[rule-PLT-R-001]] — tenant isolation is one join deep and **unenforced** ·
[[rule-PLT-R-016]] — the spine is **not settled** ·
[[rule-LAY-R-166e]] — **no mechanism passes values between workflow steps** ·
[[rule-WF-R-055]] — the engine can write **exactly one field** ·
[[rule-AST-R-006]] — `RemainingAssetBalance` is **magnitude-typed** ·
[[rule-TAX-R-011]] — **a won appeal is reconciled nowhere**

## Rules that describe absences

Several of the most useful entries record something the product **does not do**, proved by exhaustive
inspection rather than observed directly — which is the only way to prove a negative:
[[rule-CON-R-118]] · [[rule-POR-R-011]] · [[rule-DOC-R-010]] · [[rule-DOC-R-011]] ·
[[rule-PRJ-R-014]] · [[rule-PPL-R-013]] · and [[rules-workflow]]'s 23-row *"rules that do not exist"*
table.

← [[00-start-here]] · [[map-of-features]] · [[evidence-labels]]
