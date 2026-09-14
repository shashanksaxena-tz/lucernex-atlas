# RPT-R-041 — E. Audit reporting

*Configuration, Layouts, Forms & Reporting · Observed*

**Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report. |
| Stated as | Observed (columns) + Derived (11-for-11 match with the observed Audit Log dialog) |
| Stated as | `all-fields.csv`; 007 |

## What it constrains

[AuditColumn](../entities/AuditColumn.md), [ReportGroupData](../entities/ReportGroupData.md)

Columns named: `AuditColumn.GroupID`

---

Source: `docs/modules/reporting/rules.md`
