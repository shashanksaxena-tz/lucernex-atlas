# The code-table registry — all 207 Firm Drop Downs, with their type IDs

**Stated up front.** Lucernex has one generic code-table editor, `FirmCodeEdit.jsp`, discriminated
by a numeric `TableType`. The 207 platform-defined "Firm Drop Downs" are simply 207 values of that
discriminator. Two things follow, and both matter more than the catalogue itself:

1. **`TableType=2035` is `Issue Type Code`** — and `Manage Forms` opens
   `FirmCodeEdit.jsp?includeType=Manage&TableType=2035&tableName=Manage Forms`. **A "Form" is an
   Issue Type.** The four form types are four rows in the Issue Type code table, and the record a
   form produces is an `Issue`.
2. **The IDs fall in two bands**, 2000–2190 and 3000–3016, and the split is not arbitrary. The
   3000-band tables are the ones whose rows carry *behaviour* (`CodeExpenseType` has 31 fields
   including schedule-routing foreign keys); the 2000-band are mostly plain lookups.

Captured 2026-09-10 from `/en/admin/FirmCodeList.jsp`, tenant `(ASG)American Freight`, build
`26.08.0.46`. Read-only: no code table or value was created, edited or deleted.
Confidence: **Observed** throughout unless stated.

## Why "a Form is an Issue Type" is the important finding

[`forms-vs-pages-vs-layouts.md`](../modules/layouts-and-forms/forms-vs-pages-vs-layouts.md)
established that a Form is a tenant-defined request type with its own fields, its own layout per
workflow step, and an entity-attachability matrix. This document supplies the missing piece: the
*record* those forms create is not a new bespoke table. It is an **`Issue`**.

Every previously loose observation now lines up:

| Observation | Explained by |
|---|---|
| Form types carry a `Sequence Prefix` (`ASR`, `LAR`, `RPR`) and `Global Sequence Numbers?` | `Issue` carries `SequenceNumber`; issues are numbered tickets |
| Form types declare attachability per entity kind | `Issue` hangs off `ProjectEntity`, the universal supertype |
| Form types report `WORK FLOW field set? = Yes` | `Issue` is what a workflow routes |
| `Auto close`, `Allow Reply` | ticket lifecycle properties |
| GraphQL declares an `IssueInterface` | `Issue` is a supertype with variants |
| `InvoiceIssue` (23 fields) and `BidderIssue` (21 fields) exist as separate objects | those are two more Issue variants, for invoicing and bidding |
| `CodeIssueType` exists as an object with 19 fields | the code table behind `TableType=2035` |
| `Issue` has 56 fields — far more than a simple lookup | it is the generic unit-of-work record for the whole product |

**Derived:** Lucernex did not build a form builder. It built one ticket type (`Issue`), made its
subtype a code-table value, gave each subtype its own user-defined fields and a layout per workflow
step, and got a form builder for free. That is a genuinely economical design and ASG Edge+ should
consider copying it rather than modelling each request type as its own aggregate.

The corollary is a warning: **every request-shaped feature in this product is the same table.** A
rebuild that gives Lease Admin Requests, Rent Payment approvals, invoice disputes and bid questions
four separate models will need four separate workflow engines. Lucernex needs one.

## The two ID bands

**Derived**, from cross-referencing the ID band against each code table's object in
`_lucernex_objects_summary.txt`.

| Band | Count | Character |
|---|---:|---|
| `2000`–`2190` | 190 | Mostly plain lookups: a short name, a long name, an inactive flag. Values classify a record but do not drive computation. |
| `3000`–`3016` | 17 | Behaviour-bearing. These are the `* Type Code` tables whose rows carry configuration that the engines read. |

The 3000-band, in full: Asset Type, Problem, Amendment Type, Contract Type, Covenant Type, Facility
Type, Key Date Type, Location Type, Parcel Type, Usage Group, Usage Type, Responsibility Type, Sales
Type, **Expense Type**, Parcel Access Type, Recovery Type, Recovery Item Type.

`Expense Type` (`3013`) is the one to study first. Its object `CodeExpenseType` carries 31 fields
including `CodeSLScheduleID`, `CodeASC842ScheduleID` and `CodeIFRS16ScheduleID` — meaning **an
administrator choosing an expense type is choosing which accounting schedules that money flows
into.** A code-table row is a routing decision, not a label. See
[`../modules/accounting/README.md`](../modules/accounting/README.md).

## Accounting-relevant code tables

Worth calling out because they are the configuration surface of the accounting engine:

| ID | Code table |
|---:|---|
| 2160 | Schedule Creation Reason Code |
| **2161** | **Straight Line Schedule Type Code** |
| **2162** | **ASC 842 Schedule Type Code** |
| **2163** | **IFRS 16 Schedule Type Code** |
| 2164 | Cap Type Code |
| 2165–2167 | Escalation Category / Group / Type Code |
| 2168 | Exp Rec Based On Code |
| 2169–2171 | Index Group / Source / Type Code |
| 2086 | Base Year Amount Type Code |
| 2098 | Denominator Code |
| 2131 | Pass Through Type Code |
| 2139 | Pro Rata Share Method Code |
| 2179–2180 | Recovery Group / Recovery Item Group Code |
| 2182 | Adjustment Method Code |
| 2183 | Exclusion Cap Code |
| 3013 | Expense Type Code |
| 3015–3016 | Recovery Type / Recovery Item Type Code |

## Captured values

Four code tables were opened directly. All **Observed**, 2026-09-10.

### `2162` ASC 842 Schedule Type Code — **1 value**

Columns: `Type*`, `Description`, `Don't Amortize Asset Value`, `Inactive`.

| Type | Description | Don't Amortize Asset Value | Inactive |
|---|---|---|---|
| `842 Rent` | 842 Rent | no | no |

### `2161` Straight Line Schedule Type Code — **empty**

"No rows to display." Same four columns.

### `2163` IFRS 16 Schedule Type Code — **empty**

"No rows to display." Same four columns.

**Derived, and important for the rebuild scope:** this tenant runs **ASC 842 only**, through a single
schedule type. IFRS 16 is not configured at all, and no legacy straight-line schedule type exists
either. The engine supports all three standards — the three code tables are structurally identical,
exactly as `docs/modules/accounting/README.md` predicted — but ASG uses one.

That is a scoping fact worth confirming with the business before ASG Edge+ builds IFRS 16. The
capability is present in the incumbent and unused. It also means any migration will carry exactly
one schedule type across, not a matrix.

### `2094` Contract Status Code — **3 values**

Columns: `Name`, `Description`, `Inactive`.

| Name | Description | Row actions |
|---|---|---|
| `AI Abstracted` | AI Abstracted | edit, delete |
| `Active` | Active | **edit only — no delete** |
| `Inactive` | Inactive | edit, delete |

Two observations here.

**`Active` cannot be deleted.** It is the only one of the three without a `delete` action, which
means the platform protects at least one status value as system-required. A rebuild needs the same
notion of an undeletable seeded value, and it interacts directly with ASG Edge+'s `D-07` /
`DeactivationPolicy` question.

**`AI Abstracted` is a tenant-added status.** ASG has extended the contract lifecycle to record that
a contract was abstracted by AI rather than by a person. This is not in any BRD reviewed so far and
is worth raising — it says the abstraction process already has an automated path in production, and
the rebuild's Lease Admin Request workflow (whose step 2 is "Abstract Lease Document") will need to
represent the same distinction.

### The contract lifecycle — resolved

The apparent gap against BRD-24 has been traced, and the answer changes where the rebuild should
look.

`docs/contracts-explained.html` describes a lifecycle of Open → Active → Possession → Paying Rent →
Closed, taken from the BRD. `Contract Status Code`'s three values do not contain any of those. The
resolution is that **contract lifecycle does not live in `Contract Status Code` at all.**

The `ASG Contract Summary` layout carries **two** required status fields side by side —
`Contract Status *` and `Lease Status *` (**Observed**, layout `PageLayoutID=96289`). Following
`Lease Status` leads somewhere unexpected: not to the platform `Lease Status Code` table (2043),
which holds a single value, `Expired`, but to a **tenant-authored Client Drop Down of the same
name**. This is the naming duplication [007](../admin/007-firm-and-client-drop-downs.md) flagged,
and it turns out to matter enormously.

**Client Drop Down `Lease Status` — 9 values** (**Observed**, `CustomCodeTableEdit.jsp`):

| Value | Reading |
|---|---|
| `Open` | Deal signed, nothing occupied yet |
| `Future Possession` | Possession scheduled but not taken |
| `Possession` | Space held, rent not yet running |
| `Possession - Paying Rent` | Space held and rent running |
| `Active` | The steady state |
| `Closed - Active` | Closed but still carrying activity |
| `Closed` | Terminated |
| `Accounting Purposes Only` | Carried for accounting, not operationally live |
| `Accounting Purposes Only: Close…` | A second accounting-only variant (label truncated in the grid) |

![The tenant-authored Lease Status drop-down and its values](../assets/screenshots/drop-downs/client-lease-status-values.jpg)

**This is BRD-24's lifecycle**, and then some. Open → Future Possession → Possession →
Possession - Paying Rent → Active → Closed maps directly onto the BRD's
Open → Active → Possession → Paying Rent → Closed, with the BRD's five states expanded to nine.

Three consequences for ASG Edge+, and they are significant:

1. **The lifecycle is tenant data, not platform schema.** Nine states that a rebuild would naturally
   model as an enum are, in Lucernex, rows in a customer-editable drop-down. Anyone at ASG with
   drop-down rights can add a tenth state or rename `Active`, and nothing in the platform would
   object. Whether Edge+ keeps that flexibility or hard-codes the state machine is a real decision
   and it should be made deliberately rather than inherited.
2. **`Contract Status` and `Lease Status` are different concepts.** `Contract Status` (3 platform
   values, `Active` undeletable) is a coarse record-level flag — is this row live, retired, or
   machine-abstracted. `Lease Status` (9 tenant values) is the operational lifecycle. A rebuild that
   collapses them into one field will lose information that ASG uses today.
3. **The BRD is describing real behaviour**, not aspiration. That is reassuring for BRD-24's other
   claims, and it means the earlier note in `docs/contracts-explained.html` needs no correction —
   only a pointer to where the states actually live.

The two `Accounting Purposes Only` variants have no counterpart in the BRD and are worth asking
about: they suggest contracts that exist for ASC 842 measurement while being operationally dormant,
which the accounting engine would need to treat differently.

## A negative result worth recording

**`Work Flow Status Code` is not among the 207.** `docs/modules/workflow/state-machine.md` assumed
it was one of the fixed Firm Drop Downs and therefore capturable here. It is not in the catalogue,
so its values cannot be read from this screen.

The nearest candidates present are `Approval Status Code` (2081), `Last Action Status Code` (2082)
and `Decision Status Code` (2025). **Inferred:** workflow status is likely a platform-internal
enumeration not exposed for tenant editing at all, which would be consistent with it governing
engine behaviour rather than presentation. This remains open — see the open questions.

## The full catalogue

```
2000  Appointment Type Code              2098  Denominator Code
2001  Asset Department Code              2099  Escalation Payment Method Code
2002  Asset Group Code                   2100  Evaluation Rating Code
2003  Asset Operation Status Code        2101  Exchange Rate Type Code
2004  Asset Product Type Code            2102  Expense Acct Code
2005  Asset Suspension Status Code       2103  Expense Category Code
2006  Budget Change Reason Code          2104  Expense Group Code
2007  Budget Column Status Code          2105  Facility Category Code
2008  Budget Value Units Code            2106  Facility Group Code
2009  Building Area Unit Code            2107  Facility Status Code
2010  Building Class Code                2108  Facility Use Code
2011  CAM Category Code                  2109  Financial Adjustment Status Code
2012  Change Department Code             2110  Guarantee Type Code
2013  Change Package Type Code           2111  Holding Interest Code
2014  Issue/RFI/Proposed Change Cause    2112  Insurance Group Code
2015  Change Source Code                 2113  Insurance Type Code
2016  Change Type Code                   2114  Key Date Group Code
2017  Classification Code                2115  Legal Classification Code
2018  Competitor Type Code               2116  Location Category Code
2019  Complex Status Code                2117  Location Group Code
2020  Complex Type Code                  2118  Location Status Code
2021  Construction Type Code             2119  Location Use Code
2022  Contact Type Code                  2120  Org Category Code
2023  Coverage Code                      2121  Org Group Code
2024  Deal Type Code                     2122  Org Type Code
2025  Decision Status Code               2123  Parcel Category Code
2026  Demographic Results Type Code      2124  Parcel Group Code
2027  Discipline Code                    2125  Parcel Status Code
2028  Distribution Center Code           2126  Parcel Use Code
2029  Document Content Code              2127  Parking Group Code
2030  Document Type Code                 2128  Parking Type Code
2031  Funding Type Code                  2129  Party Group Code
2032  Inspection Period Start Code       2130  Party Type Code
2033  Inspection Type Code               2131  Pass Through Type Code
2034  Insurance Policy Type Code         2132  Payment Method Code
2035  Issue Type Code  << Manage Forms   2133  Unit Sales Type Code
2036  Invoice Status Code                2134  Usage Unit Type Code
2037  Job Function Code                  2135  Usage Category Code
2038  Job Title Code                     2136  Use Rent Model Type Code
2039  Land Area Unit Code                2137  CPI Index Code
2040  Lease Co Tenant Type Code          2138  Plan Forecast Group Code
2041  Lease Option Other Type Code       2139  Pro Rata Share Method Code
2042  Lease Option Type Code             2140  Rating Code
2043  Lease Status Code                  2141  Region Code
2044  Lease Type Code                    2142  Responsibility Group Code
2045  Location Access Code               2143  Sales Category Code
2046  Location Code                      2144  Sales Group Code
2047  Asset Category Code                2145  Security Deposit Group Code
2048  Maintenance Remedy Code            2146  Security Deposit Type Code
2049  Market Area Code                   2147  Space Group Code
2050  Market Demographics Code           2148  Space Status Code
2051  Market Type Code                   2149  Space Type Code
2052  Master Employer Group Code         2150  Space Use Code
2053  Misc Expense Category Code         2151  Tenant Category Code
2054  Pro Forma Budget Status Code       2152  Tenant Group Code
2055  Project Type Code                  2153  Tenant Status Code
2056  Property Primary Use Code          2154  Tenant Type Code
2057  RE Transaction Status Code         2155  Tenant Use Code
2058  Responsible Party Code             2156  Covenant Category Code
2059  Scenario Deal Type Code            2157  Covenant Status Code
2060  Scenario Type Code                 2158  Key Date Action Code
2061  Security Privilege Code            2159  Term Type Code
2062  Service Type Code                  2160  Schedule Creation Reason Code
2063  Site Rating Code                   2161  Straight Line Schedule Type Code
2064  Slot Type Code                     2162  ASC 842 Schedule Type Code
2065  SRQ Source Code                    2163  IFRS 16 Schedule Type Code
2066  SRQ Status Code                    2164  Cap Type Code
2067  SRQ Type Code                      2165  Escalation Category Code
2068  Store Phase Code                   2166  Escalation Group Code
2069  Tax Category Code                  2167  Escalation Type Code
2070  User Class Code                    2168  Exp Rec Based On Code
2071  Utility Category Code              2169  Index Group Code
2072  Vendor Grade Code                  2170  Index Source Code
2073  Vertical Industry Code             2171  Index Type Code
2074  Zoning Code                        2172  Source Entity Code
2075  Address Group Code                 2173  Insurance Category Code
2076  Address Type Code                  2174  Store Type Code
2077  Agreement Type Code                2175  Offset Group Code
2078  Allowance Group Code               2176  Offset Type Code
2079  Allowance Type Code                2177  Parcel Access Category Code
2080  Amendment Group Code               2178  Parcel Access Group Code
2081  Approval Status Code               2179  Recovery Group Code
2082  Last Action Status Code            2180  Recovery Item Group Code
2083  Area Code                          2181  Security Deposit Status Code
2084  Asset Class Code                   2182  Adjustment Method Code
2085  Asset Type Test Code               2183  Exclusion Cap Code
2086  Base Year Amount Type Code         2184  Property Tax Status Code
2087  Co Tenancy Group Code              2185  Property Tax Type Code
2088  Co Tenancy Type Code               2186  Tax Appeal Result Code
2089  Company Group Code                 2187  Tax Appeal Status Code
2091  Concept Code                       2188  Tax Paid To Code
2092  Contract Category Code             2189  Tax Refund Type Code
2093  Contract Group Code                2190  Tax Type Code
2094  Contract Status Code
2095  Contract Use Code                  3000  Asset Type Code
2096  Covenant Group Code                3001  Problem Code
2097  Covenant Template Code             3002  Amendment Type Code
                                         3003  Contract Type Code
                                         3004  Covenant Type Code
                                         3005  Facility Type Code
                                         3006  Key Date Type Code
                                         3007  Location Type Code
                                         3008  Parcel Type Code
                                         3009  Usage Group Code
                                         3010  Usage Type Code
                                         3011  Responsibility Type Code
                                         3012  Sales Type Code
                                         3013  Expense Type Code
                                         3014  Parcel Access Type Code
                                         3015  Recovery Type Code
                                         3016  Recovery Item Type Code
```

`2090` is absent from the sequence. **Inferred:** a retired code table; the discriminator is a fixed
platform enumeration, so gaps are expected where a table was withdrawn.

## Notes for ASG Edge+ Masters (MDM-01)

- This catalogue is the closest thing to a definitive answer to "what masters does the incumbent
  system have?". 207 platform-fixed tables plus an unbounded number of tenant-authored Client Drop
  Downs ([007](../admin/007-firm-and-client-drop-downs.md)).
- **The platform catalogue is fixed and the tenant cannot extend it.** A tenant may edit the *values*
  in a Firm Drop Down but cannot add a new Firm Drop Down. New tenant-specific masters go into
  Client Drop Downs, a structurally different mechanism. ASG Edge+'s Global/Firm split needs to make
  the same distinction deliberately, and D-01's central-push model should be checked against it.
- **Naming collisions already exist in this tenant.** `Lease Status Code` (2043, platform) sits
  alongside a tenant-authored `Lease Status` Client Drop Down. Any migration has to disambiguate.
- The 3000-band's behaviour-bearing rows are the ones that cannot be modelled as a simple
  `(code, label, active)` triple. Size the Masters model for them, not for the 2000-band.

## Open questions

1. **What are the values in `Straight Line Schedule Type Code`, `ASC 842 Schedule Type Code` and
   `IFRS 16 Schedule Type Code`?** These are the accounting engine's configuration surface and each
   value carries 20 `ExportAcctNNumber` GL slots. Opening 2161/2162/2163 would settle a large part
   of `docs/modules/accounting/asc-842.md`'s open questions.
2. **What are the values in `Contract Status Code` (2094)?** Needed for the contract lifecycle state
   machine.
3. **Where does workflow status actually live**, given `Work Flow Status Code` is not in this
   catalogue?
4. **Confirm the 2000/3000 band distinction** by checking every 3000-band table's object for
   behaviour-bearing columns. The claim currently rests on `CodeExpenseType` plus the naming pattern.
5. **What is `Source Entity Code` (2172)?** It appears alongside `AccrualTransaction.SourceEntityTable`,
   suggesting a polymorphic-association discriminator — which would be a second soft-reference
   mechanism worth understanding.
