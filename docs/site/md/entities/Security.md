# Security

*21 fields · module: Platform & Tenancy · Postgres: `none exported`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 21 declared fields, filed under Platform & Tenancy, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 17 of its 21 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Fields with a vendor definition | 17 of 21 inventoried |
| Physical tables | — |
| Replication database | — |
| Catalogued fields | not in the catalogue |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### 17 fields carry a vendor definition

**Observed.** 17 of this record's 21 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### 21 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 21 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-006](../rules/PLT-R-006.md) | Both declare the same 21 fields | Derived |

## Fields

### Relationships (foreign keys) (7)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnTypeID` | Budget Column Type | This field determines the security for a given budget type for a user class. | Budget Type ID | — |  | not extracted | [BudgetColumnType](BudgetColumnType.md) |
| `DashboardComponentID` |  |  | DashboardComponent ID | — |  | not extracted | unresolved |
| `PageLayoutID` | Page Layout | This field determines the security for a given page layout for a user class. | item ID | — |  | not extracted | unresolved |
| `ReportGroupAvailableFieldID` | Report Group Available Field | The reporting field that is associated with the object. | Report/Form Field ID | — |  | not extracted | [ReportGroupAvailableField](ReportGroupAvailableField.md) |
| `ReportGroupDataID` | Report Group Data | The Report Group Data that is associated with the security object. | item ID | — |  | not extracted | unresolved |
| `RootReportGroupDataID` | Parent Report Group |  | item ID | — |  | not extracted | unresolved |
| `SubReportGroupDataID` | Report Group |  | item ID | — |  | not extracted | unresolved |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SecurityLevelByteValue` |  |  | Dropdown | — |  | not extracted |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeSecurityPrivilegeID` | Security Privilege | This field determines the security for a given action for a user class. | Dropdown (Security Privilege Code) | — |  | not extracted | Security Privilege Code |
| `CodeUserClassID` | User Class | This field determines the user class that the security is associated with. | Dropdown (User Class) | — | yes | not extracted | User Class |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `UserClassSecurityID` | User Class Security RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | not extracted |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DashboardComponentTitle` | Dashboard Component Title | The value of this field is computed from the title of the associated dashboard component. | Text | — |  | not extracted |  |
| `GroupHierarchy` | Name With Full Hierarchy | The value of this field is computed as the full hierarchy of groups, up to the root group, including the name of the current security object. | Text | — |  | not extracted |  |
| `GroupHierarchyNoPrefix` | Group Hierarchy | The value of this field is computed as the full hierarchy of groups, up to the root group, but doesn't include the name of the current security object. | Text | — |  | not extracted |  |
| `ParentGroupName` | Parent Group Name | The value of this field is computed as the name of the parent group of the security object. | Text | — |  | not extracted |  |
| `SecurityLevelName` | Security Level | The localized name of the security level (No Access, View, Edit, Delete). | Text | — |  | not extracted |  |
| `SecurityObjectNameText` | Security Object Name | The localized name of the item that the security object is for. | Text | — |  | not extracted |  |
| `SecurityType` | Security Type | This field returns name of the security type (Page, Action, Field, Budget). | Text | — |  | not extracted |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | User Class Security ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | — | yes | not extracted |  |
| `ModifiedByID` | Modified By | Determines the security for a given page layout for a user class. | Member ID | — |  | not extracted | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Computed as the name of the parent group of the security object. | Time | — |  | not extracted |  |
