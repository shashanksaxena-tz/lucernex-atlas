# ReportGroupAvailableField

*27 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `report_group_available_field`*

Metadata about the Data Fields catalog itself — API table name, dropdown table name, field type and definition — meaning this entity is Lx describing its own field-metadata system, the same system this documentation set is built from. 27 Global fields under Company Items, directly relevant to understanding how Manage Data Fields (005) is implemented.

Source: `data-fields/report-group-available-field.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Fields with a vendor definition | 22 of 27 inventoried |
| Physical tables | `report_group_available_field` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 4 keys from 4 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 4 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in report_group_available_field

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 22 fields carry a vendor definition

**Observed.** 22 of this record's 27 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 27 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 4 are marked required.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ParentReportGroupDataID` | Parent Report Group | This field captures the ID of the parent report group. | item ID | Global |  | `report_group_available_field.ParentReportGroupDataID · TEXT` | unresolved |
| `ReportGroupDataID` | Report Group | The ID of the Report Group associated with the field. | item ID | Global | yes | `report_group_available_field.ReportGroupDataID · TEXT` | unresolved |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FormFieldType` | Field Type | Calculated as true if the field has a client extension field number. | Dropdown | Global | yes | `report_group_available_field.FormFieldType · TEXT` |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeSQLTableID` | Table Name | Select the database table that the field should be associated with from this field. Our best practice recommendation is to select the highest table level possible. | Dropdown (SQL Table Code) | Global | yes | `report_group_available_field.CodeSQLTableID · TEXT` | SQL Table Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MaxLength` | Maximum Length | This field specifies the maximum length in characters the field may have. | Number | Global |  | `report_group_available_field.MaxLength · TEXT` |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsClientExtensionField` | Is UDF Field? | The value of this field is true if the field has a client extension field number. | Boolean | Global |  | `report_group_available_field.IsClientExtensionField · TEXT` |  |
| `IsFunctional` | Is Functional? | This indicates whether a field is functional or informational. A field is functional when it impacts other parts of the system, and a field is informational when it does not impact other parts of the system. | Boolean | Global |  | `report_group_available_field.IsFunctional · TEXT` |  |
| `IsGlobal` | Is Global Field? |  | Boolean | Global |  | `report_group_available_field.IsGlobal · TEXT` |  |
| `IsReadOnly` | Is ReadOnly? |  | Boolean | Global |  | `report_group_available_field.IsReadOnly · TEXT` |  |
| `IsRequired` | Is Required? | The Required? flag defaults to No and is read-only. To make a field required, modify the field from the Manage Page Layouts section of the System Administrator Dashboard or the Manage Forms page. | Boolean | Global |  | `report_group_available_field.IsRequired · TEXT` |  |

### Text & notes (15)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccessorName` | Field Name | Enter the field name in this field. This field name is used to identify the field in the database. The Field Name must not contain spaces. | Text | Global |  | `report_group_available_field.AccessorName · TEXT` |  |
| `ApiTableName` | Api Table Name |  | Text | Global |  | `report_group_available_field.ApiTableName · TEXT` |  |
| `DefaultLabel` | Label | Enter the field label that will be displayed on the page in this field. | Text | Global | yes | `report_group_available_field.DefaultLabel · TEXT` |  |
| `DefaultValue` | Default Value | If you want a default value to appear in the field, enter the default value in this field. | Text | Global |  | `report_group_available_field.DefaultValue · TEXT` |  |
| `Definition` |  | This field displays the definition your system administrator has entered for a field, if there is one. | Text | Global |  | `report_group_available_field.Definition · TEXT` |  |
| `DropdownTableName` | Dropdown Table Name |  | Text | Global |  | `report_group_available_field.DropdownTableName · TEXT` |  |
| `FieldText` |  | This field stores additional information about the field. Notable case: this field holds the math expression for SimpleMathFields. | Text | Global |  | `report_group_available_field.FieldText · TEXT` |  |
| `FirmID` |  | The record's Firm ID. | Text | Global |  | `report_group_available_field.FirmID · TEXT` |  |
| `GlobalDefinition` | Global Definition | This field displays the global definition of a field. | Text | Global |  | `report_group_available_field.GlobalDefinition · TEXT` |  |
| `HierarchyName` | Hierarchy Name | The computed Report Group Data hierarchy list of the field without the field included, separated by colons, such as Pro Forma Lease : General Lease Info. | Text | Global |  | `report_group_available_field.HierarchyName · TEXT` |  |
| `ScriptName` | Script Name | This is the script name for the field. | Text | Global |  | `report_group_available_field.ScriptName · TEXT` |  |
| `TableName` | Table Detail | This is the table name for the field. | Text | Global |  | `report_group_available_field.TableName · TEXT` |  |
| `UILabel` | Report Field Label |  | Text | Global |  | `report_group_available_field.UILabel · TEXT` |  |
| `VersionAdded` | Version Added | The version a global field was added to the system. | Text | Global |  | `report_group_available_field.VersionAdded · TEXT` |  |
| `VersionModified` | Version Modified | The version a global field was modified in the system. | Text | Global |  | `report_group_available_field.VersionModified · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedDate` | RGAF Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Date | Global |  | `report_group_available_field.CreatedDate · TEXT` |  |
| `ModifiedDate` | RGAF Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Date | Global |  | `report_group_available_field.ModifiedDate · TEXT` |  |

## What points here (4 keys)

| Record type | Via column |
|---|---|
| [CLRExtensionPart](CLRExtensionPart.md) | `ReportGroupAvailableFieldID` |
| [ClientListRow](ClientListRow.md) | `ReportGroupAvailableFieldID` |
| [Security](Security.md) | `ReportGroupAvailableFieldID` |
| [UserClassSecurity](UserClassSecurity.md) | `ReportGroupAvailableFieldID` |
