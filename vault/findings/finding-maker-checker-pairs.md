---
title: The abstraction workflow is maker-checker pairs — with one gap
tags: [finding, workflow, accounting]
evidence: Derived
---

[[tenant-bbw|BBW]]'s two `Implementation Workflow` templates are the **first direct evidence anywhere
in this corpus** for BRD-24's abstraction path, which was wholly unobserved at
[[tenant-american-freight|American Freight]].

**Document Abstraction** (2 steps): `Abstract Lease Documents` → `Review Lease Abstract`.

**Financial Abstraction** (6 steps) — and note the alternation:

| Step | Name | Approval Level |
|---:|---|---|
| 1 | Set up Recurring Expenses | Ad Hoc |
| 2 | Review Recurring Expenses | Member |
| 3 | Set Up Percent Rent | Ad Hoc |
| 4 | Review Percent Rent | Member |
| 5 | **Set Up ASC 842 Schedules** | ***(none)*** |
| 6 | Final Review of Financial Abstract | Member |

**The pattern is maker-checker pairs**: an `Ad Hoc` set-up step followed by a `Member` review step,
once per financial layer, closed by a final review.

> **Step 5 has no approval level at all.** The ASC 842 schedule set-up is the one financial layer with
> no paired reviewer — which, given its materiality, is worth raising.

The six steps map one-for-one onto the seven `ASG Lease Abstract - *` layouts
([[ExpenseSetup]], [[ExpenseSchedule]], [[PercentageRent]], [[Covenant]], [[KeyDate]],
[[ContractTerm]], Funds and Expenses) — together with the two `ASG Approval - *` list layouts, **this
is the abstraction pipeline's own UI**, and underneath it sits
[[atlas-ai-abstraction|a production AI integration]].

**So the BRD's abstraction path is not purely human.** See [[finding-tenants-differ-by-one-feature]].

`Lease Admin Request`'s eight steps — BRD-24's, observed for the first time — carry two flags worth
checking before any migration: **steps 5 and 6 share one form**, and **step 8's name and its form name
disagree** ([[q-bbw-08-step-8-form-mismatch]]).
