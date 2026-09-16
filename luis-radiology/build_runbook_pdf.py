#!/usr/bin/env python3
"""
Build a fixed-layout PDF from the day-of runbook markdown.

Why a PDF and not just the .docx: Rick reads this on an iPad while typing
commands into someone else's laptop. A PDF opens in Files/Books with no app
dependency, never reflows, and keeps code blocks on one line -- which matters
when the line is a command he is retyping.

Usage: python3 build_runbook_pdf.py <input.md> <output.pdf> ["Doc Title"]
"""
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ACCENT = colors.HexColor("#1F4E79")
CODE_BG = colors.HexColor("#F2F2F2")
CODE_FG = colors.HexColor("#A31515")
WARN_BG = colors.HexColor("#FFF4E5")
HDR_BG = colors.HexColor("#DEEAF6")

ss = getSampleStyleSheet()

S = {
    "title": ParagraphStyle("t", parent=ss["Title"], fontSize=19, leading=23,
                            textColor=ACCENT, spaceAfter=10),
    "h1": ParagraphStyle("h1", parent=ss["Heading1"], fontSize=14, leading=17,
                         textColor=ACCENT, spaceBefore=12, spaceAfter=5),
    "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontSize=12.5, leading=15,
                         textColor=ACCENT, spaceBefore=11, spaceAfter=4),
    "h3": ParagraphStyle("h3", parent=ss["Heading3"], fontSize=11, leading=14,
                         textColor=colors.HexColor("#333333"),
                         spaceBefore=8, spaceAfter=3),
    "h4": ParagraphStyle("h4", parent=ss["Heading4"], fontSize=10.5, leading=13,
                         spaceBefore=6, spaceAfter=2),
    "body": ParagraphStyle("b", parent=ss["BodyText"], fontSize=10, leading=13.5,
                           alignment=TA_LEFT, spaceAfter=5),
    "bullet": ParagraphStyle("bu", parent=ss["BodyText"], fontSize=10, leading=13.5,
                             leftIndent=16, bulletIndent=5, spaceAfter=3),
    "code": ParagraphStyle("c", parent=ss["BodyText"], fontName="Courier",
                           fontSize=8.8, leading=11.5, leftIndent=8,
                           rightIndent=4, spaceAfter=0, spaceBefore=0,
                           backColor=CODE_BG, textColor=colors.black),
    "quote": ParagraphStyle("q", parent=ss["BodyText"], fontSize=10, leading=13.5,
                            leftIndent=14, rightIndent=8, backColor=WARN_BG,
                            borderPadding=5, spaceBefore=4, spaceAfter=6),
    "cell": ParagraphStyle("cl", parent=ss["BodyText"], fontSize=9, leading=11.5,
                           spaceAfter=0),
    "cellh": ParagraphStyle("ch", parent=ss["BodyText"], fontSize=9, leading=11.5,
                            spaceAfter=0, fontName="Helvetica-Bold"),
}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(text):
    """Markdown inline -> reportlab markup. Escape first, then add tags."""
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 (\2)", text)
    out, pos = [], 0
    for m in re.finditer(r"\*\*([^*]+)\*\*|`([^`]+)`", text):
        out.append(esc(text[pos:m.start()]))
        if m.group(1) is not None:
            out.append("<b>%s</b>" % esc(m.group(1)))
        else:
            out.append('<font face="Courier" size="9" color="#A31515">%s</font>'
                       % esc(m.group(2)))
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out)


def is_row(s):
    return s.strip().startswith("|") and s.strip().endswith("|")


def cells(s):
    return [c.strip() for c in s.strip().strip("|").split("|")]


def build(src, out, title):
    md = open(src, encoding="utf-8").read().split("\n")
    doc = SimpleDocTemplate(
        out, pagesize=letter,
        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
        topMargin=0.55 * inch, bottomMargin=0.55 * inch,
        title=title or "Runbook", author="Gio / RGF Global Ventures",
    )
    avail = doc.width
    F = []
    i, first_h1 = 0, True

    while i < len(md):
        s = md[i].strip()

        if s.startswith("```"):
            i += 1
            buf = []
            while i < len(md) and not md[i].strip().startswith("```"):
                buf.append(md[i])
                i += 1
            i += 1
            blk = [Paragraph(esc(ln) if ln.strip() else "&nbsp;", S["code"])
                   for ln in buf]
            F.append(KeepTogether(blk + [Spacer(1, 5)]))
            continue

        if is_row(s) and i + 1 < len(md) and re.match(r"^\|[\s:|-]+\|$", md[i + 1].strip()):
            hdr = cells(s)
            i += 2
            rows = []
            while i < len(md) and is_row(md[i].strip()):
                rows.append(cells(md[i].strip()))
                i += 1
            n = len(hdr)
            data = [[Paragraph(inline(h), S["cellh"]) for h in hdr]]
            for r in rows:
                r = (r + [""] * n)[:n]
                data.append([Paragraph(inline(c), S["cell"]) for c in r])
            t = Table(data, colWidths=[avail / n] * n, repeatRows=1)
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#AAAAAA")),
                ("BACKGROUND", (0, 0), (-1, 0), HDR_BG),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]))
            F.append(t)
            F.append(Spacer(1, 7))
            continue

        if s.startswith("#### "):
            F.append(Paragraph(inline(s[5:]), S["h4"]))
        elif s.startswith("### "):
            F.append(Paragraph(inline(s[4:]), S["h3"]))
        elif s.startswith("## "):
            F.append(Paragraph(inline(s[3:]), S["h2"]))
        elif s.startswith("# "):
            if first_h1:
                F.append(Paragraph(inline(title or s[2:]), S["title"]))
                first_h1 = False
            else:
                F.append(Paragraph(inline(s[2:]), S["h1"]))
        elif s in ("---", "***", "___"):
            F.append(Spacer(1, 3))
            F.append(HRFlowable(width="100%", thickness=0.6,
                                color=colors.HexColor("#BFBFBF")))
            F.append(Spacer(1, 5))
        elif s.startswith("> "):
            F.append(Paragraph(inline(s[2:]), S["quote"]))
        elif re.match(r"^[-*+] ", s):
            F.append(Paragraph(inline(s[2:]), S["bullet"], bulletText="•"))
        elif re.match(r"^\d+\. ", s):
            num = s.split(".", 1)[0]
            F.append(Paragraph(inline(re.sub(r"^\d+\.\s+", "", s)), S["bullet"],
                               bulletText=num + "."))
        elif s:
            F.append(Paragraph(inline(s), S["body"]))
        i += 1

    doc.build(F)
    print("wrote", out)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
