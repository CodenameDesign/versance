#!/usr/bin/env python3
"""
Reports a site's pages to Mission Control.

    python3 mc_sync.py --site /path/to/site-repo [--url https://missioncontrol.futurebits.io] [--dry-run] [--force]

The token comes from the environment (MC_SYNC_TOKEN); never put it in a file in the repository.

What it does: reads the site's own files (never the running website), works out which pages it has and which
files each page loads, and sends that list to Mission Control. It does not say who may open anything. New pages
arrive closed; Mission Control keeps the settings you chose.

It only uses the Python standard library (3.8 or newer) so it can run inside any site build.

Layout supported: the "static admin" sites (4Mativ, CNO and their forks): a folder with admin/, system/, design-tokens/,
an nginx.conf, and tools/build_admin.py whose PAGES list names the public prototype pages (as dict(...) or P(name, slug,
file, ...) entries) and, optionally, MOUNTS (folders served in place under /public/<mount>/). Page files may sit in the
folder above the site folder (CNO keeps its pages beside its cno-admin folder).
"""
import argparse
import ast
import json
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import unquote

DEFAULT_URL = "https://missioncontrol.futurebits.io"

# Files Traefik serves without asking Mission Control, so they need no area.
ALWAYS_OPEN_PATTERNS = ["/design-tokens/*", "/admin/system/system.css", "/admin/system/system.js"]
ALWAYS_OPEN_SUFFIXES = [".woff2"]

TAG = re.compile(r"""<(?:link|script|img|source|iframe|video|audio|embed)\b[^>]*?\b(?:src|href|poster)\s*=\s*["']([^"']+)["']""", re.I)
CSS_URL = re.compile(r"""url\(\s*["']?([^"')]+)["']?\s*\)""", re.I)
CSS_IMPORT = re.compile(r"""@import\s+["']([^"']+)["']""", re.I)


# ---------- paths ----------

def normalise(raw):
    """A root-absolute reference as a clean path, or None if it is not one (external, relative, odd)."""
    raw = raw.strip()
    if not raw.startswith("/") or raw.startswith("//"):
        return None
    raw = re.split(r"[?#]", raw, 1)[0]
    p = unquote(raw)
    if "\\" in p or "%" in p or any(ord(c) < 32 for c in p):
        return None
    parts = [s for s in p.split("/")[1:]]
    if parts and parts[-1] == "":
        parts.pop()
    if any(s in ("", ".", "..") for s in parts):
        return None
    if parts and parts[-1] == "index.html":
        parts.pop()
    return "/" + "/".join(parts)


def is_always_open(path):
    for pat in ALWAYS_OPEN_PATTERNS:
        if pat.endswith("/*"):
            base = pat[:-2]
            if path == base or path.startswith(base + "/"):
                return True
        elif path == pat:
            return True
    return any(path.lower().endswith(s) for s in ALWAYS_OPEN_SUFFIXES)


def dependencies(html_path):
    """Root-absolute files a page or stylesheet loads, not counting links to other pages."""
    try:
        with open(html_path, encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError:
        return []
    found = []
    for rx in (TAG, CSS_URL, CSS_IMPORT):
        for m in rx.finditer(text):
            p = normalise(m.group(1))
            if p and p not in found:
                found.append(p)
    return found


def locate(repo, rel):
    """A page file's full path: in the site folder, else in the folder above it (CNO keeps its pages there)."""
    here = os.path.join(repo, rel)
    if os.path.exists(here):
        return here
    above = os.path.join(os.path.dirname(os.path.abspath(repo)), rel)
    return above if os.path.exists(above) else here


def files_of(repo, rel, own_urls):
    """The files a page loads that need an area: its dependencies minus always-open files and its own addresses."""
    deps = dependencies(locate(repo, rel))
    return [d for d in deps if not is_always_open(d) and d not in own_urls]


# ---------- reading the site ----------

def read_build_admin(repo):
    """The PAGES and MOUNTS lists of tools/build_admin.py, read as data without running the file.
    Returns (pages, mounts): pages as dicts with name, url, file and files; mounts as (mount, folder)."""
    path = os.path.join(repo, "tools", "build_admin.py")
    if not os.path.exists(path):
        return [], []
    with open(path, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    consts = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                consts[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, SyntaxError):
                pass

    def literal(node):
        try:
            return ast.literal_eval(node)
        except (ValueError, SyntaxError):
            if isinstance(node, ast.Name) and node.id in consts:
                return consts[node.id]
            raise

    pages, mounts = [], []
    for node in tree.body:
        # PAGES = [...] and PAGES += [...] (a site may add its pages in several lists)
        if not isinstance(node, (ast.Assign, ast.AugAssign)) or not isinstance(node.value, ast.List):
            continue
        names = [t.id for t in (node.targets if isinstance(node, ast.Assign) else [node.target]) if isinstance(t, ast.Name)]
        if "PAGES" in names:
            for el in node.value.elts:
                entry = {}
                if isinstance(el, ast.Call) and getattr(el.func, "id", "") == "dict":
                    for kw in el.keywords:
                        try:
                            entry[kw.arg] = literal(kw.value)
                        except (ValueError, SyntaxError):
                            pass
                elif isinstance(el, ast.Call) and getattr(el.func, "id", "") == "P" and len(el.args) >= 3:
                    try:
                        name, page_slug, file = (literal(a) for a in el.args[:3])
                    except (ValueError, SyntaxError):
                        continue
                    entry = {"name": name, "url": "/public/" + page_slug, "file": file}
                    for kw in el.keywords:
                        if kw.arg == "files":
                            try:
                                entry["files"] = list(literal(kw.value))
                            except (ValueError, SyntaxError, TypeError):
                                pass
                if entry.get("name") and entry.get("url") and entry.get("file"):
                    pages.append(entry)
        elif "MOUNTS" in names:
            for el in node.value.elts:
                if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                    try:
                        mounts.append((literal(el.elts[0]), literal(el.elts[1])))
                    except (ValueError, SyntaxError):
                        pass
    return pages, mounts


def read_pages(repo):
    """The pages of tools/build_admin.py (see read_build_admin)."""
    return read_build_admin(repo)[0]


def source_rules(nginx):
    """What the server shows as text under /admin/source/, from the generated rule: ([relative file, ...], [folder, ...]).
    An alternative that is a plain file name is a file; one written as a pattern (a site whose rule is a regular expression
    over many files) gives the folder it starts in."""
    files, folders = [], []
    for m in re.finditer(r"location\s+~\s+\^/admin/source/\(", nginx):
        depth, i = 1, m.end()
        while i < len(nginx) and depth:
            c = nginx[i]
            if c == "\\":
                i += 2
                continue
            depth += (c == "(") - (c == ")")
            i += 1
        body, alts, cur, d = nginx[m.end():i - 1], [], "", 0
        for j, c in enumerate(body):
            if c == "(" and (j == 0 or body[j - 1] != "\\"):
                d += 1
            elif c == ")" and body[j - 1] != "\\":
                d -= 1
            if c == "|" and d == 0:
                alts.append(cur)
                cur = ""
            else:
                cur += c
        alts.append(cur)
        for alt in alts:
            plain = alt.replace("\\.", ".")
            if re.fullmatch(r"[A-Za-z0-9._/-]+", plain):
                if plain not in files:
                    files.append(plain)
            else:
                lead = []
                for seg in plain.split("/"):
                    if not re.fullmatch(r"[A-Za-z0-9._-]+", seg):
                        break
                    lead.append(seg)
                if lead and "/".join(lead) not in folders:
                    folders.append("/".join(lead))
    return files, folders


def source_files(nginx):
    """The repo files the server shows as text under /admin/source/ by name: [relative file, ...]."""
    return source_rules(nginx)[0]


def side_pages(repo, folder, base):
    """The pages of a system (/admin/system or /admin/identity), in the order of its side nav: [(page folder, label)].
    A site whose Overview is the system's root page gives "" for it; one that keeps the Overview in a folder of its own
    gives that folder. Read from the nav links of a system page; a folder with no page is left out."""
    candidates = [os.path.join(repo, folder, "index.html")]
    root = os.path.join(repo, folder)
    if os.path.isdir(root):
        candidates += [os.path.join(root, d, "index.html") for d in sorted(os.listdir(root)) if os.path.isdir(os.path.join(root, d))]
    rx = re.compile(r"""<a\b[^>]*\bhref\s*=\s*["']""" + re.escape(base) + r"""/([a-z0-9-]*)/?["'][^>]*>\s*([^<]+?)\s*</a>""", re.I)
    for c in candidates:
        try:
            with open(c, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        found = []
        for m in rx.finditer(text):
            page_folder, label = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
            if page_folder in [x for x, _ in found] or not label:
                continue
            if page_folder and not os.path.exists(os.path.join(repo, folder, page_folder, "index.html")):
                continue
            found.append((page_folder, label))
        if found:  # the first page that has a side nav
            return found
    return []


def system_pages(repo):
    """The pages of the design system (/admin/system)."""
    return side_pages(repo, "system", "/admin/system")


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:63] or "page"


def build_manifest(repo, source=None):
    """The list of areas for a static-admin site, read from its files."""
    nginx = ""
    nginx_path = os.path.join(repo, "nginx.conf")
    if os.path.exists(nginx_path):
        with open(nginx_path, encoding="utf-8") as f:
            nginx = f.read()
    exists = lambda rel: os.path.exists(os.path.join(repo, rel))
    areas = []

    def shell_paths(shell_url, shell_file):
        """A system's shell (the page at /admin/system that frames its pages) and the files the shell loads. They belong to
        every page of the system: whoever may open a page may load the shell, and an open page opens the shell too, so the
        address people use (/admin/system#/colour/) works for it."""
        found = [shell_url]
        if exists(shell_file):
            found += files_of(repo, shell_file, [shell_url])
        return found

    def tidy(paths):
        """Each address in the form Mission Control stores: no trailing slash and no index.html (so a page's source file at
        .../index.html is the folder's address), a trailing /* kept. Duplicates and anything unusable are left out."""
        out = []
        for p in paths:
            wild = p.endswith("/*")
            base = normalise(p[:-2] if wild else p)
            if base is None:
                continue
            q = (base + "/*") if wild else base
            if q not in out:
                out.append(q)
        return out

    def add(key, name, group, entry, paths, companion=(), replaces=None):
        areas.append({
            "key": key, "name": name, **({"group": group} if group else {}), **({"entry": entry} if entry else {}),
            "paths": tidy(paths), "companionPaths": tidy(companion), **({"replaces": replaces} if replaces else {}),
        })

    # the shell every admin page loads
    if exists("admin/index.html"):
        shell = ["/admin"]
        if "location = /admin/pages" in nginx:
            shell.append("/admin/pages")
        if "location = /admin/whoami.json" in nginx:
            shell.append("/admin/whoami.json")  # the signed-in person's email, for the "Log out" block in the left nav
        if "location = /system" in nginx:
            shell += ["/system", "/system/*"] if "location ^~ /system/" in nginx else ["/system"]
        shell += files_of(repo, "admin/index.html", shell)
        add("shell", "Shell", None, "/admin", shell)  # its entry page is the admin home, which the gate offers to a person it refuses

    if exists("index.html"):
        add("landing", "Landing page", None, None, ["/"] + files_of(repo, "index.html", ["/"]))

    if os.path.isdir(os.path.join(repo, "system")):
        pages = system_pages(repo)
        if len(pages) < 2:
            # no side nav to read: the whole design system is one page, as before
            add("design-system", "Design system", "developer-system", "/admin/system", ["/admin/system", "/admin/system/*"])
            pages = []
        # The design system is one page to the browser (a shell at /admin/system that shows each page in a frame), but
        # Mission Control lists each of its pages, so each can be allowed or closed. The shell, with the files it loads, is
        # part of every page, so an open page can be viewed at the shell's address.
        shell_sys = shell_paths("/admin/system", "admin/system.html")
        for folder, label in pages:
            if folder == "":
                own = ["/admin/system"]
                add("system-overview", label, "developer-system", "/admin/system", own + files_of(repo, "system/index.html", own), replaces="design-system")
            elif folder == "ai":
                ai = ["/admin/system/ai/*", "/admin/system/skills/*"]
                ai += files_of(repo, "system/ai/index.html", ai)
                add("ai-files", label, "developer-system", "/admin/system/ai", ai + shell_sys, replaces="design-system")
            else:
                own = ["/admin/system/%s" % folder, "/admin/system/%s/*" % folder]
                add("system-" + folder, label, "developer-system", "/admin/system/" + folder, own + files_of(repo, "system/%s/index.html" % folder, own) + shell_sys, replaces="design-system")
        if pages and not any(folder == "ai" for folder, _ in pages) and exists("system/ai/index.html"):
            ai = ["/admin/system/ai/*", "/admin/system/skills/*"] + files_of(repo, "system/ai/index.html", ["/admin/system/ai/*", "/admin/system/skills/*"])
            add("ai-files", "AI files", "developer-system", "/admin/system/ai", ai + shell_sys, replaces="design-system")
        if not pages and exists("system/ai/index.html"):
            ai = ["/admin/system/ai/*", "/admin/system/skills/*"]
            ai += files_of(repo, "system/ai/index.html", ai)
            add("ai-files", "AI files and skills", "developer-system", "/admin/system/ai", ai)

    if exists("identity/index.html") or os.path.isdir(os.path.join(repo, "identity")):
        # The identity system is shown the same way as the design system: a shell at /admin/identity that frames its pages.
        idp = side_pages(repo, "identity", "/admin/identity")
        if len(idp) < 2:
            add("identity-system", "Identity system", "identity-system", "/admin/identity", ["/admin/identity", "/admin/identity/*"])
        shell_id = shell_paths("/admin/identity", "admin/identity.html")
        for folder, label in idp:
            own = ["/admin/identity"] if folder == "" else ["/admin/identity/%s" % folder, "/admin/identity/%s/*" % folder]
            page_file = "identity/index.html" if folder == "" else "identity/%s/index.html" % folder
            add("identity-" + (folder or "overview"), label, "identity-system", own[0] if folder else "/admin/identity", own + files_of(repo, page_file, own) + shell_id)

    if exists("admin/public/index.html"):
        pl = ["/admin/public", "/admin/public/*"]
        pl += files_of(repo, "admin/public/index.html", pl)
        add("public-list", "Public list", "public", "/admin/public", pl)

    pages, mounts_list = read_build_admin(repo)
    mounts = [m[0] for m in mounts_list]
    folders = {m[0]: m[1] for m in mounts_list}
    sources, source_folders = source_rules(nginx)
    # folders the server shows in place under /public/ that are not a mount (CNO: /public/images/, which a saved article loads)
    shared = [loc for loc in re.findall(r"location\s+\^~\s+(/public/[A-Za-z0-9._-]+/)\s*\{", nginx) if loc.strip("/").split("/")[1] not in mounts]

    def mount_of(url):
        return next((m for m in mounts if url == "/public/" + m or url.startswith("/public/" + m + "/")), None)

    by_mount = {}
    for page in pages:
        u = normalise(page["url"])
        if u and mount_of(u):
            by_mount.setdefault(mount_of(u), []).append(page)

    done = set()
    for page in pages:
        url = normalise(page["url"])
        if not url:
            continue
        mount = mount_of(url)
        if mount:
            # A folder of pages served in place is one area: the mount, its pages' spec pages, and the source files in its folder.
            if mount in done:
                continue
            done.add(mount)
            members = by_mount[mount]
            home = next((m for m in members if normalise(m["url"]) == "/public/" + mount), None)
            first = home or members[0]
            name = re.sub(r"\s*\(home\)\s*$", "", (home or first)["name"]) if home else re.split(r"\s*:\s*", first["name"])[0]
            own = ["/public/" + mount, "/public/" + mount + "/*"]
            paths = list(own)
            for m in members:
                paths += files_of(repo, m["file"], paths)
            companion = []
            if os.path.isdir(os.path.join(repo, "admin", "spec", mount)):
                companion += ["/admin/spec/" + mount, "/admin/spec/" + mount + "/*"]
            folder = folders.get(mount, "")
            companion += ["/admin/source/" + f for f in sources if folder and f.startswith(folder + "/")]
            add(slug(mount), name, "public", "/public/" + mount if home else normalise(first["url"]), paths, companion)
            continue

        fname = os.path.basename(page["file"])
        urls = [url]
        alias = "/public/" + fname
        if re.search(r"location\s*=\s*" + re.escape(alias) + r"\s*\{", nginx):
            urls.append(alias)
        paths = urls + files_of(repo, page["file"], urls)
        try:
            with open(locate(repo, page["file"]), encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            text = ""
        for loc in shared:  # the page loads files from a shared folder by a path relative to its own address
            name_ = loc.strip("/").split("/", 1)[1]
            if re.search(r"""["'(=]\s*%s/""" % re.escape(name_), text):
                paths.append(loc + "*")
        page_slug = url[len("/public/"):] if url.startswith("/public/") else url.rsplit("/", 1)[-1]
        companion = []
        if exists("admin/spec/%s/index.html" % page_slug):
            companion.append("/admin/spec/" + page_slug)
        source_url = "/admin/source/" + fname
        if page["file"] in sources:
            companion.append("/admin/source/" + page["file"])
        elif "admin/source/" in nginx and fname.replace(".", r"\.") in nginx:
            companion.append(source_url)
        companion += ["/admin/source/" + f for f in page.get("files", []) if f in sources and "/admin/source/" + f not in companion]
        add(slug(url.rsplit("/", 1)[-1]), page["name"], "public", url, paths, companion)

    # A mount whose pages are made by a loop in the build file (Versance's extension styles) has no entry to read: it is still one area.
    for mount in mounts:
        if mount in done:
            continue
        folder = folders.get(mount, "")
        own = ["/public/" + mount, "/public/" + mount + "/*"]
        paths = list(own)
        root = os.path.join(repo, folder) if folder else None
        if root and not os.path.isdir(root):
            root = os.path.join(os.path.dirname(os.path.abspath(repo)), folder)
        if root and os.path.isdir(root):
            for here, _dirs, names in sorted(os.walk(root)):
                for n in sorted(names):
                    if n.endswith(".html"):
                        paths += files_of(repo, os.path.normpath(os.path.join(folder, os.path.relpath(here, root), n)), paths)
        companion = []
        if os.path.isdir(os.path.join(repo, "admin", "spec", mount)):
            companion += ["/admin/spec/" + mount, "/admin/spec/" + mount + "/*"]
        companion += ["/admin/source/" + f for f in sources if folder and f.startswith(folder + "/")]
        companion += ["/admin/source/" + f + "/*" for f in source_folders if f == folder or f.startswith(folder + "/")]
        add(slug(mount), re.sub(r"[-_]+", " ", folder or mount).strip().capitalize(), "public", "/public/" + mount, paths, companion)

    return {"version": 1, "source": source or "", "areas": areas}


# ---------- reporting ----------

def post(url, token, manifest, force):
    req = urllib.request.Request(
        url.rstrip("/") + "/api/sync" + ("?force=true" if force else ""),
        data=json.dumps(manifest).encode("utf-8"),
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json", "User-Agent": "mc-sync/1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8") or "{}")
        except ValueError:
            return e.code, {"error": "HTTP %d" % e.code}


def describe(summary):
    parts = []
    for label, key in (("new", "created"), ("changed", "updated"), ("gone", "removed"), ("back", "restored"), ("now following the site", "adopted")):
        if summary.get(key):
            parts.append("%s: %s" % (label, ", ".join(summary[key])))
    parts.append("%d unchanged" % summary.get("unchanged", 0))
    return "; ".join(parts)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Report a site's pages to Mission Control.")
    ap.add_argument("--site", default=".", help="the site's repo folder")
    ap.add_argument("--url", default=os.environ.get("MC_URL", DEFAULT_URL))
    ap.add_argument("--source", default=os.environ.get("MC_SYNC_SOURCE", ""), help="free text for the audit log, for example a commit")
    ap.add_argument("--dry-run", action="store_true", help="print the list and send nothing")
    ap.add_argument("--force", action="store_true", help="accept a list that switches most areas off")
    args = ap.parse_args(argv)

    manifest = build_manifest(os.path.abspath(args.site), args.source)
    if not manifest["areas"]:
        print("mc-sync: no pages found in %s (is it a static-admin site?)" % args.site, file=sys.stderr)
        return 2
    if args.dry_run:
        print(json.dumps(manifest, indent=2))
        return 0
    token = os.environ.get("MC_SYNC_TOKEN", "")
    if not token:
        print("mc-sync: set MC_SYNC_TOKEN (the token made on the account's page in Mission Control)", file=sys.stderr)
        return 2
    try:
        status, body = post(args.url, token, manifest, args.force)
    except (urllib.error.URLError, OSError) as e:
        print("mc-sync: could not reach Mission Control: %s" % e, file=sys.stderr)
        return 3
    if status == 200:
        print("mc-sync: reported %d areas. %s" % (len(manifest["areas"]), describe(body)))
        return 0
    print("mc-sync: Mission Control refused the list (%d): %s" % (status, body.get("error", body)), file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
