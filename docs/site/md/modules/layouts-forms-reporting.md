# Configuration, Layouts, Forms & Reporting

*In scope for the rebuild*

The tenant-configurable presentation layer that has a business-object footprint: custom lists and their extension parts, custom code fields, questions, and report group metadata. Most of this module's surface (page layouts, data fields, drop downs) lives OUTSIDE these 223 business objects — see docs/admin/005-008.

|  | Count |
|---|---|
| Record types | 6 |
| Fields | 107 |
| Keys in | 2 |
| Keys out | 13 |
| Rules | 133 |

## What was found here

### Conditional display is a real rule engine

**Observed.** Every field, or a whole sub-page section, can carry one rule set, read as a sentence: [Show | Show and Require | Hide] this field when [all | any] of the following rules match. Flat structure — no nesting, no mixed AND/OR.

### Operators depend on the driver's type

**Observed.** Dropdown drivers get is in / is not in. Number drivers get = <> > >= < <=. Boolean drivers get selected / not selected. All three also get is specified / is not specified. 'is any value' is the neutral state that contributes no predicate.

### Rules cross entity boundaries

**Observed.** A Contract layout offers 85 candidate driver fields drawn from four tables: Contract 65, ProjectEntity 9, Facility 7, Location 4. A Contract field can be hidden because of a value on its Location record.

### Text and Date can never drive a rule

**Observed.** Only Dropdown, Number and Boolean fields appear as drivers, even though Contract has many text and date columns. A deliberate constraint that keeps rules explicable and indexable.

### A Form is not a Page

**Observed.** A Page Layout presents a record that already exists. A Form defines a new tenant-authored request type and gets one layout per workflow step. A Custom List is a Form without the workflow.

### Rules are stored as an opaque JSON blob

**Observed.** One json.conditionalFieldsConfig per target. Cheap to write, impossible to query — Lx cannot answer 'which layouts depend on this drop-down?'. Storing predicates as rows instead would give the rebuild a Where-Used answer for free.

### The report catalogue and the field catalogue are one table

**Observed.** Every field-consuming subsystem joins to ReportGroupAvailableField, and the vendor's own schema names the key to it 'Report/Form Field ID' — a single type unifying report field and form field.

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [ReportGroupAvailableField](../entities/ReportGroupAvailableField.md) | `report_group_available_field` | 27 | 4 |
| [CLRExtensionPart](../entities/CLRExtensionPart.md) | `c_l_r_extension_part` | 24 | 0 |
| [ClientListRow](../entities/ClientListRow.md) | `client_list_row` | 24 | 0 |
| [Question](../entities/Question.md) | `question` | 14 | 0 |
| [CustomCodeField](../entities/CustomCodeField.md) | `custom_code_field` | 13 | 1 |
| [ReportGroupData](../entities/ReportGroupData.md) | `report_group_data` | 5 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [LAY-R-001](../rules/LAY-R-001.md) | … LAY-R-018 — from live capture | Two of those bear repeating here because everything below assumes them: - `LAY-R-011` — a conditional rule set declares exactly one action: `SHOW`, `SHOW_AND_REQUIRE` or `HIDE`. Visibility and require | Derived |
| [LAY-R-002](../rules/LAY-R-002.md) | The reconciliation, stated as rules | A Page Layout presents a platform-defined entity. It does not define fields; | Derived |
| [LAY-R-003](../rules/LAY-R-003.md) | The reconciliation, stated as rules | A Form is a tenant-defined record type registered in the code-table registry (`TableType=2035`), extended with its own field schema and one layout per workflow step. | Derived |
| [LAY-R-004](../rules/LAY-R-004.md) | The reconciliation, stated as rules | A Custom List is a tenant-defined record type with its own field schema and a layout, but no workflow. | Derived |
| [LAY-R-005](../rules/LAY-R-005.md) | The reconciliation, stated as rules | A Form type declares attachability as a boolean per entity kind (Portfolio, RE Contract, Facility, …). A request may only be raised against an entity whose flag is set. | Derived |
| [LAY-R-006](../rules/LAY-R-006.md) | The reconciliation, stated as rules | A Form type declares a sequence prefix and whether numbering is global. | Derived |
| [LAY-R-007](../rules/LAY-R-007.md) | The reconciliation, stated as rules | Every Form type has exactly one Work Flow, identified by the same name. | Derived |
| [LAY-R-008](../rules/LAY-R-008.md) | The reconciliation, stated as rules | A Work Flow is an ordered sequence of steps, each of type `Form` or `Task`. A `Form` step binds one of the form type's layouts. | Derived |
| [LAY-R-009](../rules/LAY-R-009.md) | The reconciliation, stated as rules | A step resolves its approver by `Approval Level`: `Member`, `Job Title`, or `Ad Hoc`. | Derived |
| [LAY-R-010](../rules/LAY-R-010.md) | Rules for the ASG Edge+ rule engine | A conditional rule set attaches to exactly one target, identified by a stable key. A target is either a single field or an entire sub-page section. | Derived |
| [LAY-R-011](../rules/LAY-R-011.md) | Rules for the ASG Edge+ rule engine | A rule set declares exactly one action: `SHOW`, `SHOW_AND_REQUIRE`, or `HIDE`. | Derived |
| [LAY-R-012](../rules/LAY-R-012.md) | Rules for the ASG Edge+ rule engine | A rule set declares exactly one quantifier over its predicates: `ALL` or `ANY`. Nesting is not supported. | Derived |
| [LAY-R-013](../rules/LAY-R-013.md) | Rules for the ASG Edge+ rule engine | A predicate is a triple `(driverField, operator, value)`. Operators are constrained by the driver field's type: Dropdown → `IN`, `NOT_IN`, `IS_SPECIFIED`, `IS_NOT_SPECIFIED`; | Derived |
| [LAY-R-014](../rules/LAY-R-014.md) | Rules for the ASG Edge+ rule engine | `is any value` is the neutral state and contributes no predicate. | Derived |
| [LAY-R-015](../rules/LAY-R-015.md) | Rules for the ASG Edge+ rule engine | Candidate driver fields are: the layout's primary table, plus every table reachable by a many-to-one FK from it, plus `ProjectEntity`. | Derived |
| [LAY-R-016](../rules/LAY-R-016.md) | Rules for the ASG Edge+ rule engine | Only Dropdown, Number and Boolean fields may be drivers. Text and Date fields may not. | Derived |
| [LAY-R-017](../rules/LAY-R-017.md) | Rules for the ASG Edge+ rule engine | Rule sets apply to the edit layout. List layouts carry a separate, independent rule surface. | Derived |
| [LAY-R-018](../rules/LAY-R-018.md) | Rules for the ASG Edge+ rule engine | `SHOW_AND_REQUIRE` makes the target mandatory for validation purposes only while its predicates match. (Inferred — the runtime behaviour was not observed, only the configuration option.) | Inferred |
| [LAY-R-100](../rules/LAY-R-100.md) | … — from the schema | Each carries an evidence label. Observed = seen in a capture or source artefact. | Observed |
| [LAY-R-101](../rules/LAY-R-101.md) | A. Record identity and typing | Summary Pages, Sub-pages, List Layouts, Forms, Wizards, Map Popups, Reports and Dashboard tiles are all rows of one table, `PageLayout`. They are distinguished by discriminator columns, not by separat | Observed |
| [LAY-R-102](../rules/LAY-R-102.md) | A. Record identity and typing | Every layout has exactly one required `PageLayoutType`, one required `OutputType`, and one required `PageLayoutName`. · Observed · `all-fields.csv` | Observed |
| [LAY-R-103](../rules/LAY-R-103.md) | A. Record identity and typing | A layout declares a single Primary Table (`PrimaryCodeSQLTableID`). Every field it may place is either a field of that table or a field reachable from it by a declared FK ("Related Fields"). | Observed |
| [LAY-R-104](../rules/LAY-R-104.md) | A. Record identity and typing | A layout may be Global (platform-shipped, rendered with a `[Global Layout]` suffix) or Firm (tenant-authored). A tenant may keep the Global default per entity type or override it; | Observed |
| [LAY-R-105](../rules/LAY-R-105.md) | A. Record identity and typing | `AllowEdit = No` makes a layout read-only. `AllowUserCreate` separately controls whether end users may create records through it. | Observed |
| [LAY-R-106](../rules/LAY-R-106.md) | A. Record identity and typing | A layout with a non-blank `URL` bypasses its own field configuration entirely and redirects to that system page. Vendor help text: "Leave blank for standard functionality. | Observed |
| [LAY-R-107](../rules/LAY-R-107.md) | A. Record identity and typing | A layout can be scoped to specific Portfolios/Capital Programs via a required multi-select, defaulting to All Portfolios/Capital Programs — the same control used for dropdown values. · Observed (UI); | Observed |
| [LAY-R-110](../rules/LAY-R-110.md) | B. Composition | A Summary Page is composed of Sub-pages, not authored monolithically. Each visible section corresponds to an independently-managed Sub-page layout. | Observed |
| [LAY-R-111](../rules/LAY-R-111.md) | B. Composition | The inclusion mechanism is a `PageLayoutField` row whose `SubPageLayoutID` points at the child layout, positioned by the same coordinates as a field. · Inferred (high) · `all-fields.csv` | Inferred |
| [LAY-R-112](../rules/LAY-R-112.md) | B. Composition | A section's title is supplied by the parent at the point of inclusion (`PageLayoutField.DisplayLabel`), not by the sub-page. A sub-page opened on its own renders with no title bar. | Observed |
| [LAY-R-113](../rules/LAY-R-113.md) | B. Composition | A `PageLayoutField` row need not carry a field at all: it can be an embedded sub-layout (`SubPageLayoutID`) or literal copy (`StaticText`). · Observed (columns) · `all-fields.csv` | Observed |
| [LAY-R-114](../rules/LAY-R-114.md) | B. Composition | A multi-step creation Wizard is a sequence of Sub-page layouts (`ASG Contract Wizard`, `Wizard Step 2`…`Step 5`), bound as an entity's creation flow via a Setup Page assignment. · Observed · 008 | Observed |
| [LAY-R-115](../rules/LAY-R-115.md) | B. Composition | Layout ordering among siblings uses a previous-pointer chain (`PreviousPageLayoutID`, `PreviousID`) with a materialised `ComputedSequenceNumber`, not a plain integer sort key. · Observed (columns) · ` | Observed |
| [LAY-R-116](../rules/LAY-R-116.md) | B. Composition | Layouts host placeable, reorderable business-action buttons (Approve Payments, Generate Rent, Extend Contracts, Alternate Rent Wizard, Copy Transaction, …) alongside fields, in the same grid with the  | Observed |
| [LAY-R-117](../rules/LAY-R-117.md) | B. Composition | [BLOCKED] Action buttons are presumed to be `PageLayoutField` rows with no `ReportGroupAvailableFieldID`, identified by `DisplayOption`/`JSONConfigText`. No column declares a button. | Inferred |
| [LAY-R-120](../rules/LAY-R-120.md) | C. The Edit / List duality | A single `PageLayoutID` can carry both a detail Edit Layout and a grid List Layout, as two orthogonal facets of one record. Proven on `ASG Contract Payments` (96214, `PaymentTransaction`). | Observed |
| [LAY-R-121](../rules/LAY-R-121.md) | C. The Edit / List duality | The facet a placement belongs to is flagged by `PageLayoutField.IsInEditLayout`, and each facet has its own coordinate set — `EditRow/ColumnPosition`+`EditFieldWidth/Height` vs `ViewRow/ColumnPosition | Inferred |
| [LAY-R-122](../rules/LAY-R-122.md) | C. The Edit / List duality | A top-level parent entity with no natural "list of many inside one" view renders "List Layout not applicable for current layout type." This is a property of the target table, not a general one-facet-o | Observed |
| [LAY-R-123](../rules/LAY-R-123.md) | C. The Edit / List duality | A field can be searchable but hidden from the grid — a distinct third visibility state, rendered in green as `(Searchable, Hidden in grid)`, present in both the Edit and List facets. · Observed · 008 | Observed |
| [LAY-R-124](../rules/LAY-R-124.md) | C. The Edit / List duality | A layout carries a separate mobile ordering (`MobileRowPosition`), i.e. responsive layout is configured, not derived. | Derived |
| [LAY-R-125](../rules/LAY-R-125.md) | C. The Edit / List duality | Per-placement CSS is configurable independently for label and value (`LabelCSSStyle`, `ValueCSSStyle`). · Observed (columns) · `all-fields.csv` | Observed |
| [LAY-R-130](../rules/LAY-R-130.md) | D. Conditional field display — where the rules are stored | A conditional rule set is posted as a single JSON document per target — hidden form field `json.conditionalFieldsConfig` on form `ConditionFilter` — not as normalised rows. · Observed · conditional-fi | Observed |
| [LAY-R-131](../rules/LAY-R-131.md) | D. Conditional field display — where the rules are stored | Superseded. An earlier reading of this corpus put conditional rules in `PageLayoutFilter` with `IsListFilter = false`. | Derived |
| [LAY-R-132](../rules/LAY-R-132.md) | D. Conditional field display — where the rules are stored | [BLOCKED] The destination column for that JSON is not observed. `PageLayoutField.DisplayOptionJSON` (optional per-placement textarea) is the strongest candidate: a `subPage_<id>` target is a `PageLayo | Observed |
| [LAY-R-133](../rules/LAY-R-133.md) | D. Conditional field display — where the rules are stored | Conditional rules are invisible to the data API. No type matching `condition`, `rule`, `criteria`, `visib`, `depend`, `trigger`, `expression` or `predicate` exists in the 490-type GraphQL schema, and  | Derived |
| [LAY-R-134](../rules/LAY-R-134.md) | D. Conditional field display — where the rules are stored | Because storage is an opaque blob, Lx cannot answer "which layouts depend on this field or this dropdown value". Any Where-Used capability requires normalised predicate rows. | Derived |
| [LAY-R-140](../rules/LAY-R-140.md) | D2. `PageLayoutFilter` — the row-filter and pivot table | `PageLayoutFilter` holds row filters, not field-visibility rules: `ReportGroupAvailableFieldID` (required) + `CriteriaType1`/`CriteriaValue1` + `CriteriaType2`/`CriteriaValue2`, discriminated by a req | Observed |
| [LAY-R-141](../rules/LAY-R-141.md) | D2. `PageLayoutFilter` — the row-filter and pivot table | The same row also carries grouping and totalling: `RowOrderBy`, `ColumnOrderBy`, `ShowLabel`, `ShowSubtotal`. Lx list/report output is pivot-shaped, not flat-list-shaped. | Observed |
| [LAY-R-142](../rules/LAY-R-142.md) | D2. `PageLayoutFilter` — the row-filter and pivot table | Two `CriteriaType`/`CriteriaValue` pairs on one row express a two-clause predicate on one field — a `between`. Multiple rows chain through `ExtendedGroupFilterID` (self-FK); | Inferred |
| [LAY-R-143](../rules/LAY-R-143.md) | D2. `PageLayoutFilter` — the row-filter and pivot table | [BLOCKED] `IsListFilter` and the layout builder's `showInList=1` parameter (passed when `layoutMode` is `list` or `budget`) describe the same edit-vs-list split from two directions. Whether they are t | Derived |
| [LAY-R-144](../rules/LAY-R-144.md) | D2. `PageLayoutFilter` — the row-filter and pivot table | A filter may target a field reached through a relation, disambiguated by `FieldContext` — the same column `PageLayoutField` carries. · Inferred (moderate) · `all-fields.csv`; | Inferred |
| [LAY-R-150](../rules/LAY-R-150.md) | E. Fields, required-ness and read-only-ness | Placeable fields come from the shared field registry (`ReportGroupAvailableField`), scoped to the layout's Primary Table, presented as the Available Fields tree. · Observed · 008 | Observed |
| [LAY-R-151](../rules/LAY-R-151.md) | E. Fields, required-ness and read-only-ness | Related-table fields are placeable through Related Fields, which for a true many-to-one FK target exposes that table's complete native catalog, not a curated subset. · Observed · 009 | Observed |
| [LAY-R-152](../rules/LAY-R-152.md) | E. Fields, required-ness and read-only-ness | The relationship is asymmetric by cardinality: from the many side, the one side appears under Related Fields; from the one side, the many side appears as an embedded `(One to Many List)` List Layout,  | Observed |
| [LAY-R-153](../rules/LAY-R-153.md) | E. Fields, required-ness and read-only-ness | A layout's Available Fields tree exposes each table's Custom Lists as a nested branch, drilling into that list's own fields. A custom list appears only under the table it belongs to. | Observed |
| [LAY-R-154](../rules/LAY-R-154.md) | E. Fields, required-ness and read-only-ness | Required fields render in red with a trailing `*`. · Observed · 008 | Observed |
| [LAY-R-155](../rules/LAY-R-155.md) | E. Fields, required-ness and read-only-ness | Required-ness is intended to be set from the layout editor (Manage Page Layouts) or from Manage Forms, not from the field catalog — where the flag "defaults to No and is read-only". · Observed (vendor | Observed |
| [LAY-R-156](../rules/LAY-R-156.md) | E. Fields, required-ness and read-only-ness | [BLOCKED] No `IsRequired`/`IsReadOnly` column exists on `PageLayoutField`, so LAY-R-155's storage is unknown — either packed into `DisplayOption1/2/JSON`, or written back to `RGAF.IsRequired`. Check:  | Derived |
| [LAY-R-157](../rules/LAY-R-157.md) | E. Fields, required-ness and read-only-ness | Some fields render as system-computed read-only placeholders (`xxxxx` on `Check Amount`, `Check Date`, `Check Number`, `AP Export Base#`) — populated by downstream processes, not by the form. · Observ | Observed |
| [LAY-R-158](../rules/LAY-R-158.md) | E. Fields, required-ness and read-only-ness | Every registry field carries a Value Javascript hook, so a field can have scripted default/computed/visibility behaviour independent of the layout's declarative conditions. · Observed · 005 | Observed |
| [LAY-R-160](../rules/LAY-R-160.md) | F. Forms | A Form Type is a `CodeIssueType` row. Lx's schema names the dropdown that selects one `Dropdown (Form Type)`. | Observed |
| [LAY-R-161](../rules/LAY-R-161.md) | F. Forms | Manage Forms administers a firm code table (`FirmCodeEdit.jsp?TableType=2035`), i.e. the catalog of Form Types — not a layout builder. | Observed |
| [LAY-R-162](../rules/LAY-R-162.md) | F. Forms | A Form Type declares which entity types it may be raised against, via eleven `IsValidFor<Entity>` flags (Portfolio, CapProgram, CapProject, OpenProject, PotentialProject, Prototype, Parcel, Facility,  | Observed |
| [LAY-R-163](../rules/LAY-R-163.md) | F. Forms | A Form Type carries its own numbering (`SequencePrefix`, `IsSequencePerFirm`) and lifecycle behaviour (`AllowReply`, `AutoClose`, `IsWorkFlow`). · Observed · `_lucernex_objects_summary.txt` | Observed |
| [LAY-R-164](../rules/LAY-R-164.md) | F. Forms | A form instance is an `Issue` record. `Issue.LastPageLayoutID` records "the name of the last form layout used to update the issue" — singular, so it is depth-1 history, not a per-step audit trail. | Observed |
| [LAY-R-165](../rules/LAY-R-165.md) | F. Forms | Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayou | Observed |
| [LAY-R-166](../rules/LAY-R-166.md) | F. Forms | The field registry's top-level group `Specialized Forms` is the only group applicable to Issue and not to Portfolio or Entity; its member entities are the Issue-derived transactional forms (Bid Packag | Derived |
| [LAY-R-170](../rules/LAY-R-170.md) | G. Custom Lists | A Custom List is a tenant-authored mini record type: its own field schema plus its own layout. It is not a picklist. | Observed |
| [LAY-R-171](../rules/LAY-R-171.md) | G. Custom Lists | The list is a `ReportGroupData` node; its fields are `ReportGroupAvailableField` leaves; | Observed |
| [LAY-R-172](../rules/LAY-R-172.md) | G. Custom Lists | Each custom list gets its own field-name namespace derived from its initials (`CRL_*` for Client Request Log, `OpEx*` for Operating Expenses), plus shared system audit fields (`ModifiedByID`, `Modifie | Derived |
| [LAY-R-173](../rules/LAY-R-173.md) | G. Custom Lists | A custom-list field can be typed Drop Down >>, cascading into a Drop Down Type category and then a specific drop-down, binding it to Firm or Client Drop Downs. · Observed · 006, 007 | Observed |
| [LAY-R-174](../rules/LAY-R-174.md) | G. Custom Lists | A custom list has a Type — `Standard` (2634) or `Part` (2635) — sharing machinery with the Parts and Inventory module. · Observed · 006 | Observed |
| [LAY-R-175](../rules/LAY-R-175.md) | G. Custom Lists | Custom Lists are Firm-scoped only; no Global/platform custom list concept was observed. | Observed |
| [LAY-R-180](../rules/LAY-R-180.md) | H. Role binding and assignment | A layout becomes an entity's creation wizard by assignment on Setup Pages, one slot per entity type. · Observed · 008 | Observed |
| [LAY-R-181](../rules/LAY-R-181.md) | H. Role binding and assignment | Setup-page assignment exists at two levels: `Firm` (11 slots, tenant default) and `Program` (18 slots — 11 setup pages + 7 map popups, per Portfolio/Capital Program). Only the Firm level was observed  | Observed |
| [LAY-R-182](../rules/LAY-R-182.md) | H. Role binding and assignment | A setup-page selector lists any layout whose Primary Table matches the target — Summary Pages, Sub-pages and Wizards alike — not only Wizard-type records. · Observed (`ASG Client Request Log` offered  | Observed |
| [LAY-R-183](../rules/LAY-R-183.md) | H. Role binding and assignment | Map Popup Layouts are a third, minimal rendering context, distinct from Summary Page and Wizard. The seven `*MapSetupLayoutID` columns sit on `Program`, not `Firm`, implying portfolio scope. | Observed |
| [LAY-R-184](../rules/LAY-R-184.md) | H. Role binding and assignment | A layout is placed in the navigation menu via a Parent Tab tree selection, materialised as `HierarchyName` (e.g. `Contract : Details : Summary`). | Observed |
| [LAY-R-185](../rules/LAY-R-185.md) | H. Role binding and assignment | A new layout may be seeded from an existing one via "Initialize layout from existing layout", available only on create, not on edit. Whether it is a full clone or a partial template is unknown. | Observed |
| [LAY-R-190](../rules/LAY-R-190.md) | I. Security | Access is granted per user class against a layout, a field, a field group, or a dashboard component — all from one `UserClassSecurity` table with a `CodeSecurityPrivilegeID` and a `SecurityLevelByteVa | Observed |
| [LAY-R-191](../rules/LAY-R-191.md) | I. Security | Granting on a `ReportGroupDataID` (group or subgroup) means field permissions inherit down the registry tree, not per-field only. · Inferred (high) · `all-fields.csv` | Inferred |
| [LAY-R-192](../rules/LAY-R-192.md) | I. Security | Field visibility is therefore decided by three independent systems: security, layout placement, and conditional rules. A stated precedence is required; | Derived |
| [LAY-R-200](../rules/LAY-R-200.md) | J. Change tracking | Layout changes are audited — the admin dashboard exposes a Layout Changes tool (`ShowLayoutChanges.jsp`). Its contents were never opened; | Observed |
| [LAY-R-201](../rules/LAY-R-201.md) | J. Change tracking | Field-level value changes are audited in `AuditColumn`, filed under the registry's group and subgroup — so an audit entry inherits the Data Fields taxonomy. · Derived (11-for-11 column match) · 007; | Derived |
| [LAY-R-202](../rules/LAY-R-202.md) | J. Change tracking | Layout records carry `VersionAdded`/`VersionModified` at the field level (`RGAF`) but not at the layout level — layout versioning, if any, is not visible in the schema. · Observed (absence) · `all-fie | Observed |
| [RPT-R-001](../rules/RPT-R-001.md) | A. What a report is | A report is not a distinct record type. It is a `PageLayout` row with `IsReport = true`. | Derived |
| [RPT-R-002](../rules/RPT-R-002.md) | A. What a report is | A report is run, not viewed: `PageLayout.LastRunBy` and `LastRunDate` record the most recent execution on the definition row itself. · Observed (columns) + Inferred (meaning) · `all-fields.csv` | Observed |
| [RPT-R-003](../rules/RPT-R-003.md) | A. What a report is | A report's output format is a required property of the definition (`OutputType`), not chosen at run time. · Observed · `all-fields.csv` | Observed |
| [RPT-R-004](../rules/RPT-R-004.md) | A. What a report is | A report declares which entities it may be run against (`EntitySelectionFilter`) and which filters the user is offered at run time (`RunModeFilters`). Both required. | Observed |
| [RPT-R-005](../rules/RPT-R-005.md) | A. What a report is | Reports are Global (platform standard, `IsGlobalReport = true`) or tenant/personal. `OwnedByMemberID` gives a report a personal owner. | Observed |
| [RPT-R-006](../rules/RPT-R-006.md) | A. What a report is | A dashboard tile is a `PageLayout` row with `IsDashboardReport = true`, administered by Manage Dashboard Reports (`/en/reports/ManageDashboardModules.jsp`). · Observed (column + route) + Inferred (the | Observed |
| [RPT-R-007](../rules/RPT-R-007.md) | A. What a report is | A report can appear as its own navigation entry (`IsMenuLink`) and can be placed in the menu tree by `HierarchyName`, exactly like a page. · Observed (columns) · `all-fields.csv` | Observed |
| [RPT-R-008](../rules/RPT-R-008.md) | A. What a report is | A report can be redirected wholesale to a system URL (`PageLayout.URL`), discarding its configured columns. Same escape hatch as any layout (LAY-R-106). | Observed |
| [RPT-R-009](../rules/RPT-R-009.md) | A. What a report is | A layout can host report-triggering action buttons, a distinct button kind labelled "(Run Report Action)" — observed as `Expense Report` and `Check History` on the ASG Contract Payments edit layout. R | Observed |
| [RPT-R-010](../rules/RPT-R-010.md) | B. Report columns and the field registry | Report columns are drawn from the same field registry as forms — `ReportGroupAvailableField`, whose FK type Lx names `Report/Form Field ID`. There is no separate report-field catalog. | Observed |
| [RPT-R-011](../rules/RPT-R-011.md) | B. Report columns and the field registry | A field carries two labels: `DefaultLabel` ("Label") and `UILabel` ("Report Field Label"). A field may therefore present differently on a form than as a report column header. | Observed |
| [RPT-R-012](../rules/RPT-R-012.md) | B. Report columns and the field registry | A report column is a `PageLayoutField` row; grid geometry uses the `View*` coordinate set (`ViewRowPosition`, `ViewColumnPosition`, `ViewFieldWidth`, `ViewFieldHeight`, `HeaderColumnPosition`). | Inferred |
| [RPT-R-013](../rules/RPT-R-013.md) | B. Report columns and the field registry | A column can be searchable but hidden from the grid — a third visibility state distinct from shown and removed. · Observed · 008 | Observed |
| [RPT-R-014](../rules/RPT-R-014.md) | B. Report columns and the field registry | A report may include fields from related tables reached by declared FKs, disambiguated by `FieldContext`. · Observed (Related Fields) + Inferred (the column's role) · 009; | Observed |
| [RPT-R-015](../rules/RPT-R-015.md) | B. Report columns and the field registry | A report may include fields from a tenant's Custom Lists, which are ordinary registry leaves under the owning table's `Custom Lists` subgroup. · Observed · 008 | Observed |
| [RPT-R-016](../rules/RPT-R-016.md) | B. Report columns and the field registry | Every registry field carries a Value Javascript hook, so a report column's value can be scripted rather than read. · Observed · 005 | Observed |
| [RPT-R-017](../rules/RPT-R-017.md) | B. Report columns and the field registry | The registry marks computed fields with `IsFunctional` and carries a `Definition` textarea for the computation. `View Object Model` exposes a `Functional Field?` column and `Math`/`Computed` filter ra | Observed |
| [RPT-R-020](../rules/RPT-R-020.md) | C. Filters, grouping and totals | Report and list filters are `PageLayoutFilter` rows: `ReportGroupAvailableFieldID` (required) + two `CriteriaType`/`CriteriaValue` pairs, discriminated by a required `IsListFilter` boolean. This is no | Observed |
| [RPT-R-021](../rules/RPT-R-021.md) | C. Filters, grouping and totals | A filter row names one field (`ReportGroupAvailableFieldID`, required) and carries two operator/value pairs — a two-clause predicate on that field, e.g. a `between`. | Observed |
| [RPT-R-022](../rules/RPT-R-022.md) | C. Filters, grouping and totals | Multiple filter rows chain through `ExtendedGroupFilterID` (self-FK). Whether the chain is AND, OR, or an explicit group is undetermined. | Observed |
| [RPT-R-023](../rules/RPT-R-023.md) | C. Filters, grouping and totals | The same row that filters also groups: `RowOrderBy` and `ColumnOrderBy` give a field a position on each axis. Reporting in Lx is pivot-shaped, not flat-list-shaped. | Observed |
| [RPT-R-024](../rules/RPT-R-024.md) | C. Filters, grouping and totals | `ShowSubtotal` emits a subtotal at a grouping break; `ShowLabel` renders the grouping field's label there. | Observed |
| [RPT-R-025](../rules/RPT-R-025.md) | C. Filters, grouping and totals | Report currency is a property of the definition (`PageLayout.CodeCurrencyTypeID`), not of the run. · Observed (column) · `all-fields.csv` | Observed |
| [RPT-R-026](../rules/RPT-R-026.md) | C. Filters, grouping and totals | [BLOCKED] The `CriteriaType` operator codebook is a small integer enum whose members are unobservable offline. Check: distinct `CriteriaType1`/`CriteriaType2` values via GraphQL Explorer. | Derived |
| [RPT-R-030](../rules/RPT-R-030.md) | D. Purpose-built report types | A Comparison Report is a first-class record (`ComparisonReport`) that still delegates its rendering to a `PageLayout` (`PageLayoutID`, required). Even the bespoke report types run on the generic layou | Observed |
| [RPT-R-031](../rules/RPT-R-031.md) | D. Purpose-built report types | A Comparison Report's cells live in `ComparisonItem`, one row per scenario column, carrying `ScenarioName`, `ScenarioDate`, `ExpenseGroup`, `Assumptions`, `ComputedValue` and a serialised `XmlData` pa | Observed |
| [RPT-R-032](../rules/RPT-R-032.md) | D. Purpose-built report types | Demographic Reports are the only report family with an explicit asynchronous execution record: `DemographicResults` carries `TimeInitiated`, `TimeFinished`, a status code, a third-party vendor code, a | Observed |
| [RPT-R-033](../rules/RPT-R-033.md) | D. Purpose-built report types | A Demographic Report's scope is a trade area defined by radius or drive time (`DemographicStudyArea.AreaRadius`, `.AreaDriveTimeInMinutes`, `.CodeRadiusUnitID`) — a site-selection feature, not a lease | Observed |
| [RPT-R-036](../rules/RPT-R-036.md) | D. Purpose-built report types | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAc | Derived |
| [RPT-R-040](../rules/RPT-R-040.md) | E. Audit reporting | Field-level change audit is stored in `AuditColumn`, with `EntityName`, `CodeSQLTableID`, `ObjectID`, `FieldName`, `AuditAction`, `OldValue`, `NewValue` and the actor/timestamp. · Observed · `all-fiel | Observed |
| [RPT-R-041](../rules/RPT-R-041.md) | E. Audit reporting | Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy a | Observed |
| [RPT-R-042](../rules/RPT-R-042.md) | E. Audit reporting | Login, lockout and impersonation events are audited separately in `MemberAudit`, with `SrcIP` and `UserAgent`. · Observed · `_lucernex_objects_summary.txt` | Observed |
| [RPT-R-043](../rules/RPT-R-043.md) | E. Audit reporting | The Audit Log dialog is a generic viewer over `AuditColumn`, reachable from an individual record's editor — not only from a central Audit Reports screen. · Derived · 007 | Derived |
| [RPT-R-050](../rules/RPT-R-050.md) | F. Security | Report access is granted per user class through `UserClassSecurity.PageLayoutID`, alongside grants on fields (`ReportGroupAvailableFieldID`), field groups (`ReportGroupDataID`) and dashboard component | Observed |
| [RPT-R-051](../rules/RPT-R-051.md) | F. Security | Dashboard tiles are secured by title string (`UserClassSecurity.DashboardComponentTitle`), not by record id. Renaming a tile therefore breaks its grants. | Observed |
| [RPT-R-052](../rules/RPT-R-052.md) | F. Security | Granting on a registry group node means report-field permissions inherit down the catalog tree, not per-field only. · Inferred (high) · `all-fields.csv` | Inferred |
| [RPT-R-053](../rules/RPT-R-053.md) | F. Security | [BLOCKED] Whether Portfolio/Capital-Program scoping filters report rows at the query level or only hides values in the UI is unresolved — the same question 007 raises for dropdown values. Check: run a | Derived |
| [RPT-R-060](../rules/RPT-R-060.md) | G. Bulk data movement | The field catalog itself is exportable and importable as a spreadsheet, scope-aware: `DocumentDownload?type=RGAFSpreadsheet&readOnly=true&isGlobal={true\ · false}`. · Observed · 005 | Observed |
| [RPT-R-061](../rules/RPT-R-061.md) | G. Bulk data movement | An exported catalog spreadsheet is single-use: "Once a spreadsheet is imported the same spreadsheet cannot be used again. You would have to create a new spreadsheet using 'Export Data Fields' button." | Observed |
| [RPT-R-062](../rules/RPT-R-062.md) | G. Bulk data movement | The bulk-change instruction block is shown in Firm scope but not in Global scope. Reason unknown. | Observed |
| [RPT-R-063](../rules/RPT-R-063.md) | G. Bulk data movement | ASG requires a report-to-import round trip (export a report to Excel, edit, re-import to update records), priority Critical. Lx's catalog export/import is field metadata only; | Observed |
| [RPT-R-070](../rules/RPT-R-070.md) | H. Requirements ASG has already stated | Restrict edit access to standard reports (e.g. ASC 842) to prevent breakage, while allowing runtime filters to view specific data · Blocker · 242 | Derived |
| [RPT-R-071](../rules/RPT-R-071.md) | H. Requirements ASG has already stated | "Save As" personal reports — a user copy that does not affect the global standard · Critical · 243 | Derived |
| [RPT-R-072](../rules/RPT-R-072.md) | H. Requirements ASG has already stated | Report-to-import workflow — export to Excel, modify, re-import to update the system · Critical · 244 | Derived |
| [RPT-R-073](../rules/RPT-R-073.md) | H. Requirements ASG has already stated | Scheduled & external delivery — email to recipients including non-users, or encrypted SFTP · Major · 245 | Derived |
| [RPT-R-074](../rules/RPT-R-074.md) | H. Requirements ASG has already stated | Multi-tenancy / global management — a Global Admin view; today an admin logs into 21 instances separately · Critical · 246, 248 | Derived |
| [RPT-R-075](../rules/RPT-R-075.md) | H. Requirements ASG has already stated | Job log visibility — an at-a-glance status board for scheduled jobs, not a click-away list; blank reports are being sent unnoticed · — · 247 | Derived |
| [RPT-R-076](../rules/RPT-R-076.md) | H. Requirements ASG has already stated | Readable audit logs — "Audit tools are just raw links. User has to go look for logs manually in the table and infer on its own." ASG explicitly does not use Generate Enterprise Report File · — · 241 | Derived |
| [RPT-R-077](../rules/RPT-R-077.md) | H. Requirements ASG has already stated | Bulk action confirmation — preview changes before executing a bulk import, with rollback visibility · Critical · 250 | Derived |
