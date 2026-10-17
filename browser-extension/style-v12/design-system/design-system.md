# Versance Coworker — style v12: cash

Cash: electric green, chunky radii, glass, dark / light. Based on the Cash App references (eight images) plus a mining photo for the page background.

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components (with the dark / light button).
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** v9's structure (dark / light toggle), re-skinned from the Cash App references with glass and chunky radii.

## 1. Identity

- **Palette:** electric green **`#00E510`** on pure black and white; pale sky-blue gradient with a green glow behind the panel in light mode (gives the glass something to blur), pure black with a green glow in dark mode. highlighter `#E4F55B`; risk badges are soft pills (red / yellow tints).
- **Chunky radii:** panel 40px, chat card and composer 30px, cards 26px, fields / toggle rows / selects / buttons / chips / tabs fully round (999px), rail tiles 15px squircles, icon tiles 16px.
- **Glass:** frosted `backdrop-filter` (blur 8–30px, saturate) on the panel, the rail tiles, round header buttons, the segmented tab track, Web Search Off and the **toggles**: a translucent grey track with a white knob; when ON the track tints green and the knob turns electric green with a glow, like the lock slider. The reference's glass slider is the model.
- **Header:** electric-green pill (like the "Sign up now" card) with black text and a black `edit` pill. Primary buttons green with black text; active tab and Web Search On are black pills (white in dark mode); send is a round green button.
- **Type:** Inter, bold and very tight: "Hi," 54px at -0.055em, report title 32px, pane titles 20px bold; mono labels from v9 are now plain sentence-case Inter.
- **Help panel:** black screen with green sub-heads (like "Distribute paycheck"); intro tiles are soft grey fills.
- **Toggle (theme):** sun / moon glass button above the avatar, remembered between pages, `?theme=dark` to force.

The page the extension sits on is now a mining photo (`screens/assets/mining.jpg`, referenced relatively from `screens.css`, so it travels with the folder). Light mode: the photo with a 10% dark tint, the glass panel raised to 70% white for legibility; dark mode: the same photo under a 58% black overlay. The frosted glass (panel, rail, tabs, toggles) blurs the photo. ## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

### Light theme

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#6E7A96 @ 0.28` | `--glass` | 252 elements |
| `#00E510` | `--accent`, `--orange` | 119 elements |
| `#FFFFFF @ 0.88` | `--card` | 75 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#F1F1F1` | `--fill` | 38 elements |
| `#0F1A22` | set directly in this style | 19 elements |
| `#FFFFFF @ 0.7` | `--panel` | 19 elements |
| `#00E510 @ 0.3` | set directly in this style | 5 elements |
| `#E4F55B` | `--mk` | 3 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#000000` | `--ink`, `--inv-bg`, `--strong` | 1389 elements |
| `#5E6168` | `--muted` | 293 elements |
| `#94979F` | `--faint` | 80 elements |
| `#FFFFFF` | `--inv-ink`, `--risk-on` | 60 elements |
| `#D7D9DE` | set directly in this style | 4 elements |
| `#B3261E` | set directly in this style | 3 elements |
| `#6F5400` | set directly in this style | 3 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF @ 0.55` | `--glass-line` | 230 elements |
| `#000000 @ 0.12` | `--dotline` | 18 elements |
| `#000000 @ 0.08` | `--line` | 5 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#0A141E @ 0.1` | set directly in this style | 38 elements |

### Dark theme

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF @ 0.12` | `--glass` | 252 elements |
| `#00E510` | `--accent`, `--orange` | 119 elements |
| `#262626 @ 0.92` | `--card` | 75 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#141414 @ 0.72` | `--panel` | 19 elements |
| `#262626` | `--fill` | 17 elements |
| `#1B1B1B` | set directly in this style | 15 elements |
| `#1E1E1E` | set directly in this style | 6 elements |
| `#00E510 @ 0.3` | set directly in this style | 5 elements |
| `#E4F55B` | `--mk` | 3 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--ink`, `--inv-bg`, `--risk-on` | 1172 elements |
| `#A9ACB3` | `--muted` | 293 elements |
| `#000000` | `--inv-ink`, `--bg` | 276 elements |
| `#787B83` | `--faint` | 80 elements |
| `#D7D9DE` | set directly in this style | 4 elements |
| `#FFB4A8` | set directly in this style | 3 elements |
| `#F3E26B` | set directly in this style | 3 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF @ 0.18` | `--glass-line` | 230 elements |
| `#FFFFFF @ 0.16` | `--dotline` | 18 elements |
| `#FFFFFF @ 0.1` | `--line` | 5 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#000000 @ 0.58` | set directly in this style | 38 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-hover` | `#00CA0E` |
| `--accent-on` | `#111111` |
| `--accent-pressed` | `#00AE0C` |
| `--accent-tint-15` | `#D9FBDB` |
| `--accent-tint-25` | `#BFF8C3` |
| `--accent-tint-8` | `#EBFDEC` |
| `--amber-tint` | `#F4E4B8` |
| `--bg` | `#D2E0FA` |
| `--green-tint` | `#CFE0DE` |

**Not rendered:** 28 further colour variables in `tokens.css` (`--accent-grad`, `--accent-grad-diag`, `--accent-wash`, `--amber-grad`, `--amber-ink`, `--coral-grad`, `--dots`, `--exception-dark`, `--green-grad`, `--hover`, `--line-soft`, `--mark`, `--pane`, `--risk-high`, `--risk-medium`, `--soft-wash`, `--tag-filing`, `--tag-news`, `--tag-transcript`, `--tag-web`, `--teal-grad`, `--teal-ink`, `--teal-tint`, `--text-info`, `--text-selected`, `--violet-grad`, `--violet-ink`, `--violet-tint`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **Inter**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Inter | 54px | 700 | -2.97px | — |
| Lead | Inter | 20px | 600 | -0.6px | — |
| Pane title | Inter | 20px | 700 | -0.9px | — |
| Report title | Inter | 32px | 700 | -1.6px | — |
| Finding title | Inter | 14px | 600 | -0.28px | — |
| Body | Inter | 14px | 400 | — | — |
| Header bar | Inter | 14px | 600 | -0.14px | — |
| Section label | Inter | 14px | 500 | — | — |
| Meta / dates | Inter | 13px | 400 | — | — |
| Chip | Inter | 14px | 400 | — | — |
| Tab | Inter | 14px | 400 | — | — |
| Button | Inter | 14px | 600 | — | — |
| Link | Inter | 14px | 500 | — | — |
| Tag | Inter | 12px | 400 | — | — |
| Risk badge | Inter | 12px | 600 | — | — |

## 4. Shape, depth and glass

| Component | Radius | Border | Shadow | Backdrop blur |
|---|---|---|---|---|
| Panel | 40px | 1px | yes | blur(30px) saturate(1.7) |
| Chat card | 30px | 0px none | yes | — |
| Composer | 30px | 0px none | yes | — |
| Cards | 26px | 0px none | yes | — |
| Intro tile | 30px | 0px none | none | — |
| Header bar | 999px | 0px none | yes | — |
| Buttons | 999px | 0px none | none | — |
| Chips | 999px | 0px none | yes | — |
| Text fields | 999px | 2px | none | — |
| Toggle | 999px | 1px | yes | blur(8px) |
| Rail tiles | 15px | 1px | none | blur(10px) |
| Send button | 50% | 0px none | none | — |
| Tags | 999px | 0px none | none | — |

## 5. Layout

- **Panel:** docked to the right of the browser window, full window height inside a 16px margin; **440px** wide on the compact (Coworker home) screens and **799px** on the expanded screens (chat column + tool pane).
- **Icon rail (right edge):** eight items, top to bottom: **Home**, Research context (with count badge), My filings, CAD library, US library, Compliance, Output Centre, History. Icon-only tiles. The gap between the content and the rail is 22.5px.
- **Composer:** text field on top, a tools row (`+`, `@`, `/`) below with the round send button at the right; Web Search and Export Conversation in a row below.
- **Chat column tabs:** `Coworker` (alone, or beside `Filings` / `Compliance Review`) with a `new chat` / `new report` tag at the right.
- **Header:** company bar at the top of the chat column (name + `edit`, or a search field with `EXIT` while switching); the collapse button sits top-right of the panel.
- **Footer of the tool pane:** "Open Versance.ai" with the logo tile; the user avatar and the dark / light button sit at the bottom-right of the panel.

## 6. Behaviour rules (all 19 screens)

- **Home:** the Home button is the first rail item, above Research context, and is highlighted on the four Coworker home screens (101a–101b). There is no forward-arrow button.
- **Help `?`:** shown on a pane title except while that pane's own help card is open (201b, 501aa, 601a, 701a).
- **Right-pane header spacing:** title → first block 16px; title → italic sub-line 4px and sub-line → first block 16px; title → back link 8px and back link → first block 16px.
- **Close ×:** a dismiss × on intro tiles, help cards and the help panel; a remove × on source cards and the reviewed-source chip.
- **Links:** every text link is underlined, 14px; the back links (Switch companies, Exit document) are underlined too; `Clear all` / `Clear` are the quiet grey link.
- **Message box:** a real text input. The send button is disabled until there is text; Enter or the button sends and clears the field; whitespace alone does not enable it.
- **Focus:** buttons and other clickable controls take `2px solid #00E510` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
- **Motion:** hover and press transitions only; nothing animates on page load.
- **Navigation in the HTML pages:** the "All screens" list (top-left) and, in every style except v1, the `‹ n ›` style switcher (bottom-left). Both are neutral and identical in every style.
- **Dark / light:** the sun / moon button above the avatar sets `data-theme` on `<html>`, is remembered in `localStorage` and can be forced with `?theme=dark`.

## 7. Screens

| State | Screen | Contents |
|---|---|---|
| 101a | Coworker home (compact) | Welcome tile, three prompt chips, composer. |
| 101ab | Company switcher | Recent companies dropdown. |
| 101ac | Company switcher, searching | "Aar" typed; recent + all companies; `EXIT`. |
| 101b | How the Versance Coworker works | Four-step help panel. |
| 102a | Research context | Two toggles, Add a URL / Upload a Document, three source cards. |
| 102aa | Research context, Add a URL | Paste-a-link field with `ADD`; Cancel. |
| 102s | Research context, empty | "No documents added yet." empty state. |
| 201a | Primary Company Filings | Search + filter, filing list. |
| 201b | Primary Company Filings, help | Help card open (no `?`). |
| 401aa | Search Canadian Filings | Find a Company, A–Z, company list. |
| 401ab | Search <Company> Filings | Switch-companies link, filing list with hover action. |
| 411a | Filing viewer | Exit document, Add Document to Context, page preview, prompt chips. |
| 501aa | Compliance review, start | Welcome tile, two action buttons, how-it-works card. |
| 501ab | Compliance review, options | Reviewed source, Country / Regulation / Document Type, Run Report. |
| 501bb | Compliance report | Re-Run Report, Report Generated card, High / Medium findings. |
| 601a | Output Centre, empty | Info card, empty state. |
| 601b | Output Centre | Search + filter, seven report rows with tags. |
| 701a | Conversation History, empty | Info card, "You haven't had any conversations yet." |
| 701b | Conversation History | Search conversations, chat open on the left. |

The red annotation labels and leader lines in the reference designs were specs and never appear in the screens.

## 8. Content notes

- Company names in the mock data (Integra Resources, Australis Capital, Equinox Gold, South Railroad, Company A–C, Aardvark …) are placeholders; the switcher uses "Company Two" (the reference design had a typo).
- The 501ab reference annotation "new copy once you've selected a" is cut off in the reference design; only the visible copy is used.
- The empty History screen reads "You haven't had any conversations yet."
- No success state and no low-risk badge are defined: no reference shows one.
