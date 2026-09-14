---
title: "LAY-R-011 — One rule set declares one action"
tags: [rule, layouts-and-forms]
evidence: Observed
---

**`LAY-R-011`** · [[module-layouts-and-forms]] · **Observed**

A [[conditional-field|conditional rule set]] declares exactly one action — `SHOW`, `SHOW_AND_REQUIRE`
or `HIDE`.

**Visibility and required-ness are one decision**, not two. That is why
[[finding-no-layout-level-required|there is no separate layout-level required flag]]: the only
layout-level required-ness that exists is `showAndRequire`, and it is used **zero** times.

See [[rules-layouts-and-forms]] for the full register.
