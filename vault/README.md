---
title: Vault README
tags: [meta]
---

# The Lx knowledge vault

An Obsidian-compatible graph of small, densely interlinked notes about the Lx product. It is a
sibling of [`docs/`](../docs/INDEX.md), not a replacement for it.

- **`docs/`** is a *reference corpus* — long documents, read top to bottom, exhaustive.
- **`vault/`** is a *graph* — one note per thing, linked to the things it touches, wandered rather
  than read.

Start at **[[00-start-here]]**.

## Opening it in Obsidian

**Recommended: open the repository root as the vault.**

```
Obsidian → Open folder as vault → …/Lx
```

Everything then resolves: the `[[wikilinks]]` between notes, the embedded screenshots (which live
under `docs/assets/screenshots/` and are referenced with relative paths), and the outbound links
from vault notes into the `docs/` corpus. The graph view will also show the `docs/` files, which is
usually what you want — the vault is the map and `docs/` is the territory. Use Obsidian's
**Graph view → Filters** with the query `path:vault` to see the vault's own graph alone.

**Alternative: open `vault/` itself.** The note-to-note graph works exactly the same. Embedded
screenshots will not render, because the image files live outside that folder. They are deliberately
not copied in: the screenshot sets are periodically re-captured and renumbered, and a duplicated copy
would silently rot. Every embed is followed by the canonical path in `code` formatting, which is the
citation that cannot break.

There is no `.obsidian/` directory here on purpose — adding one would hard-code a choice between the
two modes above.

## How the graph is organised

| Folder | Holds | Filename shape |
|---|---|---|
| `concepts/` | The ideas the product is built out of — a layout, a code table, required-ness, the entity spine | kebab-case prose, `page-layout-concept.md` |
| `entities/` | One note per significant record type, named with the **real object name** | `Contract.md`, `SLSummary.md` |
| `modules/` | The thirteen functional modules, each a hub for its entities and rules | `module-accounting.md` |
| `features/` | The twelve feature areas — the product as a user meets it | `feature-page-layouts.md` |
| `screens/` | One note per captured screen, embedding its screenshot | `screen-manage-discount-rates.md` |
| `rules/` | The numbered business rules, grouped by module, plus the individually load-bearing ones | `rules-accounting.md`, `rule-ACC-R-011.md` |
| `findings/` | One note per significant finding, each stating its evidence | `finding-publish-then-fork.md` |
| `open-questions/` | One note per open question, each stating what would settle it | `q-bbw-03-task-step.md` |
| `tenants/` | The two tenants read, and what differs between them | `tenant-bbw.md` |
| `methods/` | How things were found out, and the ways the finding-out went wrong | `method-fetch-is-not-render.md` |

Five **maps of content** are the hubs: [[map-of-concepts]], [[map-of-entities]], [[map-of-features]],
[[map-of-findings]], [[map-of-open-questions]], plus [[map-of-screens]] and [[map-of-rules]].

## Conventions

**Naming.** The product is written **Lx** throughout. Real technical identifiers — `LxRetail`, `lxID`,
`PageLayoutField`, `Firm_LeaseAnalyst`, table and column names — are code, and are left exactly as
they are.

**Links.** `[[wikilinks]]` are used *only* for note-to-note connections, because that is what drives
Obsidian's graph. Everything else — screenshots, links into `docs/`, links to raw captures — uses
standard markdown, so the same files render in Obsidian, on GitHub and in any generated site.

**Frontmatter.** Every note carries `title`, `tags`, and — where it makes a claim — `evidence:` one
of `Observed`, `Derived` or `Inferred`. See [[evidence-labels]]. Notes that make claims at several
confidence levels carry the *weakest* label in frontmatter and label each claim in the body.

**Screenshots.** Embedded with a standard markdown image, `!` + `[caption]` + `(relative/path.jpg)`, and immediately followed by the
canonical path in `code`. The caption says what to notice, not what the picture is of.

**Length.** A note that needs scrolling probably wants splitting. If you are adding to a note and it
is getting long, the thing you are adding is usually its own note.

**Nothing is invented.** If a claim is Inferred, it says so. If something is unknown, it is an
open-question note with a falsifier, not a confident sentence.

## Adding to it

1. One note, one thing. Give it a `title`, `tags`, and an `evidence` label if it claims anything.
2. Link it to at least one hub and at least two siblings. **A note with no inbound and no outbound
   links is a failure** — it will sit alone in the graph and never be found again.
3. Cite the `docs/` document the fact came from, as a relative markdown link.
4. If you are recording a person's name, stop. See [[method-omitting-identities]].
