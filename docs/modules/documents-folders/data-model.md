# Documents, Folders & Correspondence — data model

**Stated up front.** Ten objects, 99 fields, and the field counts alone reveal the module's real
shape: **four of the ten objects are near-empty stubs** (`DocumentMarkup` and `EMailSentLog` at 1
field each, `FolderTemplate` at 1 field), while the substantive content sits in `Document` (23),
`FolderTemplateAudit` (18), `Folder` (16), `VirtualTemplateFolder` (16), and `EMailReceivedLog` (15).
**The stubs are not a documentation gap — they are what the schema export actually contains.** A
document can be flagged `HasMarkups = true` on the `Document` record, but the markup content itself
lives on an object with exactly one field (`ProjectEntityID`); a document's checkout, version, and
release-state metadata is rich, but the *mechanism* linking successive versions of "the same"
document into one lineage is not an explicit column anywhere in this module (§2.3); and the whole
navigation-visible **"Binders"** feature — present on every `ProjectEntity` root in
[003](../../screens/003-main-navigation.md), routed to its own JSP
(`CommitteeDocuments/PECommPkg.jsp`, internally "Committee Packages" per
[`../../data-model/screen-routing.md`](../../data-model/screen-routing.md)) — **has no backing
object anywhere in the 223-object census** (§3). This module documents what the schema shows and is
explicit, throughout, about what it does not.

Source: `_lucernex_objects_summary.txt` (**Observed**, field lists reproduced below), cross-checked
against [`../../mindmap/edges.json`](../../mindmap/edges.json) (**Derived** FK resolution).

## 1. The object roster

| Object | PG table | Fields | Role | In/Out | Notes |
|---|---|---:|---|---:|---|
| `Document` | `document` | 23 | `entity_scoped` | 0 / 10 | The file-metadata record — author, checkout lock, version, release gate. |
| `DocumentMarkup` | `document_markup` | 1 | `entity_scoped` | 0 / 1 | **A stub.** Only field: `ProjectEntityID`. Markup content itself is not captured in this export — see §2.1. |
| `Folder` | `folder` | 16 | `entity_scoped` | 0 / 7 | The container `Document` rows live in. Self-references via `PreviousFolderID`. |
| `FolderSecurity` | `folder_security` | 3 | `entity_scoped` *(no `ProjectEntityID`; see below)* | 0 / 3 | Per-folder security by user class — `CodeFolderSecurityTypeID` × `CodeUserClassID` × `FolderID`, nothing else. |
| `FolderTemplate` | `folder_template` | 1 | `entity_scoped` | 0 / 1 | **A stub.** Only field: `ProjectEntityID`. Its own metadata (name, description, which entity types it applies to) lives on `VirtualTemplateFolder` instead — see §2.2. |
| `FolderTemplateAudit` | `folder_template_audit` | 18 | `entity_scoped` | 0 / 7 | Records when a template package — folder **and** budget **and** task templates together — was applied to a new entity. See §4. |
| `VirtualTemplateFolder` | `virtual_template_folder` | 16 | `firm_global` | 0 / 12 | Read-only projection of `FolderTemplate` metadata, carrying the 11 `IsValidFor*` attachability flags. |
| `EMailReceivedLog` | `e_mail_received_log` | 15 | `entity_scoped` | 0 / 3 | A logged inbound email — sender, subject, body, arrival date, attachment count. |
| `EMailSentLog` | `e_mail_sent_log` | 1 | `entity_scoped` | 0 / 1 | **A stub.** Only field: `ProjectEntityID`. Outbound correspondence has essentially no captured structure — a real asymmetry against `EMailReceivedLog`'s 15 fields; see §5. |
| `LinkEMailReceivedLogDocument` | `link_e_mail_received_log_document` | 5 | `entity_scoped` | 0 / 3 | Joins a received email to the `Document` row(s) created from its attachments. |

**`FolderSecurity` carries no `ProjectEntityID` at all** — its three columns are
`CodeFolderSecurityTypeID`, `CodeUserClassID`, and `FolderID`. It is scoped entirely through the
`Folder` it secures, not independently to any `ProjectEntity`. **Observed**, exhaustive field-list
read.

## 2. What the stub objects mean for a rebuild

### 2.1 `DocumentMarkup` does not capture markup content

**Observed:** `DocumentMarkup`'s entire field list, per `_lucernex_objects_summary.txt`, is
`ProjectEntityID(Entity ID)` — one column. `Document.HasMarkups` (boolean) is the only signal on the
`Document` record itself that markups exist. **Whatever markup data the live product actually
stores — annotation positions, redline shapes, colors, page numbers, authorship — is not represented
in this schema export at all.** Two readings are both plausible and neither is confirmed: (a) markup
data is held by a third-party document-viewer/annotation service outside Lucernex's own relational
schema and only a boolean flag is mirrored back, or (b) the export tool that produced
`_lucernex_objects_summary.txt` failed to enumerate `DocumentMarkup`'s real columns. **This
materially changes what "build document markups" means for ASG Edge+** — it is not a matter of
copying a few columns; the data model for markups does not exist in any source available to this
documentation pass.

### 2.2 `FolderTemplate` is a stub; `VirtualTemplateFolder` carries the real metadata

**Observed:** `FolderTemplate`'s only field is `ProjectEntityID`. The template's actual name,
description, and entity-type attachability live on the separate, `firm_global`
`VirtualTemplateFolder` object (16 fields: `TemplateID`, `TemplateName`, `Description`, `Notes`, plus
11 `IsValidFor*` booleans). This mirrors exactly the `VirtualTemplateBudget`/`VirtualTemplateSchedule`
pattern [`../../data-model/project-entity.md`](../../data-model/project-entity.md) §1.4 documents for
budget and schedule templates — a read-only projection carrying the descriptive metadata, sitting
beside a thin, almost-empty "real" template object. **Derived:** this is consistent product-wide
plumbing, not something specific to folders; a rebuild should treat `VirtualTemplateFolder`'s field
list as the authoritative shape of "what a folder template is," not `FolderTemplate`'s.

**The 11 `IsValidFor*` flags** (`IsValidForCapProgram`, `IsValidForCapProject`,
`IsValidForContract`, `IsValidForEquipContract`, `IsValidForFacility`, `IsValidForLocation`,
`IsValidForOpenProject`, `IsValidForParcel`, `IsValidForPortfolio`, `IsValidForPotentialProject`,
`IsValidForPrototype`) are the identical eleven-subtype enumeration
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §1.4 documents — a folder
template declares which `ProjectEntity` subtypes it may be applied to, exactly as a Form/Issue type
does. **Observed**, field list.

### 2.3 Document versioning has no explicit lineage column

**Observed:** `Document.Version` (a number) and `Document.IsLatestVersion` (a boolean) both exist,
but **no column anywhere in `Document`'s 23 fields groups successive versions of the same logical
file together** — there is no `PriorVersionDocumentID`, no `DocumentFamilyID`, nothing of the kind.
**Derived, and this is a real ambiguity, not a settled fact:** the only plausible grouping key
visible from the schema is matching `BaseName` within the same `ParentFolderID`, which is an
inference from field names, not an explicit relationship. Contrast this directly with `Folder`
itself, which **does** carry an explicit self-referencing `PreviousFolderID` for its own history —
the schema is internally inconsistent about whether "history of a record" is modelled with an
explicit link (`Folder`) or left implicit (`Document`).

## 3. "Binders" have no backing object

**Observed**, exhaustively: no object named `Binder`, `Committee`, `CommitteePackage`, or anything
resembling either appears anywhere in the 223-object census
([`../../data-model/object-catalog.md`](../../data-model/object-catalog.md)). Yet
[003](../../screens/003-main-navigation.md) shows `Binders` as a universal tab on every
`ProjectEntity` root, routed to `/en/CommitteeDocuments/PECommPkg.jsp` — internally, per
[`../../data-model/screen-routing.md`](../../data-model/screen-routing.md), **"Committee Packages."**
**This is the single largest gap in this module: a real, universally-available end-user feature with
no discoverable schema object behind it in any source available offline.** Two explanations are
possible and neither is confirmed: the underlying table exists but under a name unrelated to
"Binder"/"Committee" that this pass did not think to search for, or the feature is built on document/
folder infrastructure dynamically assembled at render time with no dedicated persistent record at
all (a "binder" could, in principle, be nothing more than a saved query over existing `Document`
rows). Opening the screen directly is the only way to resolve this — see Open Questions.

## 4. A folder template application is one audit event across three template types

**Observed**, `FolderTemplateAudit`'s 18 fields: `EntityTemplateID`, `FolderEntityTemplateID`,
`BudgetEntityTemplateID`, and `TaskEntityTemplateID` — all four typed `Template ID`, all four
resolving to `EntityTemplate` in `platform-tenancy`
([`../../mindmap/edges.json`](../../mindmap/edges.json)) — plus `CopyFolderStructure` (boolean),
`AppliedDate`, `ScheduleStartDate`/`ScheduleEndDate`, and `CodeFolderActionIDList`.

**Derived:** applying "a template" to a newly-created entity is not three independent actions in
this schema — it is **one audit row** that can simultaneously reference a folder template, a budget
template, and a task/schedule template, plus record whether the folder structure was actually
copied and over what schedule window. This corroborates, from the documents side,
[`../../data-model/project-entity.md`](../../data-model/project-entity.md)'s general point about
`EntityTemplate`/`TemplateAudit` being shared, cross-cutting platform infrastructure rather than a
per-module concern — this module owns only the `FolderEntityTemplateID` slot of a larger, shared
templating event.

## 5. Correspondence is asymmetric: inbound is modelled, outbound almost isn't

**Observed:** `EMailReceivedLog` carries 15 real fields — `Sender`, `Subject`, `Body`,
`ArrivalDate`, `IsCritical`, `NumberOfAttachments`, `MailServiceEventID`. `EMailSentLog` carries
**one** field, `ProjectEntityID`. `LinkEMailReceivedLogDocument` (5 fields:
`EMailReceivedLogID`, `DocumentID`, plus `ProjectEntityID`) is the join that promotes a received
email's attachments into ordinary `Document` rows in the standard `Folder` hierarchy — inbound
correspondence and document storage share one system by construction, but there is no equivalent
`LinkEMailSentLogDocument` and no equivalent structure for what was sent, to whom, or with what
content. **Derived:** this asymmetry is either a genuine product gap (the vendor never built out
sent-mail tracking to the same depth) or an export/capture artefact; either way, a rebuild should not
assume outbound correspondence can be ported from this schema — it would have to be designed fresh.

## 6. Cross-module edges

**Observed** ([`../../mindmap/edges.json`](../../mindmap/edges.json)). Every object in this module
carries the standard audit pair to `Member` and its own `ProjectEntityID`/`FolderID`-based scoping.
The two internal edges are `LinkEMailReceivedLogDocument.DocumentID → Document` and
`.EMailReceivedLogID → EMailReceivedLog`. Inbound from other modules — **16 edges, but the shape is
one relationship repeated**: `Document`/`Folder` are referenced as a generic attachment pair
(`AssociatedDocumentID`/`FolderID`) from `PaymentTransaction`, `LandlordInvoice`, `Covenant`,
`ContractFinancialTest`, `FacilityExpense`, `ParcelAccess` (accounting, contracts-leases,
facilities-locations) and from `ExpenseRecoveryItemMapping.DocumentID` (expense-recovery) and
`DemographicResults.DocumentID` (facilities-locations) — i.e., "attach a supporting document/folder
to this record" is a generic capability nearly every financial and operational record in the
product uses, not something specific to any one of them.

## 7. Confidence summary

| Claim | Label |
|---|---|
| `DocumentMarkup`, `EMailSentLog`, `FolderTemplate` are 1-field stubs in this export | **Observed**, exhaustive field-list read |
| Markup *content* is not represented in any source available to this pass | **Derived** — absence, two unconfirmed explanations offered |
| `VirtualTemplateFolder`, not `FolderTemplate`, carries the real template metadata | **Observed**, field-list comparison |
| No `Binder`/`Committee` object exists anywhere in the 223-object census | **Observed**, exhaustive |
| A template application spans folder + budget + task templates in one audit row | **Observed**, field list + `edges.json` resolution to `EntityTemplate` |
| Outbound correspondence is essentially unmodelled versus inbound | **Observed**, field-count comparison |
| Document version lineage has no explicit FK | **Observed**, absence in the 23-field list |

## Open questions

Ranked by how much each blocks a rebuild decision.

1. **What object, if any, actually backs the "Binders" / "Committee Packages" feature?** The single
   biggest gap in this module — a universally-navigable feature with no discoverable schema object.
   Opening `/en/CommitteeDocuments/PECommPkg.jsp` directly is the only way this pass could not
   resolve it further.
2. **Where does markup annotation content actually live**, if not in `DocumentMarkup`? Determines
   whether ASG Edge+'s markup feature (if built) needs its own new data model from scratch (almost
   certainly yes) or can port anything from Lucernex.
3. **How are successive versions of the same logical document actually grouped**, given no explicit
   FK exists? Confirming whether it is `BaseName` + `ParentFolderID` matching, or something else
   entirely, would settle §2.3.
4. **Is outbound correspondence tracking a genuine product gap, or an export artefact?** If genuine,
   ASG Edge+ needs to decide whether sent-mail tracking is in scope at all, since Lucernex offers no
   model to draw from.
5. **What does `CodeFolderActionIDList` on `FolderTemplateAudit` actually record** — which folder
   actions (create/copy/skip?) were taken when the template was applied?
