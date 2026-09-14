---
title: Two files serve 56% of the product
tags: [finding, navigation, layouts]
evidence: Derived
---

**17 distinct JSP renderers serve all 105 routed screens**, and two of them serve **59 — 56%**:

| Renderer | Screens | Serves |
|---|---:|---|
| `/en/pagebuilder/PLForm.jsp` | **37** | a list — a grid of child records |
| `/en/pagebuilder/PForm.jsp` | **22** | a detail form — one record |
| `/en/issue/IssueList.jsp` | 8 | **Forms *and* Work Flow** (`?mode=WorkFlow`) |
| `/en/reports/SavedReportList.jsp` | 8 | Reports |
| `MemberDirectory.jsp` · `document/Index.jsp` · `PECommPkg.jsp` | 4 each | Members · Documents · Binders |
| 10 more files | 1–3 each | Gantt, org chart, demographics, work orders, lease maintenance |

They are the **same page builder in two modes** — **P**age **Form** and **P**age **L**ist **Form** —
and the layout's [[layout-modes|mode]] picks the renderer. **One layout registry, two renderers, and
the navigation is a table of layout ids.**

`requestedProjectEntityType` has four values and one parameter switches the entity:
Portfolio → **`Program`** (20 screens), Location (16), Facility (24), Contract (45). Everything else
stays the same.

Two structural facts fall out:

- **`Forms` and `Work Flow` are one screen** — `IssueList.jsp`, with a mode parameter. Consistent with
  [[form-vs-page|a Form being an Issue Type]].
- **A contract is a small header plus twenty-five collections** — `PForm.jsp` serves 7 of its screens
  plus 4 group landing pages; `PLForm.jsp` serves the other 25.

The split even encodes an accounting fact: `Capital Lease Test` is a **detail** form while
`ASC 842 Test` is a **list** — the ASC 840 test is one record per contract, the ASC 842 test produces
many rows.

See [[navigation-tree]] · [`screen-routing.md`](../../docs/data-model/screen-routing.md)
