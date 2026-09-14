---
title: "LAY-R-130 — Rules are posted as one JSON document"
tags: [rule, layouts-and-forms]
evidence: Observed
---

**`LAY-R-130`** · [[module-layouts-and-forms]] · **Observed**

A [[conditional-field|conditional rule set]] is posted as a **single JSON document**
(`json.conditionalFieldsConfig`), not as normalised rows.

That storage choice is what causes [[rule-LAY-R-134]], and it is half of why a probe reading the
served HTML [[method-fetch-is-not-render|could never have observed a rule]].

See [[rules-layouts-and-forms]] for the full register.
