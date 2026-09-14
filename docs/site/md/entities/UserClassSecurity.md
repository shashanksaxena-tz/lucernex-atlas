# UserClassSecurity

*21 fields · module: Platform & Tenancy · Postgres: `user_class_security`*

A named security role/permission class — dashboard component visibility and group hierarchy, referenced by WorkFlowTemplateStep's 'Assignee User Class List' fields. 20 Global fields under Company Items.

Source: `data-fields/user-class-security.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 5 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnTypeID` | Budget Column Type | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `DashboardComponentID` |  | DashboardComponent ID | — |  | unresolved |
| `PageLayoutID` | Page Layout | item ID | Global |  | unresolved |
| `ReportGroupAvailableFieldID` | Report Group Available Field | Report/Form Field ID | Global |  | [ReportGroupAvailableField](ReportGroupAvailableField.md) |
| `ReportGroupDataID` | Report Group Data | item ID | Global |  | unresolved |
| `RootReportGroupDataID` | Parent Report Group | item ID | Global |  | unresolved |
| `SubReportGroupDataID` | Report Group | item ID | Global |  | unresolved |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SecurityLevelByteValue` |  | Dropdown | Global |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeSecurityPrivilegeID` | Security Privilege | Dropdown (Security Privilege Code) | Global |  | Security Privilege Code |
| `CodeUserClassID` | User Class | Dropdown (User Class) | Global | yes | User Class |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `UserClassSecurityID` | User Class Security RecID | Number | Global |  |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DashboardComponentTitle` | Dashboard Component Title | Text | Global |  |  |
| `GroupHierarchy` | Name With Full Hierarchy | Text | Global |  |  |
| `GroupHierarchyNoPrefix` | Group Hierarchy | Text | Global |  |  |
| `ParentGroupName` | Parent Group Name | Text | Global |  |  |
| `SecurityLevelName` | Security Level | Text | Global |  |  |
| `SecurityObjectNameText` | Security Object Name | Text | Global |  |  |
| `SecurityType` | Security Type | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | User Class Security ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
