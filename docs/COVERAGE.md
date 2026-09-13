# Coverage — every known surface of Lucernex, and whether it is documented

**Stated up front.** Lucernex exposes **744 distinct surfaces** that this corpus has to account for: 141 end-user navigation nodes (108 of them leaf screens), 57 administration tools, 93 page layouts, 227 sql tables, 207 firm drop-downs, 13 workflow templates and 6 form types. This file is the scoreboard. It is **generated** — do not hand-edit it; edit [`tools/coverage-owners.json`](tools/coverage-owners.json) and re-run `python3 docs/tools/build_coverage.py`.

Two columns carry different weight, and the difference matters:

| Column | Means |
|---|---|
| **Owner doc** | A document that *explains* this surface. Curated by hand in `tools/coverage-owners.json`. This is the real coverage number. |
| **Named in** | A document whose text contains the surface name verbatim. Computed. Proves only that the name has been written down somewhere — **not** that it is understood. |
| **Shot** | A screenshot whose filename slug matches the surface name. |

**Granularity, stated honestly.** Page layouts, workflow templates, form types and the Equipment Contract screens are owned at **registry level**: the owning document enumerates every one of them with its mode, primary table and attachment, but does not walk each one field by field. Sql tables and drop-downs are deliberately left **unowned** — they have registry coverage in [`data-model/`](data-model/) and no document explains any of them individually.

Captured from `(ASG)BBW` (firmID 3159) and `(ASG)American Freight` (firmID 3158), both on build `26.09.0.113`, 2026-09-13. Confidence: **Derived** throughout — every row is a mechanical join over Observed captures.

## Scoreboard

| Surface class | Count | Owner doc | Named in some doc | Screenshot | Section |
|---|---:|---:|---:|---:|---|
| End-user navigation nodes (BBW) | 141 | 32 | — | — | [§1](#1-end-user-navigation-141-nodes) |
| — of which leaf screens | 108 | 26 | — | — | [§1](#1-end-user-navigation-141-nodes) |
| — of which have a captured route | 82 | — | — | — | [§1](#1-end-user-navigation-141-nodes) |
| Administration tools | 57 | 34 | 57 | 55 | [§2](#2-administration-tools-57) |
| Page layouts | 93 | 93 | 73 | — | [§3](#3-page-layouts-93) |
| Workflow templates | 13 | 13 | 13 | — | [§4](#4-workflow-templates-13-and-form-types-6) |
| Form types | 6 | 6 | 6 | — | [§4](#4-workflow-templates-13-and-form-types-6) |
| Firm drop-downs | 207 | 0 | 207 | — | [§5](#5-firm-drop-downs-207) |
| Sql tables | 227 | 0 | 163 | — | [§6](#6-sql-tables-227) |

> **Caveat on every field count below (severity HIGH, stated by the capture itself).** The sweep behind `bbw-platform-tables.json` passed `showGlobal=true`, which selects the schema viewer's **Global Fields** radio rather than *Global and Firm Fields*. Its 6,487 fields are the **global layer only** — firm (`Firm_`-prefixed) columns are absent by construction. `Contract` shows 307 fields there against **570** in the 223-object census. Treat every field and required count derived from it as a **lower bound**. Re-running with `showGlobal=false` would fix it.

Field-level depth already held: **202 of 227** sql tables have full field detail (6,785 fields with name, type, required flag, UI label, version added and max size); **25** are refused by the viewer. **202 of 227** appear in the 223-object census — **25 do not**, and those are the real blind spot.

## 1. End-user navigation (141 nodes)

`(ASG)BBW` carries **141** navigation nodes under **5** roots; `(ASG)American Freight` carries **109** under 4. All 109 AF `PageLayoutID`s are present in BBW unchanged, so **routes below are joined from the AF capture by `PageLayoutID`**; the **32** BBW-only nodes have no captured route yet.

> **A route is not an addressable URL.** These are the JSP routes the menu declares. Driving all 46 Contract nodes in a real browser found only **14 render standalone**; **22 return a full HTML document and then redirect client-side** to the default Summary, 8 are AccessDenied and 2 bounce server-side. `Equipment Contract` is not deep-linkable at all. See [`data-model/screen-routing.md`](data-model/screen-routing.md).

Source: [`mindmap/navtree-bbw.json`](mindmap/navtree-bbw.json), [`mindmap/navtree.json`](mindmap/navtree.json), [`data-model/screen-routing.md`](data-model/screen-routing.md).

| Path | Kind | PageLayoutID | Route | Entity | In AF? | Owner doc | Named in |
|---|---|---:|---|---|:--:|---|---|
| Portfolio | group | `924` | `—` | Program | yes | — | — |
| Portfolio : Details | group | `935` | `/en/pagebuilder/PForm.jsp` | Program | yes | — | — |
| Portfolio : Details : Summary | screen | `936` | `/en/pagebuilder/PForm.jsp` | Program | yes | — | [README.md](features/page-layouts/README.md) |
| Portfolio : Details : Members/Contacts | screen | `938` | `/en/project/MemberDirectory.jsp` | Program | yes | — | [004-company-administration.md](admin/004-company-administration.md), [screen-routing.md](data-model/screen-routing.md) +9 |
| Portfolio : Details : Forms | screen | `939` | `/en/issue/IssueList.jsp` | Program | yes | — | *name too generic to measure* |
| Portfolio : Details : Work Flow | screen | `2283` | `/en/issue/IssueList.jsp?mode=WorkFlow` | Program | yes | — | *name too generic to measure* |
| Portfolio : Details : Documents | screen | `937` | `/en/document/Index.jsp` | Program | yes | — | *name too generic to measure* |
| Portfolio : Details : Binders | screen | `931` | `/en/CommitteeDocuments/PECommPkg.jsp` | Program | yes | — | *name too generic to measure* |
| Portfolio : Details : Budget | screen | `1109` | `/en/budget/BudgetColumnEdit.jsp` | Program | yes | — | *name too generic to measure* |
| Portfolio : Demographics | group | `925` | `/en/admin/DemographicReportEdit.jsp` | Program | yes | — | — |
| Portfolio : Demographics : Criteria | screen | `928` | `/en/admin/DemographicReportEdit.jsp` | Program | yes | — | [005-manage-data-fields.md](admin/005-manage-data-fields.md), [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +14 |
| Portfolio : Demographics : Study Areas | screen | `927` | `/en/admin/DemographicStudyAreaEdit.jsp` | Program | yes | — | [003-main-navigation.md](screens/003-main-navigation.md) |
| Portfolio : Demographics : Demographics | screen | `926` | `/en/admin/DemographicFactEditForm.jsp` | Program | yes | — | [005-manage-data-fields.md](admin/005-manage-data-fields.md), [INDEX.md](data-fields/INDEX.md) +13 |
| Portfolio : Org Chart | group | `933` | `/en/admin/OrgChartEdit.jsp` | Program | yes | — | — |
| Portfolio : Org Chart : Org Chart | screen | `934` | `/en/admin/OrgChartEdit.jsp` | Program | yes | — | [004-company-administration.md](admin/004-company-administration.md), [link-member-project-entity.md](data-fields/link-member-project-entity.md) +12 |
| Portfolio : Facility / Store List | group | `4854` | `/en/pagebuilder/PLForm.jsp` | Program | yes | — | — |
| Portfolio : Facility / Store List : Facility / Store List | screen | `4862` | `/en/pagebuilder/PLForm.jsp` | Program | yes | — | [003-main-navigation.md](screens/003-main-navigation.md) |
| Portfolio : Equipment | group | `51793` | `/en/pagebuilder/PLForm.jsp` | Program | yes | — | — |
| Portfolio : Equipment : Equipment | screen | `51809` | `/en/pagebuilder/PLForm.jsp` | Program | yes | — | *name too generic to measure* |
| Portfolio : Reports | group | `3573` | `/en/reports/SavedReportList.jsp` | Program | yes | — | — |
| Portfolio : Reports : Program Reports | screen | `3574` | `/en/reports/SavedReportList.jsp` | Program | yes | — | [003-main-navigation.md](screens/003-main-navigation.md) |
| Location | group | `3535` | `—` | Location | yes | — | — |
| Location : Details | group | `3536` | `/en/pagebuilder/PForm.jsp` | Location | yes | — | — |
| Location : Details : Summary | screen | `3537` | `/en/pagebuilder/PForm.jsp` | Location | yes | — | [README.md](features/page-layouts/README.md) |
| Location : Details : Members/Contacts | screen | `3542` | `/en/project/MemberDirectory.jsp` | Location | yes | — | [004-company-administration.md](admin/004-company-administration.md), [screen-routing.md](data-model/screen-routing.md) +9 |
| Location : Details : Forms | screen | `3543` | `/en/issue/IssueList.jsp` | Location | yes | — | *name too generic to measure* |
| Location : Details : Work Flow | screen | `3544` | `/en/issue/IssueList.jsp?mode=WorkFlow` | Location | yes | — | *name too generic to measure* |
| Location : Details : Documents | screen | `3545` | `/en/document/Index.jsp` | Location | yes | — | *name too generic to measure* |
| Location : Details : Binders | screen | `3546` | `/en/CommitteeDocuments/PECommPkg.jsp` | Location | yes | — | *name too generic to measure* |
| Location : Details : Schedule | screen | `3547` | `/en/reports/TaskGantt2.jsp` | Location | yes | — | *name too generic to measure* |
| Location : Details : Budget | screen | `3548` | `/en/budget/BudgetColumnEdit.jsp` | Location | yes | — | *name too generic to measure* |
| Location : Complex/Center | group | `3549` | `/en/pagebuilder/PForm.jsp` | Location | yes | — | — |
| Location : Complex/Center : Complex/Center Details | screen | `3551` | `/en/pagebuilder/PForm.jsp` | Location | yes | — | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +4 |
| Location : Equipment | group | `51796` | `/en/pagebuilder/PLForm.jsp` | Location | yes | — | — |
| Location : Equipment : Equipment | screen | `51810` | `/en/pagebuilder/PLForm.jsp` | Location | yes | — | *name too generic to measure* |
| Location : Equipment : Work Orders | screen | `51811` | `/en/issue/WorkOrderList.jsp` | Location | yes | — | *name too generic to measure* |
| Location : Reports | group | `3556` | `/en/reports/SavedReportList.jsp` | Location | yes | — | — |
| Location : Reports : Location Reports | screen | `3557` | `/en/reports/SavedReportList.jsp` | Location | yes | — | [003-main-navigation.md](screens/003-main-navigation.md) |
| Facility | group | `1005` | `—` | Facility | yes | — | — |
| Facility : Details | group | `1006` | `/en/pagebuilder/PForm.jsp` | Facility | yes | — | — |
| Facility : Details : Summary | screen | `1007` | `/en/pagebuilder/PForm.jsp` | Facility | yes | — | [README.md](features/page-layouts/README.md) |
| Facility : Details : Members/Contacts | screen | `1009` | `/en/project/MemberDirectory.jsp` | Facility | yes | — | [004-company-administration.md](admin/004-company-administration.md), [screen-routing.md](data-model/screen-routing.md) +9 |
| Facility : Details : Forms | screen | `1010` | `/en/issue/IssueList.jsp` | Facility | yes | — | *name too generic to measure* |
| Facility : Details : Work Flow | screen | `2286` | `/en/issue/IssueList.jsp?mode=WorkFlow` | Facility | yes | — | *name too generic to measure* |
| Facility : Details : Documents | screen | `1013` | `/en/document/Index.jsp` | Facility | yes | — | *name too generic to measure* |
| Facility : Details : Binders | screen | `1030` | `/en/CommitteeDocuments/PECommPkg.jsp` | Facility | yes | — | *name too generic to measure* |
| Facility : Details : Schedule | screen | `1008` | `/en/reports/TaskGantt2.jsp` | Facility | yes | — | *name too generic to measure* |
| Facility : Details : Budget | screen | `1011` | `/en/budget/BudgetColumnEdit.jsp` | Facility | yes | — | *name too generic to measure* |
| Facility : Demographics | group | `5420` | `/en/project/ScoutDemographicInfo.jsp` | Facility | yes | — | — |
| Facility : Demographics : Summary | screen | `5431` | `/en/project/ScoutDemographicInfo.jsp` | Facility | yes | — | *name too generic to measure* |
| Facility : Demographics : Demographics Study | screen | `5432` | `/en/project/DemographicsStudy.jsp` | Facility | yes | — | [003-main-navigation.md](screens/003-main-navigation.md) |
| Facility : Asset Management | group | `3525` | `/en/pagebuilder/PLForm.jsp` | Facility | yes | — | — |
| Facility : Asset Management : Equipment (FF&E) | screen | `1036` | `/en/pagebuilder/PLForm.jsp` | Facility | yes | — | [README.md](modules/assets-equipment/README.md), [data-model.md](modules/assets-equipment/data-model.md) +1 |
| Facility : Asset Management : Service Requests / Work Orders | screen | `3526` | `/en/issue/WorkOrderList.jsp` | Facility | yes | — | [README.md](modules/assets-equipment/README.md), [003-main-navigation.md](screens/003-main-navigation.md) |
| Facility : Space Management | group | `3527` | `/en/pagebuilder/PLForm.jsp` | Facility | yes | — | — |
| Facility : Space Management : Space Management | screen | `3528` | `/en/pagebuilder/PLForm.jsp` | Facility | yes | — | [README.md](modules/facilities-locations/README.md), [rules.md](modules/facilities-locations/rules.md) +2 |
| Facility : Facility Expense | group | `13239` | `/en/pagebuilder/PLForm.jsp` | Facility | yes | — | — |
| Facility : Facility Expense : Facility Expense | screen | `13240` | `/en/pagebuilder/PLForm.jsp` | Facility | yes | — | [facility-expense.md](data-fields/facility-expense.md), [space-management.md](modules/facilities-locations/space-management.md) +1 |
| Facility : Pro Forma Lease | group | `1014` | `/en/pagebuilder/PForm.jsp` | Facility | yes | — | — |
| Facility : Pro Forma Lease : Pro Forma Lease | screen | `5421` | `/en/pagebuilder/PForm.jsp` | Facility | yes | — | [005-manage-data-fields.md](admin/005-manage-data-fields.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +5 |
| Facility : Pro Forma Lease : Responsibilities | screen | `1015` | `/en/lease/LeaseMaintenanceEdit.jsp` | Facility | yes | — | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [screen-routing.md](data-model/screen-routing.md) +5 |
| Facility : Reports | group | `3533` | `/en/reports/SavedReportList.jsp` | Facility | yes | — | — |
| Facility : Reports : Facility Reports | screen | `3534` | `/en/reports/SavedReportList.jsp` | Facility | yes | — | [003-main-navigation.md](screens/003-main-navigation.md) |
| Contract | group | `3492` | `—` | Contract | yes | — | — |
| Contract : Details | group | `3493` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | — |
| Contract : Details : Summary | screen | `3494` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +3 |
| Contract : Details : Members/Contacts | screen | `3495` | `/en/project/MemberDirectory.jsp` | Contract | yes | — | [004-company-administration.md](admin/004-company-administration.md), [screen-routing.md](data-model/screen-routing.md) +9 |
| Contract : Details : Forms | screen | `3496` | `/en/issue/IssueList.jsp` | Contract | yes | — | *name too generic to measure* |
| Contract : Details : Work Flow | screen | `3497` | `/en/issue/IssueList.jsp?mode=WorkFlow` | Contract | yes | — | *name too generic to measure* |
| Contract : Details : Documents | screen | `3498` | `/en/document/Index.jsp` | Contract | yes | — | *name too generic to measure* |
| Contract : Details : Binders | screen | `3499` | `/en/CommitteeDocuments/PECommPkg.jsp` | Contract | yes | — | *name too generic to measure* |
| Contract : Details : Schedule | screen | `3500` | `/en/reports/TaskGantt2.jsp` | Contract | yes | — | *name too generic to measure* |
| Contract : Abstract Info | group | `3502` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | — |
| Contract : Abstract Info : Abstract Details | screen | `3503` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Contract : Abstract Info : Terms | screen | `3504` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Abstract Info : Amendments | screen | `3505` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Abstract Info : Covenants | screen | `3506` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Abstract Info : Key Dates | screen | `3507` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Abstract Info : Responsibilities | screen | `3508` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Abstract Info : Insurance | screen | `3509` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | *name too generic to measure* |
| Contract : Abstract Info : Co-Tenancy | screen | `3510` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info | group | `3512` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | — |
| Contract : Payment Info : Payment Details | screen | `3513` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Recurring Expenses | screen | `3514` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Alternate Rent | screen | `15951` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Transactions | screen | `3518` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Invoices | screen | `108382` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Receipts | screen | `3519` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Recoveries | screen | `3516` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Scheduled Offsets | screen | `19844` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [scheduled-offset.md](data-fields/scheduled-offset.md), [screen-routing.md](data-model/screen-routing.md) +4 |
| Contract : Payment Info : Allowances | screen | `3517` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Security Deposit | screen | `12444` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Payment Info : Percentage Rent | screen | `3515` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Contract : Payment Info : Sales | screen | `3520` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Accounting Info | group | `12293` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | — |
| Contract : Accounting Info : Accounting Details | screen | `45615` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | [screen-routing.md](data-model/screen-routing.md), [README.md](features/equipment-contracts/README.md) +1 |
| Contract : Accounting Info : Capital Lease Test | screen | `12295` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | [screen-routing.md](data-model/screen-routing.md), [README.md](features/equipment-contracts/README.md) +4 |
| Contract : Accounting Info : Straight-Line Rent | screen | `12445` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Accounting Info : Accounting Assumptions | screen | `43784` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +12 |
| Contract : Accounting Info : ASC 842 Test | screen | `41136` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [screen-routing.md](data-model/screen-routing.md), [README.md](features/equipment-contracts/README.md) +6 |
| Contract : Accounting Info : ASC 842 Rent Schedule | screen | `43785` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [README.md](features/page-layouts/README.md) |
| Contract : Accounting Info : IFRS 16 Rent Schedule | screen | `45609` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [contract.md](data-fields/contract.md), [screen-routing.md](data-model/screen-routing.md) +6 |
| Contract : Accrual Info | group | `45610` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | — |
| Contract : Accrual Info : Accrual Details | screen | `12294` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | [screen-routing.md](data-model/screen-routing.md), [README.md](features/equipment-contracts/README.md) +2 |
| Contract : Accrual Info : Expense Accruals | screen | `12297` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [contract.md](data-fields/contract.md), [README.md](features/equipment-contracts/README.md) +2 |
| Contract : Accrual Info : Transactions | screen | `12298` | `/en/pagebuilder/PLForm.jsp` | Contract | yes | — | [graphql-api.md](data-model/graphql-api.md), [screen-routing.md](data-model/screen-routing.md) +8 |
| Contract : Accrual Info : Percentage Rent Accruals | screen | `12296` | `/en/pagebuilder/PForm.jsp` | Contract | yes | — | [contract.md](data-fields/contract.md), [screen-routing.md](data-model/screen-routing.md) +3 |
| Contract : Reports | group | `3521` | `/en/reports/SavedReportList.jsp` | Contract | yes | — | — |
| Contract : Reports : Contract Reports | screen | `3522` | `/en/reports/SavedReportList.jsp` | Contract | yes | — | [README.md](features/equipment-contracts/README.md), [003-main-navigation.md](screens/003-main-navigation.md) +1 |
| Equipment Contract | group | `41087` | `(BBW-only, not captured)` | EquipmentContract | **BBW only** | [README.md](features/equipment-contracts/README.md) | — |
| Equipment Contract : Details | group | `41094` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | — |
| Equipment Contract : Details : Summary | screen | `41095` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Details : Members/Contacts | screen | `41128` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [004-company-administration.md](admin/004-company-administration.md), [screen-routing.md](data-model/screen-routing.md) +9 |
| Equipment Contract : Details : Forms | screen | `41129` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Details : Work Flow | screen | `41130` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Details : Documents | screen | `41131` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Abstract Info | group | `41090` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | — |
| Equipment Contract : Abstract Info : Abstract Details | screen | `41091` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [INDEX.md](INDEX.md), [screen-routing.md](data-model/screen-routing.md) +5 |
| Equipment Contract : Abstract Info : Terms | screen | `41117` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Abstract Info : Amendments | screen | `41114` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Abstract Info : Covenants | screen | `41115` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Abstract Info : Key Dates | screen | `41120` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Abstract Info : Responsibilities | screen | `41121` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [screen-routing.md](data-model/screen-routing.md) +5 |
| Equipment Contract : Abstract Info : Insurance | screen | `41122` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Payment Info | group | `41092` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | — |
| Equipment Contract : Payment Info : Payment Details | screen | `41093` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [screen-routing.md](data-model/screen-routing.md) +4 |
| Equipment Contract : Payment Info : Recurring Payments | screen | `41116` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [README.md](features/equipment-contracts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Equipment Contract : Payment Info : Transactions | screen | `41123` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [graphql-api.md](data-model/graphql-api.md), [screen-routing.md](data-model/screen-routing.md) +8 |
| Equipment Contract : Payment Info : Receipts | screen | `41124` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Payment Info : Scheduled Offsets | screen | `41125` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [scheduled-offset.md](data-fields/scheduled-offset.md), [screen-routing.md](data-model/screen-routing.md) +4 |
| Equipment Contract : Payment Info : Allowances | screen | `41126` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | *name too generic to measure* |
| Equipment Contract : Payment Info : Security Deposit | screen | `41127` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [lease-info.md](data-fields/lease-info.md) +11 |
| Equipment Contract : Accounting Info | group | `41118` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | — |
| Equipment Contract : Accounting Info : Accounting Details | screen | `45607` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [screen-routing.md](data-model/screen-routing.md), [README.md](features/equipment-contracts/README.md) +1 |
| Equipment Contract : Accounting Info : Straight-Line Rent | screen | `41153` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [screen-routing.md](data-model/screen-routing.md), [README.md](features/equipment-contracts/README.md) +3 |
| Equipment Contract : Accounting Info : Accounting Assumptions | screen | `43781` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +12 |
| Equipment Contract : Accounting Info : ASC 842 Test | screen | `41152` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [screen-routing.md](data-model/screen-routing.md), [README.md](features/equipment-contracts/README.md) +6 |
| Equipment Contract : Accounting Info : ASC 842 Rent Schedule | screen | `43782` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [INDEX.md](INDEX.md), [screen-routing.md](data-model/screen-routing.md) +5 |
| Equipment Contract : Accounting Info : IFRS 16 Rent Schedule | screen | `41151` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [contract.md](data-fields/contract.md), [screen-routing.md](data-model/screen-routing.md) +6 |
| Equipment Contract : Reports | group | `41119` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | — |
| Equipment Contract : Reports : Equipment Contract Reports | screen | `41154` | `(BBW-only, not captured)` | — | **BBW only** | [README.md](features/equipment-contracts/README.md) | [README.md](features/equipment-contracts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |

## 2. Administration tools (57)

The BBW admin dashboard lists **57** tools; AF lists **63**. **6** appear on AF and not on BBW: `Document Content Code`, `Document Type Code`, `Export Schema`, `Job Function Code`, `Job Title Code`, `User Class Code`.

Source: [`tenants/bbw-platform-inventory.json`](tenants/bbw-platform-inventory.json) (`DashboardDispatchOld.jsp?dashboardName=admin`).

| Tool | Route | Owner doc | Shot | Named in |
|---|---|---|---|---|
| Audit Reports | `/en/reports/AuditReport.jsp` | [README.md](features/security-access/README.md) | `af-admin/53-audit-reports.jpg`, `bbw-admin/47-audit-reports.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +5 |
| Client Drop Downs | `/en/admin/CustomCodeTableEdit.jsp` | [README.md](features/drop-downs-code-tables/README.md) | `af-admin/29-client-drop-downs.jpg`, `bbw-admin/28-client-drop-downs.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +16 |
| Data Conversion Cleaner | `/en/admin/lxadmin/DataLoadTweaks.jsp` | — | `af-admin/58-data-conversion-cleaner.jpg`, `bbw-admin/51-data-conversion-cleaner.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| Delete Entities | `/en/admin/lxadmin/DeleteEntities.jsp` | — | `af-admin/64-delete-entities.jpg`, `bbw-admin/55-delete-entities.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| Email Log | `/en/reports/EMailLogs.jsp` | — | `af-admin/54-email-log.jpg`, `bbw-admin/48-email-log.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +7 |
| Export Configuration | `/en/admin/MessengerExportData.jsp` | [README.md](features/import-export/README.md) | `af-admin/15-export-configuration.jpg`, `bbw-admin/14-export-configuration.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +9 |
| Generate Enterprise Report File | `/en/admin/GenBaseReport.jsp` | — | `af-admin/62-generate-enterprise-report-file.jpg`, `bbw-admin/53-generate-enterprise-report-file.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +3 |
| GraphQL Explorer | `/en/admin/graphql.jsp` | [graphql-api.md](data-model/graphql-api.md) | — | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +12 |
| Import Best Practice Templates | `/en/admin/BestPracticeTemplates.jsp` | [README.md](features/import-export/README.md) | `af-admin/14-import-best-practice-templates.jpg`, `bbw-admin/13-import-best-practice-templates.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +3 |
| Import Data | `/en/admin/Messenger.jsp` | [README.md](features/import-export/README.md) | `af-admin/13-import-data.jpg`, `bbw-admin/12-import-data.jpg` | [004-company-administration.md](admin/004-company-administration.md), [005-manage-data-fields.md](admin/005-manage-data-fields.md) +7 |
| Job Log | `/en/admin/JobLogEdit.jsp` | [README.md](features/import-export/README.md) | `af-admin/16-job-log.jpg`, `bbw-admin/15-job-log.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +7 |
| Layout Changes | `/en/admin/ShowLayoutChanges.jsp` | [README.md](features/page-layouts/README.md) | `af-admin/63-layout-changes.jpg`, `bbw-admin/54-layout-changes.jpg` | [004-company-administration.md](admin/004-company-administration.md), [005-manage-data-fields.md](admin/005-manage-data-fields.md) +7 |
| Manage Bid Package Templates | `/en/admin/BidPackageTemplate.jsp` | — | `af-admin/19-manage-bid-package-templates.jpg`, `bbw-admin/18-manage-bid-package-templates.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Binder Templates | `/en/CommitteeDocuments/BinderTemplateEdit.jsp` | — | `af-admin/05-manage-binder-templates.jpg`, `bbw-admin/04-manage-binder-templates.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| Manage Budget Index Variables | `/en/budget/BudgetIndexEdit.jsp` | — | `af-admin/24-manage-budget-index-variables.jpg`, `bbw-admin/23-manage-budget-index-variables.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Budget Summary Page | `/en/budget/BudgetSummaryEdit.jsp` | — | `af-admin/23-manage-budget-summary-page.jpg`, `bbw-admin/22-manage-budget-summary-page.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Budget Templates | `/en/budget/BudgetTemplateEdit.jsp` | — | `af-admin/20-manage-budget-templates.jpg`, `bbw-admin/19-manage-budget-templates.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Budget Types | `/en/budget/BudgetColumnTypeEdit.jsp` | — | `af-admin/22-manage-budget-types.jpg`, `bbw-admin/21-manage-budget-types.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Budget Views | `/en/budget/BudgetLayoutView.jsp` | — | `af-admin/21-manage-budget-views.jpg`, `bbw-admin/20-manage-budget-views.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage CPI Data | `/en/admin/ManageCPIData.jsp` | [README.md](features/reference-data/README.md) | `af-admin/27-manage-cpi-data.jpg`, `bbw-admin/26-manage-cpi-data.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| Manage Company | `/en/admin/FirmEdit.jsp` | [004-company-administration.md](admin/004-company-administration.md) | `af-admin/02-manage-company.jpg`, `bbw-admin/01-manage-company.jpg` | [004-company-administration.md](admin/004-company-administration.md), [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +6 |
| Manage Complex/Center Details | `/en/admin/ComplexEdit.jsp` | — | `af-admin/46-manage-complex-center-details.jpg`, `bbw-admin/42-manage-complex-center-details.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Contracts | `/en/admin/ContractEdit.jsp` | — | `af-admin/44-manage-contracts.jpg`, `bbw-admin/40-manage-contracts.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Custom Lists | `/en/admin/CustomListEdit.jsp` | [README.md](features/custom-lists/README.md) | `af-admin/07-manage-custom-lists.jpg`, `bbw-admin/06-manage-custom-lists.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +10 |
| Manage Dashboard Reports | `/en/reports/ManageDashboardModules.jsp` | [admin-tools.md](modules/reporting/admin-tools.md) | `af-admin/12-manage-dashboard-reports.jpg`, `bbw-admin/11-manage-dashboard-reports.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +5 |
| Manage Data Fields | `/en/pagebuilder/ReportGroupAvailableFieldEdit.jsp` | [README.md](features/data-fields/README.md) | `af-admin/11-manage-data-fields.jpg`, `bbw-admin/10-manage-data-fields.jpg` | [CONVENTIONS.md](CONVENTIONS.md), [INDEX.md](INDEX.md) +43 |
| Manage Discount Rates | `/en/admin/ManageDiscountRates.jsp` | [README.md](features/reference-data/README.md) | `af-admin/26-manage-discount-rates.jpg`, `bbw-admin/25-manage-discount-rates.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +5 |
| Manage Employer Members | `/en/admin/ManageEmployerMembers.jsp` | — | `af-admin/35-manage-employer-members.jpg`, `bbw-admin/34-manage-employer-members.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| Manage Employers | `/en/admin/EmployerEdit.jsp` | [README.md](modules/people-parties/README.md) | `af-admin/36-manage-employers.jpg`, `bbw-admin/35-manage-employers.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +3 |
| Manage Exchange Rates | `/en/admin/ManageCurrencyRates.jsp` | [README.md](features/reference-data/README.md) | `af-admin/25-manage-exchange-rates.jpg`, `bbw-admin/24-manage-exchange-rates.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| Manage Facilities | `/en/admin/FacilityEditForm.jsp` | — | `af-admin/43-manage-facilities.jpg`, `bbw-admin/39-manage-facilities.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Firm Dictionary | `/en/admin/Dictionary.jsp` | [README.md](features/administration/README.md) | `af-admin/18-manage-firm-dictionary.jpg`, `bbw-admin/17-manage-firm-dictionary.jpg` | [CONVENTIONS.md](CONVENTIONS.md), [004-company-administration.md](admin/004-company-administration.md) +2 |
| Manage Firm Drop Downs | `/en/admin/FirmCodeList.jsp` | [README.md](features/drop-downs-code-tables/README.md) | `af-admin/28-manage-firm-drop-downs.jpg`, `bbw-admin/27-manage-firm-drop-downs.jpg` | [004-company-administration.md](admin/004-company-administration.md), [006-manage-custom-lists.md](admin/006-manage-custom-lists.md) +12 |
| Manage Fiscal Calendar | `/en/admin/ManageFiscalPeriod.jsp` | [README.md](features/reference-data/README.md) | `af-admin/32-manage-fiscal-calendar.jpg`, `bbw-admin/31-manage-fiscal-calendar.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| Manage Folder Templates | `/en/admin/FolderTemplateEdit.jsp` | [README.md](modules/documents-folders/README.md) | `af-admin/48-manage-folder-templates.jpg`, `bbw-admin/44-manage-folder-templates.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| Manage Forms | `/en/admin/FirmCodeEdit.jsp` | [README.md](features/workflows-forms/README.md) | `af-admin/06-manage-forms.jpg`, `bbw-admin/05-manage-forms.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +15 |
| Manage Holiday Calendar | `/en/admin/ManageHolidayCalendar.jsp` | [README.md](features/reference-data/README.md) | `af-admin/33-manage-holiday-calendar.jpg`, `bbw-admin/32-manage-holiday-calendar.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| Manage Locations | `/en/admin/LocationEdit.jsp` | — | `af-admin/45-manage-locations.jpg`, `bbw-admin/41-manage-locations.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Members/Contacts | `/en/admin/ContactEdit.jsp` | [README.md](modules/people-parties/README.md) | `af-admin/34-manage-members-contacts.jpg`, `bbw-admin/33-manage-members-contacts.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| Manage Membership | `/en/admin/ManageOneMemberManyProjects.jsp` | — | `af-admin/38-manage-membership.jpg`, `bbw-admin/37-manage-membership.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| Manage Milestone Timeline | `/en/admin/ProcessTimelineEdit.jsp` | — | `af-admin/04-manage-milestone-timeline.jpg`, `bbw-admin/03-manage-milestone-timeline.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| Manage Organizations | `/en/admin/OrganizationEdit.jsp` | — | `af-admin/47-manage-organizations.jpg`, `bbw-admin/43-manage-organizations.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Page Layouts | `/en/pagebuilder/SummaryEntityPageLayoutEdit.jsp` | [README.md](features/page-layouts/README.md) | `af-admin/10-manage-page-layouts.jpg`, `bbw-admin/09-manage-page-layouts.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +18 |
| Manage Parts and Inventory | `/en/lease/PartEdit.jsp` | [README.md](modules/assets-equipment/README.md) | `af-admin/08-manage-parts-and-inventory.jpg`, `bbw-admin/07-manage-parts-and-inventory.jpg` | [004-company-administration.md](admin/004-company-administration.md), [006-manage-custom-lists.md](admin/006-manage-custom-lists.md) +1 |
| Manage Portfolios/Capital Programs | `/en/admin/ProgramEdit.jsp` | [README.md](modules/portfolio-transactions/README.md) | `af-admin/30-manage-portfolios-capital-programs.jpg`, `bbw-admin/29-manage-portfolios-capital-programs.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Regions/Org Chart | `/en/admin/OrgChartEdit.jsp` | [README.md](modules/platform-tenancy/README.md) | `af-admin/31-manage-regions-org-chart.jpg`, `bbw-admin/30-manage-regions-org-chart.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) |
| Manage Schedule Templates | `/en/admin/TaskTemplateEdit.jsp` | [scheduling.md](modules/projects-capital/scheduling.md) | `af-admin/03-manage-schedule-templates.jpg`, `bbw-admin/02-manage-schedule-templates.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| Manage Security | `/en/admin/SecurityPageAccess.jsp` | [README.md](features/security-access/README.md) | `af-admin/39-manage-security.jpg`, `bbw-admin/38-manage-security.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/README.md) +5 |
| Manage Top Menu | `/en/admin/ManageTopMenu.jsp` | [README.md](features/security-access/README.md) | `af-admin/17-manage-top-menu.jpg`, `bbw-admin/16-manage-top-menu.jpg` | [004-company-administration.md](admin/004-company-administration.md), [screen-routing.md](data-model/screen-routing.md) +4 |
| Manage Vendors | `/en/admin/VendorActivate.jsp` | — | `af-admin/37-manage-vendors.jpg`, `bbw-admin/36-manage-vendors.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| Manage Work Flows | `/en/workflow/WorkFlowTemplateEdit.jsp` | [README.md](features/workflows-forms/README.md) | `af-admin/09-manage-work-flows.jpg`, `bbw-admin/08-manage-work-flows.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +11 |
| Modify Straight Line Status | `/en/admin/lxadmin/SLDemoTweaks.jsp` | — | `af-admin/57-modify-straight-line-status.jpg`, `bbw-admin/50-modify-straight-line-status.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +2 |
| RESTful WebService Docs | `/en/test/RESTful.jsp` | [README.md](features/import-export/README.md) | — | [004-company-administration.md](admin/004-company-administration.md), [graphql-api.md](data-model/graphql-api.md) +6 |
| Report Log | `/en/admin/JobLogEdit.jsp` | [README.md](features/import-export/README.md) | `af-admin/55-report-log.jpg`, `bbw-admin/49-report-log.jpg` | [INDEX.md](INDEX.md), [004-company-administration.md](admin/004-company-administration.md) +8 |
| Test Email Address | `/en/admin/lxadmin/EmailTest.jsp` | — | `af-admin/59-test-email-address.jpg`, `bbw-admin/52-test-email-address.jpg` | [004-company-administration.md](admin/004-company-administration.md), [README.md](features/administration/README.md) +1 |
| View Data Model / Data Values (experimental) | `/en/test/walkHierarchy.jsp` | — | `af-admin/52-view-data-model-data-values-experimental.jpg`, `bbw-admin/46-view-data-model-data-values-experimental.jpg` | [004-company-administration.md](admin/004-company-administration.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +1 |
| View Object Model | `/en/admin/ShowObjectDetails.jsp` | [README.md](features/data-fields/README.md) | `af-admin/51-view-object-model.jpg`, `bbw-admin/45-view-object-model.jpg` | [004-company-administration.md](admin/004-company-administration.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +13 |

## 3. Page layouts (93)

**15 SEP** (summary/detail pages), **32 SUB** (sub-pages), **46 LIST** (list layouts). **80** are shared with AF by `(mode, name)` and **0** by id — one ASG template set, copied per tenant and re-keyed, then forked.

> SUB layouts carry no ParentPageLayoutID - sub-pages attach to a parent layout, not to navigation (0 of 32 have one).

> **Scope of this count.** These 93 are the **firm-authored** layouts — the rows Manage Page Layouts lists. They are not all the layouts in the tenant. A further **42 form layouts** are reachable only through Issue Types (135 in total), and beyond both lies the platform-seeded population that renders the administration screens themselves — the `Manage Discount Rates` grid is rendered by a layout in **neither** set. "All 93 layouts" always means all *firm* layouts. See [`features/page-layouts/`](features/page-layouts/).

Source: [`tenants/bbw-page-layouts.json`](tenants/bbw-page-layouts.json), [`tenants/layout-set-comparison.json`](tenants/layout-set-comparison.json).

| Mode | Layout | PageLayoutID | Primary table | Attached to | In AF? | Owner doc | Named in |
|---|---|---:|---|---|:--:|---|---|
| LIST | ASG ASC 842 Schedule | `98859` | `Straight-Line Schedule` | Contract : Accounting Info : ASC 842 Rent Schedule | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| LIST | ASG Approval - Expense Schedules | `99146` | `Expense Schedule` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Approval - Transactions | `99147` | `Payment Transaction` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Allowance | `98860` | `Allowance` | Contract : Payment Info : Allowances | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| LIST | ASG Contract Allowance Transaction | `102775` | `Allowance Transaction` | — | **BBW only** | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Alternate Rent | `98861` | `Alternate Rent Schedule` | Contract : Payment Info : Alternate Rent | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Amendments | `98862` | `Contract Amendment` | Contract : Abstract Info : Amendments | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Cotenants | `98863` | `Co Tenancy` | Contract : Abstract Info : Co-Tenancy | **BBW only** | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Covenants | `98864` | `Covenant` | Contract : Abstract Info : Covenants | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Expense Recovery | `99143` | `Expense Recovery` | Contract : Payment Info : Recoveries | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Expense Recovery (Net) | `99144` | `Expense Recovery` | Contract : Payment Info : Recoveries | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Expense Setup | `99051` | `Expense Setup` | Contract : Payment Info : Recurring Expenses | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Expense Setup - Expense Schedule | `99050` | `Expense Schedule` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Expense Setup - Vendor Allocation | `99049` | `Expense Vendor Allocation` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Key Dates | `98865` | `Key Date` | Contract : Abstract Info : Key Dates | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract List | `98918` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md), [README.md](features/page-layouts/README.md) +1 |
| LIST | ASG Contract Payment Details - Allowance | `98909` | `Allowance` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payment Details - Alternate Rent | `98910` | `Alternate Rent Schedule` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payment Details - Breakpoints | `98908` | `Percentage Rent Period` | — | yes | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Payment Details - Expense Recovery | `98911` | `Expense Recovery` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payment Details - Expense Setup | `98916` | `Expense Setup` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payment Details - Percent Rent | `98914` | `Percentage Rent` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payment Details - Rent Steps | `98917` | `Expense Schedule` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payment Details - Scheduled Offset | `98912` | `Scheduled Offset` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payment Details - Security Deposit | `98866` | `Security Deposit` | Contract : Payment Info : Security Deposit | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Payment Details - Security Deposit | `98915` | `Security Deposit` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Payment Details - Transactions | `98907` | `Payment Transaction` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Payments | `98867` | `Payment Transaction` | Contract : Payment Info : Transactions | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +5 |
| LIST | ASG Contract Percent Rent | `99145` | `Percentage Rent` | Contract : Payment Info : Percentage Rent | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Percent Rent - Breakpoints | `98913` | `Percentage Rent Breakpoint` | — | yes | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Contract Percent Rent - Schedule | `98920` | `Sales Period` | — | yes | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Contract Receipts | `98868` | `Payment Receipt` | Contract : Payment Info : Receipts | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Responsibilities | `98869` | `Responsibility` | Contract : Abstract Info : Responsibilities | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Sales History | `98870` | `Sales` | Contract : Payment Info : Sales | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Contract Terms | `98871` | `Contract Term` | Contract : Abstract Info : Terms | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| LIST | ASG Covenant List View | `98906` | `Covenant` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Employers | `98872` | `Employer` | Administration : Dashboard : Manage Employers | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| LIST | ASG Facility List | `98919` | `Facility` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| LIST | ASG Lease Abstract - Contract Term | `102506` | `Contract Term` | — | **BBW only** | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Lease Abstract - Covenants | `102250` | `Covenant` | — | **BBW only** | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | ASG Lease Abstract - Expense Schedule | `102251` | `Expense Schedule` | — | **BBW only** | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Lease Abstract - Expense Setup | `102252` | `Expense Setup` | — | **BBW only** | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Lease Abstract - Key Dates | `102266` | `Key Date` | — | **BBW only** | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG Lease Abstract - Percent Rent | `102109` | `Percentage Rent` | — | **BBW only** | [README.md](features/page-layouts/README.md) | — |
| LIST | ASG SL Summary | `98873` | `Straight-Line Schedule` | Contract : Accounting Info : Straight-Line Rent | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| LIST | zdelete | `102270` | `Comparison Report Item` | — | **BBW only** | [README.md](features/page-layouts/README.md) | *name too generic to measure* |
| SEP | ASG Breakpoint Schedule | `98921` | `Percentage Rent Period` | Contract : Payment Info : Percentage Rent | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| SEP | ASG Common Area Maintenance | `98924` | `Contract` | Contract : Abstract Info : Abstract Details | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| SEP | ASG Contract Abstract Details | `98925` | `Contract` | Contract : Abstract Info : Abstract Details | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [README.md](features/required-and-validation/README.md) |
| SEP | ASG Contract Payment Details | `98926` | `Contract` | Contract : Payment Info : Payment Details | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| SEP | ASG Contract Summary | `98927` | `Contract` | Contract : Details : Summary | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +8 |
| SEP | ASG Cotenancy Language | `98923` | `Contract` | Contract : Abstract Info : Co-Tenancy | **BBW only** | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| SEP | ASG Delivery Requirements | `98928` | `Contract` | Contract : Abstract Info : Abstract Details | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SEP | ASG Facility Summary | `98929` | `Facility` | Facility : Details : Summary | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +1 |
| SEP | ASG Funds and Expenses | `98930` | `Contract` | Contract : Abstract Info : Abstract Details | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SEP | ASG Last Deferred SL Entry | `98931` | `Contract` | Contract : Accounting Info : Straight-Line Rent | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SEP | ASG Lease Logs | `98932` | `Contract` | Contract : Details : Summary | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [014-contract-record-end-user.md](screens/014-contract-record-end-user.md) |
| SEP | ASG Location Summary | `98933` | `Location` | Location : Details : Summary | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| SEP | ASG Percent Rent Schedule | `98934` | `Percentage Rent Period` | Contract : Payment Info : Percentage Rent | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| SEP | ASG Portfolio Summary | `98935` | `Portfolio` | Portfolio : Details : Summary | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| SEP | ASG Real Estate Taxes | `99140` | `Contract` | Contract : Abstract Info : Abstract Details | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Accounting Schedule Details | `98858` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [014-contract-record-end-user.md](screens/014-contract-record-end-user.md) |
| SUB | ASG Co Tenancy | `98874` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| SUB | ASG Common Area Maintenance | `98875` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| SUB | ASG Contract Critical Dates | `98876` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| SUB | ASG Contract Facility Information | `98877` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Contract Firm Information | `98878` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) |
| SUB | ASG Contract Header | `98879` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +2 |
| SUB | ASG Contract Location Information | `98880` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Contract Log Header | `98881` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) |
| SUB | ASG Contract Space Information | `98882` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) |
| SUB | ASG Contract Wizard | `98883` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +2 |
| SUB | ASG Contract Wizard Step 2 | `98884` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| SUB | ASG Contract Wizard Step 3 | `98885` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| SUB | ASG Contract Wizard Step 4 | `98886` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| SUB | ASG Contract Wizard Step 5 | `98887` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| SUB | ASG Delivery Requirements | `98891` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Documents Form Field | `98936` | `Entity` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Facility Address | `98895` | `Facility` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) |
| SUB | ASG Facility Header | `98896` | `Facility` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) |
| SUB | ASG Facility Location Information | `98898` | `Facility` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) |
| SUB | ASG Facility Space Information | `98897` | `Facility` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) |
| SUB | ASG Facility Wizard | `99141` | `Facility` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| SUB | ASG Funds and Expenses | `98894` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Hours of Operation | `100867` | `Covenant` | — | **BBW only** | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| SUB | ASG Lease Abstract - Funds and Expenses | `102629` | `Contract` | — | **BBW only** | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Location Address | `98903` | `Location` | — | yes | [README.md](features/page-layouts/README.md) | — |
| SUB | ASG Location Area Information | `98904` | `Location` | — | yes | [README.md](features/page-layouts/README.md) | — |
| SUB | ASG Location Financial Information | `98905` | `Location` | — | yes | [README.md](features/page-layouts/README.md) | — |
| SUB | ASG Location Header | `98902` | `Location` | — | yes | [README.md](features/page-layouts/README.md) | — |
| SUB | ASG Location Wizard | `99142` | `Location` | — | yes | [README.md](features/page-layouts/README.md) | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md), [README.md](features/page-layouts/README.md) +1 |
| SUB | ASG Real Estate Taxes | `98890` | `Contract` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |
| SUB | ASG Workflow Footer | `98937` | `Entity` | — | yes | [README.md](features/page-layouts/README.md) | [README.md](features/page-layouts/README.md) |

## 4. Workflow templates (13) and form types (6)

**13 templates, 62 steps.** Every configured step is `type=Form`; approval levels observed are `Ad Hoc`, `Member`. **Not one step is a `Task` step**, so half the step model is unobserved.

Source: [`tenants/bbw-workflow-steps.json`](tenants/bbw-workflow-steps.json).

| Workflow template | WorkFlowTemplateID | Steps | Owner doc | Named in |
|---|---:|---:|---|---|
| ASC 842 Tracking | `2475` | 2 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Cotenancy Update | `2478` | 2 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Implementation Workflow - Document Abstraction | `2401` | 2 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Implementation Workflow - Financial Abstraction | `2402` | 6 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Lease Admin Request | `2472` | 8 | [README.md](features/workflows-forms/README.md) | [INDEX.md](INDEX.md), [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +20 |
| Lease Admin Request v1 | `2399` | 8 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Lease Admin Request v2 | `2468` | 10 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Lease Date Review | `2473` | 2 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Lucernex Change Request | `2469` | 6 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Lucernex Change Request v1 | `2463` | 5 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| User Request | `2400` | 2 | [README.md](features/workflows-forms/README.md) | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md), [README.md](features/workflows-forms/README.md) +9 |
| Vendor Change (Notice) | `2461` | 4 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Vendor Changes (Integration) | `2418` | 5 | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |

Form types — `TableType=2035` (`Issue Type Code`). A **Form is an Issue Type**; a Custom List is a Form without the workflow.

| Form type | Owner doc | Named in |
|---|---|---|
| ASC 842 Tracking | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| Change Request | [README.md](features/workflows-forms/README.md) | [README.md](features/administration/README.md), [README.md](features/custom-lists/README.md) +3 |
| Lease Admin Request | [README.md](features/workflows-forms/README.md) | [INDEX.md](INDEX.md), [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +20 |
| QC Request | [README.md](features/workflows-forms/README.md) | [README.md](features/custom-lists/README.md), [README.md](features/workflows-forms/README.md) +2 |
| User Request | [README.md](features/workflows-forms/README.md) | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md), [README.md](features/workflows-forms/README.md) +9 |
| Vendor Changes (Integration) | [README.md](features/workflows-forms/README.md) | [README.md](features/workflows-forms/README.md), [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |

## 5. Firm drop-downs (207)

All **207** code tables, `TableType` 2000–3016. Identical set in both tenants (207/207 matching `TableType`s). Values, row actions and the `isReadOnlyRecord` delete gate are in [`tenants/af-code-table-actions.json`](tenants/af-code-table-actions.json) and [`data-model/code-table-registry.md`](data-model/code-table-registry.md).

| TableType | Drop-down | Named in |
|---:|---|---|
| `2000` | Appointment Type Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +1 |
| `2001` | Asset Department Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2002` | Asset Group Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2003` | Asset Operation Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2004` | Asset Product Type Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2005` | Asset Suspension Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +5 |
| `2006` | Budget Change Reason Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2007` | Budget Column Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +1 |
| `2008` | Budget Value Units Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2009` | Building Area Unit Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +4 |
| `2010` | Building Class Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2011` | CAM Category Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +1 |
| `2012` | Change Department Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2013` | Change Package Type Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +1 |
| `2014` | Issue/RFI/Proposed Change Cause | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +1 |
| `2015` | Change Source Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2016` | Change Type Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2017` | Classification Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2018` | Competitor Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2019` | Complex Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2020` | Complex Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2021` | Construction Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2022` | Contact Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2023` | Coverage Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2024` | Deal Type Code | [code-table-registry.md](data-model/code-table-registry.md) +5 |
| `2025` | Decision Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +3 |
| `2026` | Demographic Results Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2027` | Discipline Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2028` | Distribution Center Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2029` | Document Content Code | [004-company-administration.md](admin/004-company-administration.md) +1 |
| `2030` | Document Type Code | [004-company-administration.md](admin/004-company-administration.md) +3 |
| `2031` | Funding Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2032` | Inspection Period Start Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2033` | Inspection Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2034` | Insurance Policy Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2035` | Issue Type Code | [code-table-registry.md](data-model/code-table-registry.md) +14 |
| `2036` | Invoice Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2037` | Job Function Code | [004-company-administration.md](admin/004-company-administration.md) +2 |
| `2038` | Job Title Code | [004-company-administration.md](admin/004-company-administration.md) +6 |
| `2039` | Land Area Unit Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2040` | Lease Co Tenant Type Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2041` | Lease Option Other Type Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2042` | Lease Option Type Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2043` | Lease Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +4 |
| `2044` | Lease Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2045` | Location Access Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2046` | Location Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2047` | Asset Category Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2048` | Maintenance Remedy Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2049` | Market Area Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2050` | Market Demographics Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2051` | Market Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2052` | Master Employer Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2053` | Misc Expense Category Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2054` | Pro Forma Budget Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +2 |
| `2055` | Project Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2056` | Property Primary Use Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2057` | RE Transaction Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +4 |
| `2058` | Responsible Party Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2059` | Scenario Deal Type Code | [code-table-registry.md](data-model/code-table-registry.md) +4 |
| `2060` | Scenario Type Code | [code-table-registry.md](data-model/code-table-registry.md) +4 |
| `2061` | Security Privilege Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2062` | Service Type Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2063` | Site Rating Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2064` | Slot Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2065` | SRQ Source Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2066` | SRQ Status Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2067` | SRQ Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2068` | Store Phase Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2069` | Tax Category Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2070` | User Class Code | [004-company-administration.md](admin/004-company-administration.md) +3 |
| `2071` | Utility Category Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2072` | Vendor Grade Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2073` | Vertical Industry Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2074` | Zoning Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2075` | Address Group Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2076` | Address Type Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2077` | Agreement Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2078` | Allowance Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2079` | Allowance Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2080` | Amendment Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2081` | Approval Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +3 |
| `2082` | Last Action Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +8 |
| `2083` | Area Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2084` | Asset Class Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2085` | Asset Type Test Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2086` | Base Year Amount Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2087` | Co Tenancy Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2088` | Co Tenancy Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2089` | Company Group Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2091` | Concept Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2092` | Contract Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2093` | Contract Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2094` | Contract Status Code | [INDEX.md](INDEX.md) +11 |
| `2095` | Contract Use Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2096` | Covenant Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2097` | Covenant Template Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2098` | Denominator Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2099` | Escalation Payment Method Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2100` | Evaluation Rating Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2101` | Exchange Rate Type Code | [code-table-registry.md](data-model/code-table-registry.md) +4 |
| `2102` | Expense Acct Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2103` | Expense Category Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2104` | Expense Group Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2105` | Facility Category Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2106` | Facility Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2107` | Facility Status Code | [INDEX.md](INDEX.md) +3 |
| `2108` | Facility Use Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2109` | Financial Adjustment Status Code | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +4 |
| `2110` | Guarantee Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2111` | Holding Interest Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2112` | Insurance Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2113` | Insurance Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2114` | Key Date Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2115` | Legal Classification Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2116` | Location Category Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2117` | Location Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2118` | Location Status Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2119` | Location Use Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2120` | Org Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2121` | Org Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2122` | Org Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2123` | Parcel Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2124` | Parcel Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2125` | Parcel Status Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2126` | Parcel Use Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2127` | Parking Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2128` | Parking Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2129` | Party Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2130` | Party Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2131` | Pass Through Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2132` | Payment Method Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2133` | Unit Sales Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2134` | Usage Unit Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2135` | Usage Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2136` | Use Rent Model Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2137` | CPI Index Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2138` | Plan Forecast Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2139` | Pro Rata Share Method Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2140` | Rating Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2141` | Region Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2142` | Responsibility Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2143` | Sales Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2144` | Sales Group Code | [code-table-registry.md](data-model/code-table-registry.md) |
| `2145` | Security Deposit Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2146` | Security Deposit Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2147` | Space Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2148` | Space Status Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2149` | Space Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2150` | Space Use Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2151` | Tenant Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2152` | Tenant Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2153` | Tenant Status Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2154` | Tenant Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2155` | Tenant Use Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2156` | Covenant Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2157` | Covenant Status Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2158` | Key Date Action Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2159` | Term Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2160` | Schedule Creation Reason Code | [code-table-registry.md](data-model/code-table-registry.md) +8 |
| `2161` | Straight Line Schedule Type Code | [code-table-registry.md](data-model/code-table-registry.md) +7 |
| `2162` | ASC 842 Schedule Type Code | [code-table-registry.md](data-model/code-table-registry.md) +7 |
| `2163` | IFRS 16 Schedule Type Code | [code-table-registry.md](data-model/code-table-registry.md) +7 |
| `2164` | Cap Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2165` | Escalation Category Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2166` | Escalation Group Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2167` | Escalation Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2168` | Exp Rec Based On Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2169` | Index Group Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2170` | Index Source Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2171` | Index Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2172` | Source Entity Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2173` | Insurance Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2174` | Store Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2175` | Offset Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2176` | Offset Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2177` | Parcel Access Category Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2178` | Parcel Access Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2179` | Recovery Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2180` | Recovery Item Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2181` | Security Deposit Status Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2182` | Adjustment Method Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2183` | Exclusion Cap Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `2184` | Property Tax Status Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2185` | Property Tax Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `2186` | Tax Appeal Result Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2187` | Tax Appeal Status Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2188` | Tax Paid To Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2189` | Tax Refund Type Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `2190` | Tax Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `3000` | Asset Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3001` | Problem Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3002` | Amendment Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `3003` | Contract Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3004` | Covenant Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `3005` | Facility Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `3006` | Key Date Type Code | [code-table-registry.md](data-model/code-table-registry.md) +3 |
| `3007` | Location Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `3008` | Parcel Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3009` | Usage Group Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3010` | Usage Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3011` | Responsibility Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3012` | Sales Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3013` | Expense Type Code | [CONVENTIONS.md](CONVENTIONS.md) +5 |
| `3014` | Parcel Access Type Code | [code-table-registry.md](data-model/code-table-registry.md) +1 |
| `3015` | Recovery Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |
| `3016` | Recovery Item Type Code | [code-table-registry.md](data-model/code-table-registry.md) +2 |

## 6. Sql tables (227)

The `ShowObjectDetails.jsp` picker exposes **227** tables. **202** yielded field detail; **25** are refused ("Data for that table not supported") — including the entire `Page Layout` trio, which is why the layout engine has to be read from its UI rather than its schema. **Required?** counts below are the table's own NOT-NULL-equivalent flag, distinct from layout-level required.

Source: [`tenants/bbw-platform-tables.json`](tenants/bbw-platform-tables.json), [`tenants/bbw-platform-inventory.json`](tenants/bbw-platform-inventory.json), [`data-model/object-catalog.md`](data-model/object-catalog.md).

| sqlTableID | Table | Physical | Fields | Required | In 223-object census? | Named in |
|---:|---|---|---:|---:|:--:|---|
| `2884` | Accrual Transaction | `AccrualTransaction` | 55 | 1 | yes | [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +4 |
| `3057` | Accting Assumption Adjust | `AcctingAssumptionAdjust` | 19 | 5 | yes | [accting-assumption-adjust.md](data-fields/accting-assumption-adjust.md) +1 |
| `2686` | Allowance | `Allowance` | 23 | 1 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +24 |
| `2687` | Allowance Transaction | `AllowanceTransaction` | 15 | 3 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) +2 |
| `2946` | Alternate Rent Schedule | `AlternateRentSchedule` | 26 | 2 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +6 |
| `2885` | App Activity Log | `AppActivityLog` | **refused** | — | **no** | — |
| `2561` | Asset | `Asset` | 122 | 2 | yes | *name too generic to measure* |
| `2957` | Asset History | `AssetHistory` | 13 | 3 | yes | [audit-history-tables.md](data-fields/audit-history-tables.md) +1 |
| `2870` | Audit Column | `AuditColumn` | 14 | 1 | yes | — |
| `2871` | Audit Master | `AuditMaster` | **refused** | — | **no** | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| `2872` | Audit Table | `AuditTable` | 1 | 0 | yes | — |
| `2958` | Bid Package | `BidPackage` | 48 | 4 | yes | [004-company-administration.md](admin/004-company-administration.md) +11 |
| `3163` | Bid Package Alternate | `BidPackageAlternate` | 5 | 2 | yes | [bid-package-ancillary-tables.md](data-fields/bid-package-ancillary-tables.md) |
| `3164` | Bid Package Alternate Value | `BidPackageAlternateValue` | 4 | 3 | yes | [bid-package-ancillary-tables.md](data-fields/bid-package-ancillary-tables.md) |
| `3173` | Bid Package Breakout Value | `BidPackageBreakoutValue` | 6 | 3 | yes | [bid-package-ancillary-tables.md](data-fields/bid-package-ancillary-tables.md) |
| `3120` | Bid Package Template | `BidPackageTemplate` | 32 | 3 | yes | [004-company-administration.md](admin/004-company-administration.md) +6 |
| `2959` | Bidder Issue | `BidderIssue` | 21 | 6 | yes | [bidder-issue.md](data-fields/bidder-issue.md) +1 |
| `2654` | Budget Column | `BudgetColumn` | 21 | 7 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +16 |
| `2655` | Budget Column Item Value | `BudgetColumnItemValue` | 19 | 3 | yes | [budget-column-item-value.md](data-fields/budget-column-item-value.md) |
| `2656` | Budget Column Type | `BudgetColumnType` | 31 | 20 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +9 |
| `2666` | Budget Index | `BudgetIndex` | 6 | 2 | yes | [004-company-administration.md](admin/004-company-administration.md) +4 |
| `2667` | Budget Index Value | `BudgetIndexValue` | 8 | 4 | yes | [budget-ancillary-tables.md](data-fields/budget-ancillary-tables.md) |
| `2657` | Budget Line Item | `BudgetLineItem` | 26 | 5 | yes | [bid-package-ancillary-tables.md](data-fields/bid-package-ancillary-tables.md) +3 |
| `2668` | Budget Option | `BudgetOption` | 13 | 5 | yes | [budget-ancillary-tables.md](data-fields/budget-ancillary-tables.md) +1 |
| `3002` | Budget Option Template | `VirtualTemplateBudgetOption` | 17 | 0 | yes | [budget-ancillary-tables.md](data-fields/budget-ancillary-tables.md) |
| `3001` | Budget Template | `VirtualTemplateBudget` | 17 | 0 | yes | [004-company-administration.md](admin/004-company-administration.md) +11 |
| `2886` | Budget View | `BudgetView` | 10 | 2 | yes | [004-company-administration.md](admin/004-company-administration.md) +8 |
| `2635` | CLR Extension Part | `CLRExtensionPart` | 24 | 4 | yes | — |
| `3082` | CPI | `CPI` | 10 | 3 | yes | *name too generic to measure* |
| `2460` | Change Manage | `ChangeManage` | 1 | 0 | yes | [006-manage-custom-lists.md](admin/006-manage-custom-lists.md) +3 |
| `3102` | Change Order | `ChangeOrder` | 16 | 2 | yes | [006-manage-custom-lists.md](admin/006-manage-custom-lists.md) +7 |
| `2634` | Client List Row | `ClientListRow` | 24 | 4 | yes | — |
| `2688` | Co Tenancy | `CoTenancy` | 28 | 1 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +11 |
| `2516` | Committee Package | `CommitteePackage` | 1 | 0 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) +4 |
| `2517` | Committee Package Template | `CommitteePackageTemplate` | **refused** | — | **no** | — |
| `2683` | Comparison Item | `ComparisonItem` | 9 | 2 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2684` | Comparison Report | `ComparisonReport` | 4 | 2 | yes | [009-related-fields-and-data-model.md](admin/009-related-fields-and-data-model.md) +5 |
| `2518` | Competitor | `Competitor` | 26 | 2 | yes | [INDEX.md](data-fields/INDEX.md) +12 |
| `2791` | Complex | `Complex` | 45 | 2 | yes | *name too generic to measure* |
| `2792` | Contract | `Contract` | 477 | 7 | yes | *name too generic to measure* |
| `2793` | Contract Amendment | `ContractAmendment` | 20 | 1 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +9 |
| `3054` | Contract Financial Test | `ContractFinancialTest` | 93 | 1 | yes | [contract-financial-test.md](data-fields/contract-financial-test.md) +2 |
| `2794` | Contract Term | `ContractTerm` | 26 | 1 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +20 |
| `3176` | Cost Tracking Template | `CostTrackingTemplate` | 28 | 1 | yes | [cost-tracking-template.md](data-fields/cost-tracking-template.md) |
| `2795` | Covenant | `Covenant` | 56 | 1 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +53 |
| `2604` | Custom Code Field | `CustomCodeField` | 13 | 3 | yes | [code-reference-tables.md](data-fields/code-reference-tables.md) |
| `2605` | Custom Code Table | `CustomCodeTable` | **refused** | — | **no** | [code-reference-tables.md](data-fields/code-reference-tables.md) +1 |
| `2829` | DMA | `DMA` | 7 | 4 | yes | *name too generic to measure* |
| `2519` | Dashboard | `Dashboard` | **refused** | — | **no** | [INDEX.md](INDEX.md) +50 |
| `2522` | Demographic Fact | `DemographicFact` | 10 | 2 | yes | [demographics-market-tables.md](data-fields/demographics-market-tables.md) |
| `2523` | Demographic Report | `DemographicReport` | 10 | 2 | yes | [demographics-market-tables.md](data-fields/demographics-market-tables.md) +1 |
| `2664` | Demographic Results | `DemographicResults` | 12 | 3 | yes | [demographics-market-tables.md](data-fields/demographics-market-tables.md) +2 |
| `2524` | Demographic Study Area | `DemographicStudyArea` | 6 | 2 | yes | [demographics-market-tables.md](data-fields/demographics-market-tables.md) |
| `2525` | Development Plan | `DevelopmentPlan` | 7 | 3 | yes | [development-slot.md](data-fields/development-slot.md) +1 |
| `2526` | Development Target | `DevelopmentSlot` | 31 | 7 | yes | [object-catalog.md](data-model/object-catalog.md) +2 |
| `3113` | Discount Rate | `DiscountRate` | 16 | 4 | yes | [004-company-administration.md](admin/004-company-administration.md) +19 |
| `2527` | Document | `Document` | 23 | 7 | yes | [CONVENTIONS.md](CONVENTIONS.md) +88 |
| `3071` | Document Markup | `DocumentMarkup` | 1 | 0 | yes | — |
| `3055` | E Mail Received Log | `EMailReceivedLog` | 15 | 3 | yes | — |
| `3045` | E Mail Sent Log | `EMailSentLog` | 1 | 0 | yes | — |
| `2529` | Employer | `Employer` | 71 | 5 | yes | [CONVENTIONS.md](CONVENTIONS.md) +61 |
| `3183` | Employer Site | `EmployerSite` | 20 | 3 | yes | [employer-site.md](data-fields/employer-site.md) |
| `2994` | Entity Template | `EntityTemplate` | 1 | 0 | yes | [INDEX.md](data-fields/INDEX.md) +2 |
| `2796` | Escalation Index | `EscalationIndex` | 12 | 2 | yes | [expense-escalation.md](data-fields/expense-escalation.md) +4 |
| `2821` | Excel Server Status | `ExcelServerStatus` | **refused** | — | **no** | — |
| `2822` | Excel Service Log | `ExcelServiceLog` | **refused** | — | **no** | — |
| `2823` | Excel Service Queue | `ExcelServiceQueue` | **refused** | — | **no** | — |
| `2950` | Exchange Rate | `ExchangeRate` | 8 | 6 | yes | [004-company-administration.md](admin/004-company-administration.md) +10 |
| `2905` | Exp Accrual Forecast Period | `VirtualExpAccrualForecastPeriod` | 13 | 0 | yes | [README.md](features/data-fields/README.md) |
| `2900` | Expense Accrual Schedule | `ExpenseAccrualSchedule` | 31 | 3 | yes | [expense-accrual-schedule.md](data-fields/expense-accrual-schedule.md) +2 |
| `2901` | Expense Accrual Setup | `ExpenseAccrualSetup` | 31 | 2 | yes | [accrual-transaction.md](data-fields/accrual-transaction.md) +4 |
| `2797` | Expense Allocation | `ExpenseAllocation` | 15 | 1 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) +1 |
| `2798` | Expense Escalation | `ExpenseEscalation` | 28 | 3 | yes | [expense-escalation.md](data-fields/expense-escalation.md) +1 |
| `2861` | Expense Forecast Period | `VirtualExpenseForecastPeriod` | 20 | 0 | yes | [README.md](features/data-fields/README.md) |
| `2799` | Expense Recovery | `ExpenseRecovery` | 568 | 1 | yes | [INDEX.md](INDEX.md) +7 |
| `2858` | Expense Recovery Item | `ExpenseRecoveryItem` | 47 | 4 | yes | [expense-recovery-item.md](data-fields/expense-recovery-item.md) +2 |
| `3179` | Expense Recovery Item Mapping | `ExpenseRecoveryItemMapping` | 6 | 3 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2825` | Expense Schedule | `ExpenseSchedule` | 51 | 5 | yes | [expense-schedule.md](data-fields/expense-schedule.md) +8 |
| `2800` | Expense Setup | `ExpenseSetup` | 98 | 2 | yes | [accting-assumption-adjust.md](data-fields/accting-assumption-adjust.md) +23 |
| `2873` | Expense Vendor Allocation | `ExpenseVendorAllocation` | 16 | 3 | yes | [expense-vendor-allocation.md](data-fields/expense-vendor-allocation.md) +2 |
| `2530` | Facility | `Facility` | 139 | 14 | yes | *name too generic to measure* |
| `2911` | Facility Expense | `FacilityExpense` | 22 | 2 | yes | [facility-expense.md](data-fields/facility-expense.md) +2 |
| `2531` | Favorite Link | `FavoriteLink` | **refused** | — | **no** | — |
| `3065` | Financial Adjustment | `FinancialAdjustment` | 19 | 3 | yes | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +7 |
| `2532` | Firm | `Firm` | 18 | 1 | yes | *name too generic to measure* |
| `2827` | Fiscal Period | `FiscalPeriod` | 17 | 6 | yes | [fiscal-period.md](data-fields/fiscal-period.md) +8 |
| `2445` | Folder | `Folder` | 16 | 2 | yes | *name too generic to measure* |
| `3003` | Folder Template | `VirtualTemplateFolder` | 16 | 0 | yes | [004-company-administration.md](admin/004-company-administration.md) +10 |
| `2452` | General Entity Info | `ProjectEntity` | 107 | 5 | yes | [object-catalog.md](data-model/object-catalog.md) +2 |
| `2874` | Global Property | `GlobalProperty` | 4 | 1 | yes | [foreign-key-graph.md](data-model/foreign-key-graph.md) +1 |
| `2878` | Global Property Section | `GlobalPropertySection` | **refused** | — | **no** | [foreign-key-graph.md](data-model/foreign-key-graph.md) +1 |
| `3051` | Grid Preference | `GridPreference` | **refused** | — | **no** | [bbw-vs-american-freight.md](tenants/bbw-vs-american-freight.md) |
| `2995` | Holiday Date | `HolidayDate` | 12 | 5 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2996` | Holiday Schedule | `HolidaySchedule` | 8 | 2 | yes | [program.md](data-fields/program.md) +1 |
| `3068` | Information Overlay | `InformationOverlay` | **refused** | — | **no** | — |
| `2801` | Insurance | `Insurance` | 27 | 1 | yes | *name too generic to measure* |
| `2951` | Invoice Issue | `InvoiceIssue` | 23 | 3 | yes | [invoice-issue.md](data-fields/invoice-issue.md) +2 |
| `2952` | Invoice Item | `InvoiceItem` | 18 | 2 | yes | [invoice-item.md](data-fields/invoice-item.md) +4 |
| `2446` | Issue | `Issue` | 56 | 6 | yes | *name too generic to measure* |
| `2535` | Issue Response | `IssueResponse` | 11 | 4 | yes | [workflow-notification-ancillary-tables.md](data-fields/workflow-notification-ancillary-tables.md) |
| `2536` | Issue Submittal | `IssueSubmittal` | 1 | 0 | yes | — |
| `2802` | Job Log | `JobLog` | **refused** | — | **no** | *name too generic to measure* |
| `2538` | Jurisdiction | `Jurisdiction` | 11 | 3 | yes | [INDEX.md](data-fields/INDEX.md) +25 |
| `2803` | Key Date | `KeyDate` | 39 | 1 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +17 |
| `2539` | Land Purchase Summary | `LandPurchaseSummary` | 35 | 1 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) +1 |
| `3189` | Landlord Invoice | `LandlordInvoice` | 31 | 0 | yes | [landlord-invoice-item.md](data-fields/landlord-invoice-item.md) +3 |
| `3190` | Landlord Invoice Item | `LandlordInvoiceItem` | 28 | 3 | yes | [landlord-invoice-item.md](data-fields/landlord-invoice-item.md) +2 |
| `2540` | Lease Audit | `LeaseAudit` | 1 | 0 | yes | [audit-history-tables.md](data-fields/audit-history-tables.md) |
| `2542` | Lease Info | `LeaseInfo` | 219 | 2 | yes | [lease-info.md](data-fields/lease-info.md) |
| `2672` | Link Budget Index BLI | `LinkBudgetIndexBLI` | 1 | 0 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `2902` | Link Budget View BLI | `LinkBudgetViewBLI` | 1 | 0 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `2549` | Link Comm Pkg Templ Doc Content | `LinkCommPkgTemplDocContent` | **refused** | — | **no** | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `3056` | Link E Mail Received Log Document | `LinkEMailReceivedLogDocument` | 5 | 2 | yes | — |
| `2608` | Link Issue Part | `LinkIssuePart` | 13 | 4 | yes | — |
| `2627` | Link Issue Part Order | `LinkIssuePartOrder` | 16 | 6 | yes | — |
| `2554` | Link Land Purchase Inspection | `LinkLandPurchaseInspection` | 8 | 4 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `3191` | Link Landlord Inv Payment Txn | `LinkLandlordInvPaymentTxn` | 13 | 5 | yes | — |
| `2615` | Link Member Project Entity | `LinkMemberProjectEntity` | 7 | 2 | yes | [link-member-project-entity.md](data-fields/link-member-project-entity.md) +1 |
| `3070` | Link PE Member Code Job Title | `LinkPEMemberCodeJobTitle` | 1 | 0 | yes | — |
| `2826` | Link Project Entity Contact | `LinkProjectEntityContact` | 12 | 3 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `2998` | Link Project Entity Vendor | `LinkProjectEntityVendor` | 4 | 2 | yes | — |
| `3169` | Link Re Trans Scen Contact | `LinkReTransScenContact` | 33 | 1 | yes | — |
| `2969` | Link Receipt Transaction | `LinkReceiptTransaction` | 12 | 3 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `2593` | Link Region Manager | `LinkRegionManager` | 1 | 0 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `2594` | Link Region Market | `LinkRegionMarket` | **refused** | — | **no** | [link-relationship-tables.md](data-fields/link-relationship-tables.md) |
| `2970` | Link Sched Offset Exp Grp Type | `LinkSchedOffsetExpGrpType` | 12 | 3 | yes | — |
| `2633` | Link Task By Code Member | `LinkTaskByCodeMember` | 8 | 2 | yes | — |
| `2999` | Link Task Document | `LinkTaskDocument` | 1 | 0 | yes | — |
| `2560` | Link Task Member | `LinkTaskMember` | 5 | 3 | yes | — |
| `2804` | Location | `Location` | 143 | 8 | yes | *name too generic to measure* |
| `2562` | Map Client Budget | `MapClientBudget` | **refused** | — | **no** | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2563` | Map Client Schedule | `MapClientSchedule` | 10 | 3 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2564` | Member | `Member` | 81 | 19 | yes | *name too generic to measure* |
| `2565` | Member Audit | `MemberAudit` | 12 | 3 | yes | [audit-history-tables.md](data-fields/audit-history-tables.md) |
| `3004` | Member Template | `VirtualTemplateMember` | 1 | 0 | yes | [object-catalog.md](data-model/object-catalog.md) +1 |
| `2566` | Non Member | `NonMember` | 37 | 8 | yes | — |
| `2642` | Notify | `Notify` | 1 | 0 | yes | *name too generic to measure* |
| `2644` | Notify Template | `NotifyTemplate` | **refused** | — | **no** | [workflow-notification-ancillary-tables.md](data-fields/workflow-notification-ancillary-tables.md) +1 |
| `2645` | Notify Template Member | `NotifyTemplateMember` | **refused** | — | **no** | [workflow-notification-ancillary-tables.md](data-fields/workflow-notification-ancillary-tables.md) |
| `2805` | Organization | `Organization` | 17 | 2 | yes | [004-company-administration.md](admin/004-company-administration.md) +33 |
| `2567` | Ownership | `Ownership` | 9 | 5 | yes | [INDEX.md](data-fields/INDEX.md) +12 |
| `2611` | Page Layout | `PageLayout` | **refused** | — | **no** | [INDEX.md](INDEX.md) +43 |
| `2612` | Page Layout Field | `PageLayoutField` | **refused** | — | **no** | [page-layout-field.md](data-fields/page-layout-field.md) +1 |
| `2613` | Page Layout Filter | `PageLayoutFilter` | **refused** | — | **no** | [page-layout-filter.md](data-fields/page-layout-filter.md) +1 |
| `2806` | Parcel | `Parcel` | 154 | 10 | yes | *name too generic to measure* |
| `2847` | Parcel Access | `ParcelAccess` | 20 | 2 | yes | [parcel-access.md](data-fields/parcel-access.md) +3 |
| `2807` | Parking | `Parking` | 19 | 2 | yes | *name too generic to measure* |
| `2614` | Part | `Part` | 16 | 2 | yes | *name too generic to measure* |
| `2638` | Part Package | `PartPackage` | 6 | 2 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2639` | Part Package Item | `PartPackageItem` | 7 | 4 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2808` | Party | `Party` | 12 | 1 | yes | *name too generic to measure* |
| `3105` | Pay App | `PayApp` | 15 | 2 | yes | *name too generic to measure* |
| `2809` | Payment Receipt | `PaymentReceipt` | 21 | 1 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +5 |
| `2810` | Payment Transaction | `PaymentTransaction` | 139 | 1 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +10 |
| `2811` | Percentage Rent | `PercentageRent` | 47 | 1 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +19 |
| `2906` | Percentage Rent Accrual Period | `VirtualPRAccrualPeriod` | 20 | 0 | yes | [virtual-pr-accrual-period.md](data-fields/virtual-pr-accrual-period.md) +1 |
| `2955` | Percentage Rent Breakpoint | `PercentageRentBreakpoint` | 40 | 1 | yes | [percentage-rent-breakpoint.md](data-fields/percentage-rent-breakpoint.md) +2 |
| `2848` | Percentage Rent Period | `VirtualPercentageRentPeriod` | 38 | 0 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +3 |
| `2956` | Percentage Rent Summary Period | `VirtualPRPAggregate` | 16 | 0 | yes | [README.md](features/data-fields/README.md) |
| `2569` | Person | `Person` | 37 | 8 | yes | *name too generic to measure* |
| `3177` | Pgp Config | `PgpConfig` | **refused** | — | **no** | — |
| `2571` | Potential Project | `PotentialProject` | 108 | 9 | yes | [bid-package-template.md](data-fields/bid-package-template.md) +6 |
| `2682` | Pro Forma Budget | `ProFormaBudget` | 47 | 1 | yes | [007-firm-and-client-drop-downs.md](admin/007-firm-and-client-drop-downs.md) +3 |
| `2573` | Process Timeline | `ProcessTimeline` | 31 | 0 | yes | [process-timeline.md](data-fields/process-timeline.md) +1 |
| `2574` | Process Timeline Template | `ProcessTimelineTemplate` | 10 | 5 | yes | — |
| `2575` | Program | `Program` | 181 | 8 | yes | *name too generic to measure* |
| `2576` | Program Revenue Weeks | `ProgramRevenueWeeks` | 13 | 3 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2577` | Project | `Project` | 111 | 11 | yes | *name too generic to measure* |
| `2971` | Property Tax Appeal | `PropertyTaxAppeal` | 41 | 3 | yes | [property-tax-appeal-award.md](data-fields/property-tax-appeal-award.md) +2 |
| `2972` | Property Tax Appeal Award | `PropertyTaxAppealAward` | 18 | 3 | yes | [property-tax-appeal-award.md](data-fields/property-tax-appeal-award.md) |
| `2973` | Property Tax Assessment | `PropertyTaxAssessment` | 25 | 3 | yes | [property-tax-appeal.md](data-fields/property-tax-appeal.md) +3 |
| `2974` | Property Tax Bill | `PropertyTaxBill` | 32 | 3 | yes | [payment-transaction.md](data-fields/payment-transaction.md) +4 |
| `2975` | Property Tax Detail | `PropertyTaxDetail` | 15 | 3 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) |
| `2976` | Property Tax Summary | `PropertyTaxSummary` | 32 | 2 | yes | [property-tax-assessment.md](data-fields/property-tax-assessment.md) +2 |
| `2579` | Prototype | `Prototype` | 113 | 15 | yes | [INDEX.md](INDEX.md) +54 |
| `3197` | Punch List | `PunchList` | 10 | 2 | yes | [object-catalog.md](data-model/object-catalog.md) +2 |
| `3198` | Punch List Assignee | `PunchListAssignee` | 5 | 1 | yes | [object-catalog.md](data-model/object-catalog.md) +1 |
| `3199` | Punch List Task | `PunchListTask` | 13 | 3 | yes | [object-catalog.md](data-model/object-catalog.md) +1 |
| `3200` | Punch List Task Assignee | `PunchListTaskAssignee` | 5 | 1 | yes | [object-catalog.md](data-model/object-catalog.md) +1 |
| `3107` | Purchase Order | `PurchaseOrder` | 20 | 2 | yes | [006-manage-custom-lists.md](admin/006-manage-custom-lists.md) +9 |
| `3122` | Question | `Question` | 14 | 4 | yes | [INDEX.md](INDEX.md) +23 |
| `3143` | RE Transaction | `RETransaction` | 31 | 3 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +13 |
| `3170` | Re Trans Scen Contact | `ReTransScenContact` | 28 | 3 | yes | — |
| `3171` | Recalc Override Notes | `RecalcOverrideNotes` | 7 | 2 | yes | [sl-summary.md](data-fields/sl-summary.md) +3 |
| `2580` | Region | `Region` | 1 | 0 | yes | *name too generic to measure* |
| `2595` | Report Group Available Field | `ReportGroupAvailableField` | 27 | 4 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +5 |
| `2596` | Report Group Data | `ReportGroupData` | 5 | 1 | yes | [user-class-security.md](data-fields/user-class-security.md) |
| `2813` | Responsibility | `Responsibility` | 32 | 1 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +21 |
| `2859` | SL Period | `SLPeriod` | 79 | 4 | yes | — |
| `2860` | SL Summary | `SLSummary` | 136 | 2 | yes | [README.md](features/page-layouts/README.md) +1 |
| `2814` | Sales | `Sales` | 28 | 1 | yes | *name too generic to measure* |
| `2841` | Sales Exclusion | `SalesExclusion` | 19 | 1 | yes | [sales-exclusion-cap.md](data-fields/sales-exclusion-cap.md) +3 |
| `2883` | Sales Exclusion Cap | `SalesExclusionCap` | 23 | 2 | yes | [sales-exclusion-cap.md](data-fields/sales-exclusion-cap.md) +2 |
| `2849` | Sales Period | `VirtualSalesPeriod` | 66 | 0 | yes | [virtual-sales-period.md](data-fields/virtual-sales-period.md) +5 |
| `3144` | Scenario | `Scenario` | 69 | 4 | yes | [INDEX.md](INDEX.md) +25 |
| `3005` | Schedule Template | `VirtualTemplateSchedule` | 16 | 0 | yes | [004-company-administration.md](admin/004-company-administration.md) +6 |
| `2629` | Scheduled Job | `ScheduledJob` | **refused** | — | **no** | [work-flow-template-step.md](data-fields/work-flow-template-step.md) +1 |
| `2977` | Scheduled Offset | `ScheduledOffset` | 19 | 1 | yes | [link-relationship-tables.md](data-fields/link-relationship-tables.md) +7 |
| `3092` | Scratch Pad | `ScratchPad` | 1 | 0 | yes | [admin-tools.md](modules/reporting/admin-tools.md) +1 |
| `3093` | Scratch Pad Section | `ScratchPadSection` | **refused** | — | **no** | — |
| `2815` | Security Deposit | `SecurityDeposit` | 26 | 1 | yes | [008-manage-page-layouts.md](admin/008-manage-page-layouts.md) +12 |
| `2903` | Service Request | `ServiceRequest` | 30 | 3 | yes | [asset.md](data-fields/asset.md) +9 |
| `2451` | Site Survey | `SiteSurvey` | 79 | 1 | yes | [005-manage-data-fields.md](admin/005-manage-data-fields.md) +3 |
| `2816` | Space | `Space` | 27 | 3 | yes | *name too generic to measure* |
| `2585` | State Province Country | `StateProvinceCountry` | 11 | 5 | yes | [link-re-trans-scen-contact.md](data-fields/link-re-trans-scen-contact.md) +2 |
| `2448` | Task | `Task` | 37 | 2 | yes | *name too generic to measure* |
| `3000` | Task Predecessor | `TaskPredecessor` | 15 | 6 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) +1 |
| `3046` | Template Audit | `TemplateAudit` | 18 | 3 | yes | [template-audit.md](data-fields/template-audit.md) |
| `2817` | Tenant | `Tenant` | 42 | 3 | yes | *name too generic to measure* |
| `3075` | Usage | `Usage` | 14 | 1 | yes | *name too generic to measure* |
| `3080` | Usage Period | `VirtualUsagePeriod` | 66 | 0 | yes | [virtual-usage-period.md](data-fields/virtual-usage-period.md) +2 |
| `3076` | Use Based Rent | `UseBasedRent` | 23 | 2 | yes | [small-miscellaneous-entities.md](data-fields/small-miscellaneous-entities.md) +5 |
| `3078` | Use Based Rent Breakpoint | `UseBasedRentBreakpoint` | 31 | 1 | yes | [use-based-rent-breakpoint.md](data-fields/use-based-rent-breakpoint.md) +1 |
| `3081` | Use Based Rent Period | `VirtualUseBasedRentPeriod` | 23 | 0 | yes | [README.md](features/data-fields/README.md) |
| `3079` | Use Based Rent Summary Period | `VirtualUBRPAggregate` | 14 | 0 | yes | [README.md](features/data-fields/README.md) |
| `2630` | User Class Security | `UserClassSecurity` | 21 | 2 | yes | [user-class-security.md](data-fields/user-class-security.md) |
| `2842` | Variable Rent Offset | `VariableRentOffset` | 20 | 1 | yes | — |
| `2904` | Vendor Insurance | `VendorInsurance` | 15 | 2 | yes | [vendor-insurance.md](data-fields/vendor-insurance.md) |
| `2618` | Work Flow | `WorkFlow` | 19 | 6 | yes | *name too generic to measure* |
| `2619` | Work Flow Step | `WorkFlowStep` | 47 | 6 | yes | [work-flow-step-approver.md](data-fields/work-flow-step-approver.md) +4 |
| `2631` | Work Flow Step Approver | `WorkFlowStepApprover` | 20 | 5 | yes | [type-system.md](data-model/type-system.md) +1 |
| `2632` | Work Flow Step Assignee | `WorkFlowStepAssignee` | 11 | 6 | yes | — |
| `2621` | Work Flow Template | `WorkFlowTemplate` | 25 | 9 | yes | [work-flow-step-approver.md](data-fields/work-flow-step-approver.md) +8 |
| `2623` | Work Flow Template Step | `WorkFlowTemplateStep` | 56 | 10 | yes | [work-flow-step-approver.md](data-fields/work-flow-step-approver.md) +5 |
| `2624` | Work Flow Template Step Action | `WorkFlowTemplateStepAction` | 37 | 15 | yes | [work-flow-template-step-action.md](data-fields/work-flow-template-step-action.md) +1 |
| `2625` | Work Flow Template Step Member | `WorkFlowTemplateStepMember` | **refused** | — | **no** | — |
| `2907` | Work Order | `WorkOrder` | 30 | 3 | yes | [service-request.md](data-fields/service-request.md) +8 |

## 7. The gaps this file makes visible

| Gap | Size | Consequence |
|---|---:|---|
| Sql tables absent from the 223-object census | 25 | **Composition matters more than the count.** The catalogue derives from `ShowObjectDetails.jsp`, so every table that viewer refuses is absent **by construction**: **25** are the refused set (all recoverable over REST), **4** are the out-of-scope `Punch List` family, and only **2** are genuine in-scope omissions — `ChangeManage` and `VirtualTemplateMember`, one field each. The business-object census is essentially complete for in-scope work. Joined on **physical name**; a label join invents 12 phantom gaps. |
| Tables refused by the schema viewer | 25 | **Recoverable after all** — all 25 appear in `GET /rest/firm/types` and deep-serialise via `/rest/businessObject/{type}/lxid/{id}?deep=true`. The layout trio was recovered this way. REST returns only *populated* columns, so it is a lower bound. |
| Navigation nodes with no captured route | 36 | Groups mostly, plus every BBW-only Equipment Contract node. |
| Admin tools with no screenshot | 2 | Capture in progress. |
| Admin tools with no owning document | 23 | All 57 are classified with routes and 55 are screenshotted in `features/administration/`. Of the unowned, **10 are deliberate** — 6 budget/bidding (out of scope by decision) and 4 vendor-only `/lxadmin/` — so the real debt is the remainder. The five financial reference-data tools (discount rates, CPI, exchange rates, fiscal and holiday calendars) are the highest value: they feed the accounting engine. |
| Page layouts with no owning document | 0 | Every layout is enumerated with its mode, primary table and attachment in `features/page-layouts/`; **none is documented field by field**. |
| Sql tables with no owning document | 227 | Field detail exists for 202; no document explains an individual table. |
| Firm drop-downs with no owning document | 207 | Registry-level coverage only, in `data-model/code-table-registry.md`. |

### Census objects the sql-table picker never lists (27)

The gap runs both ways. These objects are in the 223-object census and absent from the 227-table picker, so neither inventory is complete — **the union is 254 distinct tables**. The `Code*` objects are expected (they are edited through `FirmCodeEdit.jsp`, not the sql viewer); the two `*FullImport` tables are not, and are a direct lead for import/export.

| Object |
|---|
| `BidPackageBreakout` |
| `BudgetLineGroup` |
| `BudgetLineLeaf` |
| `BudgetOptionTemplate` |
| `BudgetTemplate` |
| `BudgetTemplateAudit` |
| `CodeASC842Schedule` |
| `CodeAssetCategory` |
| `CodeBudgetColumnStatus` |
| `CodeExpenseType` |
| `CodeIFRS16Schedule` |
| `CodeIssueType` |
| `CodeProblem` |
| `CodeResponsibleParty` |
| `CodeSLSchedule` |
| `CodeSalesGroup` |
| `CodeSalesType` |
| `FolderSecurity` |
| `FolderTemplate` |
| `FolderTemplateAudit` |
| `PaymentTransactionFullImport` |
| `Security` |
| `TaskGroup` |
| `TaskItem` |
| `TaskTemplate` |
| `TaskTemplateAudit` |
| `WFStepFullImport` |

### Sql tables absent from the 223-object census

| sqlTableID | Table | Physical | Fields |
|---:|---|---|---:|
| `2885` | App Activity Log | `AppActivityLog` | **refused** |
| `2871` | Audit Master | `AuditMaster` | **refused** |
| `2517` | Committee Package Template | `CommitteePackageTemplate` | **refused** |
| `2605` | Custom Code Table | `CustomCodeTable` | **refused** |
| `2519` | Dashboard | `Dashboard` | **refused** |
| `2821` | Excel Server Status | `ExcelServerStatus` | **refused** |
| `2822` | Excel Service Log | `ExcelServiceLog` | **refused** |
| `2823` | Excel Service Queue | `ExcelServiceQueue` | **refused** |
| `2531` | Favorite Link | `FavoriteLink` | **refused** |
| `2878` | Global Property Section | `GlobalPropertySection` | **refused** |
| `3051` | Grid Preference | `GridPreference` | **refused** |
| `3068` | Information Overlay | `InformationOverlay` | **refused** |
| `2802` | Job Log | `JobLog` | **refused** |
| `2549` | Link Comm Pkg Templ Doc Content | `LinkCommPkgTemplDocContent` | **refused** |
| `2594` | Link Region Market | `LinkRegionMarket` | **refused** |
| `2562` | Map Client Budget | `MapClientBudget` | **refused** |
| `2644` | Notify Template | `NotifyTemplate` | **refused** |
| `2645` | Notify Template Member | `NotifyTemplateMember` | **refused** |
| `2611` | Page Layout | `PageLayout` | **refused** |
| `2612` | Page Layout Field | `PageLayoutField` | **refused** |
| `2613` | Page Layout Filter | `PageLayoutFilter` | **refused** |
| `3177` | Pgp Config | `PgpConfig` | **refused** |
| `2629` | Scheduled Job | `ScheduledJob` | **refused** |
| `3093` | Scratch Pad Section | `ScratchPadSection` | **refused** |
| `2625` | Work Flow Template Step Member | `WorkFlowTemplateStepMember` | **refused** |

---

_Generated by [`tools/build_coverage.py`](tools/build_coverage.py). Re-run after any new capture lands in `docs/tenants/`._
