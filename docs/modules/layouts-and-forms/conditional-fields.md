# Conditional field filtering — the mechanism, fully resolved

**Stated up front.** Lucernex's conditional field filtering is a small, well-bounded rule engine
attached to a page layout. One rule set reads:

> **[Show | Show and Require | Hide]** this field when **[all | any]** of the following rules match

…followed by a grid of candidate **driver fields**, each of which may be given one operator and one
value. The rule set is stored as JSON on the layout, evaluated against the record being rendered,
and applies to the **edit layout only — never the list layout**. Driver fields are not limited to
the layout's own table: they reach across foreign keys into related entities.

This document supersedes the "not yet explored / blocked" status in
[008](../../admin/008-manage-page-layouts.md#show-conditional-field-associations). The blocker is
resolved and explained in [How the blocker was cleared](#how-the-blocker-was-cleared).

| Property | Value |
|---|---|
| Editor route | `/en/pagebuilder/ConditionFilterEx.jsp` |
| Opened by | `conditionOptions(fieldKey, hashCode, isFormLayout, isLabelField, pageLayoutID)` |
| Rendered into | `optionsEditDiv` on the layout builder page — an in-page Ext dialog, **not** a popup window |
| Driver-field data source | `/servlet/BOList?…&BOType=ConditionFilterList` |
| Persisted as | hidden form field `json.conditionalFieldsConfig` on form `ConditionFilter` |
| Saved by | `saveConditionalChanges()` → `Lx.ui.saveConditionalFilter()` → `postAJAXForm(...)` |
| Captured | 2026-09-10, tenant `(ASG)American Freight`, build `26.08.0.46` |
| Evidence layout | `ASG Contract Summary`, `PageLayoutID=96289`, primary table `Contract` |
| Exploration mode | Read-only. The dialog was opened and inspected; **Save was never clicked**, and no rule was created, edited or deleted. |

![The Conditional Filter dialog, open on the ASG Contract Header sub-page of the ASG Contract Summary layout](../../assets/screenshots/conditional-fields/conditional-filter-editor-contract-header.jpg)

## The rule model

### The target — what a rule controls

**Observed.** The target is identified by a `fieldKey`. Two kinds were found on this one layout:

| `fieldKey` shape | Target | Example |
|---|---|---|
| `txt_<hash>` | A single placed field or label | `txt_1960392586` |
| `subPage_<PageLayoutID>` | **An entire sub-page section** | `subPage_96253` (= `ASG Contract Header`) |

The second is the important one and was not previously known: **a conditional rule can show or hide
a whole composed section**, not just an individual field. Since
[008](../../admin/008-manage-page-layouts.md) established that Summary Pages are composed from
independently-managed Sub-page fragments, this means whole page regions appear and disappear by rule.

**Derived.** The `ASG Contract Summary` layout carries **20** conditional-capable targets.

### The action — three values, not two

**Observed**, from the `showHide` select:

| Action | Effect |
|---|---|
| `Show` | Target is displayed when the rules match |
| `Show and Require` | Target is displayed **and becomes mandatory** when the rules match |
| `Hide` | Target is hidden when the rules match |

`Show and Require` is the one to note. **Visibility and required-ness are governed by the same rule
in a single declaration** — there is no separate "conditional required" feature. Any
reimplementation that models visibility and validation as independent concerns will need two rules
where Lucernex needs one, and will drift.

### The quantifier

**Observed**, from the `allAny` select: `all` (conjunction) or `any` (disjunction). One level only —
there is no nesting, no parentheses, no mixed AND/OR within a single rule set.

**Derived:** the rule language is deliberately flat. A rule set is
`ACTION WHEN (all|any) OF [ predicate, predicate, … ]`. This is a significant simplification and
worth preserving in the rebuild; arbitrary boolean trees are far more expensive to build, to
validate, and to explain to an administrator.

### The predicates — operators are type-dependent

Each row in the grid is one candidate driver field, with one operator dropdown. **Observed** — three
distinct operator sets exist, selected by the driver field's type:

| Driver `Field Type` | Operators |
|---|---|
| **Dropdown** | `is any value`, `is in`, `is not in`, `is specified`, `is not specified` |
| **Number** | `is any value`, `=`, `<>`, `>`, `>=`, `<`, `<=`, `is specified`, `is not specified` |
| **Boolean** | `is any value`, `selected`, `not selected` |

`is any value` is the neutral/no-op state — a driver row with `is any value` contributes no
predicate. That is how an 85-row grid represents a rule set containing two rules: 83 rows sit at
`is any value` and are ignored.

Note that **Dropdown uses set membership (`is in` / `is not in`), not equality**. A single predicate
can therefore match several coded values at once, which removes most of the need for `any`
quantification in practice.

`is specified` / `is not specified` are null tests, available on every type.

## The driver-field catalog — rules cross entity boundaries

This is the most architecturally significant finding.

**Observed / Derived.** For `PageLayoutID=96289` (primary table `Contract`), the driver grid offers
**85** candidate fields, drawn from **four different tables**:

| Table | Drivers | How it is reached |
|---|---:|---|
| `Contract` | 65 | The layout's own primary table |
| `ProjectEntity` | 9 | The universal entity spine (a declared GraphQL interface — see [`graphql-api.md`](../../data-model/graphql-api.md)) |
| `Facility` | 7 | Via `Contract.FacilityID`, type `Facility ID` |
| `Location` | 4 | Via `Contract.LocationID`, type `Location ID` |
| **Total** | **85** | |

The related-table drivers correspond exactly to the many-to-one FK columns that
[009](../../admin/009-related-fields-and-data-model.md) established on `Contract`. **A field on a
Contract form can therefore be shown or hidden based on a value held on its Facility or Location
record.** The conditional engine and the Related Fields palette walk the same FK graph.

By driver type:

| Type | Count |
|---|---:|
| Dropdown | 78 |
| Number | 5 |
| Boolean | 2 |

**Derived, and worth dwelling on:** there are **no Date and no Text drivers** in this set, although
`Contract` has many of both. Conditional logic keys off *enumerable or comparable* values only.
Free text is never a driver. This is a deliberate constraint that keeps rules explicable and
indexable, and the rebuild should adopt it rather than allowing conditions on arbitrary strings.

### Driver scope switch — `All` / `UDF` / `Global`

**Observed.** A three-way radio labelled **Filter Options** with values `All`, `UDF`, `Global`
scopes which fields appear in the driver grid — mirroring the Global-versus-Firm duality that runs
through Manage Data Fields ([005](../../admin/005-manage-data-fields.md)) and Page Layouts
([008](../../admin/008-manage-page-layouts.md)). `UDF` restricts the list to tenant-authored
user-defined fields; `Global` to platform-defined ones; `All` shows both.

A **Conditions Applied** checkbox filters the grid down to rows that already carry a rule, and a
search box filters by name. Both are conveniences over the same 85-row set.

## Scope of evaluation — edit layout only

**Observed.** The `Show Conditional Field Associations` dialog is headed, verbatim:

> Conditions affect the edit layout and NOT the list layout

**Observed** from the `conditionOptions` source: when `layoutMode` is `"list"` or `"budget"` the
editor is opened with an extra `showInList=1` parameter — so list-mode layouts have a *different*
conditional surface rather than sharing the edit layout's.

**Derived.** Edit-layout rules and list-layout rules are configured and stored separately for the
same `PageLayoutID`, consistent with 008's finding that a single layout record can carry both an
Edit Layout and a List Layout with independent configuration.

## Storage format

**Observed.** The dialog's form (`ConditionFilter`) carries these fields:

| Field | Value on the captured target |
|---|---|
| `fieldKey` | `subPage_96253` |
| `pageLayoutID` | `96289` |
| `formFieldType` | `0` |
| `json.conditionalFieldsConfig` | *(empty — this target has no rules)* |
| `formSubmit` | `true` |

The `json.` prefix is a serialisation convention: **the entire rule set for one target is persisted
as a single JSON document**, not as normalised rows. The save path is
`Lx.ui.saveConditionalFilter()` (which serialises the grid state into that hidden field) followed by
`postAJAXForm(...)`.

**Inferred, and flagged as unconfirmed:** the JSON is presumed to hold the action, the `all`/`any`
quantifier, and an array of `{driverField, operator, value}` triples. The captured target had no
rules, so **the populated shape has not been observed.** Resolving this is the top open question
below.

Corroborating evidence for the JSON-blob reading: **no type matching `condition`, `rule`, `criteria`,
`visib`, `depend`, `trigger`, `expression` or `predicate` exists anywhere in the 490-type GraphQL
schema** (see [`graphql-api.md`](../../data-model/graphql-api.md)). Conditional rules are layout
configuration, invisible to the data API — consistent with being stored as an opaque JSON column on
the page-layout record rather than as first-class entities.

## How the blocker was cleared

[006](../../admin/006-manage-custom-lists.md), [008](../../admin/008-manage-page-layouts.md) and
[009](../../admin/009-related-fields-and-data-model.md) all record the same blocker: the layout
builder was reached by navigating directly to `LayoutEditorAJAX.jsp`, and field-level editors could
not be triggered.

The diagnosis in those documents — a popup/window-opener dependency — was **wrong**, and the
correction is useful for future exploration. `conditionOptions` does not open a window at all; it
renders an Ext dialog into a `div` on the *current* page. What actually blocked it was that the
dialog's JSP depends on the host page's `Lx` JavaScript namespace. Loading
`ConditionFilterEx.jsp` directly yields a bare, non-functional form (second screenshot below);
the same URL rendered into the layout builder works completely.

The working method, for reuse on the other blocked editors (`editOptions` on Custom List fields, and
placed related-field properties):

1. Navigate to `LayoutEditorAJAX.jsp?...&PageLayoutID={id}`.
2. Harvest real arguments from the DOM — every conditional target appears as an inline
   `conditionOptions('<fieldKey>','<hashCode>',…)` call.
3. Invoke the page's own function with those arguments.

![ConditionFilterEx.jsp loaded standalone — renders the sentence but no grid, because the host page's Lx namespace is absent](../../assets/screenshots/conditional-fields/conditional-filter-standalone-no-host.jpg)

## Rules for the ASG Edge+ rule engine

Stated so a rule engine can consume them. Confidence: **Observed** unless marked.

| ID | Rule |
|---|---|
| `LAY-R-010` | A conditional rule set attaches to exactly one target, identified by a stable key. A target is either a single field or an entire sub-page section. |
| `LAY-R-011` | A rule set declares exactly one action: `SHOW`, `SHOW_AND_REQUIRE`, or `HIDE`. |
| `LAY-R-012` | A rule set declares exactly one quantifier over its predicates: `ALL` or `ANY`. Nesting is not supported. |
| `LAY-R-013` | A predicate is a triple `(driverField, operator, value)`. Operators are constrained by the driver field's type: Dropdown → `IN`, `NOT_IN`, `IS_SPECIFIED`, `IS_NOT_SPECIFIED`; Number → `EQ`, `NEQ`, `GT`, `GTE`, `LT`, `LTE`, `IS_SPECIFIED`, `IS_NOT_SPECIFIED`; Boolean → `SELECTED`, `NOT_SELECTED`. |
| `LAY-R-014` | `is any value` is the neutral state and contributes no predicate. |
| `LAY-R-015` | Candidate driver fields are: the layout's primary table, plus every table reachable by a many-to-one FK from it, plus `ProjectEntity`. |
| `LAY-R-016` | Only Dropdown, Number and Boolean fields may be drivers. Text and Date fields may not. |
| `LAY-R-017` | Rule sets apply to the edit layout. List layouts carry a separate, independent rule surface. |
| `LAY-R-018` | `SHOW_AND_REQUIRE` makes the target mandatory for validation purposes only while its predicates match. *(Inferred — the runtime behaviour was not observed, only the configuration option.)* |

### Design notes for the rebuild

- **Model the action as one enum, not two booleans.** The `Show and Require` case shows that
  visibility and required-ness are one decision in the administrator's mental model.
- **Keep the flat `all`/`any` structure.** It is the reason the UI is a single grid rather than a
  tree editor, and it is very likely why administrators actually use the feature.
- **The driver set is derivable, not configured.** Given a primary table, ASG Edge+ can compute the
  legal driver list from its own FK metadata exactly as Lucernex does — no separate registry needed.
- **Decide storage deliberately.** Lucernex persists a JSON blob per target. That is cheap to write
  and impossible to query ("which layouts depend on `codeContractStatusID`?"). Given ASG Edge+
  already has an unresolved Where-Used problem (`D-07`, which forced `DeactivationPolicy` to default
  to `WARN_AND_BLOCK`), storing predicates as queryable rows instead would let a future Where-Used
  answer "this dropdown value drives 14 layout rules" — something Lucernex cannot answer about
  itself.
- **Evaluation timing is unresolved.** See open questions.

## Open questions

Ranked by how much they block the rebuild.

1. **What is the populated JSON shape of `json.conditionalFieldsConfig`?** The captured target had
   no rules. Find a layout that already has conditional rules applied — use the **Conditions
   Applied** checkbox across layouts, or the `Show Conditional Field Associations` dialog, which
   lists `Field / Rule / Criteria` for any layout that has them — and read the hidden field. Until
   this is done, the storage format is inferred, not known.
2. **Is evaluation server-side at render, or client-side on change?** This determines whether a rule
   can depend on a value the user has just typed but not yet saved. Decisive for UX and for where
   the rule engine lives. Testable by opening an end-user Contract page with a rule applied and
   watching for a network round-trip when the driver field changes.
3. **What does `Show and Require` do at runtime** when the target is a sub-page rather than a single
   field — does it require every field in the section, or only those already marked required?
4. **How does the list-layout conditional surface (`showInList=1`) differ**, given the dialog's own
   heading says conditions do not affect list layouts?
5. **Are Date drivers genuinely unsupported, or absent only from this layout?** The layout builder
   defines `hideShowDateFieldsForCriteria` and `hideShowNumberCriteriaFields`, which implies
   date-specific criteria inputs exist somewhere. Check a layout whose primary table is
   date-heavy.
6. **What is `formFieldType`, observed as `0`?** Likely a discriminator distinguishing field targets
   from sub-page targets.
