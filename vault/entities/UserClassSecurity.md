---
title: UserClassSecurity
tags: [entity, security, platform-tenancy]
evidence: Observed
---

**`user_class_security` · 21 fields · [[module-platform-tenancy]]**

The editable permission grant — the real table behind [[Security]]'s projection.

Its columns name the four securable surfaces directly: `SecurityLevelByteValue`, `PageLayoutID`,
`ReportGroupAvailableFieldID`, `ReportGroupDataID`, `DashboardComponentID`. A grant targets **exactly
one** of them, at a level from `DEFAULT`, `NO_ACCESS`, `VIEW`, `EDIT`, `DELETE`
([[rule-PLT-R-007]]).

[[tenant-american-freight|American Freight]] has **10 user classes**. `Default Security` (id `7884`)
denies almost everything — and is what the Page Access tab loads on, which is a trap for anyone
reading the blank matrix as "unselected".

**`Default` means inherit, not allowed** — see [[security-ladder]] and
[[finding-root-renders-iff-record-exists]].

Screens: [[screen-manage-security]]
