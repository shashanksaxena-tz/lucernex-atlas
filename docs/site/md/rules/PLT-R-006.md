# PLT-R-006 — `Security` is a read-only, computed shadow of `UserClassSecurity`

*Platform & Tenancy · Derived*

**Both declare the same 21 fields.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any permission check |
| What it reads | `UserClassSecurity` (has a physical table) and `Security` (does not) |
| The test | Both declare the same 21 fields |
| What it writes | `UserClassSecurity` is the editable grant; `Security` is what a rebuild's authorization service would compute and cache, never what an admin edits directly |

## What it constrains

[UserClassSecurity](../entities/UserClassSecurity.md), [Security](../entities/Security.md)

## Confidence

Derived — exhaustive field-list diff, `data-model.md`

---

Source: `docs/modules/platform-tenancy/rules.md`
