---
title: "Caveat: every UI label may be tenant-local"
tags: [caveat, method, configuration, meta]
evidence: Observed
---

`Manage Firm Dictionary` ([[screen-manage-firm-dictionary]]) lets a firm **overwrite field labels
tenant-wide** by uploading a spreadsheet — the screen's own note offers it *"to provide new
translation or to just overwrite the field labels"* — with global and firm-specific layers and
per-language variants.

**This is a caveat on the whole corpus, not one document.** Every screen name, navigation node name,
field label and [[code-table]] value name recorded anywhere may be a tenant-local override rather than
the product's own vocabulary.

**Internal names are unaffected** — `ScriptName`, `CodeContractStatusID`, physical table names — which
turns the writing convention *"use real field and table names in `code`, never paraphrases"* from a
style preference into a **correctness requirement**.

It also explains a measurement error. The census reconciliation reported 18 missing tables when matched
on UI label and **6** when matched on physical name; ten of the twelve phantoms were
[[virtual-projection|`Virtual*`]] views the UI renames, and one was [[ProjectEntity]] itself, labelled
*"General Entity Info"*. Label-versus-physical-name mismatch is exactly the failure this mechanism
produces at scale — see [[method-cheap-signals]].

Whether either tenant has actually overridden anything is **unknown**. One `Download Current
Dictionary` with *Firm specific phrases* selected would settle it.

Source: [`features/administration/`](../../docs/features/administration/README.md)
