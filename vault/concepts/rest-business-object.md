---
title: The generic REST controller
tags: [concept, api, core]
evidence: Observed
---

One controller serves **all 227 record types**. The full OpenAPI 3.0.1 document is served at
`/rest/api-docs/swagger`: **141 paths, 160 operations — 104 GET, 40 POST, 7 PUT, 9 DELETE**, 11 tags,
25 schemas.

```
POST   /rest/businessObject/{objectType}                     create  (?allowUpdate=true upserts)
PUT    /rest/businessObject/{objectType}                     update
POST   /rest/businessObject/{parentObjectType}/{parentID}    create child
DELETE /rest/businessObject/{objectType}/lxid/{lxID}
DELETE /rest/businessObject/{objectType}/clientid/{clientID}
GET    /rest/businessObject/{objectType}/details?fiql=…&fields=…&$skip&$top
```

**REST is the write path.** The corpus's standing picture — *"617 GraphQL queries against 3
mutations, so the write path is unknown"* — describes GraphQL only.

The body is a recursive `BusinessObject`: `botype` required, `fields[]`, nested `children[]`, JSON or
XML. **A contract and its children can be written in one call**, which is probably how the
[[screen-contract-wizard|wizard's multi-entity step]] is served.

Three things to carry:

- **[[finding-http-200-is-not-success]]** — writes return an `ImportResults` bulk envelope.
- **Dual identifier space.** `/lxid/{id}` is the internal key; `/clientid/{id}` is
  `BOMapClientRecordID`, the integration key, required on 133 of 202 tables and confirmed as the
  upsert key.
- Reads use [[fiql]], `fields` is **mandatory**, and the endpoint returns **413** when too many are
  requested.

It is also how the **25 tables the schema viewer refuses** were recovered, including the whole
[[PageLayout]] family — with the caveat that the serialiser emits only *populated* columns, so column
lists from this route are a **lower bound, not a schema**.

Auth is out of band: the spec declares **no `securitySchemes`**; Basic or JWT Bearer supplied
externally.

Source: [`data-model/api/`](../../docs/data-model/api/README.md)
