---
title: Soft references — the relationships a schema tool cannot see
tags: [concept, data-model, gap]
evidence: Derived
---

Ten type names carry **118 fields** that are references in fact but not in type. A tool that derives
the [[foreign-key-graph]] from declared types misses every one of them.

| Type | Fields / objects | Points at |
|---|---|---|
| `Contact` | 54 / 25 | the [[Person]] identity aggregate — **polymorphically** ([[rule-PPL-R-002]]) |
| `Dropdown` (bare, no code list) | 21 / 20 | nothing declared |
| `Entity` | 14 / 13 | [[ProjectEntity]] — softly |
| `Document List` | 8 / 8 | [[Document]] |
| `Custom List` | 7 / 1 | [[custom-list]] |
| `Part` · `Parts Package` | 5 / 3 | the parts catalog |
| `Holiday Calendar` | 3 | the holiday calendar |
| `Member` (bare) | 2 | [[Member]] |
| `Response` | 1 | — |

Two consequences that already bit:

- **`AssetHistory` is classified wrongly** because it carries `ProjectEntityID` typed soft `Entity`
  rather than hard `Entity ID` — see [[entity-spine]].
- **`ServiceRequest` and `WorkOrder` link to [[Issue]] through an untyped `Text` column**, so the FK
  graph misses the maintenance loop entirely ([[rule-AST-R-012]]).

The broader version of the same problem is [[finding-fk-graph-undercounts]]: **87 more edges** exist
that are *named* like a foreign key and *typed* as a scalar.

Source: [`data-model/type-system.md`](../../docs/data-model/type-system.md)
