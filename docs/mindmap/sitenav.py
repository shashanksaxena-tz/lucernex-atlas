#!/usr/bin/env python3
"""
One navigation, shared by every generator that writes into docs/site/.

The site used to offer nine peers in a flat bar — Overview, Feature map,
Interactive app, Research, Screens, Vault, Record types, Rules, Open questions —
with nothing saying which to use when. It read as nine separate projects, which
is exactly what the owner said: *"all of these things are going in a direction
where it is not really connected."*

The organising idea here is SCALE. One subject, looked at from different
heights: what the product is, how a capability works, what a user sees, what is
underneath, and how it all joins up. Every view belongs to one rung of that
ladder, and every page says which rung it is on.

The markup was duplicated in three `page()` functions and had already drifted —
build_site.py rendered ten links, build_research.py eight, build_vault.py seven,
each with its own idea of relative depth. It lives here now so it cannot drift
again.

Read-only. Imported by build_site.py, build_research.py and build_vault.py.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
VAULT = os.path.join(os.path.dirname(DOCS), "vault")

# ---------------------------------------------------------------- the ladder
# (key, label, href from the site root, one line saying what it is FOR)
# The one-liner is not decoration: a reader who arrives deep, from a search or a
# link, needs to know what they are looking at without going back to the index.

SECTIONS = [
    ("Understand", "What the product is, and what each part of it does.", [
        ("overview", "Overview", "index.html",
         "The whole product in two paragraphs, and a route to whichever scale you need."),
        ("features", "Feature areas", "features/index.html",
         "Every capability the product has, in product language: what it does, who for, "
         "through which screens, governed by which rules."),
    ]),
    ("Explore", "Follow a thread, at whatever depth it takes you.", [
        ("featuremap", "Feature map", "atlas.html#/map?set=feature",
         "The product as one expandable tree, organised by what it does."),
        ("schemamap", "Schema map", "atlas.html#/map",
         "The same product as records, fields and foreign keys. The graph is cyclic, so "
         "you can keep following keys indefinitely."),
        ("vault", "Vault", "vault/index.html",
         "The same findings as small linked notes. Start anywhere and follow the links — "
         "this is the view for wandering rather than looking something up."),
    ]),
    ("Reference", "Look one thing up.", [
        ("entities", "Record types", "entities/index.html",
         "Every record the product stores, what it is for, and every field on it."),
        ("rules", "Rules", "rules/index.html",
         "Every numbered rule, stated so a rule engine could consume it, with the "
         "evidence label the source document gave it."),
        ("datamodel", "Data model", "research/data-model/index.html",
         "The schema itself: the object catalogue, the foreign-key graph, the type "
         "system, and both APIs."),
        ("markdown", "Markdown", "markdown.html",
         "Every page on this site as a markdown file, for pasting into a ticket or a spec."),
    ]),
    ("Evidence", "What the claims rest on, and what is still unknown.", [
        ("screens", "Screens", "research/screens.html",
         "The 179 captured screens — the product as a user actually sees it."),
        ("research", "Research", "research/index.html",
         "The written corpus: feature manuals, module analyses, tenant comparisons, "
         "admin tools."),
        ("questions", "Open questions", "questions.html",
         "The things nobody has confirmed. Each one is work somebody has to do before "
         "the thing it blocks can be built."),
    ]),
]

# key -> (label, href, purpose)
BY_KEY = {k: (label, href, why)
          for _sec, _blurb, items in SECTIONS for k, label, href, why in items}


def purpose(key):
    """The one-line 'what this view is for', shown at the top of the view."""
    return BY_KEY.get(key, ("", "", ""))[2]


def nav_html(root, current=""):
    """The grouped navigation.

    `root` is the prefix from the current page to the site root — "" for a page
    at the root, "../" one level down, and so on. Passing the wrong depth here is
    the defect that took broken references from 13 to 3,001 once already, so it
    is the ONE thing a caller has to get right, and it is the same argument for
    every generator.
    """
    out = []
    for section, blurb, items in SECTIONS:
        links = []
        for key, label, href, _why in items:
            on = ' class="on"' if key == current else ""
            links.append(f'<a href="{root}{href}"{on}>{label}</a>')
        out.append(f'<span class="navgrp" title="{blurb}"><b>{section}</b>'
                   + "".join(links) + "</span>")
    return '<nav class="sitenav">' + "".join(out) + "</nav>"


NAV_CSS = """
nav.sitenav{margin-left:auto;display:flex;gap:18px;flex-wrap:wrap;align-items:baseline}
nav.sitenav .navgrp{display:flex;gap:9px;align-items:baseline;flex-wrap:wrap}
nav.sitenav .navgrp b{font-size:9px;letter-spacing:.1em;text-transform:uppercase;
 color:var(--faint);font-weight:600;white-space:nowrap}
nav.sitenav a{font-size:12.5px;color:var(--ink2);white-space:nowrap}
nav.sitenav a:hover{color:var(--accent)}
nav.sitenav a.on{color:var(--accent);font-weight:600}
.viewfor{font-size:12.5px;color:var(--muted);border-left:2px solid var(--line);
 padding:2px 0 2px 11px;margin:0 0 18px;max-width:72ch}
.ladder{display:grid;gap:1px;background:var(--line2);border:1px solid var(--line2);
 border-radius:var(--r);overflow:hidden;margin:0 0 26px}
.ladder a{display:grid;grid-template-columns:150px 1fr;gap:16px;background:var(--surface);
 padding:13px 16px;color:inherit}
.ladder a:hover{background:var(--surface2);text-decoration:none}
.ladder b{font-size:13.5px;font-weight:600}
.ladder b span{display:block;font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;
 color:var(--faint);font-weight:600;margin-top:2px}
.ladder p{margin:0;font-size:12.5px;color:var(--muted);max-width:none}
.seealso{display:flex;gap:9px;flex-wrap:wrap;margin:0 0 20px}
.seealso a{font-size:12px;padding:5px 10px;border:1px solid var(--line);border-radius:var(--r);
 background:var(--surface);color:var(--ink2)}
.seealso a:hover{border-color:var(--accent);color:var(--ink);text-decoration:none}
.seealso i{font-style:normal;color:var(--faint);margin-right:5px}
"""


# ------------------------------------------------------------ the vault index
# The vault names its notes by convention, so joining to it is a name lookup
# rather than a search: entities/<Object>.md, features/feature-<slug>.md,
# rules/rule-<ID>.md, modules/module-<id>.md.

def vault_index():
    """{(kind, key): path under site/vault/} for the notes worth cross-linking."""
    out = {}
    if not os.path.isdir(VAULT):
        return out
    for kind in ("entities", "features", "rules", "modules", "screens", "concepts"):
        d = os.path.join(VAULT, kind)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            stem = fn[:-3]
            key = stem
            for prefix in ("feature-", "rule-", "module-", "screen-", "concept-"):
                if stem.startswith(prefix):
                    key = stem[len(prefix):]
                    break
            out[(kind, key)] = "vault/%s/%s.html" % (kind, stem)
    return out


def vault_link(index, kind, key):
    """The vault note for one subject, or None."""
    return index.get((kind, key))


# --------------------------------------------------------- coverage owners
# docs/tools/coverage-owners.json is the hand-curated surface-name -> owning-doc
# map that COVERAGE.md is built from. Only its `adminTools` bucket joins to the
# screenshot filenames: captures in this corpus are named after admin tools and
# never after layouts, navigation screens, workflows or form types. That is a
# naming convention, not missing evidence — a layout with no capture named for it
# is normal, and its image has to come from the citation index instead.

def coverage_owners():
    import json
    p = os.path.join(DOCS, "tools", "coverage-owners.json")
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def admin_tool_shots(shot_index, owners=None):
    """{admin tool name: (owning doc, [capture paths])} — a clean three-way join.

    Returns the misses too, because a name in the owners file that resolves to
    no capture is a free audit of naming drift between the two.
    """
    owners = owners if owners is not None else coverage_owners()
    tools = owners.get("adminTools") or {}
    hit, miss = {}, []
    for name, doc in sorted(tools.items()):
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        shots = shot_index.get(slug, [])
        if shots:
            hit[name] = (doc, shots)
        else:
            miss.append(name)
    return hit, miss


if __name__ == "__main__":
    vi = vault_index()
    print("sections   %d, %d links"
          % (len(SECTIONS), sum(len(i) for _s, _b, i in SECTIONS)))
    print("vault      %d linkable notes" % len(vi))
    for kind in ("entities", "features", "rules", "modules"):
        print("  %-9s %d" % (kind, sum(1 for k in vi if k[0] == kind)))
    import corpus
    hit, miss = admin_tool_shots(corpus.shot_index())
    print("adminTools %d resolve to a capture, %d do not" % (len(hit), len(miss)))
    print("  misses:", ", ".join(miss))
