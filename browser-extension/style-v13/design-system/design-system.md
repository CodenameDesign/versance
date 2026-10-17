# Versance Coworker — style v13: sidekick

Sidekick: violet gradient, glass window, labelled rail, Figtree. Light only. Based on the browser-sidebar references (two images).

**Files in this folder**

- `tokens.css` — the design variables this style uses (colour, type, radius, spacing, elevation, motion).
- `components.css` — the base component rules, driven by the tokens.
- `specimen.html` — the style rendered live from its real components.
- `view-design-system.html`, `view-tokens.html`, `view-components.html` — readable pages for this document and the two CSS files, each with a Back arrow (generated from them by `../tools/viewers.py`).
- `../screens/screens.css` — this style's overrides on top of the tokens and components; `../screens/*.html` are the 8 pages that hold the 19 screens (use the "All screens" list in the top-left).

**Lineage:** Started from v1 again, re-skinned from the browser-sidebar references, in Figtree.

## 1. Identity

- **Font:** Figtree throughout, with no other typeface.
- **Backdrop and window:** periwinkle → violet → lilac gradient (`#8EA6FF` → `#7A78FF` → `#8B6CFA` → `#D6B4F6`) with a soft pink glow bottom-right; the panel is a frosted-glass window (white at 74%, 24px blur, 24px radius, violet-tinted shadow).
- **Accent:** violet `#5B3DF5` (hover `#4A2EDB`, tints `#E7E2FE` / `#F3F0FF`): toggles, links, primary buttons, `new chat` tag, active tab text, focus ring, active rail item. The logo is a **red** tile (`#E5372E`) like the red "N", and the count badge is red.
- **Labelled icon rail:** each rail item is an icon tile over a short caption (Research, Filings, CAD, US, Review, Output, History) like Chat / Hand / Code / More; inactive = grey, active = white tile with a violet icon and caption. The panel is 12px wider (451 / 810px) so the 24px gap to the content is kept.
- **Composer:** a toolbar row above a big rounded message box: a Web Search chip with a chevron (violet tint when on, grey when off), an attach icon, then the box with `Export Conversation` bottom-left and a plain paper-plane send bottom-right (grey when empty, a violet tile once there is text).
- **Tabs / chips:** soft lavender segmented track with a white active pill; grey pill chips with icon (like "Summarize").
- **Cards:** frosted white cards, 14px radius, hairline `#EDEBF7`; intro / help cards are pale violet `#F6F4FF`.

## 2. Colours

Measured from the 19 rendered screens: every fill, text, icon, line and gradient stop that appears. The token column names the variable that holds that value, or says the style sets it directly. Colours used on only 1–2 elements are left out as minor tints.

**Surfaces and fills**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF` | `--accent-on`, `--bg`, `--panel` | 132 elements |
| `#D9DDE5` | set directly in this style | 67 elements |
| `#FFFFFF @ 0.92` | set directly in this style | 38 elements |
| `#FFFFFF @ 0.85` | set directly in this style | 38 elements |
| `#E5372E` | set directly in this style | 32 elements |
| `#FFFFFF @ 0.95` | set directly in this style | 24 elements |
| `#EEEBFB` | set directly in this style | 21 elements |
| `#8A8CF6` | set directly in this style | 19 elements |
| `#FFFFFF @ 0.74` | set directly in this style | 19 elements |
| `#F0EDFE` | set directly in this style | 17 elements |
| `#FFFFFF @ 0.96` | set directly in this style | 16 elements |
| `#F3F3F8` | `--hover` | 15 elements |
| `#F6F4FF` | set directly in this style | 13 elements |
| `#F1F1F6` | set directly in this style | 13 elements |
| `#C9C7DA` | set directly in this style | 11 elements |

**Text and icons**

| Colour | Token | Used on |
|---|---|---|
| `#7C7C94` | set directly in this style | 627 elements |
| `#16162A` | `--ink` | 516 elements |
| `#6A6A82` | `--muted` | 203 elements |
| `#5B3DF5` | `--accent`, `--tag-filing` | 144 elements |
| `#B1B1C4` | set directly in this style | 70 elements |
| `#4A2EDB` | `--accent-hover`, `--text-info`, `--text-selected` | 69 elements |
| `#B6B6C8` | set directly in this style | 48 elements |
| `#000000` | set directly in this style | 18 elements |
| `#4D4D66` | set directly in this style | 16 elements |
| `#CFC6FD` | `--accent-tint-25` | 12 elements |
| `#A0A0B4` | `--faint` | 3 elements |

**Lines and outlines**

| Colour | Token | Used on |
|---|---|---|
| `#FFFFFF @ 0.9` | set directly in this style | 74 elements |
| `#EDEBF7` | set directly in this style | 38 elements |
| `#DCD8F2` | set directly in this style | 25 elements |
| `#FFFFFF @ 0.8` | set directly in this style | 19 elements |
| `#E7E2FE` | `--accent-tint-15` | 18 elements |
| `#EFEFF6` | `--line-soft` | 18 elements |
| `#E7E7F0` | `--line` | 3 elements |

**Gradient stops**

| Colour | Token | Used on |
|---|---|---|
| `#F0C8FA @ 0.85` | set directly in this style | 19 elements |
| `#96AAFF @ 0.7` | set directly in this style | 19 elements |
| `#8EA6FF` | set directly in this style | 19 elements |
| `#7A78FF` | set directly in this style | 19 elements |
| `#8B6CFA` | set directly in this style | 19 elements |
| `#D6B4F6` | set directly in this style | 19 elements |

**Interaction-state colours** (hover, pressed, focus, disabled; not visible in the static screens)

| Token | Value |
|---|---|
| `--accent-pressed` | `#3B22B8` |

**Not rendered:** 7 further colour variables in `tokens.css` (`--exception-dark`, `--pane`, `--risk-high`, `--risk-medium`, `--tag-news`, `--tag-transcript`, `--tag-web`) are carried over from earlier styles. They are still referenced by base rules that this style overrides, so they are kept in the file under "Carried over", but none appears on a screen.

## 3. Type

Families: **Figtree**. Sizes below are the rendered values on the 19 screens.

| Role | Family | Size | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Display ("Hi,") | Figtree | 28px | 700 | -0.84px | — |
| Lead | Figtree | 18px | 400 | — | — |
| Pane title | Figtree | 14px | 700 | -0.21px | — |
| Report title | Figtree | 22px | 700 | -0.66px | — |
| Finding title | Figtree | 14px | 600 | — | — |
| Body | Figtree | 14px | 400 | — | — |
| Header bar | Figtree | 14px | 600 | — | uppercase |
| Section label | Figtree | 14px | 400 | — | — |
| Meta / dates | Figtree | 14px | 400 | — | — |
| Chip | Figtree | 14px | 500 | — | — |
| Tab | Figtree | 14px | 600 | — | — |
| Button | Figtree | 14px | 600 | — | — |
| Link | Figtree | 14px | 400 | — | — |
| Tag | Figtree | 12px | 400 | — | — |
| Risk badge | Figtree | 12px | 700 | 0.24px | uppercase |

## 4. Shape, depth and glass

| Component | Radius | Border | Shadow | Backdrop blur |
|---|---|---|---|---|
| Panel | 24px | 1px | yes | blur(24px) saturate(1.5) |
| Chat card | 18px | 1px | yes | — |
| Composer | 0px | 0px none | none | — |
| Cards | 14px | 1px | yes | — |
| Intro tile | 16px | 1px | none | — |
| Header bar | 12px | 1px | yes | — |
| Buttons | 10px | 1px | none | — |
| Chips | 999px | 1px | none | — |
| Text fields | 12px | 1px | none | — |
| Toggle | 999px | 0px none | none | — |
| Rail tiles | 12px | 0px none | none | — |
| Send button | 10px | 0px none | none | — |
| Tags | 999px | 0px none | none | — |

## 5. Layout

- **Panel:** docked to the right of the browser window, full window height inside a 16px margin; **451px** wide on the compact (Coworker home) screens and **810px** on the expanded screens (chat column + tool pane).
- **Icon rail (right edge):** eight items, top to bottom: **Home**, Research context (with count badge), My filings, CAD library, US library, Compliance, Output Centre, History. Each item is an icon tile over a short caption. The gap between the content and the rail is 22px.
- **Composer:** a toolbar row (Web Search chip, attach icon) above a large rounded message box; Export Conversation inside the box at the bottom-left and the send icon at the bottom-right.
- **Chat column tabs:** `Coworker` (alone, or beside `Filings` / `Compliance Review`) with a `new chat` / `new report` tag at the right.
- **Header:** company bar at the top of the chat column (name + `edit`, or a search field with `EXIT` while switching); the collapse button sits top-right of the panel.
- **Footer of the tool pane:** "Open Versance.ai" with the logo tile; the user avatar sit at the bottom-right of the panel.

## 6. Behaviour rules (all 19 screens)

- **Home:** the Home button is the first rail item, above Research context, and is highlighted on the four Coworker home screens (101a–101b). There is no forward-arrow button.
- **Help `?`:** shown on a pane title except while that pane's own help card is open (201b, 501aa, 601a, 701a).
- **Right-pane header spacing:** title → first block 16px; title → italic sub-line 4px and sub-line → first block 16px; title → back link 8px and back link → first block 16px.
- **Close ×:** a dismiss × on intro tiles, help cards and the help panel; a remove × on source cards and the reviewed-source chip.
- **Links:** every text link is underlined, 14px; the back links (Switch companies, Exit document) are underlined too; `Clear all` / `Clear` are the quiet grey link.
- **Message box:** a real text input. The send button is disabled until there is text; Enter or the button sends and clears the field; whitespace alone does not enable it.
- **Focus:** buttons and other clickable controls take `2px solid #5B3DF5` with a 2px offset and keep their own radius; text fields show no ring, only their 1px border changes colour; the composer container adds nothing.
- **Motion:** hover and press transitions only; nothing animates on page load.
- **Navigation in the HTML pages:** the "All screens" list (top-left) and, in every style except v1, the `‹ n ›` style switcher (bottom-left). Both are neutral and identical in every style.

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
