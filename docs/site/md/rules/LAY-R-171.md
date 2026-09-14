# LAY-R-171 — G. Custom Lists

*Configuration, Layouts, Forms & Reporting · Observed*

**The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves;.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves; its layout is a `PageLayout` whose `ClientListRGDID` points back at the node. The list itself is also an RGAF leaf of type `sTYPE_CLIENT_LISTS` on its owning entity. |
| Stated as | Observed (6/6 name match) |
| Stated as | `all-fields.csv`; 006 |

## What it constrains

[ReportGroupData](../entities/ReportGroupData.md), [ReportGroupAvailableField](../entities/ReportGroupAvailableField.md)

---

Source: `docs/modules/layouts-and-forms/rules.md`
