---
title: "RPT-R-063 — There is no report-data export"
tags: [rule, reporting]
evidence: Derived
---

**`RPT-R-063`** · [[module-reporting]] · **Derived**

ASG requires a **report-to-import round trip**. Lx exports field **metadata** only — there is **no
report-data equivalent**.

Combined with [[finding-no-generic-export]] and the fact that GraphQL carries no layout or report
type at all, **reports cannot be migrated through any API.** They are a hand rebuild.

See [[rules-reporting]] for the full register.
