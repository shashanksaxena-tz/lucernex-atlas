# Documents, Folders & Correspondence — module overview

**Stated up front.** Ten objects, 99 fields — the smallest field count of any in-scope module — and
the count itself is the finding: **four of the ten objects are 1-to-3-field stubs.**
`DocumentMarkup` and `EMailSentLog` carry exactly one field each (`ProjectEntityID`);
`FolderTemplate` carries one field too; `FolderSecurity` carries three. The substantive content sits
in `Document` (23 fields), `FolderTemplateAudit` (18), `Folder` (16), `VirtualTemplateFolder` (16),
and `EMailReceivedLog` (15). This module is universal in reach — every `ProjectEntity` root carries
a `Documents` tab (`document/Index.jsp`, per [003](../../screens/003-main-navigation.md)) and a
`Binders` tab (`CommitteeDocuments/PECommPkg.jsp`) — but two of its most-asked-about capabilities
turn out to have **no substantive backing in the schema export available to this pass**: markup
content (`DocumentMarkup` is a stub; only a boolean flag on `Document` survives) and **Binders
themselves**, which route to a JSP internally named "Committee Packages" but correspond to **no
object anywhere in the 223-object census** — not `Binder`, not `Committee`, not anything close.
Meanwhile the live tenant holds **11,905 documents**
([`../../data-model/graphql-api.md`](../../data-model/graphql-api.md)), the largest single
collection in the product, so this is not a lightly-used corner of the schema — it is a heavily-used
feature whose full data model this pass could not fully recover.

*Evidence class for this paragraph: **Observed** field counts from `_lucernex_objects_summary.txt`
and an exhaustive object-name search against
[`../../data-model/object-catalog.md`](../../data-model/object-catalog.md); the explanations for the
gaps are explicitly **Derived**/unconfirmed — see [`data-model.md`](data-model.md) for the full
argument and the open questions this leaves.*

## The module at a glance

| Property | Value |
|---|---|
| Objects | 10 |
| Fields | 99 |
| Stub objects (≤3 fields) | 4 — `DocumentMarkup` (1), `EMailSentLog` (1), `FolderTemplate` (1), `FolderSecurity` (3) |
| Internal FK edges | 2 — both from `LinkEMailReceivedLogDocument` |
| Inbound cross-module edges | 16 — nearly all a generic "attach a document/folder to this record" pattern used by financial and operational records across the product |
| Outbound cross-module edges | 20 |
| Dashboard heading | Folder Administration |
| Live tenant volume | **11,905 documents** — the largest collection captured in this corpus ([`../../data-model/graphql-api.md`](../../data-model/graphql-api.md)) |
| End-user surface | Universal `Documents` tab on every entity root; universal `Binders` tab, no backing object found (§ below) |

## Documents are universal, and Binders are "Committee Packages" — with no schema object

Every entity root's `Documents` tab is the same renderer, `document/Index.jsp`, for every entity
type — this module, like `../facilities-locations/`'s address block or
`../../modules/layouts-and-forms/`'s Forms tab, is part of the shared `ProjectEntity` tab strip
[`../../data-model/screen-routing.md`](../../data-model/screen-routing.md) documents. **Binders**
share that same universality but resolve to a route Lucernex's own internals name "Committee
Packages" (`PECommPkg.jsp`) — and an exhaustive search of all 223 objects in
[`../../data-model/object-catalog.md`](../../data-model/object-catalog.md) finds **no** `Binder`,
`Committee`, or similarly-named object anywhere. This is the module's single largest open question:
either the backing object exists under a name this pass did not think to search for, or the feature
is assembled dynamically over existing `Document`/`Folder` rows with no dedicated persistent record
of its own. [`data-model.md`](data-model.md#3-binders-have-no-backing-object) has the full argument.

## What exists, and what doesn't, behind each headline capability

| Capability visible in the UI/navigation | What backs it in the schema |
|---|---|
| Document storage, folders, checkout, versioning | `Document` (23 fields) + `Folder` (16 fields) — genuinely substantive |
| Document markups (`Document.HasMarkups`) | `DocumentMarkup` — a 1-field stub; markup content itself is not represented anywhere available to this pass |
| Version history (`Document.Version`/`.IsLatestVersion`) | Present as flags, but **no explicit FK groups successive versions of the same file together** — `Folder`, by contrast, does have an explicit self-reference (`PreviousFolderID`) for its own history |
| Per-folder security | `FolderSecurity` — a genuine 3-field record (folder × user class × security type) |
| Folder templates | `FolderTemplate` is a 1-field stub; the real metadata (name, description, entity-type attachability) lives on the `firm_global` `VirtualTemplateFolder` |
| Inbound correspondence | `EMailReceivedLog` (15 fields) — substantive, and its attachments are promoted into ordinary `Document` rows via `LinkEMailReceivedLogDocument` |
| Outbound correspondence | `EMailSentLog` — a 1-field stub; essentially unmodelled |
| Binders / Committee Packages | **No object found anywhere in the 223-object census** |

## Applying a template touches folder, budget, and task templates in one event

**Non-obvious finding:** `FolderTemplateAudit` (18 fields) is not narrowly about folders — it
carries `EntityTemplateID`, `FolderEntityTemplateID`, `BudgetEntityTemplateID`, and
`TaskEntityTemplateID`, all four resolving to `EntityTemplate` in `platform-tenancy`
([`../../mindmap/edges.json`](../../mindmap/edges.json)). Applying a template package to a new
entity is one audit event spanning folder structure, budget, and schedule/task templates together —
this module owns only one slot of a shared, cross-cutting templating mechanism. `DOC-R-009`.

## What a rebuild must not get wrong

1. **Do not assume `DocumentMarkup`'s schema shape can be ported.** It is a 1-field stub; markup
   annotation data has no home in any source available to this documentation pass. `DOC-R-010`.
2. **Do not assume `Binders` can be built from an existing Lucernex object.** None was found. Confirm
   its actual backing store by opening the live screen before designing an equivalent.
3. **Do not read `FolderTemplate` for what a folder template actually is.** Its metadata lives on
   `VirtualTemplateFolder`. `DOC-R-007`.
4. **Do not assume document version lineage is queryable by FK.** `Document.Version`/
   `.IsLatestVersion` exist; the column that would group versions of one file together does not.
   `DOC-R-005`.
5. **Do not build outbound correspondence tracking by analogy to inbound.** `EMailReceivedLog` is
   rich; `EMailSentLog` is a stub. There is nothing to port for the sent side.
6. **Applying a template touches three template types in one event, not one.** A rebuild's template-
   application audit trail should account for folder, budget, and task templates together if it
   wants the same single-event semantics. `DOC-R-009`.

## Contents

| Document | Answers |
|---|---|
| [`data-model.md`](data-model.md) | Every object, the stub-object finding in full, the Binders gap, the template-audit cross-reference, and the correspondence asymmetry. |
| [`rules.md`](rules.md) | `DOC-R-001`…`DOC-R-011` — every rule in trigger/input/effect/confidence form. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What exists (nothing), what must be built, what should deliberately differ, and the decisions blocking a build. |

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **What object, if any, actually backs "Binders"/"Committee Packages"?** The single biggest gap in
   this module.
2. **Where does markup annotation content actually live**, if not in `DocumentMarkup`?
3. **How are successive versions of the same logical document actually grouped**, given no explicit
   FK exists for it?
4. **Is outbound correspondence tracking a genuine product gap or an export artefact?**
5. **What does `FolderTemplateAudit.CodeFolderActionIDList` actually record?**
