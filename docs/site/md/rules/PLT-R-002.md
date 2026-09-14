# PLT-R-002 — `FirmID` is not a first-class reference type

*Platform & Tenancy · Derived*

**No `Firm ID` type exists among the declared FK types.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any code generator or ORM that maps Lx's declared `<Entity> ID` FK types to foreign keys |
| What it reads | The type vocabulary (`Facility ID`, `Contract ID`, `Employer ID`, …, and `FirmID` itself, typed `Text`) |
| The test | No `Firm ID` type exists among the declared FK types |
| What it writes | A schema-driven FK inference tool will silently miss the one relationship every row in the product ultimately has. Tenant references must be modelled deliberately, not discovered |

## Confidence

Derived — `project-entity.md` §4, corroborated by the type list in `../../data-model/graphql-api.md`

---

Source: `docs/modules/platform-tenancy/rules.md`
