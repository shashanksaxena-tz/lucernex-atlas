---
title: LinkMemberProjectEntity
tags: [entity, platform-tenancy, people]
evidence: Observed
---

**`link_member_project_entity` · 7 fields · [[module-platform-tenancy]]**

The join assigning a [[Member]] to a [[ProjectEntity]] in an org-chart role — one of the 50 genuine
(non-[[audit-trail|audit]]) inbound edges on `Member`.

It is the mechanism behind the `Members/Contacts` screen that appears under **every** navigation root,
served by `MemberDirectory.jsp`.

See [[screen-manage-membership]]
