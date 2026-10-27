# Versance admin: working rules

## Keep the design system in step with the UI (always)
When you change how the admin (or a new page) looks or behaves, update the system in the same change:
1. Add or change values in `design-tokens/tokens.css` (one token per line, trailing `[app]` / `[ext]` / `[both]` / `[ours]` comment). `tokens.json` and `DESIGN-TOKENS.md` are generated.
2. Edit the data in `tools/build_system.py` (`COMPONENTS`, type scale, foundations, the rules in `md_agents`), add specimen CSS to `system/system.css`, then run `python3 tools/build_system.py`.
3. Run `python3 tools/build_admin.py` if the Public list changed, then `python3 tools/audit.py` and fix every FAIL.
4. Commit page and system changes together. Push and deploy only when asked.

## Tokens come from two sources
Values come from `versance.html` (the web app) and `browser-extension/style-v1/`. Search them before inventing a value; mark anything neither defines as `[ours]`. If a source changes, `audit.py` flags the drift.

## Data
Made-up company, filing and user data only. Never commit real data.
