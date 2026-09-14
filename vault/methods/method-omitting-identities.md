---
title: "Method: identities are deliberately not recorded"
tags: [method, meta, privacy]
---

Screenshots and captures in this corpus contain the names of real ASG staff — workflow approvers,
lease analysts, members, contacts.

> **No note in this vault records a real individual's name.**

Where the source recorded an approver, only **`approverCount`** is carried. `bbw-workflow-steps.json`
was captured with approver identities **deliberately omitted at capture time**, not redacted
afterwards.

This is why [[finding-routing-is-to-named-people]] is stated as *"a list of named individuals"* and
never as a list. The finding survives the omission intact — the fact that matters is that routing
resolves to people rather than to positions, and the count is enough to establish it.

Related: the `RESTful WebService Docs` admin page **renders live Basic and JWT credentials** for copy.
It is one of only two of the 57 admin tools with **no screenshot**, and the capture was structure-only
— no token was read, captured or recorded at any point. The other is `Delete Entities`.

The BBW capture was also **read-only throughout**: no record, layout, drop-down, workflow or rule was
created, edited, saved or deleted. No `Save` button was clicked. Every probe was a `GET`. Which is
also why [[q-bbw-03-task-step]] and [[q-bbw-15-import-results]] could not be answered — both would
require a write.

See [[README]]
