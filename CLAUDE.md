# CLAUDE.md

Operator's guide for any agent (or human) refreshing data in this repo's `README.md`. This file describes **what information lives where, and in what order**. For **how it renders** (colors, fonts, voice, sanitizer constraints), see `DESIGN_SYSTEM.md` in the same folder.

If you are about to edit `README.md`, read this file first, then skim `DESIGN_SYSTEM.md` for the design rules.

---

## Files in this repo

| File | Purpose | Edit cadence |
|---|---|---|
| `README.md` | The profile README that renders on `github.com/RealEmmettS`. Mix of static structure and live-refreshed content. | Frequent (daily to weekly during active sprints) |
| `DESIGN_SYSTEM.md` | The visual / structural design contract. Colors, voice, sanitizer rules, exact component templates. | Rare (only when the design itself changes) |
| `CLAUDE.md` | This file. Data layout map for refresh agents. | Rare (when the README's structural outline changes) |
| `Résumé.md` | Plain-text résumé content. Not rendered by GitHub on the profile. | Occasional |
| `agents/` | Local-only Claude Code agent descriptors (`docs-updater.md`, `git-deploy-manager.md`, `senior-bug-fixer.md`). Not relevant to the README. | Rare |

`README.md` is the only file that renders on Emmett's GitHub profile page. Everything else in this repo is supporting documentation or local tooling.

---

## README structure at a glance

`README.md` is laid out as seven sequential blocks, separated by `---` horizontal rules. Read top to bottom:

```
1. HERO          Identity, taglines, status badges, bio, contact pills
2. TOC           Collapsible jump-nav linking the other six sections
3. NOW           This week's shipping list, as a GFM [!NOTE] callout
4. CURRENT WORK  2x3 grid of major projects + collapsible workshop list
5. STACK         Mindmap, release timeline table, badge rows, collapsible focus deep-dive
6. NUMBERS       Live stat shields, paired widget cards, full-width activity graph
7. COLOPHON      Self-documenting techniques catalogue, then footer banner
```

Do not reorder. Do not introduce an eighth top-level section without weighing what to drop, since GitHub's profile-page render area is finite and reads as a single scroll.

---

## Per-section data inventory

For each section: what content lives there, what changes on each refresh, what stays static.

### 1. HERO

- **Capsule wave banner** (top): "EMMETT SHAUGHNESSY" / "DIGITAL CRAFTSMAN". Static. Only update if the user changes their tagline.
- **Typing SVG** (cycling): 4 lowercase tagliners cycling through identities. Refresh when a major identity shift happens (new role, new founding venture). Update both the dark `srcset` and the light `src` URLs and the `alt`.
- **Status pulse badges** (4): Profile views, Followers, Last push, Stars. All auto-pulled live from external services. No content updates needed.
- **One-line bio**: Plain-text sentence. Refresh when the active workshop changes substantially (e.g., a major project ends or starts). Currently mentions Qube TX, Magic Pantry, Dorsey 2026.
- **Contact pills** (4): Website / Qube TX / Resume / Email. Static unless a URL changes.

### 2. TOC

- A collapsible `<details>` block with `<kbd>` styled summary.
- Anchor links to `#now`, `#current-work`, `#stack`, `#numbers`, `#colophon`.
- Only update if a section heading is renamed (must update both the heading and the matching anchor).

### 3. NOW

- A GFM `> [!NOTE]` block.
- **Heading line**: `**MONTH YEAR, actively shipping**` (e.g., `**MAY 2026, actively shipping**`). Update the month every cycle.
- **Exactly three bullets**, each in the shape: `&middot; **Project name**, one-line description of what is shipping`.
- This is the highest-signal block on the page and the one that should be refreshed most often.

### 4. CURRENT WORK

- **Heading**: `## CURRENT WORK`. Static.
- **2x3 HTML `<table>`**: 6 cells, each a project card. Project lineup as of this writing:
  1. Qube TX, top-left
  2. QorkMe, top-right
  3. shaughvOS, middle-left
  4. Dorsey 2026, middle-right
  5. Magic Pantry, bottom-left
  6. Personal Site, bottom-right
- Each cell follows a strict shape: linked heading, bold tagline, 4 inline backtick-pill tech tags, then a single continuous descriptive paragraph.
- The descriptive paragraphs are the primary refresh target. They should reflect what is currently shipping in each project.
- **Workshop block** below the table: a single `<details>` with one long paragraph listing secondary projects. Update when a new secondary project lands or an old one closes.

### 5. STACK

- **Heading**: `## STACK`. Static.
- **Mermaid mindmap** ("WHAT I BUILD"): four semantic branches (`WEB`, `SYSTEMS`, `MOBILE`, `BACKEND`), three leaves each. Update only when the user's build categories shift; this is a near-static map.
- **`### 2026 release timeline`**: markdown table with three columns (`Quarter`, `Month`, `Shipped`). Append a row each month with the month's releases.
- **`### Languages`**: 6 shields. Update if the user adopts or drops a language.
- **`### Frameworks & libraries`**: 8 shields. Same rule.
- **`### Cloud & infrastructure`**: 5 shields. Same rule.
- **Focus deep-dive `<details>`**: a bulleted breakdown of every active focus area. Bullets refresh as work progresses (this is where the longer-form "what's happening across the workshop" content lives).

### 6. NUMBERS

- **Heading**: `## NUMBERS`. Static.
- **Stat shield row** (5 shields in a single centered row):
  1. `PUBLIC REPOS` (live, GitHub API via `dynamic/json`)
  2. `TOTAL STARS` (live, shields.io GitHub endpoint)
  3. `PUBLIC GISTS` (live, GitHub API via `dynamic/json`)
  4. `FOLLOWING` (live, shields.io GitHub endpoint)
  5. `ON GITHUB SINCE 2017` (static; update the year only if the value is wrong)
- **Paired widget cards** (2x1 table):
  - Left: Streak card (live, github-readme-streak-stats)
  - Right: Top languages card (live, github-readme-stats top-langs)
- **Activity graph** (full-width, centered): 52-week commit sparkline. Live.
- No trophy row. (Tried, rejected, do not add it back.)

### 7. COLOPHON

- **Heading**: `## COLOPHON`. Static.
- A collapsible `<details>` containing:
  - Intro paragraph explaining what the README demonstrates.
  - **Technique catalogue table**: every rendering technique used in the README, with one row per technique. Update this row-by-row when a technique is added or removed.
  - "Things the sanitizer blocks that this respects" paragraph. Mostly static.
  - "Deferred to a future automation pass" paragraph. Update when a deferred item is added or shipped.
  - Source links.
- **Footer capsule banner**: "BUILDING RELIABLE SYSTEMS / EMMETT@EMMETTS.DEV · EMMETTSHAUGHNESSY.COM". Static unless contact info changes.

---

## Refresh cadence map

| Content block | Source | Refresh cadence | Updated by |
|---|---|---|---|
| Capsule banners (header / footer) | Static markup | Never | Manual only |
| Typing SVG tagliners | Static markup | Rarely (identity shift) | Manual |
| Status pulse badges (4) | shields.io + komarev | Live on every page load | Auto |
| Hero one-line bio | Static markup | Quarterly or on workshop change | Manual or refresh automation |
| Contact pills (4) | Static markup | Never (unless URL changes) | Manual |
| TOC anchors | Static markup | Only on heading rename | Manual |
| `NOW` block (3 bullets) | Static markup | Weekly | Refresh automation |
| Project cards (6 descriptions) | Static markup | Per-project as work ships | Refresh automation |
| Workshop paragraph | Static markup | When secondary projects change | Refresh automation |
| Mermaid mindmap | Static markup | Rarely | Manual |
| Release timeline table | Static markup | Monthly (append new row) | Refresh automation or manual |
| Language / framework / cloud badges | Static markup | When stack adopts or drops a tool | Manual |
| Focus deep-dive bullets | Static markup | Weekly | Refresh automation |
| Stat shields (5) | shields.io + GitHub API | Live on every page load (mostly) | Auto |
| Streak card | github-readme-streak-stats | Live | Auto |
| Top languages card | github-readme-stats | Live (cached ~24h via Camo) | Auto |
| Activity graph | github-readme-activity-graph | Live | Auto |
| Colophon technique table | Static markup | Whenever a technique is added or removed | Manual |
| Sanitizer source links | Static markup | Never | Manual |

"Live" entries refresh by virtue of being parameterized image URLs that the rendering services regenerate on demand. "Auto" entries do not require any commit. "Manual" / "refresh automation" entries require an edit to `README.md` and a push.

---

## Common refresh operations

Quick recipes for the operations refresh agents perform most often. For exact markup, see `DESIGN_SYSTEM.md` § Component templates.

### Updating the `NOW` block for a new week

1. Locate the `## NOW` heading.
2. Inside the `> [!NOTE]` block, update the `**MONTH YEAR, actively shipping**` header.
3. Replace the three `&middot; **Project, headline.**` bullets with the current week's shipping list.
4. Keep exactly three bullets. If you have four candidates, pick the three highest-impact.
5. **Cap each bullet at 2-3 short paragraphs.** Lead with `&middot; **Project name, one-line headline.**` followed by a 2-3 sentence summary. If the bullet has a natural multi-part structure (PR #1 / PR #2 / PR #3; headline / what sits under it; reporting tool / scorecards dashboard / stack), break it into multiple paragraphs inside the same bullet, separated by blank `>` lines, each opening with a bold inline lede (`**PR #2:**`, `**Underneath:**`, `**Stack:**`). Never write a single 8-12 sentence run-on bullet. The `NOW` block is the most-read section of the page; readability beats density.

### Updating a project card description

1. Locate the `## CURRENT WORK` table.
2. Find the `<td>` cell whose `### [Project](url)` heading matches the project.
3. Replace the descriptive paragraph(s) beneath the tech-pill row. Do not touch the heading, tagline, or tech pills unless those have legitimately changed.
4. Use **multiple short paragraphs separated by blank lines**, not one wall of text. Lead with a 1-2 sentence "what it is" paragraph, then 2-3 follow-up paragraphs each scoped to a specific theme (latest ship, what sits under it, surrounding repos / surfaces). Each follow-up paragraph may open with a bold inline lede (`**Latest, offline queue.**`, `**Underneath, 2.0 / 2.0.1 store-ready prep.**`) so the reader can scan. Stay in prose form (no bullets inside cards). Use backticks for code names, markdown links for cross-repo references.

### Appending a month to the release timeline

1. Locate `### 2026 release timeline` under `## STACK`.
2. Append a new row to the table.
3. If the month belongs to a new quarter, fill in `**Q3**` / `**Q4**` etc. and leave subsequent rows of the same quarter blank in that column.
4. The `Month` cell is always bold. The `Shipped` cell is plain.
5. If the `Shipped` cell would otherwise become a wall of comma-separated text, group by project family with a bold inline lede (`**TR-300:**`, `**Magic Pantry:**`, `**SHAUGHV brand:**`, `**Other:**`) and use `<br><br>` between groups so the cell renders with paragraph-like breathing room.

### Adding a focus bullet to the deep-dive

1. Open the `<details>` with summary "More on what I'm building right now, full breakdown" under `## STACK`.
2. Add a bullet in the shape: `- **Topic heading.** One-sentence summary.` followed by nested sub-bullets for specifics: `  - **Sub-heading:** specific detail ending in a period.` When a bullet has multiple distinct sub-points (phases of a sprint, multiple PRs landing the same week, multiple components touched), break them out as nested sub-bullets rather than packing 8-12 sentences into one prose paragraph. Each sub-bullet opens with a bold inline lede so the reader can scan.
3. Insertion order is roughly by priority / recency.

### Adding a project to `CURRENT WORK`

If the table already has 6 cells (full), decide which existing project to demote to the workshop. Then:
1. Promote: write a new `<td>` cell for the new project; insert into the table; demote one existing project by deleting its `<td>` and mentioning it in the workshop paragraph instead.
2. Or replace: swap the demoted project's `<td>` contents with the new project's.

### Adding a new technique to the README

If you introduce a new sanitizer-safe trick (e.g., a new GFM feature, a new widget, a new Mermaid type):
1. Implement it inline.
2. Add a row to the colophon's technique table describing it and where it's used.

### Adding a stat shield to NUMBERS

1. Locate the centered `<div align="center">` row of stat shields under `## NUMBERS`.
2. Add a new `![Name](url)` line, using either the `shields.io/badge/dynamic/json` pattern (for arbitrary GitHub API fields) or the `shields.io/github/<endpoint>/<user>` pattern.
3. Follow the color rule from `DESIGN_SYSTEM.md`: `color=204F20&labelColor=F5E0C5`.
4. Add a row to the colophon table.

---

## What to never touch without a reason

- The order of the seven top-level sections.
- The 6-cell layout of `CURRENT WORK` (`<table>` with two `<td width="50%">` per `<tr>`).
- The `<picture>`-wrapped dual-source pattern on every dark/light-themed widget.
- The exact heading names `## NOW`, `## CURRENT WORK`, `## STACK`, `## NUMBERS`, `## COLOPHON` (anchors and refresh-automation selectors depend on them).
- The two-color palette of forest `#204F20` and cream `#F5E0C5`.
- The "no em dashes ever" rule (this overrides the SHAUGHV master design system).

---

## When in doubt

1. Check `DESIGN_SYSTEM.md` for the visual and structural rule.
2. If the rule is not in `DESIGN_SYSTEM.md`, look at the existing `README.md` and match the pattern of nearby content.
3. If neither answers the question, ask the user before improvising.
