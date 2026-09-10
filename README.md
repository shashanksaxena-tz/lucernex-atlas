# Lucernex Atlas

A map of **Lucernex IWMS** (LxRetail, by Accruent) as it actually runs — read out of a live
training tenant and its own schema tools, so that the platform can be understood before anything
is rebuilt.

**→ [Browse the atlas](https://shashanksaxena-tz.github.io/lucernex-atlas/)**

| | |
|---|---:|
| Modules | 15 |
| Record types | 223 |
| Fields | 7,421 |
| Foreign keys | 972 |
| Numbered rules | 384 |
| Open questions | 286 |
| Manage Data Fields leaves | 6,158 |
| GraphQL API types | 490 |

Captured 2026-09-10 from build `26.08.0.46`. Exploration was read-only throughout: no record,
layout, workflow, code table or configuration value was created, edited or deleted.

## What is here

### The atlas — `docs/site/`

628 static HTML pages, no server needed. Open `docs/site/index.html` and it works.

- `index.html` — the overview
- `entities/` — one page per record type, every field grouped and explained, foreign keys linked
  in both directions
- `modules/` — one page per functional module
- `rules/` — one page per numbered rule
- `questions.html` — every open question, by area
- `atlas.html` — the interactive application: search, drillable mind map, and shared notes

### The documents — `docs/`

Around 190 markdown files. Start at [`docs/INDEX.md`](docs/INDEX.md), which routes both people and
agents. [`docs/CONVENTIONS.md`](docs/CONVENTIONS.md) defines the evidence discipline every document
follows.

| Path | Holds |
|---|---|
| `docs/admin/` | Administration screens, captured with screenshots |
| `docs/modules/` | Five module deep-dives: accounting, contracts, workflow, layouts-and-forms, reporting |
| `docs/data-model/` | Object catalog, foreign-key graph, type system, GraphQL and REST APIs, the 207-entry code-table registry |
| `docs/data-fields/` | All 6,158 Manage Data Fields leaves, per entity, plus a flat CSV |
| `docs/mindmap/` | The build scripts and their JSON output |
| `docs/assets/screenshots/` | Evidence for the screen captures |

## Evidence discipline

Every claim carries one of three labels, and they are load-bearing:

- **Observed** — somebody saw it in the running application or a vendor export
- **Derived** — computed from observed data
- **Inferred** — domain reasoning or naming convention, *not confirmed*

An Inferred claim is a hypothesis someone still has to check. The 286 open questions are the ones
that matter most, and they are indexed rather than buried.

## Rebuilding the site

Everything under `docs/site/` and `docs/mindmap/*.json` is generated. After a fresh capture:

```bash
cd docs/mindmap
python3 build_graph.py       # parse the schema dump -> objects/edges/modules JSON
python3 build_mapdata.py     # compact it for the browser, pull in curated trees
python3 build_rules.py       # extract 384 numbered rules from the module documents
python3 build_questions.py   # gather every open question
python3 build_app.py         # assemble the single-file interactive application
python3 build_site.py        # regenerate the 628-page static site
```

No network access, no dependencies beyond the Python standard library.

## A note on scope

Cost management, budgeting and bidding are **out of scope by decision**. Those record types stay in
the catalog and the foreign-key graph so the model stays whole, grouped under
`out-of-scope-cost-budget` with one-line descriptions only.

## Provenance

This documents a third-party commercial product for the purpose of understanding it. Lucernex and
LxRetail are products of Accruent. Nothing here is vendor documentation — where a reading is
inferred rather than observed, the documents say so.
