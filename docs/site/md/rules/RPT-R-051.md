# RPT-R-051 — F. Security

*Configuration, Layouts, Forms & Reporting · Observed*

**Dashboard tiles are secured by title string (`UserClassSecurity.DashboardComponentTitle`), not by record id. Renaming a tile therefore breaks its grants.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Dashboard tiles are secured by title string (`UserClassSecurity.DashboardComponentTitle`), not by record id. Renaming a tile therefore breaks its grants. |
| Stated as | Observed (column) + Inferred (consequence) |
| Stated as | `all-fields.csv` |

## What it constrains

[UserClassSecurity](../entities/UserClassSecurity.md)

Columns named: `UserClassSecurity.DashboardComponentTitle`

---

Source: `docs/modules/reporting/rules.md`
