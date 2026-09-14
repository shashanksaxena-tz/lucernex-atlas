---
title: Security and access
tags: [feature, security]
evidence: Observed
---

Concepts: [[security-ladder]] · [[audit-trail]]
Entities: [[UserClassSecurity]] · [[Security]]

Four securable kinds on four tabs: **Page Access**, **Actions (70 verbs)**, **Field Security (6,553
fields)**, Budget Columns. `SecurityFieldSecurity.jsp` is a **5.0 MB page with 26,212 radio inputs**.

Two corrections this feature delivered, both of which mattered:

1. **Read-only is `View` on a field**, not a field property. The [[data-field-catalog|catalog]]'s
   uniform `ReadOnly = No` is measuring a different question, not erroring.
2. **It refutes the three-gate explanation of the [[equipment-contract|Equipment Contract]] root.**
   Page access is granted at AF for **8 of 10** classes, and [[Program]] is granted by **all ten** and
   also fails to render. So a fourth mechanism existed — and it is
   [[finding-root-renders-iff-record-exists]].

The trap that caused the error: **`Default` means *inherit*, not *allowed***.

Method note worth reusing: the class selector is a **GET parameter**
(`SecurityPageAccess.jsp?UserClass={id}`), so all ten classes can be read with no UI interaction. And
the tabs default to *different* classes — Page Access opens on `Default Security` (`7884`), Field
Security on `System Administrator` (`7885`).

**14 menu structures, 892 nodes** exist against the 4–5 roots a user meets.

Screens: [[screen-manage-security]] · [[screen-audit-reports]]

[`features/security-access/`](../../docs/features/security-access/README.md)
