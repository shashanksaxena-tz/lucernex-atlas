# The Lucernex REST API, explained

**Stated up front.** Lucernex exposes **one generic CRUD controller that serves all 227 record
types**, plus about a dozen purpose-built subsystems around it. The whole surface is **141 paths and
160 operations — 104 GET, 40 POST, 7 PUT, 9 DELETE**. Writes are first-class, which corrects the
corpus's standing picture that the write path was unknown (that picture came from GraphQL, which has
617 queries against 3 mutations — a different surface entirely).

The complete specification is stored verbatim at
[`lucernex-openapi-3.0.1.yaml`](lucernex-openapi-3.0.1.yaml) — OpenAPI 3.0.1, 132,839 bytes, fetched
from `GET /rest/api-docs/swagger` on build `26.09.0.113`.

| | |
|---|---|
| Title / version | `Lucernex API` 1.0.0 |
| Server | `https://{tenant}.lucernex.com/rest` |
| Paths / operations | 141 / 160 |
| Schemas | 25 |
| Declared `securitySchemes` | **none** — see [Authentication](#authentication) |

---

## 1. The shape: one controller, many satellites

**Observed.** Nine operations under `/businessObject` handle every one of the 227 record types.
Everything else is a specialised subsystem. Grouped by path family, largest first:

| Family | Ops | What it is |
|---|---:|---|
| `/documents` | 19 | Document search (SOLR-backed) and index jobs |
| `/reportBuilder` | 15 | Stateful, server-side report construction |
| `/cluster` | 12 | Hazelcast cluster, async tasks, scheduled jobs |
| `/lookerapi` | 10 | Looker BI embedding — dashboards, looks, folders |
| **`/businessObject`** | **9** | **The generic CRUD surface for all 227 types** |
| `/adapter-config` | 9 | Vendor adapter field-mapping, with per-firm overrides |
| `/task` | 9 | Async task lifecycle |
| `/atlas-api` | 6 | AI lease-abstraction import |
| `/firm` | 6 | Bulk import (the Messenger format) |
| `/audit` | 5 | Change audit trail |
| `/i18n` | 5 | Currency, date and number formatting |
| `/jwt` | 5 | Token minting |
| `/pageLayout`, `/pagelayoutfield`, `/mobilelayout` | 9 | Layout engine |
| `/codeTableEntry`, `/fieldGroup`, `/properties` | 10 | Configuration |
| `/guardrails`, `/loadlimits` | 5 | Operational protection |
| others | ~20 | photo, msproject, payments, entity search, virtual records |

**The design reading:** Lucernex did not build 227 controllers. It built **one**, parameterised by
`{objectType}`, and then added satellites only where generic CRUD genuinely could not serve — search,
reporting, async, integration, layout.

---

## 2. The generic CRUD surface

Nine operations, and they are the whole data API.

```
GET    /businessObject/{objectType}                      list links
GET    /businessObject/{objectType}/details              query records
GET    /businessObject/{objectType}/lxid/{lxID}          read one, by internal id
GET    /businessObject/{objectType}/clientid/{clientID}  read one, by YOUR id
POST   /businessObject/{objectType}                      create  (?allowUpdate=true → upsert)
PUT    /businessObject/{objectType}                      update
POST   /businessObject/{parentObjectType}/{parentID}     create child under a parent
DELETE /businessObject/{objectType}/lxid/{lxID}          delete by internal id
DELETE /businessObject/{objectType}/clientid/{clientID}  delete by YOUR id
```

`{objectType}` accepts any type from **`GET /firm/types`**. That endpoint is also the way to
discover what exists — it returns types the object-model viewer refuses to show, which is how the
`PageLayout` family was recovered.

### Two identifier spaces, and this is a design decision worth copying

Every read and delete exists **twice**: once by `lxid` (Lucernex's internal primary key) and once by
`clientid` (**an identifier you supply**). Creation upserts on the client id when
`?allowUpdate=true`.

That is why **`BOMapClientRecordID` is required in 133 of 202 tables** — by a wide margin the most
mandatory field in the product. It is the correlation key an external system uses to address records
without ever learning Lucernex's ids.

**For a rebuild:** a stable external identifier on every record is load-bearing here, not decoration.
It is what makes the integration surface idempotent.

### The payload is recursive

```jsonc
{
  "botype": "Contract",              // required
  "clientID": "ASG1234",             // your identifier
  "fields":   [ { "name": "ContractName", "value": "..." } ],
  "children": [ { "botype": "Allowance", "fields": [ ... ] } ]   // recursive
}
```

`children[]` holds `BusinessObject` again, to any depth. **A parent and its children go in one
call** — which is very likely how the 5-step contract wizard persists, since its step 1 writes across
both `Contract` and `Facility`.

Note the flat `fields[]` array of `{name, value}` pairs rather than a typed object. Everything is a
string on the wire; typing lives in the schema, not the payload.

Both **JSON and XML** are accepted and returned. This is not cosmetic — the same tenant answered one
call in JSON and another in XML during this capture, so **a client that assumes either format will
silently mis-parse**. Set `Accept` explicitly.

### Querying: FIQL, with a caveat

```
GET /businessObject/{objectType}/details?fiql=...&fields=...&$skip=...&$top=...
```

- **`fields` is mandatory.** There is no "give me everything".
- **`413 Too many records returned`** is a declared response — the server refuses oversized result
  sets rather than truncating. Page with `$skip`/`$top`.
- **FIQL does not work as documented.** *(Observed.)* `fiql=ProjectEntityTypeName==Contract` returns
  `{}` despite 2,007 matching records. The parameter is accepted and silently yields nothing. **Use
  `$top` scans and filter client-side**, and do not build against the documented filter without
  testing it.

---

## 3. Writes return a bulk envelope — HTTP 200 does not mean success

**This is the single most important integration constraint in the API.**

Writes respond with `ImportResults`:

```jsonc
{
  "successes": [ { "objectType": "...", "clientID": "...", "lxID": "...",
                   "create": true, "update": false, "delete": false } ],
  "errors":    [ { "objectType": "...", "clientID": "...", "message": "...",
                   "lookup": false, "fatal": true, "position": 12 } ]
}
```

A request can return **`200 OK` with a populated `errors[]`**. Any client treating 2xx as success
**loses data silently**.

`ImportError` distinguishes two failure kinds:
- **`lookup`** — a referenced record could not be resolved
- **`fatal`** — the write itself failed

`position` locates the failure within a batch. A rebuild should keep both the envelope and that
distinction: "your reference was wrong" and "the write broke" need different handling by the caller.

---

## 4. Bulk import: `POST /firm`

```
POST /rest/firm?synchronous={bool}&stopOnError={bool}
```

- `synchronous=true` → **200** with results; `false` → **202 Accepted**, poll via `/task`.
- **`stopOnError` defaults to on-first-error** in the UI, so a partial import is opt-in, not the
  default.
- Consumes the **same XML** that `Export Configuration` produces — which is why **configuration and
  data round-trip through one format**, and why the Hub→Spoke publish mechanism has working prior art
  here.
- The importer **creates parents implicitly**: importing Facility records creates or updates their
  Location. A rebuild that rejects a facility whose location does not exist will fail on files
  Lucernex accepts.

`POST /firm/document` imports documents; `GET /firm/types` lists the type vocabulary.

---

## 5. Async: everything slow is a Task

`/task` and `/cluster` implement one pattern used across the API:

```
POST /task                     → create, returns a name
GET  /task/state/{name}        → poll state
GET  /task/{name}              → full record
GET  /task/download/{name}     → retrieve the generated file
DELETE /task/{name}            → cancel
GET  /task/mine                → the caller's latest
```

`/cluster` exposes the Hazelcast grid beneath it — members, stats, `rejoin`, scheduled jobs,
async-task eviction. **Lucernex runs clustered**, which is consistent with the `hazelcast.sessionId`
cookie and with the load-balancer node-affinity behaviour that repeatedly killed sessions during this
capture.

Long imports are async by design: `POST /atlas-api/import/{leaseId}/async` returns a task, and
`GET /atlas-api/import/events/{taskName}` **streams progress events**.

---

## 6. The AI lease-abstraction pipeline

Three families — 16 operations — form a **third-party AI abstraction integration**:

```
GET  /atlas-api/leases                     list leases available from Atlas
POST /atlas-api/import/{leaseId}           import one
POST /atlas-api/import/{leaseId}/async     import one, async
POST /atlas-api/sync                       import all
GET  /atlas-api/contracts                  contracts eligible for update-existing import
GET  /atlas-api/import/events/{taskName}   stream progress
POST /vendor-lease/{vendorId}/import       import an abstract from a vendor-specific JSON payload
```

and the mapping layer that makes it tenant-configurable:

```
GET|PUT|DELETE /adapter-config/{vendorId}/{fileName}                    vendor default
GET|PUT|DELETE /adapter-config/firms/{firmId}/{vendorId}/{fileName}     per-firm override
GET            /adapter-config/vendors                                  registered adapters
```

**The AI-extraction → Lucernex field mapping is configuration, per tenant, not code.** `/vendor-lease`
being vendor-parameterised means Atlas is one adapter among a possible several.

This explains four otherwise-unconnected observations: the `Allow AI Lease Abstraction` Firm flag,
BBW's seven `ASG Lease Abstract - *` layouts, the `AI Abstracted` value across four status code
tables, and that value becoming platform-protected in build `26.09`.

---

## 7. Reporting is stateful and server-side

`/reportBuilder` is not a query API. It is a **session-scoped builder**:

```
addfield · deletefield · movefield · updateSpan · setAlignment
setcriteria · setsort · columns · includedfields
builderState · restoreBuilderState · clearBuilderState · save · insert
```

The user's in-progress report lives **on the server**, mutated field by field. Fourteen of its
fifteen operations are `GET` — including the mutating ones — so it is not REST in any meaningful
sense; it is a remote-procedure surface over HTTP.

`/lookerapi` is a separate, modern BI embedding path (dashboards, looks, folders, `embedurl`). **Two
generations of reporting coexist.**

---

## 8. Authentication

**The spec declares no `securitySchemes` at all.** Authentication is out-of-band, and the product
offers two, both mintable:

- **Basic**
- **JWT Bearer** — `POST /jwt`, with variants `/jwt/help`, `/jwt/invoicesService`, and
  `/jwt/crue/refresh` + `/jwt/crue/touch` for the Lease-AI host page

`/en/test/RESTful.jsp` renders live tokens of both kinds for the signed-in user. **That page is on the
capture-exclusion list** ([`../../tenants/CAPTURE-EXCLUSIONS.md`](../../tenants/CAPTURE-EXCLUSIONS.md));
no token was read or recorded at any point in this work.

That an API this broad ships with **no security scheme in its own specification** is itself worth
noting — a generated client will have no auth wired in.

---

## 9. Operational surfaces worth knowing

| Family | Why it matters |
|---|---|
| `/guardrails/override/{enable,disable,status}` | An **emergency override**, LxAdmin-only, per firm. Guardrails exist and can be switched off |
| `/loadlimits`, `/loadlimits/config` | Query-load metering and its configuration |
| `/audit`, `/audit/{peid}/{lastModified}` | Change audit; the `peid`+`lastModified` form supports incremental sync |
| `/deletions` | Tombstones — how a consumer learns something was deleted |
| `/cluster/stats`, `/cluster/members` | Cluster health |

`/audit/{peid}/{lastModified}` plus `/deletions` plus `lastModifiedValue` on the list endpoint is a
**complete incremental-replication toolkit**: changed records, deleted records, and a watermark. If
ASG Edge+ needs to sync from Lucernex during migration, that is the mechanism.

---

## 10. What this means for ASG Edge+

**Copy:**
- **One generic CRUD controller** parameterised by type, not 227 controllers.
- **Dual identifier space** — internal id *and* caller-supplied id, with upsert on the latter.
- **Recursive payloads** so an aggregate writes in one call.
- **The incremental-sync triple** — audit-since, deletions, last-modified watermark.

**Fix:**
- **`200` must mean success.** The `ImportResults` envelope is a genuine trap. Keep the
  `lookup`/`fatal` distinction, but surface failure in the status code.
- **Make the query language work.** FIQL is documented and non-functional.
- **Declare the security scheme** so generated clients are usable.
- **Pick one wire format**, or set `Content-Type` reliably.

**Decide deliberately:**
- Stateful server-side report building is a heavy pattern. Lucernex already runs a second, modern
  reporting path alongside it.
- `mobilelayout` and `pagelayoutfield/securityaccess` show layout, security and mobile are all
  API-addressable — a broad configuration-as-API surface to reproduce or narrow on purpose.

---

## Open questions

1. **FIQL.** Is it non-functional, or does it require a syntax the spec does not document? It is the
   only filtering mechanism offered, and it returns `{}` rather than an error.
2. **`updateOnly` and `match`** on `BusinessObject` are undocumented in the spec. `match` is described
   only as *"match employer only by clientID"*, which reads like a leaked special case.
3. **`/virtual/{virtualBOType}`** — "Query virtual records for a Contract". The `Virtual*` projections
   are API-addressable, but the semantics are undescribed.
4. **107 of 160 operations carry no tag and 60-odd have no summary.** The generated spec is thin on
   description; behaviour for most of the satellites is unverified by this document.
5. **Nothing here has been exercised with a write.** Every claim about write behaviour is read from
   the specification, not observed — this work was read-only throughout.
