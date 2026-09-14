---
title: Conditional fields
tags: [concept, layouts, rules]
evidence: Observed
---

*"Show this field when the request type is Estoppel."* A flat rule engine attached to a field
placement, stored as JSON inside `PageLayoutField.JSONConfigText` — never on the
[[PageLayout|layout]] itself.

The definitive read is one call, no rendering and no builder session:

```
GET /rest/businessObject/PageLayout/lxid/{pageLayoutID}?deep=true
```

The populated shape:

```json
{
  "allAny": "all",
  "showHide": "show",
  "criteriaFields": [
    { "scriptName": "Issue.LAR_RequestType",
      "crtOpt1": "2",
      "crtVal1": ["Estoppel"],
      "isCheckBox": false }
  ]
}
```

| Element | Observed across 50 records / 54 clauses | Vocabulary available |
|---|---|---|
| `showHide` | `show` (50/50) | `show`, `showAndRequire`, `hide` |
| `allAny` | `all` (50/50) | `all`, `any` |
| `crtOpt1` | `2` = **in** (51), `17` = **not in** (3) | wider set unobserved |
| `crtVal1` | array of **display strings** | — |

Three things a rebuild must not miss:

1. **[[finding-rules-store-labels-not-ids]]** — `crtVal1` holds rendered labels, so renaming a
   drop-down value silently breaks every rule referencing it. Design this out; do not reproduce it.
2. The `1` suffix implies `crtOpt2`/`crtVal2` the engine supports and nobody uses. *(Inferred.)*
3. **The usage is far narrower than the capability.** Never `hide`, never `showAndRequire`, never
   `any`.

Where they are: **8 layouts, 50 records**, concentrated almost entirely in one workflow —
[[finding-form-layouts-are-hidden]]. And because storage is an opaque blob, Lx **cannot answer "which
layouts depend on this field"** ([[rule-LAY-R-134]]).

A completely separate second rule mechanism exists at the workflow level and holds raw JavaScript —
[[q-bbw-06-conditional-workflow-js]].

Source: [`modules/layouts-and-forms/conditional-fields.md`](../../docs/modules/layouts-and-forms/conditional-fields.md)
