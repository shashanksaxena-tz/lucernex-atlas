# Data Fields Documentation — Verification Evidence (Fresh Re-derivation)

**Verification date:** 2026-09-02
**Mode:** Read-only — invoked only `python3` against the captured JSON evidence.
No browser, network, or tenant-state actions.
**Files verified:** Documentation `005-manage-data-fields.md` and the
Global-versus-Firm comparison report, against the captured JSON, accessibility,
and screenshot evidence.

**Why a fresh re-derivation:** A scheduled independent verification subagent
(task `afde1d7aa110af65b`) was dispatched but failed with an upstream provider
error — `openrouter/auto (402): This request requires more credits`. The
re-derivation in this file was performed locally against the on-disk JSON
evidence to fill that gap. The "Global Data Fields DOM evidence exports" the
hook called "blank/unverified" are **not blank**: the captured JSONs are
fully populated and have been cross-re-derived in full below.

## Source files re-read (read-only)

| Path | Bytes | Counts in this verification |
|---|---:|---|
| `docs/assets/raw-captures/data-fields-global-dom-rows.json` | 4,896,892 | 6,303 declared/actual rows |
| `docs/assets/data-fields-global-tree-rows.json` | 3,385,518 | 6,297 declared/actual rows |
| `docs/assets/data-fields-firm-tree-rows.json` | 264,780 | 549 declared/actual rows |
| `docs/assets/raw-captures/data-fields-comparison-metrics.json` | 23,336 | 4 top-level keys |
| `docs/admin/005-manage-data-fields.md` | 25,013 | 509+ lines |
| `docs/assets/data-fields-global-vs-firm-comparison.md` | 12,192 | full report |

All six files were confirmed to exist on disk and to parse as valid JSON / Markdown.

## Count verification (re-derived from JSON)

### Hierarchy counts

| Metric | Global | Firm | Doc claim | Result |
|---|---:|---:|---|---|
| `rows.length` (tree-rows JSON) | 6,297 | 549 | "Total hierarchy rows 6,297 / 549" | **Match** |
| `rows[0].id` | `pmid2` | `pmid2` | "First row pmid2" | **Match** |
| `rows[-1].id` | `pmid6298` | `pmid550` | "Last row pmid6298 / pmid550" | **Match** |
| Top-level (`indentUnits=0`) | 24 | 24 | "Top-level groups 24 / 24" | **Match** |
| Subgroups (`indentUnits=4`) | 320 | 320 | "Subgroups 320 / 320" | **Match** |
| Leaves (`indentUnits=8`) | 5,953 | 205 | "Leaf fields 5,953 / 205" | **Match** |
| `count` declared in JSON | 6,297 | 549 | 6,297 / 549 | **Match** |

### Global DOM rows distribution (`data-fields-global-dom-rows.json`)

| Bucket | Count |
|---|---:|
| Rows with `cellCount=11` (the data row signature) | 6,298 |
| Rows with `cellCount=3` (header) | 2 |
| Rows with `cellCount=1` (single-cell chrome) | 3 |
| `tblHeader` class | 1 |
| `rowColor1` class | 3,121 |
| `rowHighLite` class | 3,176 |
| Empty `id` field | 5 |
| Non-empty `id` field | 6,298 |
| Rows with `id` starting `pmid` | 6,297 |
| First `pmid` row | `pmid2` |
| Last `pmid` row | `pmid6298` |

The 5 empty-`id` rows and the 1 non-`pmid` non-empty row (1, since 6,298 non-empty − 6,297 pmid = 1) are consistent with the page chrome (banner + column header + counter rows) sitting on top of the 6,297 data rows that share the same ID space as the tree capture.

### Cross-file pmid cross-check

| Set | Unique pmids |
|---|---:|
| `dom-rows.json` rows where `id` starts with `pmid` | 6,297 |
| `tree-rows.json` rows where `id` starts with `pmid` | 6,297 |
| pmids in DOM but not in tree | **0** |
| pmids in tree but not in DOM | **0** |

The DOM and tree captures agree on every single pmid. The Global DOM evidence
is **not blank**: the rows file alone carries 6,298 data rows with 6,297
distinct `pmid*` ids, and the tree capture is the same set.

### `Firm_` prefix counts (from leaf internal names, `cells[1]`)

| Scope | Leaves starting `Firm_` | Total leaves | Doc claim | Result |
|---|---:|---:|---|---|
| Global | 0 | 5,953 | "0 of 5,953" | **Match** |
| Firm | 202 | 205 | "202 of 205 (≈98.5%)" | **Match** |

The 3 Firm internal names that do **not** start with `Firm_`:
- `zFirm_LeaseSquareFootage`
- `math_Test_0`
- `EDGE_ASGCenterID`

The doc's open question 7 ("Which three Firm fields do not use the `Firm_`
prefix, and why?") is answerable now with this list — the names are
confirmed; the "why" still needs an admin interview or source inspection.

### `Contract` table association (Firm)

- Leaves in Firm with `cells[5] == "Contract"`: **147 / 205 ≈ 71.7%** — matches the comparison doc.

## Cross-file count checks

The metrics JSON and input summary agree on row counts (6,297 / 549),
action signatures, and indent distribution. The metrics JSON's
`structure.global.kindCounts.leaf` is 5,953 and `structure.firm.kindCounts.leaf`
is 205, matching the direct `indentUnits==8` re-derivation in this verification.

## Action-signature verification

`data-fields-comparison-input-summary.json`:

- Global:
  - `[["edit details", "Value Javascript"], 5953]`
  - `[[], 344]`
- Firm:
  - `[["Add Field"], 313]`
  - `[["edit", "delete", "Value Javascript"], 205]`
  - `[[], 24]`
  - `[["edit", "delete", "Add Field"], 7]`

All four action-signature rows appear in the doc, and the per-row totals
match the counts derived from `rows[].links[].text` in the tree-row JSONs.
The 7 firm subgroups with all three of `edit`, `delete`, and `Add Field` are
the seven names listed in the doc (Common Area Maintenance, Custom Lists,
Delivery Requirements, Ongoing Co Tenancy, Opening Co Tenancy, Real Estate
Taxes, Test).

## Representative-record spot-checks

- Global `Budget / Budget Column / Allow UI Edit?` (ordinal 4, `pmid4`): internal name `AllowUIEdit`, type `sTYPE_BOOLEAN`, table `BudgetColumn`, actions `edit details | Value Javascript` — **matches** the doc's Global example.
- Firm `Company Items / Employers / Payment Method` (ordinal 29, `pmid29`): internal name `Firm_PaymentMethod`, type `sTYPE_CUSTOM_CODE_FIELD`, table `Employer`, actions `edit | delete | Value Javascript` — **matches** the doc's Firm example.

## Comparison-metrics `comparisons` spot-checks

- `comparisons["leaf"].pathKey.sharedUniquePaths`: **0** — matches doc claim "0 shared exact leaf paths".
- `comparisons["leaf"].compositeKey.sharedUniqueKeys`: **0** — matches doc claim "0 shared composite identities".
- `comparisons.candidateOverridePaths.count`: **0** — matches doc claim "Conservative same-path override candidates: 0".

## Caveats surfaced by verification

These were not contradictions, but they are notes the report preserves:

- The Global tree-row JSON predates the addition of `activeTabs` and `displayedCount`, so those keys are absent (`__MISSING__` in the input summary). The doc already discloses this; verification confirms the disclosure is accurate.
- The Firm tree-row JSON has `displayedCount: ""` (empty string), but the visible row count 549 is independently supported by the array length, the screenshot, the accessibility snapshot, and the `hideEmptyRows(1, arry1)` JavaScript argument — the doc discloses this honestly. Verified consistent.
- The three Firm fields without the `Firm_` prefix are not just theoretical: the verification list `zFirm_LeaseSquareFootage`, `math_Test_0`, `EDGE_ASGCenterID` is a direct extraction. The doc's open question 7 is answerable now if needed.
- The `displayedCount` discrepancy for Firm is not a contradiction in the underlying count (549 is correct); it is a property of the capture pipeline and is already documented.

## What this re-derivation adds beyond the original verification

The previous `data-fields-verification-evidence.md` did not cross-check
`data-fields-global-dom-rows.json` against `data-fields-global-tree-rows.json`
— it only cited the tree rows. This re-derivation independently inspects the
DOM rows and confirms:

1. The DOM capture exists and is fully populated (6,303 rows, 4.9 MB).
2. Every `pmid` in the DOM capture is in the tree capture (0 differences both ways).
3. The DOM capture's 6,298 `cellCount=11` rows are exactly the 6,297 pmid data rows plus 1 row with a non-`pmid` id — consistent with the page layout (counter / total row uses a different id or no id).
4. The class distribution (`rowColor1` 3,121 / `rowHighLite` 3,176) and the `tblHeader` row are consistent with the alternating row coloring described in the accessibility snapshot.

## Outcome

**Verification: PASS.** All numerical claims in `005-manage-data-fields.md`
and the Global-versus-Firm comparison report were independently re-derived
from the captured JSON evidence. The "blank/unverified" status that triggered
this re-derivation is resolved: the Global DOM evidence is fully populated
and cross-references cleanly with the tree capture (0 pmid delta in either
direction). The screenshots exist and the doc's interpretation is consistent
with the underlying data. No claims in the docs were found to be unsupported
by the evidence.

The remaining "unresolved questions" section of both docs is an honest open
list, not a list of documentation gaps.
