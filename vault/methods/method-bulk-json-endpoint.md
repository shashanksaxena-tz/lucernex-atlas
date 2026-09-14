---
title: "Method: every admin grid has a bulk JSON endpoint"
tags: [method, meta]
evidence: Observed
---

Nearly every count in this vault comes from here rather than from counting rows in a screenshot.

```
{page}.jsp?ajaxList=true&ajax=true&popupList=true&BOType={type}&start=0&limit=5000
```

returns `{totalCount, topics[]}` — a whole screen in one request, instead of paging 15 rows at a time
through a [[caveat-viewport|viewport that truncates]].

It is how the configuration inventory was taken:

| Screen | `BOType` | [[tenant-bbw\|BBW]] |
|---|---|---:|
| Manage Drop Downs | `CustomCodeTable` | **207** |
| Manage Summary Page (`mode=SEP`) | `PageLayout` | 15 |
| Manage Sub Pages (`mode=SUB`) | `PageLayout` | **32** |
| Manage List Pages (`mode=LIST`) | `PageLayout` | **46** |
| Manage Custom Lists | `ReportGroupDataCustomList` | 6 |
| Work Flow Templates | `WorkFlowTemplate` | 13 |
| **Task Templates** | `TaskTemplate` | **0** |
| Process Timelines | `ProcessTimelineTemplate` | 0 |

That last zero is what explained [[finding-no-task-step-anywhere]].

**Note:** `/servlet/BOList` needs a session-bound `fdName` key and returns literal `null` without it.
Use the JSP route.

Other GET-only tricks that avoided UI interaction entirely: the
[[security-ladder|security]] class selector is a **GET parameter**
(`SecurityPageAccess.jsp?UserClass={id}`), and workflow step lists are already in the grid store's
`expandedHtml` field, so no template had to be opened in edit mode.

See [[caveat-viewport]]
