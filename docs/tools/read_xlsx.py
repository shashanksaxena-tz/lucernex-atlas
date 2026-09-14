"""Minimal xlsx reader — standard library only, matching the repo's build chain.

The subtlety that bites: a self-closing empty cell (<c r="E2" s="2"/>) must be
matched BEFORE the open/close form, otherwise `[^>]*` happily consumes the
trailing slash, the regex looks ahead for the next </c>, and the cell swallows
its neighbour — silently shifting every value after it by one column.
"""
import html as H
import re
import zipfile

_CELL = re.compile(r'<c\b([^>]*?)/>|<c\b([^>]*?)>(.*?)</c>', re.S)
_COL = re.compile(r'r="([A-Z]+)\d+"')
_TYP = re.compile(r't="(\w+)"')


def _colnum(s):
    n = 0
    for ch in s:
        n = n * 26 + ord(ch) - 64
    return n - 1


def read(path, sheet_index=0):
    z = zipfile.ZipFile(path)
    ss = []
    if "xl/sharedStrings.xml" in z.namelist():
        x = z.read("xl/sharedStrings.xml").decode("utf-8", "replace")
        ss = [H.unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", si, re.S)))
              for si in re.findall(r"<si>(.*?)</si>", x, re.S)]
    names = [n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml$", n)]
    data = z.read(sorted(names)[sheet_index]).decode("utf-8", "replace")
    out = []
    for row in re.findall(r"<row[^>]*>(.*?)</row>", data, re.S):
        vals, auto = {}, 0
        for m in _CELL.finditer(row):
            attrs = m.group(1) if m.group(1) is not None else m.group(2)
            inner = m.group(3) or ""
            cm = _COL.search(attrs or "")
            idx = _colnum(cm.group(1)) if cm else auto
            auto = idx + 1
            tm = _TYP.search(attrs or "")
            t = tm.group(1) if tm else "n"
            v = re.search(r"<v>(.*?)</v>", inner, re.S)
            istr = re.search(r"<is>.*?<t[^>]*>(.*?)</t>", inner, re.S)
            if istr:
                val = H.unescape(istr.group(1))
            elif v is None:
                val = ""
            elif t == "s":
                i = v.group(1)
                val = ss[int(i)] if i.isdigit() and int(i) < len(ss) else ""
            else:
                val = H.unescape(v.group(1))
            vals[idx] = val
        if vals:
            out.append([vals.get(i, "") for i in range(max(vals) + 1)])
    return out
