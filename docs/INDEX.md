# Lucernex exploration — master index

This corpus documents **Lucernex IWMS (LxRetail by Accruent)** as it actually runs, so that ASG
Edge+ can be rebuilt from evidence rather than from memory. Everything here was read out of the
live `(ASG)American Freight` training tenant, build `26.08.0.46`, or out of the vendor's own schema
exports.

**Start here if you are new:** [The interactive atlas](#the-atlas) for the shape of the system, then
[the four big answers](#the-four-answers) for what was learned, then the module you care about.

**If you are an AI agent:** read [`CONVENTIONS.md`](CONVENTIONS.md) first. It defines the folder
layout, the Observed / Derived / Inferred evidence discipline every document follows, and the raw
source files available offline.

---

## The atlas

[**`mindmap/lucernex-atlas.html`**](mindmap/lucernex-atlas.html) — the interactive app. It carries
**two deliberately separate maps**, switched by a **Feature view / Schema view** toggle on the map
itself:

- **The feature map** (`#/map?set=feature`) — the product organised by *what it does*, written in
  product language: 18 features from ASC 842 Accounting to Admin & Tenancy, each opening onto its
  capabilities with **every label a short name (≤24 characters) and the full explanation in the
  panel that opens when the node is clicked**. The product's **519 numbered rules** sit in one
  collapsed *Rules (N)* folder per feature; each rule's visible name is a short summary and its ID
  lives in the panel, which links to the full rule page (676 nodes). It opens fully expanded to
  feature → capability, so the shape of the product is visible with zero clicks. Deep-link a
  feature with `#/map?set=feature&f=<module id>`. Built by
  [`mindmap/build_featuremap.py`](mindmap/build_featuremap.py).
- **The schema map** (`#/map`) — drills **Product → Module → Entity → Field group → Field → Type →
  the record that type points at**, and keeps going, because the foreign-key graph is cyclic. Every
  node carries its confidence label and its source. Three modules carry a hand-written **Analysis**
  branch (tinted, named `Analysis · …`) — internal mechanics, kept out of the feature map.

Both built by two re-runnable scripts: [`mindmap/build_graph.py`](mindmap/build_graph.py) (parses the
schema dump into `objects.json` / `edges.json` / `modules.json`) and
[`mindmap/build_mapdata.py`](mindmap/build_mapdata.py) (compacts them into `mapdata.json` for the
page). Re-run both after any schema recapture, then rebuild the HTML.

Built by two re-runnable scripts: [`mindmap/build_graph.py`](mindmap/build_graph.py) (parses the
schema dump into `objects.json` / `edges.json` / `modules.json`) and
[`mindmap/build_mapdata.py`](mindmap/build_mapdata.py) (compacts them into `mapdata.json` for the
page). Re-run both after any schema recapture, then rebuild the HTML.

Three schema-map modules additionally carry a **hand-written Analysis** branch, tinted so it
reads as analysis rather than generated structure. These explain how the module works *internally*
and carry the rules and constraints no schema dump can express — together **758 nodes, 277 of them
rule nodes**. They deliberately stay inside the schema map; the feature map tells the product
story instead.

| Tree | Nodes | Depth | Rule nodes |
|---|---:|---:|---:|
| [`mindmap/accounting-tree.json`](mindmap/accounting-tree.json) | 275 | 10 | 67 |
| [`mindmap/contracts-tree.json`](mindmap/contracts-tree.json) | 281 | 9 | 148 |
| [`mindmap/workflow-tree.json`](mindmap/workflow-tree.json) | 202 | 11 | 62 |

`build_mapdata.py` picks these up automatically by filename; adding
`facilities-tree.json` and so on requires only registering the module in its `CURATED_FOR` map.

| | |
|---|---:|
| Modules | 15 |
| Record types | 223 |
| Fields | 7,421 |
| Foreign keys | 972 |
| Manage Data Fields leaves | 6,158 |
| GraphQL types | 490 |

---

## The four answers

The questions that drove this pass, and where each is settled.

| Question | Answer | Document |
|---|---|---|
| **How does conditional field filtering work?** | A flat rule engine: `[Show \| Show and Require \| Hide] this field when [all \| any] of these rules match`. Operators depend on the driver's type. Drivers cross foreign keys into related entities. | [`modules/layouts-and-forms/conditional-fields.md`](modules/layouts-and-forms/conditional-fields.md) |
| **How is a Form different from a Page?** | A Page presents an entity that already exists. A **Form is an Issue Type** — a tenant-defined request type with one layout per workflow step. A Custom List is a Form without the workflow. | [`modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`](modules/layouts-and-forms/forms-vs-pages-vs-layouts.md), [`data-model/code-table-registry.md`](data-model/code-table-registry.md) |
| **What are the workflows?** | Four live workflows, 1:1 with four form types. Lease Admin Request's 8 steps *are* BRD-24. Routing is by organisational position, not by name. | [`modules/workflow/`](modules/workflow/) |
| **How does ASC 842 work?** | One engine, three standards, selected by flags on `SLSummary`. Classification is a separate 93-field record. Schedules are **approved, not published**. | [`modules/accounting/`](modules/accounting/) |

---

## Screens explored

| ID | Screen | Status | Document |
|---:|---|---|---|
| 001 | Dashboard home | Captured | [Open](screens/001-dashboard-home.md) |
| 002 | Help menu | Captured | *document not yet written* |
| **003** | **Main navigation — the whole product in four roots** | **Captured** | [Open](screens/003-main-navigation.md) |
| 004 | System Administrator Dashboard | Captured | [Open](admin/004-company-administration.md) |
| 005 | Manage Data Fields (Global + Firm) | Captured, read-only | [Open](admin/005-manage-data-fields.md) |
| 006 | Manage Custom Lists | Captured, read-only | [Open](admin/006-manage-custom-lists.md) |
| 007 | Manage Firm / Client Drop Downs | Captured, read-only | [Open](admin/007-firm-and-client-drop-downs.md) |
| 008 | Manage Page Layouts (5 sub-systems) | Captured, read-only | [Open](admin/008-manage-page-layouts.md) |
| 009 | Related Fields and the data model | Captured, read-only | [Open](admin/009-related-fields-and-data-model.md) |
| 010 | Manage Forms | Captured, read-only | folded into [forms-vs-pages-vs-layouts](modules/layouts-and-forms/forms-vs-pages-vs-layouts.md) |
| 011 | Manage Work Flows | Captured, read-only | folded into [forms-vs-pages-vs-layouts](modules/layouts-and-forms/forms-vs-pages-vs-layouts.md) and [modules/workflow](modules/workflow/) |
| 012 | GraphQL Explorer | Captured, read-only | [data-model/graphql-api.md](data-model/graphql-api.md) |
| 013 | Conditional Filter editor | Captured, read-only | [conditional-fields.md](modules/layouts-and-forms/conditional-fields.md) |
| **014** | **A contract, as a user sees it** — Contract Summary and the ASC 842 Rent Schedule | **Captured, read-only** | [Open](screens/014-contract-record-end-user.md) |

### The end-user application

Screens 001–013 are administration. **003 and 014 are the first captures of the product as a user
actually meets it**, and they change the shape of what is known:

- The whole end-user surface is **four roots — Portfolio, Location, Facility, Contract — 24 groups
  and 81 screens**. Contract alone carries 39 of them.
- **56% of those screens are served by two files**, `PForm.jsp` (detail) and `PLForm.jsp` (list) —
  the runtime face of the Edit Layout / List Layout split. The full routing table, every screen
  mapped to its `PageLayoutID`, is in
  [`data-model/screen-routing.md`](data-model/screen-routing.md) and
  [`mindmap/navtree.json`](mindmap/navtree.json).
- **`Generate Rent` and `Calculate Schedule` are buttons on a record**, not batch jobs. The
  accounting engine is user-triggered.

> **Note on 006, 008 and 009.** All three record a blocker they diagnosed as a popup/window-opener
> problem. That diagnosis was **wrong** and is corrected in
> [`conditional-fields.md`](modules/layouts-and-forms/conditional-fields.md#how-the-blocker-was-cleared)
> — the real dependency is on the host page's `Lx` JavaScript namespace, and the working method is
> written up there for reuse on the editors that remain unopened.

---

## Modules

Each folder carries, at minimum, `README.md`, `data-model.md`, `rules.md` and
`asg-edgeplus-mapping.md`. Rules are numbered so other documents can cite them.

| Module | Rules | What it holds |
|---|---|---|
| [**accounting**](modules/accounting/) | `ACC-R-001…045` | ASC 842, IFRS 16, straight-line. Includes [`computed-vs-input-fields.md`](modules/accounting/computed-vs-input-fields.md) — **666 fields classified INPUT / COMPUTED / CODE-TABLE with evidence per row**, the primary feed for the rule engine |
| [**contracts**](modules/contracts/) | `CON-R-*` | The Contract aggregate and its financials. [`setup-schedule-transaction-pattern.md`](modules/contracts/setup-schedule-transaction-pattern.md) is the architectural centrepiece — and records that **CAM does not follow the pattern** |
| [**workflow**](modules/workflow/) | `WF-R-*` | Template/instance split, step actions, routing, and the **three nested state machines** |
| [**layouts-and-forms**](modules/layouts-and-forms/) | `LAY-R-001…018` | Conditional fields, and the Forms/Pages/Layouts/Custom Lists reconciliation |
| [**reporting**](modules/reporting/) | `RPT-R-*` | The shared field registry — **confirmed**, not hypothesised — and the admin tool inventory |
| [**facilities-locations**](modules/facilities-locations/) | `FAC-R-001…020` | Facility/Location/Complex/Parcel/Prototype/Space/Tenant and the demographics/site-selection family. [`location-vs-facility-vs-site.md`](modules/facilities-locations/location-vs-facility-vs-site.md) settles the central naming question: **Location is the site/"Center", Facility is the building on it** |
| [**platform-tenancy**](modules/platform-tenancy/) | `PLT-R-001…016` | `Firm`, the entity spine's tenant boundary, security, geography, and the org-chart region hierarchy. [`tenancy-model.md`](modules/platform-tenancy/tenancy-model.md) — **`FirmID` is the tenant key, `ProjectEntityID` is not**, and what that does and doesn't settle about ASG Edge+'s two contradictory ADR-004s |
| [**people-parties**](modules/people-parties/) | `PPL-R-001…013` | `Member`, `Person`, `Party`, `Employer`. [`member-vs-person-vs-party.md`](modules/people-parties/member-vs-person-vs-party.md) — **`Person` is a second supertype**, `Member`/`NonMember` its subtypes on a shared key, and why 290 of the schema's foreign keys point at `Member` (83% is just the universal audit-stamp pair) |
| [**assets-equipment**](modules/assets-equipment/) | `AST-R-001…016` | `Asset`/equipment, the `ServiceRequest`→`WorkOrder` maintenance loop, and the parts catalog. [`equipment-leases.md`](modules/assets-equipment/equipment-leases.md) is the module's most valuable file: `ContractFinancialTest`/`SLSummary`/`SLPeriod` each carry a nullable FK straight to `Asset` — **the ASC 842/IFRS 16 engine runs per equipment asset, not only per lease** |
| [**property-tax**](modules/property-tax/) | `TAX-R-001…012` | The `PropertyTaxSummary → Assessment → {Bill → Detail, Appeal → Award}` roll-up under `Parcel`, and — via `CodeRecoveryGroupID`/`CodeRecoveryTypeID` — property tax modelled as a recoverable (CAM) expense, not a simple landlord bill. [`appeals.md`](modules/property-tax/appeals.md) traces the appeal/award workflow and the gap where a won appeal never touches an already-issued bill |
| [**documents-folders**](modules/documents-folders/) | `DOC-R-001…011` | Universal `Documents`/`Binders` tabs on every entity root. Four of the ten objects are near-empty stubs — markup content and outbound correspondence are not recoverable from this schema, and **no object anywhere in the 223-object census backs the universally-visible "Binders" tab** |
| [**portfolio-transactions**](modules/portfolio-transactions/) | `POR-R-001…016` | `Program` (the Portfolio) and the pre-lease deal pipeline `PotentialProject` ("Site") → `RETransaction` → `Scenario`. [`site-pipeline.md`](modules/portfolio-transactions/site-pipeline.md) — the two unique `Program` layout fields (`SiteToProjectSetupLayoutID`, `ProjectToFacilitySetupLayoutID`) that name the Site → Project → Facility promotion pipeline, and the one confirmed FK (`Project.FacilityID`) that closes half of it |
| [**projects-capital**](modules/projects-capital/) | `PRJ-R-001…014` | Capital-project scheduling and the issue/RFI loop. [`scheduling.md`](modules/projects-capital/scheduling.md) — **`Task`, `TaskGroup`, and `TaskItem` are byte-identical tables, and every foreign key of that shape in the entire schema resolves to `TaskGroup` alone**; the WBS hierarchy and the CPM dependency network are two separate graphs over the same rows |

**Two modules have no folder of their own, but are documented.** `expense-recovery` (3 record types,
618 fields) and `variable-rent` (17 record types, 472 fields) are named in
[`modules.json`](mindmap/modules.json) with no `docs/modules/` directory, because the analysis
naturally sat inside the contracts module and was written there:

| Module in `modules.json` | Where it is documented |
|---|---|
| Expense Recovery (CAM / Reconciliation) | [`contracts/expense-recovery-cam.md`](modules/contracts/expense-recovery-cam.md) and [`contracts/cam-waterfall.md`](modules/contracts/cam-waterfall.md) — `ExpenseRecovery` *is* the CAM waterfall |
| Variable Rent (Percentage / Use-Based) & Sales | [`contracts/percentage-rent.md`](modules/contracts/percentage-rent.md) |

So **every in-scope record type has documentation** — 196 of 196, 6,875 of 6,875 fields — but the
folder layout does not map one-to-one onto `modules.json`. Twelve of the fourteen in-scope modules
have a dedicated directory; these two live under `contracts`.

**Out of scope by decision:** cost management, budgeting and bidding. Those objects remain in the
catalogue and the foreign-key graph so the model stays whole, grouped under
`out-of-scope-cost-budget`, with one-line descriptions only.

---

## Data model

| Document | What it holds |
|---|---|
| [`data-model/README.md`](data-model/README.md) | Entry point |
| [`data-model/object-catalog.md`](data-model/object-catalog.md) | All 223 record types: name, Postgres table, field count, module, purpose |
| [`data-model/foreign-key-graph.md`](data-model/foreign-key-graph.md) | The 972 edges, plus hub analysis |
| [`data-model/project-entity.md`](data-model/project-entity.md) | **`ProjectEntity` is the universal entity supertype, and it is *not* the tenant key — `FirmID` is.** Decisive for the database-per-tenant design |
| [`data-model/type-system.md`](data-model/type-system.md) | The full type vocabulary by family |
| [`data-model/graphql-api.md`](data-model/graphql-api.md) | The live API: 490 types, 617 queries, 3 mutations, and the canonical 10-value `FieldType` enum behind the 448 `sTYPE_*` codes |
| [`data-model/rest-api.md`](data-model/rest-api.md) | The REST surface over all 223 record types. Record sets are `Base` / `CodeTables` / `Issues`; fields filter by required / editable / read-only. The endpoint shapes themselves did **not** render and remain uncaptured |
| [`data-model/screen-routing.md`](data-model/screen-routing.md) | **All 81 end-user screens mapped to their `PageLayoutID` and JSP.** 17 renderers serve the lot; two of them serve 56%. Proves Forms and Work Flow are one screen, and that "Portfolio" is `Program` |
| [`data-model/code-table-registry.md`](data-model/code-table-registry.md) | **All 207 Firm Drop Downs with their `TableType` IDs**, the 2000/3000 band split, captured values, and **the contract lifecycle, resolved** |

---

## Field-level reference

[`data-fields/`](data-fields/INDEX.md) — every one of the **6,158** Manage Data Fields leaves,
tabulated per entity across 131 files, plus [`all-fields.csv`](data-fields/all-fields.csv) as a flat
export for the ASG Edge+ parity comparison, and a legend for all 448 field-type codes.

---

## Raw source material

Held at the repository root, outside `docs/`.

| File | Contents |
|---|---|
| `_lucernex_objects_summary.txt` | **223 objects, 7,421 fields** with Postgres table names and declared types. The richest offline artefact |
| `_crossmap.tsv` | Per-field cross-map joining Data Fields leaves to objects/columns, with an `ASGStatus` column |
| `_xlsx_lucernex_jcrew.txt` | Vendor field-definition workbook, including the physical `PG Data Type` column |
| `_xlsx_feature_list.txt` | Vendor feature workbook |
| `docs/assets/raw-captures/` | DOM captures behind the Data Fields analysis |

---

## What is still open

Ranked by how much each blocks the rebuild.

1. **The populated shape of `json.conditionalFieldsConfig`.** The conditional-rule storage format is
   inferred, not observed — the target opened had no rules on it. Find a layout that does.
2. **Contract lifecycle.** `Contract Status Code` has only three values (`AI Abstracted`, `Active`,
   `Inactive`), which does not match BRD-24's Open → Active → Possession → Paying Rent → Closed.
   Resolve before the contract schema is frozen.
3. **The write path.** 617 GraphQL queries against 3 mutations. `RESTful WebService Docs`
   (`/en/test/RESTful.jsp`) has not been opened.
4. **`Export Schema`** would yield the complete physical schema in one file. It is a download and
   needs explicit approval.
5. **No `Task` step exists in this tenant**, so half the workflow step model is unobserved.
   `WorkFlowTemplateStep` has 55 fields; the admin grid surfaces six.
6. **Where workflow status lives** — `Work Flow Status Code` is *not* among the 207 Firm Drop Downs.
7. **IFRS 16 is configured nowhere.** Confirm with the business whether the rebuild needs it at all.

---

_Last updated: 2026-09-10._
