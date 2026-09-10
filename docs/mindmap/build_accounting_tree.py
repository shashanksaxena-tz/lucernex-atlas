# -*- coding: utf-8 -*-
"""
Builds docs/mindmap/accounting-tree.json — the accounting module rendered as a nested
tree for the interactive mind map.

Re-runnable from the repository root:   python3 docs/mindmap/build_accounting_tree.py

Node schema: {name, kind, detail, confidence, source, children}
  kind        module | submodule | capability | entity | field-group | field |
              type | rule | constraint | code-table | code-value
  confidence  observed | derived | inferred   (docs/CONVENTIONS.md)
  detail      plain language, written for a reader who does not know lease accounting
  source      the file or route the fact came from

The script asserts every node's kind and confidence are in the allowed vocabulary and
that no node has an empty name, detail or source, so a malformed edit fails the build
rather than reaching the artifact. It prints depth and node counts per spine.

Every ACC-R-NNN rule in docs/modules/accounting/rules.md hangs off the entity or
capability it governs, so the map doubles as a rule browser. All 62 are present.
"""
import json, io

OBJ   = "_lucernex_objects_summary.txt"
JCREW = "_xlsx_lucernex_jcrew.txt (vendor field definitions)"
CSV   = "docs/data-fields/all-fields.csv"
IDX   = "docs/data-fields/INDEX.md (field-type legend)"
GQL   = "docs/data-model/graphql-api.md (live GraphQL schema, build 26.08.0.46, 2026-09-10)"
WF    = "docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md (live tenant, 2026-09-10)"
ADM4  = "docs/admin/004-company-administration.md"
DASH  = "docs/screens/001-dashboard-home.md"
RUL   = "docs/modules/accounting/rules.md"
DM    = "docs/modules/accounting/data-model.md"
SL    = "docs/modules/accounting/straight-line.md"
A842  = "docs/modules/accounting/asc-842.md"
IF16  = "docs/modules/accounting/ifrs-16.md"
CVI   = "docs/modules/accounting/computed-vs-input-fields.md"
MAP   = "docs/modules/accounting/asg-edgeplus-mapping.md"
REG   = "docs/data-model/code-table-registry.md (live tenant, 2026-09-10)"
BRD   = "KnowledgeFolder/ProjectProposals/ASG Edge Plus/Source/_md_cache/ASG_Gen_accounting engine.md"

def n(name, kind, detail, confidence, source, children=None):
    detail = " ".join(detail.split()).strip()
    d = {"name": name, "kind": kind, "detail": detail,
         "confidence": confidence, "source": source,
         "children": children or []}
    return d

def rule(rid, title, detail, confidence, extra_source=None):
    return n("%s — %s" % (rid, title), "rule", detail, confidence, extra_source or RUL)

# ---------------------------------------------------------------- SPINE 1
spine1 = n(
 "Straight-line & accounting schedules", "submodule",
 "The calculation half of the engine. One pair of tables — a schedule header and one row per "
 "accounting period — produces every lease schedule the product makes, whether it is a legacy "
 "straight-line schedule, an ASC 842 schedule or an IFRS 16 schedule. The name is historical: "
 "'straight-line' was the old accounting method, but the tables outlived it.",
 "observed", OBJ,
 [
  n("SLSummary — the schedule header", "entity",
    "One row per accounting schedule. 134 fields in the object export (135 in the field catalog). "
    "Holds the assumptions the schedule was built under, the opening balances, every present-value "
    "adjustment, the deltas against any schedule it replaced, and two blocks of pre-computed "
    "disclosure figures. Physical table: s_l_summary.",
    "observed", OBJ,
    [
     # --- L4 field groups ---
     n("Schedule identity flags", "field-group",
       "Three independent yes/no flags that say which accounting standard this schedule was "
       "generated under. They are the only thing distinguishing a straight-line schedule from an "
       "ASC 842 one — the columns, the arithmetic and the period rows are otherwise identical. "
       "Nothing in the database stops two of them being true at once.",
       "observed", CSV,
       [
        n("IsASC842Schedule", "field",
          "'Is ASC 842 Schedule?' — set when the schedule was produced by the Generate 842 Rent "
          "Schedule button. Vendor definition: \"This flag indicates that the schedule is an ASC 842 "
          "schedule.\" It is written by the system, not ticked by a user.",
          "observed", JCREW,
          [
           n("CodeASC842Schedule — the schedule-type table it implies (TableType 2162)", "code-table",
             "A schedule flagged as ASC 842 must point at a row in this tenant-defined table via "
             "CodeASC842ScheduleID. The table is what actually connects the calculation to the "
             "customer's general ledger. 24 columns, of which only four carry meaning and twenty "
             "are numbered account slots. Its IFRS 16 and straight-line twins are byte-identical "
             "in shape — confirmed from the admin screen, where all three render the same four "
             "columns. Physical table: code_a_s_c842_schedule.",
             "observed", OBJ,
             [
              n("842 Rent — the only configured schedule type", "code-value",
                "Opened directly in the tenant on 2026-09-10: this table holds exactly one row. Type "
                "'842 Rent', description '842 Rent', Don't Amortize Asset Value unchecked, Inactive "
                "unchecked. So every ASC 842 schedule in the tenant routes through this one "
                "configuration, and there is exactly one set of twenty general-ledger slots in play — "
                "not a matrix. That makes a migration substantially simpler than the schema suggested.",
                "observed", REG,
                [
                 n("GL export account slots (ExportAcct1Number … ExportAcct20Number)", "field-group",
                   "Twenty free-text columns holding general-ledger account numbers. Vendor definition, "
                   "repeated on all twenty: \"Export Accounts are tied to GL accounts in your Enterprise "
                   "Resource Planning (ERP) System.\" When a schedule is generated, all twenty values are "
                   "copied verbatim onto every single period row, so a 120-month lease carries 2,400 "
                   "copies of the same twenty numbers.",
                   "observed", JCREW,
                   [
                    n("ExportAcct1Number", "field",
                      "The first GL account slot. Which accounting concept it represents — lease "
                      "liability, ROU asset, interest expense, amortisation — is not recorded anywhere "
                      "in the schema. The slot is numbered, not named.",
                      "observed", OBJ,
                      [
                       n("Text, max length 50", "type",
                         "Lucernex type 'Text'; catalog type sTYPE_TEXT; stored in PostgreSQL as TEXT. "
                         "An account number is a label, not a quantity, so text is the right choice here "
                         "— unlike the currency columns, which are also TEXT and should not be.",
                         "observed", JCREW),
                       n("The slot number is not a name", "constraint",
                         "Nothing in the data model says what slot 1 means. Twenty unnamed slots, and "
                         "the mapping from slot to accounting concept is pure tenant convention held "
                         "outside the system. It must be recovered before any ERP export can be "
                         "rebuilt — and because only one schedule type is configured, that is now a "
                         "single row of twenty values to read rather than a survey. It is also why "
                         "ASG Edge+ should replace numbered slots with named debit/credit mapping "
                         "rules.",
                         "derived", MAP),
                       rule("ACC-R-029", "GL account denormalization",
                            "On creating each period row, the schedule type's twenty account numbers are "
                            "copied onto it unchanged.", "derived"),
                      ]),
                   ]),
                 n("DontAmortizeAssetValue", "field",
                   "The only behaviour switch on the entire table. A yes/no flag whose name says it "
                   "suppresses amortisation of the right-of-use asset for schedules of this type. "
                   "It has no vendor definition anywhere, so what exactly it suppresses is unconfirmed.",
                   "observed", OBJ,
                   [
                    n("Unchecked on the only configured row — so it does nothing here", "constraint",
                      "The single ASC 842 schedule type, 842 Rent, has this flag off, and the other "
                      "two schedule-type tables are empty. The flag therefore has no observable "
                      "effect anywhere in this tenant's data, so the rule below can never be "
                      "validated against it and stays permanently a guess. A rebuild should either "
                      "implement it from the accounting standard and flag the divergence risk, or "
                      "leave it out and record the omission — but should not claim parity on it.",
                      "observed", REG),
                    rule("ACC-R-030", "Suppress ROU asset amortization",
                         "If the flag is set, no asset amortisation is recognised. Inferred from the "
                         "field name — the only rule in the module resting on naming alone, and now "
                         "known to be inert in production.", "inferred"),
                   ]),
                 n("ShortName / ActualLongName / Inactive", "field-group",
                   "The three generic code-table columns every Lucernex drop-down carries: the short "
                   "label shown in the list, a long description, and a soft-delete flag. They are absent "
                   "from the Manage Data Fields catalog, which only exposes the twenty account slots "
                   "and the amortisation switch.",
                   "observed", OBJ),
                ]),
             ]),
           n("BOOLEAN (canonical) / sTYPE_CHECKBOX (presentation)", "type",
             "A yes/no value. Lucernex's live API declares a ten-value canonical type system in which "
             "BOOLEAN is one entry; the 448 sTYPE_* codes in Manage Data Fields are a presentation "
             "layer over it.",
             "observed", GQL),
          ]),
        n("IsIFRS16Schedule", "field",
          "'Is IFRS 16 Schedule?' — the same flag for the international standard, pointing at the "
          "structurally identical CodeIFRS16Schedule table.",
          "observed", JCREW),
        n("IsSLSchedule", "field",
          "'Is SL Schedule?' — the legacy straight-line flag, kept alongside the two newer standards "
          "rather than replaced by them.",
          "observed", JCREW),
        n("Only one of the three is usable in this tenant", "constraint",
          "The ASC 842 schedule-type table holds one row; the straight-line and IFRS 16 tables are "
          "both empty. With nothing to point at, no straight-line or IFRS 16 schedule can be "
          "generated — so IsSLSchedule and IsIFRS16Schedule should be false on every row. Any row "
          "where one of them is true is an orphan whose schedule type was deleted, and it would "
          "still be carrying balances. A one-query data-integrity check with real migration "
          "consequences.",
          "observed", REG),
        n("Three independent booleans, no uniqueness rule", "constraint",
          "These are three separate yes/no columns, not one 'which standard' choice. The database "
          "does not prevent two being true on one schedule, nor two active ASC 842 schedules on one "
          "contract. ASG Edge+ should replace them with a single standard enum plus a uniqueness "
          "constraint.",
          "derived", MAP),
       ]),

     n("Opening balances", "field-group",
       "What the lease is worth on the books the day the schedule starts: the liability owed to the "
       "landlord, and the right-of-use asset that mirrors it.",
       "observed", CSV,
       [
        n("InitialLiabilityBalance", "field",
          "The lease liability at the accounting begin date. Vendor definition: \"This is the total of "
          "all of the Period Payment Present Values over the life of the lease\" — i.e. every future "
          "rent payment discounted back to today and added up.",
          "observed", JCREW,
          [
           n("MONEY (canonical) / sTYPE_MONEY (presentation)", "type",
             "A currency amount. Declared maximum 999,999,999,999,999 — fifteen digits — with no "
             "declared decimal scale. Lucernex's live API keeps MONEY distinct from FLOAT and "
             "publishes BigDecimal as a scalar, so the vendor does not treat money as a float either.",
             "observed", GQL,
             [
              n("Stored in PostgreSQL as TEXT", "constraint",
                "Every non-key column in the customer database export is TEXT, currency included. "
                "There is no numeric typing to inherit and no database guarantee that a currency "
                "column even contains a number. Every migrated value must be parsed, and each parse "
                "failure is a data-quality finding rather than an error to swallow.",
                "observed", JCREW),
             ]),
           rule("ACC-R-031", "Initial liability balance",
                "Sum the present value of every period's cash payment across the life of the lease.",
                "observed"),
          ]),
        n("InitialAssetBalance", "field",
          "The right-of-use asset at the accounting begin date. Vendor definition says only \"This is a "
          "calculated value which contains the initial value over the asset of the lease\" — the actual "
          "arithmetic is documented nowhere.",
          "observed", JCREW,
          [
           n("The formula is missing", "constraint",
             "Every ingredient exists as its own field — initial direct costs, lease incentives, "
             "pre-commencement payments, dismantling costs, a manual adjustment — but no source states "
             "how they combine. This is the single most important undocumented computation in the "
             "module and it blocks the measurement service in any rebuild.",
             "observed", A842),
           rule("ACC-R-033", "Initial asset balance",
                "Standard practice is liability + prepaid rent + initial direct costs − lease "
                "incentives, and all four fields exist, but the actual formula is not stated. Do not "
                "code from the schema alone.", "inferred"),
          ]),
        n("BalanceForward", "field",
          "When a schedule replaces an earlier one, the difference between the asset and the liability "
          "carried across. It splits two ways: the part that stays on the balance sheet, and the part "
          "recognised immediately as a gain or loss.",
          "observed", JCREW,
          [
           rule("ACC-R-034", "Balance forward and its split",
                "BalanceForward = InitialAssetBalance − InitialLiabilityBalance, and it equals "
                "RemeasurementBalanceForward + ProfitAndLossImpact.", "derived"),
          ]),
       ]),

     n("Recalculation state", "field-group",
       "The engine does not recompute when something changes. It raises a dirty flag and waits for a "
       "human. This group is that flag plus its audit trail.",
       "observed", CSV,
       [
        n("NeedsRecalculation", "field",
          "Shown in the UI as 'Recalc?'. Vendor definition: \"When set to Yes, this flag indicates that "
          "the lease accounting schedule must be recalculated.\" The System Administrator Dashboard has "
          "a dedicated 'ASC 842 Recalculations' widget for working the queue.",
          "observed", JCREW,
          [
           n("RecalcTriggerDate", "field",
             "The date the flag went up — so an analyst can see how long a schedule has been stale.",
             "observed", JCREW),
           n("NeedsRecalcModifiedByMemberIDList", "field",
             "Every user whose edit would have raised the flag, kept as a list inside a single text "
             "column. A rebuild should make this a proper join table; the separator Lucernex uses is "
             "not documented.",
             "observed", JCREW),
           rule("ACC-R-020", "Schedule-type change dirties the schedule",
                "Changing the ASC 842 or IFRS 16 schedule type on the Accounting Assumptions, Covenants "
                "or Recurring Expenses page sets Recalc? to Yes.", "observed"),
           rule("ACC-R-021", "New expense setup dirties the schedule using its expense type",
                "Creating an expense setup with a schedule flips Recalc? on whichever accounting "
                "schedule uses that expense type.", "observed"),
           rule("ACC-R-022", "Accounting method change requires remeasurement",
                "Vendor definition of the accounting method field: \"If its value is changed, you will "
                "need to remeasure your schedule.\" It states the consequence, not whether the flag is "
                "set.", "observed"),
           rule("ACC-R-023", "Recalculation audit trail",
                "Raising the flag stamps the date, the last user, and appends to the member list.",
                "observed"),
          ]),
        n("AssociatedExpenseSetupIDs", "field",
          "A maintained reverse index: the list of expense setups whose expense type feeds this "
          "schedule. It exists so the engine can find which schedules to dirty when an expense setup "
          "changes, without scanning everything. Stored as delimited text, and not typed as a foreign "
          "key even though that is what it is.",
          "observed", JCREW),
        n("RecalcOverrideNotes", "entity",
          "A free-text justification attached to a schedule when someone decides not to recalculate. "
          "Seven fields, essentially a note plus who wrote it. Whether writing one clears the flag is "
          "unknown.",
          "observed", OBJ,
          [rule("ACC-R-024", "Recalculation override",
                "A note is recorded against the schedule. Whether it clears Recalc? is undocumented.",
                "derived")]),
       ]),

     n("Modification and remeasurement deltas", "field-group",
       "Lucernex does not record a lease modification as an event. It creates a whole new schedule "
       "carrying six difference figures measured against the one it replaces, and marks the old one "
       "inactive. This group is those six figures.",
       "observed", A842,
       [
        n("PriorLastPostedPeriodID", "field",
          "Points back at the schedule this one replaced — the link that makes the version chain "
          "walkable.",
          "observed", JCREW),
        n("PostedInitAssetAdj / PostedInitLiabilityAdj", "field",
          "How far the new schedule's opening balances differ from the old schedule's balances as at "
          "the last period that was already posted to the ledger.",
          "observed", JCREW),
        n("Shortened-term differences", "field-group",
          "Four further figures used only when a lease is terminated early: the restated liability "
          "over the shortened term, and three differences against the original schedule.",
          "observed", JCREW,
          [rule("ACC-R-047", "Term shortening",
                "Four formulas, all stated verbatim by the vendor, covering the restated liability and "
                "the asset, liability and rent differences.", "observed")]),
        rule("ACC-R-045", "Schedule supersession",
             "Creating a replacement schedule links it to its predecessor, copies the posted cut-off "
             "date, computes four adjustment figures, and marks the predecessor inactive.", "observed"),
        rule("ACC-R-046", "Mid-period remeasurement split",
             "Two fields hold the partial interest and partial expense from the period start to the "
             "remeasurement date.", "observed"),
       ]),

     n("Roll-forward disclosure block", "field-group",
       "25 fields reproducing the asset and liability roll-forward that ASC 842 requires in the "
       "financial statement notes: opening balances, plus new leases, plus remeasurements, plus "
       "reclassifications, less expirations and amortisation, equals closing balances. Every one of "
       "the 25 is a currency figure and none of them has a vendor definition — this is the "
       "least-documented block in the whole module.",
       "observed", CSV,
       [
        n("Two near-identical reclassification triples", "constraint",
          "The block contains both Reclassification* and Reclass* versions of gross asset, "
          "accumulated amortisation and lease liability impact — six fields, two sets of three, and "
          "nothing offline explains the difference between them.",
          "observed", A842),
       ]),

     n("Maturity ladder block", "field-group",
       "14 fields giving the future cash expense by fiscal year — this year, next year, third through "
       "sixth, and everything beyond — plus four quarterly figures for the current year. ASC 842 asks "
       "for five years plus a tail; Lucernex offers six.",
       "observed", CSV,
       [
        n("Quarterly fields are conditionally populated", "constraint",
          "Q1 only fills if the report starts in period 1; Q2 if periods 1–4; Q3 if 1–7; Q4 if 1–9. "
          "Stated exactly in the vendor definitions and very easy to miss.",
          "observed", JCREW),
       ]),

     n("Commitment totals", "field-group",
       "Two headline figures a portfolio manager reads without opening the schedule: everything still "
       "owed, and everything ever owed.",
       "observed", JCREW,
       [
        n("TotalCommitment", "field",
          "Vendor definition: \"The sum of all rent payments for the life of the lease.\"",
          "observed", JCREW,
          [rule("ACC-R-035", "Total commitment", "Sum of all rent payments over the lease life.",
                "observed")]),
        n("CurrentRemainingCashBalance", "field",
          "The current and future remaining lease payments. A sibling field gives the same figure "
          "excluding the current period.",
          "observed", JCREW,
          [rule("ACC-R-036", "Remaining cash balance",
                "One figure includes the current period, the other excludes it.", "observed")]),
       ]),
     n("SLRemainingAssetBalance", "field",
       "How much right-of-use asset should remain after the schedule ends — used on finance leases "
       "where the tenant expects to keep something of value.",
       "observed", JCREW,
       [
        n("Percent or Currency — the value carries no unit", "type",
          "A single column that may hold either a percentage or a dollar amount. Vendor definition: "
          "\"If you enter a value between 0-100, the system will default the option button setting to "
          "Percentage. If you enter a value of 100.01 or above, the system will default the option "
          "button setting to Currency. You can override the default option button setting.\"",
          "observed", JCREW,
          [
           n("Migration hazard: the guess can be overridden", "constraint",
             "Because a user can override the magnitude-based guess, and no column in the schema "
             "stores that override, a stored 50 might mean 50% or $50 and nothing in the data says "
             "which. Reading it by magnitude will silently misinterpret every overridden record — and "
             "this field drives a balance-sheet number, not a display.",
             "derived", MAP),
          ]),
        rule("ACC-R-049", "Final asset amount / residual carve-out",
             "Only available on finance contracts. The final-asset date defaults to the schedule end "
             "date; a later date amortises beyond it.", "observed"),
       ]),
    ]),

  # ---- SLPeriod under the same submodule
  n("SLPeriod — one row per accounting period", "entity",
    "The atomic output of the engine: for each month (or each of 13 retail periods) it records what "
    "cash was paid, what expense was recognised, how much of that was interest, and what the asset "
    "and liability are worth at the end. 79 fields — but 23 of them exist only for currency "
    "translation and 23 more only to carry general-ledger account numbers, so the real accounting "
    "payload is about 21 numbers. Physical table: s_l_period.",
    "observed", OBJ,
    [
     n("Cash versus expense — the straight-line idea itself", "field-group",
       "The whole point of straight-lining: rent is often paid unevenly (free months, step-ups), but "
       "accounting recognises it evenly. The gap between what you paid and what you recognised is the "
       "deferred balance.",
       "observed", JCREW,
       [
        n("PeriodCashAmount", "field",
          "What was actually paid this period.", "observed", JCREW),
        n("PeriodExpenseAmount", "field",
          "Vendor definition: \"The cash rent straight lined over the life of the schedule.\" The even "
          "figure recognised in the profit and loss account.",
          "observed", JCREW),
        n("PeriodDeferredAmount", "field",
          "Vendor definition: \"The difference between the period cash rent and straight line rent "
          "expense.\" Positive in periods you overpay relative to the even line, negative when you "
          "underpay.",
          "observed", JCREW,
          [n("Sign convention unstated", "constraint",
             "The wording implies cash minus expense, but no source says so outright. Getting the sign "
             "backwards inverts the deferred-rent balance for the whole lease.",
             "derived", RUL)]),
        n("CumulativeDeferredBalance", "field",
          "The running total of deferred rent from the start of the schedule to this period — the "
          "balance-sheet accrual a straight-line schedule exists to produce.",
          "observed", JCREW),
        n("PVOfPeriodCashAmount", "field",
          "This period's payment expressed in today's money. Vendor definition: \"The Present Value of "
          "a future cash payment in today's valuation. This value is discounted to present value from "
          "the period that the payment will be made.\" Summing this column across the lease is what "
          "produces the opening liability.",
          "observed", JCREW,
          [rule("ACC-R-032", "Present value of a period payment",
                "Discount the payment from its own period back to the accounting begin date. The "
                "compounding convention is not documented.", "derived")]),
        rule("ACC-R-037", "Straight-line expense and deferral",
             "Expense is the total cash spread evenly; deferral is cash minus expense; the cumulative "
             "balance is the running sum.", "observed"),
       ]),
     n("Balances and amortisation", "field-group",
       "How the asset and the liability wind down period by period.",
       "observed", JCREW,
       [
        n("CumulativeAssetAmortExpense", "field",
          "Accumulated amortisation. Vendor definition gives the recurrence exactly: for the first "
          "period it equals that period's amortisation; for every later period it is that period's "
          "amortisation plus the previous period's accumulated balance.",
          "observed", JCREW,
          [rule("ACC-R-039", "Accumulated amortization recurrence",
                "A simple running total, stated verbatim by the vendor.", "observed")]),
        n("GrossAssetBalance", "field",
          "Vendor definition: \"This field's value is equal to the Asset Balance + the Accumulated "
          "Amortization Balance\" — i.e. the asset before any wear-down, useful for the disclosure "
          "roll-forward.",
          "observed", JCREW,
          [rule("ACC-R-040", "Gross asset balance", "Asset balance plus accumulated amortisation.",
                "observed")]),
        n("PeriodInterestAmount", "field",
          "The interest accruing on the lease liability at the discount rate. Whether it is computed "
          "on the opening or the closing balance is not documented — a one-period difference that "
          "compounds across the whole lease.",
          "observed", JCREW,
          [rule("ACC-R-038", "Interest expense",
                "Interest on the liability at the discount rate; the balance it is charged on is "
                "unconfirmed.", "derived")]),
       ]),
     n("Short-term / long-term split", "field-group",
       "Balance sheets separate what falls due within twelve months from what falls due later. This "
       "group computes both sides — and stores two competing versions of the short-term liability.",
       "observed", JCREW,
       [
        n("Forward12MonthLiabilityAmortBased", "field",
          "The next twelve months of liability reduction, computed on an amortisation basis.",
          "observed", JCREW),
        n("Forward12MonthLiabilityPVBased", "field",
          "The same quantity computed on a present-value basis. Both are stored on every row.",
          "observed", JCREW),
        n("A firm setting picks the winner", "constraint",
          "Admin > Manage Company > Financial Settings holds a 'Short-Term/Long-Term Liability "
          "Calculation Method' choice. That page is not an object in the schema export, so where it "
          "persists is unknown — the 18-field Firm record's JSONConfigText column is the only "
          "plausible home. The present-value formula itself is not available offline.",
          "observed", JCREW,
          [rule("ACC-R-042", "Which short-term liability is reported",
                "A firm-level setting selects the amortisation-based or PV-based figure.", "observed")]),
       ]),
     n("Currency translation", "field-group",
       "Twelve fields for leases denominated in a foreign currency. Four of the formulas are published "
       "verbatim by the vendor — and one of them is almost certainly wrong.",
       "observed", JCREW,
       [
        n("LiabilityTranslationAdjustment", "field",
          "The published formula reads: current asset balance + (payment − interest) − prior month's "
          "asset balance.",
          "observed", JCREW,
          [n("The published formula is probably a documentation error", "constraint",
             "It references the asset balance twice and never the liability balance, while calling "
             "itself a liability adjustment. Do not implement as written; confirm against a live "
             "FX-impact grid first.",
             "derived", SL)]),
        n("ConversionRateAverage / ConversionRateMonthEnd", "field",
          "The two exchange rates a period needs: an average rate for flows and a month-end rate for "
          "balances. Both typed to six decimal places.",
          "observed", JCREW),
        rule("ACC-R-043", "Currency translation",
             "Four published formulas covering asset, liability, cumulative translation adjustment and "
             "liability FX impact.", "observed"),
        rule("ACC-R-044", "Translation vs. revaluation mapping",
             "A contract flagged 'Is Translation' uses the translation mapping; otherwise the "
             "revaluation mapping.", "observed"),
       ]),
     n("NumberDays", "field",
       "How many days long this period is. It is stored rather than derived because the amortisation "
       "basis setting can weight each period by its day count — see the portfolio policy branch.",
       "observed", JCREW),
     n("RecordStatus", "field",
       "Where this period stands with the ledger: posted, not posted, or mixed. 'Mixed' means a period "
       "can be partially posted, which is why the closed/open boundary is a date rather than a flag.",
       "observed", JCREW),
     rule("ACC-R-028", "Period row generation",
          "One period row per fiscal period between the schedule's begin and end dates, taken from the "
          "portfolio's fiscal calendar.", "derived"),
     rule("ACC-R-041", "Short-term / long-term split",
          "Five formulas covering the twelve-month-forward changes and the long-term remainder.",
          "observed"),
    ]),

  n("The three generate buttons", "capability",
    "The engine has exactly three entry points, all of them buttons on the contract summary page. "
    "They are not stored data — the field catalog types them as form action buttons that trigger a "
    "server-side process.",
    "observed", CSV,
    [
     n("GenerateStraightLineRent", "field",
       "'Generate Straight-line Rent Schedule' — produces a legacy straight-line schedule.",
       "observed", CSV),
     n("GenerateFASBSchedule", "field",
       "'Generate 842 Rent Schedule' — produces an ASC 842 schedule. Named for FASB, the US standards "
       "board, rather than for the standard.",
       "observed", CSV),
     n("GenerateIFRS16Schedule", "field",
       "'Generate IFRS 16 Rent Schedule' — produces an IFRS 16 schedule.",
       "observed", CSV),
     n("ModifyStraightLineStatus", "field",
       "'Modify Straight-Line Status' — a fourth button with no vendor definition at all. A "
       "similarly-named but different admin utility also exists at a separate route.",
       "observed", CSV,
       [n("Two controls share this name", "constraint",
          "One is this contract-level button; the other is a firm-wide admin utility at "
          "/en/admin/lxadmin/SLDemoTweaks.jsp, sitting beside Data Conversion Cleaner and Delete "
          "Entities, classified during exploration as explicitly mutating and high risk. Neither was "
          "activated, so what either does is unknown.",
          "observed", ADM4)]),
     rule("ACC-R-027", "Schedule-type flag stamping",
          "Whichever button ran sets the matching identity flag on the new schedule header.",
          "derived"),
    ]),
 ])

# ---------------------------------------------------------------- SPINE 2
spine2 = n(
 "ASC 842 classification — operating or finance?", "submodule",
 "Before a lease can be measured it must be classified. A finance lease sits on the balance sheet "
 "like a purchase; an operating lease is a smoother, simpler charge. Lucernex decides with five "
 "pass/fail tests, and the polarity is counter-intuitive: passing all five means operating, and "
 "failing any single one means finance.",
 "observed", JCREW,
 [
  n("ContractFinancialTest — the classification record", "entity",
    "93 fields. One row per test run; a contract accumulates many over its life and only the locked "
    "ones count. It holds the five test results, the inputs they consume, and — unusually — two "
    "complete parallel measurements, one under ASC 842 and one under IFRS 16, computed whether or "
    "not the tenant reports under both. Physical table: contract_financial_test.",
    "observed", OBJ,
    [
     n("The five ASC 842 tests", "field-group",
       "Three of the five are simply questions a person answers with a tick box. Two are computed "
       "comparisons against a threshold. Together they implement the classification criteria in the "
       "US standard.",
       "observed", JCREW,
       [
        n("Test #1 — does ownership transfer to the tenant?", "rule",
          "A tick box. If ownership of the asset ends up with the tenant, the arrangement is really a "
          "purchase, so the lease is a finance lease.",
          "observed", JCREW,
          [rule("ACC-R-005", "Test 1: title transfer",
                "Title reverts to the tenant = Fail = finance lease.", "observed")]),
        n("Test #2 — is there a purchase option the tenant will take?", "rule",
          "A tick box. If the tenant is reasonably certain to buy, it is a purchase in substance. "
          "",
          "observed", JCREW,
          [rule("ACC-R-006", "Test 2: purchase option reasonably certain to be exercised",
                "A bargain purchase option = Fail = finance lease.", "observed")]),
        n("Test #3 — is the lease term most of the asset's remaining life?", "rule",
          "Computed. Divide the term used for the test by the asset's remaining economic life; if the "
          "result is below the threshold (usually 75%) the lease passes. A separate tick box, 'is the "
          "lease commencement at or near the end of the economic life', forces a pass regardless. "
          "",
          "observed", JCREW,
          [rule("ACC-R-007", "Test 3: major part of remaining economic life",
                "Test term divided by remaining life, compared against the threshold. The default "
                "threshold comes from the portfolio.", "observed"),
           rule("ACC-R-008", "Test 3 override: commencement near end of economic life",
                "The 'lease is near end' tick box forces a Pass unconditionally.", "observed")]),

        # ---- the deep leg ----
        n("Test #4 — do the payments amount to substantially all the asset's value?", "rule",
          "Computed, and the most involved of the five. If the present value of what you will pay is "
          "close to what the asset is worth, you have effectively bought it. Vendor definition: \"If "
          "you exceed your Threshold Fair Value Controlled, your Test #4 result will be 'Failed'.\"",
          "observed", JCREW,
          [
           rule("ACC-R-009", "Test 4: substantially all of fair value",
                "Fair value times the portion controlled times the threshold gives the benchmark; a "
                "liability above it fails. Which liability figure is used is ambiguous.", "observed"),
           n("Test #4 inputs", "field-group",
             "Four values feed this test: what the whole asset is worth, how much of it you control, "
             "the threshold percentage, and the liability you booked.",
             "observed", JCREW,
             [
              n("FairValueOfAsset", "field",
                "What the whole underlying asset is worth. Vendor definition quotes the standard: "
                "\"FASB 842.10.20 defines fair value as the price that would be received to sell an "
                "asset or paid to transfer a liability in an orderly transaction between market "
                "participants at the measurement date.\"",
                "observed", JCREW,
                [
                 n("MONEY / sTYPE_MONEY", "type",
                   "A currency amount, entered by a person rather than computed. Fifteen declared "
                   "digits, no declared decimal scale, stored as TEXT in the customer database.",
                   "observed", CSV,
                   [
                    n("Asset — the source entity this value also lives on", "entity",
                      "For an equipment lease the same fair value is recorded on the physical asset "
                      "record, not just on the test. Asset carries 122 fields and a complete duplicate "
                      "of the classification inputs — fair value, discount rate override, "
                      "'too specialised for the lessor', 'has a buyout option', 'title reverts to "
                      "tenant', residual, depreciable life — because an equipment contract can hold "
                      "many assets, each classified in its own right.",
                      "observed", OBJ,
                      [
                       n("The comparison that makes Test #4 decisive", "constraint",
                         "Fair value alone decides nothing. It is multiplied by the portion of the "
                         "asset you control to give the fair value you actually command, then "
                         "multiplied by the threshold percentage (usually 90%) to give the benchmark. "
                         "The lease liability is compared against that benchmark, and exceeding it "
                         "fails the test and makes the lease a finance lease. Which liability figure "
                         "is used — before or after manual adjustment — is genuinely ambiguous in the "
                         "vendor's own documentation, and it is the difference between an operating "
                         "and a finance lease on a borderline contract.",
                         "observed", A842),
                       n("Asset-level overrides beat the contract", "constraint",
                         "Asset carries its own discount rate override, accounting method override, "
                         "and accounting begin/end dates. Vendor definition: if the override dates are "
                         "blank, the test and schedules run from the asset's expense schedule dates "
                         "instead.",
                         "observed", JCREW),
                      ]),
                   ]),
                ]),
              n("PortionOfAssetControlled", "field",
                "What share of the asset this lease actually gives you — vendor definition: \"the "
                "percentage based upon the rentable area divided by the total area of the asset\". "
                "A floor in a tower is not the tower.",
                "observed", JCREW),
              n("FairValueThreshold", "field",
                "The fraction of fair value that counts as 'substantially all'. Vendor definition: "
                "\"This value is usually set to 90%.\" The default comes from the portfolio.",
                "observed", JCREW),
              n("FairValueControlled (computed)", "field",
                "Fair value multiplied by the portion controlled. Typed by the catalog as a "
                "system-calculated currency amount, so the engine writes it rather than a user.",
                "observed", CSV),
              n("ThresholdFairValueControlled (computed)", "field",
                "The controlled fair value multiplied by the threshold — the actual benchmark the "
                "liability is measured against.",
                "observed", CSV),
              n("InitLiabilityBalToThreshFairValueCtrld (computed)", "field",
                "The liability expressed as a percentage of that benchmark. Over 100% and the test "
                "fails.",
                "observed", CSV),
             ]),
          ]),
        n("Test #5 — is the asset too specialised to re-let?", "rule",
          "A tick box. If nobody but this tenant could use the asset, the landlord has effectively "
          "sold it.",
          "observed", JCREW,
          [rule("ACC-R-010", "Test 5: specialised asset",
                "A specialised asset = Fail = finance lease.", "observed")]),
        n("Fail any one, and the lease is a finance lease", "constraint",
          "Stated on all five result fields: \"If you 'fail' at least one of the five tests, the lease "
          "will be classified as a Finance lease. If you 'pass' all tests, the lease will be "
          "considered an Operating lease.\" The result is written to Final Result. Note the inverted "
          "polarity — 'passing' is the unremarkable outcome.",
          "observed", JCREW,
          [rule("ACC-R-011", "Final classification (inverted polarity)",
                "Any fail means finance; all five passes means operating.", "observed"),
           rule("ACC-R-012", "Accounting method override",
                "An 'Accounting Type Override' on the test, and a second override on the asset, can "
                "supersede the computed verdict. Precedence between the two is undocumented.",
                "derived")]),
        n("PASS_FAIL / COMPUTED", "type",
          "The five result fields are typed as a pass/fail pair in the field catalog — a computed "
          "verdict, not an input. Lucernex's live API makes COMPUTED one of its ten canonical field "
          "types, which is vendor confirmation that the platform itself separates calculated values "
          "from entered ones.",
          "observed", GQL),
       ]),
     n("Accounting dates", "field-group",
       "The window the test and the schedule are run over - which is not the same as the lease's own "
       "commencement and expiry.",
       "observed", JCREW,
       [
        n("Topic842BeginDate", "field",
          "Labelled 'Accounting Begin Date'. Vendor definition: \"This date is the date your "
          "organization is adopting ASC 842, or the Possession Begin Date, whichever is later.\"",
          "observed", JCREW),
        n("Topic842EndDate", "field",
          "Labelled 'Accounting End Date'. Vendor definition: \"This is the end date of your ASC 842 "
          "financial accounting for the contract, including any likely options.\"",
          "observed", JCREW),
        n("CommenceDate / ExpireDate", "field",
          "Both are pulled from the contract summary page rather than typed here.", "observed", JCREW),
        rule("ACC-R-017", "Accounting date window",
             "Begin date is the later of the firm's adoption date and possession; end date includes "
             "likely options.", "observed"),
        rule("ACC-R-018", "Asset-level accounting date override",
             "On an equipment lease, asset-level override dates set the window; if blank, the asset's "
             "expense schedule dates do.", "observed"),
       ]),
     n("Three different term lengths", "field-group",
       "The easiest thing to get wrong. A lease has a contractual term, a 'likely' term including "
       "renewal options the tenant will probably take, and a term chosen specifically for the test — "
       "and Lucernex stores all three separately.",
       "observed", JCREW,
       [
        n("TermLength", "field", "Simply expiry date minus commencement date.", "observed", JCREW),
        n("LikelyTermLength", "field",
          "Computed from renewal terms a user has marked 'Likely' on the contract's Terms page.",
          "observed", JCREW),
        n("TestTermLength", "field",
          "The term actually fed into Test #3. Its vendor definition names 'Test Begin Date' and "
          "'Test End Date' fields that do not exist anywhere in the schema.",
          "observed", JCREW,
          [n("The fields its definition names are missing", "constraint",
             "The nearest candidates are the Accounting Begin and End Dates. Whether they are the "
             "same fields under a later label is unresolved.",
             "observed", A842)]),
        rule("ACC-R-016", "Term-length sourcing", "Three term lengths, three different definitions.",
             "observed"),
       ]),
     n("Dual measurement — both standards, every time", "field-group",
       "Fourteen fields, seven per standard, computing the same seven quantities twice: the cash value "
       "of the lease before and after adjustments, its present value before and after adjustments, the "
       "opening asset, the opening liability, and the net liability. The ASC 842 and IFRS 16 vendor "
       "definitions are word-for-word identical.",
       "observed", JCREW,
       [
        n("ASC842InitialLiabilityBalance / IFRS16InitialLiabilityBalance", "field",
          "The same quantity under each standard. Both are typed as system-calculated currency "
          "amounts. Whether the IFRS 16 half is ever actually populated in this tenant is untested.",
          "observed", CSV),
       ]),
     n("Present-value adjustments", "field-group",
       "Twelve things that move the measured value up or down: purchase and cancellation options, "
       "residual value guarantees, structuring costs, initial direct costs, lease incentives, "
       "impairments, dismantling costs, pre-commencement payments. Nine are typed by a person; three "
       "are pulled automatically from the contract's covenants.",
       "observed", JCREW,
       [
        n("Covenant — where three of them come from", "entity",
          "A covenant is any promise written into the lease. Three kinds carry money into the "
          "accounting: a purchase option, a cancellation option, and a residual value guarantee. "
          "Vendor definition: the amount is pulled into the accounting assumptions and the schedule "
          "only if the covenant's accounting adjustment type is one of those three.",
          "observed", JCREW,
          [
           n("CodeAccountingAdjustmentTypeID", "code-table",
             "The gate. Its values are known from the vendor definition of the matching field on "
             "Financial Adjustment: Cancellation Option, Residual Value Guarantee, Purchase Option.",
             "observed", JCREW,
             [
              n("Purchase Option", "code-value",
                "A right to buy the asset. Feeds Purchase Option Amount on both the test and the "
                "schedule, and is what Test #2 is asking about.",
                "observed", JCREW),
              n("Residual Value Guarantee", "code-value",
                "A promise that the asset will be worth a certain amount at the end. Splits into a "
                "total and the portion a third party guarantees.",
                "observed", JCREW),
              n("Cancellation Option", "code-value",
                "A right to end the lease early, with its own price.", "observed", JCREW),
             ]),
           rule("ACC-R-019", "Covenant-sourced measurement adjustments",
                "Only the three named adjustment types flow into the accounting.", "observed"),
          ]),
        n("Impairments are entered as negative numbers", "constraint",
          "Stated three times, on three different objects: \"Enter any deductions related to the "
          "diminished value of the asset as a negative number.\" Three separate impairment inputs "
          "exist — on the schedule, on the test, and on the asset — and which one wins when more than "
          "one is filled in is not documented.",
          "observed", JCREW,
          [rule("ACC-R-048", "Impairment",
                "Total impairment impact is the impairment plus the prior accumulated amortisation "
                "balance. Precedence among the three inputs is unresolved.", "observed")]),
       ]),
     n("Locking makes a test authoritative", "field-group",
       "A test is a draft until someone locks it. Locking is one-way.",
       "observed", JCREW,
       [
        n("IsLocked", "field",
          "Vendor definition: \"Locking the test ensures that the test cannot be modified. You cannot "
          "delete a classification test once it has been locked, but you can create another test as "
          "necessary.\" An append-only, immutable-once-locked audit chain.",
          "observed", JCREW),
        n("Contract.LatestFinancialTestFinalResult", "field",
          "The contract-level answer. Vendor definition: \"The final result of the most recently "
          "locked ASC 842 test.\" Unlocked tests do not count.",
          "observed", JCREW),
        n("AutoComputed", "field",
          "Vendor definition: \"This field will have a true value if the ASC 842 test was computed "
          "automatically by the system.\" The conditions under which the system decides to run a test "
          "on its own are not documented anywhere.",
          "observed", JCREW,
          [rule("ACC-R-015", "Auto-computation marker",
                "Set when the system ran the test rather than a user. The trigger is unknown.",
                "observed")]),
        rule("ACC-R-013", "Test locking", "Locked tests are immutable and undeletable.", "observed"),
        rule("ACC-R-014", "Propagation of the authoritative result",
             "The most recently locked test's verdict propagates to the contract.", "observed"),
       ]),
    ]),
  n("The legacy Cap Lease Test", "capability",
    "A second, older five-test structure still sitting on the contract record itself — the ASC 840 "
    "capital-lease test that ASC 842 replaced. It splits Test 5 into 5a and 5b, bases its Test 4 on "
    "building and land market values rather than present value, stores its results as free text "
    "instead of pass/fail, and has no lock and no child record. Eight of its fields are documented "
    "as dead. Migrate the data for audit; do not rebuild the logic.",
    "observed", JCREW,
    [
     n("Four Ratio* fields", "field-group",
       "Vendor definition on all four: \"This is a legacy field that was used in the Capital Lease "
       "Test. It is no longer used, and does not impact the test.\"",
       "observed", JCREW),
     n("Four renewal-option flags", "field-group",
       "Vendor definition on all four: \"This field is not implemented for contracts or equipment "
       "contracts.\"",
       "observed", JCREW),
    ]),
 ])

# ---------------------------------------------------------------- SPINE 3
spine3 = n(
 "Cash-flow sourcing and routing", "submodule",
 "Before anything can be straight-lined there has to be a stream of payments to straight-line. That "
 "stream comes from the rent engine, and the route it takes into a particular accounting schedule is "
 "decided by something surprising: the expense *type*, not the contract and not the expense record.",
 "observed", JCREW,
 [
  n("ExpenseSetup — a recurring charge on a lease", "entity",
    "96 fields. One row per recurring obligation: base rent, common-area maintenance, real estate "
    "taxes, insurance. It defines what is owed, to whom, how often, on what area basis, with what "
    "caps — but not the individual amounts. Physical table: expense_setup.",
    "observed", OBJ,
    [
     n("ExpenseSchedule — the amounts, period by period", "entity",
       "51 fields. The generated child of an expense setup: for each date range, what the payment is, "
       "what the annual amount is, what taxes apply, whether it has been approved and processed. This "
       "is the actual cash stream the accounting engine consumes. Physical table: expense_schedule.",
       "observed", OBJ,
       [
        n("CodeExpenseType — the routing table (TableType 3013)", "code-table",
          "Every expense setup names an expense type, and the expense type is where the routing lives. "
          "Vendor definition: \"Expense Types are used to associate records with lease accounting "
          "schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, "
          "and real estate tax accounts.\" 31 fields, most of them account numbers. Physical table: "
          "code_expense_type.",
          "observed", JCREW,
          [
           n("The three schedule-type foreign keys", "field-group",
             "One routing key per accounting standard, sitting side by side on the expense type. This "
             "is the mechanism that lets a single contract feed three different schedules at once — "
             "and it means changing one expense type's routing dirties every schedule that uses it.",
             "observed", OBJ,
             [
              n("CodeASC842ScheduleID", "field",
                "Which ASC 842 schedule type this expense's cash flows belong to. Vendor definition "
                "adds a behavioural note: \"This field is functional, and changing its value on the "
                "Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will "
                "set the Recalc? flag to YES.\"",
                "observed", JCREW,
                [
                 n("CodeASC842Schedule — the table it points at", "code-table",
                   "The same tenant-defined schedule-type table the schedule header points at. Reached "
                   "here from a completely different direction: the header says which type a schedule "
                   "*is*; the expense type says which type a cash flow *goes to*.",
                   "observed", OBJ,
                   [
                    n("842 Rent — the single configured row", "code-value",
                      "In principle a tenant defines several schedule types to separate, say, "
                      "real-estate from equipment leases, or to route expense categories to "
                      "different ledger accounts. In practice this tenant defined one. Every expense "
                      "type's ASC 842 routing therefore resolves to the same destination, and the "
                      "two sibling routing keys have no valid target at all.",
                      "observed", REG,
                      [
                       n("DontAmortizeAssetValue — the behaviour flag", "field",
                         "The only switch on the table that changes what the engine computes rather "
                         "than where it exports. Name says it suppresses right-of-use asset "
                         "amortisation for schedules of this type. No vendor definition exists, so its "
                         "exact effect is the one genuinely load-bearing unknown at this depth.",
                         "observed", OBJ,
                         [n("BOOLEAN / sTYPE_BOOLEAN", "type",
                            "A plain yes/no. Present identically on all three schedule-type tables — "
                            "ASC 842, IFRS 16 and straight-line — each with its own independent value.",
                            "observed", CSV)]),
                      ]),
                   ]),
                ]),
              n("CodeIFRS16ScheduleID", "field",
                "The same routing key for the international standard.", "observed", OBJ),
              n("CodeSLScheduleID", "field",
                "The same routing key for the legacy straight-line schedule.", "observed", OBJ),
             ]),
           n("The 2000/3000 TableType band does not predict behaviour", "constraint",
             "Lucernex registers all 207 of its drop-down tables under numeric type ids in two "
             "bands, 2000-2190 and 3000-3016, and it is tempting to read the 3000 band as 'the "
             "tables that carry behaviour'. Checked against the eleven code-table objects the schema "
             "actually contains, that is wrong. Expense Type (3013) supports it, but Sales Type "
             "(3012) is a bare three-column lookup and Problem (3001) close to one — while the three "
             "schedule-type tables (2161-2163, 24 fields each) and Issue Type (2035, 19 fields) are "
             "the most behaviour-bearing tables in the product and all sit in the 2000 band. The "
             "band is a registration-order artefact. Which code tables need more than a code, a "
             "label and an active flag has to be read per table.",
             "derived", REG),
           n("Sixteen GL account slots", "field-group",
             "Four sets of four: expense accrual accounts, percentage-rent accrual accounts, real "
             "estate tax accrual accounts, and accounts-payable export numbers. Copied down onto "
             "accrual transactions when they are generated.",
             "observed", OBJ),
          ]),
        n("HoldFlag", "field",
          "A yes/no marker on a schedule. Every hold flag in this module is documented as "
          "informational only — the hold is a convention among users, not something the system "
          "enforces.",
          "observed", JCREW),
       ]),
     n("AcctingAssumptionAdjust — accounting-only overlay", "entity",
       "19 fields. A payment stream that exists purely for accounting and never produces cash: a way "
       "for an accountant to say 'for measurement purposes, assume this extra amount over this "
       "period'. Carries its own routing keys, so an adjustment can be steered to a different "
       "schedule from the base rent. Physical table: accting_assumption_adjust.",
       "observed", JCREW,
       [
        n("Entering one amount fills in three others", "constraint",
          "Vendor definition: the first payment, last payment and annual amount \"will auto-populate "
          "depending upon the value you enter in the Payment Amount field and the frequency you "
          "select from the Frequency field\".",
          "observed", JCREW),
        n("SecondaryRentSchedAllocPercent", "field",
          "Splits an amount across a primary and a secondary schedule. Where the remainder goes is "
          "not stated.",
          "observed", JCREW),
        n("AdjustmentPercent", "field",
          "Documented as dead: \"This field is a placeholder in preparation for an upcoming "
          "enhancement.\"",
          "observed", JCREW),
       ]),
     n("AlternateRentSchedule — the rent overlay", "entity",
       "25 fields. Used when a lease temporarily switches to a different rent basis — commonly a "
       "percentage of sales during a co-tenancy failure. Contains the three flags most often "
       "mistaken for accounting controls.",
       "observed", OBJ,
       [
        n("SuspendSL", "field",
          "'Suspend SL?' — the field whose name promises the ability to pause a straight-line "
          "schedule. Vendor definition, in full: \"This field is no longer used.\" Do not rebuild it. "
          "If ASG Edge+ needs schedule suspension, that is a new requirement, not a port.",
          "observed", JCREW),
        n("SetExpHoldFlag / SetPRHoldFlag", "field",
          "These put generated recurring-expense and percentage-rent transactions on hold during an "
          "alternate-rent window. They are cash-side controls and do not touch the accounting "
          "schedule at all.",
          "observed", JCREW,
          [rule("ACC-R-055", "Alternate-rent hold propagation",
                "A hold flag is set on transactions generated during the window.", "observed")]),
       ]),
     rule("ACC-R-025", "Cash-flow routing by expense type",
          "Each cash flow lands on the schedule its expense type designates for the standard being "
          "generated.", "derived"),
     rule("ACC-R-026", "Secondary schedule allocation",
          "A stated percentage goes to a secondary schedule; the remainder is assumed to go to the "
          "primary.", "derived"),
    ]),
 ])

# ---------------------------------------------------------------- OTHER BRANCHES
policy = n(
 "Portfolio-level accounting policy", "submodule",
 "Almost every setting that changes how the engine computes lives not on the contract or the "
 "schedule but on the Portfolio — the object Lucernex calls Program. This branch was missed entirely "
 "in the first pass of this documentation and found later from the vendor field definitions.",
 "observed", JCREW,
 [
  n("Program (UI: Portfolio)", "entity",
    "180 fields, of which about 25 are accounting policy. It is the default-setter: the discount "
    "rate, both classification thresholds, three amortisation-basis switches, two proration "
    "switches, the fiscal year end, and fourteen exchange-rate-type selectors. Physical table: "
    "program.",
    "observed", OBJ,
    [
     n("The amortisation basis", "field-group",
       "How an amount is spread across periods. Not one setting but three independent ones, and the "
       "asset switch alone carries a scope restriction the other two do not.",
       "observed", JCREW,
       [
        n("SLAssetAmortizeMethod", "field",
          "Vendor definition: \"There are two options: Per Day, and Per Period. By Period distributes "
          "the amortization equally among periods, and Per Day distributes the amortization according "
          "to the number of days in the period. This setting impacts only ASC 842 Finance leases.\"",
          "observed", JCREW,
          [
           n("GaapAmortizeMode", "code-table",
             "The live GraphQL API names this value set as a two-value enumeration. It is the "
             "authoritative value list, because the database columns themselves are just free text.",
             "observed", GQL,
             [
              n("PER_PERIOD", "code-value",
                "Every period gets an equal share, whatever its length.", "observed", GQL),
              n("PER_DAY", "code-value",
                "Each period is weighted by how many days it contains. This is what the day count "
                "stored on every period row is for.",
                "observed", GQL),
             ]),
           n("Stored as free text, not an enum", "constraint",
             "The three columns are typed Text in the schema and TEXT in PostgreSQL, while the API "
             "exposes a proper enumeration. Whether the column stores the enum name, a display string "
             "or a code is unknown, and a migration needs to know.",
             "observed", JCREW),
           rule("ACC-R-056", "Amortisation basis: Per Day or Per Period",
                "Three independent switches, one per schedule column. Do not collapse them into one.",
                "observed"),
          ]),
        n("SLCashAmortizeMethod / SLExpenseAmortizeMethod", "field",
          "The same choice for cash rent and for rent expense. Neither carries the finance-lease "
          "restriction the asset switch does.",
          "observed", JCREW),
       ]),
     n("SLProrate35As28", "field",
       "A proration rule for partial first and last periods. Vendor definition: prorate on a 28-day "
       "multiplier, and \"If you have a partial period that is greater than or equal to 28 days, it "
       "will be considered a whole period by the system and will not prorate.\" Only affects columns "
       "set to Per Period.",
       "observed", JCREW,
       [rule("ACC-R-057", "28-day proration of partial periods",
             "Interacts with the amortisation basis: inert on Per Day columns.", "observed")]),
     n("SLDiscountRate", "field",
       "The portfolio's default borrowing rate — the rate used to discount future rent back to today's "
       "money. Vendor definition ends with a trap: \"To enter a discount rate, enter the number no % "
       "or decimal is necessary.\"",
       "observed", JCREW,
       [
        n("5 means five percent, not five hundredths", "constraint",
          "The entry convention is a bare number with no percent sign and no decimal point. That is a "
          "migration parsing rule, not a display nicety, and getting it wrong scales every present "
          "value by a hundred.",
          "observed", JCREW),
        rule("ACC-R-001", "Default discount rate resolution",
             "Portfolio rate first; firm rate if there is none. The contract-level rate is explicitly "
             "not consulted for this default.", "observed"),
       ]),
     n("The two classification thresholds", "field-group",
       "The portfolio holds the defaults that Test #3 and Test #4 compare against. Both vendor "
       "definitions end with the same sentence: \"This field is used in the ASC 842 Test.\"",
       "observed", JCREW,
       [
        n("FairValueThreshold", "field",
          "\"Usually set to 90%.\" The fraction of the asset's value that counts as substantially all "
          "of it.",
          "observed", JCREW),
        n("RemainingEconomicLifeThreshold", "field",
          "\"Usually set to 75%.\" The fraction of remaining life that counts as a major part of it.",
          "observed", JCREW),
        n("Contract-level twins are computed, not stored", "constraint",
          "The matching contract fields are typed as computed precisely because they resolve the "
          "chain — portfolio value if one exists, otherwise the firm value — rather than holding a "
          "value of their own.",
          "observed", JCREW),
       ]),
     n("Fourteen exchange-rate-type selectors", "field-group",
       "Seven schedule columns — asset amortisation, asset balance, liability amortisation, liability "
       "balance, cash expenses, interest, single lease expense — each with two settings: one for "
       "contracts needing revaluation and one for contracts needing translation. This is what the "
       "contract's 'Is Translation' flag actually selects between.",
       "observed", JCREW,
       [rule("ACC-R-059", "Per-column FX rate-type selection",
             "The rate type is chosen per schedule column at portfolio level, not once per firm.",
             "observed")]),
     n("FiscalYearEnd", "field",
       "The month and day the fiscal year ends — the anchor the whole fiscal calendar is built from.",
       "observed", JCREW),
     n("SLMatchYearEnds", "field",
       "\"This field determines if the program allows for matching of fiscal/calendar year rent.\" The "
       "only setting that could reconcile the contract's parallel fiscal-year and calendar-year "
       "rollups. What it actually does is unconfirmed.",
       "observed", JCREW,
       [rule("ACC-R-058", "Fiscal / calendar year-end matching",
             "The switch exists and is named; what matching does is inferred, not documented.",
             "inferred")]),
    ]),
  n("FiscalPeriod — the calendar backbone", "entity",
    "17 fields defining each named period of the fiscal year: begin and end dates, days, weeks, "
    "quarter, and the calendar month it overlaps. Retail tenants commonly run 13 periods of 4 or 5 "
    "weeks rather than 12 calendar months, which is why every period row stores its own day count. "
    "Physical table: fiscal_period.",
    "observed", OBJ,
    [n("Is4or5WeekPeriod", "field",
       "Marks a retail period as four or five weeks long — the source of the uneven period lengths "
       "the Per Day amortisation basis exists to handle.",
       "observed", JCREW)]),
  n("DiscountRate — the rate lookup table", "entity",
    "16 fields. A rate scoped by portfolio, country, state, contract use, accounting method, and a "
    "schedule-length band in months, with an effective-through date. Vendor definition of the "
    "accounting-method column: \"If you leave the field blank, the discount rate will apply to both "
    "Finance and Operating.\" Physical table: discount_rate.",
    "observed", JCREW,
    [
     n("No standard dimension", "constraint",
       "The table can scope a rate to finance or operating, but not to ASC 842 versus IFRS 16. An "
       "entity reporting under both with different borrowing rates has nowhere to put the second one.",
       "derived", IF16),
     rule("ACC-R-002", "Contract-level discount rate override",
          "A rate typed directly on the contract is used ahead of the resolved default. The precedence "
          "is not stated by the vendor.", "inferred"),
     rule("ACC-R-003", "Asset-level discount rate override",
          "An equipment asset may carry its own rate, which supersedes both.", "observed"),
     rule("ACC-R-004", "Discount rate applicability scoping",
          "A blank accounting method matches both; the month band bounds the schedule lengths the rate "
          "applies to.", "observed"),
    ]),
 ])

approval = n(
 "Review, approval and posting", "submodule",
 "The engine's output is not published by the calculation. A generated schedule is a proposal that a "
 "chain of people accepts — and this is the part of the module that is invisible in the database and "
 "only shows up in the running application.",
 "observed", WF,
 [
  n("ASC 842 Schedule Review/Approval", "capability",
    "A live, configured workflow in the ASG tenant. Three ordered steps, every one a form step, every "
    "one resolving its approver as a named member. Captured from Manage Work Flows at build "
    "26.08.0.46 on 2026-09-10.",
    "observed", WF,
    [
     n("Step 1 — Initial Review of ASC 842 Schedules", "capability",
       "The first human look at a generated schedule.",
       "observed", WF,
       [n("ASR Initial Review of ASC 842 Schedule", "field-group",
          "The form layout bound to this step. A form type gets one layout per workflow step, so the "
          "same record shows different fields to different people depending where it is in the "
          "process. What this layout actually collects has not been read.",
          "observed", WF)]),
     n("Step 2 — Approve ASC 842 Schedules (ASG)", "capability",
       "ASG, the service provider, signs off internally before the client ever sees it.",
       "observed", WF,
       [n("ASR Approve ASC 842 Schedules (ASG)", "field-group",
          "The internal approval layout.", "observed", WF)]),
     n("Step 3 — Approve ASC 842 Schedules (Client)", "capability",
       "The client signs off. Only after this does the schedule count.",
       "observed", WF,
       [n("ASR Approve ASC 842 Schedules (Client)", "field-group",
          "The client-facing approval layout.", "observed", WF)]),
     n("Attachable to Portfolio and RE Contract only", "constraint",
       "The form type declares a yes/no per entity kind. Portfolio and RE Contract are yes; Equipment "
       "Contract is no — even though equipment leases generate ASC 842 schedules and have their own "
       "Generate 842 button. So either equipment schedules skip the approval gate entirely or they are "
       "approved at portfolio level. Unresolved, and it blocks the approval design.",
       "observed", WF,
       [rule("ACC-R-061", "What an ASC 842 review request may be raised against",
             "Portfolio and RE Contract only; Equipment Contract excluded.", "observed")]),
     rule("ACC-R-060", "Schedules are not auto-published",
          "Generate, review, ASG approval, client approval. A schedule therefore has a state, not a "
          "flag — and only the final state is representable in the database.", "observed"),
     rule("ACC-R-062", "Approver resolution",
          "All three steps resolve their approver as a named Member, even though the platform also "
          "supports routing by job title or org-chart position.", "observed"),
    ]),
  n("SLSummary.IsApproved", "field",
    "The one column that records the outcome. Vendor definition: \"This flag indicates that the "
    "schedule has been approved. Once a schedule has been approved, it cannot be un-approved.\"",
    "observed", JCREW,
    [
     n("Irreversible, with no rejection path", "constraint",
       "Approval cannot be undone through the application, and nothing in the schema represents a "
       "rejected schedule. What happens when a client rejects at step 3 is undocumented.",
       "observed", JCREW),
     n("Five real states, one storable", "constraint",
       "The true lifecycle is draft, submitted, under initial review, ASG-approved, client-approved. "
       "Only the last is representable on the schedule; the four before it live in the workflow "
       "instance. A rebuild that models approval as a boolean setter has modelled the wrong thing.",
       "derived", MAP),
     rule("ACC-R-050", "Approval is irreversible", "One-way, and it is the terminus of the workflow.",
          "observed"),
    ]),
  n("Posting to the ledger", "field-group",
    "Separate from approval. Posting happens period by period, and a period can be partially posted "
    "— the status vocabulary is posted, not posted, or mixed.",
    "observed", JCREW,
    [
     n("LastPostedEndDate", "field",
       "The closed/open cut line. Everything at or before it is settled; everything after can be "
       "re-derived. A modification measures all its differences against exactly this date.",
       "observed", JCREW),
     n("LastBalancePosted", "field",
       "\"This is the asset minus the liability as of the last posted period.\"", "observed", JCREW),
     rule("ACC-R-051", "Posting state and the closed cut-line",
          "The last posted period's end date is the boundary all remeasurement deltas are taken "
          "against.", "derived"),
    ]),
 ])

accruals = n(
 "Accruals", "submodule",
 "A separate, smaller engine for recognising an expense before it is billed — the classic case being "
 "an annual property tax bill accrued monthly through the year so no single month carries the whole "
 "hit.",
 "observed", JCREW,
 [
  n("ExpenseAccrualSetup", "entity",
    "31 fields configuring what to accrue and over which periods. Its record-type field decides "
    "whether this is an accrual, a forecast or a plan — three different purposes on one table. "
    "Physical table: expense_accrual_setup.",
    "observed", JCREW,
    [
     n("CodeAccrualTypeID", "code-table",
       "Vendor definition names all three values: \"Select whether this is an accrual, a forecast, or "
       "a plan from this field.\"",
       "observed", JCREW,
       [
        n("Accrual", "code-value", "A real accounting entry.", "observed", JCREW),
        n("Forecast", "code-value", "A projection, not posted.", "observed", JCREW),
        n("Plan", "code-value", "A budget figure.", "observed", JCREW),
       ]),
     n("Blank rentable area is not the same as zero", "constraint",
       "Vendor definition: \"If you are not going to use rentable area, do not enter 0. Leave this "
       "field blank.\" A real behavioural difference between empty and zero.",
       "observed", JCREW),
    ]),
  n("ExpenseAccrualSchedule", "entity",
    "31 fields holding the generated period-by-period amounts, plus growth and cap percentages for "
    "the forecast and plan variants. Physical table: expense_accrual_schedule.",
    "observed", JCREW,
    [rule("ACC-R-052", "Accrual amount derivation",
          "Entering any one of the annual amount, period amount or accrual rate auto-fills the other "
          "two plus the first and last payment amounts.", "observed")]),
  n("AccrualTransaction", "entity",
    "55 fields — the individual posting. Carries eight organisation account numbers plus sixteen more "
    "copied down from the expense type, and four tax amounts. Physical table: accrual_transaction.",
    "observed", OBJ,
    [
     n("TaxesIncludedFlag flips which field is editable", "constraint",
       "If taxes are not included, the total is computed and read-only. If they are included, the "
       "period amount is disabled, the system subtracts the taxes from it, and the total becomes "
       "editable. Two different data-entry modes on one record.",
       "observed", JCREW,
       [rule("ACC-R-053", "Accrual transaction tax handling",
             "Both branches are stated verbatim by the vendor.", "observed")]),
     n("ProcessedFlag", "field",
       "Vendor definition carries its own warning: \"Warning - once you mark a transaction as "
       "processed, you cannot change it.\"",
       "observed", JCREW,
       [rule("ACC-R-054", "Accrual transaction immutability",
             "Processed accrual transactions are frozen.", "observed")]),
    ]),
 ])

ifrs = n(
 "IFRS 16", "submodule",
 "The international counterpart to ASC 842. In this data model it is not a second engine — it is one "
 "extra code table, one routing key repeated on five objects, seven measurement columns, and a flag. "
 "Everything else is shared verbatim with ASC 842.",
 "observed", IF16,
 [
  n("CodeIFRS16Schedule (TableType 2163) — empty", "code-table",
    "24 columns, structurally identical to its ASC 842 and straight-line twins: a name, a long "
    "description, an inactive flag, one amortisation switch, and twenty GL account slots. Opened "
    "directly on 2026-09-10 and it returns 'No rows to display'. Physical table: "
    "code_i_f_r_s16_schedule.",
    "observed", REG,
    [
     n("With no schedule type, no IFRS 16 schedule can exist", "constraint",
       "The schedule header's IFRS 16 routing key has nothing valid to point at, no expense type can "
       "route to IFRS 16, and the Generate IFRS 16 Rent Schedule button has no type to stamp. The "
       "capability is present in the product and unused by this customer.",
       "derived", IF16),
     n("The measurement columns may still hold data", "constraint",
       "The seven IFRS16-prefixed columns on the classification record are computed per test, "
       "independently of any schedule configuration. So they may well be populated even though no "
       "IFRS 16 schedule has ever been produced. That is the sharpest remaining technical question "
       "on this branch: it separates 'IFRS 16 is dead schema' from 'IFRS 16 measurement runs "
       "silently and nobody looks at it'.",
       "derived", IF16),
    ]),
  n("Building IFRS 16 is a business decision, not a technical one", "constraint",
    "The incumbent supports IFRS 16 and ASG does not use it, so building it in the replacement is a "
    "product choice about future international leases rather than a parity requirement. If the "
    "answer is no, roughly a fifth of the measurement surface drops out along with standard-scoped "
    "accounting dates, standard-scoped practical expedients and a standard dimension on the "
    "discount rate. If the answer is yes, all of those are still needed — but as greenfield design, "
    "because there is no working configuration to copy.",
    "derived", MAP),
  n("No IFRS 16 classification test exists", "constraint",
    "Correctly so — IFRS 16 does not ask lessees to classify leases. But it means every "
    "classification concept in this module is ASC 842's.",
    "observed", IF16),
  n("No IFRS 16 accounting dates exist", "constraint",
    "The only accounting begin and end dates are named for ASC 842 ('the date your organization is "
    "adopting ASC 842'). An entity that adopted IFRS 16 in 2019 and ASC 842 in 2022 cannot express "
    "both transition dates.",
    "observed", IF16),
  n("No IFRS 16 approval workflow exists", "constraint",
    "The tenant runs exactly four workflows and one of them is ASC-842-named. If ASG reports under "
    "IFRS 16, those schedules are ungated. This single question decides how much of the IFRS 16 "
    "surface matters at all.",
    "observed", WF),
  n("Practical expedients are not scoped to a standard", "constraint",
    "'Is Short Term' and 'Is Low Asset Value' exist on both the contract and the asset, unnamespaced "
    "— even though the low-value exemption is an IFRS 16 concept with no ASC 842 equivalent. On the "
    "asset they are three-state (yes / no / unset); on the contract they are plain yes/no.",
    "observed", CSV,
    [n("Three-state versus two-state", "type",
       "The asset versions use a null-checkbox type carrying a meaningful 'unset', which almost "
       "certainly means 'inherit from the contract'. Modelling both as a plain boolean destroys that. "
       "Nothing documents the inheritance rule.",
       "observed", CSV)]),
 ])

output = n(
 "Output surfaces", "submodule",
 "What leaves the engine: journal entries for the customer's finance system, and the disclosure "
 "tables that go into the financial statements.",
 "observed", JCREW,
 [
  n("GL export", "capability",
    "Every period row carries twenty account numbers copied from its schedule type, plus three "
    "straight-line-specific ones. The slots are numbered rather than named, so the mapping from slot "
    "to accounting concept lives entirely in tenant convention.",
    "observed", JCREW),
  n("Roll-forward report", "capability",
    "The asset and liability movement table required in the financial statement notes. Gated by a "
    "single include flag on the schedule header, and built from 25 stored fields that carry no vendor "
    "documentation at all.",
    "observed", CSV),
  n("Maturity analysis", "capability",
    "Future cash commitments laid out by fiscal year, with quarterly detail for the current year. "
    "Six years plus a tail, where the standard asks for five.",
    "observed", JCREW),
  n("ASC 842 Recalculations dashboard widget", "capability",
    "The operational surface for the recalculation queue — a configurable dashboard component "
    "observed in the tenant's widget catalog.",
    "observed", DASH),
 ])

rebuild = n(
 "Rebuild notes for ASG Edge+", "submodule",
 "Where this module meets the replacement system. The target design already exists and is in several "
 "respects better than what it replaces; the work is porting the calculation surface into a "
 "structure that was designed differently on purpose.",
 "derived", MAP,
 [
  n("Money precision conflict", "constraint",
    "The platform's Money type rounds to the currency's natural scale — two decimal places for "
    "dollars. The Accounting Engine requirements document asks for at least four. Amortisation "
    "divides a total across a hundred-odd periods, so rounding each intermediate to cents drifts "
    "visibly over the life of a lease. This must be resolved before any schedule arithmetic is "
    "written.",
    "observed", MAP),
  n("No rate primitive exists", "constraint",
    "Money is the only financial type in the platform. Discount rates, exchange rates (six decimal "
    "places) and threshold percentages all need their own type, or the classic 0.04375-versus-4.375 "
    "unit bug crosses a service boundary sooner or later.",
    "derived", MAP),
  n("The vendor independently forbids floats too", "constraint",
    "Lucernex's live API keeps MONEY and PERCENTAGE distinct from FLOAT and publishes BigDecimal as a "
    "scalar. The all-text database columns are a persistence-layer artefact, not the intended design "
    "— which is a useful argument when the no-doubles rule is questioned.",
    "observed", GQL),
  n("Thresholds should become versioned policy, not columns", "constraint",
    "The classification thresholds, borrowing rates and low-value limits sit on the Portfolio as bare "
    "unversioned columns. The replacement design puts them in an administration screen where each "
    "value is versioned, effective-dated, and approved by a second person — and explicitly does not "
    "retroactively change anything already posted.",
    "observed", BRD),
  n("The schedule approval gate is not in the requirements yet", "constraint",
    "The Accounting Engine requirements cover transaction approval. The gate found in the live tenant "
    "sits one level up, on the schedule that produces those transactions, and involves two parties. "
    "That is a build item, not a port.",
    "derived", MAP),
  n("Fifteen dead fields", "constraint",
    "Fifteen accounting fields are documented by the vendor as no longer used, not implemented, "
    "legacy, or informational-only. Migrate the data for audit; do not implement the behaviour.",
    "observed", CVI),
 ])

root = n(
 "Lease Accounting Engine", "module",
 "The part of Lucernex that turns a lease contract into accounting numbers. It answers three "
 "questions: is this lease effectively a purchase or a rental (classification), what is it worth on "
 "the balance sheet on day one (measurement), and how do those numbers move month by month until it "
 "ends (the schedule). 38 objects and 1,265 fields in the product's own module taxonomy; this map "
 "covers the 20 that carry the calculation, plus the live approval process that governs its output. In production ASG runs "
 "one of the three standards the engine supports: the ASC 842 schedule-type table holds a single "
 "row, and the straight-line and IFRS 16 tables are empty.",
 "observed", "docs/modules/accounting/README.md",
 [spine1, spine2, spine3, policy, approval, accruals, ifrs, output, rebuild])

# ---- validate ----
def depth(node, d=1):
    if not node["children"]:
        return d
    return max(depth(c, d+1) for c in node["children"])

def count(node):
    return 1 + sum(count(c) for c in node["children"])

def deepest_path(node, path=None):
    path = (path or []) + [node["name"]]
    if not node["children"]:
        return path
    best = None
    for c in node["children"]:
        p = deepest_path(c, path)
        if best is None or len(p) > len(best):
            best = p
    return best

KINDS = {"module","submodule","capability","entity","field-group","field","type","rule",
         "constraint","code-table","code-value"}
CONF = {"observed","derived","inferred"}
def validate(node, path="root"):
    assert node["kind"] in KINDS, "bad kind %s at %s" % (node["kind"], path)
    assert node["confidence"] in CONF, "bad confidence %s at %s" % (node["confidence"], path)
    assert node["name"] and node["detail"] and node["source"], "empty field at %s" % path
    for c in node["children"]:
        validate(c, path + " > " + node["name"])
validate(root)

out = "docs/mindmap/accounting-tree.json"
with io.open(out, "w", encoding="utf-8") as f:
    json.dump(root, f, ensure_ascii=False, indent=1)

print("nodes:", count(root))
print("max depth:", depth(root))
for c in root["children"]:
    print("  L2 %-42s depth %2d  nodes %4d" % (c["name"][:42], depth(c)+1, count(c)))
print()
print("deepest path:")
for i, nm in enumerate(deepest_path(root), 1):
    print("  %2d %s%s" % (i, "  "*(i-1), nm))
from collections import Counter
def kinds(node, c=None):
    c = c if c is not None else Counter()
    c[node["kind"]] += 1
    for x in node["children"]: kinds(x, c)
    return c
print()
print("kinds:", dict(kinds(root)))
def confs(node, c=None):
    c = c if c is not None else Counter()
    c[node["confidence"]] += 1
    for x in node["children"]: confs(x, c)
    return c
print("confidence:", dict(confs(root)))
