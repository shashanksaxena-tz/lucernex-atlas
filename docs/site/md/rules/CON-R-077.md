# CON-R-077 — 7. Use-based rent

*Contracts & Leases · Derived*

**Usage-based rent is computed: structurally identical to the percentage-rent tiering with Sales→Usage and PRP→UBRP; the tier value is a unit cost, not a percentage rate.**

Usage-based rent is computed: structurally identical to the percentage-rent tiering with Sales→Usage and PRP→UBRP; the tier value is a unit cost, not a percentage rate.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Usage-based rent is computed |
| Stated as | `Usage.UsageCount`, `.UsageShare`, `UseBasedRentBreakpoint.BreakpointCount1..8`, `.BreakpointCost1..8` |
| Stated as | Structurally identical to `CON-R-050`…`CON-R-063` with `Sales`→`Usage` and `PRP`→`UBRP`. Tier value is a unit cost, not a percentage rate |
| Stated as | `UBRPRentDue`, `UBRPTotalRent` |
| Stated as | Derived (field-for-field mirror confirmed) |

## What it constrains

[Usage](../entities/Usage.md), [Sales](../entities/Sales.md)

Columns named: `Usage.UsageCount`

## Rules it cites

[CON-R-050](CON-R-050.md), [CON-R-063](CON-R-063.md)

---

Source: `docs/modules/contracts/rules.md`
