# 005 — Manage Data Fields

## Identification

| Property | Value |
|---|---|
| Administration label | Manage Data Fields |
| Browser/page title | Manage Report Group Available Fields |
| Tenant | `(ASG)American Freight` |
| Base route | `https://train-americanfreight.lucernex.com/en/pagebuilder/ReportGroupAvailableFieldEdit.jsp` |
| Explicit Global route | `https://train-americanfreight.lucernex.com/en/pagebuilder/ReportGroupAvailableFieldEdit.jsp?isGlobal=true` |
| Explicit Firm route | `https://train-americanfreight.lucernex.com/en/pagebuilder/ReportGroupAvailableFieldEdit.jsp?isGlobal=false` |
| Captured | 2026-09-02 local session date; page footer showed 2026-09-01 Central Standard Time |
| Application build | `26.08.0.39 (2026/08/21 21:28)` |
| Exploration mode | Read-only inspection |

The Administration label and internal title use different terminology. **Manage Data Fields** opens a page called **Manage Report Group Available Fields**. The internal title directly identifies the page as an “available fields” catalog associated with report groups. It may also feed forms or page layouts, but that broader use has not yet been demonstrated.

## Screenshots

### Global Fields

![Manage Data Fields — Global Fields](../assets/screenshots/data-fields/manage-data-fields-global.png)

### Firm Fields

![Manage Data Fields — Firm Fields](../assets/screenshots/data-fields/manage-data-fields-firm.png)

The Global screenshot was recaptured after explicit navigation to `?isGlobal=true`. An earlier image bearing the Global filename had shown the default Firm state and was replaced. The images linked above are the corrected captures.

## Raw and derived evidence

| Artifact | Description |
|---|---|
| [`data-fields-global-landing.snapshot.txt`](../assets/raw-captures/data-fields-global-landing.snapshot.txt) | Accessibility tree from the explicit Global route. |
| [`data-fields-firm-current.snapshot.txt`](../assets/raw-captures/data-fields-firm-current.snapshot.txt) | Accessibility tree from the explicit Firm route. |
| [`data-fields-global-dom-rows.json`](../assets/raw-captures/data-fields-global-dom-rows.json) | Full Global table DOM capture, including shell rows. |
| [`data-fields-global-tree-rows.json`](../assets/data-fields-global-tree-rows.json) | Normalized Global `pmid` hierarchy rows. |
| [`data-fields-firm-tree-rows.json`](../assets/data-fields-firm-tree-rows.json) | Normalized Firm `pmid` hierarchy rows. |
| [`data-fields-global-row-summary.txt`](../assets/raw-captures/data-fields-global-row-summary.txt) | Compact sample of Global rows and handlers. |
| [`data-fields-global-budget-column-row.json`](../assets/raw-captures/data-fields-global-budget-column-row.json) | Focused Global hierarchy example. |
| [`data-fields-comparison-input-summary.json`](../assets/raw-captures/data-fields-comparison-input-summary.json) | Structural/action summary for both scopes. |
| [`data-fields-comparison-metrics.json`](../assets/raw-captures/data-fields-comparison-metrics.json) | Validated deterministic comparison metrics. |
| [`data-fields-global-vs-firm-comparison.md`](../assets/data-fields-global-vs-firm-comparison.md) | Detailed Global-versus-Firm method and findings. |

Credentials, cookies, session identifiers, and authorization values are intentionally excluded.

## Entry path

1. Sign in to the authorized Lucernex training tenant.
2. Open the **Administration** toolbar destination.
3. In **Company Administration**, follow **Manage Data Fields**.
4. Use the explicit **Global Fields** and **Firm Fields** links to establish the active scope unambiguously.

Only navigation, page rendering, accessibility capture, DOM inspection, Ext JS inspection, network review, console review, and local documentation were performed.

## Scope behavior and correction history

### Observed default

The unparameterized base route resolved to the **Firm Fields** state. This was proven by three independent observations:

- The Firm Fields control was active in the rendered page.
- Export behavior contained `isGlobal=false`.
- Import behavior contained `isGlobal=false`.

The initial unparameterized accessibility artifact, [`data-fields-landing.snapshot.txt`](../assets/raw-captures/data-fields-landing.snapshot.txt), must therefore be treated as **Firm/default-route evidence**, despite its earlier ambiguous name.

### Explicit scope links

- **Global Fields** navigates to `?isGlobal=true`.
- **Firm Fields** navigates to `?isGlobal=false`.

These are server-routed links, not merely a client-side filter applied to one already-loaded row set.

## Visible page layout

### Global shell

The page retains the Lucernex application shell:

- Top Menu region.
- Search box and Advanced Search control.
- Global toolbar controls rendered by Ext JS.
- Tenant heading `(ASG)American Freight`.
- Main Panel region.
- Printable View link.
- Collapsed left navigation rail showing `>>`.
- Footer with Accruent copyright, privacy link, authenticated display name, tenant, server time, time zone, and build.

### Main content

The content is a large hierarchical table. The initial visual state shows 24 collapsed top-level groups. Child subgroups and fields are already present in the DOM with `display:none`; expanding is therefore primarily a visibility operation over a pre-rendered hierarchy.

The page is implemented as a legacy table/tree interface rather than a modern paginated data grid. Alternating row classes include `rowColor1` and `rowHighLite`; the header uses `tblHeader`. Expand/collapse icons are loaded from `/RolloutManager/img/`.

## Firm-only instruction block

The Firm Fields capture visibly displays these instructions:

> Please read these instructions first before making any changes.
>
> Use add/edit/delete links to change an individual Field or Group
>
> For bulk changes export these fields into a spreadsheet and make changes to it and import that spreadsheet.
>
> Before making changes to spreadsheet please read the instruction at the top.
>
> Once a spreadsheet is imported the same spreadsheet cannot be used again. You would have to create a new spreadsheet using "Export Data Fields" button.

The corrected Global screenshot and Global accessibility evidence did not visibly show this warning block. The reason for the scope difference is not known.

The one-use spreadsheet statement is operationally important: an exported spreadsheet appears to contain versioned, nonce-like, or otherwise one-time import context. That mechanism is an interpretation; no spreadsheet was exported or imported to test it.

## Scope and tree controls

| Control | Observed behavior/evidence | Activated? |
|---|---|---|
| Global Fields | Navigates to `?isGlobal=true`. | Yes, navigation only. |
| Firm Fields | Navigates to `?isGlobal=false`. | Yes, navigation only. |
| `<Expand All>` | `javascript:ToggleAll(1,arry1)` | No. |
| Numeric count/hide control | `javascript:hideEmptyRows(1,arry1)`; shows 6,297 Global or 549 Firm. | No. |
| Plus icon | Description: `Show Sub Items`; reveals child rows. | No. |
| Printable View | Page-local printable link. | No. |

The 6,297 and 549 values are complete hierarchy-row totals, not leaf-field totals.

## Named columns

The hierarchy table exposes ten named data columns and an unnamed action column:

1. **Group Name/Field Label**
2. **Field Name**
3. **Form Field Type**
4. **Reqd?**
5. **Read Only?**
6. **Table Association**
7. **Default Value**
8. **Valid For Portfolio or Capital Program?**
9. **Valid For Entity?**
10. **Valid For Issue?**
11. Unnamed per-row action cell

### Meaning supported by labels

- **Group Name/Field Label** carries all three hierarchy levels: group, subgroup, and field display label.
- **Field Name** is the internal field identifier for leaf records.
- **Form Field Type** identifies a Lucernex field/widget or value type.
- **Reqd?** and **Read Only?** are field-behavior flags.
- **Table Association** links the metadata entry to a business-object table/entity name.
- **Default Value** stores an optional field default.
- The three **Valid For...** columns describe applicability at structural levels; their leaf cells were empty in the captured examples.
- The unnamed final cell contains edit/delete/add/script actions according to scope and row type.

The exact runtime semantics of these columns in forms, reports, and layouts require downstream observation.

## Top-level group inventory

The same 24 top-level groups and applicability values were captured in both scopes:

| Top-level group | Portfolio / Capital Program | Entity | Issue |
|---|:---:|:---:|:---:|
| Budget | Yes | Yes | Yes |
| Company Items | No | No | No |
| Complex | Yes | Yes | Yes |
| Contract | No | Yes | Yes |
| Demographics Criteria | Yes | Yes | No |
| Documents | No | No | No |
| Equipment/Assets | No | Yes | Yes |
| Facility | Yes | Yes | Yes |
| Location | No | Yes | Yes |
| Milestones | Yes | Yes | Yes |
| Parcel | Yes | Yes | Yes |
| Pro Forma Lease | Yes | Yes | Yes |
| Program Summary Information | Yes | No | Yes |
| Prototype | Yes | Yes | Yes |
| Purchase Management | Yes | Yes | Yes |
| RE Planner | Yes | No | No |
| RE Transaction | Yes | Yes | Yes |
| Schedule | Yes | Yes | Yes |
| Site Survey | Yes | Yes | Yes |
| Specialized Forms | No | No | Yes |
| Statics | No | No | No |
| Summary Information | Yes | Yes | Yes |
| Wizard | No | Yes | No |
| Workflow | No | No | No |

## Hierarchy model

DOM inspection established exactly three levels:

| Indentation | Expandable | Row type |
|---:|---|---|
| 0 units | Yes | Top-level group |
| 4 units | Yes | Subgroup |
| 8 units | No | Leaf field |

### Validated counts

| Metric | Global | Firm |
|---|---:|---:|
| Top-level groups | 24 | 24 |
| Subgroups | 320 | 320 |
| Leaf fields | 5,953 | 205 |
| **Total hierarchy rows** | **6,297** | **549** |
| Maximum indentation | 8 | 8 |
| Levels observed | 3 | 3 |
| Duplicate reconstructed leaf paths | 0 | 0 |

For both captures, the declared JSON count equals the actual row-array length. Row ordinals are unique. Global spans `pmid2` through `pmid6298`; Firm spans `pmid2` through `pmid550`.

## Global-versus-Firm comparison

### Shared taxonomy, separate leaf sets

Deterministic reconstruction found:

- All 24 top-level paths are shared.
- All 320 subgroup paths are shared.
- Captured metadata does not differ on the matched top-level groups or subgroups.
- No exact reconstructed leaf path is shared.
- No composite identity of path + internal name + table association is shared.
- No conservative same-path candidate override was found.

| Comparison level | Shared | Global-only | Firm-only |
|---|---:|---:|---:|
| Top-level paths | 24 | 0 | 0 |
| Subgroup paths | 320 | 0 | 0 |
| Leaf paths | 0 | 5,953 | 205 |

This is strong evidence that both scopes use a common classification scaffold while exposing disjoint field-definition sets.

It does **not** prove how the application merges, inherits, or selects these fields downstream. A Firm field might represent the same business concept using a different path, label, internal name, or table association.

### Naming pattern

- Global leaf internal names beginning with `Firm_`: **0 of 5,953**.
- Firm leaf internal names beginning with `Firm_`: **202 of 205** (approximately 98.5%).

This is strong evidence of a tenant-specific namespace but is not an absolute rule because three Firm records do not follow the prefix pattern.

### Required and read-only metadata

| Value | Global | Firm |
|---|---:|---:|
| Required = Yes | 637 | 0 |
| Required = No | 5,316 | 205 |
| Read Only = Yes | 0 | 0 |
| Read Only = No | 5,953 | 205 |

### Default values

- Global: 5,953 empty defaults.
- Firm: 203 empty defaults and 2 values equal to `TBD`.

### Dominant field types

Global’s most frequent captured types are:

- `sTYPE_TEXT` — 961
- `sTYPE_MONEY` — 891
- `sTYPE_DATE` — 365
- `sTYPE_NUMBER` — 336
- `sTYPE_UNFORMATTED_NUMBER` — 279
- `sTYPE_MEMBER` — 261
- `sTYPE_MONEY_MATH_OPERATION` — 258
- `sTYPE_TIME` — 232
- `sTYPE_BOOLEAN` — 229
- `sTYPE_PERCENTAGE` — 179
- `sTYPE_TEXTAREA` — 158
- `sTYPE_CHECKBOX` — 153

Firm’s most frequent captured types are:

- `sTYPE_TEXT` — 83
- `sTYPE_CUSTOM_CODE_FIELD` — 54
- `sTYPE_DATE` — 12
- `sTYPE_NUMBER` — 12
- `sTYPE_PERCENTAGE` — 9
- `sTYPE_TEXTAREA` — 8
- `sTYPE_MONEY` — 8
- `sTYPE_CLIENT_LISTS` — 6
- `sTYPE_MONEY_MATH_OPERATION` — 4
- `sTYPE_FIRM_LOGO` — 3

The presence of `sTYPE_CUSTOM_CODE_FIELD` and `sTYPE_CLIENT_LISTS` makes Manage Custom Lists and the dropdown-management screens direct follow-up targets.

### Dominant table associations

Global’s largest associations include:

- `ExpenseRecovery` — 558
- `Contract` — 255
- `LeaseInfo` — 218
- `ProjectEntity` — 165
- `SLSummary` — 135
- `Asset` — 126
- `PaymentTransaction` — 118
- `ExpenseSetup` — 103

Firm’s largest associations are:

- `Contract` — 147
- `KeyDate` — 10
- `ExpenseRecovery` — 9
- `Covenant` — 7
- `Employer` — 5
- `Location` — 5
- `ProjectEntity` — 5
- `Allowance` — 4

`Contract` accounts for 147 of 205 Firm leaves, approximately 71.7%.

## Representative Global hierarchy

| Level | Label | Internal name | Type | Required | Read only | Table |
|---|---|---|---|:---:|:---:|---|
| Group | Budget | — | — | — | — | — |
| Subgroup | Budget Column | — | — | — | — | — |
| Leaf | Allow UI Edit? | `AllowUIEdit` | `sTYPE_BOOLEAN` | No | No | `BudgetColumn` |

Other captured fields under **Budget / Budget Column** include:

- Bid Package — `BidPackageID` — `sTYPE_BID_PACKAGE`
- Budget Column ClientID — `BOMapClientRecordID` — `sTYPE_TEXT`
- Budget Column Name — `BudgetColumnName` — `sTYPE_TEXT`
- Budget Column RecID — `BudgetColumnID` — `sTYPE_UNFORMATTED_NUMBER`
- Budget Column Status — `CodeBudgetColumnStatusID` — `sCODE_BUDGET_COLUMN_STATUS`
- Budget Column Type — `BudgetColumnTypeID` — `sTYPE_BUDGET_COLUMN_TYPE`
- Budget Template — `BudgetTemplateID` — `sTYPE_BUDGET_TEMPLATE`
- Created By Member — `CreatedByMemberID` — `sTYPE_MEMBER`
- Created Date — `CreatedDate` — `sTYPE_TIME`
- Description — `Description` — `sTYPE_TEXTAREA`
- Initialized From Budget Column — `InitializedFromBudgetColumnID` — `sTYPE_BUDGET_COLUMN`

## Representative Firm fields

| Reconstructed path | Internal name | Field type | Table association |
|---|---|---|---|
| Company Items / Employers / Alternate Payee | `Firm_AlternatePayee` | `sTYPE_TEXT` | `Employer` |
| Company Items / Employers / Payment Method | `Firm_PaymentMethod` | `sTYPE_CUSTOM_CODE_FIELD` | `Employer` |
| Contract / Allowance / Cost PSF | `Firm_AllowCostPSF` | `sTYPE_MONEY_MATH_OPERATION` | `Allowance` |
| Contract / Common Area Maintenance / Administrative Fee | `Firm_CAMAdministrativeYN` | `sTYPE_CUSTOM_CODE_FIELD` | `Contract` |
| Contract / Common Area Maintenance / Administrative Fee Percent | `Firm_CAMAdministrativeFeePercent` | `sTYPE_PERCENTAGE` | `Contract` |

All five examples were captured as Required = No and Read Only = No.

## Per-row actions

### Global action signatures

| Rows | Actions |
|---:|---|
| 5,953 leaf rows | `edit details`, `Value Javascript` |
| 344 group/subgroup rows | None |

Because `edit details` is exposed for every Global leaf to this account, Global metadata is not described here as technically immutable. It was only treated as read-only for this exploration.

Representative handler evidence:

```javascript
popupFormEdit(4,28963,'ReportGroupAvailableField','ReportGroupAvailableFieldID')
```

```javascript
Lx.Popup.createScriptRGAFWindow(28963,'Allow UI Edit?')
```

### Firm action signatures

| Rows | Actions |
|---:|---|
| 205 leaf rows | `edit`, `delete`, `Value Javascript` |
| 313 subgroup rows | `Add Field` |
| 7 subgroup rows | `edit`, `delete`, `Add Field` |
| 24 top-level group rows | None |

The seven Firm-defined/editable subgroup paths are:

1. Contract / Common Area Maintenance
2. Contract / Custom Lists
3. Contract / Delivery Requirements
4. Contract / Ongoing Co Tenancy
5. Contract / Opening Co Tenancy
6. Contract / Real Estate Taxes
7. Contract / Test

Representative Add Field pattern:

```javascript
popupFormAdd('ReportGroupAvailableField', 'ReportGroupDataID',1029,549)
```

No row action was activated.

## Page-level controls and handlers

| Control | Global behavior | Firm behavior | Activated? |
|---|---|---|---|
| Add Group | `popupFormAdd('ReportGroupData')` | Same visible control | No |
| Export Data Fields | Document download with `isGlobal=true` | Document download with `isGlobal=false` | No |
| Import Data Fields | Import popup with `isGlobal=true` | Import popup with `isGlobal=false` | No |

Global export:

```javascript
download('/servlet/DocumentDownload?type=RGAFSpreadsheet&readOnly=true&isGlobal=true',100,100,true,'DownloadSpreadsheet')
```

Firm export:

```javascript
download('/servlet/DocumentDownload?type=RGAFSpreadsheet&readOnly=true&isGlobal=false',100,100,true,'DownloadSpreadsheet')
```

Global import target:

```text
/en/pagebuilder/ImportReportGroupAvailableField.jsp?isGlobal=true
```

Firm import target:

```text
/en/pagebuilder/ImportReportGroupAvailableField.jsp?isGlobal=false
```

The export URL includes `readOnly=true`; this is direct handler evidence but does not by itself define the permissions or contents of the generated workbook.

## Observed behavior

- The page distinguishes Global and Firm through an `isGlobal` query parameter.
- The base route defaults to Firm for this account/session.
- The collapsed tree is fully pre-rendered in the DOM.
- Both scopes render the same 24 groups and 320 subgroups.
- Firm displays only 205 leaf fields inside that scaffold; Global displays 5,953.
- Scope-specific import/export handlers preserve the active `isGlobal` value.
- Firm rows expose add/edit/delete capabilities more explicitly than Global rows.
- Every captured leaf in both scopes exposes **Value Javascript**, indicating field-level scripted-value capability.
- No expand, hide-empty, edit, delete, add, JavaScript editor, export, import, or printable action was used.

## Network evidence

The explicit Firm capture included:

- `GET /en/pagebuilder/ReportGroupAvailableFieldEdit.jsp?isGlobal=false` — `200`.
- Ext JS, Ext Gantt, Lucernex CSS/JavaScript, OpenLayers, and RolloutManager assets — `200`.
- `GET /servlet/uihelper?reqType=getLayoutNames...` — `200`.
- `GET /servlet/JSONDataRequest?...&reqType=RMTopMenu&node=root` — `200`.
- Cloudflare RUM telemetry POST — `204`.
- A cross-origin tenant header image request to `americanfreight.lucernex.com` was blocked by ORB.
- Pendo assets loaded successfully.

The request list reinforces the legacy JSP/servlet architecture combined with Ext JS and shared Lucernex client code.

No export, import, save, delete, or script-update request was generated.

## Browser console state

The filtered Firm console state contained:

- One deprecated-feature issue.
- One cross-origin response-blocking issue in the CORB/ORB family.
- No uncaught JavaScript exception in the warning/error/issue listing.

This is not a completely clean console, but no page-breaking exception was observed.

## Tenant and permission implications

### Direct observations

- The tenant heading remains `(ASG)American Freight`.
- The account can see both Global and Firm catalogs.
- The account is presented with Global `edit details` links.
- The account is presented with Firm add/edit/delete controls.
- Import and export controls exist for both scopes.

### Implications requiring caution

- Visibility of a control does not prove the operation would pass server-side authorization.
- The ability to view both scopes does not define whether “Global” means all Lucernex tenants, the current deployment, or all contexts within this tenant.
- Field-level Value JavaScript can potentially affect calculations, defaults, visibility, or other behavior; its execution contract has not been inspected.
- Firm deletion could affect existing data, reports, forms, workflows, integrations, and layouts that reference an internal field name.
- The one-use spreadsheet warning implies that bulk changes may be guarded by generated import context, but the exact mechanism is unknown.

## Mutation-risk register

| Control/action | Potential effect | Exploration decision |
|---|---|---|
| Add Group | Creates hierarchy metadata. | Not activated. |
| Add Field | Creates a field definition. | Not activated. |
| edit / edit details | Opens or changes metadata. | Not activated. |
| delete | Removes group or field definitions and may orphan references. | Not activated. |
| Value Javascript | Opens or changes executable field logic. | Not activated. |
| Import Data Fields | Bulk mutation from spreadsheet. | Not activated. |
| Export Data Fields | Generates/downloads tenant metadata. | Not activated. |
| Printable View | Changes presentation only, but unnecessary for capture. | Not activated. |
| Expand All / Show Sub Items / hide-empty control | Likely local visibility changes. | Not activated; DOM inspection made them unnecessary. |

No Lucernex field, group, hierarchy, JavaScript value, spreadsheet, or tenant configuration was modified.

## Interpretation

### High-confidence conclusions

1. **Manage Data Fields is a metadata catalog.** The screen exposes labels, internal field names, types, behavioral flags, table associations, defaults, applicability, and script/edit actions.
2. **The page has two explicit scopes.** Global and Firm are represented by distinct `isGlobal` values and scope-aware bulk handlers.
3. **The scopes share a business taxonomy.** All 24 group paths and all 320 subgroup paths match in this capture.
4. **The captured leaf namespaces are disjoint.** None of 5,953 Global paths matches any of 205 Firm paths using the documented method.
5. **Firm fields are tenant-manageable extensions.** Their naming and add/edit/delete patterns strongly support this conclusion.
6. **Contract customization dominates this tenant.** 147 of 205 Firm leaves are associated with `Contract`.

### Moderate-confidence architectural model

The most evidence-consistent model is:

- Global Fields define built-in Lucernex/platform field metadata.
- Firm Fields define tenant-specific additions.
- A common taxonomy provides placement and applicability context.
- Other builders or runtime screens likely compose both catalogs.

This is intentionally phrased as a model rather than a proven internal implementation. The page capture does not reveal downstream joins, inheritance rules, cache behavior, versioning, or referential-integrity enforcement.

### Terminology caution

“Report Group Available Fields” suggests reporting/business-object availability. The presence of **Form Field Type**, **Valid For Entity**, Value JavaScript, and Page Layout administration nearby suggests wider reuse is possible. Until a report builder, form, and page-layout editor are traced to these definitions, the documentation should not claim that this page governs all application fields.

## Confidence and unresolved questions

### High confidence

- URLs, title, visible controls, columns, instruction text, tenant/build context, and top-level applicability are directly captured.
- Hierarchy counts and row classification are validated from complete normalized DOM exports.
- Global-versus-Firm structural and leaf-path comparisons are deterministic and reproducible from local evidence.
- Action signatures and representative JavaScript handlers are directly present in the DOM captures.

### Requires further exploration

1. Does this catalog feed reporting only, or also entity forms, page layouts, workflows, imports, and APIs?
2. Where and how are Global and Firm fields combined?
3. Can a Firm field override a Global field through an identifier not exposed in the captured columns?
4. Can Firm configuration alter a Global field’s label, type, required/read-only flags, default, association, applicability, or Value JavaScript?
5. Why is the full 320-subgroup scaffold rendered in Firm scope when only 205 Firm leaves exist?
6. Are the shared groups/subgroups copied records, inherited records, or views over one common taxonomy?
7. Which three Firm fields do not use the `Firm_` prefix, and why?
8. Which two Firm fields have the `TBD` default, and how is that default applied?
9. ~~How do `sTYPE_CUSTOM_CODE_FIELD` and `sTYPE_CLIENT_LISTS` connect to Manage Custom Lists, Firm Drop Downs, and Client Drop Downs?~~ **Partially answered** — see Addendum below.
10. ~~Which Data Fields are selectable in Manage Page Layouts?~~ **Answered** — see Addendum below.
11. Are changes versioned or audited, and does **Layout Changes** include Data Fields?
12. Which permissions govern Global edit details, Firm add/edit/delete, import/export, and Value JavaScript separately?
13. Does “Global” mean platform-wide across tenants, deployment-wide, or globally usable within the current tenant?
14. Why does Firm show the bulk-change warning while Global does not?
15. Why did the captured Firm `displayedCount` selector return an empty string even though 549 was visibly rendered?

## Addendum (2026-09-10) — links confirmed via Custom Lists and Page Layouts exploration

Two open questions above are now partly resolved by later exploration; full detail lives in the
linked documents rather than repeated here.

- **Data Fields ⇄ Page Layouts (question 10, answered).** The **Manage Page Layouts** builder’s
  **Available Fields** sidebar is this same catalog, scoped to one Primary Table: expanding it for
  the `Contract` table reproduced the exact subgroup names documented above (`Contract Dates`,
  `Contract Info`, `Contract Term`, `Common Area Maintenance`, `Delivery Requirements`, etc.), plus
  a `Custom Lists` subgroup. See
  [008 — Manage Page Layouts § Available Fields sidebar](008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists).
- **`sTYPE_CUSTOM_CODE_FIELD` / `sTYPE_CLIENT_LISTS` (question 9, partly answered).** This
  catalog’s own field types were not re-tested directly, but the *sibling* per-custom-list field
  editor (a separate catalog from this one — see [006](006-manage-custom-lists.md)) exposes an
  equivalent mechanism: a field’s Form Field Type can be set to **”Drop Down >>”**, cascading into
  a **Drop Down Types** category picker whose six values plausibly partition **Firm Drop
  Downs**/**Client Drop Downs** ([007](007-firm-and-client-drop-downs.md)) for field-binding
  purposes. Whether the *Global/Firm Data Fields* catalog documented in this file exposes the same
  cascade for its own `sTYPE_CUSTOM_CODE_FIELD` / `sTYPE_CLIENT_LISTS` types was not directly
  re-verified — flagged as still open.
