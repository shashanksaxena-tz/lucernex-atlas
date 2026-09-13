# Documentation conventions

Every document in `docs/` follows these rules so that both humans and AI agents can navigate the
corpus predictably. Read this before creating or editing anything.

## Folder map

| Path | Holds |
|---|---|
| `docs/INDEX.md` | The master index. Every new document must be registered here. |
| `docs/COVERAGE.md` | The surface scoreboard — every known screen, tool, layout, table and drop-down, and whether a document owns it. **Generated. Do not hand-edit.** |
| `docs/tools/` | The generator behind `COVERAGE.md`: `build_coverage.py` plus the hand-curated `coverage-owners.json`. Edit the JSON and re-run `python3 docs/tools/build_coverage.py`. Same pattern as `docs/mindmap/build_*.py`. |
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
- **Cite screenshots by path in `code`, never as a markdown link.** The screenshot sets are
  periodically re-captured and renumbered — `bbw-admin/` went from 56 files to 0 mid-session during
  one such sweep — so hard links rot while the evidence itself is fine. A `code`-formatted path
  satisfies the citation requirement and cannot break. `COVERAGE.md` resolves screenshots from the
  filesystem at build time and so self-heals on re-run.
- **A screenshot is evidence only for what is inside the frame.** These admin grids are wider than
  the capture width, and the right edge is exactly where row-action columns, pagination and required
  asterisks live. **Check for truncation before inferring absence.** This rule exists because an
  inference was published and then withdrawn after a `*` turned out to be cropped out of frame. Where
  a grid's data can be read as JSON, prefer that as the primary evidence and treat the screenshot as
  illustration.
- **When a signal is conveniently to hand, that is exactly when to check it against the thing it
  stands for.** Four confident readings in this project were wrong for the same reason, and in every
  case the wrong signal was *cheaper to read* than the right one:

  | Wrong signal | Right one | Cost difference |
  |---|---|---|
  | A column **name** (`PreviousPageLayoutID` → "versioning") | What the values actually link | The name is right there; the join needs building |
  | A UI **label** (12 phantom census gaps) | The physical name | The label is on screen; the physical name needs a lookup |
  | A **key-union** (`DisplayOption` "only 0 and 288") | The values themselves | One pass versus many |
  | A **default parameter** (`showGlobal=true`) | The correct one | No thought versus knowing what the radio means |
  | A **network response** (`fetch` says 36 of 46 routes resolve; a real browser says **14**) | What actually renders | One request versus driving a browser |

  Cheapness is the warning sign, not the convenience. Test the reading against the thing it stands
  for before publishing it.

- **In this application, a `200` with a plausible body proves the server answered and nothing about
  what renders.** The fifth case above is the most dangerous of the five, because the other four are
  obviously *proxies* once you look at them — a name, a label, a sample, a parameter — whereas a
  network response feels like direct evidence. 22 of 46 Contract routes return a full 37–40KB HTML
  document and then **bounce client-side** to `EntityInfo.jsp`, rendering the default Summary. A
  fetch-based route audit overstates deep-linkability by more than 2×.

  This is the same failure that produced this corpus's retracted conditional-fields false negative:
  fetching `LayoutEditorAJAX.jsp`, finding no conditional targets because they are injected
  client-side, and concluding the feature was unused across 93 layouts.

- **These failures do not produce errors; they produce clean-looking results.** Empty where you
  expected empty, complete where you expected complete — which is why neither case was caught by the
  person who made it. **The guard has to be structural, not attentional:** state which population you
  sampled, state how you sampled it, and prefer the method that observes the thing a user would see.
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
  **This is load-bearing, not stylistic.** `Manage Firm Dictionary` (`/en/admin/Dictionary.jsp`) lets
  a firm **overwrite field labels tenant-wide** by uploading an XLSX, with global and firm-specific
  layers and per-language variants
  ([`features/administration/`](features/administration/#manage-firm-dictionary--every-label-in-this-corpus-is-tenant-overridable)).
  So **every UI label recorded in this corpus is potentially tenant-local** — screen names,
  navigation node names, field labels, code-table value names. Internal names (`ScriptName`,
  `CodeContractStatusID`, physical table names) are not affected, and are the only safe identifier
  to build against. Whether either tenant has actually overridden a label is unknown.
- No filler. If a section has nothing in it, delete the section.
