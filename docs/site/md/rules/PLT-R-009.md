# PLT-R-009 — `Region`'s real shape is not in this export

*Platform & Tenancy · Derived*

**12 other objects reference `Region` across 34 columns.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any attempt to enumerate a region's own attributes (name, parent, level number) |
| What it reads | `Region`'s one declared field, `ProjectEntityID` |
| The test | 12 other objects reference `Region` across 34 columns |
| What it writes | A rebuild cannot fully specify the `Region` entity from this corpus alone; treat it as a known gap, not an empty table |

## What it constrains

[Region](../entities/Region.md)

## Confidence

Derived — `object-catalog.md` open question 1, unresolved

---

Source: `docs/modules/platform-tenancy/rules.md`
