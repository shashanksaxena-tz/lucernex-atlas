# POR-R-010

*Portfolio & Real-Estate Transactions · Derived*

**A physical site's lifecycle needs to distinguish "building it" from "leasing it" · `Project.ProjectType` = "Opening Project or Capital Project" (`Project`, `platform-tenancy`) vs. `Contract` (`contracts-leases`) · Two independent subtype roots with independent financial engines (Task/schedule….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A physical site's lifecycle needs to distinguish "building it" from "leasing it" |
| Stated as | `Project.ProjectType` = "Opening Project or Capital Project" (`Project`, `platform-tenancy`) vs. `Contract` (`contracts-leases`) |
| Stated as | Two independent subtype roots with independent financial engines (Task/schedule budget vs. ASC 842 accounting engine); no schema-level FK forces one through the other. |
| Stated as | Derived, see `site-pipeline.md` §3 |

## The wording it rests on

> · `Project.ProjectType` =

## What it constrains

[Project](../entities/Project.md), [Contract](../entities/Contract.md)

Columns named: `Project.ProjectType`

---

Source: `docs/modules/portfolio-transactions/rules.md`
