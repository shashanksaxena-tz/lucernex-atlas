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
| **What are the workflows?** | **Corrected.** `(ASG)American Freight` has 4 workflows and 4 form types, which looked 1:1; `(ASG)BBW` has **13 workflows, 62 steps and 6 form types**, and only 4 of 13 names match — **Form↔Workflow is not 1:1**. Two form types have no workflow at all. Versioning is by name suffix (`… v1`, `… v2`). Lease Admin Request's 8 steps *are* BRD-24. Routing resolves in practice to lists of named individuals, not positions. | [`features/workflows-forms/`](features/workflows-forms/), [`modules/workflow/`](modules/workflow/) |
| **How does ASC 842 work?** | One engine, three standards, selected by flags on `SLSummary`. Classification is a separate 93-field record. Schedules are **approved, not published**. | [`modules/accounting/`](modules/accounting/) |

---

## Coverage — what is documented and what is not

[**`COVERAGE.md`**](COVERAGE.md) is the scoreboard: **744 known surfaces** — 141 navigation nodes,
57 administration tools, 93 page layouts, 227 sql tables, 207 firm drop-downs, 13 workflow
templates and 6 form types — each with its route, whether a document explains it, and whether a
screenshot exists. It is **generated** from the raw captures by
[`tools/build_coverage.py`](tools/build_coverage.py); edit
[`tools/coverage-owners.json`](tools/coverage-owners.json) and re-run rather than hand-editing the
table. Read it before assuming an area is covered.

It also surfaces the structural gaps: **31 sql tables absent from the 223-object census**, **25
tables the schema viewer refuses** (including the whole `Page Layout` family), and **49 of 57 admin
tools with no owning document**.

## Feature areas

[`features/`](features/README.md) documents the product as a **manual** — feature by feature, screen
by screen — complementing [`modules/`](modules/) (domain concepts) and
[`data-model/`](data-model/) (schema).

| Area | What it settles |
|---|---|
| [**required-and-validation**](features/required-and-validation/) | **At least three, probably four, independent sources of required-ness**, and they are **not** one flag surfaced several times: the column's `Required?` and the catalog's `Required` disagree on 44 fields **in both directions** — 42 owner foreign keys the application demands but the database permits to be null, and 2 audit columns the reverse — so they are *NOT NULL at storage* versus *the user must supply this*, two obligations that mostly coincide. Collapsing them loses 44 obligations. The red asterisk is a third source whose storage is **unresolved** with one candidate left under test; `Show and Require` is a fourth that is **used zero times**. `Contract` has 307 columns and requires 7, none of them a business fact. *(The agreement percentage is withheld — the sweep behind it captured global fields only.)* |
| [**page-layouts**](features/page-layouts/) | One `PageLayout` table in **two tiers**, joined by a self-referential `ParentPageLayoutID` — nav ids and firm layout ids are disjoint but not separate things. **Several layouts on one navigation node form an ordered chain** via `PreviousPageLayoutID`, and the chain renders as a **layout-selector dropdown** — the runtime shows the head and offers the rest, which is why five layouts can share one node. Chains cross modes (a LIST head followed by SEP pages). From the first rendered end-user screens: **SUB layouts render as titled sections** and are reused across pages, and **action buttons render in a right-hand rail and are per-layout** (13 on Summary, 4 on Abstract Details, same record). SEP/SUB/LIST composition, the publish-and-fork model, the recovered 17+20-column engine schema, per-placement behaviour in `JSONConfigText`, and layouts as hosts for **business-action buttons** |
| [**equipment-contracts**](features/equipment-contracts/) | BBW's fifth root with all 32 node ids. `Contract` minus the retail layers, the ASC 842 engine kept whole. **No `EquipmentContract` table exists** in the 223-object census, the 227-table picker, or the 25 refused tables |
| [**workflows-forms**](features/workflows-forms/) | **Corrects the 1:1 Form↔Workflow claim.** Workflow versioning by name suffix; workflows chain; two separate JavaScript escape hatches |
| [**data-fields**](features/data-fields/) | **205 `Firm`-scope custom fields and not one of them is a physical column** — 147 are CAM clauses on `Contract`, making ASG's customisation of Lucernex almost entirely a CAM abstraction. Field *definitions* are rows in `ReportGroupAvailableField` (`IsGlobal` + `FirmID` + `IsClientExtensionField`); where the *values* are stored is unidentified. Also reconciles the three inventories — census 223, picker 227, catalog 214 — **none complete, union 254** |
| [**security-access**](features/security-access/) | Security is granted to a **user class** over four kinds of thing — navigation/layout **pages**, **70 action verbs**, **6,553 individual fields**, and budget columns — on a `NoAccess` / `View` / `Edit` / `Delete` / `Default` ladder. **Read-only turns out to be `View` on a field**, and the field catalog's uniform `ReadOnly = No` is *not* an error: definition-level and per-class grant measure different things. It also **refutes** this corpus's three-gate explanation of why `Equipment Contract` fails to render at American Freight — entitlement, menu structure and page access are **all open** there (granted for 8 of 10 classes), and `Program` is granted by all 10 and also does not render, so **a fourth mechanism exists and is unidentified**. Also documents the **audit trail** — a synchronous, in-transaction, field-level table with old/new values, bearing on ASG's open **ADR-0020** vs **ADR-0012** decision |
| [**reference-data**](features/reference-data/) | Discount rates, CPI, exchange rates, fiscal and holiday calendars. **Four of the five tables are empty in BBW** — most consequentially the **discount-rate table, while the tenant runs ASC 842, IFRS 16 and straight-line**, so the rate must reach the engine by a per-record override. CPI holds **3,683 rows of one BLS series** (1932–2019). The discount-rate lookup is keyed by **seven dimensions** including a lease-length band and the accounting method. The fiscal calendar supports **4-4-5** and **13-period** retail years and **extrapolates** beyond the last defined year — so a fiscal period is not a calendar month. The holiday calendar turns out to feed **project scheduling, not accounting** |
| [**administration**](features/administration/) | **All 57 administration tools, classified with routes** — the complete inventory, which did not previously exist. A quarter of the admin surface is the configuration engine. Settles from the routes that Firm Drop Downs (`FirmCodeList.jsp`) and Client Drop Downs (`CustomCodeTableEdit.jsp`) are **two distinct registries**, that Import and Export are one "Messenger" subsystem, and that `Job Log` and `Report Log` are one screen. Names the **five undocumented financial reference-data tools** — discount rates, CPI data, exchange rates, fiscal and holiday calendars — that feed the accounting engine |
| [**import-export**](features/import-export/) | **Three publish tiers and four inbound data paths.** Accruent ships **versioned configuration packages** (`Version`, **`Min Version`**, `Released`) via `Import Best Practice Templates` — the closest prior art anywhere for the Hub→Spoke "never more than one version behind" rule; **`Export Configuration` is the firm-to-firm publish mechanism** — it exports layouts/forms/reports as XML with a `Clone` checkbox whose two modes ("new layouts created when this xml is imported" versus "moving from one firm to another") **are exactly the publish-and-fork model** derived from id arithmetic elsewhere. Generic bulk import is an XML form post (`POST /rest/firm`, `synchronous` required, UI defaults to stop-on-first-error, no dry-run) and **creates parent records implicitly** — importing a Facility creates its Location. **`BOMapClientRecordID` is confirmed as the upsert key** — `/clientid/{id}` addresses records by it and `POST …?allowUpdate=true` upserts — which is why it is required on 133 of 202 tables. `/atlas-api` + `/adapter-config` + `/vendor-lease` are a **live AI lease-abstraction pipeline** tying together the `Allow AI Lease Abstraction` flag, BBW's 7 Lease Abstract layouts and the `AI Abstracted` status value. And `Job Log`'s **818 entries** are the first evidence of the product *running*: a real XLSX import, an **hourly inbound HTTP integration**, and `Generate Payments` logged as a user-triggered job |
| [**search-filtering**](features/search-filtering/) | Search participation is configured **per field per placement** (`IncludeInSearch`, 9 placements tenant-wide), paging is layout configuration (`rowsPerPage`), inline row editing is the default, and layout-level run-mode filters are **built and unused**. The API query surface is **FIQL** with mandatory `fields` and a 413 ceiling |
| [**custom-lists**](features/custom-lists/) | A Custom List is a tenant-authored **mini record type** with its own field namespace, layout and parent binding — and it is **a Form without the workflow**: `CodeIssueType.IsWorkFlow` is the only difference, so Manage Forms and Manage Custom Lists are two views over one code table. Form attachability is **11 `IsValidFor…` boolean columns**, one of them `IsValidForEquipContract` |
| [**drop-downs-code-tables**](features/drop-downs-code-tables/) | The value census behind the 207-table registry: **73 populated, 134 empty, 1,140 values**, three tables holding 56% of them. `delete` is gated by a server-supplied **`isReadOnlyRecord`**, not a reference count — so Lucernex is **no precedent for Where-Used**, and D-07 / MST-015 stand. The flag **moved between builds**, which corrects two claims in [`data-model/code-table-registry.md`](data-model/code-table-registry.md) |

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
| [**`data-model/api/`**](data-model/api/README.md) | **The full REST API explained** — the complete OpenAPI 3.0.1 spec verbatim (132KB), a machine-readable operation index, and a written account of how the API works: one generic CRUD controller for all 227 types, dual identifier space, the `ImportResults` trap, the AI pipeline, and what to copy vs fix |
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

## A second tenant

[`tenants/bbw-vs-american-freight.md`](tenants/bbw-vs-american-freight.md) — the `(ASG)BBW` training
tenant (build `26.09.0.113`) read against `(ASG)American Freight` (`26.08.0.46`). The four end-user
navigation roots are **identical name-for-name**; BBW adds a fifth, **`Equipment Contract`** — a
parallel lease aggregate that keeps the entire ASC 842 / IFRS 16 / straight-line engine and drops
every retail-real-estate layer (co-tenancy, recoveries/CAM, percentage rent, sales, the whole Accrual
Info group). It also carries **13 workflow templates / 62 steps** against American Freight's 4 — including the
document- and financial-abstraction workflows, and **BRD-24's eight `Lease Admin Request` steps,
observed for the first time**. Not one of those 62 steps is a `Task` step.

| Data | Holds |
|---|---|
| [`mindmap/navtree-bbw.json`](mindmap/navtree-bbw.json) | BBW navigation, 141 nodes. Route columns need re-capture |
| [`tenants/bbw-conditional-sweep.json`](tenants/bbw-conditional-sweep.json) | **854** conditional targets across **all 93** layouts — **zero populated** |
| [`tenants/bbw-workflow-steps.json`](tenants/bbw-workflow-steps.json) | 13 templates, 62 steps. Approver identities deliberately omitted |
| [`tenants/bbw-page-layouts.json`](tenants/bbw-page-layouts.json) | All **93** page layouts across `SEP`/`SUB`/`LIST`, with primary table and navigation |
| [`tenants/bbw-drop-downs.json`](tenants/bbw-drop-downs.json) | All **207** Firm Drop Downs with their `TableType` ids (2000-3016) |
| [`tenants/bbw-wizards.json`](tenants/bbw-wizards.json) | The **5-step contract creation wizard**, field by field, plus Facility and Location wizards |
| [`tenants/bbw-platform-inventory.json`](tenants/bbw-platform-inventory.json) | **227** sql tables, **57** admin tools, **6** form types |
| [`tenants/bbw-platform-tables.json`](tenants/bbw-platform-tables.json) | Field detail for **202** of 227 tables, **6,487** fields — **caveat: global layer only** (`showGlobal=true`); firm fields absent, re-run queued. 25 platform-internal tables (incl. the `Page Layout` trio) are **refused** by the viewer |
| [`tenants/layout-set-comparison.json`](tenants/layout-set-comparison.json) | AF↔BBW layout join: **0 shared ids but 80 shared names** — one ASG template set, copied per tenant and forked |
| [`tenants/af-*.json`](tenants/) | American Freight on the **same build**: Firm record, all 207 code tables' row actions, navigation, platform tables, comparison counts |

**Four corrections to this corpus** come out of it — including a **retraction** (§3): the
reference-count reading of code-table `delete` protection was wrong, and must not be used to reopen
**D-07** / **MST-015**. It, all recorded in that document: the single-tenant
reading of code-table `delete` protection is insufficient; a sweep method that reads
`LayoutEditorAJAX.jsp` over HTTP yields **false negatives** because conditional targets are injected
client-side; and workflow routing, documented as "by organisational position, not by name", resolves
in practice to lists of **named individuals**. It also surfaces two undocumented mechanisms —
workflows **chain** (one kicks off another), and a `Conditional Workflow JS` field holds
workflow-level rules as **JavaScript**, separate from `conditionalFieldsConfig`.

---

## What is still open

Ranked by how much each blocks the rebuild.

1. ~~**The populated shape of `json.conditionalFieldsConfig`.**~~ **ANSWERED, 2026-09-13.** The
   "854 targets, zero populated" reading held only for the **93 page layouts**; the feature is used
   on the **42 form layouts**. A REST sweep of all **135** finds **8 layouts, 50 conditional-field
   records, 54 criteria clauses**, and the stored shape is now Observed:
   `{allAny, showHide, criteriaFields:[{scriptName, crtOpt1, crtVal1[], isCheckBox}]}`, with operator
   codes `2` = *in* and `17` = *not in*, and **`crtVal1` holding display labels, not ids**. All 50
   use `show`; `showAndRequire` is used **0** times. See
   [`features/page-layouts/`](features/page-layouts/) and
   [`tenants/bbw-form-layout-sweep.json`](tenants/bbw-form-layout-sweep.json).
2. **Contract lifecycle.** The platform's `Contract Status Code` has only three values
   (`AI Abstracted`, `Active`, `Inactive`), which does not match BRD-24's Open → Active →
   Possession → Paying Rent → Closed. **A strong lead has appeared:** BBW carries **38 firm-defined
   drop-downs** in `Client Drop Downs`, and one of them is **`Lease Status`** — exactly what a tenant
   would create to track a lifecycle the platform field cannot express. **The first rendered Contract
   screens show both fields on one record — `Contract Status = Active` and `Lease Status = Open` —
   and the record's own breadcrumb header ends with the `Lease Status`, not the contract status.**
   `Open` is BRD-24's first state and is not among the platform field's three values. Reading the
   full `Lease Status` value list is one click, and is requested. Note also that `Facility Status Code` *does* carry `Open`, `Closed` and
   `Possession`, so the BRD-24 vocabulary exists in the product on the **facility**. Resolve before
   the contract schema is frozen. See [`features/drop-downs-code-tables/`](features/drop-downs-code-tables/).
3. ~~**The write path.**~~ **ANSWERED, 2026-09-13.** `/en/test/RESTful.jsp` was opened. The REST
   surface is **fully CRUD — 160 operations over 141 paths: 104 GET, 40 POST, 7 PUT, 9 DELETE.** The
   617-queries-against-3-mutations picture describes GraphQL only and does not describe the product's
   write path. See [`tenants/bbw-rest-api.json`](tenants/bbw-rest-api.json). *(No token or credential
   was captured; the page renders live Basic and JWT tokens and the capture was structure-only.)*
   REST is also how the 25 tables the schema viewer refuses were recovered — see
   [`tenants/bbw-layout-engine-tables.json`](tenants/bbw-layout-engine-tables.json).
4. **`Export Schema`** would yield the complete physical schema in one file. It is a download and
   needs explicit approval.
5. **No `Task` step exists in either tenant**, so half the workflow step model is unobserved.
   `WorkFlowTemplateStep` has 55 fields; the admin grid surfaces six. **0 of 19** AF steps and
   **0 of 62** BBW steps are `Task` steps — see [`features/workflows-forms/`](features/workflows-forms/).
6. **Where workflow status lives** — `Work Flow Status Code` is *not* among the 207 Firm Drop Downs.
7. **IFRS 16 is configured nowhere.** Confirm with the business whether the rebuild needs it at all.

---

_Last updated: 2026-09-13._
