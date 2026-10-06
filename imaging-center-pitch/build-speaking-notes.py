#!/usr/bin/env python3
"""Convert SPEAKING-NOTES-2026-10-20.md into a print-ready rehearsal HTML.

Structure-aware: slide blocks (### SLIDE N) become non-splitting cards,
SAY/THEN SAY/DEPTH/BEAT labels become typographic tiers.
"""
import html
import re
import sys
from pathlib import Path

SRC = Path(__file__).with_name("SPEAKING-NOTES-2026-10-20.md")
OUT = Path(__file__).with_name("speaking-notes-2026-10-20.html")

CSS = """
:root {
  --paper: #faf8f3; --ink: #1c1b18; --soft: #4a4740; --faint: #8a867c;
  --rule: #d9d4c7; --accent: #7a1f2b; --accent-soft: #f1e4e5;
  --serif: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, Georgia, "Times New Roman", serif;
  --sans: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", Helvetica, Arial, sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--sans); color: var(--ink); background: var(--paper); font-size: 12.5pt; line-height: 1.45; }
.sheet { max-width: 7.5in; margin: 0.5in auto; padding: 0 0.25in; }
h1 { font-family: var(--serif); font-weight: 400; font-size: 30pt; line-height: 1.1; margin: 0 0 10pt 0; }
h1.part { font-size: 26pt; border-top: 3px solid var(--ink); padding-top: 14pt; margin-top: 36pt; }
h2 { font-family: var(--serif); font-weight: 400; font-size: 18pt; margin: 22pt 0 8pt 0; }
h3.slide { font-family: var(--serif); font-weight: 400; font-size: 20pt; line-height: 1.15; margin: 0 0 6pt 0; }
h3.slide .num { color: var(--accent); font-weight: 600; font-family: var(--sans); font-size: 11pt; letter-spacing: 0.14em; text-transform: uppercase; display: block; margin-bottom: 4pt; }
h3.slide .clock { color: var(--faint); font-family: var(--sans); font-size: 11pt; letter-spacing: 0.06em; display: block; margin-top: 4pt; }
.kicker { font-size: 10pt; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); font-weight: 600; margin-bottom: 6pt; }
p { margin: 0 0 8pt 0; }
.meta { color: var(--soft); font-size: 12pt; }
.block { border-top: 2px solid var(--ink); padding: 14pt 0 10pt 0; margin: 18pt 0 0 0; page-break-inside: avoid; break-inside: avoid; }
.block .pre { color: var(--soft); font-style: italic; margin-bottom: 8pt; }
.label { font-family: var(--sans); font-size: 10pt; letter-spacing: 0.14em; text-transform: uppercase; font-weight: 700; margin: 12pt 0 4pt 0; color: var(--ink); }
.label.say { color: var(--accent); }
.label.then { color: var(--accent); }
.label.depth { color: var(--faint); }
.label.beat { color: var(--ink); }
.say p { font-family: var(--serif); font-size: 15.5pt; line-height: 1.4; color: var(--ink); border-left: 4px solid var(--accent); padding-left: 12pt; margin-bottom: 9pt; }
.then p { font-family: var(--serif); font-size: 15pt; line-height: 1.4; color: var(--ink); border-left: 4px solid var(--accent); padding-left: 12pt; background: var(--accent-soft); padding-top: 5pt; padding-bottom: 5pt; margin-bottom: 9pt; }
.depth p, .depth li { font-size: 10.5pt; line-height: 1.38; color: var(--soft); }
.depth p { margin-bottom: 6pt; }
.beat p { font-size: 12pt; color: var(--ink); font-weight: 600; }
.beat p::before { content: "\\25B8  "; color: var(--accent); }
ul, ol { margin: 0 0 8pt 18pt; }
li { margin-bottom: 4pt; }
li.task::before { content: "\\2610  "; }
ul.tasks { list-style: none; margin-left: 0; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 12pt 0; font-size: 11pt; page-break-inside: avoid; break-inside: avoid; }
th { text-align: left; font-size: 9pt; letter-spacing: 0.1em; text-transform: uppercase; color: var(--faint); font-weight: 600; padding: 0 8pt 5pt 0; border-bottom: 1.5px solid var(--ink); }
td { padding: 6pt 8pt 6pt 0; border-bottom: 1px solid var(--rule); vertical-align: top; }
code { font-family: Menlo, Consolas, monospace; font-size: 0.92em; background: #efece4; padding: 0 3pt; }
hr { border: 0; border-top: 1px solid var(--rule); margin: 14pt 0; }
.card { border: 2px solid var(--ink); padding: 14pt 16pt; margin: 14pt 0; page-break-inside: avoid; break-inside: avoid; background: #fff; }
.card .say p { font-size: 16pt; }
.strip { border: 2px solid var(--accent); padding: 10pt 14pt; margin: 12pt 0; page-break-inside: avoid; break-inside: avoid; }
.strip h2 { margin-top: 0; color: var(--accent); }
.part-intro { page-break-inside: avoid; break-inside: avoid; }
.drill { page-break-inside: avoid; break-inside: avoid; margin-bottom: 10pt; }
@media print {
  @page { size: letter; margin: 0.6in 0.65in 0.7in 0.65in; }
  body { background: #fff; font-size: 12pt; }
  .sheet { max-width: none; margin: 0; padding: 0; }
  h1.part { page-break-before: always; break-before: page; border-top: 0; margin-top: 0; padding-top: 0; }
  .block, .card, .strip, table, .drill { page-break-inside: avoid; break-inside: avoid; }
  /* every slide starts on a fresh page so the SAY tier is always at the top of a sheet;
     SAY, THEN SAY and BEAT tiers never split; DEPTH may flow to a second page of the same slide */
  .block { page-break-before: always; break-before: page; margin-top: 0; padding-top: 0; border-top: 0; }
  .say, .then, .beat { page-break-inside: avoid; break-inside: avoid; }
  .depth p { page-break-inside: avoid; break-inside: avoid; }
  h2, h3, .label { page-break-after: avoid; break-after: avoid; }
  a { color: inherit; text-decoration: none; }
}
"""

INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_CODE = re.compile(r"`([^`]+)`")


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = INLINE_CODE.sub(r"<code>\1</code>", s)
    s = INLINE_BOLD.sub(r"<b>\1</b>", s)
    return s


def render_table(rows):
    head = rows[0]
    body = rows[2:]
    out = ["<table>", "<thead><tr>"]
    for c in head:
        out.append(f"<th>{inline(c)}</th>")
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


LABELS = {
    "SAY": "say", "SAY, in one breath": "say", "SAY, exactly this, once": "say",
    "THEN SAY (the caveat)": "then", "THEN SAY (two caveats, both mandatory)": "then",
    "THEN SAY (the caveat, on the BAA)": "then",
    "DEPTH / IF ASKED": "depth", "BEAT": "beat",
}


def convert(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    in_block = False      # inside a slide block
    in_part1 = False
    tier = None           # current tier div
    list_open = None      # 'ul' | 'ol' | 'tasks'
    para = []

    def flush_para():
        nonlocal para
        if para:
            text = " ".join(x.strip() for x in para)
            out.append(f"<p>{inline(text)}</p>")
            para = []

    def close_list():
        nonlocal list_open
        if list_open:
            out.append("</ul>" if list_open in ("ul", "tasks") else "</ol>")
            list_open = None

    def close_tier():
        nonlocal tier
        flush_para(); close_list()
        if tier:
            out.append("</div>")
            tier = None

    def close_block():
        nonlocal in_block
        close_tier()
        if in_block:
            out.append("</div>")
            in_block = False

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # tables
        if s.startswith("|"):
            flush_para(); close_list()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i])); i += 1
            out.append(render_table(rows))
            continue

        if s == "":
            flush_para(); close_list(); i += 1; continue

        if s == "---":
            flush_para(); close_list()
            if not in_block:
                out.append("<hr>")
            i += 1; continue

        if s.startswith("# "):
            close_block()
            title = s[2:].strip()
            if title.startswith("PART"):
                out.append(f'<h1 class="part">{inline(title)}</h1>')
                in_part1 = title.startswith("PART 1")
            else:
                out.append(f"<h1>{inline(title)}</h1>")
            i += 1; continue

        if s.startswith("### SLIDE"):
            close_block()
            body = s[4:]
            parts = [p.strip() for p in body.split("·")]
            num = parts[0]
            title = parts[1] if len(parts) > 1 else ""
            clock = parts[2] if len(parts) > 2 else ""
            out.append('<div class="block">')
            out.append(f'<h3 class="slide"><span class="num">{inline(num)}</span>{inline(title)}<span class="clock">{inline(clock)}</span></h3>')
            in_block = True
            i += 1; continue

        if s.startswith("## "):
            close_block()
            title = s[3:].strip()
            if in_part1 and title.startswith("The first 90 seconds"):
                out.append('<div class="card"><div class="kicker">Cold open, verbatim</div>')
                out.append(f"<h2>{inline(title)}</h2>")
                # consume until next heading, wrapping quotes in say tier
                i += 1
                out.append('<div class="say">')
                in_quote = False
                while i < len(lines) and not lines[i].startswith("## ") and not lines[i].startswith("# "):
                    t = lines[i].strip()
                    if t == "" or t == "---":
                        i += 1; continue
                    if t.startswith('"'):
                        in_quote = True
                    if in_quote:
                        out.append(f"<p>{inline(t)}</p>")
                    else:
                        out.append(f'<p class="pre" style="font-family:var(--sans);font-size:12pt;border:0;padding:0;color:var(--soft);">{inline(t)}</p>')
                    if t.endswith('"'):
                        in_quote = False
                    i += 1
                out.append("</div></div>")
                continue
            if in_part1 and title.startswith("The landmine strip"):
                out.append('<div class="strip">')
                out.append(f"<h2>{inline(title)}</h2>")
                i += 1
                while i < len(lines) and not lines[i].startswith("## ") and not lines[i].startswith("# "):
                    t = lines[i]
                    if t.strip().startswith("|"):
                        rows = []
                        while i < len(lines) and lines[i].strip().startswith("|"):
                            rows.append(split_row(lines[i])); i += 1
                        out.append(render_table(rows)); continue
                    if t.strip() and t.strip() != "---":
                        out.append(f"<p>{inline(t.strip())}</p>")
                    i += 1
                out.append("</div>")
                continue
            if title.startswith("Drill"):
                out.append('<div class="drill">')
                out.append(f"<h2>{inline(title)}</h2>")
                i += 1
                # drill body until next ## or #
                while i < len(lines) and not lines[i].startswith("## ") and not lines[i].startswith("# "):
                    t = lines[i]; st = t.strip()
                    if st.startswith("|"):
                        flush_para(); close_list()
                        rows = []
                        while i < len(lines) and lines[i].strip().startswith("|"):
                            rows.append(split_row(lines[i])); i += 1
                        out.append(render_table(rows)); continue
                    if st == "" or st == "---":
                        flush_para(); close_list(); i += 1; continue
                    m = re.match(r"^(\d+)\. (.*)", st)
                    if m:
                        flush_para()
                        if list_open != "ol":
                            close_list(); out.append("<ol>"); list_open = "ol"
                        out.append(f"<li>{inline(m.group(2))}</li>"); i += 1; continue
                    if st.startswith("- "):
                        flush_para()
                        if list_open != "ul":
                            close_list(); out.append("<ul>"); list_open = "ul"
                        out.append(f"<li>{inline(st[2:])}</li>"); i += 1; continue
                    if st.startswith('"') and st.endswith('"') and len(st) > 120:
                        flush_para(); close_list()
                        out.append(f'<div class="say"><p>{inline(st)}</p></div>'); i += 1; continue
                    para.append(st); i += 1
                flush_para(); close_list()
                out.append("</div>")
                continue
            out.append(f"<h2>{inline(title)}</h2>")
            i += 1; continue

        # labels inside a slide block
        if in_block and s.startswith("**") and s.endswith("**"):
            label = s.strip("*").strip()
            cls = LABELS.get(label)
            if cls:
                close_tier()
                out.append(f'<div class="label {cls}">{inline(label)}</div>')
                out.append(f'<div class="{cls}">')
                tier = cls
                i += 1; continue

        # pre-label instruction lines inside a block (before first tier)
        if in_block and tier is None and not s.startswith("-"):
            out.append(f'<p class="pre">{inline(s)}</p>')
            i += 1; continue

        # lists
        if s.startswith("- [ ] "):
            flush_para()
            if list_open != "tasks":
                close_list(); out.append('<ul class="tasks">'); list_open = "tasks"
            out.append(f'<li class="task">{inline(s[6:])}</li>'); i += 1; continue
        if s.startswith("- "):
            flush_para()
            if list_open != "ul":
                close_list(); out.append("<ul>"); list_open = "ul"
            out.append(f"<li>{inline(s[2:])}</li>"); i += 1; continue
        m = re.match(r"^(\d+)\. (.*)", s)
        if m:
            flush_para()
            if list_open != "ol":
                close_list(); out.append("<ol>"); list_open = "ol"
            out.append(f"<li>{inline(m.group(2))}</li>"); i += 1; continue

        # paragraphs: inside say/then tiers each line is its own paragraph
        if tier in ("say", "then", "beat"):
            out.append(f"<p>{inline(s)}</p>")
        else:
            para.append(s)
        i += 1

    close_block()
    flush_para(); close_list()
    return "\n".join(out)


def main():
    md = SRC.read_text(encoding="utf-8")
    body = convert(md)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Speaking Notes: Imaging Center Dinner, El Paso, 2026-10-20</title>
<style>{CSS}</style>
</head>
<body>
<div class="sheet">
{body}
</div>
</body>
</html>
"""
    OUT.write_text(doc, encoding="utf-8")
    print(f"wrote {OUT} ({len(doc)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
