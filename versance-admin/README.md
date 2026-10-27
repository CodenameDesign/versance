# Versance admin

The same admin as CNO, 4Mativ and Equinox (left-nav shell, **Public** page list with a developer-spec page per entry, **System** design system), styled from the Versance web app and the browser-extension designs. Served at versance.futurebits.io.

**Tokens are based on two sources:** `versance.html` (the web app) and `browser-extension/style-v1/`. Each token in `design-tokens/tokens.css` is tagged `[app]`, `[ext]`, `[both]` or `[ours]`; `tools/audit.py` checks the colour values against the source files.

```
design-tokens/   tokens.css (source of truth), fonts.css, tokens.json + DESIGN-TOKENS.md (generated)
admin/           shell: index, system (iframe), public (generated list), spec/ (generated, one page per entry), admin.css, menu.js
system/          generated design-system site, AI files and the versance-ui skill (system.css and logo-white.svg are hand-written)
tools/           build_system.py, build_admin.py, audit.py, skill_template/
nginx.conf, Dockerfile, index.html (logo on white)
```

## Commands (run from `versance-admin/`)

```
python3 tools/build_system.py   # system/**, AI files, skill, tokens.json, DESIGN-TOKENS.md
python3 tools/build_admin.py    # admin/public/index.html, admin/spec/**, and the /public + /admin/source routes in nginx.conf
python3 tools/audit.py          # drift check; fix every FAIL
```

## The Public list is generated from the repo

`build_admin.py` reads `versance.html`, `edgar/versance.html`, `medicus-01.html` and every `browser-extension/style-vN/` (its `design-system/` pages and `screens/VBE-*.html`), so a new style or screen appears after re-running it. Pages are served under `/public/` without changing the URL: `browser-extension/` is mounted in place at `/public/extension/` (so each page's relative CSS keeps working), single files are served by an internal rewrite (their root URLs return 404). `/` and `/public/` show only the logo.

To add a page that is not in those folders, add a `P(...)` entry in `tools/build_admin.py` and a `COPY` line in the Dockerfile.

## Docker

Build from the **repo root**: `docker build -f versance-admin/Dockerfile -t versance-admin .`

## Notes

- Figtree and Roboto Mono load from Google Fonts, as in the source designs. To self-host, download the font files and replace the import in `design-tokens/fonts.css`.
- The System section documents the web app and style v1 (the baseline). Styles v2 to v13 are explorations: each has its own design-system pages in the Public list.
- `medicus-01.html` is a saved page from another company's site, listed as a reference only.
