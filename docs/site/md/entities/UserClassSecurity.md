# UserClassSecurity

*21 fields · module: Platform & Tenancy · Postgres: `user_class_security`*

A named security role/permission class — dashboard component visibility and group hierarchy, referenced by WorkFlowTemplateStep's 'Assignee User Class List' fields. 20 Global fields under Company Items.

Source: `data-fields/user-class-security.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Fields with a vendor definition | 20 of 21 inventoried |
| Physical tables | `user_class_security` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 5 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in user_class_security

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 20 fields carry a vendor definition

**Observed.** 20 of this record's 21 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-190](../rules/LAY-R-190.md) | Access is granted per user class against a layout, a field, a field group, or a dashboard component — all from one `UserClassSecurity` table with a `CodeSecurityPrivilegeID` and a `SecurityLevelByteValue`. (A fifth subject in the out-of-sco | Observed |
| [RPT-R-050](../rules/RPT-R-050.md) | Report access is granted per user class through `UserClassSecurity.PageLayoutID`, alongside grants on fields (`ReportGroupAvailableFieldID`), field groups (`ReportGroupDataID`) and dashboard components. · Observed · `all-fields.csv` | Observed |
| [RPT-R-051](../rules/RPT-R-051.md) | Dashboard tiles are secured by title string (`UserClassSecurity.DashboardComponentTitle`), not by record id. Renaming a tile therefore breaks its grants. | Observed |
| [PLT-R-006](../rules/PLT-R-006.md) | Both declare the same 21 fields | Derived |
| [PLT-R-007](../rules/PLT-R-007.md) | The grant is scoped to a whole page layout, a single field-registry leaf, a field-registry subtree, or a dashboard component — never more than one kind at a time, and the level (`SecurityLevelByteValue`) is one of `DEFAULT \| NO_ACCESS \| VIE | Observed |

## Fields

### Relationships (foreign keys) (7)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnTypeID` | Budget Column Type | The budget column type that this security setting is for. | Budget Type ID | Global |  | `user_class_security.BudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `DashboardComponentID` |  |  | DashboardComponent ID | — |  | `user_class_security.DashboardComponentID · TEXT` | unresolved |
| `PageLayoutID` | Page Layout | The page layout that this security applies to. | item ID | Global |  | `user_class_security.PageLayoutID · TEXT` | unresolved |
| `ReportGroupAvailableFieldID` | Report Group Available Field | The reporting field that is associated with the object. | Report/Form Field ID | Global |  | `user_class_security.ReportGroupAvailableFieldID · TEXT` | [ReportGroupAvailableField](ReportGroupAvailableField.md) |
| `ReportGroupDataID` | Report Group Data | The Report Group Data ID that is associated with the security object. | item ID | Global |  | `user_class_security.ReportGroupDataID · TEXT` | unresolved |
| `RootReportGroupDataID` | Parent Report Group | The ID of the top-level Report Group. | item ID | Global |  | `user_class_security.RootReportGroupDataID · TEXT` | unresolved |
| `SubReportGroupDataID` | Report Group | The ID of the sub-Report Group of the RGAF field this security is associated with. | item ID | Global |  | `user_class_security.SubReportGroupDataID · TEXT` | unresolved |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SecurityLevelByteValue` |  | The numeric representation of the security setting's security level. | Dropdown | Global |  | `user_class_security.SecurityLevelByteValue · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeSecurityPrivilegeID` | Security Privilege | The action this setting is for. | Dropdown (Security Privilege Code) | Global |  | `user_class_security.CodeSecurityPrivilegeID · TEXT` | Security Privilege Code |
| `CodeUserClassID` | User Class | The user class that the current set of security settings applies to. | Dropdown (User Class) | Global | yes | `user_class_security.CodeUserClassID · TEXT` | User Class |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `UserClassSecurityID` | User Class Security RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `user_class_security.UserClassSecurityID · VARCHAR(64) NOT NULL` |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DashboardComponentTitle` | Dashboard Component Title | The name of the dashboard component that this security setting is for. | Text | Global |  | `user_class_security.DashboardComponentTitle · TEXT` |  |
| `GroupHierarchy` | Name With Full Hierarchy | The full hierarchy of groups this security setting belongs to, including the security type. | Text | Global |  | `user_class_security.GroupHierarchy · TEXT` |  |
| `GroupHierarchyNoPrefix` | Group Hierarchy | The hierarchy of groups this security setting belongs to, not including the security type. | Text | Global |  | `user_class_security.GroupHierarchyNoPrefix · TEXT` |  |
| `ParentGroupName` | Parent Group Name | The name of the parent group of the security object. | Text | Global |  | `user_class_security.ParentGroupName · TEXT` |  |
| `SecurityLevelName` | Security Level | The security level's name. | Text | Global |  | `user_class_security.SecurityLevelName · TEXT` |  |
| `SecurityObjectNameText` | Security Object Name | The name of the item this security is for, such as the RGAF name or the PageLayoutName. | Text | Global |  | `user_class_security.SecurityObjectNameText · TEXT` |  |
| `SecurityType` | Security Type | The type of security: Page, Action, Field, or Budget. | Text | Global |  | `user_class_security.SecurityType · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | User Class Security ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `user_class_security.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `user_class_security.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `user_class_security.ModifiedDate · TEXT` |  |
