# PPL-R-001 — `Person` is a supertype; `Member` and `NonMember` are its subtypes on a shared key

*People & Parties · Derived*

**`Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any read or write that treats `Member`, `Person`, or `NonMember` as unrelated tables |
| What it reads | `PersonID`, typed `Number` (not a declared FK type) on all three objects |
| The test | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields |
| What it writes | All three share one identity key space. A rebuild should model one identity aggregate with an optional login/authorization extension, not three tables |

## What it constrains

[Member](../entities/Member.md), [Person](../entities/Person.md), [NonMember](../entities/NonMember.md)

## Confidence

Derived — exhaustive field diff, `member-vs-person-vs-party.md`

---

Source: `docs/modules/people-parties/rules.md`
