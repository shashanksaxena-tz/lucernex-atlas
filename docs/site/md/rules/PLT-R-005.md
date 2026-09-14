# PLT-R-005 — Global/Firm scope is a column, not a second schema

*Platform & Tenancy · Observed*

**Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | A tenant customises the field registry, or reads `GlobalProperty` |
| What it reads | `IsGlobal` + `FirmID` on `ReportGroupAvailableField`/`ReportGroupData`; `FirmID` alone on `GlobalProperty` |
| What it writes | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically |

## What it constrains

[GlobalProperty](../entities/GlobalProperty.md), [ReportGroupAvailableField](../entities/ReportGroupAvailableField.md), [ReportGroupData](../entities/ReportGroupData.md)

## Confidence

Observed — `udf-registry.md`, `../reporting/report-field-registry.md`. ## Security

---

Source: `docs/modules/platform-tenancy/rules.md`
