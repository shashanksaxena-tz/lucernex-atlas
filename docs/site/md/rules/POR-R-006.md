# POR-R-006

*Portfolio & Real-Estate Transactions · Observed*

**A `RETransaction` is opened against a site the tenant may already occupy · `RETransaction.FacilityID` · Optional direct FK to an existing `Facility` — a renewal/expansion transaction can name its Facility before any Scenario or Contract exists. · Observed.**

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A `RETransaction` is opened against a site the tenant may already occupy |
| Stated as | `RETransaction.FacilityID` |
| Stated as | Optional direct FK to an existing `Facility` — a renewal/expansion transaction can name its Facility before any Scenario or Contract exists. |
| Stated as | Observed |

## What it constrains

[RETransaction](../entities/RETransaction.md), [Facility](../entities/Facility.md)

Columns named: `RETransaction.FacilityID`

---

Source: `docs/modules/portfolio-transactions/rules.md`
