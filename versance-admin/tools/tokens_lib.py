"""Reads design-tokens/tokens.css, the one set of Versance tokens: raw values, var() aliases resolved, and the group / note / source tag of each line."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "design-tokens/tokens.css"
SOURCES = {"both": "Web app and extension", "ext": "Extension style-v1", "app": "Web app", "ours": "Ours (admin tool)"}
GROUP_RE = re.compile(r"\s*/\*\s*((?:Color|Typography|Radius|Spacing|Elevation|Motion|Layout)[^*]*?)\s*\*/\s*$")

def read(path=CANONICAL):
    """[(group, name, raw, note, tag)] in file order; tag is both|ext|app|ours or ''."""
    out, group = [], ""
    for line in Path(path).read_text().splitlines():
        m = GROUP_RE.match(line)
        if m:
            group = m.group(1)
            continue
        c = re.search(r"/\*\s*(.+?)\s*\*/\s*$", line)
        note = c.group(1) if c else ""
        tag = re.match(r"\[(both|ext|app|ours)\]\s*", note)
        note, tag = (note[tag.end():], tag.group(1)) if tag else (note, "")
        for n, v in re.findall(r"(--[a-z0-9-]+)\s*:\s*([^;]+);", re.sub(r"/\*.*?\*/", "", line)):
            out.append((group, n, v.strip(), note, tag))
    return out

def table(tokens=None):
    return {n: raw for _, n, raw, _, _ in (tokens or read())}

def resolve(raw, tbl, seen=()):
    """Replace every var(--x) in a value with that token's own (resolved) value."""
    def sub(m):
        name = m.group(1)
        if name in seen or name not in tbl:
            raise KeyError(f"cannot resolve var({name}) in {raw!r}")
        return resolve(tbl[name], tbl, seen + (name,))
    return re.sub(r"var\((--[a-z0-9-]+)\)", sub, raw)

def resolved(tokens=None):
    tokens = tokens or read()
    tbl = table(tokens)
    return {n: resolve(v, tbl) for n, v in tbl.items()}

def upper_hex(s):
    """The source designs write hex colours in capitals; the canonical file uses lower case."""
    return re.sub(r"#[0-9a-fA-F]{3,8}\b", lambda m: m.group(0).upper(), s)
