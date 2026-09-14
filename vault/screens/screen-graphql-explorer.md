---
title: "GraphQL Explorer"
tags: [screen, administration,api,diagnostics]
evidence: Observed
---

`/en/admin/graphql.jsp`

The live API introspection surface. **490 types (433 objects), 617 queries, 3 mutations.**

**Those three mutations are why the write path was a mystery for most of this corpus's life** — and
the answer is that [[rest-business-object|REST is the write path]], not GraphQL.

Two other things it settles:

- The canonical **10-value `FieldType` enum** behind the 448 `sTYPE_*` codes in the
  [[data-field-catalog]].
- The `KickOffMethod` enum — **four** values, one of which the vendor's own help text omits
  ([[rule-WF-R-014]]).

**And one absence that shapes a migration:** GraphQL contains **no layout, report, chart or rule
type**. Layouts and reports **cannot** be migrated through the data API
([[finding-no-generic-export]]).

See [`data-model/graphql-api.md`](../../docs/data-model/graphql-api.md)

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
