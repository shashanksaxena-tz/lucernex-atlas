---
title: FIQL — the query surface
tags: [concept, api, search]
evidence: Observed
---

Reads on the [[rest-business-object|generic REST controller]] filter with **FIQL** (Feed Item Query
Language):

```
GET /rest/businessObject/{objectType}/details?fiql=…&fields=…&$skip=…&$top=…
```

Three constraints that shape any bulk extraction:

- **`fields` is required.** You cannot ask for the whole record.
- **413 is a real answer.** Request too many fields and the endpoint refuses.
- **FIQL fails silently.** A malformed or unmatched filter returns `{}` rather than an error — which
  is exactly the shape of a correct empty result. A verification of *zero Equipment Contracts at
  American Freight* deliberately avoided FIQL for this reason and used three other methods instead.
  See [[method-verify-a-zero]].

`GET /rest/firm/types` has four flags — `wantBase`, `wantCodeTables`, `wantIssues` and
**`wantClientLists`** — so there are **four** record-set categories, not the three the corpus
recorded.

There is **no generic bulk export endpoint**: `POST /rest/firm` has no GET counterpart among the 160
operations.

Source: [`features/search-filtering/`](../../docs/features/search-filtering/README.md)
