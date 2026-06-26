# Profile README Design System

This is the design contract for `README.md`, the profile README rendered at `github.com/RealEmmettS`.

The page is a GitHub-safe SHAUGHV surface. It borrows SHAUGHV's type-forward, proof-first, selected-work language, but this file overrides the broader SHAUGHV design system whenever GitHub constraints or profile readability require a narrower rule.

---

## Hard rules

1. **Two colors only.** Forest `#204F20` and cream `#F5E0C5`. Do not introduce any other hue, even as a small accent.
2. **No em dashes.** Use commas, periods, colons, semicolons, slashes, hyphens, or `&middot;`.
3. **No emoji.** None in headings, copy, summaries, links, or visible labels.
4. **No GitHub Actions in this repo.** Automation that refreshes content must live elsewhere and push here.
5. **No CSS or JavaScript-dependent profile rendering.** Do not add scripts, stylesheets, inline SVG, custom attributes for styling, iframes, forms, videos, audio, or new-tab targets.
6. **Sanitizer-safe HTML only.** The allowed structural vocabulary is headings, markdown, `<picture>`, `<source>`, `<img>`, `<details>`, `<summary>`, `<table>`, `<tr>`, `<td>`, `<br>`, `<sub>`, `<strong>`, `<kbd>`, `<div align="center">`, and HTML comments.
7. **Proof before density.** The first viewport must make the work legible: what Emmett builds, why it is credible, and where to click next.

---

## Palette

| Token | Hex | Use |
|---|---|---|
| Forest | `#204F20` | Dark surface, text on cream widgets, badge value blocks |
| Cream | `#F5E0C5` | Light surface, text on forest widgets, badge label blocks |

Standard badge parameters:

```text
color=204F20&labelColor=F5E0C5&logoColor=204F20
```

Theme-aware widget pattern:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="FOREST_SURFACE_URL">
  <img alt="Description" src="CREAM_SURFACE_URL">
</picture>
```

Dark-mode `srcset` uses forest background with cream foreground. Light-mode `img` uses cream background with forest foreground.

---

## Voice

- **Headings are uppercase.** Current top-level headings are `LATEST SHIPS`, `SELECTED SYSTEMS`, `STACK`, `NUMBERS`, `WORKSHOP ARCHIVE`, `COLOPHON`.
- **Body copy is sentence case.** Keep it dry, direct, and specific.
- **Use first person singular when needed.** SHAUGHV is one person. Do not write "we" unless quoting or describing a client/team system.
- **Use concrete proof.** Prefer shipped versions, repos, release links, installer behavior, architecture outcomes, and product capabilities over broad adjectives.
- **Use slash-separated identity strings.** Example: `Rust diagnostics / agent tooling / full-stack product systems.`
- **Use `&middot;` for inline metadata separation** when a visual separator is needed.
- **No exclamation marks** except markdown image syntax.

---

## Structure

The README has seven movements in this order:

```text
1. HERO              Static identity banner, positioning line, proof strip, contact pills
2. LATEST SHIPS      GFM note with exactly 3 compact proof entries
3. SELECTED SYSTEMS  Indexed selected-work table with 5 systems
4. STACK             Mermaid operating map + focused badge set
5. NUMBERS           Live profile metrics and activity widgets
6. WORKSHOP ARCHIVE  Collapsed long-form depth
7. COLOPHON          Renderer catalogue + footer banner
```

Each top-level section is separated by a single `---` rule.

Do not add an eighth top-level section without removing or merging another one. GitHub profile pages are read as a single scroll.

---

## Component Rules

### Hero

- Keep the capsule-render banner static. Do not add typing animations.
- The first text line under the banner is a short positioning statement.
- The proof strip is a four-cell table. Each cell has a short uppercase label and a `<sub>` explanation.
- Contact pills stay in the hero. Vanity metrics do not.

### Latest Ships

- Uses exactly one GFM `[!NOTE]` block.
- Contains exactly 3 entries.
- Each entry starts with `&middot; **Project or system.**`.
- Each entry is 2-3 sentences maximum and includes one public link when possible.
- Do not put implementation archaeology here. Move that to `WORKSHOP ARCHIVE`.

### Selected Systems

- Exactly 5 selected systems unless the user's active public work changes substantially.
- Current set: Qube TX, WB-300, Magic Pantry, shaughv-code, QorkMe.
- Use indexed rows: `001`, `002`, etc.
- Each row has a system name, tech pills, one short description, and an evidence column.
- Cap each system description at 120 words.
- Public evidence links beat internal-only claims. If a system is private, say so plainly and keep it brief.

### Stack

- The Mermaid map is an operating map, not a resume keyword dump.
- Current branches: `SYSTEMS`, `WEB`, `MOBILE`, `AI_WORKFLOWS`, `CLOUD_DATA`.
- Keep badges focused to the working set. Do not add every tool Emmett has ever touched.

### Numbers

- Live metrics live here, not in the hero.
- Keep profile views, followers, last push, public repos, total stars, GitHub start year, streak, top languages, and activity graph.
- All images and badges must stay forest/cream.

### Workshop Archive

- Collapsed by default.
- Holds release history, secondary public surfaces, and private/internal work summaries.
- Use short bullets with bold ledes.
- Avoid nested deep trees unless a section would otherwise become unreadable.

### Colophon

- The colophon lists only techniques actually used in the current README.
- If a rendering technique is removed from the README, remove it from the colophon.
- If a rendering technique is added, add it to the colophon and verify it is sanitizer-safe.

---

## Forbidden Patterns

- Third colors.
- Emoji.
- Em dashes or named em-dash entities.
- Typing SVGs in the hero.
- Hero vanity metric rows.
- Long uncollapsed release-ledger prose above `WORKSHOP ARCHIVE`.
- Inline SVG.
- Scripts or stylesheet-dependent rendering.
- Style attributes, class attributes, or new-tab target attributes.
- GitHub Actions in this repo.
- Trophy widgets, generated contribution snakes, 3D contribution grids, WakaTime cards, or metrics dashboards unless the no-Actions rule changes.

---

## Pre-push Checklist

Run these checks before pushing:

1. No em dashes or named em-dash entities.
2. No emoji.
3. No colors beyond `204F20` and `F5E0C5` in `README.md`.
4. No script tags, style attributes, class attributes, inline SVG, iframes, forms, video, audio, or new-tab targets.
5. Every `<picture>` has a `<source>` and an `<img>`.
6. Every `<img>` has meaningful alt text.
7. The TOC links match the current headings.
8. `LATEST SHIPS` has exactly 3 entries.
9. `SELECTED SYSTEMS` has exactly 5 systems, each with description length at or under 120 words.
10. The colophon matches the actual techniques in the README.
11. Inspect the rendered GitHub profile at desktop and mobile widths after publishing.

---

## External Services

| Service | Use |
|---|---|
| `capsule-render.vercel.app` | Header and footer wave banners |
| `img.shields.io` | Contact, metric, and stack badges |
| `komarev.com/ghpvc` | Profile view counter |
| `streak-stats.demolab.com` | Streak card |
| `github-readme-stats.vercel.app/api/top-langs` | Top languages card |
| `github-readme-activity-graph.vercel.app` | Activity graph |
| `api.github.com` | Dynamic JSON shields |

If any service breaks, update the URL or remove the widget. Do not replace a broken widget with a heavier renderer that violates the hard rules.
