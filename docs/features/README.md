# Feature areas — the product, one capability at a time

**Stated up front.** This folder documents Lucernex as a **product manual**: what each feature is,
every screen and route, every configuration surface, and the data model behind it. It is the
complement to [`../modules/`](../modules/), which is organised by *domain concept*, and to
[`../data-model/`](../data-model/), which is organised by *schema*. Where a fact belongs in an
existing module document it stays there and is cross-linked, not copied.

**Scope is measured, not asserted.** [`../COVERAGE.md`](../COVERAGE.md) enumerates all 744 known
surfaces — 141 navigation nodes, 57 admin tools, 93 page layouts, 227 sql tables, 207 drop-downs,
13 workflows, 6 form types — and reports for each whether a document owns it. Read it before
assuming an area is covered.

## Written

| Area | What it settles | Biggest open question |
|---|---|---|
| [**required-and-validation**](required-and-validation/) | **At least three, probably four independent sources of required-ness** — and the column flag and the catalog flag are **two obligations, not one**: they disagree on 44 fields in both directions, so collapsing them loses 44 obligations. The red asterisk is a third whose storage is unresolved with one candidate left under test; `Show and Require` is a fourth that is **used zero times** | Where per-placement required-ness is stored |
| [**page-layouts**](page-layouts/) | Navigation layouts and firm layouts are **disjoint id populations**; SEP/SUB/LIST composition; the publish-and-fork model (80 shared names, 0 shared ids); layouts carry **action buttons**, not just fields | How the runtime picks between 5 layouts on one navigation node |
| [**equipment-contracts**](equipment-contracts/) | BBW's fifth root, all 32 nodes with ids. `Contract` minus the retail layers; the whole ASC 842 engine kept. **No `EquipmentContract` table exists** in any inventory | Whether it stores in `Contract` under `ProjectEntityTypeName` |
| [**workflows-forms**](workflows-forms/) | **Corrects** the 1:1 Form↔Workflow claim — true in AF, false in BBW (4 of 13 match). Versioning is by **name suffix**. Two JavaScript escape hatches | Which `Lease Admin Request` variant is live |
| [**drop-downs-code-tables**](drop-downs-code-tables/) | 207 identical code tables, **134 of them empty**. `delete` is gated by a server-supplied `isReadOnlyRecord`, **not** a reference count — and the flag **changed across a build upgrade**, which corrects two claims in `data-model/code-table-registry.md`. Also: **dependent drop-downs** exist, via `CustomCodeField.ParentCustomCodeFieldID` | Whether `isReadOnlyRecord` marks provenance — one BBW value sweep settles it |
| [**custom-lists**](custom-lists/) | A Custom List is a **mini record type**, not a picklist — and **a Form without the workflow**, differing only by `CodeIssueType.IsWorkFlow`. Attachability is 11 boolean columns including `IsValidForEquipContract` | Whether list values are real columns on `ClientListRow` or EAV in `SubValue*` |
| [**data-fields**](data-fields/) | **205 firm custom fields, 0 physical columns** — 147 of them CAM clauses on `Contract`. Definitions are RGAF rows (`IsGlobal` + `FirmID` + `IsClientExtensionField`); the **value store is unidentified**. Three inventories of the schema, none complete, union **254 tables** | Where firm custom field *values* are written |

| [**import-export**](import-export/) | **Four inbound paths**, not one: generic XML bulk import (`POST /rest/firm`), document import, vendor-lease adapter pipeline, and the **Atlas (RocketClub) AI lease-abstraction API**. `BOMapClientRecordID` **confirmed** as the upsert key. No generic export endpoint exists | What the four admin screens actually offer |
| [**search-filtering**](search-filtering/) | Three separate mechanisms: per-placement list config in `JSONConfigText` (paging, totals, inline edit, **`IncludeInSearch`**), unused layout-level run-mode filters, and a **FIQL** API query surface with mandatory field selection | Everything runtime — filter menus, saved filters, quick search |

| [**administration**](administration/) | **All 57 admin tools classified with routes** — 55 screenshotted, 22 with an owning doc. `Import Data` and `Export Configuration` are one "Messenger" subsystem; Firm and Client Drop Downs are **two registries**, not two views; `Job Log` and `Report Log` are one screen | The five financial reference-data tools, then `Manage Security` |

| [**reference-data**](reference-data/) | The five reference tables. **Four of five are empty in BBW** — including the **discount-rate table, while the ASC 842 engine runs**. CPI holds 3,683 rows of one BLS series. The fiscal calendar supports **4-4-5 and 13-period retail years** and extrapolates past the last defined year | Where the ASC 842 discount rate actually comes from |

| [**security-access**](security-access/) | Four securable kinds — pages, **70 action verbs**, **6,553 fields**, budget columns — on a `NoAccess`/`View`/`Edit`/`Delete`/`Default` ladder per user class. **Read-only is `View` on a field**, which withdraws an anomaly the corpus had been treating as one. And it **refutes** the three-gate explanation of the Equipment Contract puzzle: all three gates are open at AF and the root still hides | What actually suppresses a navigation root — it must explain `Program` too |

## Not yet written

Listed so nothing is silently dropped. Evidence already in the repository is named, so the next
pass starts from data rather than from the browser.

| Area | Evidence in hand | Blocked on |
|---|---|---|
| **contracts** | Deep coverage already in [`../modules/contracts/`](../modules/contracts/) — this area should be a screen-and-route manual over it, not a second analysis | Nothing |
| **accounting-asc842** | [`../modules/accounting/`](../modules/accounting/), incl. 666 fields classified INPUT/COMPUTED/CODE-TABLE | Nothing |
| **expense-recovery-cam**, **variable-rent**, **payments** | Documented inside [`../modules/contracts/`](../modules/contracts/) | Nothing |
| **facilities-locations**, **portfolio** | [`../modules/facilities-locations/`](../modules/facilities-locations/), [`../modules/portfolio-transactions/`](../modules/portfolio-transactions/) | Nothing |
| **reporting**, **documents** | [`../modules/reporting/`](../modules/reporting/), [`../modules/documents-folders/`](../modules/documents-folders/) | Nothing |

## Conventions

Every document here follows [`../CONVENTIONS.md`](../CONVENTIONS.md): a **stated up front**
paragraph giving the conclusion before the evidence, every claim labelled **Observed** / **Derived**
/ **Inferred** with its source, tables over prose, real field and table names in `code`, and an
`## Open questions` section instead of a guess. Nothing is invented; where a fact is missing it is
written down as missing.
