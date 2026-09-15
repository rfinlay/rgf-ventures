#!/usr/bin/env python3
"""
Build a Word .docx from the Tailscale operator runbook markdown.

Purpose: Rick needs a printable/readable runbook in hand at Luis's house on
2026-09-16. This is a field document, not a report -- so it optimises for
"can I follow this on a laptop with one hand" rather than for looking pretty.

Handles: h1-h4, paragraphs, bold/inline-code runs, fenced code blocks,
GFM tables, bullet/numbered lists, blockquotes, horizontal rules.

Usage:  python3 build_runbook_docx.py <input.md> <output.docx> ["Doc Title"]
"""
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

MONO = "Consolas"
BODY = "Calibri"
ACCENT = RGBColor(0x1F, 0x4E, 0x79)
CODE_BG = "F2F2F2"
WARN_BG = "FFF4E5"


def shade(el, hexfill):
    """Apply a background fill to a paragraph or table cell element."""
    pr = el.get_or_add_pPr() if hasattr(el, "get_or_add_pPr") else el.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto")
    sh.set(qn("w:fill"), hexfill)
    pr.append(sh)


def add_runs(par, text):
    """Parse **bold**, `code`, and [label](url) into runs on a paragraph."""
    # Links -> "label (url)" so a printed page keeps the destination.
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 (\2)", text)
    for tok in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            r = par.add_run(tok[2:-2])
            r.bold = True
        elif tok.startswith("`") and tok.endswith("`"):
            r = par.add_run(tok[1:-1])
            r.font.name = MONO
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0xA3, 0x15, 0x15)
        else:
            par.add_run(tok)


def code_block(doc, lines):
    for ln in lines:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.left_indent = Inches(0.22)
        r = p.add_run(ln if ln.strip() else " ")
        r.font.name = MONO
        r.font.size = Pt(9)
        shade(p._p, CODE_BG)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def is_table_row(s):
    return s.strip().startswith("|") and s.strip().endswith("|")


def split_row(s):
    return [c.strip() for c in s.strip().strip("|").split("|")]


def build(src, out, title):
    md = open(src, encoding="utf-8").read().split("\n")

    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = BODY
    st.font.size = Pt(10.5)
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(0.7)
        s.left_margin = s.right_margin = Inches(0.75)

    i = 0
    first_h1 = True
    while i < len(md):
        ln = md[i]
        s = ln.strip()

        # fenced code
        if s.startswith("```"):
            i += 1
            buf = []
            while i < len(md) and not md[i].strip().startswith("```"):
                buf.append(md[i])
                i += 1
            i += 1
            code_block(doc, buf)
            continue

        # tables
        if is_table_row(s) and i + 1 < len(md) and re.match(r"^\|[\s:|-]+\|$", md[i + 1].strip()):
            hdr = split_row(s)
            i += 2
            rows = []
            while i < len(md) and is_table_row(md[i].strip()):
                rows.append(split_row(md[i].strip()))
                i += 1
            t = doc.add_table(rows=1, cols=len(hdr))
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for c, htxt in enumerate(hdr):
                cell = t.rows[0].cells[c]
                cell.text = ""
                add_runs(cell.paragraphs[0], htxt)
                for r in cell.paragraphs[0].runs:
                    r.bold = True
                shade(cell._tc, "DEEAF6")
            for row in rows:
                cells = t.add_row().cells
                for c, val in enumerate(row[: len(hdr)]):
                    cells[c].text = ""
                    add_runs(cells[c].paragraphs[0], val)
                    for p in cells[c].paragraphs:
                        p.paragraph_format.space_after = Pt(2)
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
            continue

        if s.startswith("#### "):
            h = doc.add_heading(level=4)
            add_runs(h, s[5:])
        elif s.startswith("### "):
            h = doc.add_heading(level=3)
            add_runs(h, s[4:])
        elif s.startswith("## "):
            h = doc.add_heading(level=2)
            add_runs(h, s[3:])
            for r in h.runs:
                r.font.color.rgb = ACCENT
        elif s.startswith("# "):
            if first_h1:
                h = doc.add_heading(level=0)
                add_runs(h, title or s[2:])
                first_h1 = False
            else:
                h = doc.add_heading(level=1)
                add_runs(h, s[2:])
        elif s in ("---", "***", "___"):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(6)
            pb = OxmlElement("w:pBdr")
            b = OxmlElement("w:bottom")
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "6")
            b.set(qn("w:color"), "BFBFBF")
            pb.append(b)
            p._p.get_or_add_pPr().append(pb)
        elif s.startswith("> "):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            add_runs(p, s[2:])
            shade(p._p, WARN_BG)
        elif re.match(r"^[-*+] ", s):
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, s[2:])
        elif re.match(r"^\d+\. ", s):
            p = doc.add_paragraph(style="List Number")
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, re.sub(r"^\d+\.\s+", "", s))
        elif not s:
            pass
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(5)
            add_runs(p, s)
        i += 1

    doc.save(out)
    print("wrote", out)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
