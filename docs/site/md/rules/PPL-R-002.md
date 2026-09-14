# PPL-R-002 — No hard FK type references a person directly; `Contact` is the soft, polymorphic type

*People & Parties · Inferred*

**No `Person ID` FK type exists anywhere in the 60-odd declared FK types.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any column that needs to reference "a person" from another object |
| What it reads | 12 columns across the schema declared type `Contact` (`Employer.AccountRepPersonID`, `Party.ContactID`, `LinkProjectEntityContact.PersonID`/`Landlord_PersonID`, `ProjectEntity. LinkProjectEntityContactListData` on all 9 spine roots, and others) |
| The test | No `Person ID` FK type exists anywhere in the 60-odd declared FK types |
| What it writes | A field typed `Contact` may resolve to a `Person`, `Member`, or `NonMember` row interchangeably. Model it as a polymorphic reference into the identity aggregate, not as an FK to a single physical table |

## What it constrains

[Employer](../entities/Employer.md), [Party](../entities/Party.md), [LinkProjectEntityContact](../entities/LinkProjectEntityContact.md), [Person](../entities/Person.md), [Member](../entities/Member.md), [NonMember](../entities/NonMember.md)

Columns named: `Employer.AccountRepPersonID`, `Party.ContactID`, `LinkProjectEntityContact.PersonID`

## Rules it cites

[PPL-R-001](PPL-R-001.md)

## Confidence

Inferred — consistent with PPL-R-001 and with `project-entity.md`'s precedent for soft types (`Entity`, and `FirmID`'s missing FK type), but not directly observed resolving live

---

Source: `docs/modules/people-parties/rules.md`
