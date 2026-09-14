# LAY-R-013 — Rules for the ASG Edge+ rule engine

*Configuration, Layouts, Forms & Reporting · Derived*

**A predicate is a triple `(driverField, operator, value)`. Operators are constrained by the driver field's type: Dropdown → `IN`, `NOT_IN`, `IS_SPECIFIED`, `IS_NOT_SPECIFIED`;.**

A predicate is a triple `(driverField, operator, value)`. Operators are constrained by the driver field's type: Dropdown → `IN`, `NOT_IN`, `IS_SPECIFIED`, `IS_NOT_SPECIFIED`; Number → `EQ`, `NEQ`, `GT`, `GTE`, `LT`, `LTE`, `IS_SPECIFIED`, `IS_NOT_SPECIFIED`; Boolean → `SELECTED`, `NOT_SELECTED`.

---

Source: `docs/modules/layouts-and-forms/conditional-fields.md`
