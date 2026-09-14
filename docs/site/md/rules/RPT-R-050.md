# RPT-R-050 — F. Security

*Configuration, Layouts, Forms & Reporting · Observed*

**Report access is granted per user class through `UserClassSecurity.PageLayoutID`, alongside grants on fields (`ReportGroupAvailableFieldID`), field groups (`ReportGroupDataID`) and dashboard components. · Observed · `all-fields.csv`.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Report access is granted per user class through `UserClassSecurity.PageLayoutID`, alongside grants on fields (`ReportGroupAvailableFieldID`), field groups (`ReportGroupDataID`) and dashboard components. |
| Stated as | Observed |
| Stated as | `all-fields.csv` |

## What it constrains

[UserClassSecurity](../entities/UserClassSecurity.md)

Columns named: `UserClassSecurity.PageLayoutID`

---

Source: `docs/modules/reporting/rules.md`
