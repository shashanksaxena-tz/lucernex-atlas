---
title: Employer
tags: [entity, people, core]
evidence: Observed
---

**`employer` · 71 fields · [[module-people-parties]]**

**One table serving vendor, landlord and tenant alike.** There is **no `Vendor`, `Landlord` or
`Tenant` object anywhere** in the 223-object schema — all three are `Employer` under different column
names ([[rule-PPL-R-004]]).

The proof is in the type system: `PaymentTransaction.VendorID` is declared type **`Employer ID`**. The
FK type name and the column name disagree, and the type is right.

Fourth in in-degree: **30 objects, 40 columns**. The property-tax family alone references it in **four
separate roles**.

This is one of four FK type names that lie about their target — see [[type-system]].

Screens: [[screen-manage-employers]] · [[screen-manage-vendors]]
