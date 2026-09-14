# PPL-R-005 — `Party` is a generic, classified role assignment, not an identity record

*People & Parties · Derived*

**Both `CompanyID` and `ContactID` are independently nullable.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | A role needs recording against a Contract that doesn't fit the standing roster (`LinkProjectEntityContact`) or a direct `Employer` relationship elsewhere on `Contract` |
| What it reads | `Party.CompanyID` (nullable `Employer ID`), `Party.ContactID` (nullable `Contact`, soft), `CodePartyGroupID`/`CodePartyTypeID`, `PrimaryFlag` |
| The test | Both `CompanyID` and `ContactID` are independently nullable |
| What it writes | A `Party` row can name a company, a person, or (in principle) both, classified by type — the escape hatch for a role that isn't one of the platform's named relationships |

## What it constrains

[LinkProjectEntityContact](../entities/LinkProjectEntityContact.md), [Employer](../entities/Employer.md), [Contract](../entities/Contract.md), [Party](../entities/Party.md)

Columns named: `Party.CompanyID`, `Party.ContactID`

## Confidence

Derived — field shape only, no live capture of populated rows

---

Source: `docs/modules/people-parties/rules.md`
