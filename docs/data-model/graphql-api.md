# Lucernex GraphQL API — schema introspection

**Stated up front:** Lucernex exposes a complete, introspectable GraphQL API at `/servlet/graphql`.
Its schema is the most authoritative description of the product's data model available to us —
better than any UI capture or spreadsheet export, because it is the contract the vendor's own
clients compile against. It contains **490 types** and **617 root query fields**, and it reveals a
clean underlying type system that the 448 messy `sTYPE_*` codes in Manage Data Fields sit on top of.

| Property | Value | Confidence |
|---|---|---|
| Endpoint | `POST /servlet/graphql` | **Observed** |
| Client | Altair GraphQL Client, embedded via iframe at `/all/altair/index.html` | **Observed** |
| Admin entry point | System Administrator Dashboard → Data/PS Tools → **GraphQL Explorer** (`/en/admin/graphql.jsp`) | **Observed** |
| Auth | Bearer JWT, minted per-session and passed to the iframe as a query parameter | **Observed** |
| Introspection | Enabled, unrestricted | **Observed** |
| Build | `26.08.0.46 (2026/08/26 16:15)`, tenant `(ASG)American Freight`, captured 2026-09-10 | **Observed** |

## Schema shape

| Kind | Count |
|---|---:|
| OBJECT | 433 |
| INPUT_OBJECT | 31 |
| SCALAR | 10 |
| ENUM | 10 |
| INTERFACE | 6 |
| **Total** | **490** |

| Root type | Fields |
|---|---:|
| `Query` | **617** |
| `Mutation` | **3** |

**Derived:** the API is overwhelmingly read-oriented — 617 queries against 3 mutations. Writes are
evidently not intended to flow through GraphQL; the separate **RESTful WebService Docs** admin tool
(`/en/test/RESTful.jsp`) is the likely write surface. *This needs confirming before ASG Edge+
commits to a GraphQL-first API design.*

## The JWT

The session JWT's claims are worth recording because ASG Edge+ has an equivalent design decision
already made (only the gateway validates a JWT; it forwards `X-User-Id`, `X-Tenant-Id`, `X-Roles`).

| Claim | Meaning | Confidence |
|---|---|---|
| `aud` = `/servlet/graphql` | Audience-scoped to the GraphQL servlet specifically | **Observed** |
| `iss` = `https://<tenant>.lucernex.com/rest` | Issued by the REST tier | **Observed** |
| `firmname` | **The tenant identifier travels inside the token** | **Observed** |
| `username` | The acting user | **Observed** |
| `cluster` | A `<host>:<tenant-schema>` pair — evidence of physical tenant partitioning | **Observed** |
| `numberFormat`, `dateFormat` | Per-session locale/formatting carried in the token | **Observed** |
| `version` | Application version | **Observed** |

**Inferred:** the `cluster` claim's `host:tenant` shape suggests Lucernex routes a request to a
tenant-specific database or schema using a value carried in the token — structurally the same idea
as ASG Edge+'s planned `AbstractRoutingDataSource` Hub/Spoke routing. Worth confirming; it would be
a strong precedent for the ASG Edge+ multi-tenancy ADR that is still unreconciled.

The token itself is a live credential and is deliberately not recorded in this repository.

## The canonical type system — `FieldType`

This is the single most important discovery for the ASG Edge+ rebuild. Manage Data Fields exposes
**448 distinct `sTYPE_*` / `sCODE_*` codes**, which looks unmanageable. The GraphQL schema shows
those are presentation-layer codes over a **10-value canonical type system**:

```
BOOLEAN  COMPUTED  DATE  DATETIME  FK  FLOAT  INTEGER  MONEY  PERCENTAGE  STRING
```

**Observed.** Two entries carry most of the weight:

- **`COMPUTED` is a first-class field type**, not a convention. This corroborates, at schema level,
  the `sTYPE_MONEY_MATH_OPERATION` / `sTYPE_PERCENT_MATH_OPERATION` families in Manage Data Fields:
  the platform distinguishes engine-calculated values from user input in its type system. Any rule
  engine ASG Edge+ builds must make the same distinction explicit.
- **`FK` is a first-class field type**, confirming from a second independent source what
  [009](../admin/009-related-fields-and-data-model.md) established from the View Object Model tool:
  the relational model is real and declared, not inferred from naming.

Note also `MONEY` and `PERCENTAGE` as distinct from `FLOAT`, and the presence of a **`BigDecimal`
scalar**. Lucernex does not represent money as a float. ASG Edge+ Constitution §4.4 forbids `double`
in financial code — the vendor independently reached the same conclusion, which is useful evidence
when defending that rule.

## Scalars

```
BigDecimal  Boolean  Date  DateTime  Float  Int  JSON  Long  String  UUID
```

**Observed.** `JSON` and `UUID` as scalars, alongside `Long` for identifiers.

## Interfaces — the architectural spine

Six interfaces carry the product's cross-cutting concepts. Each one confirms a hypothesis that was
previously only inferred from UI exploration.

| Interface | What it establishes | Corroborates |
|---|---|---|
| `ProjectEntity` | The universal entity spine. `ProjectEntityID` appears on nearly every table in the schema dump; here it is a declared interface, not a convention. | The `ProjectEntity` question in `docs/data-model/project-entity.md` |
| `HasUDFs` | User-defined fields are a **declared, generic capability** a type either has or does not. Every example query selects them as `udfs { name type value }`. | [005](../admin/005-manage-data-fields.md) — Manage Data Fields is the UDF registry |
| `iCodeTable` | All drop-downs/code tables share one interface — a uniform master-data concept. | [007](../admin/007-firm-and-client-drop-downs.md) — Firm & Client Drop Downs |
| `ClientListRowInterface` | Custom Lists are rows on a shared generic row type. | [006](../admin/006-manage-custom-lists.md), which observed the `ClientListRow` script object |
| `IssueInterface` | `Issue` is a generic unit-of-work reused across bidding, invoicing and workflow. | The `Issue`/`Task`/`WorkFlow` family |
| `HasProjectEntity` | The "belongs to a ProjectEntity" capability, separate from being one. | — |

## Enumerations — the rule vocabulary

These ten enums are, in effect, the product's rule vocabulary. Four of them answer questions that
were previously open.

### `KickOffMethod` — how a workflow is triggered

```
STEP_ACTION   PAGE_LAYOUT   STATUS_CHANGE   TASK
```

**Observed.** Lucernex workflows can be initiated four ways: by an action on a preceding workflow
step, from a page layout (i.e. a button placed on a form — which matches [008](../admin/008-manage-page-layouts.md)'s
finding that layouts can host business-action buttons), by a record's status changing, or by a task.
This is the trigger taxonomy any ASG Edge+ rule engine must reproduce.

### `AssigneeType` — how work is routed

```
ALL   PARENT   REGION1   REGION2   MARKET   JOB_TITLE
```

**Observed.** Routing is not by named user. It is by organisational position — region levels,
market, job title, or inheritance from a parent. Role-based, not identity-based.

### `MemberNotifyType` — how notifications are targeted

```
ORGCHART_ALL  ORGCHART_LEV1  ORGCHART_LEV2  ORGCHART_LEV3  ORGCHART_MKT
USERCLASS     JOBTITLE       MEMBERID
```

**Observed.** Notification targeting walks the org chart to three explicit levels, plus market,
plus the three flat targets (user class, job title, specific member). The org chart is therefore a
real, queryable structure, not just a display artefact.

### `GaapAmortizeMode` — the accounting engine's amortisation basis

```
PER_DAY   PER_PERIOD
```

**Observed.** Straight-line/GAAP amortisation runs on one of two bases. This is a genuine
accounting-policy switch and belongs in the ASG Edge+ accounting engine's rule set.

### Remaining enums

| Enum | Values |
|---|---|
| `SecurityLevel` | `DEFAULT`, `NO_ACCESS`, `VIEW`, `EDIT`, `DELETE` |
| `OperatingStatus` | `PRE_OPEN`, `OPERATING` |
| `SortDirection` | `ASC`, `DESC` |
| `FieldType` | see above |

`SecurityLevel` is the whole permission ladder — five levels, applied (per
[008](../admin/008-manage-page-layouts.md)'s `Allow Edit* = No` observation) at least down to
layout granularity.

## Query conventions

The Explorer ships **177 worked example queries** (`window.queryExamples`, 175 distinct bodies,
~62 KB). They establish the API's conventions:

| Convention | Example | Confidence |
|---|---|---|
| Fetch by internal id | `contract(lxID: 12345)` | **Observed** |
| Fetch by client's own id | `contractByClientID(clientID: "LEASE-AUSTIN-001")` | **Observed** |
| Collection query with total | `contracts(...) { total items { ... } }` | **Observed** |
| **FIQL filter language** | `fiql: "codeContractStatusID==Active;expireDate=lt=2026-01-01"` | **Observed** |
| Offset/limit pagination | `offset: 0, limit: 50` | **Observed** |
| Multi-column sort | `sort: [{ field: "expireDate", direction: ASC }]` | **Observed** |
| Code tables expand to a pair | `codeContractStatusID { shortName longName }` | **Observed** |
| UDFs selected generically | `udfs { name type value }` | **Observed** |

**FIQL** (Feed Item Query Language) is the notable one: `;` is AND, `,` is OR, `==` equality,
`=lt=`/`=gt=` comparisons, `=in=` list membership, `=like=` pattern match. Lucernex adopted a
standard filter grammar rather than inventing one. ASG Edge+ should decide deliberately whether to
do the same — it is a well-specified grammar with existing parsers.

**Dual-identity addressing** is the other one worth copying: every major entity is reachable both
by Lucernex's internal `lxID` and by the customer's own `clientID`. That is what makes migration
and integration tractable, and it is a design ASG Edge+ will need from day one.

## Example-query coverage

The 177 examples are grouped by entity and by query pattern. Entities covered include Contract,
Location, Facility, Asset, Project, Program, Member, Party, Document, Folder, Allowance, Security
Deposit, Expense Setup, Expense Schedule, Key Dates, Bid Package, Issue, and Contract Amendment.
Pattern examples include multiple filters, OR conditions, `like` filters, `in` lists, pagination,
and multi-sort.

## Open questions

1. **What are the 3 mutations?** With 617 queries and only 3 mutations, the write path is the
   single biggest unknown in the API. Enumerate them and determine what the intended write surface
   actually is.
2. **Does the schema contain the conditional-field rule storage?** The per-field conditional display
   rule editor (see [008](../admin/008-manage-page-layouts.md)) was never opened. If a
   `Condition`/`Rule`/`Criteria` type exists in these 433 object types, it settles the mechanism
   without needing the blocked UI.
3. **What does `RESTful.jsp` document**, and is it the write path implied by question 1?
4. **Does `Export Schema` produce a downloadable full schema file?** That would give the complete
   250 KB SDL and the physical model in one step, without paging it through a browser tool.
5. **Is the `cluster` JWT claim genuinely a tenant-routing key?** If so it is direct vendor
   precedent for the ASG Edge+ Hub/Spoke routing design.
