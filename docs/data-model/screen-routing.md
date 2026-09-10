# The screen routing table — how 81 screens are served by 17 files

**Stated up front.** Every entry in the end-user navigation carries a **`menuPLID`** — a Page Layout
ID — and a JSP route. Reading the whole menu tree out of its ExtJS component yields the complete
routing table for the application, and it collapses to something very small:

**59 of the 105 routed screens (56%) are served by exactly two files.**

| Renderer | Screens | What it is |
|---|---:|---|
| `/en/pagebuilder/PLForm.jsp` | **37** | A **list** — a grid of child records |
| `/en/pagebuilder/PForm.jsp` | **22** | A **detail form** — one record |
| `/en/issue/IssueList.jsp` | 8 | Forms and Work Flow |
| `/en/reports/SavedReportList.jsp` | 8 | Reports |
| `/en/project/MemberDirectory.jsp` | 4 | Members/Contacts |
| `/en/document/Index.jsp` | 4 | Documents |
| `/en/CommitteeDocuments/PECommPkg.jsp` | 4 | Binders |
| `/en/budget/BudgetColumnEdit.jsp` | 3 | Budget *(out of scope)* |
| `/en/reports/TaskGantt2.jsp` | 3 | Schedule — a Gantt chart |
| `/en/issue/WorkOrderList.jsp` | 2 | Work orders |
| `/en/admin/OrgChartEdit.jsp` | 2 | Org chart |
| `/en/project/ScoutDemographicInfo.jsp` | 2 | Demographics |
| `/en/admin/DemographicReportEdit.jsp` | 2 | Demographic criteria |
| 4 more | 1 each | Study areas, demographic facts, demographics study, lease maintenance |

Captured 2026-09-10, tenant `(ASG)American Freight`, build `26.08.0.46`, from the
`Lx.ui.MenuTree` component. Read-only. Machine-readable at
[`../mindmap/navtree.json`](../mindmap/navtree.json). Confidence: **Observed** throughout.

## What the two page-builder routes prove

`PForm.jsp` and `PLForm.jsp` are the *same page builder* in two modes: **P**age **Form** and
**P**age **L**ist **Form**. Together they render 56% of the application.

This closes a question that [008](../admin/008-manage-page-layouts.md) could only frame. That
document established that a page layout record can carry an **Edit Layout**, a **List Layout**, or
both, and that the three admin sub-tabs (Summary Pages, Sub-pages, List Layouts) are views over one
`PageLayoutID` record type. The routing table shows the consequence at runtime: **the layout's kind
picks the renderer.** A detail layout is served by `PForm.jsp`; a list layout by `PLForm.jsp`. Same
record type, same builder, two front doors.

For the rebuild that is the whole page-composition model in one sentence: *one layout registry, two
renderers, and the navigation is a table of layout ids.*

### It also explains the Contract screen mix

Of Contract's 39 screens, the split is telling:

- **`PForm.jsp` (detail)** — Summary, Abstract Details, Payment Details, Accounting Details,
  Accrual Details, Capital Lease Test, Percentage Rent Accruals, and the four group landing pages
- **`PLForm.jsp` (list)** — Terms, Amendments, Covenants, Key Dates, Responsibilities, Insurance,
  Co-Tenancy, Recurring Expenses, Alternate Rent, Transactions, Invoices, Receipts, Recoveries,
  Scheduled Offsets, Allowances, Security Deposit, Percentage Rent, Sales, Straight-Line Rent,
  Accounting Assumptions, ASC 842 Test, ASC 842 Rent Schedule, IFRS 16 Rent Schedule, Expense
  Accruals, Accrual Transactions

**Nearly everything under a contract is a list of child rows**, not a form. That matches the
one-to-many shape [009](../admin/009-related-fields-and-data-model.md) found: from the "one" side,
children appear as embedded grids. A contract is a small header plus twenty-five collections.

Note `Capital Lease Test` is a **detail** form while `ASC 842 Test` is a **list**. The older ASC 840
test is one record per contract; the ASC 842 test produces many rows. That is a real modelling
difference between the two standards' tests, visible only here.

## Forms and Work Flow are the same screen

**The strongest single confirmation in this document.** Both routes are `/en/issue/IssueList.jsp`.
The only difference is a query parameter:

```
Forms      /en/issue/IssueList.jsp?...
Work Flow  /en/issue/IssueList.jsp?mode=WorkFlow&...
```

A Form and a Work Flow are two filtered views of **one Issue list**. This independently confirms,
from the routing table, what
[`code-table-registry.md`](code-table-registry.md) established from `TableType=2035` and what
[`../modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`](../modules/layouts-and-forms/forms-vs-pages-vs-layouts.md)
established from the admin screens: **a Form is an Issue Type, and the record is an `Issue`.**

Three independent sources now agree — the code-table registry, the GraphQL `IssueInterface`, and
the URL the product actually navigates to.

## "Portfolio" is `Program`

**Observed.** Every route carries `requestedProjectEntityType`, and its four values are:

| Menu label | `requestedProjectEntityType` | Screens |
|---|---|---:|
| Portfolio | **`Program`** | 20 |
| Location | `Location` | 16 |
| Facility | `Facility` | 24 |
| Contract | `Contract` | 45 |

The menu says *Portfolio*; the platform says *Program*. The schema's object is `Program`
(`docs/mindmap/objects.json`), and `Contract.ProgramID` has declared type `Portfolio ID`. So three
names — Portfolio, Program, and the `Portfolio ID` FK type — all denote one thing. Any rebuild
glossary needs that mapping written down or the confusion is guaranteed.

More importantly: **one parameter switches the entity and everything else stays the same.** The same
`PForm.jsp` renders a Portfolio, a Location, a Facility or a Contract, differing only by layout id
and entity type. That is `ProjectEntity` polymorphism made operational — see
[`project-entity.md`](project-entity.md).

## The universal group, as routes

Every root's opening group resolves to the same five files:

| Screen | Route |
|---|---|
| Summary | `PForm.jsp` |
| Members/Contacts | `MemberDirectory.jsp` |
| Forms | `IssueList.jsp` |
| Work Flow | `IssueList.jsp?mode=WorkFlow` |
| Documents | `document/Index.jsp` |
| Binders | `CommitteeDocuments/PECommPkg.jsp` |
| Schedule | `reports/TaskGantt2.jsp` |

**Derived.** These seven capabilities are implemented once and inherited by every entity type. The
rebuild gets the same leverage only if it models the supertype first — building Contract, Facility
and Location independently would mean seven features built three times.

Two incidental discoveries: **Schedule is a Gantt chart** (`TaskGantt2.jsp`), which connects the
`Task`/`TaskPredecessor` objects to a real UI; and **Binders are "Committee Packages"**
(`PECommPkg.jsp`) — a document-assembly feature whose internal name suggests it was built for
committee submissions.

## Page Layout ID ranges

**Derived**, and useful for dating the product's features. Layout ids appear to be allocated in
issue order:

| Range | Screens |
|---|---|
| 900–1100 | Portfolio and Facility core |
| 3400–3600 | Location and Contract core, reports |
| 5400 | Facility demographics |
| 12000–13000 | Accounting Info, accruals, security deposit, facility expense |
| 15000–19000 | Alternate Rent, Scheduled Offsets |
| 41000–45000 | **ASC 842 Test, ASC 842 Rent Schedule, IFRS 16 Rent Schedule, Accounting Assumptions, Accounting Details, Accrual Info** |
| 51000 | Equipment across Portfolio/Location |
| 108382 | **Invoices** — the newest screen in the application |

The ASC 842 and IFRS 16 screens sit in a tight 41000–45000 band, well above the 12000-band
`Capital Lease Test`. **Inferred:** the lease-accounting-standard screens were added as one project,
long after the original capital-lease test, which is what you would expect of a 2019 standard
retrofitted to an older product. It is a useful signal for the rebuild about which parts are mature
and which are recent.

## Open questions

1. **What does `PForm.jsp` actually render for a real contract?** The routing is known; the output
   is not. This is the single most valuable next capture.
2. **Do these 81 screens vary by user class?** This is one user's menu. If `SecurityLevel` filters
   it, the menu is permission-driven data rather than fixed structure.
3. **What is `LeaseMaintenanceEdit.jsp`**, the sole route for Facility → Responsibilities, and why
   does Contract → Responsibilities use `PLForm.jsp` instead?
4. **`Scheduled Offsets` (19844) and `Recoveries` (3516)** are both list layouts under Payment Info
   — which schema tables back each?
5. **Are there menu entries this user cannot see?** 109 nodes were returned; the `Manage Top Menu`
   admin screen would say whether more exist.
