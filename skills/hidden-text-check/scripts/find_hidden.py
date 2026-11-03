#!/usr/bin/env python3
"""find_hidden.py: list text in a Word file (.docx) that a person reading the page can't see, before an agent reads it.
Flags runs that are white or near-white, smaller than 4 pt, or marked hidden, in the body, tables, headers and footers.
Usage: python3 find_hidden.py FILE.docx [FILE.docx ...]   (needs: pip install python-docx)
Limits: .docx only; it does not read PDFs, images, comments or tracked changes; text colored to match a non-white
background is not caught."""
import sys
try:
    import docx
    from docx.shared import Pt
except ImportError:
    sys.exit("needs python-docx: pip install python-docx")


def paragraphs(d):
    yield from (("body", p) for p in d.paragraphs)
    for t in d.tables:
        for row in t.rows:
            for cell in row.cells:
                yield from (("table", p) for p in cell.paragraphs)
    for s in d.sections:
        for where, part in (("header", s.header), ("footer", s.footer)):
            yield from ((where, p) for p in part.paragraphs)


def why(r):
    out = []
    c = r.font.color.rgb if r.font.color is not None and r.font.color.type is not None else None
    if c is not None and all(int(str(c)[k:k + 2], 16) >= 0xF0 for k in (0, 2, 4)): out.append("white")
    if r.font.size is not None and r.font.size < Pt(4): out.append("tiny")
    if r.font.hidden: out.append("hidden")
    return out


total = 0
for path in sys.argv[1:] or sys.exit(__doc__):
    hits = 0
    for where, p in paragraphs(docx.Document(path)):
        for r in p.runs:
            w = why(r)
            if w and r.text.strip():
                hits += 1
                print(f"{path} [{where}] {' '.join(w)}: {r.text[:200]}")
    print(f"{path}: {hits} hidden run(s)")
    total += hits
sys.exit(1 if total else 0)
