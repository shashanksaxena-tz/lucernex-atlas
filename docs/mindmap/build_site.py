#!/usr/bin/env python3
"""
Generate docs/site/ — a browsable static HTML mirror of the atlas.

One real file per node, so every record type, module and rule has its own page
that opens with a double-click, works from the filesystem with no server, and
can be linked to, printed, or handed to somebody who will never open the
interactive app.

  site/index.html                 the entry point
  site/modules/<id>.html          module pages
  site/entities/<Name>.html       record-type pages, one anchor per field
  site/features/<area>.html       one page per feature-map area
  site/rules/index.html           the rule index
  site/rules/<ID>.html            one page per numbered rule
  site/questions.html             the open questions
  site/markdown.html              the markdown index
  site/md/**.md                   the same content as markdown, one file per node
  site/atlas.html                 the interactive app, copied in

Every node in either map resolves to both an HTML page and a markdown document,
and every page states what the thing IS before it states how big it is.

Re-runnable: wipes and rewrites site/ each time, except research/, which
build_research.py owns and which runs after this.
"""

import html
import json
import os
import re
import shutil

import gate

# --------------------------------------------------------------- branding
# The product's name is removed from all published output. Applied at the
# point of emission so it holds however the upstream data was generated.
# Technical identifiers (LxRetail, lxID, Lx.ui.*) are already "Lx"-prefixed
# and unaffected; only the bare product name is rewritten.
_BRAND = re.compile(r"\bLucernex\b(?!\s*(?:IWMS|Atlas)\b)")


def brand(s):
    s = s.replace("Lucernex IWMS", "Lx").replace("Lucernex Atlas", "Lx Atlas")
    return _BRAND.sub("Lx", s)


HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
SITE = os.path.join(DOCS, "site")


def load(n):
    with open(os.path.join(HERE, n), encoding="utf-8") as fh:
        return json.load(fh)


M = load("mapdata.json")
R = load("rules.json")
Q = load("questions.json")
F = load("findings.json")
FM = load("featuremap.json")

meta, objects, modules = M["meta"], M["objects"], M["modules"]
edges = M["edges"]
group_blurb = M.get("groupBlurb", {})
type_legend = M.get("typeLegend", {})
rule_by_id = {r["id"]: r for r in R["rules"]}
rules_by_entity = R.get("byEntity", {})
q_by_area = {}
for _q in Q["questions"]:
    q_by_area.setdefault(_q["area"], []).append(_q)

FLAG_FIRM, FLAG_REQ, FLAG_RO = 1, 2, 4
FLAG_INV_REQ, FLAG_FUNC, FLAG_NOPG = 8, 16, 32
role_note = M.get("roleNote", {})

edges_from, edges_to = {}, {}
for e in edges:
    edges_from.setdefault(e[0], []).append(e)
    if e[3]:
        edges_to.setdefault(e[3], []).append(e)

mod_by_id = {m["id"]: m for m in modules}
HUES = ["#4E7CA1", "#7A6BA8", "#3F8A78", "#A8743F", "#8A5470", "#5B7F45", "#9A5B4C",
        "#4C6E9E", "#7E7A46", "#6A5D95", "#3E8395", "#8C6A3F", "#5D8A5C", "#96566A", "#6E7683"]
hue = {m["id"]: HUES[i % len(HUES)] for i, m in enumerate(modules)}

e = html.escape
def fmt(n): return f"{n:,}" if isinstance(n, int) else (n or "")
def slug(s): return re.sub(r"[^A-Za-z0-9_.-]", "_", s)

CONF = {"observed": ("obs", "Observed"), "derived": ("der", "Derived"),
        "inferred": ("inf", "Inferred")}
def ctag(c):
    k, l = CONF.get(c, CONF["derived"])
    return f'<span class="tag {k}">{l}</span>'


CSS = """
:root{--bg:#E7EAEE;--surface:#F8F9FB;--surface2:#EEF1F5;--ink:#12161C;--ink2:#3D4650;
 --muted:#6B7480;--faint:#9AA3AF;--line:#C4CBD4;--line2:#DDE2E8;--accent:#0E6E7E;
 --accent-soft:#D3E7EA;--ok:#2F6B45;--warn:#8A5A12;--info:#2B5590;--r:3px}
@media (prefers-color-scheme:dark){:root{--bg:#0D1116;--surface:#141A21;--surface2:#1B222B;
 --ink:#E6EAEF;--ink2:#BAC3CD;--muted:#8B95A2;--faint:#67727F;--line:#2A323C;--line2:#212932;
 --accent:#48BFD2;--accent-soft:#16323A;--ok:#6FBF8C;--warn:#D6A34A;--info:#7FA9E0}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
 font-family:"IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
 font-size:14px;line-height:1.55;-webkit-font-smoothing:antialiased}
.mono{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;font-variant-numeric:tabular-nums}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header{background:var(--surface);border-bottom:1px solid var(--line);padding:10px 22px;
 display:flex;gap:16px;align-items:baseline;flex-wrap:wrap;position:sticky;top:0;z-index:5}
header b{font-size:15px}header nav{margin-left:auto;display:flex;gap:14px;font-size:13px;flex-wrap:wrap}
main{max-width:1000px;margin:0 auto;padding:26px 22px 90px}
h1{font-size:27px;font-weight:600;letter-spacing:-.02em;margin:0 0 4px}
h1.mono{font-size:23px}
.sub{color:var(--muted);font-size:13px;margin:0 0 20px}
.crumb{font-size:11.5px;color:var(--muted);margin:0 0 12px}
h2{margin:28px 0 10px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
 font-weight:600;border-bottom:1px solid var(--line2);padding-bottom:6px}
p{max-width:70ch;color:var(--ink2)}p.lead{font-size:15px;max-width:66ch}
.tag{display:inline-block;font-size:9.5px;letter-spacing:.07em;text-transform:uppercase;padding:2px 6px;
 border-radius:2px;border:1px solid var(--line);color:var(--muted);margin:0 4px 4px 0}
.tag.obs{color:var(--ok);border-color:currentColor}
.tag.der{color:var(--info);border-color:currentColor}
.tag.inf{color:var(--warn);border-color:currentColor}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(112px,1fr));gap:1px;background:var(--line2);
 border:1px solid var(--line2);border-radius:var(--r);overflow:hidden;margin:0 0 22px}
.stats div{background:var(--surface);padding:11px 13px}
.stats b{display:block;font-size:21px;font-weight:600;letter-spacing:-.02em}
.stats span{display:block;font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(262px,1fr));gap:11px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:13px 15px;display:block;color:inherit}
.card:hover{border-color:var(--accent);text-decoration:none}
.card.oos{border-style:dashed;opacity:.75}
.card h3{margin:0 0 5px;font-size:14px;font-weight:600;display:flex;gap:7px;align-items:center}
.card .hue{width:3px;height:14px;border-radius:2px;flex:none}
.card p{margin:0 0 8px;font-size:12.5px;color:var(--muted);max-width:none}
.card .row{display:flex;gap:12px;font-size:10.5px;color:var(--faint)}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th,td{padding:6px 9px;text-align:left;border-bottom:1px solid var(--line2);vertical-align:top}
th{background:var(--surface2);color:var(--muted);font-weight:600;font-size:9.5px;
 letter-spacing:.07em;text-transform:uppercase;position:sticky;top:0;z-index:1}
.wrapt{max-height:none}
td.num,th.num{text-align:right;font-family:"IBM Plex Mono",monospace}
tr:target td{background:var(--accent-soft)}
.wrapt{border:1px solid var(--line2);border-radius:var(--r);overflow:auto;margin:0 0 8px}
dl{display:grid;grid-template-columns:auto 1fr;gap:5px 16px;font-size:13px;margin:0 0 18px}
dt{color:var(--muted);white-space:nowrap}dd{margin:0}
.find{background:var(--surface);border:1px solid var(--line);border-left:3px solid var(--accent);
 border-radius:var(--r);padding:11px 14px;margin:0 0 9px}
.find h4{margin:0 0 4px;font-size:13.5px}.find p{margin:0;font-size:12.5px;max-width:none}
.item{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:10px 13px;margin:0 0 7px}
.item .m{font-size:10.5px;color:var(--faint);margin-top:5px}
.grp{margin:0 0 16px}
.grp h3{margin:0 0 4px;font-size:14px;font-weight:600}
.grp .gb{font-size:12.5px;color:var(--muted);margin:0 0 7px;max-width:70ch}
.note{background:var(--surface2);border:1px solid var(--line2);border-radius:var(--r);
 padding:10px 13px;font-size:12.5px;color:var(--ink2);margin:0 0 18px}
.btn{display:inline-block;font-size:12.5px;padding:7px 12px;background:var(--surface);
 color:var(--ink2);border:1px solid var(--line);border-radius:var(--r);margin:0 6px 8px 0}
.btn:hover{border-color:var(--accent);color:var(--ink);text-decoration:none}
.shots{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px;margin:0 0 18px}
.shots a{display:block;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;
 background:var(--surface);color:var(--muted)}
.shots a:hover{border-color:var(--accent);text-decoration:none}
.shots img{width:100%;display:block;background:var(--surface2)}
.shots span{display:block;padding:5px 8px;font-size:10.5px;word-break:break-all}
"""


def page(title, body, depth=0, crumb=""):
    up = "../" * depth
    return gate.inject(brand(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} &middot; Lx Atlas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}atlas.css">
</head><body>
<header><b>Lx Atlas</b>
<nav><a href="{up}index.html">Overview</a><a href="{up}atlas.html#/map?set=feature">Feature map</a>
<a href="{up}atlas.html">Interactive app</a>
<a href="{up}features/index.html">Features</a>
<a href="{up}entities/index.html">Record types</a><a href="{up}rules/index.html">Rules</a>
<a href="{up}research/index.html">Research</a>\n<a href="{up}research/screens.html">Screens</a>\n<a href="{up}vault/index.html">Vault</a><a href="{up}markdown.html">Markdown</a>
<a href="{up}questions.html">Open questions</a></nav></header>
<main>{crumb}{body}</main></body></html>"""))


# --------------------------------------------------------------------- rebuild
# Preserve research/ across a rebuild: build_research.py owns it and runs after
# this script. Wiping SITE wholesale would delete it on every atlas rebuild.
# Preserve the sub-sites this script does not own. build_research.py and
# build_vault.py write into site/ too and run after this one; wiping SITE
# wholesale deletes their output, which is easy to miss because the next
# rebuild of *those* scripts silently restores it. Keep this list in sync.
_OWNED_ELSEWHERE = ("research", "vault", "md")
_stash = os.path.join(DOCS, "_site_keep")
if os.path.isdir(_stash):
    shutil.rmtree(_stash)
os.makedirs(_stash, exist_ok=True)
for _d in _OWNED_ELSEWHERE:
    _src = os.path.join(SITE, _d)
    if os.path.isdir(_src):
        shutil.move(_src, os.path.join(_stash, _d))
if os.path.isdir(SITE):
    shutil.rmtree(SITE)
os.makedirs(SITE, exist_ok=True)
for _d in os.listdir(_stash):
    shutil.move(os.path.join(_stash, _d), os.path.join(SITE, _d))
shutil.rmtree(_stash, ignore_errors=True)
for d in ("", "modules", "entities", "rules", "features",
          "md", "md/modules", "md/entities", "md/rules", "md/features"):
    os.makedirs(os.path.join(SITE, d), exist_ok=True)


# ------------------------------------------------------------------- markdown
# Every node resolves to a real markdown document as well as an HTML page: the
# HTML is for reading in a browser, the markdown is what somebody pastes into a
# ticket, a spec, or another tool. Same content, one generator.

MD_INDEX = []


def write_md(rel, title, lines):
    """Write one markdown document and record it for the markdown index."""
    path = os.path.join(SITE, "md", rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    body = brand("\n".join(lines).rstrip() + "\n")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)
    MD_INDEX.append((rel, title))
    return "md/" + rel


def md_link(depth, rel):
    """A link from an HTML page down to its markdown twin."""
    return (f'<p><a class="btn" href="{"../" * depth}md/{rel}">'
            f'Read this page as Markdown &rarr;</a></p>')


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    out.append("")
    return out


CONF_WORD = {"observed": "Observed", "derived": "Derived", "inferred": "Inferred"}


def scope_of(flags, code):
    if flags & FLAG_FIRM:
        return "Firm"
    return "Global" if code else "—"

with open(os.path.join(SITE, "atlas.css"), "w", encoding="utf-8") as fh:
    fh.write(CSS)

built = os.path.join(HERE, "lucernex-atlas.built.html")
if os.path.exists(built):
    shutil.copyfile(built, os.path.join(SITE, "atlas.html"))

NOTE = ('<div class="note">These pages are generated from the same data as the interactive app. '
        'Notes and the mind map live in <a href="atlas.html">the app</a> &mdash; these files are for '
        'reading, linking and printing.</div>')


def mod_card(m, up=""):
    return (f'<a class="card {"" if m["scope"] else "oos"}" href="{up}modules/{slug(m["id"])}.html">'
            f'<h3><span class="hue" style="background:{hue[m["id"]]}"></span>{e(m["title"])}</h3>'
            f'<p>{e(m["what"][:190])}</p><div class="row"><span>{m["oc"]} records</span>'
            f'<span>{fmt(m["fc"])} fields</span><span>{m["ei"]} in</span><span>{m["eo"]} out</span>'
            f'</div></a>')


# ------------------------------------------------------------------- index
stats = [("Modules", meta["modules"]), ("Record types", meta["objects"]),
         ("Fields", fmt(meta["fields"])), ("Foreign keys", meta["edges"]),
         ("Rules", fmt(R["total"])), ("Open questions", fmt(Q["total"])),
         ("Data Fields", fmt(meta["datafields"])), ("API types", meta["gqlTypes"])]
body = [f'<h1>Lx, as it actually runs</h1>',
        f'<p class="sub">{e(meta["vendor"])} &middot; {e(meta["tenant"])} &middot; build {e(meta["build"])} &middot; captured {e(meta["captured"])}</p>',
        NOTE.replace('href="atlas.html"', 'href="atlas.html"'),
        '<p class="lead">Everything here was read out of the live application and its own schema tools. '
        'Every claim carries an evidence label &mdash; <b>Observed</b> means somebody saw it, '
        '<b>Inferred</b> means nobody has yet.</p>',
        '<p><a class="btn" href="atlas.html#/map?set=feature">Open the feature map '
        '&mdash; the product by what it does &rarr;</a> '
        '<a class="btn" href="atlas.html#/map">Open the schema map &mdash; every record, '
        'field and key &rarr;</a></p>',
        '<div class="stats">' + "".join(
            f'<div><b class="mono">{v}</b><span>{k}</span></div>' for k, v in stats) + '</div>',
        """<h2>The running product</h2>
<p>The pages below the fold describe the <em>schema</em>. This section describes what two live
tenants actually do &mdash; where they differ, what the product does that the schema cannot show,
and what that means for a rebuild. Every claim is labelled Observed, Derived or Inferred.</p>
<div class="cards">
<a class="card" href="research/index.html"><h3>Research &rarr;</h3>
<p>Two tenants on build 26.09.0.113, read live: the full AF/BBW comparison, feature-by-feature
accounts, the REST API explained, 134 screens, and a coverage tracker that says what is still
missing.</p><div class="row"><span>17 documents</span><span>34 data captures</span></div></a>
<a class="card" href="research/tenants/bbw-vs-american-freight.html"><h3>AF vs BBW</h3>
<p>What one tenant has that the other does not, why a navigation root can be invisible, and how
configuration is published between firms and then forks.</p>
<div class="row"><span>27 sections</span></div></a>
<a class="card" href="features/index.html"><h3>Features &rarr;</h3>
<p>The feature map as pages: what the product does, who for, through which screens, governed by
which rules, with the open questions and the captured screens attached to each area.</p>
<div class="row"><span>21 areas</span></div></a>
<a class="card" href="vault/index.html"><h3>Vault &rarr;</h3>
<p>The same corpus as a graph: 200+ small notes, each about one thing, densely linked. Open
<code>vault/</code> in Obsidian for the graph view, or read it here &mdash; identical files.</p>
<div class="row"><span>graph view</span></div></a>
<a class="card" href="research/screens.html"><h3>Screens &rarr;</h3>
<p>179 captured screens from both tenants &mdash; every administration tool, and the only end-user
screens ever taken. Full width, click through for full resolution.</p>
<div class="row"><span>179 images</span></div></a>
<a class="card" href="research/data-model/api/index.html"><h3>The REST API</h3>
<p>One generic CRUD controller serving all 227 record types. 141 paths, 160 operations, and the
envelope that makes HTTP&nbsp;200 an unreliable success signal.</p>
<div class="row"><span>160 operations</span></div></a>
</div>""",
        '<h2>Modules</h2><div class="cards">' +
        "".join(mod_card(m) for m in modules if m["scope"]) + '</div>',
        '<h2>Excluded by decision</h2><div class="cards">' +
        "".join(mod_card(m) for m in modules if not m["scope"]) + '</div>']
open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(page("Overview", "".join(body)))

# ----------------------------------------------------------------- modules
for m in modules:
    rules = [r for r in R["rules"] if r["module"] == m["id"] or r["moduleTitle"] == m["title"]]
    finds = F.get(m["id"], [])
    b = [f'<p class="crumb"><a href="../index.html">Atlas</a> &rsaquo; {e(m["title"])}</p>',
         f'<h1>{e(m["title"])}</h1>',
         f'<p class="sub">{"In scope for the rebuild" if m["scope"] else "Out of scope by decision"}</p>',
         f'<p class="lead">{e(m["what"])}</p>',
         (f'<p>{e(m["lead"])}</p>' if m.get("lead") else ''),
         f'<p><a class="btn" href="../atlas.html#/map?set=feature&amp;f={e(m["id"])}">'
         f'Open this feature in the feature map &rarr;</a></p>',
         '<div class="stats">' + "".join(
             f'<div><b class="mono">{v}</b><span>{k}</span></div>' for k, v in
             [("Record types", m["oc"]), ("Fields", fmt(m["fc"])), ("Keys in", m["ei"]),
              ("Keys out", m["eo"]), ("Rules", len(rules))]) + '</div>']
    if finds:
        b.append('<h2>What was found here</h2>')
        b += [f'<div class="find"><h4>{e(t)} {ctag(c)}</h4><p>{e(d)}</p></div>' for t, c, d in finds]
    if m.get("dep"):
        b.append('<h2>Depends on</h2><div class="cards">' + "".join(
            mod_card(mod_by_id[d], "../") for d in m["dep"] if d in mod_by_id) + '</div>')
    b.append(f'<h2>Record types &middot; {m["oc"]}</h2><div class="wrapt"><table>'
             '<thead><tr><th>Record type</th><th>Postgres table</th><th class="num">Fields</th>'
             '<th class="num">Referenced by</th></tr></thead><tbody>')
    for n in m["objects"]:
        o = objects.get(n)
        if not o:
            continue
        b.append(f'<tr><td><a class="mono" href="../entities/{slug(n)}.html">{e(n)}</a></td>'
                 f'<td class="mono" style="color:var(--muted)">{e(o["t"] or "—")}</td>'
                 f'<td class="num">{fmt(o["n"])}</td>'
                 f'<td class="num">{fmt(len(edges_to.get(n, [])))}</td></tr>')
    b.append('</tbody></table></div>')
    if rules:
        b.append(f'<h2>Rules &middot; {len(rules)}</h2><div class="wrapt"><table>'
                 '<thead><tr><th>Rule</th><th>Subject</th><th>Confidence</th></tr></thead><tbody>')
        for r in rules:
            b.append(f'<tr><td><a class="mono" href="../rules/{slug(r["id"])}.html">{e(r["id"])}</a></td>'
                     f'<td><b>{e(r.get("section") or "")}</b>'
                     f'<div style="color:var(--muted);font-size:11.5px">'
                     f'{e((r.get("statement") or r.get("text") or "")[:190])}</div></td>'
                     f'<td>{ctag(r["conf"])}</td></tr>')
        b.append('</tbody></table></div>')

    md = [f"# {m['title']}", "",
          f"*{'In scope for the rebuild' if m['scope'] else 'Out of scope by decision'}*", "",
          m["what"], ""]
    if m.get("lead"):
        md += [m["lead"], ""]
    md += md_table(["", "Count"], [["Record types", m["oc"]], ["Fields", fmt(m["fc"])],
                                   ["Keys in", m["ei"]], ["Keys out", m["eo"]],
                                   ["Rules", len(rules)]])
    if finds:
        md += ["## What was found here", ""]
        for t, c, d in finds:
            md += [f"### {t}", "", f"**{CONF_WORD.get(c, c)}.** {d}", ""]
    md += ["## Record types", ""]
    md += md_table(["Record type", "Postgres table", "Fields", "Referenced by"],
                   [[f"[{n}](../entities/{slug(n)}.md)", f"`{objects[n]['t'] or '—'}`",
                     fmt(objects[n]["n"]), fmt(len(edges_to.get(n, [])))]
                    for n in m["objects"] if n in objects])
    if rules:
        md += ["## Rules", ""]
        md += md_table(["Rule", "Subject", "What it requires", "Confidence"],
                       [[f"[{r['id']}](../rules/{slug(r['id'])}.md)", r.get("section") or "",
                         (r.get("statement") or "")[:200], CONF_WORD.get(r["conf"], r["conf"])]
                        for r in rules])
    write_md("modules/%s.md" % slug(m["id"]), m["title"], md)
    b.append(md_link(1, "modules/%s.md" % slug(m["id"])))
    open(os.path.join(SITE, "modules", slug(m["id"]) + ".html"), "w", encoding="utf-8").write(page(m["title"], "".join(b), depth=1))

# ---------------------------------------------------------------- entities
names = sorted(objects, key=lambda n: -objects[n]["n"])
rows = []
for n in names:
    o = objects[n]
    mm = mod_by_id.get(o["m"])
    rows.append(f'<tr><td><a class="mono" href="{slug(n)}.html">{e(n)}</a></td>'
                f'<td style="font-size:11.5px"><a href="../modules/{slug(o["m"])}.html">'
                f'{e(mm["title"] if mm else o["m"])}</a></td>'
                f'<td class="mono" style="color:var(--muted)">{e(o["t"] or "—")}</td>'
                f'<td class="num">{fmt(o["n"])}</td>'
                f'<td class="num">{fmt(len(edges_to.get(n, [])))}</td></tr>')
open(os.path.join(SITE, "entities", "index.html"), "w", encoding="utf-8").write(page(
    "All record types",
    f'<h1>All record types</h1><p class="sub">{len(names)}, largest first</p>'
    '<div class="wrapt"><table><thead><tr><th>Record type</th><th>Module</th>'
    '<th>Postgres table</th><th class="num">Fields</th><th class="num">Ref by</th></tr></thead>'
    '<tbody>' + "".join(rows) + '</tbody></table></div>', depth=1))

for n in names:
    o = objects[n]
    mm = mod_by_id.get(o["m"])
    ins = edges_to.get(n, [])
    outs = [x for x in edges_from.get(n, []) if x[3]]
    by_src = {}
    for x in ins:
        by_src.setdefault(x[0], []).append(x[1])
    b = [f'<p class="crumb"><a href="../index.html">Atlas</a> &rsaquo; '
         f'<a href="../modules/{slug(o["m"])}.html">{e(mm["title"] if mm else o["m"])}</a> &rsaquo; {e(n)}</p>',
         f'<h1 class="mono">{e(n)}</h1>',
         f'<p class="sub">{fmt(o["n"])} fields'
         + (f' &middot; split across {o["tc"]} physical tables' if o["tc"] > 1 else '') + '</p>',
         '<dl>'
         f'<dt>Postgres table</dt><dd class="mono">{e(o["t"] or "none exported")}</dd>'
         f'<dt>Module</dt><dd><a href="../modules/{slug(o["m"])}.html">{e(mm["title"] if mm else o["m"])}</a></dd>'
         f'<dt>Referenced by</dt><dd>{fmt(len(ins))} keys from {len(by_src)} record types</dd>'
         f'<dt>Points at</dt><dd>{fmt(len(outs))} other records</dd>'
         + (f'<dt>Catalogued fields</dt><dd>{fmt(o["cat"][0])} '
            f'({fmt(o["cat"][1])} global, {fmt(o["cat"][2])} firm)</dd>' if o.get("cat") else '')
         + (f'<dt>Fields with a definition</dt><dd>{fmt(o["inv"][1])} of '
            f'{fmt(o["inv"][0])} inventoried</dd>' if o.get("inv") else '')
         + (f'<dt>Physical tables</dt><dd class="mono">{e(", ".join(o["pgt"]))}</dd>'
            if o.get("pgt") else '')
         + (f'<dt>Replication database</dt><dd class="mono">{e(o["pgdb"])}</dd>'
            if o.get("pgdb") else '')
         + '</dl>']

    # what the record IS, in the catalogue's own words, before any statistics
    if o.get("d"):
        b.append(f'<p class="lead">{e(o["d"])}</p>')
        if o.get("ds"):
            b.append('<p style="font-size:11.5px;color:var(--faint)">Source: '
                     + ", ".join(f'<code>{e(s)}</code>' for s in o["ds"]) + '</p>')

    ent_rules = [rule_by_id[i] for i in rules_by_entity.get(n, []) if i in rule_by_id]
    if o.get("notes"):
        b.append('<h2>What to know before rebuilding this</h2>')
        for t, c, d in o["notes"]:
            b.append(f'<div class="find"><h4>{e(t)} {ctag(c)}</h4><p>{e(d)}</p></div>')
    if ent_rules:
        b.append(f'<h2>Rules that govern it &middot; {len(ent_rules)}</h2>'
                 '<div class="wrapt"><table><thead><tr><th>Rule</th><th>What it requires</th>'
                 '<th>Confidence</th></tr></thead><tbody>')
        for r in ent_rules:
            b.append(f'<tr><td><a class="mono" href="../rules/{slug(r["id"])}.html">{e(r["id"])}</a></td>'
                     f'<td>{e((r.get("statement") or r.get("section") or "")[:220])}</td>'
                     f'<td>{ctag(r["conf"])}</td></tr>')
        b.append('</tbody></table></div>')

    b.append('<h2>Fields</h2>')
    for g, fields in o["g"]:
        b.append(f'<div class="grp"><h3>{e(g)} <span class="tag">{len(fields)}</span></h3>')
        if group_blurb.get(g):
            b.append(f'<p class="gb">{e(group_blurb[g])}</p>')
        b.append('<div class="wrapt"><table><thead><tr><th>Field</th><th>Label</th>'
                 '<th>What it is for</th><th>Declared type</th><th>Scope</th><th>Req</th>'
                 '<th>Physical column</th><th>Points at</th></tr></thead><tbody>')
        for f in fields:
            fn, ft, fam = f[0], f[1], f[2]
            label, flags, code = (f[3] if len(f) > 3 else ""), (f[4] if len(f) > 4 else 0), \
                                 (f[5] if len(f) > 5 else "")
            fdef = f[6] if len(f) > 6 else ""
            frole = f[7] if len(f) > 7 else ""
            fpg = f[8] if len(f) > 8 else ""
            tgt = ""
            if fam == "fk":
                ed = next((x for x in edges_from.get(n, []) if x[1] == fn), None)
                if ed and ed[3] and ed[3] in objects:
                    tgt = f'<a class="mono" href="{slug(ed[3])}.html">{e(ed[3])}</a>'
                else:
                    tgt = '<span style="color:var(--faint)">unresolved</span>'
            elif fam == "dropdown":
                cm = re.search(r"\(([^)]+)\)", ft)
                tgt = f'<span style="color:var(--muted)">{e(cm.group(1) if cm else "code table")}</span>'
            b.append(f'<tr id="f-{slug(fn)}"><td class="mono">{e(fn)}'
                     + (f'<div style="font-size:10px;color:var(--faint)">{e(frole)}</div>'
                        if frole else '')
                     + f'</td><td style="font-size:11.5px">{e(label)}</td>'
                     f'<td style="font-size:11.5px;color:var(--ink2);max-width:46ch">{e(fdef)}</td>'
                     f'<td style="color:var(--muted)" title="{e(type_legend.get(code, ""))}">{e(ft)}</td>'
                     f'<td style="font-size:11px;color:var(--muted)">{e(scope_of(flags, code))}</td>'
                     f'<td style="font-size:11px">{"yes" if flags & (FLAG_REQ | FLAG_INV_REQ) else ""}</td>'
                     f'<td class="mono" style="font-size:10.5px;color:var(--muted)">'
                     + (e(fpg.replace(":", " · ")) if fpg
                        else ('not extracted' if flags & FLAG_NOPG else ''))
                     + f'</td><td>{tgt}</td></tr>')
        b.append('</tbody></table></div></div>')
    if by_src:
        b.append(f'<h2>What points here &middot; {fmt(len(ins))} keys</h2><div class="wrapt"><table>'
                 '<thead><tr><th>Record type</th><th>Via column</th></tr></thead><tbody>')
        for s, cols in sorted(by_src.items(), key=lambda x: -len(x[1])):
            b.append(f'<tr><td><a class="mono" href="{slug(s)}.html">{e(s)}</a></td>'
                     f'<td class="mono" style="font-size:11.5px;color:var(--muted)">{e(", ".join(cols))}</td></tr>')
        b.append('</tbody></table></div>')

    # --- the same record, as markdown
    md = [f"# {n}", "",
          f"*{fmt(o['n'])} fields"
          + (f", split across {o['tc']} physical tables" if o["tc"] > 1 else "")
          + f" · module: {mm['title'] if mm else o['m']}"
          + f" · Postgres: `{o['t'] or 'none exported'}`*", ""]
    if o.get("d"):
        md += [o["d"], ""]
        if o.get("ds"):
            md += ["Source: " + ", ".join("`%s`" % s for s in o["ds"]), ""]
    md += ["## At a glance", ""]
    md += md_table(["", "Value"], [
        ["Fields declared", fmt(o["n"])],
        ["Fields with a vendor definition",
         (f"{fmt(o['inv'][1])} of {fmt(o['inv'][0])} inventoried") if o.get("inv") else "—"],
        ["Physical tables", ", ".join("`%s`" % t for t in o.get("pgt") or []) or "—"],
        ["Replication database", ("`%s`" % o["pgdb"]) if o.get("pgdb") else "—"],
        ["Catalogued fields", (f"{fmt(o['cat'][0])} ({fmt(o['cat'][1])} global, "
                               f"{fmt(o['cat'][2])} firm)") if o.get("cat") else "not in the catalogue"],
        ["Physical tables", fmt(o["tc"])],
        ["Referenced by", f"{fmt(len(ins))} keys from {len(by_src)} record types"],
        ["Points at", f"{fmt(len(outs))} other records"],
        ["Tenancy position", o.get("pe") or "—"],
        ["Rules that name it", fmt(len(ent_rules))],
    ])
    if o.get("notes"):
        md += ["## What to know before rebuilding this", ""]
        for t, c, d in o["notes"]:
            md += [f"### {t}", "", f"**{CONF_WORD.get(c, c)}.** {d}", ""]
    if ent_rules:
        md += ["## Rules that govern it", ""]
        md += md_table(["Rule", "What it requires", "Confidence"],
                       [[f"[{r['id']}](../rules/{slug(r['id'])}.md)",
                         (r.get("statement") or r.get("section") or "")[:240],
                         CONF_WORD.get(r["conf"], r["conf"])] for r in ent_rules])
    md += ["## Fields", ""]
    for g, fields in o["g"]:
        md += [f"### {g} ({len(fields)})", ""]
        if group_blurb.get(g):
            md += [group_blurb[g], ""]
        rows = []
        for f in fields:
            fn, ft, fam = f[0], f[1], f[2]
            label = f[3] if len(f) > 3 else ""
            flags = f[4] if len(f) > 4 else 0
            code = f[5] if len(f) > 5 else ""
            fdef = f[6] if len(f) > 6 else ""
            fpg = f[8] if len(f) > 8 else ""
            tgt = ""
            if fam == "fk":
                ed = next((x for x in edges_from.get(n, []) if x[1] == fn), None)
                tgt = (f"[{ed[3]}]({slug(ed[3])}.md)"
                       if ed and ed[3] and ed[3] in objects else "unresolved")
            elif fam == "dropdown":
                cm = re.search(r"\(([^)]+)\)", ft)
                tgt = cm.group(1) if cm else "code table"
            rows.append([f"`{fn}`", label, fdef, ft, scope_of(flags, code),
                         "yes" if flags & (FLAG_REQ | FLAG_INV_REQ) else "",
                         ("`%s`" % fpg.replace(":", " · ")) if fpg
                         else ("not extracted" if flags & FLAG_NOPG else ""), tgt])
        md += md_table(["Field", "Label", "What it is for", "Declared type", "Scope",
                        "Req", "Physical column", "Points at"], rows)
    if by_src:
        md += [f"## What points here ({fmt(len(ins))} keys)", ""]
        md += md_table(["Record type", "Via column"],
                       [[f"[{s}]({slug(s)}.md)", ", ".join(f"`{c}`" for c in cols)]
                        for s, cols in sorted(by_src.items(), key=lambda x: -len(x[1]))])
    rel = write_md("entities/%s.md" % slug(n), n, md)
    b.append(md_link(1, "entities/%s.md" % slug(n)))
    open(os.path.join(SITE, "entities", slug(n) + ".html"), "w", encoding="utf-8").write(page(n, "".join(b), depth=1))

# ------------------------------------------------------------------- rules
by_mod = {}
for r in R["rules"]:
    by_mod.setdefault(r["moduleTitle"], []).append(r)
b = [f'<h1>Rules</h1><p class="sub">{fmt(R["total"])} numbered rules</p>',
     '<p class="lead">Each is stated so a rule engine could consume it. The confidence label is the one '
     'the source document gave it &mdash; an <b>Inferred</b> rule is a hypothesis somebody still has to '
     'confirm.</p>']
for mt, rs in sorted(by_mod.items(), key=lambda x: -len(x[1])):
    b.append(f'<h2>{e(mt)} &middot; {len(rs)}</h2><div class="wrapt"><table>'
             '<thead><tr><th>Rule</th><th>Subject</th><th>Confidence</th></tr></thead><tbody>')
    for r in rs:
        b.append(f'<tr><td><a class="mono" href="{slug(r["id"])}.html">{e(r["id"])}</a></td>'
                 f'<td><b>{e(r.get("section") or "")}</b>'
                 f'<div style="color:var(--muted);font-size:11.5px">'
                 f'{e((r.get("statement") or r.get("text") or "")[:190])}</div></td>'
                 f'<td>{ctag(r["conf"])}</td></tr>')
    b.append('</tbody></table></div>')
open(os.path.join(SITE, "rules", "index.html"), "w", encoding="utf-8").write(page("Rules", "".join(b), depth=1))

for r in R["rules"]:
    b = [f'<p class="crumb"><a href="../index.html">Atlas</a> &rsaquo; '
         f'<a href="index.html">Rules</a> &rsaquo; {e(r["id"])}</p>',
         f'<h1 class="mono">{e(r["id"])}</h1>',
         f'<p class="sub">{e(r["moduleTitle"])} &middot; {e(r.get("section") or "")}</p>',
         ctag(r["conf"])]
    # the rule itself, stated, before anything else on the page
    if r.get("statement"):
        b.append(f'<p class="lead">{e(r["statement"])}</p>')
    if r.get("detail"):
        b.append(f'<p>{e(r["detail"])}</p>')
    if r.get("parts"):
        b.append('<h2>Stated for a rule engine</h2><div class="wrapt"><table><tbody>' +
                 "".join(f'<tr><th style="width:150px">{e(a)}</th><td>{e(bd)}</td></tr>'
                         for a, bd in r["parts"]) + '</tbody></table></div>')
    elif r.get("cells"):
        b.append('<div class="wrapt"><table><tbody>' +
                 "".join(f'<tr><td>{e(c)}</td></tr>' for c in r["cells"]) + '</tbody></table></div>')
    elif r.get("text"):
        b.append(f'<p>{e(r["text"])}</p>')
    if r.get("quote"):
        b.append(f'<div class="find"><h4>The wording it rests on {ctag("observed")}</h4>'
                 f'<p>&ldquo;{e(r["quote"])}&rdquo;</p></div>')
    if r.get("objects"):
        b.append('<h2>What it constrains</h2><p>' + ", ".join(
            (f'<a class="mono" href="../entities/{slug(o)}.html">{e(o)}</a>'
             if o in objects else f'<span class="mono">{e(o)}</span>') for o in r["objects"])
            + '</p>')
    if r.get("fields"):
        b.append('<p style="font-size:12px;color:var(--muted)">Columns named: '
                 + ", ".join(f'<code>{e(c)}</code>' for c in r["fields"]) + '</p>')
    if r.get("related"):
        b.append('<h2>Rules it cites</h2><p>' + ", ".join(
            f'<a class="mono" href="{slug(i)}.html">{e(i)}</a>' for i in r["related"]) + '</p>')
    if r.get("confNote"):
        b.append(f'<p style="font-size:12px;color:var(--muted)">Confidence: {e(r["confNote"])}</p>')
    b.append(f'<p style="font-size:11.5px;color:var(--faint);margin-top:18px">Source: '
             f'<code>docs/{e(r["doc"])}</code></p>')

    md = [f"# {r['id']} — {r.get('section') or ''}".rstrip(" —"), "",
          f"*{r['moduleTitle']} · {CONF_WORD.get(r['conf'], r['conf'])}*", ""]
    if r.get("statement"):
        md += ["**" + r["statement"].rstrip(".") + ".**", ""]
    if r.get("detail"):
        md += [r["detail"], ""]
    if r.get("parts"):
        md += ["## Stated for a rule engine", ""]
        md += md_table(["", ""], [[a, bd] for a, bd in r["parts"]])
    elif r.get("text"):
        md += [r["text"], ""]
    if r.get("quote"):
        md += ["## The wording it rests on", "", "> " + r["quote"], ""]
    if r.get("objects"):
        md += ["## What it constrains", "",
               ", ".join((f"[{o}](../entities/{slug(o)}.md)" if o in objects else o)
                         for o in r["objects"]), ""]
    if r.get("fields"):
        md += ["Columns named: " + ", ".join("`%s`" % c for c in r["fields"]), ""]
    if r.get("related"):
        md += ["## Rules it cites", "",
               ", ".join(f"[{i}]({slug(i)}.md)" for i in r["related"]), ""]
    if r.get("confNote"):
        md += ["## Confidence", "", r["confNote"], ""]
    md += ["---", "", f"Source: `docs/{r['doc']}`", ""]
    write_md("rules/%s.md" % slug(r["id"]), r["id"], md)
    b.append(md_link(1, "rules/%s.md" % slug(r["id"])))
    open(os.path.join(SITE, "rules", slug(r["id"]) + ".html"), "w", encoding="utf-8").write(page(r["id"], "".join(b), depth=1))

# --------------------------------------------------------------- questions
by_area = {}
for q in Q["questions"]:
    by_area.setdefault(q["area"], []).append(q)
b = [f'<h1>Open questions</h1><p class="sub">{fmt(Q["total"])} things nobody has confirmed yet</p>',
     '<p class="lead">Every one of these is a thing somebody has to go and find out. They are the '
     'corpus&rsquo;s most actionable output.</p>']
for area, qs in sorted(by_area.items(), key=lambda x: -len(x[1])):
    b.append(f'<h2>{e(area)} &middot; {len(qs)}</h2>')
    b += [f'<div class="item">{e(q["q"])}<div class="m">{e(q["doc"])}</div></div>' for q in qs]
open(os.path.join(SITE, "questions.html"), "w", encoding="utf-8").write(page("Open questions", "".join(b)))

# ---------------------------------------------------------------- features
# The feature map's areas, each as a real page. The map shows the shape; these
# pages are what a delivery lead reads, and what survives being printed.

def fslug(name):
    return slug(re.sub(r"[^A-Za-z0-9 ]", "", name).strip().lower().replace(" ", "-"))


def feature_body(n, depth, md=False):
    """Render one feature node and everything beneath it, HTML or markdown."""
    out = []

    def walk(node, level):
        title = node.get("name", "")
        kind = node.get("kind", "")
        conf = node.get("conf", "derived")
        rid = node.get("rid")
        detail = node.get("detail") or ""
        if md:
            h = "#" * min(6, level + 1)
            head = f"{h} {title}"
            if rid:
                head += f" — [{rid}](../rules/{slug(rid)}.md)"
            out.append(head)
            out.append("")
            out.append(f"*{CONF_WORD.get(conf, conf)} · {kind}"
                       + (f" · source: `{node['src']}`" if node.get("src") else "") + "*")
            out.append("")
            if rid and rid in rule_by_id:
                r = rule_by_id[rid]
                if r.get("statement"):
                    out.append("**" + r["statement"].rstrip(".") + ".**")
                    out.append("")
                if r.get("parts"):
                    out.extend(md_table(["", ""], [[a, bd] for a, bd in r["parts"]]))
            elif detail:
                out.append(detail)
                out.append("")
            if node.get("shots"):
                out.extend(f"![{os.path.basename(sp)}](../../{sp})" for sp in node["shots"])
                out.append("")
        else:
            out.append(f'<h{min(6, level + 2)}>{e(title)}</h{min(6, level + 2)}>')
            out.append(ctag(conf))
            if rid:
                out.append(f'<a class="tag" href="{"../" * depth}rules/{slug(rid)}.html">{e(rid)}</a>')
            if rid and rid in rule_by_id and rule_by_id[rid].get("statement"):
                out.append(f'<p class="lead">{e(rule_by_id[rid]["statement"])}</p>')
            elif detail:
                out.append(f'<p>{e(detail)}</p>')
            if node.get("src"):
                out.append(f'<p style="font-size:11px;color:var(--faint)">Source: '
                           f'<code>{e(node["src"])}</code></p>')
            # the captured screens themselves, not a list of their filenames
            if node.get("shots"):
                out.append('<div class="shots">' + "".join(
                    f'<a href="{"../" * depth}../{e(sp)}">'
                    f'<img loading="lazy" src="{"../" * depth}../{e(sp)}" alt="{e(os.path.basename(sp))}">'
                    f'<span>{e(os.path.basename(sp))}</span></a>'
                    for sp in node["shots"]) + '</div>')
        for c in node.get("children") or []:
            walk(c, level + 1)

    for c in n.get("children") or []:
        walk(c, 1)
    return out


feature_areas_out = []
for a in FM["root"].get("children") or []:
    name = a.get("name", "")
    fs = fslug(name)
    feature_areas_out.append((fs, name, a))
    b = [f'<p class="crumb"><a href="../index.html">Atlas</a> &rsaquo; '
         f'<a href="index.html">Features</a> &rsaquo; {e(name)}</p>',
         f'<h1>{e(name)}</h1>',
         (f'<p class="sub">Out of scope by decision</p>' if a.get("oos") else ''),
         f'<p class="lead">{e(a.get("detail") or "")}</p>',
         f'<p><a class="btn" href="../atlas.html#/map?set=feature&amp;f={e(a.get("key") or "")}">'
         f'Open this feature in the map &rarr;</a></p>']
    b += feature_body(a, 1)
    md = [f"# {name}", "", a.get("detail") or "", ""]
    md += feature_body(a, 1, md=True)
    write_md("features/%s.md" % fs, name, md)
    b.append(md_link(1, "features/%s.md" % fs))
    open(os.path.join(SITE, "features", fs + ".html"), "w", encoding="utf-8").write(
        page(name, "".join(b), depth=1))

b = [f'<h1>Features</h1><p class="sub">{len(feature_areas_out)} areas, '
     f'{FM["meta"]["nodes"]} nodes</p>',
     f'<p class="lead">{e(FM["meta"]["detail"])}</p>',
     '<div class="cards">']
for fs, name, a in feature_areas_out:
    b.append(f'<a class="card {"oos" if a.get("oos") else ""}" href="{fs}.html">'
             f'<h3>{e(name)}</h3><p>{e((a.get("detail") or "")[:210])}</p>'
             f'<div class="row"><span>{len(a.get("children") or [])} branches</span></div></a>')
b.append('</div>')
open(os.path.join(SITE, "features", "index.html"), "w", encoding="utf-8").write(
    page("Features", "".join(b), depth=1))

# --------------------------------------------------------------- md index
MD_INDEX.sort()
by_kind = {}
for rel, title in MD_INDEX:
    by_kind.setdefault(rel.split("/")[0], []).append((rel, title))
mb = [f'<h1>Markdown pages</h1><p class="sub">{len(MD_INDEX)} documents</p>',
      '<p class="lead">Every node in either map resolves to a markdown document as well as '
      'an HTML page. These are the files to paste into a ticket, a spec, or another tool &mdash; '
      'the same content as the HTML, without the chrome.</p>']
for kind, items in sorted(by_kind.items()):
    mb.append(f'<h2>{e(kind)} &middot; {len(items)}</h2><div class="wrapt"><table><tbody>')
    for rel, title in items:
        mb.append(f'<tr><td><a href="md/{e(rel)}">{e(title)}</a></td>'
                  f'<td class="mono" style="color:var(--muted);font-size:11px">md/{e(rel)}</td></tr>')
    mb.append('</tbody></table></div>')
open(os.path.join(SITE, "markdown.html"), "w", encoding="utf-8").write(
    page("Markdown pages", "".join(mb)))

with open(os.path.join(SITE, "md", "index.md"), "w", encoding="utf-8") as fh:
    fh.write(brand("# Lx Atlas — markdown pages\n\n"
                   "One document per node. %d files.\n\n" % len(MD_INDEX)
                   + "\n".join("- [%s](%s)" % (t, r) for r, t in MD_INDEX) + "\n"))

# ------------------------------------------------------------------ report
count = sum(len(f) for _, _, f in os.walk(SITE))
size = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(SITE) for f in fs)
print(f"wrote {SITE}")
print(f"  {count} files, {size / 1048576:.1f} MB")
print(f"  {len(modules)} modules, {len(names)} record types, {R['total']} rules, {Q['total']} questions")
print(f"  {len(feature_areas_out)} feature pages, {len(MD_INDEX)} markdown documents")
