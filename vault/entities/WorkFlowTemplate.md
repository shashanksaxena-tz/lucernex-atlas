---
title: WorkFlowTemplate
tags: [entity, workflow, core]
evidence: Observed
---

**`work_flow_template` · 25 fields · [[module-workflow]]** · firm-global

The reusable workflow definition. **13 at [[tenant-bbw|BBW]] against 4 at
[[tenant-american-freight|American Freight]]**, and they are
[[publish-and-fork|tenant-authored]] — names mostly differ, no clustered id-offset block, unlike the
layouts.

| Template | ID | Steps |
|---|---:|---:|
| ASC 842 Tracking | 2475 | 2 |
| Cotenancy Update | 2478 | 2 |
| **Implementation Workflow — Document Abstraction** | 2401 | 2 |
| **Implementation Workflow — Financial Abstraction** | 2402 | 6 |
| **Lease Admin Request** | 2472 | **8** |
| Lease Admin Request v1 / v2 | 2399 / 2468 | 8 / 10 |
| Lease Date Review | 2473 | 2 |
| `Lucernex Change Request` (+ v1) * | 2469 / 2463 | 6 / 5 |
| User Request | 2400 | 2 |
| Vendor Change (Notice) | 2461 | 4 |
| Vendor Changes (Integration) | 2418 | 5 |
| **Total** | | **62** |

\* The vendor's product name appears here because it is the **configured template name in the tenant**, reproduced as captured data. Everywhere else in this vault the product is called **Lx**.

Fields read from `formSubmit=viewBO` that the corpus had never recorded: four "notify on complete"
flags, `Auto assign initiator as ad hoc assignee`, `Default Work Flow Priority`,
**`Conditional Workflow JS`** ([[q-bbw-06-conditional-workflow-js]]), `Enable Vendor Collaboration`,
and `Process kicked off by:` reading *"(work flow specified as kickoff action in another work flow)"*
— **workflows chain** ([[q-bbw-07-workflow-kickoff-graph]]).

See [[finding-workflow-versioning-is-naming]] · [[finding-form-workflow-not-1-1]] ·
[[screen-manage-work-flows]]
