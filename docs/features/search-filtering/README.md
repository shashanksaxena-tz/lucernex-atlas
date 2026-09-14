# Search, filtering and list behaviour

**Stated up front.** How a user *finds* a record is the largest undocumented area of the product.
`PLForm.jsp` — the list renderer — serves **37 of 105 routed screens**, and until now nothing in
this corpus described what happens on one. This document assembles what the captures already prove,
and marks clearly what still needs the running UI.

**Three separate mechanisms are now identifiable**, and they are not layers of one feature:

| Mechanism | Where it is configured | Scope | Status |
|---|---|---|---|
| **Per-placement list behaviour** | `PageLayoutField.JSONConfigText` | One field on one list layout | **Observed** — 10 relevant keys |
| **Layout-level run-mode filters** | `PageLayout.RunModeFilters` + the `PageLayoutFilter` table | A whole layout | **Structure observed, unused** — BBW holds zero `PageLayoutFilter` rows |
| **API query** | `GET /rest/businessObject/{objectType}/details` | Programmatic | **Observed** — FIQL, with paging |

**The one thing that is genuinely surprising:** search participation is configured **per field per
layout**, via an `IncludeInSearch` flag on the placement — used on only **9** placements in the whole
BBW tenant. Search is not a property of the entity or of the field; it is a property of where the
field is *placed*.

Sources: [`../../tenants/bbw-layout-engine-tables.json`](../../tenants/bbw-layout-engine-tables.json),
[`../../tenants/bbw-rest-api.json`](../../tenants/bbw-rest-api.json),
[`../../data-model/screen-routing.md`](../../data-model/screen-routing.md). BBW, build
`26.09.0.113`, 2026-09-13.

> **Status: partial.** Most of what follows is configuration-side. The **runtime** has now been seen
> in part — see [The list chrome, observed](#the-list-chrome-observed) — but the column-header filter
> menus, their per-type operators and any saved-filter feature have not. Capture requested from
> `af-tracker`.

## The list chrome, observed

**Observed**, across five administration list screens in `(ASG)BBW`
([`../reference-data/`](../reference-data/), screenshots in
`bbw-admin/`). Every list renders the
same furniture:

| Element | Detail |
|---|---|
| **A typed filter row above the grid** | Per-screen, matching that entity's columns: date pickers, drop-downs defaulting to `All types` or `<Any>`, free-text boxes. On Manage Discount Rates: `Effective Date`, `Length (In Months)`, `Country`, `State / Province`, `Portfolio`, `Accounting Method`, `Use Type` |
| **A separate `Search:` box** | Top-right, placeholder *"Type to search"*. **Distinct from the filter row** — so a list has *two* narrowing mechanisms, structured filters and free text |
| **Paging** | First / previous / page number / next / last, plus a **refresh** control |
| **Row count** | *"Displaying 1 - 15 of 3683"* or *"No items to display"* |
| **`Rows per page`** | A runtime control — so `rowsPerPage` in `JSONConfigText` is a **default**, not a fixed setting |
| **`Add <Thing>…`** | Bottom-right of the grid |
| **Required markers** | Red text with a trailing `*` **on column headers** |

**Derived.** The two-mechanism design — structured filter row plus free-text search — is worth
copying deliberately. It also sharpens the `IncludeInSearch` question below: the free-text box is the
likeliest consumer of that flag, which would make it *per-list search*, not a global index.

**Derived.** The filter row is **typed per column** — a date column gets a date picker, a code-table
column gets a drop-down of its values. That is generated from the layout, not hand-built per screen.

![`Manage Discount Rates`, chosen because it is empty -- which leaves the chrome itself visible with nothing to distract from it. Every element in the table above is here: the seven-control typed filter row, the separate `Search: Type to search` box at the right, first/previous/next/last paging with a refresh, `No items to display`, a `Rows per Page` control, `Add Discount Rate...`, and four asterisked column headers.](../../assets/screenshots/bbw-admin/25-manage-discount-rates.jpg)


---

## Per-placement list behaviour

**Observed.** Of the 29 `JSONConfigText` keys found across the tenant, ten govern list and search
behaviour:

| Key | Placements | What it governs |
|---|---:|---|
| `ColumnWidthInList` | **667** | Column width in a list |
| `AutoSizeColumnWidthForInitialContent` | 163 | Auto-size from first page of content |
| `ShowColumnTotal` | **146** | A column total row |
| `DisableRowEditorInList` | 27 | Whether the row is inline-editable |
| `rowsPerPage` | **26** | **Page size, per layout** |
| `rowsPrintablePerPage` | 21 | Page size when printing |
| **`IncludeInSearch`** | **9** | **Whether this placement participates in search** |
| `NoGridWidths` | 9 | Suppress stored widths |
| `CLGridWidth` | 2 | Custom-list grid width |
| `ShowActiveInactive` | 3 | Show inactive rows |

**Derived.** Paging is **layout configuration**, not a user preference: `rowsPerPage` is stored on
the placement. A rebuild that puts page size in user settings will not reproduce this, and a tenant
that has tuned a 500-row list to 25 rows per page will notice.

**Derived.** `ShowColumnTotal` on 146 placements means **aggregation is a list feature**, configured
per column. Lists are not just grids of rows.

**Derived.** `DisableRowEditorInList` implies the default is **inline row editing in a list** — a
significant UX commitment, and it is switched off on only 27 placements. Combined with
[`../page-layouts/`](../page-layouts/), where nearly every screen under a contract is a list, this
means most data entry in Lucernex happens **in a grid**, not on a form.

### `IncludeInSearch` is the whole search story so far

**Observed.** 9 placements in the entire tenant carry it.

**Derived.** Search is opt-in, per field, **per placement** — not per entity, not per field
definition. Two readings, and they have very different rebuild consequences:

| Reading | Implication |
|---|---|
| It marks fields included in a **global/quick search index** | 9 fields tenant-wide is a plausible size for a quick-search index |
| It marks fields offered in a **per-list search box** | 9 would be a very thin configuration across 46 list layouts |

Neither is confirmed. There is also a related field, **`Issue.SearchField (Text)`** on the `Issue`
object — a denormalised search column — which suggests at least some search is served by
precomputed text rather than by querying columns. **Inferred.**

**Observed, and it narrows the two readings to one.** The `List Layout` tab of the layout editor
renders each column as a placement chip, and one of them is annotated in green:

![The `List Layout` tab on `ASG Contract Payments`, table `PaymentTransaction`. Thirteen column placements run left to right. Eight are red and asterisked -- `Effective Date *`, `Effective End Date (Coverage End Date) *`, `Expense Group *`, `Expense Type *`, `Invoice Amount *`, `Primary Tax (Tax Amount #1) *`, `Due Date *`, `Vendor *` -- and five are plain. The last chip is green and reads `(Searchable, Hidden in grid)`: a placement that exists to be searched on and is not displayed.](../../assets/screenshots/page-layouts/page-layouts-contract-payments-list-layout.png)

**Derived.** `(Searchable, Hidden in grid)` is `IncludeInSearch` rendered, and the two words it pairs
settle the reading: **searchable** and **hidden in grid** are properties of *this column on this
list*. It is a **per-list search box** configuration, not a global index — the editor has no concept
of a tenant-wide index to add a field to. That also explains why 9 is a plausible number: it is nine
deliberate additions across 46 list layouts, not an index that someone forgot to populate.

**Derived, and it is a placement capability the corpus had not named.** A field can be **on a layout
and not on the screen**. The placement record therefore needs a visibility flag independent of
position, and `-1` geometry ("not placed in that context") is not the same thing as hidden-but-live.

**Still Inferred:** whether the per-list box queries the columns directly or reads a denormalised
column like `Issue.SearchField`. The editor does not say.


---

## Layout-level filters: built, unused

**Observed.** `PageLayout` carries two integer bitmasks, **`RunModeFilters`** and
**`EntitySelectionFilter`**, and there is a dedicated `PageLayoutFilter` table whose FK to
`ReportGroupAvailableField` is **required**
([`../../modules/layouts-and-forms/data-model.md`](../../modules/layouts-and-forms/data-model.md)).

**Observed.** **BBW holds zero `PageLayoutFilter` rows.** Because the REST serializer emits only
populated columns, the table's column list could not be recovered at all — recorded as blocked, not
guessed.

**Derived.** Run-mode filtering — a saved, layout-level filter applied whenever the list renders — is
**configured in neither tenant**, exactly like conditional fields were thought to be. Unlike
conditional fields, this one really does appear unused: the sweep that found 50 populated conditional
records found no filter rows at all.

> **This paragraph previously offered `RunModeFilters` as the leading explanation for how the runtime
> picks between five layouts on one navigation node. That question has since been answered, and the
> answer is not this.** The runtime does not pick: it renders the chain head and offers the rest in a
> **layout-selector dropdown** at the top right of the content area, ordered by
> `PreviousPageLayoutID`
> ([`../page-layouts/`](../page-layouts/#how-a-chain-renders--answered-a-layout-selector-dropdown)).
> `RunModeFilters` and `EntitySelectionFilter` remain unexplained, and are now unexplained *without*
> a hypothesis attached to them.

---

## The API query surface

**Observed.** One generic endpoint serves querying for all 227 record types:

```
GET /rest/businessObject/{objectType}/details
```

| Parameter | Required | Meaning |
|---|:--:|---|
| `fiql` | no | **Record filter, in FIQL** |
| `fields` | **yes** | Comma-separated field names |
| `$skip` | no | Records to skip |
| `$top` | no | Limit on records returned |

**Observed.** The endpoint returns **413** when too many records match.

**Derived.** Three points worth carrying into a rebuild.

1. **`fields` is mandatory.** There is no "give me everything" mode — a caller must name the columns.
   On a 570-column `Contract` that is a sensible default, and it is a discipline worth copying.
2. **Filtering is a real query language** (FIQL — Feed Item Query Language, `==`, `!=`, `=gt=`,
   `and`, `or`), not a fixed set of parameters. The list UI may or may not be built on it.
3. **413 rather than truncation** means the server refuses an over-broad query instead of silently
   returning a prefix. Also worth copying — silent truncation is how wrong reports get written.

**Observed.** `GET /rest/firm/types` classifies record types with four flags — `wantBase`,
`wantCodeTables`, `wantIssues`, **`wantClientLists`**. **Derived:** the four record-set categories
are Base, Code Tables, Issues and **Client Lists** — so custom lists are a first-class REST category,
not an implementation detail ([`../custom-lists/`](../custom-lists/)). The corpus previously recorded
three categories; there are four.

---

## Related field-level filtering

**Observed.** Three `JSONConfigText` keys appear once each: `limitBy_CodeContactTypeID`,
`limitBy_ExpenseTypeName`, `limitBy_CodeJobFunctionID`. `PageLayout.JSONConfigText` carries the
same idea at layout level: `AssetID_LimitBy`, `AssetList_LimitBy`, `SL_LimitBy`.

**Derived.** A drop-down's **options** can be narrowed per placement — a `Contact` picker on one
layout can offer only contacts of a given type. That is *option* filtering, distinct from *row*
filtering, and distinct again from conditional visibility. It is used sparingly: three placements.

---

## What this means for ASG Edge+

| Finding | Consequence |
|---|---|
| `rowsPerPage` is layout configuration | Page size belongs to the layout, not to user preferences |
| `ShowColumnTotal` on 146 placements | Lists need per-column aggregation |
| Inline row editing is the default | Most data entry happens in a grid. Design lists as editable, not read-only |
| `IncludeInSearch` is per placement | Search participation is a placement property. Decide whether to copy that or move it to the field |
| `Issue.SearchField` is a denormalised text column | Expect a precomputed search column, not only live queries |
| Run-mode filters are built and unused | Safe to defer; the structure tells you the shape when you need it |
| The API filter language is FIQL with mandatory `fields` and a 413 ceiling | Adopt mandatory field selection and refuse over-broad queries |
| Four record-set categories, including Client Lists | Custom lists are first-class in the API |

---

## Open questions

All of these need the running UI. **Requested from `af-tracker`** on a well-populated list screen.

1. **What operators does a column-header filter offer, per type?** Text, date, number, drop-down and
   boolean columns presumably differ. Nothing is known.
2. **Can a filter be saved or named, and where does it live?** No `SavedFilter` object exists in the
   223-object census, which argues against a saved-filter feature — but `PageLayoutFilter` exists and
   is empty, which might *be* it.
3. **Is filter state server-side?** The URL/query-string shape when a filter is applied would settle
   it.
4. **Can a user add columns at runtime**, or only the administrator via the LIST layout?
5. **What does the quick-search box search across** — one entity, or the whole tenant? Now half
   answered: the layout editor labels an `IncludeInSearch` placement `(Searchable, Hidden in grid)`,
   which is per-list language and rules out a tenant-wide index
   ([above](#includeinsearch-is-the-whole-search-story-so-far)). What remains is whether it queries
   the columns or reads a denormalised column like `Issue.SearchField`.
6. **Sort: single or multi-column?** And is the sort stored on the layout?
7. **Is there a per-list export button**, and what formats? `rowsPrintablePerPage` implies a print
   path at least.
8. **Does the list UI use FIQL underneath**, or a separate internal query path?
9. **What do `RunModeFilters` and `EntitySelectionFilter` encode?** Two integer bitmasks. See
   [`../page-layouts/`](../page-layouts/#open-questions).
