# CustomCodeField

*13 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `custom_code_field`*

Meta-definition of a tenant-created custom code/dropdown field — the schema record behind Manage Custom Lists (see 006).

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CustomCodeTableID` | Table Name | Custom Drop Down ID | Global | yes | unresolved |
| `ParentCustomCodeFieldID` | Parent Custom Code Field | Custom Field ID | Global |  | [CustomCodeField](CustomCodeField.md) |
| `ParentCustomCodeTableID` | Parent Custom Code Table | Custom Drop Down ID | Global |  | unresolved |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CustomCodeFieldID` | Custom Code Field RecID | Number | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` |  | Boolean | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CustomCodeFieldName` | Field Name | Text | Global | yes |  |
| `Description` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Custom Code Field ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [CustomCodeField](CustomCodeField.md) | `ParentCustomCodeFieldID` |
