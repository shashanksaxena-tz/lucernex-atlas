# Global versus Firm Data Fields comparison

## Purpose

This report compares the two read-only catalogs exposed by **Manage Data Fields** in the American Freight Lucernex training tenant:

- **Global Fields** — `ReportGroupAvailableFieldEdit.jsp?isGlobal=true`
- **Firm Fields** — `ReportGroupAvailableFieldEdit.jsp?isGlobal=false`

The comparison is based on captured browser DOM evidence. It does **not** activate Add, Edit, Delete, Value JavaScript, Import, Export, Save, or any other potentially state-changing action.

## Evidence set

| Evidence | Purpose |
|---|---|
| [`data-fields-global-tree-rows.json`](data-fields-global-tree-rows.json) | Normalized Global hierarchy: 6,297 `pmid` rows. |
| [`data-fields-firm-tree-rows.json`](data-fields-firm-tree-rows.json) | Normalized Firm hierarchy: 549 `pmid` rows. |
| [`data-fields-comparison-input-summary.json`](raw-captures/data-fields-comparison-input-summary.json) | Compact structural and action summary of both captures. |
| [`data-fields-comparison-metrics.json`](raw-captures/data-fields-comparison-metrics.json) | Reproducible comparison counts, reconstructed paths, metadata summaries, and representative examples. |
| [`data-fields-global-landing.snapshot.txt`](raw-captures/data-fields-global-landing.snapshot.txt) | Accessibility evidence for explicit Global scope. |
| [`data-fields-firm-current.snapshot.txt`](raw-captures/data-fields-firm-current.snapshot.txt) | Accessibility evidence for explicit Firm scope. |
| [`screenshots/manage-data-fields-global.png`](screenshots/data-fields/manage-data-fields-global.png) | Corrected Global Fields screenshot. |
| [`screenshots/manage-data-fields-firm.png`](screenshots/data-fields/manage-data-fields-firm.png) | Firm Fields screenshot. |

The large JSON captures were validated as parseable JSON. Their declared `count` values match the actual lengths of their `rows` arrays.

## Scope identity and count validation

| Check | Global | Firm |
|---|---:|---:|
| Explicit URL flag | `isGlobal=true` | `isGlobal=false` |
| Declared scope | `global` | `firm` |
| Declared hierarchy-row count | 6,297 | 549 |
| Actual hierarchy-row count | 6,297 | 549 |
| First row | `pmid2` | `pmid2` |
| Last row | `pmid6298` | `pmid550` |
| Unique ordinals | Yes | Yes |
| Maximum indentation | 8 units | 8 units |
| Hierarchy levels observed | 3 | 3 |

The numbers **6,297** and **549** are complete rendered hierarchy-entry counts. They include groups and subgroups; they are not leaf-field-only counts.

### Capture-property caveat

The Global normalized JSON predates the addition of `activeTabs` and `displayedCount`, so those properties are absent from that file. The Firm JSON contains:

- `activeTabs: ["Firm Fields"]`
- `displayedCount: ""`

The empty Firm `displayedCount` property is retained honestly. The visible number 549 is independently supported by the accessibility snapshot, screenshot, declared JSON count, actual array length, and DOM `pmid` row count.

## Method

### Row classification

The page renders a flat sequence of table rows whose indentation and expandability preserve a three-level hierarchy:

| Indentation | Expandable | Classification |
|---:|---|---|
| 0 | Yes | Top-level group |
| 4 | Yes | Subgroup |
| 8 | No | Leaf field |

### Conservative path reconstruction

Rows were processed in document order. The most recent labels at indentation levels 0, 4, and 8 were retained, and deeper labels were cleared whenever traversal returned to a shallower level. This produces paths such as:

`Budget / Budget Column / Allow UI Edit?`

This method is deterministic for the captured ordering and indentation. It does not establish undocumented server-side parent identifiers or inheritance relationships.

### Comparison keys

Two keys were tested:

1. **Path key** — reconstructed group/subgroup/leaf path.
2. **Composite key** — reconstructed path + internal field name + table association.

A conservative candidate override would require the same reconstructed leaf path in both scopes but different internal-name/table-association identities. No such candidate was found.

## Structural result

| Row type | Global | Firm | Shared reconstructed paths | Global-only | Firm-only |
|---|---:|---:|---:|---:|---:|
| Top-level groups | 24 | 24 | 24 | 0 | 0 |
| Subgroups | 320 | 320 | 320 | 0 | 0 |
| Leaf fields | 5,953 | 205 | 0 | 5,953 | 205 |
| **All hierarchy rows** | **6,297** | **549** | — | — | — |

### Shared scaffold

The scopes contain the same 24 top-level group paths and the same 320 subgroup paths. For one-to-one matches, no difference was found in the captured structural metadata.

The shared top-level groups are:

1. Budget
2. Company Items
3. Complex
4. Contract
5. Demographics Criteria
6. Documents
7. Equipment/Assets
8. Facility
9. Location
10. Milestones
11. Parcel
12. Pro Forma Lease
13. Program Summary Information
14. Prototype
15. Purchase Management
16. RE Planner
17. RE Transaction
18. Schedule
19. Site Survey
20. Specialized Forms
21. Statics
22. Summary Information
23. Wizard
24. Workflow

## Leaf-set result

No exact reconstructed leaf path is shared between Global and Firm. The composite-key comparison also found no shared leaf identity.

| Leaf comparison | Count |
|---|---:|
| Unique Global leaf paths | 5,953 |
| Unique Firm leaf paths | 205 |
| Duplicate leaf paths within Global | 0 |
| Duplicate leaf paths within Firm | 0 |
| Shared exact leaf paths | 0 |
| Shared composite identities | 0 |
| Conservative same-path override candidates | 0 |

### What zero overlap means

Directly observed:

- The captured Global and Firm leaf sets are disjoint under both tested keys.
- The two scopes share the same category scaffold.
- Firm leaves have tenant-editable action patterns that Global leaves do not.

Not proven:

- That Firm fields can never override Global fields by an undocumented identifier.
- That a differently named Firm field cannot represent the same business concept as a Global field.
- How Lucernex combines both catalogs in reports, forms, or page layouts.
- Whether the shared scaffold is copied, inherited, or rendered from a common source.

## Metadata profile

### Internal naming

| Metric | Global | Firm |
|---|---:|---:|
| Leaf fields | 5,953 | 205 |
| Internal names beginning `Firm_` | 0 | 202 |
| Percentage beginning `Firm_` | 0% | approximately 98.5% |

The prefix is strong evidence of a tenant-specific namespace. Three Firm internal names do not use this prefix, so it is a dominant convention rather than an absolute invariant.

### Required and read-only flags

| Flag | Global | Firm |
|---|---:|---:|
| Required = Yes | 637 | 0 |
| Required = No | 5,316 | 205 |
| Read Only = Yes | 0 | 0 |
| Read Only = No | 5,953 | 205 |

These values describe the fields as represented in this catalog. They do not prove how every consuming screen enforces editability or requiredness.

### Default values

- Global: all 5,953 captured leaves have an empty default value.
- Firm: 203 leaves have an empty default value; 2 contain `TBD`.

### Most frequent field types

| Global type | Count | Firm type | Count |
|---|---:|---|---:|
| `sTYPE_TEXT` | 961 | `sTYPE_TEXT` | 83 |
| `sTYPE_MONEY` | 891 | `sTYPE_CUSTOM_CODE_FIELD` | 54 |
| `sTYPE_DATE` | 365 | `sTYPE_DATE` | 12 |
| `sTYPE_NUMBER` | 336 | `sTYPE_NUMBER` | 12 |
| `sTYPE_UNFORMATTED_NUMBER` | 279 | `sTYPE_PERCENTAGE` | 9 |
| `sTYPE_MEMBER` | 261 | `sTYPE_TEXTAREA` | 8 |
| `sTYPE_MONEY_MATH_OPERATION` | 258 | `sTYPE_MONEY` | 8 |
| `sTYPE_TIME` | 232 | `sTYPE_CLIENT_LISTS` | 6 |
| `sTYPE_BOOLEAN` | 229 | `sTYPE_MONEY_MATH_OPERATION` | 4 |
| `sTYPE_PERCENTAGE` | 179 | `sTYPE_FIRM_LOGO` | 3 |

Firm-specific use of `sTYPE_CUSTOM_CODE_FIELD` and `sTYPE_CLIENT_LISTS` is a direct metadata observation. Their relationship to Manage Custom Lists, Firm Drop Downs, or Client Drop Downs requires separate screen exploration.

### Most frequent table associations

Global is distributed across many tables. Its largest captured associations include:

- `ExpenseRecovery` — 558
- `Contract` — 255
- `LeaseInfo` — 218
- `ProjectEntity` — 165
- `SLSummary` — 135
- `Asset` — 126
- `PaymentTransaction` — 118
- `ExpenseSetup` — 103

Firm is strongly concentrated on contract metadata:

- `Contract` — 147
- `KeyDate` — 10
- `ExpenseRecovery` — 9
- `Covenant` — 7
- `Employer` — 5
- `Location` — 5
- `ProjectEntity` — 5
- `Allowance` — 4

The `Contract` association represents 147 of 205 Firm leaves, approximately 71.7%.

## Action-model comparison

### Global

| Row kind | Actions | Rows |
|---|---|---:|
| Leaf | `edit details`, `Value Javascript` | 5,953 |
| Group/subgroup | None | 344 |

The label `edit details` is reported exactly as observed. Its presence means Global records are not accurately described as purely view-only for this account, even though no edit action was activated during exploration.

### Firm

| Row kind | Actions | Rows |
|---|---|---:|
| Leaf | `edit`, `delete`, `Value Javascript` | 205 |
| Subgroup | `Add Field` | 313 |
| Subgroup | `edit`, `delete`, `Add Field` | 7 |
| Top-level group | None | 24 |

The seven Firm subgroups with group-definition edit/delete controls are:

1. Contract / Common Area Maintenance
2. Contract / Custom Lists
3. Contract / Delivery Requirements
4. Contract / Ongoing Co Tenancy
5. Contract / Opening Co Tenancy
6. Contract / Real Estate Taxes
7. Contract / Test

This is direct evidence that at least some Firm subgroup definitions and all captured Firm leaf fields are tenant-manageable from the interface.

## Representative records

### Global example

`Budget / Budget Column / Allow UI Edit?`

| Property | Value |
|---|---|
| Internal name | `AllowUIEdit` |
| Field type | `sTYPE_BOOLEAN` |
| Required | No |
| Read only | No |
| Table association | `BudgetColumn` |
| Actions | `edit details`, `Value Javascript` |

### Firm example

`Company Items / Employers / Payment Method`

| Property | Value |
|---|---|
| Internal name | `Firm_PaymentMethod` |
| Field type | `sTYPE_CUSTOM_CODE_FIELD` |
| Required | No |
| Read only | No |
| Table association | `Employer` |
| Actions | `edit`, `delete`, `Value Javascript` |

## Evidence-based interpretation

### High confidence

- Global and Firm use the same three-level taxonomy in the captured page.
- Their top-level and subgroup paths match exactly.
- Global contains 5,953 leaf definitions; Firm contains 205.
- No leaf path or composite identity is shared under the documented method.
- 202 of 205 Firm internal names use the `Firm_` prefix.
- The Firm action model supports adding fields and deleting existing Firm fields.

### Moderate-confidence architectural interpretation

The evidence most strongly supports an **additive tenant-extension model**:

- Global provides built-in/platform field definitions.
- Firm provides tenant-defined additions.
- Both are placed under a common business taxonomy.
- Downstream tooling likely combines or selects from both catalogs.

This is an interpretation, not a proven implementation contract. The report deliberately does not use terms such as “inheritance,” “override,” or “merge” as established facts.

## Unresolved questions

1. Where are Global and Firm fields combined for report building, forms, and page layouts?
2. Can an undocumented record identifier link a Firm field to a Global field despite path/name differences?
3. Why are all 320 subgroup paths rendered in both scopes even when many Firm subgroups contain no Firm leaf?
4. Are the shared group/subgroup records copied per scope, inherited, or generated from one taxonomy?
5. What are the three Firm internal names without the `Firm_` prefix, and why do they differ?
6. What do the two `TBD` default values belong to, and how are defaults applied downstream?
7. Which permissions separately govern Global `edit details`, Firm `edit`, Firm `delete`, `Add Field`, Value JavaScript, import, and export?
8. How do `sTYPE_CUSTOM_CODE_FIELD` and `sTYPE_CLIENT_LISTS` connect to Custom Lists and dropdown administration?
9. Are field changes versioned or audited, and does **Layout Changes** include them?
10. Does “Global” mean platform-wide across tenants or globally available only within this tenant context?
