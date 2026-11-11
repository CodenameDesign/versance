# Pages

One JSON file per hand-written page on the Public list. `tools/build_admin.py` reads every `*.json` here (in the order of `order`) and writes the
list, each page's developer spec and the nginx routes; `tools/mc_sync.py` reads the same files to tell Mission Control which pages exist. These files
are not served on the site. The extension styles (`browser-extension/style-vN/`) are found by scanning the folders, so they need no file; pages that page-capture adds stay in `tools/build_admin.py`.

```json
{
  "order": 10,
  "name": "Queues",
  "slug": "queues",
  "file": "versance.html",
  "description": "What the page is, in a sentence.",
  "parts": [["Table", "/admin/system/components/#table"]],
  "notes": ["Anything a developer should know"]
}
```

- `order`: where the page sits in Developer details (10, 20, 30...). Mission Control sets the order clients see.
- `slug`: the route, `/public/<slug>`. `file`: the page file, relative to the repo.
- `parts`: design-system parts the page uses, as `[label, link]` pairs. `notes`: bullets in the page's developer box.
- `group`: the group the page sits in on the Public list. `spec`: rows of the developer spec, `[{"label": "...", "bullets": ["..."]}]`; `spec_include`: shared rows in `_shared/<name>-spec.json` that go first. `files`, `target`: extra source files, and the served path if it differs.

A new page folder also needs its `COPY` line in the Dockerfile.
