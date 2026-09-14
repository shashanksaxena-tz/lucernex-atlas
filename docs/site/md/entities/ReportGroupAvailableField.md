# ReportGroupAvailableField

*27 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `report_group_available_field`*

Metadata about the Data Fields catalog itself — API table name, dropdown table name, field type and definition — meaning this entity is Lx describing its own field-metadata system, the same system this documentation set is built from. 27 Global fields under Company Items, directly relevant to understanding how Manage Data Fields (005) is implemented.

Source: `data-fields/report-group-available-field.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 4 keys from 4 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 4 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-150](../rules/LAY-R-150.md) | Placeable fields come from the shared field registry (`ReportGroupAvailableField`), scoped to the layout's Primary Table, presented as the Available Fields tree. · Observed · 008 | Observed |
| [LAY-R-171](../rules/LAY-R-171.md) | The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves; | Observed |
| [RPT-R-010](../rules/RPT-R-010.md) | Report columns are drawn from the same field registry as forms — `ReportGroupAvailableField`, whose FK type Lx names `Report/Form Field ID`. There is no separate report-field catalog. | Observed |
| [PLT-R-005](../rules/PLT-R-005.md) | Tenant-specific configuration and platform-default configuration live in the same table, discriminated by a boolean/text pair, not partitioned physically | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ParentReportGroupDataID` | Parent Report Group | item ID | Global |  | unresolved |
| `ReportGroupDataID` | Report Group | item ID | Global | yes | unresolved |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FormFieldType` | Field Type | Dropdown | Global | yes |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeSQLTableID` | Table Name | Dropdown (SQL Table Code) | Global | yes | SQL Table Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MaxLength` | Maximum Length | Number | Global |  |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsClientExtensionField` | Is UDF Field? | Boolean | Global |  |  |
| `IsFunctional` | Is Functional? | Boolean | Global |  |  |
| `IsGlobal` | Is Global Field? | Boolean | Global |  |  |
| `IsReadOnly` | Is ReadOnly? | Boolean | Global |  |  |
| `IsRequired` | Is Required? | Boolean | Global |  |  |

### Text & notes (15)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccessorName` | Field Name | Text | Global |  |  |
| `ApiTableName` | Api Table Name | Text | Global |  |  |
| `DefaultLabel` | Label | Text | Global | yes |  |
| `DefaultValue` | Default Value | Text | Global |  |  |
| `Definition` |  | Text | Global |  |  |
| `DropdownTableName` | Dropdown Table Name | Text | Global |  |  |
| `FieldText` |  | Text | Global |  |  |
| `FirmID` |  | Text | Global |  |  |
| `GlobalDefinition` | Global Definition | Text | Global |  |  |
| `HierarchyName` | Hierarchy Name | Text | Global |  |  |
| `ScriptName` | Script Name | Text | Global |  |  |
| `TableName` | Table Detail | Text | Global |  |  |
| `UILabel` | Report Field Label | Text | Global |  |  |
| `VersionAdded` | Version Added | Text | Global |  |  |
| `VersionModified` | Version Modified | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedDate` | RGAF Created Date | Date | Global |  |  |
| `ModifiedDate` | RGAF Modified Date | Date | Global |  |  |

## What points here (4 keys)

| Record type | Via column |
|---|---|
| [CLRExtensionPart](CLRExtensionPart.md) | `ReportGroupAvailableFieldID` |
| [ClientListRow](ClientListRow.md) | `ReportGroupAvailableFieldID` |
| [Security](Security.md) | `ReportGroupAvailableFieldID` |
| [UserClassSecurity](UserClassSecurity.md) | `ReportGroupAvailableFieldID` |
