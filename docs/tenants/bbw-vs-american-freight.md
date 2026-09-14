# A second tenant: `(ASG)BBW` compared with `(ASG)American Freight`

**Stated up front.** The four end-user navigation roots are **byte-for-byte identical** between the
two tenants — same groups, same screens, same order. BBW adds a **fifth root, `Equipment Contract`**,
which American Freight does not have: a parallel lease aggregate carrying the **whole ASC 842 /
IFRS 16 / straight-line engine** but with every retail-real-estate financial layer stripped out.
That single difference is the most useful thing this tenant has to say, because it is the vendor
drawing the line between *generic lease accounting* and *retail property management* — the exact line
ASG Edge+ has to draw for itself.

**Three open blockers moved.** #2 (contract lifecycle) closed, and corrected the old single-tenant
reading. #5 (the workflow `Task` step) half closed — the vocabulary is settled, but 62 configured
steps across 13 templates contain **not one** Task step, which reframes the question. #1
(`conditionalFieldsConfig`) did not close, but now has a validated sweep method and a caught false
negative. BRD-24's eight `Lease Admin Request` steps and the two abstraction workflows are
**observed for the first time**.

| Property | Value |
|---|---|
| Tenant | `(ASG)BBW`, `firmID=3159` |
| Route | `https://train-bbw.lucernex.com` |
| Build | **`26.09.0.113`** (2026/09/11 19:23) — American Freight was `26.08.0.46` |
| Captured | 2026-09-13, footer showed 2026-09-12 Central Standard Time |
| User | Test 2 User (signed in by the repository owner; no credential was handled by the agent) |
| Exploration mode | **Read-only.** No record, layout, drop-down, workflow or rule was created, edited, saved or deleted. No `Save` button was clicked. All writes avoided; every probe was a `GET`. |
| Navigation data | [`../mindmap/navtree-bbw.json`](../mindmap/navtree-bbw.json) — 141 nodes, re-captured with `entityType` intact. The `jsp` column is still empty: `href` is populated lazily per node by the Ext store and is absent until a node is expanded, so routes must be harvested from the rendered menu rather than the store |
| Conditional-rule sweep | [`bbw-conditional-sweep.json`](bbw-conditional-sweep.json) — 157 targets |
| Workflow steps | [`bbw-workflow-steps.json`](bbw-workflow-steps.json) — 13 templates, 62 steps. **Approver identities deliberately omitted** — they are real individuals; only `approverCount` is recorded |

---

## 1. The navigation tree — four roots identical, one root added

**Observed.** Read out of the `Lx.ui.MenuTree` ExtJS component (`Ext.getCmp('lxuimenutree-1029')`),
the same component and method used for American Freight, so the two are directly comparable.

| Root | AF groups | BBW groups | AF screens | BBW screens |
|---|---:|---:|---:|---:|
| Portfolio | 6 | 6 | 14 | 14 |
| Location | 4 | 4 | 12 | 12 |
| Facility | 7 | 7 | 17 | 17 |
| Contract | 6 | 6 | 39 | 39 |
| **Equipment Contract** | — | **5** | — | **26** |
| **Total** | **23** | **28** | **82** | **108** |

**Observed.** A name-for-name set difference over the four shared roots returns **empty in both
directions**. Not one group or screen differs. The end-user surface is platform-defined, not
firm-configured — which is a load-bearing fact for the Hub/Spoke design: navigation belongs in the
Hub.

## 2. `Equipment Contract` — the vendor's own generic/specific split

**Observed.** The new root (`PageLayoutID=41087`) mirrors `Contract` and then subtracts. Derived
diff of the two subtrees:

| Group | Contract | Equipment Contract | Dropped |
|---|---:|---:|---|
| Details | 7 | 5 | `Binders`, `Schedule` |
| Abstract Info | 8 | 7 | `Co-Tenancy` |
| Payment Info | 12 | 7 | `Recurring Expenses`*, `Alternate Rent`, `Invoices`, `Recoveries`, `Percentage Rent`, `Sales` |
| Accounting Info | 7 | 6 | `Capital Lease Test` |
| **Accrual Info** | **4** | **absent — whole group** | `Accrual Details`, `Expense Accruals`, `Transactions`, `Percentage Rent Accruals` |
| Reports | 1 | 1 | renamed to `Equipment Contract Reports` |
| **Total** | **39** | **26** | |

\* `Recurring Expenses` is **renamed** to `Recurring Payments`, not dropped — equipment pays rent, it
does not recover expenses.

**What survives untouched** is the whole accounting engine: `Straight-Line Rent`,
`Accounting Assumptions`, `ASC 842 Test`, `ASC 842 Rent Schedule`, `IFRS 16 Rent Schedule` — plus
`Terms`, `Amendments`, `Covenants`, `Key Dates`, `Responsibilities`, `Insurance`,
`Security Deposit`, `Allowances`, `Scheduled Offsets`, `Transactions`, `Receipts`.

**Why this matters (Derived).** Everything dropped is retail-property-specific: co-tenancy is a mall
clause; recoveries/CAM is landlord expense pass-through; percentage rent and sales are turnover rent.
Everything kept is generic to any lease under ASC 842. This **confirms by construction** the finding
in [`modules/assets-equipment/equipment-leases.md`](../modules/assets-equipment/equipment-leases.md)
that the lease-accounting engine runs per equipment asset and not only per property lease — there the
evidence was three nullable foreign keys to `Asset`; here the product exposes it as a first-class
navigation root with its own 26 screens.

**One dropped item is not real-estate-specific and deserves a question.**
`Capital Lease Test` is retained for `Contract` but dropped for `Equipment Contract`, while
`ASC 842 Test` is kept for both. See open question Q-BBW-02.

## 3. Contract lifecycle — closed; and a retraction

**Observed.** `Contract Status Code` is `TableType=2094`. Both tenants carry the same three values —
`Active`, `AI Abstracted`, `Inactive` — confirming the three-value set is not an American Freight
peculiarity.

### Retraction: the reference-count reading was wrong

An earlier revision of this document inferred, from a single difference in row actions between the
two tenants, that **`delete` is suppressed when a code-table value is referenced** — and argued that
this meant Lucernex already performs the "Where Used" check that ASG Edge+'s **D-07** ruled out of
scope, and that **MST-015** should therefore be reopened. **That inference is withdrawn. It was
wrong, and the argument built on it should not be acted on.**

Two pieces of evidence retired it.

**1. The difference was a build difference, not a tenant difference.** American Freight has since
been upgraded from `26.08.0.46` to **`26.09.0.113` — the same build BBW runs**. On that build,
`AI Abstracted` at AF now offers **edit only**, exactly as at BBW. The AF/BBW asymmetry the inference
rested on no longer exists.

**2. The mechanism is a per-row boolean, read directly from the renderer.** The Actions column
(`EditDeleteLink`) renderer reads, verbatim:

```js
var q = c.data.isReadOnlyRecord;
if (!q) { /* edit | delete */ } else { /* edit only */ }
```

**Observed.** There is no count, threshold, or usage lookup anywhere in the render path.
`isReadOnlyRecord` is supplied per row by the server; the `FirmCode` record exposes only four fields
(Name, Description, Inactive, Available-for-Portfolios) and no provenance or reference-count
attribute. What sets the flag is **not observable from the client**.

The decisive case: `TableType=3006` (`Key Date Type Code`) contains **two rows both named `Option`** —
`LxBOID 3095` protected, `LxBOID 3116` deletable. **Identical name, opposite flag: the flag tracks the
row, not the value's meaning or its usage.** A reference count could not produce that. Nor could it
produce `TableType=2157` (`Covenant Status Code`), where `Active` is deletable while `AI Abstracted`
is protected — the exact inversion of a usage-based rule.

**Full scan (Observed):** all 207 TableTypes at AF, zero scan errors — 73 tables hold values, 134 are
empty, **1,140 values total: 154 protected, 986 deletable**; 23 tables all-protected, 38
all-deletable, 12 mixed. Data in [`af-code-table-actions.json`](af-code-table-actions.json).

**Best current reading (Inferred, not proven):** `isReadOnlyRecord` marks **platform-seeded rows**,
which a firm may rename but not delete, against firm-added rows which it may delete. It fits every
mixed table, including the duplicate-`Option` case. The discriminating test is whether the same
`LxBOID` ever carries a *different* flag in the two tenants — if it does, provenance is disproved.

**What ASG Edge+ should take from this:** the platform does protect seeded values from deletion, and
a rebuild needs that notion — which still bears on `D-07` and `DeactivationPolicy`. But it is **not**
evidence of a Where-Used capability, and **MST-015 remains unsupported by anything observed here.**

## 4. Workflows — 13 templates, 62 steps, and not one `Task` step

**Observed.** `/en/workflow/WorkFlowTemplateEdit.jsp` lists **13 workflow templates** against
American Freight's **4**. Step lists were read out of the grid store's `expandedHtml` field — the
steps are already loaded client-side, so no template had to be opened in edit mode. Full data,
with approver identities omitted, in [`bbw-workflow-steps.json`](bbw-workflow-steps.json).

| Template | ID | Steps | Note |
|---|---:|---:|---|
| ASC 842 Tracking | 2475 | 2 | |
| Cotenancy Update | 2478 | 2 | |
| **Implementation Workflow - Document Abstraction** | 2401 | **2** | BRD-24 PJ-05/PJ-06 |
| **Implementation Workflow - Financial Abstraction** | 2402 | **6** | BRD-24 PJ-04 |
| **Lease Admin Request** | 2472 | **8** | current; BRD-24 |
| Lease Admin Request v1 | 2399 | 8 | *"archived and replaced on 09.22.25"* |
| Lease Admin Request v2 | 2468 | 10 | *"archived and replaced on 03.26.26"* |
| Lease Date Review | 2473 | 2 | |
| Lucernex Change Request | 2469 | 6 | current |
| Lucernex Change Request v1 | 2463 | 5 | *"archived and replaced on 10.02.25"* |
| User Request | 2400 | 2 | |
| Vendor Change (Notice) | 2461 | 4 | |
| Vendor Changes (Integration) | 2418 | 5 | |
| **Total** | | **62** | |

### The `Task` step: offered everywhere, used nowhere

This **corrects the optimistic reading in the first pass of this document.** Open blocker #5 said
*"no `Task` step exists in this tenant, so half the workflow step model is unobserved."* After BBW:

- **Observed.** The step-type vocabulary is confirmed. Every template row carries
  `edit | delete | add task step | add form step`, and the task link builds a URL with a literal
  `&StepType=Task` parameter (`popupFormEditWorkFlowTemplateStep(..., "&StepType=Task&WorkFlowTemplateID", 2401)`).
  So `Task` and `Form` are the two step types, named in the product's own code.
- **Observed.** Across **all 13 templates and all 62 steps, the `Type` column reads `Form`. Every
  time. There is not one `Task` step in this tenant either.**

So blocker #5 is **half closed and half worse**. The vocabulary is settled; the behaviour of a Task
step is still completely unobserved — and now across two tenants and 62 steps, which shifts the
reading. The likeliest explanation (**Inferred**) is that ASG's configuration simply does not use
Task steps at all. That is decision-relevant in itself: the rebuild may not need the concept, and
somebody should confirm that with the business rather than build it on spec. See Q-BBW-03.

### The step model, as observed

**Observed.** Every step row has the columns
`Step | Step Name | Form/Task | Type | Approval Level | Approver`.

- `Type` — only value seen across 62 steps: **`Form`**
- `Approval Level` — only two values seen: **`Member`** and **`Ad Hoc`**
- `Approver` — where `Approval Level = Member`, a list of **named individuals**; where `Ad Hoc`, empty

**Routing is to named people, not to roles or positions.** This qualifies the workflow module's
finding that *"routing is by organisational position, not by name"* — that holds for the
`WorkFlowTemplate` routing model, but every approval level actually configured at BBW resolves to an
explicit list of named members. A rebuild that routes only by position will not reproduce this
tenant's configuration. Their identities are deliberately not recorded in this corpus.

### The abstraction workflow, finally observed

The two `Implementation Workflow` templates are the first direct evidence anywhere in this corpus for
BRD-24's abstraction path, which was wholly unobserved at American Freight.

**Document Abstraction** (2 steps): `Abstract Lease Documents` → `Review Lease Abstract`.

**Financial Abstraction** (6 steps), and note the alternation:

| Step | Name | Approval Level |
|---:|---|---|
| 1 | Set up Recurring Expenses | Ad Hoc |
| 2 | Review Recurring Expenses | Member |
| 3 | Set Up Percent Rent | Ad Hoc |
| 4 | Review Percent Rent | Member |
| 5 | Set Up ASC 842 Schedules | *(none)* |
| 6 | Final Review of Financial Abstract | Member |

**Derived.** The pattern is **maker-checker pairs**: an `Ad Hoc` set-up step followed by a `Member`
review step, once per financial layer (recurring expenses, then percentage rent, then ASC 842
schedules), closed by a final review. Step 5 has **no approval level at all** — the ASC 842 schedule
set-up is the one financial layer with no paired reviewer, which given its materiality is worth
raising.

### `Lease Admin Request` — BRD-24's eight steps, observed

The atlas asserted that *"Lease Admin Request's 8 steps **are** BRD-24"* on the strength of the step
count. The steps themselves are now **Observed**, and there are indeed 8:

| Step | Name | Approval Level |
|---:|---|---|
| 1 | Initial Review of Lease Admin Request | Member |
| 2 | Abstract Lease Document | Member |
| 3 | ASG Review of Lease Abstract | Member |
| 4 | Client Review of Lease Abstract | Member |
| 5 | Finalize Lease Admin Request | Member |
| 6 | Finalize Lease Admin Request (Option) | Member |
| 7 | Complete Lease Admin Request | Member |
| 8 | Client Review of Estoppel | Member |

Two things to flag. **Steps 5 and 6 share one form** — both point at
`LAR Finalize Lease Admin Request(Approvers)` — so the same form is presented twice to different
approver groups, the second labelled `(Option)`. And **step 8, `Client Review of Estoppel`, points at
a form named `LAR Submit Lease Admin Request(Approvers)`** — the step name and its form name
disagree, which is either a configuration error or form reuse, and matters if the rebuild migrates
these definitions. **Inferred:** form reuse.

**Form naming is a convention, not a relation.** Forms are prefixed by workflow (`LAR ` for Lease
Admin Request, `IWF ` for the Implementation Workflows) and suffixed `(Approvers)`. Nothing enforces
it.

### Versioning is a naming convention, not a feature

**Observed.** The current template is the **unsuffixed** one; `v1` and `v2` are archived
predecessors. `Lease Admin Request` (8 steps) is current, while `v2` (10 steps) and `v1` (8 steps)
are retired — so **the current workflow has fewer steps than the version it replaced.** The archival
fact is recorded as **free text in the description field** ("Workflow has been archived and replaced
on 09.22.25"), not as a status, an effective-date range, or a supersession foreign key. A rebuild
needing auditable workflow versioning cannot copy this; it must model version, effective dates and
supersession as first-class fields.

### New `WorkFlowTemplate` fields, not previously documented

**Observed** from `WorkFlowTemplateEdit.jsp?formSubmit=viewBO` (read-only mode) on template 2401:

| Field | Value seen |
|---|---|
| `Notify the initiator when work flow is complete` | No |
| `Notify all prior assignees when work flow is complete` | No |
| `Notify all prior approvers when work flow is complete` | No |
| `Auto assign initiator as ad hoc assignee` | No |
| `Default Work Flow Priority` | `3 - Normal` (`DefaultWFCodePriorityID=3`) |
| `Process kicked off by:` | *"(work flow specified as kickoff action in another work flow)"* |
| `Conditional Workflow JS` | present as a field |
| `Available for the following Portfolios/Capital Programs:` | scoping list |
| `Enable Vendor Collaboration` / `Collaborator Job Titles` | No / `CollaboratorJobTitleIDList` |

Two of these are significant. **`Document Abstraction` is kicked off by another workflow, not by a
form** — workflows chain, which the corpus did not record. And **`Conditional Workflow JS`** implies
workflow-level conditional logic held as **JavaScript**, a second and completely separate rule
mechanism from the `conditionalFieldsConfig` of §6. Neither is documented anywhere in this corpus.

## 5. What is the same, and why that is informative

| Thing | AF | BBW | Reading |
|---|---:|---:|---|
| Firm Drop Downs | 207 | **207** | **Observed.** Identical count → the code-table registry is platform-defined (Hub), not firm-extensible in count |
| Nav groups/screens on shared roots | 23 / 82 | 23 / 82 | Platform-defined |
| `Contract Status Code` values | 3 | 3 | Platform-seeded plus the same tenant addition |
| ASG-built Summary page layouts | not counted | **15** | Firm-specific; PLIDs 98921–99140 |

## 6. Blocker #1 — not closed, but the method is now validated

The top open question is the **populated shape of `json.conditionalFieldsConfig`**. It is still open,
and here is exactly how far this session got.

**Observed.** All **15** ASG Summary page layouts were swept. **157 conditional targets** were found
and every one returned `<input type=hidden id='json.conditionalFieldsConfig' name='json.conditionalFieldsConfig' value='' />`
— an empty value. Full per-layout counts in [`bbw-conditional-sweep.json`](bbw-conditional-sweep.json).

**A false negative was caught and discarded, and the correction matters for reuse.** Fetching
`LayoutEditorAJAX.jsp` over HTTP and regexing the response returns **zero** conditional targets even
for a layout directly observed to have 22. The `conditionOptions(...)` calls are **injected
client-side after load**; they are not in the served HTML. Any future sweep must *render* the layout
(an iframe works, same-origin) and read the live DOM. The first sweep built this way reported
"0 populated of 0 targets" and was thrown away; the second reported 157 targets and is the one
recorded here.

**The validated method**, for reuse:

1. Render `LayoutEditorAJAX.jsp?formSubmit=editBO&popupEdit=true&buildLayout=true&PageLayoutID={id}`
   and poll the DOM until `conditionOptions(...)` calls appear.
2. For each, `GET`
   `/en/pagebuilder/ConditionFilterEx.jsp?&fieldKey={key}&CustomObjectDelID={hash}&ajax=true&pageLayoutID={id}&IsReportLayout=true`
   (`&IsIssueLayout=true` for form layouts).
3. Read `json.conditionalFieldsConfig` out of the response. No dialog rendering and no `Save` needed —
   the whole probe is a `GET`.

**Where to look next, and why it was not reached.** Only the **Summary Page** sub-system was swept.
`SummaryEntityPageLayoutEdit.jsp` takes `mode={SEP,SUB,LIST}`, so sub-page and list layouts are
unswept, and **Form (Issue) layouts were not swept at all** — which is the likeliest home for
conditional rules, since "show this field when…" is a request-form behaviour. With 13 workflow
templates and their form steps, BBW is a far better hunting ground than American Freight was.

## 7. The configuration inventory — 93 page layouts, not 15

**Observed.** Every admin grid exposes a bulk JSON endpoint:
`{page}.jsp?ajaxList=true&ajax=true&popupList=true&BOType={type}&start=0&limit=5000`, returning
`{totalCount, topics[]}`. That enumerates a whole screen in one request instead of paging 15 rows at
a time, and it is how the numbers below were taken. (`/servlet/BOList` needs a session-bound `fdName`
key and returns literal `null` without it — use the JSP route.)

| Screen | BOType | BBW total |
|---|---|---:|
| Manage Drop Downs | `CustomCodeTable` | **207** |
| Manage Summary Page (`mode=SEP`) | `PageLayout` | 15 |
| Manage Sub Pages (`mode=SUB`) | `PageLayout` | **32** |
| Manage List Pages (`mode=LIST`) | `PageLayout` | **46** |
| **All page layouts** | | **93** |
| Manage Custom Lists | `ReportGroupDataCustomList` | 6 |
| Work Flow Templates | `WorkFlowTemplate` | 13 |
| **Task Templates** | `TaskTemplate` | **0** |
| Process Timelines | `ProcessTimelineTemplate` | 0 |

Full data: [`bbw-page-layouts.json`](bbw-page-layouts.json), [`bbw-drop-downs.json`](bbw-drop-downs.json).

**This corrects §6 of this document.** The conditional sweep covered 15 layouts and reported 157
targets — but 15 is only the `SEP` sub-system. **78 of the 93 layouts were never swept.** The
"157 targets, all empty" result stands only for Summary Pages, and the sub-page and list layouts —
the likelier home for conditional rules — remain unexamined.

**`Task Templates = 0` explains §4.** There are no Task steps in any workflow because the tenant has
**no task templates at all**. The `Task` step type is real in the product's vocabulary and entirely
unused in ASG's configuration.

**Sub-pages are not navigable (Observed).** All 32 `SUB` layouts return no `ParentPageLayoutID`,
against 15/15 for `SEP` and 21/46 for `LIST`. Sub-pages attach to a parent layout; they are
composition units, not destinations.

**30 distinct primary tables** back the 93 layouts, including several the object catalog should be
checked against: `Expense Vendor Allocation`, `Allowance Transaction`, `Percentage Rent Breakpoint`,
`Sales Period`, `Expense Setup`, `Expense Schedule`, `Comparison Report Item`.

### The contract creation flow — found

The largest previously-identified gap was that **contract creation appears nowhere in the
navigation**: the 105-screen tree is navigation *within* a record that already exists. It is not in
the navigation because it is built from **sub-page layouts**:

| PLID | Layout | Primary table |
|---:|---|---|
| 98883 | **ASG Contract Wizard** | `Contract` |
| 98884 | ASG Contract Wizard Step 2 | `Contract` |
| 98885 | ASG Contract Wizard Step 3 | `Contract` |
| 98886 | ASG Contract Wizard Step 4 | `Contract` |
| 98887 | ASG Contract Wizard Step 5 | `Contract` |
| 99141 | ASG Facility Wizard | `Facility` |
| 99142 | ASG Location Wizard | `Location` |

**Observed:** a five-step contract creation wizard exists as five sub-page layouts, with parallel
single-step wizards for Facility and Location. **Their field contents are not yet captured** — the
layout builder must be rendered to read them, and the session expired before that ran.

### The Lease Abstract layout family

**Observed.** A distinct set of layouts, PLIDs in the 102xxx band (later than the 98xxx core), named
for abstraction rather than for navigation:

`ASG Lease Abstract - Contract Term` (102506) · `- Covenants` (102250) · `- Expense Schedule` (102251)
· `- Expense Setup` (102252) · `- Key Dates` (102266) · `- Percent Rent` (102109) ·
`- Funds and Expenses` (102629)

**Derived.** These match, one for one, the financial layers stepped through by the
`Implementation Workflow - Financial Abstraction` workflow in §4. Together with the two
`ASG Approval - *` list layouts (`Expense Schedules` 99146, `Transactions` 99147), this is the
abstraction pipeline's own UI — the BRD-24 PJ-04→PJ-09 path, in layouts.

One layout is named **`zdelete`** (102270, `Comparison Report Item`) — abandoned configuration left
in a live tenant, worth noting if these definitions are ever migrated wholesale.

## 8. Layouts are built on computed projections, not only on tables

**Offline analysis**, joining the 30 distinct `PrimaryCodeSQLTableName` values behind the 93 layouts
against [`../data-model/object-catalog.md`](../data-model/object-catalog.md). No tenant access needed.

**24 of 30 resolve to a catalog object by name.** The six that do not are the interesting ones:

| Layout's primary table | Resolves to | Reading |
|---|---|---|
| `Portfolio` | `Program` | **Display alias.** Confirms the atlas reading that "Portfolio" is `Program` |
| `Entity` | `ProjectEntity` | **Display alias** for the universal supertype |
| **`Percentage Rent Period`** | **`VirtualPercentageRentPeriod`** | a `Virtual*` computed projection |
| **`Sales Period`** | **`VirtualSalesPeriod`** | a `Virtual*` computed projection |
| `Straight-Line Schedule` | `SLSummary` / `SLPeriod` / `CodeSLSchedule` — **ambiguous** | three candidates, none an exact match |
| `Comparison Report Item` | `ComparisonItem` *(Inferred)* | only on the abandoned `zdelete` layout |

### Four layouts render objects that are not tables

**Observed.** These layouts name a `Virtual*` projection as their primary table:

| PLID | Layout | Mode | Primary table |
|---:|---|---|---|
| 98921 | ASG Breakpoint Schedule | **SEP** | `Percentage Rent Period` |
| 98934 | ASG Percent Rent Schedule | **SEP** | `Percentage Rent Period` |
| 98908 | ASG Contract Payment Details - Breakpoints | LIST | `Percentage Rent Period` |
| 98920 | ASG Contract Percent Rent - Schedule | LIST | `Sales Period` |

**Why this matters.** [`foreign-key-graph.md`](../data-model/foreign-key-graph.md) records that the 13
`Virtual*` objects have **no primary key and not one audit column** — "computed projections, not
tables." The corpus treats them as internal machinery. But two of them are the **primary table of
user-facing page layouts, two of which are top-level Summary Pages.**

For ASG Edge+ this is a direct design constraint, and it contradicts the natural assumption: **the
layout engine must be able to target a read-model or computed projection, not just an entity table.**
A rebuild that only permits layouts over persisted entities cannot reproduce the percentage-rent
breakpoint and sales-period schedule screens at all. It also means these screens are **inherently
read-only** — there is no key to write back to — which a layout engine has to model explicitly rather
than discover at runtime.

### One more oddity

`ASG ASC 842 Schedule` (98859) and `ASG SL Summary` (98873) declare **the same primary table**,
`Straight-Line Schedule`. The ASC 842 rent schedule screen and the straight-line summary screen
render the same underlying object through two different layouts — consistent with the atlas finding
that one engine serves three standards, but it means the standard is a *layout* distinction here, not
a data one.

## 9. The platform layer is seeded identically — proved by primary key, not by name

**Offline analysis.** Two cross-tenant joins, no tenant access required. Both are stronger than the
name-level comparison in §1 and §5, because they compare **identifiers**, not labels.

### Navigation: 109 of 109 nodes share the same `PageLayoutID`

**Observed.** Every node of the four shared roots — 4 roots, 23 groups, 82 screens — carries not
merely the same name in both tenants but the **same numeric `PageLayoutID`**. Zero differences across
109 nodes. `Contract : Details : Summary` is `PageLayoutID=3494` at American Freight and `3494` at
BBW; `Portfolio` is `924` in both.

### Drop downs: 207 of 207 share the same `TableType`

**Observed.** Joining [`bbw-drop-downs.json`](bbw-drop-downs.json) against the registry in
[`../data-model/code-table-registry.md`](../data-model/code-table-registry.md): **all 207 tables match
on both name and `TableType` id. Not one mismatch, and neither tenant has a table the other lacks.**
`Contract Status Code` is `2094` in both; `Issue Type Code` is `2035` in both.


### Page-layout ids share nothing — but the layouts themselves are the same set

**Observed.** American Freight has **88** page layouts (17 `SEP`, 31 `SUB`, 40 `LIST`) against BBW's
**93** (15/32/46). Joined on `(mode, PageLayoutID)`, **not one pair is shared.**

**That is not the whole story, and taken alone it misleads.** Joined instead on `(mode, name)`:

| Join | Result |
|---|---:|
| Shared `(mode, PageLayoutID)` | **0** |
| Shared `(mode, name)` | **80** |
| …of those 80, `primaryTable` mismatches | **0** |
| Only at AF | 7 (four are scratch: `TABLE`, `test` ×3) |
| Only at BBW | 12 |

*(87 and 92 distinct `(mode, name)` keys against 88 and 93 rows — both tenants carry the very same
duplicate, `LIST / ASG Contract Payment Details - Security Deposit`, twice.)*

**80 of ~87 layouts are the same layout, under the same name, over the same primary table, at a
different id.** The ids are not random either: `BBW_id − AF_id` clusters in a narrow band around
**+2626 … +2677**, the signature of a contiguous block reassigned when a layout set is copied into a
new tenant.

**Derived — and this replaces a wrong earlier reading.** An earlier revision took "zero shared ids"
to mean page layouts are independently firm-authored, and filed them under Spoke as unrelated
per-firm work. They are not unrelated. **ASG maintains one standard layout set and deploys a copy
into each client tenant, where it is re-keyed and then drifts.** Even the duplicate row was carried
across by the copy.

**The drift is legible, and it points one way.** Almost everything unique to BBW is the newer
abstraction pipeline — `ASG Lease Abstract - Contract Term / Covenants / Expense Schedule /
Expense Setup / Key Dates / Percent Rent / Funds and Expenses` (7 layouts), plus
`ASG Hours of Operation`, `ASG Contract Allowance Transaction`, `ASG Contract Cotenants`,
`ASG Cotenancy Language`, and the abandoned `zdelete`. What is unique to AF is older co-tenancy
variants (`ASG Co Tenancy`, `ASG Contract Co Tenancy`), `ASG Client Request Log`, and scratch rows.
**BBW is the more advanced fork; AF retains superseded versions of the same layouts.**

**Refined by §17:** "more advanced" overstates it. The divergence is not general drift — it is
**one entitled feature**. Almost every BBW-only layout is the `ASG Lease Abstract - *` family, which
serves the Atlas AI lease-abstraction pipeline that BBW has switched on and AF does not use.

**Why this matters for ASG Edge+.** This is the incumbent product already running a
**template-set-published-per-tenant-then-forked** model — the same shape as the Hub→Spoke
publish/accept/fork mechanism the target architecture proposes and has not yet specified. It is
evidence that the mechanism is needed, and evidence of its failure mode: with nothing tracking
versions, the two tenants have silently diverged, and **the only way to tell they came from one
source is to join on name and notice the id offset.** A rebuild needs the layout's provenance —
template id, version, fork point — as first-class data. Lucernex does not carry it.

### What this settles

Same names across two tenants could mean two firms configured themselves the same way. **Same primary
keys cannot.** These rows are seeded from one platform source, identical per tenant.

For the Hub/Spoke target architecture this converts an assumption into evidence:

| Layer | Evidence | Belongs in |
|---|---|---|
| Navigation tree and its `PageLayoutID`s | 109/109 identical ids | **Hub** — seeded, not firm-authored |
| Code-table registry (the 207 `TableType`s) | 207/207 identical ids | **Hub** — the *registry* is platform-fixed |
| Code-table **values** | differ (§3: same 3 contract statuses, different delete actions) | **Spoke** — firms populate the tables |
| Page layouts | 0 shared ids, but **80 shared names**, 0 table mismatches | **Spoke — but published from one ASG template set, then forked** |
| The 227-table platform schema | 227/227 identical, both tenants | **Hub** |
| `Equipment Contract` root | present at BBW, absent at American Freight | **Hub, licence-gated** *(Inferred)* |

The `Equipment Contract` row is pursued in §13 — and the simple entitlement reading there turns out
to be **insufficient**.

## 10. The contract creation wizard, captured

**Observed.** All five `ASG Contract Wizard` sub-page layouts rendered and their placed fields read
from the live DOM. Full data in [`bbw-wizards.json`](bbw-wizards.json). This is the create-and-abstract
path the approved BRDs care most about, and it existed nowhere in this corpus before.

| Step | PLID | Fields | What it collects |
|---|---:|---:|---|
| 1 — Contract Summary Setup | 98883 | 35 | contract identity, parties, and **every critical date** |
| 2 — Contract Terms | 98884 | 10 | renewal options: count, term type, term length, rentable area |
| 3 — Covenants | 98885 | 6 | **clones covenants from a template contract** |
| 4 — Responsibilities | 98886 | 6 | **clones responsibilities from a template contract** |
| 5 — Expense Setup | 98887 | 22 | recurring rent/expense with escalation |

Plus `ASG Facility Wizard` (99141, 26 fields) and `ASG Location Wizard` (99142, 23 fields).

**Field naming is `{Entity}_{Column}`, and firm-custom fields are `{Entity}_Firm_{Column}`** — direct
confirmation of the object catalog's note that 258 of `Contract`'s 570 fields are `Firm_`-prefixed
tenant customisations. Step 1 alone carries eight of them (`Contract_Firm_LeaseAnalyst`,
`Contract_Firm_BuildoutDuration`, `Contract_Firm_FixturingPeriod`,
`Contract_Firm_LatestCommencementDate`, `Contract_Firm_RentCommencementNotes`,
`Contract_Firm_LeaseExpirationReference`, `Contract_Firm_LeaseDateHistory`,
`Contract_Firm_LeaseStatusNotes`, `Contract_Firm_LeaseYearReference`).

Three findings that change the rebuild picture.

**Step 1 writes across two entities.** Alongside the `Contract_*` fields it carries
`Facility_OpenDate` and `Facility_CloseDate` — **the contract wizard updates the Facility record in
the same step**. A rebuild treating creation as a single-aggregate transaction will not reproduce it.

**Steps 3 and 4 are template cloning, not data entry.** Both read *"Select the Contract template
below to clone its covenant/Responsibility entries automatically"* and expose exactly one control,
`Covenant_ContractWizardTemplate` / `Responsibility_ContractWizardTemplate`. **Contract templates are
a first-class creation mechanism** and are documented nowhere in this corpus — no `ContractTemplate`
object exists in the 223-object census.

**Some fields are computed, not entered.** `TermLength`, `Contract_Firm_FixturingPeriod` and
`Contract_Firm_LatestCommencementDate` render as `input[type=hidden]` — derived during the wizard
rather than captured. `computed-vs-input-fields.md` classifies 666 accounting fields; these are
date-family equivalents it does not cover.

**Live data volumes** (Derived, from select option counts): 2,191 master contracts, 2,141 locations,
2,062 facilities, 151 expense types, 166 currency types, 142 lease analysts. BBW is a substantially
populated tenant, unlike American Freight.

## 11. Conditional fields — SOLVED, and my sweep was a false negative

**Open blocker #1 — the populated shape of `json.conditionalFieldsConfig` — is closed.**

### Retraction

Sections 6 and 11 of earlier revisions reported **"854 conditional targets across all 93 layouts,
zero populated"** and concluded the feature was wired everywhere and used nowhere. **That was a false
negative, and the conclusion was wrong.**

The method read the `value` attribute of the hidden `json.conditionalFieldsConfig` input in
`ConditionFilterEx.jsp`'s **server response**. That attribute is **always empty in served HTML** — the
builder populates it client-side from the field's stored record. The probe was therefore structurally
incapable of ever observing a rule, and "empty" was guaranteed regardless of the data.

This is the same failure mode as the `LayoutEditorAJAX` false negative in §6: a method validated
against a case with no data, where "nothing found" looks like correct behaviour. **Two of the eight
populated layouts sit inside the 93 I swept**, so this was not a scoping gap — it was a wrong reading
of real data.

### Where the rules actually live

**Observed.** Storage is `PageLayoutField.JSONConfigText` — a JSON blob on the **field**, with
`conditionalFieldsConfig` as a **nested object** inside it. It is never on `PageLayout` itself.

The definitive read is one REST call, no rendering and no builder session:

```
GET /rest/businessObject/PageLayout/lxid/{pageLayoutID}?deep=true
```

### The answer: the populated shape

```json
{
  "allAny": "all",
  "showHide": "show",
  "criteriaFields": [
    { "scriptName": "Issue.LAR_RequestType",
      "crtOpt1": "2",
      "crtVal1": ["Estoppel"],
      "isCheckBox": false }
  ]
}
```

**Observed across 50 records / 54 criteria clauses:**

| Element | Values seen | Vocabulary available |
|---|---|---|
| `showHide` | `show` (50/50) | `show`, `showAndRequire`, `hide` |
| `allAny` | `all` (50/50) | `all`, `any` |
| `crtOpt1` | `2` = **in** (51), `17` = **not in** (3) | wider set unobserved |
| `crtVal1` | array of **display strings**, not code ids | — |

Three things a rebuild must not miss:

**`crtVal1` stores display labels, not ids.** Values are `"Estoppel"`, `"New Lease"`, `"Yes"` — the
rendered text of the driver's code-table value, not its `CodeXxxID`. **Renaming a drop-down value
silently breaks every rule referencing it.** This is a defect to design out, not to reproduce.

**The `1` suffix implies a second operand slot.** Only `crtOpt1`/`crtVal1` are ever populated; the
naming implies `crtOpt2`/`crtVal2` the engine supports and BBW never uses. *(Inferred.)*

**BBW exercises a fraction of the engine** — never `hide`, never `showAndRequire`, never `any`. The
corpus's §"flat rule engine" description of the *capability* stands; the *usage* is much narrower.

### Where they are

**Observed.** 135 layouts swept (93 page + 42 form), 134 readable. **8 layouts carry 50 conditional
records.**

| Layout | Kind | Conditions |
|---|---|---:|
| `LAR Submit Lease Admin Request` (98946) | FORM | 19 |
| `LAR Initial Review of Lease Admin Request` (98944) | FORM | 16 |
| `LAR ASG Review of Lease Abstract` (98938) | FORM | 4 |
| `LAR Client Review of Lease Abstract` (98940) | FORM | 3 |
| `LAR Complete Lease Admin Request` (98941) | FORM | 3 |
| `LAR Finalize Lease Admin Request` (98942) | FORM | 3 |
| **`ASG Contract Covenants` (98864)** | **LIST** | 1 |
| **`ASG Lease Abstract - Covenants` (102250)** | **LIST** | 1 |

**The feature is concentrated almost entirely in one workflow.** 44 of 54 criteria clauses are driven
by a single field, `Issue.LAR_RequestType` — the Lease Admin Request's request-type selector. The
rest are Estoppel sub-questions and `Covenant.CodeCovenantTypeID`. **Conditional fields exist in this
tenant to make one request form adapt to its request type**, which is exactly BRD-24's territory.

### Form layouts are a hidden sub-system

**Observed.** Form layouts are reachable **only through Issue Types** — `mode=ISSUE` and `mode=FORM`
silently fall back to `SEP`, which is why they never appeared in the 93. **42 form layouts across the
6 Issue Types.** `PageLayoutField.CodeIssueTypeID` is what makes a layout a form layout.

**True layout total: 135, not 93.**

## 12. Two whole surfaces the corpus never saw

### 57 administration tools

**Observed.** `/en/dashboard/DashboardDispatchOld.jsp?dashboardName=admin` lists **57 admin tools**.
The corpus documents ten (screens 004-013). Full list in
[`bbw-platform-inventory.json`](bbw-platform-inventory.json). This is why the `ASG Employers` layout
pointed at an `Administration` node absent from the 105-screen tree: `Lx.ui.MenuTree` carries only the
**end-user** menu. Administration is a separate surface entirely.

Four of the 57 bear directly on open blockers:

| Tool | Route | Bears on |
|---|---|---|
| **RESTful WebService Docs** | `/en/test/RESTful.jsp` | **open blocker #3** — the write path |
| **View Object Model** | `/en/admin/ShowObjectDetails.jsp` | the object census itself |
| **Export Configuration** | `/en/admin/MessengerExportData.jsp` | would export the whole tenant config |
| **Layout Changes** | `/en/admin/ShowLayoutChanges.jsp` | layout change audit |

`RESTful.jsp` renders (42 KB) and is an interactive generator — *"Choose one or more record types
above and click the Load button to see the RESTful apis for those record types"* — with **Basic** and
**JWT Bearer** authentication tokens offered for copy. That settles the REST surface's auth model
(**Observed**); the per-record-type endpoint shapes still need the generator driven. *The page exposes
live credentials; none were captured, read, or recorded here.*

### 227 sql tables against a 223-object census — 31 undocumented, and only 6 are real gaps

**Observed.** `ShowObjectDetails.jsp` exposes a `sqlTableID` picker listing **227 tables**.

**A correction to an earlier revision of this section.** It reported "~34 tables genuinely absent from
the census", derived by matching **UI labels** against the catalog. That number was an artefact of the
matching key. Reconciled properly — matching both the UI label *and* the **physical table name** across
all 202 readable tables:

| Match key | Tables flagged absent |
|---|---:|
| UI label only | 18 |
| **Physical name** | **6** |

**Twelve of the eighteen were label mismatches, not gaps.** Ten are `Virtual*` computed views the UI
renames: `Sales Period` → `VirtualSalesPeriod`, `Development Target` → `DevelopmentSlot`, and —
importantly — **`General Entity Info` → `ProjectEntity`**, the universal supertype, which was never
missing at all. *(This also retires the §8 ambiguity: `Percentage Rent Period` and `Sales Period` are
confirmed as the `Virtual*` projections, by physical name.)*

**The six genuine omissions:**

| UI name | Physical | Fields |
|---|---|---:|
| Change Manage | `ChangeManage` | 1 |
| Member Template | `VirtualTemplateMember` | 1 |
| **Punch List** | `PunchList` | 10 |
| **Punch List Assignee** | `PunchListAssignee` | 5 |
| **Punch List Task** | `PunchListTask` | 13 |
| **Punch List Task Assignee** | `PunchListTaskAssignee` | 5 |

Two are one-field stubs of the kind the catalog already lists 18 of. The four-table **`Punch List`
family** (33 fields) is the only substantive omission — **and it is out of scope.**

**Out of scope, by the BRDs' own architecture (Observed).** All 38 approved BRDs were searched:
`punch`, `snag`, `defect list` and `site survey` return **zero files**, against a control term
(`contract`) hitting 31 — so the absence is real, not a failed search. More decisively, two BRDs
describe *"the existing ASG Edge system (the deal-making and **construction management** platform)"*
as a **separate product** that ASG Edge+ integrates with and migrates away from. Punch List is
snagging, which is construction management, so it belongs to legacy ASG Edge by the BRDs' own
statement — not merely unrequested, but assigned elsewhere. No BRD covers projects or capital
programs at all, consistent with that area already being out of scope.

Treat the four tables as the 27 Budgeting/Bid/Cost-Tracking objects are treated: retained for census
and FK-graph completeness, one-line purpose, no analysis.

**Which leaves the in-scope census gap at two one-field tables** — `ChangeManage` and
`VirtualTemplateMember`. The business-object catalogue is in better shape than even the corrected
number suggested.

**Total undocumented: 31 of 227** — the 6 real omissions plus the **25 tables the viewer refuses**
(§14 shows those are recoverable over REST). **The composition is the finding: this is a story about a
viewer withholding its own configuration tables, not about a census that missed things.** The
business-object census is in far better shape than a label-only diff suggests.

The refused 25 remain the important set, because they are the platform's own machinery — `Page Layout`,
`Page Layout Field`, `Page Layout Filter`, `Custom Code Table`, `Dashboard`, `Job Log`, `Audit Master`,
`Notify Template`, `Grid Preference`, the Excel integration trio, and others. **`PageLayout` is still
absent from the 223-object census**, and the reporting module's claim that *"a report **is** a
`PageLayout` row with `IsReport = true`"* still rests on a table the census does not carry. That
remains true and remains the gap that matters for rebuilding the layout engine.

### Forms: 6, and the 1:1 claim does not hold

**Observed.** `Issue Type Code` (`TableType=2035`) has **6** values at BBW: `ASC 842 Tracking`,
`Change Request`, `Lease Admin Request`, `QC Request`, `User Request`, `Vendor Changes (Integration)`.

The workflow module records *"four live workflows, 1:1 with four form types"*. At BBW there are
**13 workflow templates against 6 form types**. The 1:1 relationship is an American Freight
coincidence, not a platform rule — several workflows share a form type, and archived workflow
versions retain theirs.

## 13. Why `Equipment Contract` renders at BBW and not at AF

**American Freight is now on build `26.09.0.113` — the same build as BBW** (it was `26.08.0.46` when
first captured). Every comparison below is therefore same-build, which removes the most obvious
explanation. AF still shows **4 navigation roots and 109 nodes**; BBW shows 5 and 141.

Three candidate gates were tested.

**Gate 1 — the `Firm` record. Ruled out on its own (Observed).** AF's `Firm` (firmID 3158; BBW is
3159) carries **`Allow Equipment Contracts? = Yes`**. The flag is already on, and the root still does
not render. There is also **no `Equipment Contract Setup Page` field anywhere on `FirmEdit.jsp`** —
the object catalog's description of `Firm` holding per-module setup-page assignments is derived from
the schema and is not exposed in the UI. Full record (71 fields) in
[`af-firm-record.json`](af-firm-record.json).

**But the `Allow X?` flags clearly do gate roots (Observed).** `/en/admin/ManageTopMenu.jsp` shows AF
carries **14 top-level menu structures, 892 nodes** — far more than the 4 that render. Matching them
against the Firm flags:

| Menu structure | `Allow X?` | Renders |
|---|---|---|
| Portfolio, Location, Facility, Contract | Yes | **yes** |
| Program, Prototype, Site, Project, Parcel, Capital Project | No | no |
| **Equipment Contract** (id **41087**) | **Yes** | **no** |

Thirteen of fourteen line up exactly. **`Equipment Contract` is the single exception**, so a second
condition exists.

**AF carries the whole tree already (Observed).** AF's Menu Structure holds a complete
`Equipment Contract` structure — **id `41087`, 5 groups, 64 nodes — the same `PageLayoutID` as BBW's
rendered root.** Consistent with §9: the tree is seeded identically in both tenants; only rendering
differs. AF is also not equipment-free — it has `Equipment` *groups* under Portfolio (`51793`) and
Location (`51796`), exactly as BBW does. What AF lacks is only the top-level **root**.

**Gate 2 — user-class page access. TESTED, AND IT IS NOT THE GATE.**
`/en/admin/SecurityPageAccess.jsp` carries a per-User-Class page-access matrix
(No Access / View / Edit / Delete / Default) with a dedicated **`Equipment Contract` row
(`SecurityFieldId_99`)**, alongside `Contract` (`_97`), `Portfolio` (`_106`), `Parcel` (`_105`),
`Prototype` (`_109`).

**Now tested across all ten user classes, and the hypothesis is refuted (Observed).** The class
selector turned out to be a **GET parameter** (`SecurityPageAccess.jsp?UserClass={id}`), so no UI
interaction was needed. `Equipment Contract` is **granted at AF for 8 of 10 classes** — `Delete` for
the five admin classes, `View` for the three client classes. **In every class that grants `Contract`
at all, `Equipment Contract` is granted at the same level.** The two are indistinguishable. Only
`Default Security` and `Lease Admin Mail` deny it, and `Default Security` denies nearly everything
including `Contract`.

*(A related correction: the blank matrix on first load is not an "unselected default" as recorded
earlier — the page loads with `Default Security` genuinely selected, and that class really does deny
almost everything. The caution was right; the stated reason was wrong.)*

**So all three gates are open at AF and the root still does not render.** An earlier revision of this
document concluded "by elimination it is gate 3". **That conclusion is withdrawn.**

**And the decisive evidence is a second anomaly, not this one.** `Program` is granted by **all ten**
classes and **also fails to render as a root**. Two roots with the same shape means the missing
mechanism is **general**, not specific to Equipment Contract — and any explanation must account for
both.

> **A conflation to avoid:** AF's root *labelled* `Portfolio` carries
> `requestedProjectEntityType=Program`. The hidden structure is the **separate `Program` menu
> structure, id `3851`**. It is easy to see "Portfolio renders" and wrongly dismiss the counterexample.

**One more trap, worth stating because it caused the error:** `Default` in that matrix means
**inherit — "not explicitly granted"** — not "granted". `Program` proves the distinction: `Default`
for all ten classes, rendering for none.

**Status: Q-BBW-12 remains OPEN, with three gates now eliminated.**

| Gate | State at AF | Verdict |
|---|---|---|
| Build version | same `26.09.0.113` as BBW | ruled out |
| `Firm` entitlement (`Allow Equipment Contracts?`) | **Yes** | ruled out |
| Menu structure (id `41087`, 64 nodes) | **present** | ruled out |
| User-class page access | **granted, 8 of 10 classes** | ruled out |

**A fourth, unidentified mechanism exists**, and it must explain both `Equipment Contract` *and*
`Program`. First candidate to check: the securable action
**`Default access to Equipment Contracts for Portfolio Members`**, one of the 70 verbs on the Actions
tab — though note it cannot explain `Program`, so it is at best half an answer.

### Other same-build AF/BBW differences

| | AF | BBW |
|---|---:|---:|
| Navigation roots / nodes | 4 / 109 | 5 / 141 |
| Page layouts (SEP/SUB/LIST) | 17 / 31 / 40 = **88** | 15 / 32 / 46 = **93** |
| Workflow templates | 4 | 13 |
| Form types | 4 | 6 |
| Admin tools | **63** | 57 |
| Firm Drop Downs | 207 | 207 — identical |
| Sql tables | 227 | 227 — identical |

**The forms-to-workflows 1:1 claim is an AF artefact.** The workflow module records "four live
workflows, 1:1 with four form types" — true at AF (4 and 4), false at BBW (13 and 6). It is a
coincidence of one tenant, not a platform rule.

**AF exposes 6 more admin tools than BBW**, including `lxadmin`-only entries (`Modify Straight Line
Status`, `Data Conversion Cleaner`, `Test Email Address`). Admin-tool visibility is therefore
per-tenant or per-user-class, not fixed — which is itself a datapoint for the §12 count of 57.

## 14. The REST write path — open blocker #3 closed

**Observed.** `/en/test/RESTful.jsp` embeds stock Swagger UI pointed at **`/rest/api-docs/swagger`**,
which serves the complete **OpenAPI 3.0.1** document. Fetching it makes the interactive generator
unnecessary. Full capture in [`bbw-rest-api.json`](bbw-rest-api.json).

| | |
|---|---:|
| Paths | **141** |
| Operations | **160** |
| GET / POST / PUT / DELETE | **104 / 40 / 7 / 9** |
| Tags | 11 |
| Schemas | 25 |

**Write verbs exist and are first-class.** The corpus's standing picture — *"617 GraphQL queries
against 3 mutations, so the write path is unknown"* — describes GraphQL only. **REST is fully CRUD**,
and it is the write path.

### One generic controller serves all 227 record types

```
POST   /rest/businessObject/{objectType}                     create  (?allowUpdate=true upserts)
PUT    /rest/businessObject/{objectType}                     update
POST   /rest/businessObject/{parentObjectType}/{parentID}    create child
DELETE /rest/businessObject/{objectType}/lxid/{lxID}
DELETE /rest/businessObject/{objectType}/clientid/{clientID}
GET    /rest/businessObject/{objectType}/details?fiql=…&fields=…&$skip&$top
```

The request body is a recursive `BusinessObject` — `botype` required, `fields[]`, and nested
`children[]`, in JSON or XML. So **a contract and its children can be written in one call**, which is
how the wizard's multi-entity step (§10) is likely served.

Reads use **FIQL** filtering; `fields` is mandatory and the endpoint returns **413** when too many are
requested — a real constraint for any bulk extraction.

### The trap worth designing around

**Writes return `ImportResults` — a bulk envelope of `successes[]` and `errors[]`.** A write can
therefore return **HTTP 200 while having failed**; the caller must inspect `errors[]`. Any ASG Edge+
integration that treats 2xx as success will silently lose data.

**Auth is out-of-band.** The spec declares **no `securitySchemes`**; authentication is Basic or JWT
Bearer supplied externally. *(No token was read, captured, or recorded at any point.)*

### It also unlocks the tables the object viewer refuses

**Observed.** `GET /rest/businessObject/PageLayout/lxid/{id}?deep=true` serialises a layout together
with its `PageLayoutField` children, exposing real column names — **`PageLayout` 17 columns,
`PageLayoutField` 20** — for tables `ShowObjectDetails.jsp` refuses (§12). All 25 refusals appear in
`GET /rest/firm/types` and are recoverable this way.

`CodeIssueTypeID` on a layout is what makes it a form layout. Geometry is three parallel coordinate
sets (`Edit*` / `View*` / `Header*`).

**Caveat, stated by the capture:** the serialiser emits only **populated** columns, so column lists
from this route are a **lower bound**, not a schema. `PageLayoutFilter` is a valid REST type with
**zero rows** in BBW — genuinely empty, not inferred.

### Two mechanics worth reusing

- `ConditionFilterEx.jsp` does **not** require `CustomObjectDelID`; `fieldKey` + `pageLayoutID` return
  a byte-identical response.
- **Only one `LayoutEditorAJAX` builder can be open per session** — concurrent iframes collide. Any
  future layout sweep must be serial.

## 15. The foreign-key graph under-counts by ~9%

**Observed.** The corpus's FK graph (972 edges) is built by matching column **types** — a column
counts as a foreign key when its declared type names a target object (`Contract ID`, `Entity ID`).
That rule misses columns *named* like a key but *typed* as a scalar.

| | |
|---|---:|
| Columns named `*ID` with a typed object FK | 864 |
| Columns named `*ID` but scalar-typed | 523 |
| …of those, matching a real object name | 237 |
| …less the table's own primary key | **−150** |
| **True missed edges** | **87** |
| Source tables affected | 60 |
| Target objects under-counted | 30 |
| **Under-count against 972** | **~9%** |

The hidden types are not only `Text` (59) — also `Number` (13), `Part` (5), `Parts Package` (3),
`Currency` (2), `Holiday Calendar` (2), `Contact` (2), `Entity` (1). The pattern is *"named like a
foreign key, typed as something that is not a reference"*.

**The under-counted targets are central, not peripheral:** `Issue` by 13, `Firm` by 12,
**`ProjectEntity` by 9**, then `BudgetLineItem` 5, `Part` 5, `BudgetColumn` 4, `Person` 4.

**The spine classification survives — one exception.** All 148 catalogued `entity_scoped` objects in
the capture carry `ProjectEntityID` typed `Entity ID`, and none lacks the column, so
[`project-entity.md`](../data-model/project-entity.md)'s classification was applied consistently. The
9 `subtype_root` objects carry it typed `Number`, which the catalogue already models separately on a
shared key — correct behaviour, not a defect.

The single exception is **`AssetHistory`**, which carries `ProjectEntityID` typed `Entity` (not
`Entity ID`) and is classed `firm_global`. It is plausibly mis-classified and should perhaps be
`entity_scoped` — but it is a point-in-time snapshot of an `Asset`, so whether it is scoped to the
entity or to the asset is a **data-model judgement**, not something a column type settles. Flagged,
not changed.

**For the rebuild:** a model derived from declared column **types** rather than naming convention
silently loses 87 relationships. The `Punch List` family is the extreme case — all three children
reference their parent through a `Text`-typed `PunchListID`, so the family renders as four
disconnected tables. That artefact is what made the pattern visible.

*Computed over the global-only capture (§12), so **87 is itself a lower bound**.*

## 16. Firm custom fields are physical columns — and that settles ADR-004

**Observed, verified directly against `_lucernex_objects_summary.txt`.** Tenant custom fields are not
rows in a metadata table. They are **ordinary physical columns**, named `Firm_<Name>`, fully typed.

| | |
|---|---:|
| `Firm_` columns across the schema | **359** |
| Objects carrying them | **20** |
| …on `Contract` alone | **258** of its 570 columns |

Next largest: `Location` 10, `Facility` 8, `Covenant` 7, `KeyDate` 7, `AllowanceTransaction` 6,
`Parcel` 6. They carry real types — 188 Text, 77 `Dropdown (Custom Field)`, 28 Date, 22 Percentage,
19 Currency, 7 Custom List.

> **On the count.** 359 is from the **census** (`_lucernex_objects_summary.txt`). The **catalog**
> (`all-fields.csv`) exposes only **205** `Firm`-scope leaves — 147 on `Contract` against the census's
> 258 — and diverges the other way elsewhere (`KeyDate` 10 against 7). This is a known,
> already-documented divergence, not a new discrepancy: see
> [`reading-the-census.md`](../data-model/reading-the-census.md), which records that the three field
> inventories (census 7,421 · catalog 6,158 · View Object Model 7,047) disagree in both directions and
> **none is the physical schema**. Treat 359 as "the census's count of firm columns", not as a
> verified physical total.
>
> **The argument below does not rest on the number.** It rests on firm fields being *physical columns
> at all*, which every inventory agrees on — the census lists them as typed columns, the catalog scopes
> them `Firm`, and the layout editor places them as `Contract_Firm_*`. Whether it is 205 or 359,
> adding one is still DDL.

### The consequence

**Adding a firm custom field is a DDL change against the tenant's table.** A per-firm column on a
shared table is only workable if **each tenant has its own database**.

The workspace `CLAUDE.md` records two contradicting ADR-004s: the KB's
`ADR-004-multi-tenancy-database-per-tenant.md`, and configuration-service's
`0004-multi-tenant-defense-in-depth.md` arguing one shared platform database. **Lucernex is direct
evidence for database-per-tenant and against a shared database.** 258 tenant-specific columns on one
shared `Contract` table cannot coexist with other tenants' columns in a single database without
either a union-of-all-tenants table or per-tenant schemas — and the incumbent chose neither.

It also explains an observation the corpus recorded without explaining: **Manage Data Fields is
read-only to a firm in both tenants.** You cannot self-service a DDL change. Field creation is a
vendor operation because it has to be.

### Knock-on: field counts from the platform capture are a floor

`bbw-platform-tables.json` reads `Contract` at **307** fields against the census's **570** — the
difference is almost exactly the 258 `Firm_` columns plus the global/firm split of §12. **Every field
count derived from that capture is a lower bound** until the `showGlobal=false` re-run lands.

## 17. There is a live AI lease-abstraction pipeline

**Observed**, from the OpenAPI capture (§14). Three of the API's eleven tags are a third-party
**AI lease-abstraction integration** — 16 operations in total:

| Route | Verbs | What it does |
|---|---|---|
| `/atlas-api/import/{leaseId}` | POST | Fetch one lease from the **Atlas** API and import it |
| `/atlas-api/import/{leaseId}/async` | POST | Same, scheduled asynchronously |
| `/atlas-api/contracts` | GET | List active contracts for Atlas *update-existing* import |
| `/adapter-config/{vendorId}/{fileName}` | GET · PUT · DELETE | The vendor's field-mapping config |
| `/adapter-config/firms/{firmId}/{vendorId}/{fileName}` | GET · PUT · DELETE | **Per-firm override** of that mapping |
| `/adapter-config/vendors` | GET | Registered vendor adapter ids |
| `/vendor-lease` | — | The vendor-lease surface itself |

**The field mapping is tenant-configurable.** A vendor adapter has a default config, and a firm can
upload an override at `/adapter-config/firms/{firmId}/…`. So the AI extraction → Lucernex field
mapping is configuration, per tenant, not code.

### It ties together four previously unconnected observations

Each of these was recorded separately in this document with no explanation:

| Observation | Where |
|---|---|
| `Allow AI Lease Abstraction` is a `Firm` entitlement flag | §13 |
| BBW has seven `ASG Lease Abstract - *` layouts AF lacks | §9 |
| `AI Abstracted` is a value in four status code tables | §3 |
| `AI Abstracted` became **delete-protected** in build `26.09` | §3 |

They are one feature. `AI Abstracted` becoming platform-protected in `26.09` reads as the vendor
promoting the AI-abstraction path from a tenant-added convention to shipped functionality — which
also **retires the corpus's claim that `AI Abstracted` is "a tenant-added status"**
([`code-table-registry.md`](../data-model/code-table-registry.md)). On current evidence it is
vendor-shipped. *(Inferred — we observed the flag change across builds, not the value's origin.)*

### What it means for the AF/BBW difference

**The two tenants do not differ by general drift.** Almost every BBW-only layout serves this one
pipeline. BBW has the entitlement and uses it; AF does not. That is a far more precise statement than
"BBW is the more advanced fork", and it changes the rebuild question from *"why have these tenants
diverged?"* to *"is AI lease abstraction in scope for ASG Edge+?"*

**It bears directly on BRD-24.** The corpus already records that the Lease Admin Request workflow's
step 2 is "Abstract Lease Document", and §4 shows two `Implementation Workflow` templates for document
and financial abstraction. A production AI abstraction pipeline with per-tenant field mapping sits
underneath that workflow. **The BRD's abstraction path is not purely human**, and a rebuild must
decide whether to reproduce the integration, replace it, or drop it — a question nobody has been
asked, because nothing in the corpus showed the pipeline existed.

## 18. The discount-rate table is empty in both tenants

**Observed, verified from the screens themselves** in both tenants
(`docs/assets/screenshots/bbw-admin/25-manage-discount-rates.jpg`,
`docs/assets/screenshots/af-admin/26-manage-discount-rates.jpg`, both build `26.09.0.113`).
`Manage Discount Rates` reads **"No rows to display"** and **"No items to display"** at BBW *and* at
American Freight.

**Why that is a problem.** ASC 842 and IFRS 16 both require a discount rate to compute the lease
liability. Both tenants run both standards plus straight-line. Two independent tenants showing an
empty table retires the "this one happens to be unpopulated" explanation.

So either the rate reaches the engine by the **per-record override** — `Asset.DiscountRateOverride`
and its `SLSummary` equivalent, both already in
[`modules/accounting/`](../modules/accounting/) — **or no schedule in either tenant has ever actually
been calculated.** Both readings matter:

- If the override is the real path, **ASG Edge+ implementing the rate table alone reproduces an
  engine that cannot calculate.**
- If nothing has been calculated, then the ASC 842 output this corpus documents has never been
  exercised against real rates, and the schedules seen in §10/§4 are structure without arithmetic.

**This should be put to ASG before the accounting engine is specified.** *(Q-BBW-18.)*

**And it is stranger than a dormant tenant would be.** BBW is not idle: `Job Log` carries 818
entries, a real XLSX import, and an **hourly inbound HTTP integration** posting transaction data
(Q-BBW-19). A tenant with live operational traffic *and* an empty discount-rate table is harder to
explain than an unused one — it makes the per-record-override reading more likely than "nobody has
run a schedule yet", and it raises the question of what the hourly feed is doing if the lease
liability cannot be discounted.

### What the table is designed to do is richer than assumed

Even empty, the column set gives the lookup key. A rate is selected by **seven dimensions**:

| Dimension | Note |
|---|---|
| Effective date range | `Effective End Date *` |
| **Lease-length band** | `Length Month (min) *` – `Length Month (max) *` — an incremental-borrowing-rate curve |
| Country | |
| State / Province | |
| Portfolio | |
| **Accounting Method** | |
| Use Type | |

**`Accounting Method` as a lookup dimension means the same lease can discount differently under
ASC 842 and IFRS 16** — consistent with the corpus's finding that one engine serves three standards
off flags on `SLSummary`. And the length band is an IBR curve, not a single rate: a rebuild needs
range-matched lookup, not a scalar.

### The asterisk appears on list column headers — which moves §11's open question

**Observed, from the same screenshots.** The red `*` sits on **list column headers** —
`Effective End Date *`, `Length Month (min) *`, `Length Month (max) *`, `Discount Rate *` — while
`Country`, `State / Province`, `Portfolio`, `Accounting Method` and `Use Type` carry none.

That is a useful narrowing of the required-ness hunt. Whatever drives the asterisk **travels with the
placement and renders on a LIST layout**, not only on a detail form. It therefore cannot be explained
by anything specific to `PForm.jsp`, and it is consistent with storage on `PageLayoutField` — which
keeps `DisplayOption1`/`DisplayOption2` as the last standing candidate after the other three were
eliminated (§ required-ness chain: schema `Required?`, the RGAF catalog, and `JSONConfigText` are all
ruled out for the decisive layout).

It also gives a second test target that needs no session beyond one REST call: this list layout has a
clean split of five asterisked against five plain columns, which is a better discriminator than the
2-versus-1 split on layout 98927.

## 19. The product names its own publish-and-fork model

**Observed**, from `Export Configuration` (`/en/admin/MessengerExportData.jsp`),
`docs/assets/screenshots/bbw-admin/14-export-configuration.jpg`, BBW build `26.09.0.113`.

It is not a data export. It is a **configuration** export, tabbed by exactly the sub-systems §12
enumerated — Summary Pages / Sub Pages / List Pages / Forms / Reports / Templates / Others — and the
Summary Pages tab reads "Displaying 1 - 15 of 15", matching BBW's 15 `SEP` layouts precisely.

Above the grid sits a checkbox that states the model in the vendor's own words:

> ☐ **Clone these layouts in this firm and environment** (new layouts/fields created when this xml is imported)
> *Do not check this if you are moving layouts, forms,… from one environment to another or one firm to another (e.g. dev to iwms)*

**That is §9's publish-and-fork model, named by the product.** §9 derived it from arithmetic — 80
layouts shared by name, zero by id, offsets clustered at +2626…+2677, the same duplicate row in both
tenants. This is the operation that produced those numbers, and it names **both** modes:

| Mode | Effect |
|---|---|
| **Clone** checked | New layouts and fields created on import — **new ids** |
| **Clone** unchecked | Moving between environments or firms — **identity preserved** |

ASG exported its template set and imported it with **Clone** checked. That is precisely why the ids
are disjoint while the names match, and why the sets then drifted independently.

**Configuration round-trips through the same format as data** — this export produces XML, and
`POST /rest/firm` consumes XML. So the Hub→Spoke publish mechanism the workspace `CLAUDE.md` records
as *"not written down anywhere"* has working prior art in the incumbent.

**With one limitation worth designing around.** Clone-on-import leaves the Spoke's copy with **no
pointer back to the Hub original** — no `source_global_layout_id`, no version stamp. That is exactly
why the AF↔BBW comparison had to be done by joining on name (§9), and why the two tenants could
diverge silently. **ASG Edge+ should keep the lineage Lucernex discards.**

### The same model governs code tables — and there are exactly three

**Observed.** The AF↔BBW drop-down join had to be done on **name**, not id: the tenants share **zero**
value ids, exactly as the layouts did. On the **646** values sharing `(tableType, name)`,
`isReadOnlyRecord` agrees **646 of 646**. Of the **1,045** values unique to one tenant (477 AF,
568 BBW), **zero** are read-only.

So code tables are distributed exactly like page layouts: one seeded set, re-keyed into disjoint
per-tenant id spaces, then forked locally with firm-added values that are all deletable.

**The estate therefore runs three distinct distribution models, and the boundaries matter as much as
the pattern:**

| Model | Applies to | Signature |
|---|---|---|
| **Platform-seeded and shared** | navigation nodes, the 227-table catalog | **identical ids** across tenants |
| **Published, then forked** | page layouts, code-table values | **matching names, disjoint ids** |
| **Tenant-authored** | workflow templates | names mostly differ, no id pattern |

A rebuild needs all three, and needs to know which surface is which — treating a published-then-forked
surface as tenant-authored loses the template; treating it as platform-seeded loses the fork.

### `PreviousPageLayoutID` is a sequence pointer, not a version pointer

**Observed.** The same screen carries a **`Previous Layout`** column, and joining those pairs against
the registry gives ordered chains — **8 of 8 chained pairs share the same navigation parent**, and
every navigation node with more than one layout resolves to exactly one chain with a single head:

```
Contract : Abstract Info : Abstract Details
  Contract Abstract Details → Common Area Maintenance → Delivery Requirements
    → Funds and Expenses → Real Estate Taxes

Contract : Payment Info : Percentage Rent
  ASG Contract Percent Rent [LIST] → Percent Rent Schedule [SEP] → Breakpoint Schedule [SEP]
```

**This corrects an earlier reading.** `bbw-layout-engine-tables.json` recorded
`PreviousPageLayoutID` as "a second self-reference used for versioning/duplication" — a fair
inference from the column name, but wrong. The chains link **semantically distinct layouts in a
reading order**, not versions of one thing.

**This answers the layout system's biggest open question.** §"many-to-one attachment" observed that
five layouts share one navigation node and asked how the runtime picks between them. **It does not
pick — they are an ordered sequence.**

Two consequences for a rebuild:

- The model is **`(navigation_node, sequence)`** on the layout. A *set* of layouts pointing at a node
  is not enough; the order carries meaning.
- **Chains cross modes.** Two heads are `LIST` layouts followed by `SEP` pages — for Percentage Rent
  the user meets the grid first, then the schedule page, then the breakpoints. A rebuild that models
  list and detail layouts as separate populations cannot express this.

What remains open is only *presentation* — tab strip, stacked sections, or next/previous navigation.
One rendered end-user screen on a chained node settles it.

*(The same screen also labels two layouts' primary table `VirtualPercentageRentPeriod` outright,
confirming §8's `Virtual*` projection reading in the product's own words.)*

## 20. Configuration publishes along three tiers — and only the vendor's is versioned

**Observed**, from `Import Best Practice Templates`
(`docs/assets/screenshots/bbw-admin/13-import-best-practice-templates.jpg`). This is
**Accruent's own publish channel into a tenant**: seven versioned configuration packages, with
columns **`Version`**, **`Min Version`** and **`Released`**.

| Package | Version | Min Version |
|---|---:|---:|
| Bidding Sub-Module Package | 1.8 | 20.10 |
| Budget Package — Site and Project Standard Budget Items | 4.4 | 19.12 |
| Folder Template — RE Contracts | 1.9 | 19.12 |
| Folder Template — Sites and Projects | 2.9 | 19.12 |
| Package — GC Bidding | 1.0 | 19.12 |
| Project Cost Tracking Package | 4.1 | 20.2 |
| Request for Information (RFI) | 2.3 | 19.12 |

Their descriptions say what a package contains — *"key forms and a bid package template"*, *"our
standard sub page layouts, forms, and workflows"*. These are layouts, forms and workflows shipped as
a unit.

### The three tiers

| Tier | Mechanism | Versioned | Lineage kept |
|---|---|:--:|:--:|
| **Accruent → firm** | Best Practice Templates | **Yes** — Version / Min Version / Released | unknown |
| **Firm → firm, env → env** | `Export Configuration` XML, clone or move (§19) | **No** | **No** — clone discards it |
| **Within a firm** | Direct layout editing | No | — |

**This is the closest prior art available for the Hub→Spoke rule the workspace `CLAUDE.md` records as
unwritten.** A package carrying a **`Min Version`** is a real compatibility contract between a
configuration package and the platform release it installs onto, and `Released` separates published
from draft. That is the shape of *"never more than one version behind"*, already implemented — at the
vendor tier.

**And the gap is precisely where ASG operates.** The vendor's tier is versioned; the **firm-to-firm
tier is not**, and §19 showed clone-on-import discards the origin pointer. ASG publishes its layout
set into each client tenant through the *unversioned, lineage-less* tier. That is the whole
explanation for §9: same layouts, disjoint ids, silent divergence, and a name-join as the only way to
detect common origin.

**ASG Edge+ should build the vendor tier's discipline at the firm tier** — version, minimum-version
compatibility, released/draft, and the lineage pointer Lucernex omits at both.

Two further observations from the same screen: **package dependencies are prose, not modelled**
(*"IMPORTANT: Import the Budget Package first"* appears on two packages, with nothing enforcing it),
and a **dev → Train → production environment progression** is assumed (*"import this into your Train
environment first to confirm setup"*).

**Note what is absent.** All seven packages target bidding, budgets, cost tracking, RFI and folder
templates — very nearly the exact set ASG Edge+ has ruled **out of scope**. Accruent ships no best-
practice package for lease accounting, contracts or ASC 842. The channel exists; it is empty for the
product's core.

## 21. Every UI label in this corpus is potentially tenant-local

**Observed**, from `Manage Firm Dictionary` (`/en/admin/Dictionary.jsp`). A firm can **overwrite field
labels tenant-wide** by uploading a spreadsheet — the screen's own note offers it *"to provide new
translation **or to just overwrite the field labels**"* — with global and firm-specific layers and
per-language variants.

**This is a caveat on the whole corpus, not one document.** Every screen name, navigation node name,
field label and code-table value name recorded anywhere in these documents may be a tenant-local
override rather than the product's own vocabulary. **Internal names are unaffected**, which turns the
existing convention *"use real field and table names in `code`, never paraphrases"* from a style
preference into a **correctness requirement**. It has been added to
[`CONVENTIONS.md`](../CONVENTIONS.md).

It also bears on §12's census reconciliation: the UI-label-versus-physical-name mismatches that
inflated the missing-table count from 6 to 18 are exactly the failure mode this mechanism produces at
scale.

Whether either tenant has actually overridden anything is **unknown** — one `Download Current
Dictionary` with *Firm specific phrases* selected would settle it, and it is worth doing.

**This is the third subsystem on the identical global/firm two-tier pattern**, after the field
registry (`RGAF.IsGlobal` + `FirmID`) and the layout registry (`Firm Layouts` / `Global Layouts`).
That consistency is itself an argument for the Hub/Spoke shape: the incumbent applies it to *every*
configuration surface, not just data.

## 22. How "required" works — there is no layout-level layer

**Observed, and this closes the question.** The discount-rate list layout (`PageLayoutID 88572`) gives
a clean 1:1 test, because its grid has four asterisked columns against six plain ones on a single
layout:

| Column | Asterisked | Schema `required` |
|---|:--:|:--:|
| `DiscountRate` | ✳ | **Yes** |
| `EffectiveThroughDate` | ✳ | **Yes** |
| `MinSchedMons` (Length min) | ✳ | **Yes** |
| `MaxSchedMons` (Length max) | ✳ | **Yes** |
| `Country` · `State / Province` · `Portfolio` · `Accounting Method` · `Use Type` · `Notes` | — | No |

The `DiscountRate` table has **exactly four** required columns, and they are **exactly the four** the
builder marks. **4 of 4 and 6 of 6, no exception in either direction.**

### The answer

**The asterisk is schema-required, rendered at paint time. There is no layout-level required layer at
all.**

`DisplayOption1`/`DisplayOption2` are eliminated, and the bit pattern shows why they were never going
to work: bit 3 is set on `EffectiveThroughDate` and `DiscountRate` but **not** the two Length fields;
bits 14+27 are set on the Lengths and `DiscountRate` but **not** the date. **No single bit covers the
asterisked set.** What the bits actually track is **data type** — 14+27 appear on the three
numeric/percentage fields and not on the date — which is exactly what layout 98925's
placement-kind pattern had suggested.

### What this means for ASG Edge+

**Do not build a per-placement required flag.** Required-ness is a property of the *field*, resolved
from the schema at render time. Adding an `IsRequired` column to a `PageLayoutField` equivalent would
model something the source product does not have — and the absence of that column, noted repeatedly
in this corpus as a puzzle, turns out to be the design, not an omission.

The layers that **do** exist are three, and only two are storage:

| Layer | What it expresses | Where |
|---|---|---|
| Schema `required` | NOT NULL at storage | the column |
| Catalog `Required` | the user must supply this when creating the record — additionally covers **parent linkage** | `ReportGroupAvailableField` |
| Conditional `showAndRequire` | required *only when* a rule matches | `PageLayoutField.JSONConfigText` (§11) — **used zero times in BBW** |

**On the correct denominator** the join is **5,650 agree / 42 catalog-only / 2 schema-only = 99.2%**,
and the 44 disagreements are **byte-identical** to those found on the partial set — the same 34
`ContractID`, 8 `ProjectEntityID` and 2 `ProjectEntity` audit stamps. The caveat is lifted and the
number published.

**Corroborated by a third, independent source.** The owner-supplied
[`bbw-field-inventory.csv`](../data-model/pg/bbw-field-inventory.csv) carries its own `Required`
column (606 of 7,358). Joined against the Manage Data Fields catalogue on `(object, field name)`:
**5,768 joined · 5,725 agree (99.3%) · 43 disagree — every one catalogue-Yes / inventory-No, and
34 of them `ContractID` plus 8 `ProjectEntityID`.**

Three sources, three slightly different totals (603 · 637 · 606), and **the same structural
signature every time: the disagreements are owner foreign keys.** That is the finding — a parent
link the application demands and the database permits to be null. The exact count varies with the
source because each inventory covers a slightly different population; the pattern does not vary at
all, which is what makes it trustworthy.

§3's note stands: the first two are **not** one flag twice. 42 catalog-Yes/schema-No cases are all
owner foreign keys, 2 reverse cases are audit columns, so neither is a subset. A rebuild needs both —
`NOT NULL` cannot express *"you must pick a parent Contract when creating an Allowance"*.

### A method failure worth recording

**The test every one of us designed could never have worked.** Layout `98927` was chosen as the
target by three separate parties — the capturing agent, this document, and the knowledge-base agent —
on the assumption it placed `Contract Status`, `Location` and `Master Contract`. **It does not.** Its
22 placements are `Notes`, six action buttons, five Sub Edit Forms and six section headers; those
fields live inside sub-layouts embedded through `SubEditForm`. Nobody checked the layout contained
the fields before building a comparison around them.

**Unresolved counterexample, recorded rather than explained:** `docs/admin/008` reports
`Contract Status` and `Location` painted red on the layout builder, yet neither is schema-required on
`Contract`. The likely explanation is that they render from a sub-layout with a different primary
table — untested, and it is the one piece of evidence that does not fit §22's rule.

## 23. The contract lifecycle lives in a firm-defined drop-down

**Observed.** `Lease Status` (`CustomCodeTableID 7727`) is one of BBW's **38 firm-defined** Client
Drop Downs — not a platform code table — and carries **seven** values:

`Open` · `Possession` · `Possession - Paying Rent` · `Closed` · `Closed - Active` ·
`Future Possession` · `Accounting Purposes Only`

**This substantially answers a question open since the corpus began.** §3 established that the
platform's `Contract Status Code` has only three values (`Active`, `AI Abstracted`, `Inactive`) and
never matched BRD-24. It does not have to: **ASG tracks the lifecycle in a field it defined itself.**

| BRD-24 stage | In `Lease Status` |
|---|---|
| Open | `Open` — exact |
| Active | **absent as a standalone** (only inside the compound `Closed - Active`) |
| Possession | `Possession` — exact |
| Paying Rent | `Possession - Paying Rent` — compound |
| Closed | `Closed` — exact |

Four of five present, one only as a compound, plus two stages BRD-24 does not name
(`Future Possession`, `Accounting Purposes Only`). **Close to the BRD, not identical with it** — worth
putting in front of whoever owns BRD-24, because the tenant's real lifecycle is the one in production.

### The detail that matters most

**`SortOrder` is null on every value, so the drop-down renders alphabetically.** The sequence
Open → Possession → Paying Rent → Closed exists **only as convention in users' heads**. The platform
stores no ordering, no transitions, and no state machine.

**A rebuild that models this as an ordered state machine is adding structure the source system does
not have** — which may well be the right thing to do, but it is a *decision*, not a migration, and it
needs stating as such.

**Also captured:** `Lease Admin Request Type`, 13 values, containing every value referenced in the
conditional-field configs (`Estoppel`, `New Lease`, `Vendor Change`, `Amendment`) — confirming it as
the source of `Issue.LAR_RequestType`, which drives 44 of 54 conditional clauses (§11). **The
conditional engine's principal driver is a firm-defined drop-down, not a platform one.**

**And a negative worth having:** all 38 firm tables have `ParentCustomCodeTableID` empty — so the
**dependent/cascading drop-down capability exists and is used nowhere in BBW.**

## 24. The Equipment Contract record, and why only four screens exist

**Observed.** Four end-user screens captured at full width — `docs/assets/screenshots/bbw-enduser/` —
`eq-01-details-summary`, `eq-02-abstract-details`, `eq-03-payment-details`, `eq-04-accounting-details`.
All four md5s differ, so they are four genuinely distinct screens.

**These are the first end-user screens ever rendered in this tenant**, and the first of the
Equipment Contract module anywhere in this corpus.

> **Standing caveat on everything in this section.** BBW holds **exactly one** equipment contract
> (`ASG Equipment Contract`, lxID 507018, 1 of 2,008 contracts). These screens show **one record's
> population, not the module's range** — an empty section may be empty for this record rather than
> unused in the module.

The record carries `Contract ID ASG1234`, commence `01/09/2026`, expire `30/09/2031`, one asset
(`Tractor`, asset group `ASG`), and an Actions panel offering `Edit`, `Add Equipment`, `Audit Log`,
**`Generate Payments`**, **`Approve Payments`**, `Extend Contracts`, `Extend Asset P…`,
`Save to Document`, `Link`. Those action buttons are the placeable, securable verbs of §"Actions".

### 28 of the 32 nodes are not deep-linkable — and that is the finding

**Observed.** `PForm.jsp?menuPLID=…` does **not** address these sub-screens. Three distinct behaviours:

| Behaviour | Nodes |
|---|---|
| Group node **redirects to its first leaf** | `Details` renders identically to `Summary` |
| Returns `/en/ErrorPages/AccessDenied.jsp` | Members/Contacts, Forms, Work Flow, Documents, Reports — the capturing user lacks rights |
| Returns an empty fragment, or **bounces to `EntityInfo.jsp` which renders the default Summary** | Terms, Amendments, Covenants, Key Dates, Insurance, Transactions, Straight-Line Rent, ASC 842 Test, ASC 842 Rent Schedule, IFRS 16 |

**The mechanism:** `EntityInfo.jsp` is the record **shell**, loading the active sub-screen into an
inner iframe (`EntityInfo.jsp?projectEntityID={id}&inPanel=true`). **Sub-screens are selected by the
in-app menu tree, not by URL.** Appending `&inPanel=true` to the `PForm` route does not change this —
tested.

**For a rebuild this is a routing requirement, not a footnote** — but it is **not uniform across
entity types**, and an earlier revision of this section overstated it as "the incumbent has no
addressable URL per sub-screen". Corrected:

| Root | Addressability |
|---|---|
| **Equipment Contract** | **Not deep-linkable at all.** Only group heads resolve, and they render their first leaf |
| **Contract** | **Partially.** 14 of 46 sub-screens have real URLs; 22 look addressable but silently redirect; 8 are AccessDenied; 2 bounce server-side |

So roughly **a third of Contract's sub-screens would survive** a link migration and none of Equipment
Contract's would. Anything migrating saved links needs that distinction rather than a blanket
statement.

### A fetch-based route audit overstates deep-linkability by more than 2×

**Observed, and this is the methodological finding.** Classifying all 46 Contract routes by **raw
fetch** reported **36 addressable**. Driving the same 46 in a real browser produced **14**.

The 22-route gap is **client-side JS redirection**: the server returns a full 37–40 KB HTML document,
so `fetch` sees a clean success — and then the page's own script bounces to `EntityInfo.jsp` and
renders the default Summary. **Only a real browser reveals it.**

Without the post-capture URL guard this would have produced 22 correctly-named files all containing
the same Summary page.

**This is the same failure that produced §11's retracted false negative** — there, fetching
`LayoutEditorAJAX.jsp` returned zero conditional targets because they are injected client-side. Both
times a cheap network signal (status plus body size) was taken to stand for what a user actually
sees, and both times it was wrong in the direction that looks like success. **In this application,
a 200 with a plausible body proves the server answered, and nothing about what renders.**

**What the capture guard prevented.** Sweeping all 32 naively would have produced roughly **20 files
with distinct, meaningful names all containing the same default Summary page**, plus six Access
Denied pages. They load correctly, are full-size, and look like real screens — the corruption would
have been near-impossible to detect later. Every one was caught by the final-URL check.

### It settles §22's open counterexample

`docs/admin/008` reported `Contract Status` and `Location` painted red in the **layout editor**, which
was the one piece of evidence contradicting §22's rule that the asterisk is schema-required.

**On the rendered end-user screen, `Contract Status` (value `Active`), `Location` and `Master
Contract` all appear — and none is marked required.** Verified directly in
`docs/assets/screenshots/bbw-enduser/eq-01-details-summary.jpg`.

**So the builder's red text is an editor affordance, not a stored obligation, and it does not reach
the end user.** Q-BBW-21 is closed, and §22's model stands without exception:

| Layer | Where | Used in BBW |
|---|---|---|
| Schema `required` | the column | yes — and it is what the asterisk renders |
| Catalog `Required` | `ReportGroupAvailableField` | yes — adds parent-linkage obligations |
| Conditional `showAndRequire` | `PageLayoutField.JSONConfigText` | **never** |

**There is no fourth layer, and no per-placement required flag.**

## 25. Q-BBW-12 answered: a root renders if and only if a record of its type exists

**The question open since §13 is resolved.** Four gates were eliminated — build version, the `Firm`
entitlement flag, the seeded menu structure, and per-user-class page access — all confirmed open at
American Freight while the `Equipment Contract` root still refused to render.

**The fourth gate is row count.**

> **A navigation root renders if and only if the firm holds at least one record of that root's
> `ProjectEntity` type.** Entitlement is necessary but not sufficient.

### The discriminating measurement

**Observed**, verified independently for this document against both tenants, format-agnostically
(BBW's REST surface answered in JSON on one call and XML on another — counting must not assume
either):

```
GET /rest/businessObject/Contract/details?fields=ProjectEntityTypeName&$top=5000
```

| Tenant | Contracts returned | typed `Equipment Contract` | `Equipment Contract` root |
|---|---:|---:|:--:|
| **BBW** | 2,014 | **1** | **renders** |
| **American Freight** | 2 | **0** | **does not render** |

**One record is the entire difference.** BBW's whole Equipment Contract module — 32 navigation nodes,
26 screens, a root in the main menu — is switched on by a single row.

### It explains the `Program` anomaly too, which is what makes it the answer

§13 recorded that `Program` is granted by all ten user classes at AF and also fails to render — and
that any candidate gate had to explain **both** anomalies. This one does, via a naming subtlety:

**AF's `Program` table rows carry `ProjectEntityTypeName = "Portfolio"`, not `"Program"`.** So the
menu structure named **`Portfolio`** (id 924) matches three real entities and renders, while the
separate structure named **`Program`** (id 3851) matches **zero** and does not. Two structures, one
table, different type strings — and the rule holds for both.

This also retires the conflation warning from §13: the root *labelled* `Portfolio` was never the
hidden one.

### The threshold is existence, not volume

BBW's `Program` **table** holds only **two** rows — and they are typed `"Portfolio"`, which is what
makes the **Portfolio** root render, normally, alongside `Location`, `Facility` and `Contract` at
~2,000 records each. **One row is enough; there is no "meaningfully populated" threshold.**

> **Read the table name and you will get this wrong.** *Neither tenant renders a root named
> `Program`.* Nothing in either tenant is typed `"Program"`, so structure 3851 stays hidden in both.
> A row reading *"Program — 2 records — renders"* means *"the Program **table** holds 2 rows, typed
> Portfolio, so the **Portfolio** root renders"*. Mistaking the **table** name for the
> **`ProjectEntityTypeName`** is precisely what made `Program` look like an unexplained anomaly and
> killed the three-gate model.

### Confidence, and the honest caveat

**Inferred, not Observed as a mechanism.** This is an 11-for-11 correlation across two tenants, not a
reading of the server's rendering code. **The falsifier is specific and worth stating:** a tenant with
the entitlement on, the type registered, page access granted and **zero rows** that *still* renders
the root would disprove it.

**The circularity objection, and why `Equipment Contract` escapes it.** Record existence could be a
*consequence* rather than a cause — nobody creates records for a module they cannot see.
`Equipment Contract` breaks that loop twice over:

1. **AF holds the entitlement and could therefore have created one.** It has not, and the root stays
   hidden.
2. **The `EquipmentContract` objectType is registered and live at AF** — `HTTP 200` with zero rows,
   against `HTTP 400 unknown objectType` for `Site`, `Equipment` and `OpeningProject`.
   **Not-provisioned and not-populated are distinguishable, and AF is the latter.**

That second point also eliminates **type registration** as the gate — which had been the leading
alternative candidate.

**AF's zero was verified three ways**, because a false zero was the obvious failure mode: the
`Contract/details` type scan, the dedicated `EquipmentContract` endpoint, and a **spelling control** —
`Equipment%20Contract` returns `400 unknown objectType`, proving the no-space form is the right one
and the zero is real rather than a typo. (FIQL was not used; it silently returns `{}` — §"FIQL".)

### What this means for ASG Edge+

**Navigation visibility in the incumbent is data-driven, not configuration-driven.** A rebuild that
models navigation purely from entitlements and layouts will show empty roots the incumbent hides —
and a tenant's menu will change shape as its first record of a type is created. That is either a
feature to reproduce deliberately or a behaviour to reject deliberately, but it should not be
discovered by accident.

It also explains §9 and §17 more cleanly than "BBW is the more advanced fork" ever did: **BBW differs
from AF by one feature, and that feature is visible because one row exists.**

## Open questions

| ID | Question | How to settle it |
|---|---|---|
| **Q-BBW-01** | ~~Is code-table `delete` suppressed by reference count?~~ **Answered: NO — and §3 retracts the inference built on it.** It is a server-supplied per-row boolean `isReadOnlyRecord`, read straight from the grid renderer; the AF/BBW difference was a *build* difference and has vanished now both run `26.09.0.113`. Remaining: what sets the flag (provenance is the best-supported guess, unproven). | Compare the same `LxBOID` across both tenants: identical flag supports provenance; differing flag disproves it. |
| **Q-BBW-02** | Why is `Capital Lease Test` dropped from `Equipment Contract` while `ASC 842 Test` is kept? It is not retail-specific, so the generic/specific reading does not explain it. | Open both `Accounting Info` groups and compare. Likely that `Capital Lease Test` is the legacy FAS 13 test and equipment leases were only ever onboarded post-842 — if so, ASG Edge+ can omit it for equipment too. |
| **Q-BBW-03** | **What does a `Task` step actually do?** Answered in part: `Task` and `Form` are the two step types, named in the product's own code — but across two tenants, 13 templates and 62 steps, **zero** Task steps are configured. Does ASG use them at all? | Ask the business before building the concept. To observe one, a Task step would have to be created, which is a **write** and out of scope for read-only exploration. |
| **Q-BBW-04** | ~~Does any layout carry a populated `conditionalFieldsConfig`?~~ **CLOSED — §11.** Yes: 8 layouts, 50 records. The earlier "zero populated" was a false negative. Open blocker #1 is solved. Residual: the full operator-code vocabulary (only `2`=in and `17`=not in observed) and whether `crtOpt2`/`crtVal2` exist. | Read more tenants, or find the validator's operator list in the builder JS. |
| **Q-BBW-09** | ~~What does the 5-step contract wizard collect?~~ **Answered in §10.** Follow-ons: (a) **Contract templates** drive steps 3-4 but no `ContractTemplate` object exists in the census — what backs them? (b) Step 1 writes `Facility_OpenDate`/`CloseDate`, so creation spans two entities — is that transactional? | (a) `ShowObjectDetails.jsp` on the wizard-template dropdown's source. (b) Open a contract record and check whether Facility dates round-trip. |
| **Q-BBW-13** | ~~Are ~34 tables absent from the census?~~ **Largely answered — §12.** Reconciled on physical name, only **6** are genuine gaps (4 of them the undocumented `Punch List` family); 12 were label mismatches. **31 of 227 undocumented = 6 omissions + 25 viewer refusals.** Residual: field detail for the 25 refusals, recoverable via `GET /rest/businessObject/{type}/lxid/{id}?deep=true` (§14) — and `PageLayout` is still absent from the census while the reporting module depends on it. | Pull the 25 over REST. Note the serialiser emits only populated columns, so results are a lower bound. |
| **Q-BBW-16** | ~~Is the `Punch List` family in scope?~~ **CLOSED — §12: no.** Zero coverage across all 38 approved BRDs (control term verified), and the BRDs place construction management in the *separate* legacy ASG Edge product. Document for census completeness only. **In-scope census gap is now just two one-field tables.** | — |
| **Q-BBW-14** | ~~What are the REST endpoint shapes?~~ **CLOSED — §14.** Full OpenAPI 3.0.1 at `/rest/api-docs/swagger`: 141 paths, 160 operations, 40 POST / 7 PUT / 9 DELETE. Open blocker #3 is solved. | — |
| **Q-BBW-19** | **An hourly inbound integration is running in a tenant we have been treating as training.** `Job Log` shows `BBW Transaction Update` executing every hour on the half-hour, initiated by `Lx Administrator`, each with an `LxHttpMsg…` input and an `LxDataImportLog_…` output — an external system posting transaction data over HTTP. Nothing in the corpus recorded this. **What is it, and is BBW actually a training tenant?** | Ask ASG. It changes the risk profile of any future write testing, and it means BBW carries live-shaped data. |
| **Q-BBW-20** | ~~Does the contract lifecycle live in a firm-defined drop-down?~~ **CLOSED — §23: yes.** `Lease Status`, 7 values, 4 of BRD-24's 5 stages. Residual: **`SortOrder` is null on all 7**, so no ordering is stored — a rebuild modelling an ordered state machine is making a decision, not migrating one. Confirm the intended sequence with whoever owns BRD-24. | Business question. |
| **Q-BBW-18** | **Has any ASC 842 / IFRS 16 schedule in either tenant ever been calculated against a real discount rate?** The rate table is empty in both (§18). Either the per-record override is the real path — in which case a rebuild must implement it, not the table — or the engine has never been exercised. | Ask ASG. Technically: open a contract with an ASC 842 schedule and check whether `Asset.DiscountRateOverride` / the `SLSummary` equivalent carry values. |
| **Q-BBW-17** | **Is AI lease abstraction in scope for ASG Edge+?** §17 shows a live Atlas integration with per-firm configurable field mapping, and BBW's entire layout advantage over AF serves it. No BRD reviewed so far mentions it. | A business question, not a technical one. Raise it — the answer determines whether ~7 layouts, a status value, an entitlement flag and an integration are in or out. |
| **Q-BBW-15** | Writes return `ImportResults` with `successes[]`/`errors[]`, so **HTTP 200 does not mean success**. What is the full `ImportError` vocabulary, and is a partial write transactional or does it leave a half-created aggregate? | Read the `ImportError`/`ImportResults` schemas in the captured spec; determining transactionality would require a write, which is out of scope under the read-only rule. |
| **Q-BBW-10** | ~~Do the 30 primary tables behind the 93 layouts appear in the census?~~ **Answered in §8:** 24 of 30 match by name; 2 are display aliases (`Portfolio`→`Program`, `Entity`→`ProjectEntity`); 2 are `Virtual*` projections; 1 (`Straight-Line Schedule`) is **ambiguous across three candidates**; 1 is on the abandoned `zdelete` layout. | Remaining: pin `Straight-Line Schedule` to one of `SLSummary` / `SLPeriod` / `CodeSLSchedule`. A `ShowObjectDetails.jsp` pass, or read the two layouts' placed fields. |
| **Q-BBW-12** | ~~What suppresses the `Equipment Contract` root when all known gates are open?~~ **ANSWERED — §25.** A root renders iff the firm holds ≥1 record of that `ProjectEntity` type. BBW has exactly one equipment contract and renders it; AF has zero and does not. The rule also explains `Program`. **Inferred** — an 11-for-11 correlation, not a reading of the rendering code; the falsifier is a tenant with zero rows that still renders the root. | To settle the mechanism rather than the correlation, find the render-time filter in the menu-tree build. |
| **Q-BBW-11** | Can a layout over a `Virtual*` projection be **written to**, or is it structurally read-only? The projections have no primary key. This decides whether ASG Edge+'s layout engine needs a read-only layout class. | Open `ASG Breakpoint Schedule` (98921) in the builder and check whether its fields are editable or display-only. |
| **Q-BBW-05** | ~~Does `Equipment Contract` have its own record type?~~ **Answered: yes.** Its `requestedProjectEntityType` is **`EquipmentContract`**, a distinct ProjectEntity type — not `Contract` with a discriminator at the navigation layer. The four shared roots resolve to `Program` / `Location` / `Facility` / `Contract`, confirming the atlas reading that "Portfolio" is `Program`. **The follow-on is now the real question:** the 223-object census contains **no `EquipmentContract` object**, so either the census is incomplete or the type maps onto `Contract` at the storage layer. | Resolve against a schema export. There is no BBW equivalent of `_lucernex_objects_summary.txt`, so this cannot be settled from the navigation alone. |
| **Q-BBW-06** | What is **`Conditional Workflow JS`**? A workflow-level rule mechanism holding **JavaScript**, entirely separate from the field-level `conditionalFieldsConfig`. Undocumented anywhere in this corpus. | Open a template that populates it. `ASC 842 Tracking` or `Cotenancy Update` are the likeliest candidates. |
| **Q-BBW-07** | Workflows **chain** — `Document Abstraction` is "kicked off by ... another work flow". What is the full kickoff graph across the 13 templates? | Read `KickOffDescription` and the kickoff action on each of the 13 via `formSubmit=viewBO`. Cheap; a single sweep. |
| **Q-BBW-08** | `Lease Admin Request` step 8 is named `Client Review of Estoppel` but points at form `LAR Submit Lease Admin Request(Approvers)`, and steps 5/6 share one form. Configuration error, or deliberate reuse? | Matters if these definitions are migrated. Open both steps. |

### Newly opened

| ID | Question | How to settle it |
|---|---|---|
| **Q-BBW-21** | ~~Why are `Contract Status` and `Location` painted red in the builder when neither is schema-required?~~ **CLOSED — §24.** On the rendered end-user screen **neither is marked required**. The builder's red text is an **editor affordance that does not reach the end user**. §22's three-layer model stands without exception. | — |
| **Q-BBW-24** | **Sub-screen addressability differs by entity type (§24).** Equipment Contract: none addressable. Contract: 14 of 46. A third of Contract's saved links would survive a migration; none of Equipment Contract's would. Is uniform routable deep-linking a requirement for ASG Edge+? | A product decision. Choosing routable URLs is an improvement but a departure — and the migration question is per-entity, not global. |
| **Q-BBW-22** | **Three sources give three firm-field counts** — 359 (census), 298 (the `showGlobal=false`differencing), 205 (`all-fields.csv`). They measure different populations and are **not reconciled**. No one of them should be quoted as authoritative. | Determine what each population actually is before publishing any firm-field total. |
| **Q-BBW-23** | The tenant holds **1,647 `PageLayout` rows** against the 93 in the Manage Page Layouts registry and 135 including form layouts. What are the other ~1,500? | Likely report layouts (`IsReport = true`), sub-layouts, and per-Issue-Type step layouts. `GET /rest/businessObject/PageLayout/details?fields=…` with a group-by would settle it. |

## Caveat on this document

A **single session against a training tenant**, in two passes (the first ended when two MCP instances
contended for one Chrome profile; the second recovered the session from the persisted browser
profile).

What is solid: counts of *screens*, *drop-down tables*, *workflow templates*, *steps* and *layouts*
are **Observed**, read from live components and from read-only `GET`s.

What is not: **nothing here comes from a vendor schema export for BBW** — there is no BBW equivalent
of `_lucernex_objects_summary.txt`, so no field-level or table-level claim is made. The
generic/specific reading of `Equipment Contract` is **Derived from the navigation diff alone**; no
`Equipment Contract` record was ever opened, and not one end-user screen in this tenant was rendered.
The reference-count explanation for code-table `delete` suppression (§3) is **Inferred** and has a
rival explanation still standing.

Approver identities were read in the course of capturing the step model and are **deliberately
excluded** from this corpus; only counts are recorded.
