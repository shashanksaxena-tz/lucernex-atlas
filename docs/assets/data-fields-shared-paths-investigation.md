# Data Fields — Shared Paths Investigation (2026-09-02)

## Question
The doc `data-fields-global-vs-firm-comparison.md` claims:
- `sharedUniquePaths = 0` (no shared exact leaf paths)
- `sharedUniqueKeys = 0` (no shared composite identities)
- `candidateOverridePaths.count = 0`

## Independent re-derivation

### From JSON evidence (`data-fields-comparison-metrics.json`)

| Field | Value | Doc claim | Match |
|---|---:|---|---|
| `comparisons.leaf.pathKey.sharedUniquePaths` | 0 | 0 | YES |
| `comparisons.leaf.compositeKey.sharedUniqueKeys` | 0 | 0 | YES |
| `comparisons.candidateOverridePaths.count` | 0 | 0 | YES |
| `structure.global.kindCounts.leaf` | 5953 | 5953 | YES |
| `structure.firm.kindCounts.leaf` | 205 | 205 | YES |
| `pathKey.globalRows` | 5953 | 5953 | YES |
| `pathKey.firmRows` | 205 | 205 | YES |
| `pathKey.sharedRowsMultiset` | 0 | 0 | YES |
| `pathKey.globalOnlyRowsMultiset` | 5953 | 5953 | YES |
| `pathKey.firmOnlyRowsMultiset` | 205 | 205 | YES |
| `pathKey.globalOnlyUniquePaths` | 5953 | 5953 | YES |
| `pathKey.firmOnlyUniquePaths` | 205 | 205 | YES |

### Discrepancy found in prior turn

The prior turn's `/tmp/_verify3.py` used `cells[0]` (the leaf label alone) as the path key:

| Metric | Global | Firm | Shared |
|---|---:|---:|---:|
| Leaves by leaf-label only (`cells[0]`) | 3762 | 153 | 10 |
| Leaves by composite key (label + internal name + type + table) | 5953 | 205 | 0 |

The doc uses the **composite** key (or a `pathKey` that captures the full hierarchical
path), not the leaf label alone. By label, 10 labels coincide. By composite identity
or full path, 0 coincide. The doc's "0 shared exact leaf paths" is correct under its
own definition.

## Resolution

The doc claims are correct as stated:
- `sharedUniquePaths=0` — no Global leaf path appears identically in Firm (this is
  the `pathKey` join, which is a deeper full-path or composite key, not just `cells[0]`).
- `sharedUniqueKeys=0` — no Global leaf matches a Firm leaf on label + internal name
  + field type + table association.
- `candidateOverridePaths.count=0` — no Global leaf has the same reconstructed path
  in Firm where the identity set (internal-name, table-association) differs.

The 10 by-label coincidences are simply labels reused across scopes (e.g. "Comments"
or "Name" — common field names) without the underlying field being the same record.

## Open follow-up (not a documentation defect)

If anyone asks "show me the 10 labels that collide by name alone", we can produce
that list from the tree-row JSON. It's not currently in the docs because the docs
use the stricter composite/path key, which is the right thing for a data-mapping
report.
