# LAY-R-164 — F. Forms

*Configuration, Layouts, Forms & Reporting · Observed*

**A form instance is an `Issue` record. `Issue.LastPageLayoutID` records "the name of the last form layout used to update the issue" — singular, so it is depth-1 history, not a per-step audit trail.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A form instance is an `Issue` record. `Issue.LastPageLayoutID` records "the name of the last form layout used to update the issue" — singular, so it is depth-1 history, not a per-step audit trail. It does not make a multi-step form reproducible as each participant saw it. |
| Stated as | Observed (vendor Definition text) |
| Stated as | `_xlsx_feature_list.txt`; `_lucernex_objects_summary.txt` |

## The wording it rests on

> the name of the last form layout used to update the issue

## What it constrains

[Issue](../entities/Issue.md)

Columns named: `Issue.LastPageLayoutID`

---

Source: `docs/modules/layouts-and-forms/rules.md`
