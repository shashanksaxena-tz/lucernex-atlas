# ASG Edge+ mapping

**Stated up front.** ASG Edge+ has document storage already, since `ASG-Edgeplus-Documents-Service`
exists and is running as one of the extracted microservices (per the workspace index,
`ASG/Code/CLAUDE.md`). This module's job is therefore not "build document storage from nothing" but
**"decide how much of Lucernex's model to check against the existing service, and what to
deliberately not copy"** — and two of Lucernex's own headline capabilities (markups, Binders) turn
out to have no recoverable schema of their own to check against at all (§2).

## 1. What exists today

| ASG Edge+ artefact | What it says | Gap |
|---|---|---|
| `ASG-Edgeplus-Documents-Service` | A running, extracted document-storage service | Whether it already models folders, checkout, versioning, or per-folder security to the same depth as Lucernex is not established by this pass — that comparison should happen against the service's own code, not this document. |
| Workspace index target architecture | Does not name Documents/Folders as Hub or Spoke explicitly | Given `Document`/`Folder` are `entity_scoped` in Lucernex (attached via `ProjectEntityID`), and per-tenant `ProjectEntityID` scoping is a Spoke concept per [`../../data-model/project-entity.md`](../../data-model/project-entity.md) §5, documents attached to Spoke-side entities (Contracts, Facilities) should themselves live Spoke-side, database-per-tenant, consistent with the rest of that argument. |

## 2. What must be built, and what cannot be recovered from this schema

| Lucernex capability | ASG Edge+ status | Reasoning |
|---|---|---|
| `Document` + `Folder` (storage, checkout, folder tree, per-folder security) | Compare against `ASG-Edgeplus-Documents-Service`'s existing model; port what's missing | Substantive, well-defined objects (`Document` 23 fields, `Folder` 16, `FolderSecurity` 3) — a real basis for comparison. |
| Document version lineage | **Must design fresh, even if porting `Document`** | Lucernex's own `Version`/`IsLatestVersion` flags have no explicit grouping FK (`DOC-R-005`) — there is nothing to port here beyond the two flags themselves; the actual lineage mechanism needs new design. |
| Document markups | **Cannot be ported — must design fresh if wanted** | `DocumentMarkup` is a 1-field stub (`DOC-R-010`); no source available to this pass shows what markup data actually looks like. Confirm with the business whether markups (annotations/redlines) are even required before designing this from scratch. |
| Binders / Committee Packages | **Cannot be ported — must design fresh if wanted, and its scope is unknown** | No backing object was found anywhere in the 223-object census (§3 of `data-model.md`). Before building anything, open the live Lucernex screen to learn what a Binder actually assembles — otherwise ASG Edge+ risks guessing at a feature whose real shape is unknown. |
| Folder templates | Should build, reading `VirtualTemplateFolder`'s shape, not `FolderTemplate`'s | `FolderTemplate` itself is a stub (`DOC-R-007`); the template's real metadata and its `IsValidFor*` attachability matrix live on `VirtualTemplateFolder`. |
| Inbound correspondence (`EMailReceivedLog` + attachment promotion) | Can defer | Substantive but self-contained; not load-bearing for any other module. |
| Outbound correspondence | **Cannot be ported at all** | `EMailSentLog` is a 1-field stub. If ASG needs sent-mail tracking, it is a from-scratch design with no Lucernex precedent to draw on. |

## 3. What should deliberately differ

- **Give document version lineage an explicit FK from day one.** Lucernex's flags-only approach
  (`DOC-R-005`) is a real gap worth fixing rather than reproducing.
- **Decide the templating event's shape deliberately.** If ASG Edge+ needs folder/budget/task
  templates applied together as one event (`DOC-R-009`), design that relationship explicitly rather
  than discovering it as an emergent side effect of three separate template-application flows, the
  way Lucernex's `FolderTemplateAudit` suggests happened there.
- **Confirm Binders' actual requirement before designing anything.** Since no object was found,
  there is no risk of silently under-building against a hidden schema — but there is a real risk of
  over-building a guess. Open the live screen first.
- **Confirm whether markups and per-folder, per-user-class security are both genuinely required**
  before investing in either — one (`FolderSecurity`) is a small, well-defined feature worth keeping
  if wanted; the other (markups) has no known shape to build toward and should not be estimated
  until that shape is established.

## 4. Decisions blocking a build

1. **What does `ASG-Edgeplus-Documents-Service` already model**, and where does it already exceed or
   fall short of what Lucernex's `Document`/`Folder` capture? This document does not answer that —
   it requires reading the service's own code, out of scope for this pass.
2. **Is Binders/Committee Packages in scope for ASG Edge+ at all**, and if so, what does it actually
   need to do? Blocked entirely on opening the live Lucernex screen, which this pass did not do.
3. **Are document markups a real business requirement**, or a Lucernex capability ASG has never
   exercised? A business question, not checked here.
4. **Is outbound correspondence tracking required at all?** No Lucernex precedent exists to size the
   feature against either way.

## Open questions

Carried forward from the other documents in this folder, ranked by how much each blocks a build
decision.

1. What object, if any, actually backs "Binders"/"Committee Packages" in Lucernex? Blocks whether
   ASG Edge+ has anything at all to model against.
2. Where does markup annotation content actually live in the live product, if not in
   `DocumentMarkup`?
3. How are successive versions of the same logical document actually grouped in Lucernex's live
   behaviour, independent of the missing FK?
4. Is outbound correspondence tracking a genuine Lucernex product gap, or an artefact of this
   export?
