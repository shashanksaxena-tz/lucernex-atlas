# Documentation conventions

Every document in `docs/` follows these rules so that both humans and AI agents can navigate the
corpus predictably. Read this before creating or editing anything.

## Folder map

| Path | Holds |
|---|---|
| `docs/INDEX.md` | The master index. Every new document must be registered here. |
| `docs/CONVENTIONS.md` | This file. |
| `docs/screens/NNN-*.md` | End-user screens, numbered in exploration order. |
| `docs/admin/NNN-*.md` | Administration screens, numbered in exploration order (shared number series with `screens/`). |
| `docs/modules/<module>/` | Functional module deep-dives. One folder per module. Not screen-shaped — concept-shaped. |
| `docs/data-model/` | Schema reference: objects, tables, columns, foreign keys, cardinality. |
| `docs/data-fields/` | The 6,158-leaf Manage Data Fields catalog, one file per entity. |
| `docs/mindmap/` | Source data for the interactive mind map artifact. |
| `docs/assets/screenshots/<area>/` | Screenshots, grouped by area, referenced with relative paths. |

## Every module folder must contain

1. `README.md` — the module's entry point. What it is, why it exists, its place in the system,
   and a linked table of contents for the rest of the folder.
2. `data-model.md` — the objects/tables this module owns, their fields, and their FK edges.
3. `rules.md` — the business rules, computations, and state transitions the module enforces.
   This is the file that feeds the ASG Edge+ rule engine. Be explicit about what is *observed*
   versus *inferred*.
4. `asg-edgeplus-mapping.md` — how this maps onto ASG Edge+: what exists, what must be built,
   what should deliberately differ, and the open questions blocking a decision.

## Evidence discipline

This corpus is the input to a rebuild. A wrong "fact" here becomes a wrong line of code later.

- **Label every claim.** Use one of: **Observed** (seen directly in the UI or a data export),
  **Derived** (computed from observed data, e.g. counting rows in a capture), or **Inferred**
  (domain reasoning, naming conventions, or analogy — not confirmed).
- **Cite the source** for observed facts: screen route, screenshot path, or source file and line.
- Never restate an inference as a fact in a later document. If document B cites document A, it
  inherits A's confidence label.
- Where a question could not be answered, say so in a `## Open questions` section rather than
  guessing. Open questions are valuable output, not failure.

## Source material available offline

| File | Contents |
|---|---|
| `_lucernex_objects_summary.txt` | **223 Lucernex objects, 7,421 fields.** TSV: `LUCERNEX OBJECT / PG TABLE / FIELD COUNT / FIELDS`. The `FIELDS` column is ` \| `-separated `Name(Type)` pairs. Types include FK types (`Contract ID`, `Employer ID`, `Entity ID`), dropdown bindings (`Dropdown (Expense Type Code)`), and plain types. **This is the single richest offline artifact — the schema of the whole product.** |
| `_crossmap.tsv` | Per-leaf-field cross-map, 17 columns, joins Manage Data Fields leaves to Lucernex objects/columns and carries an `ASGStatus`. |
| `docs/data-fields/all-fields.csv` | 6,158 Manage Data Fields leaves: `Entity, Label, InternalName, FieldType, Scope, Required, ReadOnly, Default`. |
| `docs/data-fields/INDEX.md` | 214 entities with plain-language explanations; full 448-code field-type legend. |
| `docs/data-fields/<entity>.md` | Per-entity field tables. |
| `docs/admin/004-009*.md` | The screens explored so far. 009 establishes the FK-driven relational model. |
| `_xlsx_lucernex_jcrew.txt`, `_xlsx_feature_list.txt` | Vendor/feature workbooks exported to text. |

## Writing style

- Tables over prose wherever the content is enumerable.
- Every document opens with a short **stated up front** paragraph giving the conclusion, before
  the evidence. A reader who stops after the first paragraph should still have the answer.
- Use real field and table names in `code` formatting, never paraphrases of them.
- No filler. If a section has nothing in it, delete the section.
