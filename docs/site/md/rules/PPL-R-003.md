# PPL-R-003 — `ConvertToMember` implies promotion, not replacement

*People & Parties · Inferred*

**The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | A `Person`/`NonMember` is granted system login |
| What it reads | `Member.ConvertToMember` (Boolean) |
| What it writes | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1 |

## What it constrains

[Person](../entities/Person.md), [NonMember](../entities/NonMember.md), [Member](../entities/Member.md)

Columns named: `Member.ConvertToMember`

## Confidence

Inferred from the field name alone. ## Companies and roles

---

Source: `docs/modules/people-parties/rules.md`
