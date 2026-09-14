---
title: Form and workflow are not 1:1 — that was one tenant's coincidence
tags: [finding, workflow, retraction]
evidence: Observed
---

The workflow module recorded *"four live workflows, 1:1 with four form types"*. True at
[[tenant-american-freight|American Freight]] (4 and 4). **False at [[tenant-bbw|BBW]]: 13 workflow
templates against 6 form types.**

- Only **4 of 13** BBW workflow names match a form name.
- **9 match none.**
- **2 form types have no workflow at all.**
- Archived workflow versions retain their form type, so several workflows share one.

**It is a coincidence of one tenant, not a platform rule.** A rebuild that enforces the cardinality
would refuse configurations the incumbent permits and ASG actually uses.

This is the clearest single case for why the second tenant was worth reading: a confident, documented,
evidence-backed claim from one tenant that a second tenant refutes in one screen. See
[[tenant-bbw]].

The underlying mechanism is unchanged and still true — **[[form-vs-page|a Form *is* an Issue Type]]**
([[CodeIssueType]], `TableType 2035`). It is only the cardinality that was wrong.

See [[feature-workflows-forms]]
