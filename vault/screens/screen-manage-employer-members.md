---
title: "Manage Employer Members"
tags: [screen, administration,people]
evidence: Observed
---

`/en/admin/ManageEmployerMembers.jsp`

![People belonging to an employer.](../assets/screenshots/bbw-admin/34-manage-employer-members.jpg)
`docs/assets/screenshots/bbw-admin/34-manage-employer-members.jpg` · `af-admin/35-manage-employer-members.jpg`

The join between [[Employer]] and the [[Person]] identity aggregate.

**And the relationship is invisible to schema-driven tooling**: no hard FK type references a person at
all — the 12 columns typed `Contact` are a [[soft-reference|soft type]], polymorphic into
[[Person]]/[[Member]]/[[NonMember]] ([[rule-PPL-R-002]]).

One of the six Member Administration screens the corpus names and has not opened in depth.

See [[screen-manage-members-contacts]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
