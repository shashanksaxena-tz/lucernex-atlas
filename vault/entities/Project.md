---
title: Project
tags: [entity, platform-tenancy, subtype-root]
evidence: Observed
---

**`project` · 111 fields · [[module-platform-tenancy]]**

A lightweight project identity record — and a genuine [[subtype-root]], distinct from the much richer
[[ProjectEntity]].

**The two are unreconciled, and that is a live problem.** `Project` and `ProjectEntity` are both
candidates for the spine, and [[rule-PLT-R-016]] says explicitly: do not silently pick one.

`Project.FacilityID` is the **one confirmed foreign key** that closes half of the
Site → Project → Facility promotion pipeline that [[Program]]'s two unique layout columns name
([[rule-POR-R-012]]). The first half — [[PotentialProject]] → Project — has no FK corroboration at all.

"Building it" ([[Project]]) and "leasing it" ([[Contract]]) are independent subtype roots with
independent financial engines ([[rule-POR-R-010]]).

`projects` returns **0 rows** in the live tenant.

See [[module-projects-capital]] · [[module-portfolio-transactions]]
