# Reports & Exports

Reporting and data export. Every field-consuming subsystem - reports, forms, exports - joins to one shared field registry. The vendor's own schema names the key to it 'Report/Form Field ID': a single type unifying report field and form field.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Anyone who has to get data out — analysts, auditors, and the integrations that read the product rather than the database.

## Where it is used

*Observed · fact · source: `docs/data-model/screen-routing.md`*

The report builder, the export tools, and the REST surface.

## One field registry

*Observed · capability · source: `docs/modules/reporting/README.md`*

The report catalogue and the field catalogue are one table, confirmed from the schema rather than hypothesised. A rebuilt reporting layer needs the same single registry or it will re-implement field metadata per consumer.

## Admin tool inventory

*Derived · capability · source: `docs/modules/reporting/`*

The admin reporting tools are inventoried in the docs: what each exposes, and that none of them define calculation logic - computed values are all defined at the field level, in the accounting and recovery engines.

## Import Export

*Observed · fact · source: `docs/features/import-export/README.md`*

What the import export manual settles: Four inbound paths, not one: generic XML bulk import (POST /rest/firm), document import, vendor-lease adapter pipeline, and the Atlas (RocketClub) AI lease-abstraction API. BOMapClientRecordID confirmed as the upsert key. No generic export endpoint exists. Biggest open question: What the four admin screens actually offer.

## Manual contents

*Observed · fact · source: `docs/features/import-export/README.md`*

The import export manual is organised as: HTTP 200 does not mean the write succeeded; The generic import: POST /rest/firm; The Import Data screen; Export Configuration is the publish mechanism; Import Best Practice Templates — the vendor's publish channel; Job Log — the first evidence of the product actually running; The lease-abstraction pipeline; Export; Staging tables; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Search Filtering

*Observed · fact · source: `docs/features/search-filtering/README.md`*

What the search filtering manual settles: Three separate mechanisms: per-placement list config in JSONConfigText (paging, totals, inline edit, IncludeInSearch), unused layout-level run-mode filters, and a FIQL API query surface with mandatory field selection. Biggest open question: Everything runtime — filter menus, saved filters, quick search.

## Manual contents

*Observed · fact · source: `docs/features/search-filtering/README.md`*

The search filtering manual is organised as: The list chrome, observed; Per-placement list behaviour; Layout-level filters: built, unused; The API query surface; Related field-level filtering; What this means for ASG Edge+. Read it rather than this node when you need the detail — this is the index.

## Evidence

*Observed · fact · source: `features/import-export/README.md`*

Written up in features/import-export/README.md, features/search-filtering/README.md. 4 screen captures on disk, under docs/assets/screenshots/data-model — the screens themselves, not a description of them. 4 of them are cited by name in the documentation, which is what ties a capture to the screen it shows.

![Contract schema table row: FacilityID, Type "Facility ID", UI Label "Facility"](../../assets/screenshots/data-model/object-model-contract-facilityid.jpg)
![Contract schema table rows: LocationID (Type "Location ID") and MasterContractID (Type "Contract ID", self-referencing)](../../assets/screenshots/data-model/object-model-contract-locationid-mastercontractid.jpg)
![PaymentTransaction schema table row: VendorID, Type "Employer ID", UI Label "Vendor"](../../assets/screenshots/data-model/object-model-paymenttransaction-vendorid.jpg)
![walkHierarchy.jsp showing Contract as an aggregate root with ~70 nested owned child tables](../../assets/screenshots/data-model/walk-hierarchy-re-contract-schema.jpg)

## Open questions (83)

*Inferred · group*

83 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Does Lx have charts at

*Inferred · question · source: `docs/modules/reporting/README.md`*

Does Lx have charts at all? No chart, series, axis, widget or visualisation object exists in the 223-table schema. Either dashboard tiles are grid/text only, or configuration is packed into PageLayout.JSONConfigText. This decides whether BRD 8's dashboards are a parity feature or a greenfield one. *Check:* open Manage Dashboard Reports and inspect one tile. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### Is there any report

*Inferred · question · source: `docs/modules/reporting/README.md`*

Is there any report-run history beyond LastRunBy/LastRunDate? Report Log is the same JSP as Job Log with type=reportlog, i.e. a *job* log. If no run history exists, ASG's operational requirements (RPT-R-075, "blank reports still sent") are greenfield, not migration. *Check:* open Report Log. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### Does Lx schedule

*Inferred · question · source: `docs/modules/reporting/README.md`*

Does Lx schedule reports, and where is a schedule stored? No schedule or subscription table exists in the schema. RPT-R-073 (scheduled + SFTP delivery, Major) may have nothing to migrate from. *Check:* Report Log, Email Log, Job Log. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### Are PageLayout

*Inferred · question · source: `docs/modules/reporting/README.md`*

~~Are PageLayout / PageLayoutField / PageLayoutFilter exposed over GraphQL?~~ Answered: no. The schema has 490 types, 433 of them objects, and contains no layout, report, chart or rule type — 617 queries against 3 mutations, all over business objects (graphql-api.md). Reports and layouts cannot be migrated through the data API. *Still to check:* whether the REST tier differs, since it appears to be the write surface. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### What are the

*Inferred · question · source: `docs/modules/reporting/README.md`*

What are the OutputType and PageLayoutType value sets? Sets the output-format and layout-type enums, and the true scope of work areas 27-31. *Check:* GraphQL introspection, or distinct EquivalentPLTypes values. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### Is Portfolio Capital

*Inferred · question · source: `docs/modules/reporting/README.md`*

Is Portfolio/Capital-Program scoping enforced at the query level or only in the UI? A multi-tenant correctness and SOC 2 question, raised but unresolved in 007. *Check:* run a report as a scoped user. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### Does Export

*Inferred · question · source: `docs/modules/reporting/README.md`*

Does Export Configuration include layouts and reports, or only master data? Determines the migration vehicle for Reports/Layout/Field Migration. *Check:* inspect an export. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### Where does

*Inferred · question · source: `docs/modules/reporting/README.md`*

Where does ReportGroupData store the three "Valid For..." applicability flags? They are rendered by Manage Data Fields but exist on neither RGAF nor RGD in the object model. Affects how ASG Edge+ models field applicability. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### What does

*Inferred · question · source: `docs/modules/reporting/README.md`*

What does ComparisonItem.XmlData contain? A serialised blob at the heart of the comparison report; unqueryable and a migration risk. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### How is a report s

*Inferred · question · source: `docs/modules/reporting/README.md`*

How is a report's Portfolio/Capital-Program scope stored? The chip control is observed on the layout edit dialog; no column in either offline artefact holds it. Nobody has confirmed this. Recorded in modules/reporting/README.md, under the Reporting area. Until it is settled, anything built on the assumption is a guess.

### What is the item ID

*Inferred · question · source: `docs/data-model/README.md`*

What is the item ID type's actual target table? 56 columns carry it; 54 are named *PageLayoutID / *LayoutID / *ReportGroupDataID and the remaining two are AuditColumn's GroupID / SubGroupID — i.e. **all 56 point at configuration metadata that lives outside these 223 business objects**. Confirming the physical target needs a ShowObjectDetails.jsp pass over a layout-carrying table (Firm carries 11 of them). Nobody has confirmed this. Recorded in data-model/README.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### walkHierarchy jsp

*Inferred · question · source: `docs/data-model/README.md`*

walkHierarchy.jsp lists Site, Opening Project, Capital Program, Capital Project and Equipment Contract as aggregate roots, but no object of those names exists in the export. The IsValidFor* flags on VirtualTemplateBudget enumerate the same 11 names. Are these ProjectEntityTypeName discriminator values over shared tables, or separate tables absent from this export? See project-entity.md §4. Nobody has confirmed this. Recorded in data-model/README.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Only 33 of 223 objects

*Inferred · question · source: `docs/data-model/README.md`*

Only 33 of 223 objects have a populated LucObject in _crossmap.tsv; the remaining join has to go through LeafTable, which covers 195. The 28 objects with neither have no Manage Data Fields catalog entry at all — are they genuinely not user-configurable, or was the capture incomplete?. Nobody has confirmed this. Recorded in data-model/README.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Contract names four

*Inferred · question · source: `docs/data-model/README.md`*

Contract names four physical tables but repeats ContractID only three times, while ExpenseRecovery names four and repeats ExpenseRecoveryID four times. Is contract_firm1 keyed differently, or is this an export artefact?. Nobody has confirmed this. Recorded in data-model/README.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Does the GraphQL

*Inferred · question · source: `docs/data-model/README.md`*

Does the GraphQL schema in graphql-api.md agree with this graph? It reports 490 types against these 223 objects. Reconciling the two would settle several open questions at once — in particular ProjectEntityTypeName's value set, whether Site / Opening Project / Equipment Contract are separate types, and what item ID points at. Nobody has confirmed this. Recorded in data-model/README.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What are the values in

*Inferred · question · source: `docs/data-model/code-table-registry.md`*

**What are the values in Straight Line Schedule Type Code, ASC 842 Schedule Type Code and IFRS 16 Schedule Type Code?** These are the accounting engine's configuration surface and each value carries 20 ExportAcctNNumber GL slots. Opening 2161/2162/2163 would settle a large part of docs/modules/accounting/asc-842.md's open questions. Nobody has confirmed this. Recorded in data-model/code-table-registry.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What are the values in

*Inferred · question · source: `docs/data-model/code-table-registry.md`*

What are the values in Contract Status Code (2094)? Needed for the contract lifecycle state machine. Nobody has confirmed this. Recorded in data-model/code-table-registry.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Where does workflow

*Inferred · question · source: `docs/data-model/code-table-registry.md`*

Where does workflow status actually live, given Work Flow Status Code is not in this catalogue?. Nobody has confirmed this. Recorded in data-model/code-table-registry.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Confirm the 2000 3000

*Inferred · question · source: `docs/data-model/code-table-registry.md`*

Confirm the 2000/3000 band distinction by checking every 3000-band table's object for behaviour-bearing columns. The claim currently rests on CodeExpenseType plus the naming pattern. Nobody has confirmed this. Recorded in data-model/code-table-registry.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What is Source Entity

*Inferred · question · source: `docs/data-model/code-table-registry.md`*

What is Source Entity Code (2172)? It appears alongside AccrualTransaction.SourceEntityTable, suggesting a polymorphic-association discriminator — which would be a second soft-reference mechanism worth understanding. Nobody has confirmed this. Recorded in data-model/code-table-registry.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Is referential

*Inferred · question · source: `docs/data-model/foreign-key-graph.md`*

Is referential integrity enforced? The FK *types* are declared, but nothing in this export shows whether the database has constraints. If not, migrated data may contain dangling references and ASG Edge+ cannot assume clean joins. Nobody has confirmed this. Recorded in data-model/foreign-key-graph.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What is LeaseInfo 219

*Inferred · question · source: `docs/data-model/foreign-key-graph.md`*

What is LeaseInfo? 219 fields, in-degree 0, two outbound FKs. Reporting projection, or a legacy table superseded by Contract? It is the third-largest object in the product and nothing in the corpus explains it. Nobody has confirmed this. Recorded in data-model/foreign-key-graph.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### item ID s physical

*Inferred · question · source: `docs/data-model/foreign-key-graph.md`*

item ID's physical target. Confirmed to point at configuration metadata; the actual table is unknown. A ShowObjectDetails.jsp pass on Firm (11 such columns) would settle it. Nobody has confirmed this. Recorded in data-model/foreign-key-graph.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Do templates and

*Inferred · question · source: `docs/data-model/foreign-key-graph.md`*

Do templates and instances really share tables? WorkFlow.WorkFlowTemplateID typed Work Flow ID and WorkFlowStep.WorkFlowTemplateStepID typed Step ID say yes, but WorkFlowTemplate and WorkFlowTemplateStep also exist as separate objects with their own tables. Both cannot be the whole story. Nobody has confirmed this. Recorded in data-model/foreign-key-graph.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Three parallel

*Inferred · question · source: `docs/data-model/foreign-key-graph.md`*

Three parallel milestone mechanisms (KeyDate, Task/TaskGroup/TaskItem, ProcessTimeline). Are these genuinely different concepts, or accreted duplicates? This matters before ASG Edge+ builds any of them. Nobody has confirmed this. Recorded in data-model/foreign-key-graph.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What are the 3

*Inferred · question · source: `docs/data-model/graphql-api.md`*

What are the 3 mutations? With 617 queries and only 3 mutations, the write path is the single biggest unknown in the API. Enumerate them and determine what the intended write surface actually is. Nobody has confirmed this. Recorded in data-model/graphql-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Does the schema

*Inferred · question · source: `docs/data-model/graphql-api.md`*

Does the schema contain the conditional-field rule storage? The per-field conditional display rule editor (see 008) was never opened. If a Condition/Rule/Criteria type exists in these 433 object types, it settles the mechanism without needing the blocked UI. Nobody has confirmed this. Recorded in data-model/graphql-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What does RESTful jsp

*Inferred · question · source: `docs/data-model/graphql-api.md`*

What does RESTful.jsp document, and is it the write path implied by question 1?. Nobody has confirmed this. Recorded in data-model/graphql-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Does Export Schema

*Inferred · question · source: `docs/data-model/graphql-api.md`*

Does Export Schema produce a downloadable full schema file? That would give the complete 250 KB SDL and the physical model in one step, without paging it through a browser tool. Nobody has confirmed this. Recorded in data-model/graphql-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Is the cluster JWT

*Inferred · question · source: `docs/data-model/graphql-api.md`*

Is the cluster JWT claim genuinely a tenant-routing key? If so it is direct vendor precedent for the ASG Edge+ Hub/Spoke routing design. Nobody has confirmed this. Recorded in data-model/graphql-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### The 18 one field

*Inferred · question · source: `docs/data-model/object-catalog.md`*

The 18 one-field objects. BudgetTemplate, TaskTemplate and FolderTemplate each declare one field, yet their content is clearly visible through the corresponding VirtualTemplate* projection (16–17 fields including 12 IsValidFor* flags). That pattern suggests the export lists only the *stored* column and surfaces the rest through a view — but Region (1 field, in-degree 12) and Notify (1 field) do not fit that reading. Needs a ShowObjectDetails.jsp pass on each. Nobody has confirmed this. Recorded in data-model/object-catalog.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Project vs

*Inferred · question · source: `docs/data-model/object-catalog.md`*

Project vs ProjectEntity. Project has 111 fields and is a subtype_root; ProjectEntity has 107. INDEX.md calls Project "a lightweight project identity record … distinct from the richer ProjectEntity" but reports only 6 Data-Fields leaves for it against 170 for ProjectEntity. The two sources disagree about which is the lightweight one. Nobody has confirmed this. Recorded in data-model/object-catalog.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### objects have no Manage

*Inferred · question · source: `docs/data-model/object-catalog.md`*

28 objects have no Manage Data Fields entry at all (no LeafTable match in _crossmap.tsv), including Security, TaskGroup, TaskItem, NonMember and both *FullImport objects. Are they simply not user-configurable, or is the Data Fields capture incomplete for them?. Nobody has confirmed this. Recorded in data-model/object-catalog.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What are ChangeManage

*Inferred · question · source: `docs/data-model/object-catalog.md`*

What are ChangeManage and VirtualTemplateMember? One field each, and the only two in-scope tables the picker exposes that this catalogue lacks. Nobody has confirmed this. Recorded in data-model/object-catalog.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### AuditColumn and

*Inferred · question · source: `docs/data-model/object-catalog.md`*

AuditColumn and AuditTable describe a separate audit-log model, yet **162 of 223 objects also carry inline CreatedByID/ModifiedByID columns** (161 have ModifiedByID, only 79 have CreatedByID — so most objects record who last touched a row but not who made it). Which is authoritative? This is the same choice ASG Edge+'s open ADR-0020 question poses (in-transaction audit vs. the ADR-0012 outbox), and Lx appears to run both. Nobody has confirmed this. Recorded in data-model/object-catalog.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Does Location belong

*Inferred · question · source: `docs/data-model/project-entity.md`*

Does Location belong in the ASG Edge+ Hub or the Spoke? (§5.2) Blocks any Location modelling in either service. Lx's answer and the workspace index's answer disagree. Nobody has confirmed this. Recorded in data-model/project-entity.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What are

*Inferred · question · source: `docs/data-model/project-entity.md`*

What are ProjectEntityTypeName's actual values? The eleven types are inferred from two indirect sources. A single walkHierarchy.jsp "All Values For" pass, or a ShowObjectDetails.jsp read of ProjectEntity, would confirm the enumeration directly — and this enumeration is the backbone of the whole subtype model. Nobody has confirmed this. Recorded in data-model/project-entity.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Is the subtype

*Inferred · question · source: `docs/data-model/project-entity.md`*

Is the subtype relationship a shared primary key, or a separate FK? The export shows both EntityId and ProjectEntityID as Number on every subtype root. Two numeric identity columns is unusual and unexplained; one of them may be the real shared key and the other a legacy or display id. This determines how ASG Edge+ would model the inheritance if it chose to. Nobody has confirmed this. Recorded in data-model/project-entity.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Where do Site Opening

*Inferred · question · source: `docs/data-model/project-entity.md`*

**Where do Site, Opening Project, Capital Program, Capital Project and Equipment Contract live physically?** They are named as aggregate roots and as IsValidFor* flags, but no object bears those names. Best reading: they are ProjectEntityTypeName values over PotentialProject, Project, Program and Contract — but "Capital Program vs Portfolio both mapping to Program" and "RE Contract vs Equipment Contract both mapping to Contract" needs confirming, not assuming. Nobody has confirmed this. Recorded in data-model/project-entity.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Do the 13 objects

*Inferred · question · source: `docs/data-model/project-entity.md`*

Do the 13 objects using the soft Entity type (e.g. AssetHistory) count as entity-scoped? They behave as if they do; the mechanical classification misses them because their column is typed Entity, not Entity ID. Nobody has confirmed this. Recorded in data-model/project-entity.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Is ProjectEntity

*Inferred · question · source: `docs/data-model/project-entity.md`*

Is ProjectEntity itself firm-scoped or shared? It carries FirmID, which says firm-scoped. But Complex, DMA and StateProvinceCountry — which ProjectEntity points *at* — are firm-global. A Spoke database would therefore need read access to Hub reference data on every entity read. That is the Hub→Spoke publish/accept mechanism the workspace index flags as not yet written down, and this is a concrete case for it. Nobody has confirmed this. Recorded in data-model/project-entity.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Reconcile 7 421 6 158

*Inferred · question · source: `docs/data-model/reading-the-census.md`*

Reconcile 7,421 / 6,158 / 7,047. What inclusion rule differs between the three?. Nobody has confirmed this. Recorded in data-model/reading-the-census.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Why do 12 objects have

*Inferred · question · source: `docs/data-model/reading-the-census.md`*

Why do 12 objects have census fields but no catalog rows? PotentialProject with 108 and 0 is the starkest. A plausible reading is that these are not layout-placeable, but that is Inferred. Nobody has confirmed this. Recorded in data-model/reading-the-census.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Open question

*Inferred · question · source: `docs/data-model/reading-the-census.md`*

CommitteePackageTemplate is in the View Object Model picker and absent from the census entirely. How many other objects are?. Nobody has confirmed this. Recorded in data-model/reading-the-census.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Re derive join tables

*Inferred · question · source: `docs/data-model/reading-the-census.md`*

Re-derive join tables' real keys and rebuild edges.json from the View Object Model rather than the census. Nobody has confirmed this. Recorded in data-model/reading-the-census.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Which of the 153

*Inferred · question · source: `docs/data-model/reading-the-census.md`*

Which of the 153 untyped *ID columns are genuine joins? Some will be external reference numbers that merely look like keys. Nobody has confirmed this. Recorded in data-model/reading-the-census.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What does the

*Inferred · question · source: `docs/data-model/rest-api.md`*

What does the documentation actually render — endpoint paths, verbs, payload schemas? This is the single largest remaining gap in understanding the write path. Nobody has confirmed this. Recorded in data-model/rest-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Are REST writes full

*Inferred · question · source: `docs/data-model/rest-api.md`*

Are REST writes full CRUD per record type, or is the surface read-plus-import like GraphQL? This determines whether the incumbent has a general write API at all. Nobody has confirmed this. Recorded in data-model/rest-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Confirm that Firm

*Inferred · question · source: `docs/data-model/rest-api.md`*

Confirm that Firm (tenant) fields genuinely cannot be marked required, and if so, whether Show and Require on a page layout is the only mechanism for a mandatory custom field. Nobody has confirmed this. Recorded in data-model/rest-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Does the REST layer

*Inferred · question · source: `docs/data-model/rest-api.md`*

Does the REST layer expose the same FIQL filter grammar the GraphQL examples use?. Nobody has confirmed this. Recorded in data-model/rest-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What is the Data

*Inferred · question · source: `docs/data-model/rest-api.md`*

What is the Data Dictionary menu item seen in the application chrome alongside Bookmark? It may be a further schema-documentation surface not yet explored. Nobody has confirmed this. Recorded in data-model/rest-api.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What does PForm jsp

*Inferred · question · source: `docs/data-model/screen-routing.md`*

What does PForm.jsp actually render for a real contract? The routing is known; the output is not. This is the single most valuable next capture. Nobody has confirmed this. Recorded in data-model/screen-routing.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Do these 81 screens

*Inferred · question · source: `docs/data-model/screen-routing.md`*

Do these 81 screens vary by user class? This is one user's menu. If SecurityLevel filters it, the menu is permission-driven data rather than fixed structure. Nobody has confirmed this. Recorded in data-model/screen-routing.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### What is

*Inferred · question · source: `docs/data-model/screen-routing.md`*

What is LeaseMaintenanceEdit.jsp, the sole route for Facility → Responsibilities, and why does Contract → Responsibilities use PLForm.jsp instead?. Nobody has confirmed this. Recorded in data-model/screen-routing.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Scheduled Offsets

*Inferred · question · source: `docs/data-model/screen-routing.md`*

Scheduled Offsets (19844) and Recoveries (3516) are both list layouts under Payment Info — which schema tables back each?. Nobody has confirmed this. Recorded in data-model/screen-routing.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Are there menu entries

*Inferred · question · source: `docs/data-model/screen-routing.md`*

Are there menu entries this user cannot see? 109 nodes were returned; the Manage Top Menu admin screen would say whether more exist. Nobody has confirmed this. Recorded in data-model/screen-routing.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Are the 229 dropdown

*Inferred · question · source: `docs/data-model/type-system.md`*

Are the 229 dropdown code lists Global-only, or can a tenant add code lists that appear as new Dropdown (…) types? docs/admin/007 shows both Firm and Client drop-downs; whether a Client drop-down produces a distinct schema type was not established. Nobody has confirmed this. Recorded in data-model/type-system.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Percent or Currency 2

*Inferred · question · source: `docs/data-model/type-system.md`*

Percent or Currency (2 fields) is a union type. Which column decides the interpretation at runtime?. Nobody has confirmed this. Recorded in data-model/type-system.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Number with no digits

*Inferred · question · source: `docs/data-model/type-system.md`*

Number with no digits (8 fields, 3 objects) — integer, or a formatting instruction? The name suggests presentation, which would make it a fourth leaked presentation type. Nobody has confirmed this. Recorded in data-model/type-system.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

### Does the platform

*Inferred · question · source: `docs/data-model/type-system.md`*

Does the platform enforce referential integrity on FK-typed columns, or is the type purely a UI/lookup hint? Nothing in this export settles it, and it changes whether ASG Edge+ can trust migrated data. Nobody has confirmed this. Recorded in data-model/type-system.md, under the Data model & APIs area. Until it is settled, anything built on the assumption is a guess.

## Rules (49)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### A What a report is — [RPT-R-001](../rules/RPT-R-001.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**A report is not a distinct record type. It is a `PageLayout` row with `IsReport = true`.**

|  |  |
|---|---|
| Stated as | A report is not a distinct record type. It is a `PageLayout` row with `IsReport = true`. There is no `Report` table in the schema. |
| Stated as | Derived (absence across 223 objects) + Observed (the column) |
| Stated as | `_lucernex_objects_summary.txt`; `all-fields.csv` |

### A What a report is — [RPT-R-002](../rules/RPT-R-002.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A report is run, not viewed: `PageLayout.LastRunBy` and `LastRunDate` record the most recent execution on the definition row itself. · Observed (columns) + Inferred (meaning) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | A report is run, not viewed: `PageLayout.LastRunBy` and `LastRunDate` record the most recent execution on the definition row itself. |
| Stated as | Observed (columns) + Inferred (meaning) |
| Stated as | `all-fields.csv` |

### A What a report is — [RPT-R-003](../rules/RPT-R-003.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A report's output format is a required property of the definition (`OutputType`), not chosen at run time. · Observed · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | A report's output format is a required property of the definition (`OutputType`), not chosen at run time. |
| Stated as | Observed |
| Stated as | `all-fields.csv` |

### A What a report is — [RPT-R-004](../rules/RPT-R-004.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A report declares which entities it may be run against (`EntitySelectionFilter`) and which filters the user is offered at run time (`RunModeFilters`). Both required.**

|  |  |
|---|---|
| Stated as | A report declares which entities it may be run against (`EntitySelectionFilter`) and which filters the user is offered at run time (`RunModeFilters`). Both required. |
| Stated as | Observed (columns) + Inferred (meaning) |
| Stated as | `all-fields.csv` |

### A What a report is — [RPT-R-005](../rules/RPT-R-005.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Reports are Global (platform standard, `IsGlobalReport = true`) or tenant/personal. `OwnedByMemberID` gives a report a personal owner.**

|  |  |
|---|---|
| Stated as | Reports are Global (platform standard, `IsGlobalReport = true`) or tenant/personal. `OwnedByMemberID` gives a report a personal owner. |
| Stated as | Observed (columns) |
| Stated as | `all-fields.csv` |

### A What a report is — [RPT-R-006](../rules/RPT-R-006.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A dashboard tile is a `PageLayout` row with `IsDashboardReport = true`, administered by Manage Dashboard Reports (`/en/reports/ManageDashboardModules.jsp`). · Observed (column + route) + Inferred (the binding) · `all-fields.csv`;.**

|  |  |
|---|---|
| Stated as | A dashboard tile is a `PageLayout` row with `IsDashboardReport = true`, administered by Manage Dashboard Reports (`/en/reports/ManageDashboardModules.jsp`). |
| Stated as | Observed (column + route) + Inferred (the binding) |
| Stated as | `all-fields.csv`; 004 |

### A What a report is — [RPT-R-007](../rules/RPT-R-007.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A report can appear as its own navigation entry (`IsMenuLink`) and can be placed in the menu tree by `HierarchyName`, exactly like a page. · Observed (columns) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | A report can appear as its own navigation entry (`IsMenuLink`) and can be placed in the menu tree by `HierarchyName`, exactly like a page. |
| Stated as | Observed (columns) |
| Stated as | `all-fields.csv` |

### A What a report is — [RPT-R-008](../rules/RPT-R-008.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A report can be redirected wholesale to a system URL (`PageLayout.URL`), discarding its configured columns. Same escape hatch as any layout (LAY-R-106).**

|  |  |
|---|---|
| Stated as | A report can be redirected wholesale to a system URL (`PageLayout.URL`), discarding its configured columns. Same escape hatch as any layout (LAY-R-106). |
| Stated as | Observed |
| Stated as | 008 |

### A What a report is — [RPT-R-009](../rules/RPT-R-009.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A layout can host report-triggering action buttons, a distinct button kind labelled "(Run Report Action)" — observed as `Expense Report` and `Check History` on the ASG Contract Payments edit layout. Reports are therefore invocable from inside an ordinary record page.**

|  |  |
|---|---|
| Stated as | A layout can host report-triggering action buttons, a distinct button kind labelled "(Run Report Action)" — observed as `Expense Report` and `Check History` on the ASG Contract Payments edit layout. Reports are therefore invocable from inside an ordinary record page. |
| Stated as | Observed |
| Stated as | 008 |

### B Report columns and — [RPT-R-010](../rules/RPT-R-010.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Report columns are drawn from the same field registry as forms — `ReportGroupAvailableField`, whose FK type Lx names `Report/Form Field ID`. There is no separate report-field catalog.**

|  |  |
|---|---|
| Stated as | Report columns are drawn from the same field registry as forms — `ReportGroupAvailableField`, whose FK type Lx names `Report/Form Field ID`. There is no separate report-field catalog. |
| Stated as | Observed |
| Stated as | report-field-registry.md |

### B Report columns and — [RPT-R-011](../rules/RPT-R-011.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A field carries two labels: `DefaultLabel` ("Label") and `UILabel` ("Report Field Label"). A field may therefore present differently on a form than as a report column header.**

|  |  |
|---|---|
| Stated as | A field carries two labels: `DefaultLabel` ("Label") and `UILabel` ("Report Field Label"). A field may therefore present differently on a form than as a report column header. |
| Stated as | Observed (columns and their captions) + Inferred (which surface uses which) |
| Stated as | `all-fields.csv` |

### B Report columns and — [RPT-R-012](../rules/RPT-R-012.md)

*Inferred · rule · source: `docs/modules/reporting/rules.md`*

**A report column is a `PageLayoutField` row; grid geometry uses the `View*` coordinate set (`ViewRowPosition`, `ViewColumnPosition`, `ViewFieldWidth`, `ViewFieldHeight`, `HeaderColumnPosition`).**

|  |  |
|---|---|
| Stated as | A report column is a `PageLayoutField` row; grid geometry uses the `View*` coordinate set (`ViewRowPosition`, `ViewColumnPosition`, `ViewFieldWidth`, `ViewFieldHeight`, `HeaderColumnPosition`). |
| Stated as | Inferred (high) |
| Stated as | `all-fields.csv` |

### B Report columns and — [RPT-R-013](../rules/RPT-R-013.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A column can be searchable but hidden from the grid — a third visibility state distinct from shown and removed. · Observed · 008.**

|  |  |
|---|---|
| Stated as | A column can be searchable but hidden from the grid — a third visibility state distinct from shown and removed. |
| Stated as | Observed |
| Stated as | 008 |

### B Report columns and — [RPT-R-014](../rules/RPT-R-014.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A report may include fields from related tables reached by declared FKs, disambiguated by `FieldContext`. · Observed (Related Fields) + Inferred (the column's role) · 009;.**

|  |  |
|---|---|
| Stated as | A report may include fields from related tables reached by declared FKs, disambiguated by `FieldContext`. |
| Stated as | Observed (Related Fields) + Inferred (the column's role) |
| Stated as | 009; `all-fields.csv` |

### B Report columns and — [RPT-R-015](../rules/RPT-R-015.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A report may include fields from a tenant's Custom Lists, which are ordinary registry leaves under the owning table's `Custom Lists` subgroup. · Observed · 008.**

|  |  |
|---|---|
| Stated as | A report may include fields from a tenant's Custom Lists, which are ordinary registry leaves under the owning table's `Custom Lists` subgroup. |
| Stated as | Observed |
| Stated as | 008 |

### B Report columns and — [RPT-R-016](../rules/RPT-R-016.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Every registry field carries a Value Javascript hook, so a report column's value can be scripted rather than read. · Observed · 005.**

|  |  |
|---|---|
| Stated as | Every registry field carries a Value Javascript hook, so a report column's value can be scripted rather than read. |
| Stated as | Observed |
| Stated as | 005 |

### B Report columns and — [RPT-R-017](../rules/RPT-R-017.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**The registry marks computed fields with `IsFunctional` and carries a `Definition` textarea for the computation. `View Object Model` exposes a `Functional Field?` column and `Math`/`Computed` filter radios.**

|  |  |
|---|---|
| Stated as | The registry marks computed fields with `IsFunctional` and carries a `Definition` textarea for the computation. `View Object Model` exposes a `Functional Field?` column and `Math`/`Computed` filter radios. |
| Stated as | Observed |
| Stated as | `all-fields.csv`; 009 |

### C Filters grouping — [RPT-R-020](../rules/RPT-R-020.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Report and list filters are `PageLayoutFilter` rows: `ReportGroupAvailableFieldID` (required) + two `CriteriaType`/`CriteriaValue` pairs, discriminated by a required `IsListFilter` boolean. This is not the conditional-field store — conditional field rules are persisted as a JSON document per….**

|  |  |
|---|---|
| Stated as | Report and list filters are `PageLayoutFilter` rows: `ReportGroupAvailableFieldID` (required) + two `CriteriaType`/`CriteriaValue` pairs, discriminated by a required `IsListFilter` boolean. This is not the conditional-field store — conditional field rules are persisted as a JSON document per target, per live capture (conditional-fields.md). |
| Stated as | Observed (columns) + Inferred (role) |
| Stated as | `all-fields.csv` |

### C Filters grouping — [RPT-R-021](../rules/RPT-R-021.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A filter row names one field (`ReportGroupAvailableFieldID`, required) and carries two operator/value pairs — a two-clause predicate on that field, e.g. a `between`.**

|  |  |
|---|---|
| Stated as | A filter row names one field (`ReportGroupAvailableFieldID`, required) and carries two operator/value pairs — a two-clause predicate on that field, e.g. a `between`. |
| Stated as | Observed (columns) + Inferred (the pairing) |
| Stated as | `all-fields.csv` |

### C Filters grouping — [RPT-R-022](../rules/RPT-R-022.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Multiple filter rows chain through `ExtendedGroupFilterID` (self-FK). Whether the chain is AND, OR, or an explicit group is undetermined.**

|  |  |
|---|---|
| Stated as | Multiple filter rows chain through `ExtendedGroupFilterID` (self-FK). Whether the chain is AND, OR, or an explicit group is undetermined. |
| Stated as | Observed (column) + Open (semantics) |
| Stated as | `all-fields.csv` |

### C Filters grouping — [RPT-R-023](../rules/RPT-R-023.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**The same row that filters also groups: `RowOrderBy` and `ColumnOrderBy` give a field a position on each axis. Reporting in Lx is pivot-shaped, not flat-list-shaped.**

|  |  |
|---|---|
| Stated as | The same row that filters also groups: `RowOrderBy` and `ColumnOrderBy` give a field a position on each axis. Reporting in Lx is pivot-shaped, not flat-list-shaped. |
| Stated as | Observed (columns) + Inferred (semantics) |
| Stated as | `all-fields.csv` |

### C Filters grouping — [RPT-R-024](../rules/RPT-R-024.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**`ShowSubtotal` emits a subtotal at a grouping break; `ShowLabel` renders the grouping field's label there.**

|  |  |
|---|---|
| Stated as | `ShowSubtotal` emits a subtotal at a grouping break; `ShowLabel` renders the grouping field's label there. |
| Stated as | Observed (columns) + Inferred |
| Stated as | `all-fields.csv` |

### C Filters grouping — [RPT-R-025](../rules/RPT-R-025.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Report currency is a property of the definition (`PageLayout.CodeCurrencyTypeID`), not of the run. · Observed (column) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Report currency is a property of the definition (`PageLayout.CodeCurrencyTypeID`), not of the run. |
| Stated as | Observed (column) |
| Stated as | `all-fields.csv` |

### C Filters grouping — [RPT-R-026](../rules/RPT-R-026.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**[BLOCKED] The `CriteriaType` operator codebook is a small integer enum whose members are unobservable offline. Check: distinct `CriteriaType1`/`CriteriaType2` values via GraphQL Explorer.**

|  |  |
|---|---|
| Stated as | [BLOCKED] The `CriteriaType` operator codebook is a small integer enum whose members are unobservable offline. Check: distinct `CriteriaType1`/`CriteriaType2` values via GraphQL Explorer. |
| Stated as | Open |
| Stated as | — |

### D Purpose built — [RPT-R-030](../rules/RPT-R-030.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A Comparison Report is a first-class record (`ComparisonReport`) that still delegates its rendering to a `PageLayout` (`PageLayoutID`, required). Even the bespoke report types run on the generic layout engine.**

|  |  |
|---|---|
| Stated as | A Comparison Report is a first-class record (`ComparisonReport`) that still delegates its rendering to a `PageLayout` (`PageLayoutID`, required). Even the bespoke report types run on the generic layout engine. |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt`; `all-fields.csv` |

### D Purpose built — [RPT-R-031](../rules/RPT-R-031.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A Comparison Report's cells live in `ComparisonItem`, one row per scenario column, carrying `ScenarioName`, `ScenarioDate`, `ExpenseGroup`, `Assumptions`, `ComputedValue` and a serialised `XmlData` payload. · Observed · `_lucernex_objects_summary.txt`.**

|  |  |
|---|---|
| Stated as | A Comparison Report's cells live in `ComparisonItem`, one row per scenario column, carrying `ScenarioName`, `ScenarioDate`, `ExpenseGroup`, `Assumptions`, `ComputedValue` and a serialised `XmlData` payload. |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt` |

### D Purpose built — [RPT-R-032](../rules/RPT-R-032.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Demographic Reports are the only report family with an explicit asynchronous execution record: `DemographicResults` carries `TimeInitiated`, `TimeFinished`, a status code, a third-party vendor code, and a `DocumentID` for the produced artefact. · Observed · `_lucernex_objects_summary.txt`.**

|  |  |
|---|---|
| Stated as | Demographic Reports are the only report family with an explicit asynchronous execution record: `DemographicResults` carries `TimeInitiated`, `TimeFinished`, a status code, a third-party vendor code, and a `DocumentID` for the produced artefact. |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt` |

### D Purpose built — [RPT-R-033](../rules/RPT-R-033.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**A Demographic Report's scope is a trade area defined by radius or drive time (`DemographicStudyArea.AreaRadius`, `.AreaDriveTimeInMinutes`, `.CodeRadiusUnitID`) — a site-selection feature, not a lease-accounting one. · Observed · `_lucernex_objects_summary.txt`.**

|  |  |
|---|---|
| Stated as | A Demographic Report's scope is a trade area defined by radius or drive time (`DemographicStudyArea.AreaRadius`, `.AreaDriveTimeInMinutes`, `.CodeRadiusUnitID`) — a site-selection feature, not a lease-accounting one. |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt` |

### D Purpose built — [RPT-R-036](../rules/RPT-R-036.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**`Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForecastPeriod` (20) and others — so a report can select from a….**

|  |  |
|---|---|
| Stated as | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForecastPeriod` (20) and others — so a report can select from a calculated period series with no materialisation step. |
| Stated as | Derived (naming pattern, 12 objects) + Inferred (non-persistence) |
| Stated as | `_lucernex_objects_summary.txt` |

### E Audit reporting — [RPT-R-040](../rules/RPT-R-040.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Field-level change audit is stored in `AuditColumn`, with `EntityName`, `CodeSQLTableID`, `ObjectID`, `FieldName`, `AuditAction`, `OldValue`, `NewValue` and the actor/timestamp. · Observed · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Field-level change audit is stored in `AuditColumn`, with `EntityName`, `CodeSQLTableID`, `ObjectID`, `FieldName`, `AuditAction`, `OldValue`, `NewValue` and the actor/timestamp. |
| Stated as | Observed |
| Stated as | `all-fields.csv` |

### E Audit reporting — [RPT-R-041](../rules/RPT-R-041.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report.**

|  |  |
|---|---|
| Stated as | Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report. |
| Stated as | Observed (columns) + Derived (11-for-11 match with the observed Audit Log dialog) |
| Stated as | `all-fields.csv`; 007 |

### E Audit reporting — [RPT-R-042](../rules/RPT-R-042.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Login, lockout and impersonation events are audited separately in `MemberAudit`, with `SrcIP` and `UserAgent`. · Observed · `_lucernex_objects_summary.txt`.**

|  |  |
|---|---|
| Stated as | Login, lockout and impersonation events are audited separately in `MemberAudit`, with `SrcIP` and `UserAgent`. |
| Stated as | Observed |
| Stated as | `_lucernex_objects_summary.txt` |

### E Audit reporting — [RPT-R-043](../rules/RPT-R-043.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**The Audit Log dialog is a generic viewer over `AuditColumn`, reachable from an individual record's editor — not only from a central Audit Reports screen. · Derived · 007.**

|  |  |
|---|---|
| Stated as | The Audit Log dialog is a generic viewer over `AuditColumn`, reachable from an individual record's editor — not only from a central Audit Reports screen. |
| Stated as | Derived |
| Stated as | 007 |

### F Security — [RPT-R-050](../rules/RPT-R-050.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Report access is granted per user class through `UserClassSecurity.PageLayoutID`, alongside grants on fields (`ReportGroupAvailableFieldID`), field groups (`ReportGroupDataID`) and dashboard components. · Observed · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Report access is granted per user class through `UserClassSecurity.PageLayoutID`, alongside grants on fields (`ReportGroupAvailableFieldID`), field groups (`ReportGroupDataID`) and dashboard components. |
| Stated as | Observed |
| Stated as | `all-fields.csv` |

### F Security — [RPT-R-051](../rules/RPT-R-051.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**Dashboard tiles are secured by title string (`UserClassSecurity.DashboardComponentTitle`), not by record id. Renaming a tile therefore breaks its grants.**

|  |  |
|---|---|
| Stated as | Dashboard tiles are secured by title string (`UserClassSecurity.DashboardComponentTitle`), not by record id. Renaming a tile therefore breaks its grants. |
| Stated as | Observed (column) + Inferred (consequence) |
| Stated as | `all-fields.csv` |

### F Security — [RPT-R-052](../rules/RPT-R-052.md)

*Inferred · rule · source: `docs/modules/reporting/rules.md`*

**Granting on a registry group node means report-field permissions inherit down the catalog tree, not per-field only. · Inferred (high) · `all-fields.csv`.**

|  |  |
|---|---|
| Stated as | Granting on a registry group node means report-field permissions inherit down the catalog tree, not per-field only. |
| Stated as | Inferred (high) |
| Stated as | `all-fields.csv` |

### F Security — [RPT-R-053](../rules/RPT-R-053.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**[BLOCKED] Whether Portfolio/Capital-Program scoping filters report rows at the query level or only hides values in the UI is unresolved — the same question 007 raises for dropdown values. Check: run a report as a portfolio-restricted user.**

|  |  |
|---|---|
| Stated as | [BLOCKED] Whether Portfolio/Capital-Program scoping filters report rows at the query level or only hides values in the UI is unresolved — the same question 007 raises for dropdown values. Check: run a report as a portfolio-restricted user. |
| Stated as | Open |
| Stated as | 007 |

### G Bulk data movement — [RPT-R-060](../rules/RPT-R-060.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**The field catalog itself is exportable and importable as a spreadsheet, scope-aware: `DocumentDownload?type=RGAFSpreadsheet&readOnly=true&isGlobal={true\ · false}`. · Observed · 005.**

|  |  |
|---|---|
| Stated as | The field catalog itself is exportable and importable as a spreadsheet, scope-aware: `DocumentDownload?type=RGAFSpreadsheet&readOnly=true&isGlobal={true\ |
| Stated as | false}`. |
| Stated as | Observed |
| Stated as | 005 |

### G Bulk data movement — [RPT-R-061](../rules/RPT-R-061.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**An exported catalog spreadsheet is single-use: "Once a spreadsheet is imported the same spreadsheet cannot be used again. You would have to create a new spreadsheet using 'Export Data Fields' button." This implies a nonce or version stamp inside the workbook.**

|  |  |
|---|---|
| Stated as | An exported catalog spreadsheet is single-use: "Once a spreadsheet is imported the same spreadsheet cannot be used again. You would have to create a new spreadsheet using 'Export Data Fields' button." This implies a nonce or version stamp inside the workbook. |
| Stated as | Observed (instruction text) + Inferred (mechanism) |
| Stated as | 005 |

### G Bulk data movement — [RPT-R-062](../rules/RPT-R-062.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**The bulk-change instruction block is shown in Firm scope but not in Global scope. Reason unknown.**

|  |  |
|---|---|
| Stated as | The bulk-change instruction block is shown in Firm scope but not in Global scope. Reason unknown. |
| Stated as | Observed |
| Stated as | 005 |

### G Bulk data movement — [RPT-R-063](../rules/RPT-R-063.md)

*Observed · rule · source: `docs/modules/reporting/rules.md`*

**ASG requires a report-to-import round trip (export a report to Excel, edit, re-import to update records), priority Critical. Lx's catalog export/import is field metadata only;.**

|  |  |
|---|---|
| Stated as | ASG requires a report-to-import round trip (export a report to Excel, edit, re-import to update records), priority Critical. Lx's catalog export/import is field metadata only; no equivalent for report data was found. |
| Stated as | Observed (requirement) + Derived (absence) |
| Stated as | `_xlsx_feature_list.txt` line 244 |

### H Requirements ASG — [RPT-R-070](../rules/RPT-R-070.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**Restrict edit access to standard reports (e.g. ASC 842) to prevent breakage, while allowing runtime filters to view specific data · Blocker · 242.**

|  |  |
|---|---|
| Stated as | Restrict edit access to standard reports (e.g. ASC 842) to prevent breakage, while allowing runtime filters to view specific data |
| Stated as | Blocker |
| Stated as | 242 |

### H Requirements ASG — [RPT-R-071](../rules/RPT-R-071.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**"Save As" personal reports — a user copy that does not affect the global standard · Critical · 243.**

|  |  |
|---|---|
| Stated as | "Save As" personal reports — a user copy that does not affect the global standard |
| Stated as | Critical |
| Stated as | 243 |

### H Requirements ASG — [RPT-R-072](../rules/RPT-R-072.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**Report-to-import workflow — export to Excel, modify, re-import to update the system · Critical · 244.**

|  |  |
|---|---|
| Stated as | Report-to-import workflow — export to Excel, modify, re-import to update the system |
| Stated as | Critical |
| Stated as | 244 |

### H Requirements ASG — [RPT-R-073](../rules/RPT-R-073.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**Scheduled & external delivery — email to recipients including non-users, or encrypted SFTP · Major · 245.**

|  |  |
|---|---|
| Stated as | Scheduled & external delivery — email to recipients including non-users, or encrypted SFTP |
| Stated as | Major |
| Stated as | 245 |

### H Requirements ASG — [RPT-R-074](../rules/RPT-R-074.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**Multi-tenancy / global management — a Global Admin view; today an admin logs into 21 instances separately · Critical · 246, 248.**

|  |  |
|---|---|
| Stated as | Multi-tenancy / global management — a Global Admin view; today an admin logs into 21 instances separately |
| Stated as | Critical |
| Stated as | 246, 248 |

### H Requirements ASG — [RPT-R-075](../rules/RPT-R-075.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**Job log visibility — an at-a-glance status board for scheduled jobs, not a click-away list; blank reports are being sent unnoticed · — · 247.**

|  |  |
|---|---|
| Stated as | Job log visibility — an at-a-glance status board for scheduled jobs, not a click-away list; blank reports are being sent unnoticed |
| Stated as | — |
| Stated as | 247 |

### H Requirements ASG — [RPT-R-076](../rules/RPT-R-076.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**Readable audit logs — "Audit tools are just raw links. User has to go look for logs manually in the table and infer on its own." ASG explicitly does not use Generate Enterprise Report File · — · 241.**

|  |  |
|---|---|
| Stated as | Readable audit logs — "Audit tools are just raw links. User has to go look for logs manually in the table and infer on its own." ASG explicitly does not use Generate Enterprise Report File |
| Stated as | — |
| Stated as | 241 |

### H Requirements ASG — [RPT-R-077](../rules/RPT-R-077.md)

*Derived · rule · source: `docs/modules/reporting/rules.md`*

**Bulk action confirmation — preview changes before executing a bulk import, with rollback visibility · Critical · 250.**

|  |  |
|---|---|
| Stated as | Bulk action confirmation — preview changes before executing a bulk import, with rollback visibility |
| Stated as | Critical |
| Stated as | 250 |
