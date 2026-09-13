# Page layouts — the composition engine the whole product is built on

**Stated up front.** Lucernex renders almost its entire application from a layout registry. Three
layout *modes* — **SEP** (a page), **SUB** (a reusable section), **LIST** (a grid) — compose into
every screen a user sees, and two JSP renderers serve 56% of the application from them. The most
important structural fact, and one not previously recorded in this corpus, is that
**a firm's layouts and the navigation tree are two tiers of one table**: BBW's 141 navigation nodes
and its 93 Manage Page Layouts rows share **zero** `PageLayoutID` values, and the same is true in
American Freight — yet `PageLayout.ParentPageLayoutID` is **self-referential**, so a firm layout
attaches to a platform layout by an ordinary foreign key. A firm layout does not *replace* a
navigation screen; it **hangs off** one, and several may hang off the same one. The navigation tier
is platform-seeded and identical across tenants.

Second: the layout set is **published, not authored**. AF and BBW share 80 layouts by
`(mode, name)` and **zero by id**, with zero primary-table mismatches — one ASG template set,
copied per tenant, re-keyed, and only then forked. The fork is far smaller than the headline
numbers suggest: of the 19 unshared layouts, **5 are scratch rows** (`test`, `TABLE`, `zdelete`),
**2 are renames of the same thing**, and only **3 are real functional divergence**.

| | SEP | SUB | LIST | All |
|---|---:|---:|---:|---:|
| BBW layouts | 15 | 32 | 46 | **93** |
| AF layouts | 17 | 31 | 40 | **88** |
| BBW layouts attached to a navigation node | 15 | **0** | 19 | 34 |
| BBW layouts with no parent | 0 | 32 | 27 | 59 |

Sources: [`../../tenants/bbw-page-layouts.json`](../../tenants/bbw-page-layouts.json),
[`../../tenants/af-counts.json`](../../tenants/af-counts.json),
[`../../tenants/layout-set-comparison.json`](../../tenants/layout-set-comparison.json),
[`../../mindmap/navtree-bbw.json`](../../mindmap/navtree-bbw.json). All **Observed**; joins marked
**Derived**. Build `26.09.0.113`, captured 2026-09-13.

Companion documents, which this one does not duplicate:
[`admin/008-manage-page-layouts.md`](../../admin/008-manage-page-layouts.md) (the editor, screen by
screen), [`modules/layouts-and-forms/`](../../modules/layouts-and-forms/) (conditional fields, the
Forms/Pages reconciliation, the data model),
[`data-model/screen-routing.md`](../../data-model/screen-routing.md) (the 105 routed screens),
[`../required-and-validation/`](../required-and-validation/) (where the red asterisk comes from).

---

## Two tiers of PageLayoutID, in one table

**Observed.** Every navigation node carries a `menuPLID`, called a Page Layout ID. Every row in
Manage Page Layouts carries a `PageLayoutID`. They are the same column name on what appear to be
the same table — and they never collide.

| Tenant | Nav nodes | Nav `PageLayoutID` range | Firm layouts | Layout id range | **Shared ids** |
|---|---:|---|---:|---|---:|
| `(ASG)BBW` | 141 | 924 – 108,382 | 93 | 98,858 – 102,775 | **0** |
| `(ASG)American Freight` | 109 | 924 – 51,811 | 88 | 96,206 – 110,188 | **0** |

**Derived.** 140 of BBW's 141 nav ids sit below 60,000, in bands that are byte-identical across the
two tenants (109/109 matching ids). The firm layout ids sit in a high, tenant-specific block. The
one nav node above 90,000 — `Contract : Payment Info : Invoices`, `108382` — is above BBW's highest
firm layout and does **not** appear in Manage Page Layouts, so it is platform-supplied too.

**Derived, and this is the load-bearing conclusion.** There are two tiers:

| Tier | Who owns it | Where it is listed | Identical across tenants? |
|---|---|---|:--:|
| **Platform layouts** — one per navigation node | Accruent | Not in Manage Page Layouts at all | **Yes**, 109/109 |
| **Firm layouts** — the 93/88 rows | ASG, published into the tenant | Manage Page Layouts | No — re-keyed per tenant |

A firm never edits the platform layer. It adds its own layouts and points them at platform
navigation nodes. **Any rebuild that models "one layout per screen" will not be able to represent
this**; the relationship is many firm layouts to one navigation node — see below.

---

### 93 and 135 are both small slices of a much larger population

**Observed.** Neither inventory this document works from is the whole `PageLayout` table:

| Set | Count | What it is |
|---|---:|---|
| Manage Page Layouts (`SEP`/`SUB`/`LIST` tabs) | **93** | Firm-authored layouts only |
| + form layouts reachable via Issue Types | **135** | Adds the 42 with a non-null `CodeIssueTypeID` |
| The `PageLayout` table itself | **far more** | Every platform-seeded layout as well |

**Derived, and it came from an unexpected direction.** The `Manage Discount Rates` grid is rendered
by a layout that appears in **neither** set — not in the 93 firm layouts, and not in the 134-layout
deep sweep. It is a **platform-seeded administration layout**, and the only way to address it is to
list `GET /rest/businessObject/PageLayout` and filter by name.

**Inferred.** The full population is large — an early probe of that listing returned roughly 250KB of
links. A precise count is pending and should replace this sentence when it lands.

**Derived, and it sharpens the two-tier model.** The firm tier is not one of two comparable halves;
it is a **thin layer of tenant additions on a large platform base**. Everything this document says
about composition, chains and the fork model describes that thin layer — which is the right scope,
since it is the part ASG owns and the part a rebuild must reproduce. But three consequences follow:

1. **Coverage claims must be scoped.** "All 93 layouts" means all *firm* layouts, never all layouts.
   [`../../COVERAGE.md`](../../COVERAGE.md) counts the firm set for the same reason.
2. **Administration screens are layouts too.** The reference-data grids, the code-table editors and
   the security screens are all rendered from this registry — which is why the required-field
   asterisk appears on them ([`../required-and-validation/`](../required-and-validation/)).
3. **Any sweep claiming completeness must say which population it swept.** Two of this corpus's
   corrections trace to a sweep that was complete over its own set and silently incomplete over the
   real one.

## How the three modes compose

**Observed.** Manage Page Layouts is one record type presented through three sub-tabs; the mode is
a property of the row, and the mode picks the renderer
([`screen-routing.md`](../../data-model/screen-routing.md): `PForm.jsp` for detail, `PLForm.jsp` for
list).

### SEP — a page attached to navigation

All 15 BBW SEP layouts carry a parent navigation breadcrumb. **Derived:** SEP is the only mode that
binds directly to the menu.

| PageLayoutID | Layout | Primary table | Attached to |
|---:|---|---|---|
| `98927` | ASG Contract Summary | `Contract` | Contract : Details : Summary |
| `98932` | ASG Lease Logs | `Contract` | Contract : Details : Summary |
| `98925` | ASG Contract Abstract Details | `Contract` | Contract : Abstract Info : Abstract Details |
| `98924` | ASG Common Area Maintenance | `Contract` | Contract : Abstract Info : Abstract Details |
| `98928` | ASG Delivery Requirements | `Contract` | Contract : Abstract Info : Abstract Details |
| `98930` | ASG Funds and Expenses | `Contract` | Contract : Abstract Info : Abstract Details |
| `99140` | ASG Real Estate Taxes | `Contract` | Contract : Abstract Info : Abstract Details |
| `98923` | ASG Cotenancy Language | `Contract` | Contract : Abstract Info : Co-Tenancy |
| `98926` | ASG Contract Payment Details | `Contract` | Contract : Payment Info : Payment Details |
| `98921` | ASG Breakpoint Schedule | `Percentage Rent Period` | Contract : Payment Info : Percentage Rent |
| `98934` | ASG Percent Rent Schedule | `Percentage Rent Period` | Contract : Payment Info : Percentage Rent |
| `98931` | ASG Last Deferred SL Entry | `Contract` | Contract : Accounting Info : Straight-Line Rent |
| `98929` | ASG Facility Summary | `Facility` | Facility : Details : Summary |
| `98933` | ASG Location Summary | `Location` | Location : Details : Summary |
| `98935` | ASG Portfolio Summary | `Portfolio` | Portfolio : Details : Summary |

**Derived.** The attachment is **many-to-one**: five separate SEP layouts attach to
`Contract : Abstract Info : Abstract Details`, and two to `Contract : Details : Summary` and to
`Contract : Payment Info : Percentage Rent` each. Ten of the fifteen bind `Contract`.

**Answered: they form an ordered chain.** The runtime does not *choose* between them — it renders
them in sequence. `PageLayout.PreviousPageLayoutID` is a **sequence pointer within a navigation
node**, and the `Export Configuration` screen surfaces it as a `Previous Layout` column
([`../import-export/`](../import-export/#export-configuration-is-the-publish-mechanism)). See
[the chains](#the-chain-how-several-layouts-share-one-navigation-node) below.

### The chain — how several layouts share one navigation node

**Observed.** The `Export Configuration` screen lists every layout with a **`Previous Layout`**
column (`bbw-admin/14-export-configuration.jpg`).
Its values are other layout *names*, and they are not arbitrary:

| Layout | Previous Layout |
|---|---|
| ASG Contract Abstract Details | *(none — head)* |
| ASG Common Area Maintenance | ASG Contract Abstract Details |
| ASG Delivery Requirements | ASG Common Area Maintenance |
| ASG Funds and Expenses | ASG Delivery Requirements |
| ASG Real Estate Taxes | ASG Funds and Expenses |
| ASG Contract Summary | *(none — head)* |
| ASG Lease Logs | ASG Contract Summary |
| ASG Percent Rent Schedule | ASG Contract Percent Rent |
| ASG Breakpoint Schedule | ASG Percent Rent Schedule |
| ASG Last Deferred SL Entry | ASG SL Summary |

**Derived, and it is conclusive.** Joining those pairs against the layout registry:
**8 of 8 chained pairs share the same navigation parent**, and every navigation node that carries
more than one layout resolves to **exactly one ordered chain** with a single head:

```
Contract : Abstract Info : Abstract Details
  ASG Contract Abstract Details  [SEP]
    → ASG Common Area Maintenance  [SEP]
      → ASG Delivery Requirements  [SEP]
        → ASG Funds and Expenses  [SEP]
          → ASG Real Estate Taxes  [SEP]

Contract : Details : Summary
  ASG Contract Summary  [SEP]  →  ASG Lease Logs  [SEP]

Contract : Payment Info : Percentage Rent
  ASG Contract Percent Rent  [LIST]  →  ASG Percent Rent Schedule  [SEP]  →  ASG Breakpoint Schedule  [SEP]

Contract : Accounting Info : Straight-Line Rent
  ASG SL Summary  [LIST]  →  ASG Last Deferred SL Entry  [SEP]
```

**Derived.** Three consequences.

1. **`PreviousPageLayoutID` is not a versioning pointer.** It was recorded as one in
   [`bbw-layout-engine-tables.json`](../../tenants/bbw-layout-engine-tables.json) — *"a second
   self-reference used for versioning/duplication"* — and this document repeated it. **That reading
   is wrong.** The chains link semantically distinct layouts under one navigation node, in a
   meaningful order: abstract details, then CAM, then delivery requirements, then funds and expenses,
   then real estate taxes. That is a reading sequence, not a version history.
2. **Chains cross modes.** Two heads are `LIST` layouts followed by `SEP` pages — for Percentage
   Rent, the user meets the *list* of percentage rents first, then the schedule page, then the
   breakpoint schedule. So a navigation node's content is an ordered mixture of grids and forms.
3. **Layout→screen is many-to-one and ordered.** A rebuild needs `(navigation_node, sequence)` on the
   layout, or an explicit ordered join. A set of layouts pointing at a node is not enough — the order
   carries meaning.

**Still open.** *How* the chain renders — a tab strip, stacked sections on one long page, or
next/previous navigation — has not been observed, because no end-user screen with a chained node has
been opened. The data model is settled; the presentation is not.

### How a chain renders — answered: a layout-selector dropdown

**Observed**, and this closes the remaining half of the question. The first end-user Contract screens
have now been rendered (`screenshots/bbw-enduser/ct-03-summary.jpg`,
`ct-05-abstract-details.jpg`). Every one carries, at the **top right of the content area, a
`<select>` naming the current layout** — `ASG Contract Summary` on the Summary screen,
`ASG Contract Abstract Details` on the Abstract Details screen.

**Derived.** A navigation node's chain is presented to the user as a **layout picker**. The runtime
does not silently choose one and it does not stack them: it renders the head and offers the rest as
options, in the order `PreviousPageLayoutID` defines. That is why five layouts can share
`Contract : Abstract Info : Abstract Details` without conflict — the user switches between them.

**Derived, for the rebuild.** Model a navigation node as carrying an **ordered list of layouts, one
of them the default**, and give the UI a picker. `(navigation_node, sequence)` is necessary but not
sufficient — something has to mark the head, and `PreviousPageLayoutID IS NULL` is what does it here.

### The rest of the chrome, observed

**Observed**, from the same screens:

| Element | Detail |
|---|---|
| **Group tabs** (top row) | `Details`, `Abstract Info`, `Payment Info`, `Accounting Info`, `Accrual Info`, `Reports` — the navigation **groups** |
| **Screen tabs** (second row) | The leaf screens of the active group — under `Details`: `Summary`, `Members/Contacts`, `Forms`, `Work Flow`, `Documents`, `Binders`, `Schedule` |
| **Record breadcrumb** | `Contract: 2386/Lease ID 31117 - <name> - 06/30/2034 - Open` |
| **Layout selector** | Top right, as above |
| **`Actions` panel** | A **right-hand rail**, not inline buttons |

**Derived.** The two-row tab strip *is* the navigation tree's group→leaf structure rendered as tabs.
So the 141-node tree is not a sidebar menu in practice; it is flattened into tabs once a record is
open.

### Action buttons render in a right-hand `Actions` rail, and they are per-layout

**Observed.** The `Actions` rail on **Contract Summary** carries 13 entries: `Edit`,
`Printable View`, `Add RE Contract`, **`Audit Log`**, **`Approve Payme…`**, **`Generate Rent`**,
**`Extend Contracts`**, **`Delete Payments`**, **`Alternate Rent …`**, **`Lease Abstract`**,
`Notice Address`, `Save to Docum…`, `Link`.

The rail on **Abstract Details** carries **four**: `Edit`, `Printable View`, `Save to Docum…`,
`Link`.

**Derived, and it confirms the placement model from the runtime side.** Five of Summary's entries are
exactly the placeable action-button widgets [`008`](../../admin/008-manage-page-layouts.md) found in
the layout editor — `Approve Payments`, `Generate Rent`, `Extend Contracts`, `Delete Payments`,
`Alternate Rent Wizard`. **Two layouts on the same record show different action sets**, so the
buttons are **a property of the layout, not of the entity**. A rebuild must attach actions to the
placement record, exactly as
[`../required-and-validation/`](../required-and-validation/) argues for field behaviour.

**Observed, and new.** Two rail entries were not in the editor's visible palette: **`Lease Abstract`**
— the AI lease-abstraction pipeline surfacing as a per-record action
([`../import-export/`](../import-export/)) — and **`Audit Log`**, a per-record view of the field-level
audit trail ([`../security-access/`](../security-access/)). Both are genuine capabilities this corpus
had only seen from the configuration side.

### Sub-pages render as titled sections

**Observed.** Contract Summary renders, in order: `Contract Information`, `Contract Firm
Information`, `Location Information`, `Facility Information`, `Contract Critical Dates`. Abstract
Details renders `ASG Contract Header`, `ASG Contract Critical Dates`, `ASG Contract Space
Information`, then a `Related Details` block containing `Terms` → `Contract Terms`.

**Derived.** Those section titles are **SUB layout names** — `ASG Contract Firm Information`
(`98878`), `ASG Contract Location Information` (`98880`), `ASG Contract Facility Information`
(`98877`), `ASG Contract Critical Dates` (`98876`), `ASG Contract Header` (`98879`), `ASG Contract
Space Information` (`98882`). **A sub-page renders as a titled section of its host page**, and
`ASG Contract Critical Dates` appears on *both* screens — the reuse that `SubPageLayoutID`
(include-by-reference) was inferred to allow, now observed.

**Derived.** `Related Details` is where embedded LIST layouts land — the parentless list layouts of
[the LIST section](#list--a-grid-in-two-different-jobs) render inside a host page under that heading.

### SUB — a reusable section, attached to a layout rather than to navigation

**Observed.** **0 of 32** SUB layouts carry a `ParentPageLayoutID`
([`bbw-page-layouts.json`](../../tenants/bbw-page-layouts.json), `note`). **Derived:** a sub-page is
not owned by its parent; it is *included by* a parent through a placement row
(`PageLayoutField.SubPageLayoutID` — see
[`layouts-and-forms/data-model.md`](../../modules/layouts-and-forms/data-model.md)), which makes it
reusable across many parents. That is why the parent column is empty: there is no single parent.

The 32 BBW sub-pages group cleanly by purpose:

| Group | Count | Members |
|---|---:|---|
| **Contract sections** | 12 | Accounting Schedule Details, Co Tenancy, Common Area Maintenance, Contract Critical Dates, Contract Facility Information, Contract Firm Information, Contract Header, Contract Location Information, Contract Log Header, Contract Space Information, Delivery Requirements, Funds and Expenses, Real Estate Taxes |
| **Wizard steps** | 7 | ASG Contract Wizard + Steps 2–5, ASG Facility Wizard, ASG Location Wizard |
| **Facility sections** | 4 | Facility Address, Facility Header, Facility Location Information, Facility Space Information |
| **Location sections** | 4 | Location Address, Location Area Information, Location Financial Information, Location Header |
| **Cross-entity** | 2 | ASG Documents Form Field, ASG Workflow Footer — both bind the supertype `Entity`, not a concrete table |
| **BBW-only** | 2 | ASG Hours of Operation (`Covenant`), ASG Lease Abstract - Funds and Expenses (`Contract`) |

**Derived, important.** `ASG Workflow Footer` and `ASG Documents Form Field` bind `Entity` — the
`ProjectEntity` supertype. A sub-page bound to the supertype can be placed on *any* entity's page.
That is how the universal Documents and Work Flow furniture appears on every record type without
being redefined per entity, and it confirms
[`data-model/project-entity.md`](../../data-model/project-entity.md)'s supertype reading from the
presentation side.

**Derived.** **A wizard is a chain of SUB layouts, not a distinct object type.** The five contract
wizard steps are ordinary sub-pages named `… Step 2`…`Step 5`; sequencing is by naming convention,
with no `StepNumber` or `NextPageLayoutID` observed anywhere. Field-by-field capture in
[`bbw-wizards.json`](../../tenants/bbw-wizards.json).

### LIST — a grid, in two different jobs

**Observed.** 19 of 46 LIST layouts carry a navigation parent; 27 do not.

**19 attached to navigation** — these are a user's list *screens*. Almost all are the contract's
child collections, which matches [`screen-routing.md`](../../data-model/screen-routing.md)'s finding
that nearly everything under a contract is a list:

| Attached to | Layout | Primary table |
|---|---|---|
| Contract : Abstract Info : Amendments | ASG Contract Amendments | `Contract Amendment` |
| Contract : Abstract Info : Co-Tenancy | ASG Contract Cotenants | `Co Tenancy` |
| Contract : Abstract Info : Covenants | ASG Contract Covenants | `Covenant` |
| Contract : Abstract Info : Key Dates | ASG Contract Key Dates | `Key Date` |
| Contract : Abstract Info : Responsibilities | ASG Contract Responsibilities | `Responsibility` |
| Contract : Abstract Info : Terms | ASG Contract Terms | `Contract Term` |
| Contract : Accounting Info : ASC 842 Rent Schedule | ASG ASC 842 Schedule | `Straight-Line Schedule` |
| Contract : Accounting Info : Straight-Line Rent | ASG SL Summary | `Straight-Line Schedule` |
| Contract : Payment Info : Allowances | ASG Contract Allowance | `Allowance` |
| Contract : Payment Info : Alternate Rent | ASG Contract Alternate Rent | `Alternate Rent Schedule` |
| Contract : Payment Info : Percentage Rent | ASG Contract Percent Rent | `Percentage Rent` |
| Contract : Payment Info : Receipts | ASG Contract Receipts | `Payment Receipt` |
| Contract : Payment Info : Recoveries | ASG Contract Expense Recovery | `Expense Recovery` |
| Contract : Payment Info : Recoveries | ASG Contract Expense Recovery (Net) | `Expense Recovery` |
| Contract : Payment Info : Recurring Expenses | ASG Contract Expense Setup | `Expense Setup` |
| Contract : Payment Info : Sales | ASG Contract Sales History | `Sales` |
| Contract : Payment Info : Security Deposit | ASG Contract Payment Details - Security Deposit | `Security Deposit` |
| Contract : Payment Info : Transactions | ASG Contract Payments | `Payment Transaction` |
| Administration : Dashboard : Manage Employers | ASG Employers | `Employer` |

Note `Recoveries` again carries **two** layouts — gross and net — the same many-to-one attachment
as SEP, and the clearest hint yet that the runtime offers a choice rather than picking silently.

**27 with no parent** — **Derived:** these are embedded grids, placed inside a SEP page rather than
reached from the menu. The naming makes the nesting explicit: eleven are
`ASG Contract Payment Details - <child>`, and the SEP layout `ASG Contract Payment Details`
(`98926`) is exactly where they belong. Two more — `ASG Approval - Expense Schedules`,
`ASG Approval - Transactions` — are approval grids with no navigation home, **Inferred** to be
surfaced inside a workflow step's form rather than from the menu.

**Observed.** `ASG Contract List` (`98918`), `ASG Facility List` (`98919`) and
`ASG Covenant List View` (`98906`) also have no navigation parent, despite being obvious top-level
list screens. **Open question:** what renders them?

---

## The publish-and-fork model

**Observed** ([`layout-set-comparison.json`](../../tenants/layout-set-comparison.json)): 80 layouts
shared by `(mode, name)`, 0 by id, **0 primary-table mismatches**, and both tenants carry the *same*
duplicate row — `LIST / ASG Contract Payment Details - Security Deposit`. A duplicate reproduced in
both tenants is copied, not independently authored.

**Observed.** The id offsets cluster hard: `BBW_id − AF_id` is `+2626` for 14 layouts, `+2638` for
13, `+2652` for 7, `+2653` for 7 — 58 of 80 within `+2626…+2677`. **Derived:** the set was copied in
contiguous blocks in a small number of operations, not row by row over time.

**Derived.** The 19 unshared layouts are less divergence than they look:

| Category | Count | Members |
|---|---:|---|
| **Real functional divergence (BBW ahead)** | 3 | `ASG Lease Abstract - *` family (7 rows, one feature), `ASG Contract Allowance Transaction`, `ASG Hours of Operation` |
| **Renames of the same thing** | 2 | AF `LIST ASG Contract Co Tenancy` → BBW `LIST ASG Contract Cotenants`; AF `SEP ASG Co Tenancy` → BBW `SEP ASG Cotenancy Language` |
| **Scratch / abandoned rows** | 5 | AF `LIST TABLE`, AF `LIST test`, AF `SEP test`, AF `SUB test`, BBW `LIST zdelete` |
| **AF-only feature** | 1 | `SEP ASG Client Request Log` — the custom list documented in [`006`](../../admin/006-manage-custom-lists.md) |

**Derived.** The `ASG Lease Abstract - *` family (7 layouts: Contract Term, Covenants, Expense
Schedule, Expense Setup, Key Dates, Percent Rent, and the SUB Funds and Expenses) is BBW's one
substantial advance. It aligns with the Firm entitlement flag `Allow AI Lease Abstraction`, which is
**empty** on AF ([`af-firm-record.json`](../../tenants/af-firm-record.json)). **Inferred:** these
layouts present machine-extracted lease terms for human review. Not confirmed — no Lease Abstract
screen has been opened.

**Derived.** Five scratch rows survive in a production-shaped tenant with no lifecycle to remove
them. A layout registry needs a status or archive concept; Lucernex's evidently has none, and
`zdelete` is someone's workaround for that.

### The model is specific to page layouts

**Derived.** Publish-and-fork describes **layouts and nothing else confirmed**. The same name-join
test applied to workflow templates returns **2 of 4 AF names shared with BBW's 13**, with **no
clustered id-offset block** — so workflows are tenant-authored, not published and forked
([`../workflows-forms/`](../workflows-forms/#workflows-are-tenant-authored--they-do-not-fork-from-a-published-set)).
Navigation, the 207 code-table registry and the 227 sql tables are identical across tenants, which is
a third pattern again — platform-seeded, never copied. **Three subsystems, three distribution
models**; do not generalise one to the others.

---

## What a layout contains

**Observed**, from [`008`](../../admin/008-manage-page-layouts.md) on `ASG Contract Summary`:

| Element | Detail |
|---|---|
| **Sections** | A vertical stack, each with its own reorder/delete toolbar and a 2–3 column field grid. On Contract Summary: `Contract Information, Contract Firm Information, Location Information, Facility Information, Contract Critical Dates, Space Information, Notes` |
| **Fields** | Dragged from the **Available Fields** palette, whose tree is the Manage Data Fields hierarchy for the primary table — the directly-observed link between the catalog and the layout |
| **Related fields** | Fields reached across a foreign key into a related entity ([`009`](../../admin/009-related-fields-and-data-model.md)) |
| **Sub layouts** | A palette of SUB layouts to embed |
| **List layouts** | A palette of LIST layouts to embed as child grids |
| **Action buttons** | **Placeable, reorderable business-action widgets** — `Approve Payments`, `Generate Rent`, `Extend Contracts`, `Delete Payments`, `Alternate Rent Wizard`, `Activate/Deactivate` — with the same toolbar as a field, plus empty `+` slots |
| **Budget palettes** | Budget Values, Budget Comments, Budget Fields *(out of scope)* |
| **Page controls** | Show Conditional Field Associations, Clear Layout, Remove Empty Rows, Save Layout, Close |
| **Scoping** | "Available for the following Portfolios/Capital Programs" — a required multi-select defaulting to `All` |

**Derived, and easy to miss.** A page layout is **not** a data-field surface. It also carries
business actions. `Generate Rent` and `Calculate Schedule` are buttons on a record, not batch jobs —
so **the accounting engine's trigger points are layout configuration**. A rebuild that models
layouts as field containers cannot express "this tenant's contract page can generate rent and that
one's cannot."

---

## The storage, recovered

**Previously a blind spot; now largely solved.** `PageLayout`, `PageLayoutField` and
`PageLayoutFilter` are three of the 25 tables `ShowObjectDetails.jsp` refuses with *"Data for that
table not supported"*. They are **not** hidden from the product: all 25 appear in
`GET /rest/firm/types` and are addressable as `/rest/businessObject/{type}`. Deep-serialising a
layout — `GET /rest/businessObject/PageLayout/lxid/{id}?deep=true` — returns the record with its
`PageLayoutField` children, using physical column names.

**Observed**, [`../../tenants/bbw-layout-engine-tables.json`](../../tenants/bbw-layout-engine-tables.json),
across 134 of the tenant's 135 layouts. **Caveat, stated by the capture itself:** the serializer
emits only **populated** columns, so these lists are a **lower bound** on the declared schema, not
the schema itself.

### `PageLayout` — 17 columns

| Column | Type | What it does |
|---|---|---|
| `PageLayoutName`, `Description` | string | |
| `PageLayoutType`, `OutputType` | string | Single-character discriminators (`V`, `L` observed) |
| `PrimaryCodeSQLTableID` | ref | The layout's primary table |
| **`ParentPageLayoutID`** | ref | **Self-referential** |
| **`PreviousPageLayoutID`** | ref | A second self-reference — **the sequence pointer within a navigation node**, see [the chains](#the-chain-how-several-layouts-share-one-navigation-node). *(Originally recorded as versioning/duplication; that reading is corrected there.)* |
| **`CodeIssueTypeID`** | ref | **Binds the layout to an Issue Type — this is what makes it a FORM layout.** Null on summary/sub/list layouts |
| `FirmID` | ref | The owning tenant |
| `IsGlobalReport` | boolean | Global versus firm |
| `AllowEdit`, `AllowUserCreate` | boolean | |
| `RunModeFilters`, `EntitySelectionFilter` | number | Integer bitmasks |
| `JSONConfigText` | string | Per-layout JSON blob — non-empty on **87 of 134**. Observed keys: `AssetID_LimitBy`, `AssetList_LimitBy`, `SL_LimitBy`, `NoGridWidths` |
| `@lxID`, `@clientID` | | `@clientID` is `BOMapClientRecordID`, the import key |

**Derived, and it revises this document's own headline.** `ParentPageLayoutID` is **self-referential
— a `PageLayout` pointing at another `PageLayout`.** The "Attached to" breadcrumbs in the layout list
(`Contract : Abstract Info : Abstract Details`) are therefore the *name path of another layout row*,
not a pointer into a separate navigation structure. So the earlier framing of "two disjoint
populations" is half right and half wrong:

- **Right:** the id sets are genuinely disjoint, and Manage Page Layouts lists only the firm's own.
- **Wrong:** they are not two *tables* or two *kinds of thing*. There is **one `PageLayout` table**
  holding both the platform-seeded navigation layouts and the firm's layouts, and a firm layout
  attaches to a platform one through an ordinary self-referential FK.

That is a cleaner model and a better one to copy: **one layout registry, a self-referential parent,
and tiering by `FirmID` / `IsGlobalReport` rather than by table.** The many-to-one attachment
observed earlier is unaffected — several firm layouts may share one parent.

**Derived.** `PreviousPageLayoutID` orders layouts within a navigation node — see
[the chains](#the-chain-how-several-layouts-share-one-navigation-node). It is **not** a version
lineage, so layouts have no more version tracking in the schema than workflow templates do; the
`Layout Changes` report tracks change against *platform release* versions instead.

### `PageLayoutField` — 20 columns

| Column | What it does |
|---|---|
| `PageLayoutID` | The owning layout |
| **`ReportGroupAvailableFieldID`** | FK to the data-field catalogue (RGAF). This is the `fieldKey` used by `ConditionFilterEx.jsp`; pseudo-fields (`StaticText`, `OneToManyList`) use it too |
| **`SubPageLayoutID`** | Embeds another `PageLayout` — **this is how sub-pages attach**, now Observed rather than inferred |
| `DisplayLabel` | The per-placement label override |
| `EditRowPosition`, `EditColumnPosition`, `EditFieldWidth`, `EditFieldHeight` | Geometry in **edit** context |
| `ViewRowPosition`, `ViewColumnPosition`, `ViewFieldWidth`, `ViewFieldHeight` | Geometry in **view** context |
| `HeaderColumnPosition` | Geometry in **header** context |
| **`DisplayOption1`, `DisplayOption2`** | Integer bitmasks. Observed set `0, 288, 1024, 4112, 4864, 268435456, 268435744`. On layout `98925` they track **placement kind** — `StaticText`, `SubEditForm`, `OneToManyList` — not per-field required-ness. See [`../required-and-validation/`](../required-and-validation/) |
| `JSONConfigText` | The per-field JSON blob |
| `StaticText`, `FieldContext` | Only on the field types that use them |
| `@lxID`, `@clientID` | |

**Derived.** Geometry is stored as **three parallel coordinate sets** — `Edit*`, `View*`, `Header*` —
so one placement row positions its field differently in edit, view and header contexts, with `-1`
meaning "not placed in that context". A rebuild needs three coordinate sets per placement, or an
explicit context dimension; one `(row, column)` pair cannot express this.

**Derived, and it closes a long-standing question.** There is still **no `IsRequired` and no
`IsReadOnly` column** among the 20 — confirming
[`layouts-and-forms/data-model.md`](../../modules/layouts-and-forms/data-model.md) on the column
names. The two remaining candidates are the `DisplayOption*` bitmasks and `JSONConfigText`. See
[`../required-and-validation/`](../required-and-validation/#layer-3-the-layouts-red-asterisk--observed-unexplained).

### `PageLayoutField.JSONConfigText` — the real extension point

**Observed.** 29 distinct keys across the tenant. The largest by usage:

| Key | Fields using it | What it governs |
|---|---:|---|
| `ColumnWidthInList` | 667 | List column width |
| `NumberOfDecimals` | 231 | Numeric display |
| `AutoSizeColumnWidthForInitialContent` | 163 | List layout |
| `showNameAndDescription` | 153 | Rendering |
| `ShowColumnTotal` | 146 | List aggregation |
| **`EditModeDefaultValue`** | **133** | **A per-placement default value** |
| **`FieldScript`** | **67** | **JavaScript, per field** |
| **`conditionalFieldsConfig`** | **50** | The conditional rules — see below |
| `noLink` | 45 | |
| **`FieldValidationMinValue`** | **42** | **A per-placement minimum** |
| **`FieldValidationMaxValue`** | **29** | **A per-placement maximum** |
| `DisableRowEditorInList`, `rowsPerPage`, `rowsPrintablePerPage`, `MemoColumnNumber` | 21–31 | List behaviour |
| **`IncludeInSearch`** | **9** | **Search participation** |
| `limitBy_CodeContactTypeID`, `limitBy_ExpenseTypeName`, `limitBy_CodeJobFunctionID` | 1 each | Per-placement drop-down filtering |

**Derived, and this is the significant one.** Per-placement **defaults, range validation, search
participation and a JavaScript hook** all exist — and they are all stored in a **JSON blob**, not in
columns. That is why nobody could find an `IsRequired` column: the layout engine's per-placement
behaviour lives almost entirely in `JSONConfigText`. Whether required-ness is in there too is still
open — none of the 29 observed keys is named for it, but the observed key set comes from the layouts
sampled, not from the engine's full vocabulary.

**Derived.** `FieldScript` on 67 placements is a **third** JavaScript escape hatch, alongside
`IsEnabledLxJSCode` on a step action and `Conditional Workflow JS` on a workflow
([`../workflows-forms/`](../workflows-forms/#two-mechanisms-only-bbw-shows)).

### `PageLayoutFilter` — exists, but empty

**Observed.** BBW holds **no `PageLayoutFilter` rows at all**, and the REST serializer emits only
populated columns, so its column list could not be recovered. Recorded as **blocked, not guessed**.
**Derived:** run-mode filters are configured in neither tenant.

## `Layout Changes` — the vendor's own unexplained tool, explained

**Observed** (`/en/admin/ShowLayoutChanges.jsp`,
`bbw-admin/56-layout-changes.jpg`). The vendor
feature workbook flags this tool as *"Need further explanation as to what this is"*
([`../../modules/layouts-and-forms/asg-edgeplus-mapping.md`](../../modules/layouts-and-forms/asg-edgeplus-mapping.md)).
It is a **layout change report**:

| Control | Values |
|---|---|
| *"For Layout / Layout Fields:"* | `Added Any Version` |
| *"Or:"* | `Modified Any Version` |
| *"And Modified After:"* | a date (defaulted to the current date) |
| **"For:"** | **`Firm Layouts`** (selected) or **`Global Layouts`** |
| | `Filter` button |

On-screen banner: *"Note: This functionality is currently **experimental**, removed fields not
included."* Result in BBW: **"No Records Found."**

**Derived — three things at once.**

1. **The UI itself distinguishes `Firm Layouts` from `Global Layouts`.** That is direct confirmation
   of the two-tier model derived above from `ParentPageLayoutID` and the disjoint id sets. It is not
   an inference from ids any more; the product names the two tiers.
2. **Change tracking is version-aware.** `Added Any Version` / `Modified Any Version` are version
   filters, matching `PageLayout.PreviousPageLayoutID` and the registry's `VersionAdded` /
   `VersionModified` columns ([`../data-fields/`](../data-fields/)). The platform records *when in
   its own release history* a layout or a layout field appeared or changed.
3. **This is the Hub→Spoke diff tool.** A report of "what changed in the global layouts since date
   X" is exactly what a tenant needs to decide whether to accept an upstream layout change — the
   mechanism the ASG workspace `CLAUDE.md` records as **not written down anywhere yet**, including
   its "never more than one version behind" rule. Lucernex has a first attempt at it, and labels that
   attempt *experimental*.

**Derived.** It is **experimental and incomplete by the vendor's own admission** — removed fields are
not included, so a layout diff will show additions and modifications but silently omit deletions. A
rebuild should treat this as a requirement Lucernex has not solved, not as a design to copy.

**Observed.** "No Records Found" with the date defaulted to today, which proves nothing about history.

## Conditional fields — used, and the stored shape is now known

> **Correction.** This corpus recorded, as an established fact, that there were "854 conditional
> targets across all 93 layouts, **zero populated**". That is true of the **93 page layouts** — and
> it does not generalise, because the feature is used on the **42 form layouts**, which that sweep
> never covered. A REST sweep of all **135** layouts finds **8 layouts carrying 50 conditional-field
> records and 54 criteria clauses**. The conditional engine is **in production use**.
> Source: [`../../tenants/bbw-form-layout-sweep.json`](../../tenants/bbw-form-layout-sweep.json).
>
> **There are 135 layouts, not 93.** The Manage Page Layouts screen's `SEP` / `SUB` / `LIST` tabs
> reach only 93; the other **42 are form layouts**, reachable only via Issue Types, and
> `mode=ISSUE` / `mode=FORM` **silently fall back to SEP** rather than erroring — which is why they
> were missed. **`PageLayout.CodeIssueTypeID` is what makes a layout a form layout**, and it is null
> on summary, sub and list layouts. Any sweep of "all layouts" must enumerate Issue Types separately.

**Observed.** The populated shape of `json.conditionalFieldsConfig` — the corpus's **number one open
question** — read from 33 captured values:

```json
{
  "allAny": "all",
  "showHide": "show",
  "criteriaFields": [
    { "scriptName": "Issue.LAR_RequestType",
      "crtOpt1": "17",
      "crtVal1": ["Vendor Change"],
      "isCheckBox": false }
  ]
}
```

| Element | Observed |
|---|---|
| `allAny` | `all` on **50 of 50**. Vocabulary allows `all`, `any` |
| `showHide` | `show` on **50 of 50**. Vocabulary allows `show`, `showAndRequire`, `hide` |
| `crtOpt1` | Operator code as a **string**: `2` = *in* (51 clauses), `17` = *not in* (3 clauses) |
| `crtVal1` | An **array of display strings** — `"Estoppel"`, `"New Lease"`, `"Yes"` — **not numeric code ids** |
| `scriptName` | The **driving** field's RGAF script name, e.g. `Issue.LAR_RequestType` |
| `isCheckBox` | boolean |

**Derived.** The `1` suffix on `crtOpt1` / `crtVal1` implies a second operand slot the engine
supports and this tenant never uses. **Inferred**, from naming alone.

**Derived, and it is a trap for the rebuild.** `crtVal1` stores **display labels, not ids**. Renaming
a code-table value silently breaks every conditional rule that references it, with no referential
integrity to catch it. ASG Edge+ should store ids — and if it must import Lucernex rules, it needs a
label→id resolution pass that will fail on any label that has since been renamed.

**Observed.** Where the rules actually are:

| Layout | Kind | Issue type | Conditions |
|---|---|---|---:|
| `LAR Submit Lease Admin Request` (`98946`) | FORM | Lease Admin Request | 19 |
| 5 further Issue/Form layouts | FORM | | |
| 2 LIST page layouts | LIST | — | |

Driving fields: `Issue.LAR_RequestType` drives **44 of 54** clauses; the rest are
`Issue.LAR_Estoppel*` fields and `Covenant.CodeCovenantTypeID`.

**Derived.** The feature's real job in this tenant is **one request form that changes shape by
request type** — the BRD-24 Lease Admin Request. That is a far more concrete requirement than "a
conditional field engine", and it is the one case the rebuild must actually support.

**Observed, and it matters for validation.** `showAndRequire` is in the vocabulary and used **0 of
50 times**. Conditional *visibility* is in production; conditional *required-ness* is not exercised
anywhere. See [`../required-and-validation/`](../required-and-validation/).

**Method note.** An earlier HTML sweep of `ConditionalFieldsForLayout.jsp` and a later REST sweep
**agree**: 8 layouts, 50 records. The REST route is definitive because it reads the stored JSON
rather than the rendered DOM.

## What this means for ASG Edge+

| Finding | Consequence |
|---|---|
| Nav layouts and firm layouts are two tiers of one table, joined by a self-referential `ParentPageLayoutID` | **One** layout registry with a self-referential parent, tiered by `FirmID` / `IsGlobalReport` — not two tables. The Hub/Spoke publish model in the ASG workspace `CLAUDE.md` matches this exactly |
| Many firm layouts attach to one navigation node | Layout→screen is **not** 1:1. Do not put a unique layout id on a menu row |
| SUB layouts have no parent | Sub-pages are included by reference, reusable across parents. Model `layout_placement(parent_layout_id, sub_layout_id, position)` |
| Two SUB layouts bind the `Entity` supertype | Supertype-bound sections give universal furniture (Documents, Work Flow) for free |
| A wizard is a chain of SUB layouts named by convention | Either adopt the convention deliberately or add a real `step_number` — Lucernex has none, and it shows |
| Layouts carry action buttons, not just fields | The placement record needs an element type: `FIELD \| SUBLAYOUT \| LISTLAYOUT \| ACTION` |
| 80/93 layouts are a published template set | `source_global_layout_id` + `source_version` for lineage, as [`asg-edgeplus-mapping.md`](../../modules/layouts-and-forms/asg-edgeplus-mapping.md) proposes |
| Five scratch layouts survive in both tenants | Give the registry a lifecycle: draft / published / archived |
| Conditional fields **are** in production — 8 layouts, 50 records, on **form** layouts | Not deferrable. The concrete requirement is one request form that changes shape by request type (BRD-24) |
| `crtVal1` stores display **labels**, not ids | Store ids. Any import of Lucernex rules needs a label→id resolution pass that can fail |
| Per-placement defaults, min/max validation, search participation and a JS hook live in `JSONConfigText` | The placement record needs a typed config structure, not just columns |
| Geometry is three parallel coordinate sets (Edit / View / Header) | One `(row, column)` pair per placement is not enough |
| `PreviousPageLayoutID` orders layouts within a navigation node | Model `(navigation_node, sequence)`. A layout set pointing at a node is not enough — the order carries meaning |

---

## Open questions

1. ~~**How does the runtime pick between multiple layouts on one navigation node?**~~ **Fully
   answered.** They form an ordered chain via `PreviousPageLayoutID`, and the chain renders as a
   **layout-selector dropdown** at the top right of the content area. The runtime renders the head
   and offers the rest as options. What remains is trivial by comparison: whether the dropdown lists
   the chain in `PreviousPageLayoutID` order, which needs one screenshot of the open list.
2. **What do `DisplayOption1` / `DisplayOption2` encode?** They track placement kind on the one
   layout fully examined, and every ordinary data field there is all-zero. They remain the **last
   standing** candidate for per-placement required-ness after three others were eliminated, but the
   evidence is a partial negative from a layout that may have no required fields at all. Test and
   reasoning in [`../required-and-validation/`](../required-and-validation/).
3. **Does `Layout Changes` show history if the date is widened?** It returned nothing with the date
   defaulted to today. A date set years back would show whether change history is actually retained.
4. **What is `PageLayoutField.JSONConfigText`'s full key vocabulary?** 29 keys observed, but only
   across the layouts sampled. A key governing required-ness may exist and be unused here.
5. **What are `PageLayout.PageLayoutType` and `OutputType`?** Single-character discriminators (`V`,
   `L` observed). Their relationship to the `SEP` / `SUB` / `LIST` modes is unestablished.
6. **What renders the parentless top-level lists** `ASG Contract List`, `ASG Facility List`,
   `ASG Covenant List View`?
7. **What are `PageLayoutFilter`'s columns?** BBW holds zero rows, so the serializer returns nothing.
   Needs a tenant that uses run-mode filters.
8. **Is the declared schema wider than REST returned?** The serializer emits only populated columns,
   so `PageLayout` at 17 and `PageLayoutField` at 20 are **lower bounds**.
9. **What do the `ASG Lease Abstract - *` layouts render?** Never opened.
10. **Can a SUB layout embed another SUB layout?** Structurally possible via `SubPageLayoutID`; the
   depth actually used is unknown.
11. **What is the full inventory of placeable action buttons**, and is it per entity or global?
    The `Actions` tab of `Manage Security` is the likeliest place to find it — see
    [`../security-access/`](../security-access/).
