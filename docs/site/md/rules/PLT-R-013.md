# PLT-R-013 — Audit entries file under the field-registry tree, not a separate taxonomy

*Platform & Tenancy · Derived*

**"Group Name"/"Sub-Group" columns a user sees in an Audit Log screen are the same registry group/subgroup names used everywhere else field metadata is organised.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | An `AuditColumn` row is written |
| What it reads | `GroupID`, `SubGroupID` (typed `sTYPE_REPORT_GROUP_DATA`) |
| What it writes | "Group Name"/"Sub-Group" columns a user sees in an Audit Log screen are the same registry group/subgroup names used everywhere else field metadata is organised |

## What it constrains

[AuditColumn](../entities/AuditColumn.md)

## Confidence

Derived — 11-for-11 column match, documented in full in `../reporting/report-field-registry.md`; cited, not re-derived, here. ## Thin objects — treat as gaps, not as complete

---

Source: `docs/modules/platform-tenancy/rules.md`
