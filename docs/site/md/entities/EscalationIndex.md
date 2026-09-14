# EscalationIndex

*12 fields · module: Lease Accounting & Payments · Postgres: `escalation_index`*

A named index value series (e.g., a specific published CPI series) used to drive ExpenseEscalation calculations.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 12 |
| Catalogued fields | 12 (12 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-042](../rules/CON-R-042.md) | The driver is index-based: rawChange = (IndexAmount / IndexBaseFactor) − 1 — assumes IndexAmount is a level, which is unconfirmed. | Inferred |

## Fields

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeIndexGroupID` | Index Group | Dropdown (Index Group Code) | Global |  | Index Group Code |
| `CodeIndexSourceID` | Index Source | Dropdown (Index Source Code) | Global |  | Index Source Code |
| `CodeIndexTypeID` | Index Type | Dropdown (Index Type Code) | Global |  | Index Type Code |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IndexAmount` | Index Amount | Percentage | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EscalationIndexID` | Escalation Index RecID | Number | Global |  |  |
| `PeriodMonth` | Period Month | Number | Global |  |  |
| `PeriodYear` | Period Year | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EscalationIndexName` | Escalation Index Name | Text | Global | yes |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Escalation Index ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [ExpenseEscalation](ExpenseEscalation.md) | `EscalationIndexID` |
