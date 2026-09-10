# The shared field registry — is the report field catalog the same thing as the data field catalog?

**Stated up front: yes, and it is not a hypothesis any more.** Lucernex has exactly one field
registry, the table `ReportGroupAvailableField` (RGAF), and the vendor's own schema type system
names the foreign key to it **`Report/Form Field ID`** — a single type whose name unifies
"report field" and "form field". Every field-consuming subsystem in the product — the Manage Data
Fields screen, the Page Layout builder, list/report column definitions, report and conditional
filters, Custom Lists, per-user-class field security, and the field-level audit trail — joins to
that one table. Confidence: **very high** for the identity claim; the residual uncertainty is
about which *edges* exist, not about whether the registry is shared.

## The claim, and the five independent pieces of evidence

| # | Evidence | Source | Label |
|---|---|---|---|
| 1 | The Manage **Data** Fields admin screen's route is `ReportGroupAvailableFieldEdit.jsp` and its browser title is literally "Manage **Report Group Available Fields**" | [005](../../admin/005-manage-data-fields.md#identification) | Observed |
| 2 | The FK type is named **`Report/Form Field ID`** in Lucernex's own declared schema | `_lucernex_objects_summary.txt`, `ClientListRow.ReportGroupAvailableFieldID(Report/Form Field ID)` | Observed |
| 3 | RGAF's own 27 columns are exactly the Manage Data Fields grid columns — `FormFieldType`, `IsRequired`, `IsReadOnly`, `DefaultValue`, `CodeSQLTableID`, `DefaultLabel` — **plus** `UILabel`, whose display label in the catalog is "**Report Field Label**" | `docs/data-fields/all-fields.csv`, rows `ReportGroupAvailableField,*` | Observed |
| 4 | `PageLayoutField.ReportGroupAvailableFieldID` and `PageLayoutFilter.ReportGroupAvailableFieldID` are both typed `sTYPE_REPORT_GROUP_AVAILABLE_FIELD` — a placed *layout* field and a *filter* clause both point at the same registry row | `docs/data-fields/all-fields.csv` | Observed |
| 5 | The Custom Lists field grid's create button is labelled "**Add Report/Form Field...**" and its editor dialog is titled "**Edit Report/Form Field**" | [006](../../admin/006-manage-custom-lists.md#field-schema--edit-fields-client-request-log-example) | Observed |
| 6 | The GraphQL schema declares **`HasUDFs`** as a generic capability interface with a uniform `udfs { name type value }` projection, declares **`iCodeTable`** as a single interface over every drop-down/code table, and reduces the catalog's 448 `sTYPE_*`/`sCODE_*` codes to a **10-value canonical type system** (`BOOLEAN COMPUTED DATE DATETIME FK FLOAT INTEGER MONEY PERCENTAGE STRING`) — one registry, one type system, read the same way everywhere | [graphql-api.md](../../data-model/graphql-api.md) | Observed |

Evidence 2 and 5 are the decisive pair: they are the *vendor's* words, in two independent places
(the schema type table and the admin UI), and both use the compound noun "Report/Form Field".
Lucernex does not have a report field catalog and a form field catalog. It has one catalog whose
rows are called Report/Form Fields.

## The registry's shape

Two tables, one tree, one leaf type.

| Table | Role | Key columns | Fields |
|---|---|---|---:|
| `ReportGroupData` (RGD) | The **grouping tree**. Self-referencing via `ParentReportGroupDataID`; `FirmID` makes a node tenant-owned | `ReportGroupDataName`, `ParentReportGroupDataID`, `FirmID` | 5 |
| `ReportGroupAvailableField` (RGAF) | The **leaf field definition** | see below | 27 |

`ReportGroupData` being self-referencing is the schema-level explanation for the three-level
group → subgroup → leaf hierarchy measured in [005](../../admin/005-manage-data-fields.md#hierarchy-model)
(24 top-level groups, 320 subgroups, 5,953 Global + 205 Firm leaves). RGAF carries **two** RGD
FKs — `ReportGroupDataID` (required, the owning subgroup) and `ParentReportGroupDataID` (optional,
the top-level group) — i.e. the leaf denormalises its full path. **Derived** from the column list.
This also explains why the Firm-scope screen renders the whole 320-subgroup scaffold while
containing only 205 leaves ([005](../../admin/005-manage-data-fields.md) open question 5): the
scaffold is Global RGD rows, and Firm RGAF leaves hang off them.

### RGAF's 27 columns, grouped by purpose

| Purpose | Columns |
|---|---|
| **Identity / naming** | `AccessorName` (internal field name; grid column "Field Name"), `ScriptName`, `ApiTableName`, `FieldText` |
| **Presentation** | `DefaultLabel` (required; grid column "Label"), `UILabel` (grid column "**Report Field Label**") |
| **Typing** | `FormFieldType` (typed `sTYPE_ALL_FORMFIELDS`), `DropdownTableName`, `MaxLength` |
| **Behaviour flags** | `IsRequired`, `IsReadOnly`, `IsFunctional`, `IsClientExtensionField` (grid column "**Is UDF Field?**") |
| **Binding to a business object** | `CodeSQLTableID` (required; grid column "Table Name"), `TableName` (grid column "Table Detail") |
| **Placement in the tree** | `ReportGroupDataID` (required), `ParentReportGroupDataID`, `HierarchyName` |
| **Scope** | `IsGlobal`, `FirmID` |
| **Documentation** | `Definition`, `GlobalDefinition` |
| **Value** | `DefaultValue` |
| **Lifecycle** | `CreatedDate`, `ModifiedDate`, `VersionAdded`, `VersionModified` |

Two columns deserve their own note.

- **`UILabel` is captioned "Report Field Label"** while `DefaultLabel` is captioned just "Label".
  That is a *two-label* design: one name for the field on a form, a second name for the same field
  when it appears as a report/list column header. This is the clearest single artefact of the
  registry having grown outward from the reporting side. **Observed** in `all-fields.csv`; the
  *semantics* (which surface uses which label) is **Inferred**.
- **`IsClientExtensionField` is captioned "Is UDF Field?"** — user-defined field. This is the flag
  distinguishing a platform field from a tenant-authored extension, and it is the schema
  counterpart of the `Firm_` prefix convention measured in
  [005](../../admin/005-manage-data-fields.md#naming-pattern) (202 of 205 Firm leaves prefixed
  `Firm_`). Its API counterpart is the declared `HasUDFs` interface. **Observed** column; the
  correspondence to the prefix is **Inferred**.
- **`FormFieldType` (typed `sTYPE_ALL_FORMFIELDS`) is a presentation code, not the real type.**
  The GraphQL schema collapses all 448 `sTYPE_*`/`sCODE_*` codes onto a canonical 10-value
  `FieldType` enum, in which **`COMPUTED` and `FK` are first-class members**
  ([graphql-api.md](../../data-model/graphql-api.md), **Observed**). Two consequences for ASG
  Edge+: the registry needs *both* a canonical type and a presentation type per field, and the
  platform's own type system already distinguishes engine-calculated values from user input —
  which is exactly what a rule engine needs and what `RGAF.IsFunctional` + `RGAF.Definition`
  express on the catalog side.

## The consumers — six of them, all joining to the same registry

| Consumer | Join | Source | Label |
|---|---|---|---|
| **Manage Data Fields** (the catalog editor itself) | *is* RGAF/RGD | [005](../../admin/005-manage-data-fields.md) | Observed |
| **Page Layouts** — a field placed on a form or as a list column | `PageLayoutField.ReportGroupAvailableFieldID` | `all-fields.csv` | Observed |
| **Filters / conditions** — report filters, list filters, conditional-field rules | `PageLayoutFilter.ReportGroupAvailableFieldID` (**required**) | `all-fields.csv` | Observed |
| **Custom Lists** — rows of a tenant-defined mini-entity | `ClientListRow.ReportGroupAvailableFieldID`, type `Report/Form Field ID` | `_lucernex_objects_summary.txt` | Observed |
| **Field-level security** — per user class | `UserClassSecurity.ReportGroupAvailableFieldID` (+ `ReportGroupDataID`, `RootReportGroupDataID`, `SubReportGroupDataID`) | `all-fields.csv` | Observed |
| **Budget column types** | `BudgetColumnType.ReportGroupAvailableFieldID` | `all-fields.csv`, `_lucernex_objects_summary.txt` | Observed |

And one indirect consumer:

| Consumer | Join | Source | Label |
|---|---|---|---|
| **Audit trail** — every logged field change is filed under the registry's tree | `AuditColumn.GroupID`, `AuditColumn.SubGroupID`, both typed `sTYPE_REPORT_GROUP_DATA` | `all-fields.csv` | Observed |

The audit case is worth spelling out, because it is independently corroborated by a screenshot.
The Audit Log dialog captured in [007](../../admin/007-firm-and-client-drop-downs.md#value-level-editor--scoping-and-audit-log)
has columns *Member Name, Date/Time, Group Name, Sub-Group, Entity, Table, Item ID, Field, Action,
Old Value, New Value*. `AuditColumn` has, in order, `CreatedByID, CreatedDate, GroupID, SubGroupID,
EntityName, CodeSQLTableID, ObjectID, FieldName, AuditAction, OldValue, NewValue` — an **11-for-11
match**. **Derived** (column-by-column comparison of two observed captures). The "Group Name" and
"Sub-Group" columns a user sees in an audit log are the Data Fields catalog's own group and
subgroup names.

## What the registry does *not* hold

| Missing | Consequence |
|---|---|
| No `IsValidForPortfolio` / `IsValidForEntity` / `IsValidForIssue` column on RGAF or RGD | The three "Valid For..." columns rendered by Manage Data Fields ([005](../../admin/005-manage-data-fields.md#named-columns)) are **not** in the exposed object model. They were observed populated only on group rows and empty on leaves — consistent with living on RGD, but RGD exposes only 5 columns. **Open question.** |
| No conditional-display columns | Conditions live on `PageLayoutFilter`, not on the field. See [conditional-fields.md](../layouts-and-forms/conditional-fields.md). |
| No portfolio/capital-program scope column | Value-level portfolio scoping was observed on *dropdown values* ([007](../../admin/007-firm-and-client-drop-downs.md)) and on *layouts* ([008](../../admin/008-manage-page-layouts.md#the-edit-dialog--full-metadata-surface)), never on field definitions. |

There is also a first-party statement that **`IsRequired` on the registry is not authoritative**:

> "The Required? flag defaults to No and is read-only. To make a field required, modify the field
> from the **Manage Page Layouts** section of the System Administrator Dashboard **or the Manage
> Forms page**."
> — `_xlsx_feature_list.txt` line 938, the vendor Definition text for
> `ReportGroupAvailableField.IsRequired`. **Observed.**

Two things follow. First, required-ness is intended to be **per placement**, not per field — the
registry's flag is a default a layout overrides. Second, the vendor names *Manage Page Layouts* and
*Manage Forms* as the two peer surfaces that edit a placed field, which is the strongest textual
evidence that Forms and Page Layouts are the same machinery (see
[forms-vs-pages-vs-layouts.md](../layouts-and-forms/forms-vs-pages-vs-layouts.md)).

This is unresolved against the schema: `PageLayoutField` has **no** `IsRequired` column. Either
required-ness is packed into `DisplayOption1`/`DisplayOption2`/`DisplayOptionJSON`, or the layout
editors write back to `RGAF.IsRequired`. **Open question**, ranked in the [README](README.md).

## Scope: Global vs Firm is a column, not a second table

`RGAF.IsGlobal` (boolean) + `RGAF.FirmID`. The `?isGlobal=true|false` route parameter observed in
[005](../../admin/005-manage-data-fields.md#explicit-scope-links) is a direct filter on that
column. **Derived.** The two scopes are rows in one table sharing one RGD tree — which is exactly
what [005](../../admin/005-manage-data-fields.md#shared-taxonomy-separate-leaf-sets) measured
behaviourally (24/24 groups and 320/320 subgroups shared, 0 leaf paths shared).

`ReportGroupData.FirmID` exists too, so a *group* can also be tenant-owned. That matches the seven
Firm-editable subgroups observed in [005](../../admin/005-manage-data-fields.md#firm-action-signatures)
(`Contract / Common Area Maintenance`, `Contract / Custom Lists`, `Contract / Delivery
Requirements`, `Contract / Ongoing Co Tenancy`, `Contract / Opening Co Tenancy`, `Contract / Real
Estate Taxes`, `Contract / Test`) against the 313 that were add-only.

## Custom Lists are registry rows, not a separate feature

The six Custom Lists inventoried in [006](../../admin/006-manage-custom-lists.md#data-observed--full-list-inventory)
appear in `all-fields.csv` as six Firm-scope RGAF leaves of type `sTYPE_CLIENT_LISTS`:

| Custom List (006) | RGAF leaf (`all-fields.csv`) | Entity | Layout (006) |
|---|---|---|---:|
| Default Log | `Firm_DefaultLog` | `Contract` | 96282 |
| Funds List | `Firm_Funds` | `Contract` | 96269 |
| Operating Expenses | `Firm_OperatingExpenses` | `Contract` | 96270 |
| Reconciliation Log | `Firm_ReconciliationLog` | `Contract` | 96281 |
| Savings Log | `Firm_SavingsLog` | `Contract` | 96280 |
| Client Request Log | `Firm_ClientRequestLog` | `ProjectEntity` | 96279 |

**Observed** on both sides. Six for six, including the odd one out: Client Request Log's Primary
Table was noted in [008](../../admin/008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists)
as `Portfolio` rather than `Contract`, and it is indeed the only one bound to `ProjectEntity` —
Lucernex's generic entity table.

The list's *own fields* are ordinary RGAF rows one level deeper: the `OpEx*`-prefixed leaves seen
under Available Fields → Contract → Custom Lists → Operating Expenses
([008](../../admin/008-manage-page-layouts.md#available-fields-sidebar--the-direct-link-to-data-fields-and-custom-lists))
and the `CRL_*` leaves in the Client Request Log field grid
([006](../../admin/006-manage-custom-lists.md#field-schema--edit-fields-client-request-log-example)).
The list's *layout* is bound the other way round, from the layout: **`PageLayout.ClientListRGDID`,
typed `sTYPE_REPORT_GROUP_DATA`** — a page layout points at the registry group node that defines
the list. **Observed.**

So: a Custom List = one RGD node + its RGAF children + a PageLayout whose `ClientListRGDID` points
back at the node. Nothing about it is a separate subsystem.

Row storage is partly settled. `ClientListRow` (24 exposed columns) carries a polymorphic parent
pointer (`ObjectID` + `CodeSQLTableID` + `ProjectEntityID`), a `ReportGroupAvailableFieldID`, and
five generic `SubValue`…`SubValue5` currency slots plus part/quantity/vendor columns. That reads as
entity-attribute-value, but it cannot on its own hold Client Request Log's seven mixed-type fields,
and [006](../../admin/006-manage-custom-lists.md#field-editor--edit-reportform-field-opened-via-edit-on-complete-date)
observed the script name `ClientListRow.CRL_CompleteDate` — a *dynamic* property per custom field.

The GraphQL schema resolves the shape if not the physical columns: it declares a
**`ClientListRowInterface`** interface — "Custom Lists are rows on a shared generic row type" — and a
separate **`HasUDFs`** interface whose values are selected as `udfs { name type value }`
([graphql-api.md](../../data-model/graphql-api.md), **Observed**). So custom-list and user-defined
field values are read through a generic name/type/value projection, exactly as the shared-registry
model predicts. `HasUDFs` is also the API-side counterpart of `RGAF.IsClientExtensionField`
("Is UDF Field?"). The underlying physical columns remain **not determined** by the offline
artefacts. Flagged as an open question.

## Confidence summary

| Claim | Label | Confidence |
|---|---|---|
| One registry table serves both reporting and form-building | Observed (vendor's own type name `Report/Form Field ID`) | Very high |
| RGD is the group tree, RGAF the leaves, three levels | Derived from column list + [005](../../admin/005-manage-data-fields.md) counts | High |
| Global/Firm is `IsGlobal`+`FirmID` on one table | Derived | High |
| Custom Lists are RGD nodes + RGAF leaves + a PageLayout | Observed (6/6 name match; `ClientListRGDID`) | High |
| Audit entries are filed under the registry tree | Derived (11-for-11 column match) | High |
| `UILabel` is the report-column caption, `DefaultLabel` the form caption | Inferred from captions | Moderate |
| Required-ness is per-placement, overriding the registry default | Vendor text Observed, but no schema column found to hold it | High on intent, low on mechanism |
| Custom-list values are read through a generic name/type/value projection | Observed (`HasUDFs`, `ClientListRowInterface` in the GraphQL schema) | High |
| Custom-list row values are physically stored EAV in `ClientListRow` | Inferred, and partly contradicted by the dynamic script-name evidence | Low |
