#!/usr/bin/env python3
"""
Render vault/ to docs/site/vault/ — the same notes, readable on the web.

The vault is an Obsidian graph: small notes joined by [[wikilinks]]. Obsidian
resolves those by note *name*, anywhere in the tree. This turns them into real
hrefs so the identical files work in Obsidian, on GitHub, and on the site,
without a second copy.

Also emits a graph index: every note, its folder, and its link degree — the
web equivalent of Obsidian's graph view, which needs a running app.

Re-runnable: wipes and rewrites site/vault/ each time.
"""

import html
import os
import re
import shutil

import gate
from build_research import CSS, brand, render, slug

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
ROOT = os.path.dirname(DOCS)
VAULT = os.path.join(ROOT, "vault")
OUT = os.path.join(DOCS, "site", "vault")

e = html.escape

# note name (lowercased, no extension) -> path relative to vault/
INDEX = {}


def page(title, body, depth=0, toc=None, sub=""):
    up = "../" * depth
    nav = ""
    if toc:
        nav = ('<nav class="toc"><b>On this page</b>' +
               "".join(f'<a href="#{a}">{e(t)}</a>' for a, t in toc) + "</nav>")
    return gate.inject(brand(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} &middot; Lx Vault</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}../atlas.css">
<link rel="stylesheet" href="{up}../research/research.css">
<link rel="stylesheet" href="{up}vault.css">
</head><body>
<header><b>Lx Atlas</b>
<nav><a href="{up}../index.html">Overview</a><a href="{up}../atlas.html#/map?set=feature">Feature map</a>
<a href="{up}../atlas.html">Interactive app</a>
<a href="{up}../research/index.html">Research</a>
<a href="{up}../research/screens.html">Screens</a>
<a href="{up}index.html" class="on">Vault</a>
<a href="{up}../questions.html">Open questions</a></nav></header>
<main><p class="crumb"><a href="{up}../index.html">Atlas</a> &rsaquo;
<a href="{up}index.html">Vault</a>{sub}</p>{nav}{body}</main></body></html>"""))


VCSS = """
.backlinks{margin:34px 0 0;padding:16px 18px;background:var(--card,#fff);
 border:1px solid var(--line,#e5e7eb);border-radius:10px}
.backlinks b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.08em;
 color:var(--muted,#6b7280);margin-bottom:8px}
.backlinks a{display:inline-block;margin:0 12px 6px 0;font-size:13px}
.fm{margin:0 0 22px;font-size:12px;color:var(--muted,#6b7280);
 font-family:'IBM Plex Mono',monospace}
.fm span{display:inline-block;padding:2px 8px;margin-right:6px;border-radius:20px;
 background:rgba(180,83,10,.09);color:var(--accent,#b4530a)}
.fm span.ev{background:rgba(15,23,42,.07);color:#334155}
a.wl{border-bottom:1px solid rgba(180,83,10,.35);text-decoration:none}
a.wl.missing{color:#b91c1c;border-bottom-style:dotted}
"""


def build_index():
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), VAULT)
                INDEX[f[:-3].lower()] = rel
                INDEX[slug(f[:-3])] = rel


def resolve(target, from_rel):
    """[[Note]] or [[Note|label]] -> href relative to the current page."""
    key = target.strip().lower()
    hit = INDEX.get(key) or INDEX.get(slug(target.strip()))
    if not hit:
        return None
    frm = os.path.dirname(from_rel)
    return os.path.relpath(hit[:-3] + ".html", frm or ".").replace(os.sep, "/")


WIKI = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]")


def dewiki(md, rel, missing):
    """Rewrite wikilinks to markdown links before the markdown renderer runs."""
    def sub(m):
        tgt, label = m.group(1), m.group(2)
        href = resolve(tgt, rel)
        text = label or tgt
        if href is None:
            missing.add(tgt.strip())
            return f"**{text}**"      # unresolved: show the text, do not fake a link
        return f"[{text}]({href})"
    return WIKI.sub(sub, md)


def frontmatter(md):
    if not md.startswith("---"):
        return {}, md
    end = md.find("\n---", 3)
    if end == -1:
        return {}, md
    fm = {}
    for line in md[3:end].strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("[]")
    return fm, md[end + 4:]


def main():
    if not os.path.isdir(VAULT):
        print("vault/ not present — skipping")
        return
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "vault.css"), "w", encoding="utf-8").write(CSS + VCSS)

    build_index()
    notes, missing, links = [], set(), {}

    for key, rel in sorted(set(INDEX.items()), key=lambda x: x[1]):
        pass  # INDEX holds two keys per note; iterate files instead

    seen = set()
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, f), VAULT)
            if rel in seen:
                continue
            seen.add(rel)
            md = open(os.path.join(VAULT, rel), encoding="utf-8").read()
            fm, body_md = frontmatter(md)
            outbound = {t.strip() for t, _ in
                        ((m.group(1), m.group(2)) for m in WIKI.finditer(md))}
            links[rel] = outbound
            body_md = dewiki(body_md, rel, missing)
            # images in the vault are relative to vault/, which sits beside docs/
            depth = rel.count(os.sep)
            body_md = re.sub(r"\]\((?!https?:|#)([^)]+\.(?:jpg|jpeg|png|gif|svg))\)",
                             lambda m: "](" + "../" * (depth + 2) + m.group(1).lstrip("./") + ")",
                             body_md)
            # Vault notes reference the corpus as ../docs/X.md. The number of
            # levels to climb is the SAME on the site (vault/ and research/ are
            # siblings under site/, exactly as vault/ and docs/ are siblings in
            # the repo), so swap the segment and do not add a level.
            body_md = re.sub(r"\]\(((?:\.\./)*)docs/([^)]+?)\.md\)",
                             lambda m: f"]({m.group(1)}research/{m.group(2)}.html)",
                             body_md)
            # Non-markdown targets (screenshots, csv) still live at the docs
            # root, which is one level further out than research/.
            body_md = re.sub(r"\]\(((?:\.\./)*)docs/([^)]+?)\)",
                             lambda m: f"]({m.group(1)}../{m.group(2)})", body_md)
            body, toc = render(body_md)
            chips = ""
            if fm:
                bits = []
                if fm.get("tags"):
                    bits += [f"<span>{e(t.strip())}</span>"
                             for t in fm["tags"].split(",") if t.strip()]
                if fm.get("evidence"):
                    bits.append(f'<span class="ev">{e(fm["evidence"])}</span>')
                if bits:
                    chips = '<div class="fm">' + "".join(bits) + "</div>"
            title = fm.get("title") or (re.search(r"^#\s+(.+)$", body_md, re.M).group(1)
                                        if re.search(r"^#\s+(.+)$", body_md, re.M) else f[:-3])
            dest = os.path.join(OUT, rel[:-3] + ".html")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "w", encoding="utf-8").write(
                page(re.sub(r"[`*]", "", title), chips + body, depth, toc,
                     f" &rsaquo; {e(re.sub(r'[`*]', '', title))}"))
            notes.append((rel, re.sub(r"[`*]", "", title), fm, len(outbound)))

    # backlinks
    back = {}
    for src, outs in links.items():
        for t in outs:
            hit = INDEX.get(t.lower()) or INDEX.get(slug(t))
            if hit:
                back.setdefault(hit, set()).add(src)

    # ----- index
    folders = {}
    for rel, title, fm, deg in notes:
        folders.setdefault(os.path.dirname(rel) or ".", []).append((rel, title, deg))
    total_links = sum(d for _, _, _, d in notes)
    b = ["<h1>Vault</h1>",
         "<p class='lead'>The same corpus as a <em>graph</em>: small notes, each about one thing, "
         "joined by links. Open <code>vault/</code> in Obsidian for the graph view, or read it "
         "here &mdash; these are the identical files.</p>",
         '<div class="stats">' + "".join(
             f'<div><b class="mono">{v}</b><span>{k}</span></div>' for k, v in
             [("Notes", len(notes)), ("Links", total_links),
              ("Avg links/note", f"{total_links/max(len(notes),1):.1f}"),
              ("Folders", len(folders))]) + "</div>"]
    if missing:
        b.append(f"<div class='note'><b>{len(missing)} unresolved links.</b> These point at notes "
                 "that do not exist yet; they render as plain text rather than dead links: "
                 + ", ".join(f"<code>{e(x)}</code>" for x in sorted(missing)[:14])
                 + ("&hellip;" if len(missing) > 14 else "") + "</div>")
    for fold in sorted(folders):
        rows = sorted(folders[fold], key=lambda x: x[1])
        label = fold if fold != "." else "root"
        b.append(f"<h2>{e(label)} &middot; {len(rows)}</h2><div class='denselist'>")
        for rel, title, deg in rows:
            b.append(f'<a href="{rel[:-3]}.html">{e(title[:56])}<span>{deg}</span></a>')
        b.append("</div>")
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page("Vault", "".join(b)))

    # backlink blocks appended to each page
    for rel, title, fm, deg in notes:
        srcs = sorted(back.get(rel, []))
        if not srcs:
            continue
        p = os.path.join(OUT, rel[:-3] + ".html")
        s = open(p, encoding="utf-8").read()
        frm = os.path.dirname(rel)
        items = "".join(
            f'<a href="{os.path.relpath(sp[:-3] + ".html", frm or ".")}">'
            f'{e(os.path.basename(sp)[:-3])}</a>' for sp in srcs)
        s = s.replace("</main>", f'<div class="backlinks"><b>Linked from &middot; {len(srcs)}</b>'
                                 f'{items}</div></main>')
        open(p, "w", encoding="utf-8").write(s)

    print(f"vault: {len(notes)} notes, {total_links} links, "
          f"{total_links/max(len(notes),1):.1f} avg, {len(missing)} unresolved")


if __name__ == "__main__":
    main()
