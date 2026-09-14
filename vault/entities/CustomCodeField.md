---
title: CustomCodeField
tags: [entity, configuration]
evidence: Observed
---

**`custom_code_field` · 13 fields · layouts-forms-reporting**

The meta-definition of a tenant-created custom code or drop-down field — the machinery behind
[[client-drop-down|Client Drop Downs]].

It carries `ParentCustomCodeFieldID` (a self-reference) and `ParentCustomCodeTableID`, so **dependent
and cascading drop-downs are a real capability**.

And **all 38 of BBW's firm drop-downs have `ParentCustomCodeTableID` empty.** The capability exists
and is used nowhere — a useful negative for anyone sizing the rebuild.

`sTYPE_CUSTOM_CODE_FIELD` is the second-commonest [[firm-custom-field|firm field]] type, on 54 of
them.
