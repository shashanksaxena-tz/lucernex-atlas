# RPT-R-020 — C. Filters, grouping and totals

*Configuration, Layouts, Forms & Reporting · Observed*

**Report and list filters are `PageLayoutFilter` rows: `ReportGroupAvailableFieldID` (required) + two `CriteriaType`/`CriteriaValue` pairs, discriminated by a required `IsListFilter` boolean. This is not the conditional-field store — conditional field rules are persisted as a JSON document per….**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Report and list filters are `PageLayoutFilter` rows: `ReportGroupAvailableFieldID` (required) + two `CriteriaType`/`CriteriaValue` pairs, discriminated by a required `IsListFilter` boolean. This is not the conditional-field store — conditional field rules are persisted as a JSON document per target, per live capture (conditional-fields.md). |
| Stated as | Observed (columns) + Inferred (role) |
| Stated as | `all-fields.csv` |

---

Source: `docs/modules/reporting/rules.md`
