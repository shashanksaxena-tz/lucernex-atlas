# CustomCodeField

*13 fields · module: Configuration, Layouts, Forms & Reporting · Postgres: `custom_code_field`*

Meta-definition of a tenant-created custom code/dropdown field — the schema record behind Manage Custom Lists (see 006).

Source: `data-fields/code-reference-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Fields with a vendor definition | 13 of 13 inventoried |
| Physical tables | `custom_code_field` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in custom_code_field

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 13 fields carry a vendor definition

**Observed.** 13 of this record's 13 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CustomCodeTableID` | Table Name | The ID of the custom drop-down menu. | Custom Drop Down ID | Global | yes | `custom_code_field.CustomCodeTableID · TEXT` | unresolved |
| `ParentCustomCodeFieldID` | Parent Custom Code Field | Select the parent field value you want this value to be associated with from this field. You can have multiple child values associated with the same parent value. | Custom Field ID | Global |  | `custom_code_field.ParentCustomCodeFieldID · TEXT` | [CustomCodeField](CustomCodeField.md) |
| `ParentCustomCodeTableID` | Parent Custom Code Table | If you would like this drop-down menu to hold values dependent upon the values of another field, select the parent field from this field. | Custom Drop Down ID | Global |  | `custom_code_field.ParentCustomCodeTableID · TEXT` | unresolved |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CustomCodeFieldID` | Custom Code Field RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `custom_code_field.CustomCodeFieldID · VARCHAR(64) NOT NULL` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` |  | This field indicates whether a field is active or inactive. When a field option is deactivated, it no longer appears as selectable in the field to the end-user. Important! If you deactivate a parent field option that is inked to a child field option such as the relationship demonstrated between an expense group and an expense type the child field option will also be deactivated. | Boolean | Global |  | `custom_code_field.Inactive · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CustomCodeFieldName` | Field Name | Enter a name for the field value in this field. | Text | Global | yes | `custom_code_field.CustomCodeFieldName · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `custom_code_field.Description · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Custom Code Field ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `custom_code_field.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `custom_code_field.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `custom_code_field.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `custom_code_field.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `custom_code_field.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `custom_code_field.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [CustomCodeField](CustomCodeField.md) | `ParentCustomCodeFieldID` |
