---
title: Person
tags: [entity, people, core]
evidence: Derived
---

**`person` · 37 fields · [[module-people-parties]]**

**A second supertype**, alongside [[ProjectEntity]] — and the most useful finding in its module.

`Person` and `NonMember` are **field-for-field identical: 37 fields, 37 matching types, zero
differences**. [[Member]] is that same 37-field block **plus 44** login and security columns. All three
share `PersonID` ([[rule-PPL-R-001]]).

So the identity aggregate is one supertype with two subtypes on a shared key: someone with a login
(`Member`) and someone without (`NonMember`), plus the plain contact.

**No hard FK type references a person.** The 12 columns typed `Contact` are a
[[soft-reference|soft type]], polymorphic into this aggregate ([[rule-PPL-R-002]]) — so a schema-driven
FK tool sees no relationship at all.

See [[Employer]] · [[Organization]]
