# PLT-R-004 — A new `ProjectEntity` subtype requires a new `Firm` column

*Platform & Tenancy · Observed*

**The new subtype needs a default setup-page-layout assignment, the same way the existing eleven do.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Onboarding a new kind of ownable entity (a 12th subtype beyond the 11 `IsValidFor*` categories) |
| What it reads | `Firm`'s eleven `*SetupPageLayoutID` columns |
| The test | The new subtype needs a default setup-page-layout assignment, the same way the existing eleven do |
| What it writes | `Firm` gains a twelfth column. There is no lookup table of (subtype, default layout) pairs — the enumeration is baked into the tenant record's own schema |

## What it constrains

[Firm](../entities/Firm.md)

## Confidence

Observed field list (`data-model.md`), Derived conclusion

---

Source: `docs/modules/platform-tenancy/rules.md`
