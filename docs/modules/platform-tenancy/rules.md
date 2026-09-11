# Platform & Tenancy — rules

`PLT-R-001` … `PLT-R-016`. Format: trigger / input / condition / effect / confidence. Cross-references
use the module's own shorthand (`ACC-R-*`, `WF-R-*`) where a rule from another module's rule set is
the authority.

## Tenancy and identity

### PLT-R-001 — Tenant isolation is one join deep
- **Trigger:** Any tenant-scoped read or write.
- **Input:** `ProjectEntityID` on the record; `FirmID` on the `ProjectEntity` row it points at.
- **Condition:** The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or
  one of its 9 subtype roots).
- **Effect:** The record carries **no** `FirmID` of its own. Tenant scoping must be enforced by
  joining to `ProjectEntity` and filtering on its `FirmID`, or not at all.
- **Confidence:** Derived — exhaustive field-list check, `../../data-model/project-entity.md` §4.

### PLT-R-002 — `FirmID` is not a first-class reference type
- **Trigger:** Any code generator or ORM that maps Lucernex's declared `<Entity> ID` FK types to
  foreign keys.
- **Input:** The type vocabulary (`Facility ID`, `Contract ID`, `Employer ID`, …, and `FirmID`
  itself, typed `Text`).
- **Condition:** No `Firm ID` type exists among the declared FK types.
- **Effect:** A schema-driven FK inference tool will silently miss the one relationship every row in
  the product ultimately has. Tenant references must be modelled deliberately, not discovered.
- **Confidence:** Derived — `project-entity.md` §4, corroborated by the type list in
  `../../data-model/graphql-api.md`.

### PLT-R-003 — `ProjectEntityID` survives database-per-tenant; `FirmID` does not need to
- **Trigger:** Any migration of a `ProjectEntityID`-scoped record into a per-tenant Spoke database.
- **Input:** The record's `ProjectEntityID`.
- **Condition:** The target architecture is database-per-tenant (one Spoke database per firm).
- **Effect:** `ProjectEntityID` must be retained — it is the intra-tenant partition and access-control
  unit (`LinkMemberProjectEntity`), not a tenant-scoping column being replaced. Only `FirmID`'s job
  (which physical database) is subsumed by the database boundary itself.
- **Confidence:** Derived — `tenancy-model.md`, `project-entity.md` §5.3.

## Extensibility and configuration

### PLT-R-004 — A new `ProjectEntity` subtype requires a new `Firm` column
- **Trigger:** Onboarding a new kind of ownable entity (a 12th subtype beyond the 11 `IsValidFor*`
  categories).
- **Input:** `Firm`'s eleven `*SetupPageLayoutID` columns.
- **Condition:** The new subtype needs a default setup-page-layout assignment, the same way the
  existing eleven do.
- **Effect:** `Firm` gains a twelfth column. There is no lookup table of (subtype, default layout)
  pairs — the enumeration is baked into the tenant record's own schema.
- **Confidence:** Observed field list (`data-model.md`), Derived conclusion.

### PLT-R-005 — Global/Firm scope is a column, not a second schema
- **Trigger:** A tenant customises the field registry, or reads `GlobalProperty`.
- **Input:** `IsGlobal` + `FirmID` on `ReportGroupAvailableField`/`ReportGroupData`; `FirmID` alone on
  `GlobalProperty`.
- **Condition:** —
- **Effect:** Tenant-specific configuration and platform-default configuration live in the same
  table, discriminated by a boolean/text pair, not partitioned physically.
- **Confidence:** Observed — `udf-registry.md`, `../reporting/report-field-registry.md`.

## Security

### PLT-R-006 — `Security` is a read-only, computed shadow of `UserClassSecurity`
- **Trigger:** Any permission check.
- **Input:** `UserClassSecurity` (has a physical table) and `Security` (does not).
- **Condition:** Both declare the same 21 fields.
- **Effect:** `UserClassSecurity` is the editable grant; `Security` is what a rebuild's authorization
  service would compute and cache, never what an admin edits directly.
- **Confidence:** Derived — exhaustive field-list diff, `data-model.md`.

### PLT-R-007 — A permission grant targets exactly one of four surfaces
- **Trigger:** A `UserClassSecurity` row is created.
- **Input:** `PageLayoutID`, `ReportGroupAvailableFieldID`, `ReportGroupDataID`/`RootReportGroupDataID`/
  `SubReportGroupDataID`, `DashboardComponentID`.
- **Condition:** —
- **Effect:** The grant is scoped to a whole page layout, a single field-registry leaf, a
  field-registry subtree, or a dashboard component — never more than one kind at a time, and the
  level (`SecurityLevelByteValue`) is one of `DEFAULT | NO_ACCESS | VIEW | EDIT | DELETE`.
- **Confidence:** Observed — `../../data-model/graphql-api.md` (`SecurityLevel` enum), Derived
  granularity claim from the column set.

## Org-chart and geography

### PLT-R-008 — Region is a three-level hierarchy resolved by `RegionID`/`RootRegionID`/`SubRegionID`
- **Trigger:** Workflow routing with `AssigneeType = REGION1 | REGION2 | MARKET`.
- **Input:** `ProjectEntity.RegionID`, `RootRegionID`, `SubRegionID`, `CodeMarketAreaID`,
  `CodeMarketTypeID`.
- **Condition:** The routing rule names a region-scoped principal category (see
  `../workflow/routing-and-approvals.md` §2, Dimension 2).
- **Effect:** The scope resolves against this three-column region hierarchy on the entity, not
  against a separate routing table. `Region` itself declares almost none of this shape directly — see
  `PLT-R-009`.
- **Confidence:** Derived — cross-module reconciliation between this module's schema and
  `../workflow/routing-and-approvals.md`.

### PLT-R-009 — `Region`'s real shape is not in this export
- **Trigger:** Any attempt to enumerate a region's own attributes (name, parent, level number).
- **Input:** `Region`'s one declared field, `ProjectEntityID`.
- **Condition:** 12 other objects reference `Region` across 34 columns.
- **Effect:** A rebuild cannot fully specify the `Region` entity from this corpus alone; treat it as
  a known gap, not an empty table.
- **Confidence:** Derived — `object-catalog.md` open question 1, unresolved.

### PLT-R-010 — Geography is two-level: country/state master, then jurisdiction
- **Trigger:** Any address capture on `Facility`, `Location`, `Parcel`, `Project`, `ProjectEntity`, or
  a person/company record in `people-parties`.
- **Input:** `StateProvinceCountryID` → `StateProvinceCountry` (ISO Alpha-2/3 codes); `JurisdictionID`
  → `Jurisdiction` (adds `TaxRate1`/`TaxRate2`).
- **Condition:** —
- **Effect:** Every address block in the product repeats the same `StreetAddress1..4`/`City`/
  `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not
  through the country/state master directly.
- **Confidence:** Derived — repeated field-block signature across every address-carrying object in
  `data-model.md` and `../../data-model/object-catalog.md`.

### PLT-R-011 — Exchange rates are point-in-time captures, not a live feed
- **Trigger:** A multi-currency Contract calculation.
- **Input:** `ExchangeRate.ContractID`, `ConversionRate`, `EffectiveDate`.
- **Condition:** —
- **Effect:** The rate used for a calculation is whatever was captured effective as of a given date,
  not a re-derived live lookup — supports historical reporting without recomputation.
- **Confidence:** Derived — field shape only, no live capture.

## Audit

### PLT-R-012 — Two unreconciled audit mechanisms coexist
- **Trigger:** Any change to a tracked field.
- **Input:** `AuditColumn`/`AuditTable` (explicit change log, keyed to the field-registry tree via
  `GroupID`/`SubGroupID`) **and** inline `CreatedByID`/`ModifiedByID` stamps present on most objects.
- **Condition:** 162 of 223 objects carry the inline stamps (161 `ModifiedByID`, only 79
  `CreatedByID`); it is unknown which objects also emit `AuditColumn` rows.
- **Effect:** A rebuild inherits the same open question ASG Edge+'s own unresolved ADR-0020
  (in-transaction audit vs. the ADR-0012 outbox) poses — Lucernex appears to run a version of both,
  unreconciled.
- **Confidence:** Derived — `../../data-model/object-catalog.md` open question 4.

### PLT-R-013 — Audit entries file under the field-registry tree, not a separate taxonomy
- **Trigger:** An `AuditColumn` row is written.
- **Input:** `GroupID`, `SubGroupID` (typed `sTYPE_REPORT_GROUP_DATA`).
- **Condition:** —
- **Effect:** "Group Name"/"Sub-Group" columns a user sees in an Audit Log screen are the same
  registry group/subgroup names used everywhere else field metadata is organised.
- **Confidence:** Derived — 11-for-11 column match, documented in full in
  `../reporting/report-field-registry.md`; cited, not re-derived, here.

## Thin objects — treat as gaps, not as complete

### PLT-R-014 — Single-field objects rely entirely on a join or virtual pattern for content
- **Trigger:** Any attempt to fully specify `EntityTemplate`, `MapClientSchedule`'s peers, `Notify`,
  `ScratchPad`, `AuditTable`, `Region`, `LinkPEMemberCodeJobTitle`, or `LinkRegionManager` from this
  export alone.
- **Input:** Each declares ≤1 stored field (`MapClientSchedule` is the exception at 10).
- **Condition:** —
- **Effect:** These are join/marker tables or the export is truncating them; either way, do not model
  them as one-column tables in the rebuild without a targeted schema-browser capture.
- **Confidence:** Derived — `object-catalog.md`'s "18 one-field objects" note.

### PLT-R-015 — `TemplateAudit` names four template kinds; this module owns one
- **Trigger:** A Budget, Entity, Folder, or Task template is applied to a `ProjectEntity`.
- **Input:** `TemplateAudit.BudgetEntityTemplateID`, `FolderEntityTemplateID`, `TaskEntityTemplateID`,
  `EntityTemplateID`.
- **Condition:** —
- **Effect:** A single audit table serves templating across modules; `EntityTemplate` (this module)
  is the only one of the four whose home object is filed here.
- **Confidence:** Observed field list; Derived scope conclusion.

### PLT-R-016 — `Project` and `ProjectEntity` are both live, unreconciled candidates for "the spine"
- **Trigger:** Any decision about which object is the entity supertype.
- **Input:** Both objects are classified `subtype_root`-shaped by the same mechanical test; field
  counts (111 vs. 107) and Data-Fields leaf counts (6 vs. 170) disagree about which is "lightweight."
- **Condition:** —
- **Effect:** Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity`
  and is the authority for the spine, but `Project`'s role remains genuinely open.
- **Confidence:** Derived — `object-catalog.md` open question 2, unresolved by this module's own
  pass.
