# The REST API surface

**Stated up front.** Lucernex ships a self-documenting REST API covering **all 223 record types** —
the same 223 in the schema dump, not a subset. Its documentation page lets you pick a record type
and filter the field list by *required / editable / read-only*, separately for platform fields and
tenant fields. That per-type, per-field mutability metadata is exactly what
[`modules/accounting/computed-vs-input-fields.md`](../modules/accounting/computed-vs-input-fields.md)
had to reconstruct by inference, and it exists here as first-class vendor data.

> **Superseded, 2026-09-13.** This document recorded that *"the documentation body did not render, so
> the endpoint shapes themselves remain uncaptured"*. **That is no longer true.** The full OpenAPI
> 3.0.1 spec was fetched from `/rest/api-docs/swagger` on `(ASG)BBW`, build `26.09.0.113`:
> **141 paths, 160 operations — 104 GET, 40 POST, 7 PUT, 9 DELETE.** The surface is fully CRUD over a
> single generic controller serving all 227 record types, and it is how the 25 tables
> `ShowObjectDetails.jsp` refuses were finally read. Raw capture:
> [`../tenants/bbw-rest-api.json`](../tenants/bbw-rest-api.json); analysis and the integration
> constraints in [`../features/import-export/`](../features/import-export/).
>
> Three things from that capture bear directly on this page:
> - **Writes return an `ImportResults` body with `successes[]` / `errors[]`, so HTTP 200 does not
>   mean the records were written.** A client checking only the status code silently loses data.
> - **`@clientID` in the serialisation is `BOMapClientRecordID`** — the external key that is required
>   on 133 of 202 tables — and `/businessObject/{type}/clientid/{clientID}` is a first-class peer of
>   `/lxid/{lxID}`, with `POST …?allowUpdate=true` performing an upsert against it.
> - Reads use **FIQL** via `/businessObject/{objectType}/details`, where `fields` is **mandatory** and
>   an over-broad query returns **413** rather than a truncated result.
>
> The `/en/test/RESTful.jsp` page described below renders live Basic and JWT credentials and is now
> on the capture-exclusion list; the spec route above needs no such page.

**Everything below this note describes the `/en/test/RESTful.jsp` documentation page as captured on
2026-09-10**, and its observations about per-type, per-field mutability metadata still stand.

| Property | Value |
|---|---|
| Route | `/en/test/RESTful.jsp` |
| Admin entry point | System Administrator Dashboard → Data/PS Tools → **RESTful WebService Docs** |
| Record types offered | **223** |
| Auth modes | **Basic** and **JWT Bearer** |
| Captured | 2026-09-10, tenant `(ASG)American Freight`, build `26.08.0.46` |
| Exploration mode | Read-only. The two "Copy … token to Clipboard" controls were deliberately **not** used — those are live credentials. |

## The three record sets

The page's `Record Sets` menu offers exactly three families. **Observed.**

| Record set | What it covers |
|---|---|
| `Base` | The ordinary business entities — Contract, Facility, Location, Asset, and so on |
| `CodeTables` | The master/lookup tables — the 207 Firm Drop Downs and their kin (see [`code-table-registry.md`](code-table-registry.md)) |
| `Issues` | The ticket/request family |

**This is a third independent confirmation that `Issue` is a first-class citizen of the
architecture**, not a workflow implementation detail. The vendor's own API taxonomy divides the
whole product into *things*, *lookups*, and *issues*. Taken with `IssueInterface` in the GraphQL
schema and `TableType=2035` being `Issue Type Code`, the picture in
[`../modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`](../modules/layouts-and-forms/forms-vs-pages-vs-layouts.md)
is settled from three directions.

For ASG Edge+ this is a strong hint about top-level API shape: three families, not one flat
resource list.

## Field mutability filters

Two further menus filter which fields the documentation shows. **Observed.**

| Menu | Options |
|---|---|
| `Core Fields` | `Required`, `Editable`, `ReadOnly` |
| `Firm Fields` | `Editable`, `ReadOnly` |

Two things follow.

**The platform knows, per record type, which fields are required, editable and read-only.** That
metadata is the backbone of any rebuild's validation layer, and it is available here directly rather
than inferred. It also corroborates the `COMPUTED` first-class type in the GraphQL `FieldType` enum
(see [`graphql-api.md`](graphql-api.md)): read-only fields are largely the computed ones.

**Firm fields have no `Required` option.** Core (platform) fields can be required; tenant-defined
fields apparently cannot — or at least the API documentation does not model them that way. If that
holds, it is a meaningful constraint: **a tenant cannot make its own custom field mandatory through
this surface.** It would also explain why the conditional-rule engine has a distinct
`Show and Require` action ([`conditional-fields.md`](../modules/layouts-and-forms/conditional-fields.md)) —
that may be the *only* route to a required tenant field. Worth confirming, because ASG Edge+ will
certainly be asked for mandatory custom fields.

## Relationship to the GraphQL API

[`graphql-api.md`](graphql-api.md) records 617 queries against just 3 mutations, and concludes the
GraphQL surface is read-oriented with an integration-shaped write path (`createMember`,
`importLeaseAbstract`, `importVendorLease`).

The existence of a full REST surface over all 223 types, documented with per-field editability, is
consistent with **REST being the general-purpose read/write API and GraphQL being the query and bulk-import
API**. That remains **Inferred** — the actual REST verbs were not observed — but it is the reading
the evidence supports, and it matters: a rebuild deciding between GraphQL-first and REST-first should
not conclude from Lucernex's 3 mutations that the vendor avoids write APIs.

## What did not work

The `Load` button was exercised four ways — a real click on the button, a click via its element
reference, invoking the Ext handler directly, and selecting a `Record Sets` value first and then
loading. In every case the type selection registered correctly (the tag field showed
`Selected Contract.`) and the `Base` menu item checked, but **the documentation panel stayed empty**
and the page's text content did not change.

No conclusion is drawn about why. Exploration stopped there rather than continuing to probe. The
endpoint shapes, verbs, request and response bodies are therefore **not captured**.

## Open questions

1. **What does the documentation actually render** — endpoint paths, verbs, payload schemas? This is
   the single largest remaining gap in understanding the write path.
2. **Are REST writes full CRUD per record type**, or is the surface read-plus-import like GraphQL?
   This determines whether the incumbent has a general write API at all.
3. **Confirm that Firm (tenant) fields genuinely cannot be marked required**, and if so, whether
   `Show and Require` on a page layout is the only mechanism for a mandatory custom field.
4. **Does the REST layer expose the same FIQL filter grammar** the GraphQL examples use?
5. **What is the `Data Dictionary` menu item** seen in the application chrome alongside `Bookmark`?
   It may be a further schema-documentation surface not yet explored.
