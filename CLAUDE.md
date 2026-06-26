# CLAUDE.md

Operator guide for refreshing this repo's `README.md`, the profile README rendered at `github.com/RealEmmettS`.

Read this file before editing `README.md`, then check `DESIGN_SYSTEM.md` for visual and sanitizer rules.

---

## Files

| File | Purpose | Edit cadence |
|---|---|---|
| `README.md` | Public GitHub profile page. | Frequent |
| `DESIGN_SYSTEM.md` | Rendering, voice, layout, and validation contract. | Rare |
| `CLAUDE.md` | Refresh map and content ownership. | Rare |
| Resume source | Plain-text resume content. Not rendered on the profile. | Occasional |
| `agents/` | Local agent descriptors. Not part of the public profile. | Rare |

---

## Current README Structure

```text
1. HERO              Static identity banner, positioning line, proof strip, contact pills
2. TOC               Collapsible jump navigation
3. LATEST SHIPS      Three high-signal current proof entries
4. SELECTED SYSTEMS  Five indexed selected systems
5. STACK             Operating map and focused working-set badges
6. NUMBERS           Live GitHub/profile metrics and widgets
7. WORKSHOP ARCHIVE  Collapsed release depth and secondary work
8. COLOPHON          Renderer catalogue and footer banner
```

The TOC is not counted as a content movement, but it must stay directly below the hero.

---

## Section Inventory

### HERO

Static unless the positioning changes.

- Capsule banner: Emmett Shaughnessy / Digital Craftsman.
- Positioning line: `Rust diagnostics / agent tooling / full-stack product systems.`
- One short paragraph naming the current focus.
- Four-cell proof strip.
- Contact pills: Website, Qube TX, Resume, Email.

Do not put profile metrics back in the hero.

### LATEST SHIPS

Most frequently refreshed section.

- Keep exactly 3 entries.
- Each entry is 2-3 sentences.
- Each entry should include a public link when possible.
- Good entries explain what shipped and why it matters.
- Move long implementation history to `WORKSHOP ARCHIVE`.

### SELECTED SYSTEMS

Curated work list for technical clients and developer peers.

Current systems:

1. Qube TX.
2. WB-300.
3. Magic Pantry.
4. shaughv-code.
5. QorkMe.

Each row has:

- index and category;
- linked system heading when public;
- 4 tech pills;
- one short description, 120 words max;
- evidence column with public links or concise proof.

To add a new selected system, demote one existing system to `WORKSHOP ARCHIVE` unless the user explicitly asks to expand the table.

### STACK

Operating map, not a keyword dump.

Current Mermaid branches:

- `SYSTEMS`.
- `WEB`.
- `MOBILE`.
- `AI_WORKFLOWS`.
- `CLOUD_DATA`.

Badges should represent the current working set only.

### NUMBERS

Live metrics and widgets.

Current widgets:

- profile views;
- followers;
- last push;
- public repos;
- total stars;
- GitHub since year;
- streak card;
- top languages card;
- activity graph.

Keep all metrics in this section.

### WORKSHOP ARCHIVE

Collapsed depth.

Current archive groups:

- release ledger;
- secondary public surfaces;
- private systems summarized without repo links.

Use short bullets with bold ledes. This section is where release history belongs.

### COLOPHON

Self-documenting renderer catalogue.

Update the technique table whenever a technique is added or removed. Keep the footer banner below the colophon.

---

## Refresh Cadence

| Content | Refresh cadence | Notes |
|---|---|---|
| Hero banner and contact pills | Rare | Only when identity or URLs change |
| Hero positioning and proof strip | Quarterly or major focus shift | Keep first viewport sharp |
| Latest ships | Weekly during active work | Exactly 3 entries |
| Selected systems descriptions | Monthly or major release | Keep each under 120 words |
| Stack map and badges | Rare | Only when working categories shift |
| Numbers | Live | No commit needed unless widget breaks |
| Workshop archive | Monthly or after major release | Collapsed by default |
| Colophon | Whenever rendering technique changes | Must match README |

---

## Common Operations

### Refresh Latest Ships

1. Locate `## LATEST SHIPS`.
2. Keep the note heading month current.
3. Replace the three entries with the strongest current proof.
4. Keep each entry at 2-3 sentences.
5. Include public links when available.

### Update a Selected System

1. Locate the matching row under `## SELECTED SYSTEMS`.
2. Update only the description and evidence links unless the system's role or stack actually changed.
3. Keep the description under 120 words.
4. Preserve the indexed row structure.

### Demote or Promote Work

1. If adding a selected system, choose one existing selected system to move into `WORKSHOP ARCHIVE`.
2. Keep `SELECTED SYSTEMS` to five rows unless the user explicitly asks otherwise.
3. Keep the archive summary short and link public repos.

### Update Stack

1. Edit the Mermaid map only if the operating categories changed.
2. Keep the five branch model unless the whole profile strategy changes.
3. Add badges only for tools that reinforce current positioning.

### Update Colophon

1. Compare the colophon table to actual README techniques.
2. Remove stale rows.
3. Add rows for new sanitizer-safe techniques.

---

## Validation

Before pushing:

1. Run `git diff --check`.
2. Search `README.md` for em dashes and named em-dash entities.
3. Search `README.md` for colors other than `204F20` and `F5E0C5`.
4. Search `README.md` for scripts, style attributes, class attributes, inline SVG, iframes, forms, video, audio, and new-tab targets.
5. Confirm every `<picture>` has both `<source>` and `<img>`.
6. Confirm every `<img>` has alt text.
7. Confirm the TOC anchors exist.
8. Confirm `LATEST SHIPS` has exactly 3 entries.
9. Confirm `SELECTED SYSTEMS` has exactly 5 rows and each description is at or under 120 words.
10. Inspect the live GitHub render on desktop and mobile after publishing.

When in doubt, choose readability and public proof over density.
