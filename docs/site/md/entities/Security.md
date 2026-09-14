# Security

*21 fields · module: Platform & Tenancy · Postgres: `none exported`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 21 declared fields, filed under Platform & Tenancy, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Catalogued fields | not in the catalogue |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-006](../rules/PLT-R-006.md) | Both declare the same 21 fields | Derived |

## Fields

### Relationships (foreign keys) (7)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnTypeID` |  | Budget Type ID | — |  | [BudgetColumnType](BudgetColumnType.md) |
| `DashboardComponentID` |  | DashboardComponent ID | — |  | unresolved |
| `PageLayoutID` |  | item ID | — |  | unresolved |
| `ReportGroupAvailableFieldID` |  | Report/Form Field ID | — |  | [ReportGroupAvailableField](ReportGroupAvailableField.md) |
| `ReportGroupDataID` |  | item ID | — |  | unresolved |
| `RootReportGroupDataID` |  | item ID | — |  | unresolved |
| `SubReportGroupDataID` |  | item ID | — |  | unresolved |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SecurityLevelByteValue` |  | Dropdown | — |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeSecurityPrivilegeID` |  | Dropdown (Security Privilege Code) | — |  | Security Privilege Code |
| `CodeUserClassID` |  | Dropdown (User Class) | — |  | User Class |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `UserClassSecurityID` |  | Number | — |  |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DashboardComponentTitle` |  | Text | — |  |  |
| `GroupHierarchy` |  | Text | — |  |  |
| `GroupHierarchyNoPrefix` |  | Text | — |  |  |
| `ParentGroupName` |  | Text | — |  |  |
| `SecurityLevelName` |  | Text | — |  |  |
| `SecurityObjectNameText` |  | Text | — |  |  |
| `SecurityType` |  | Text | — |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` |  | Text | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
