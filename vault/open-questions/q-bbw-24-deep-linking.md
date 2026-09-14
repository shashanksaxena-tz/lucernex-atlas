---
title: "Q-BBW-24 — Is uniform deep-linking a requirement for ASG Edge+?"
tags: [open-question, navigation, product]
evidence: Observed
status: open
---

**A product decision, and the migration question is per-entity, not global.**

[[finding-routes-are-not-addressable|Sub-screen addressability differs by entity type]]:

| Root | Addressable |
|---|---|
| [[equipment-contract\|Equipment Contract]] | **none of 32** |
| [[Contract]] | **14 of 46** |

So **roughly a third of Contract's saved links would survive a migration and none of Equipment
Contract's would.**

Choosing routable URLs for ASG Edge+ is an **improvement but a departure** — it changes what a user's
bookmark means, and it cannot be presented as "migrating existing behaviour" because existing
behaviour is inconsistent.

The mechanism to replace: `EntityInfo.jsp` is the record **shell**, loading the active sub-screen into
an inner iframe. **Sub-screens are selected by the in-app menu tree, not by URL.** Appending
`&inPanel=true` to the `PForm` route does not change this — tested.

### How to settle it

Ask. And if the answer is yes, budget for the link migration per entity type rather than as one job.
