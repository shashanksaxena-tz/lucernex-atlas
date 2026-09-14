---
title: Workflow routing resolves to named individuals
tags: [finding, workflow, people]
evidence: Observed
---

The workflow module's documented finding is that *"routing is by organisational position, not by
name"*. That holds for the [[WorkFlowTemplate]] **routing model**. It does not describe what is
configured.

**Every approval level actually configured at [[tenant-bbw|BBW]] resolves to an explicit list of named
members.** `Approval Level` takes exactly two values across all 62 steps — `Member` and `Ad Hoc` — and
where it is `Member`, the `Approver` column is a list of individuals. At
[[tenant-american-freight|AF]], **17 of 19** live steps route by named Member ([[rule-PPL-R-012]]).

> **A rebuild that routes only by position will not reproduce this tenant's configuration.**

The apparatus exists and is largely unused. A [[Member]]'s routable identity has **three independent
axes** — user class, job title, supervisor org chart ([[rule-PPL-R-009]]) — and Member's **eight
approval-amount band columns are read by no observed workflow field** at all
([[rule-PPL-R-013]]).

That is a question for the business, not a defect: routing by name is simpler and it is what ASG does.
But it means the org-chart machinery is not load-bearing evidence for anything.

**Approver identities are real ASG staff and are deliberately excluded from this corpus** — only
counts are recorded. See [[method-omitting-identities]] and [[WorkFlowStepApprover]].
