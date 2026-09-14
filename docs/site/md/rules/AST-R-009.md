# AST-R-009 — Asset carries three parallel maintenance-SLA blocks: Maintenance, Repair, Replacement

*Assets, Equipment & Maintenance · Observed*

**Input: For each of the three event types, a `Code{X}PartyID` (Responsible Party code), `{X}ResponsiblePersonID` (a `Person` contact), `Code{X}RemedyID` (a Maintenance Remedy code), and `{X}MaximumRemedyDays` (a day count) — twelve fields total, four per event type. Effect: Each event type has an….**

Input: For each of the three event types, a `Code{X}PartyID` (Responsible Party code), `{X}ResponsiblePersonID` (a `Person` contact), `Code{X}RemedyID` (a Maintenance Remedy code), and `{X}MaximumRemedyDays` (a day count) — twelve fields total, four per event type. Effect: Each event type has an independently configurable responsible party, a named contact, a remedy classification, and an SLA day count. Confidence: Observed (exhaustive field-list read, `_lucernex_objects_summary.txt`).

## What it constrains

[Person](../entities/Person.md)

## Confidence

Observed (exhaustive field-list read, `_lucernex_objects_summary.txt`)

---

Source: `docs/modules/assets-equipment/rules.md`
