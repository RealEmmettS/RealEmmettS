# Profile design system

The masthead and three illustrated sections form a small portfolio of Emmett’s independent work. Contact buttons lead to the portfolio, résumé, and email. The “On this page” disclosure links to the three native section headings.

## Artwork

Use forest `#204F20` and cream `#F5E0C5` for lettering, rules, and backgrounds. The masthead, buttons, release chart, and type specimen have separate light and dark files. The Magic Pantry card uses the approved forest artwork in both themes. The grocery UI and Goose retain their original colors.

| Asset | Source and maintenance |
|---|---|
| Masthead | Makira Black for the name, Geist Mono for the label, Geist Serif for the byline. The halftone contours are drawn in the renderer. |
| Contact buttons | Three-times-resolution PNGs displayed at their logical width and 44 pixels high. Keep the label in each link’s image alt text. |
| Magic Pantry 2 | Makira Black above Geist Serif. Keep five clear pixel rows between the visible letters at 1080 pixels wide. The renderer uses the cropped grocery-list screenshot in `tools/pantry-screen.png`. |
| Qube TX release chart | Each square is one published, non-prerelease GitHub release. The counts in `RELEASES` are a dated snapshot of the three repositories linked below the chart. When refreshing it, group their releases by UTC publication month and update the month labels, date range, totals, caption, and alt text together. |
| Type specimen | Set each family name and its sample glyph in that family. Resolve fonts from the [CDN catalog](https://cdn.shaughv.com/tree.json). |
| Goose | Cropped from the [Goose renderer’s reference frame](https://github.com/RealEmmettS/goose/blob/f463e2a7bc5f6cd6490345b948d2242bc09cca7c/crates/honk-engine/tests/golden/side_mid_stride.png). Copyright 2026 Emmett Shaughnessy &lt;hey@emmetts.dev&gt;. [Source license](https://github.com/RealEmmettS/goose/blob/f463e2a7bc5f6cd6490345b948d2242bc09cca7c/LICENSE) |

Run `python tools/render_profile.py` with Python and Pillow installed. It loads the three font faces into memory from the CDN catalog, checks their SHA-256 digests, and writes the generated PNGs to `assets/`.

## GitHub rendering

Use linked images, native headings, descriptive links, and keyboard-operable `<details>` for the contents and Goose. Keep project names, descriptions, and destinations available as text. GitHub controls the page background. The illustrated panels carry the brand colors across the page.

Before publishing, run `git diff --check`, verify paths, alt text, link destinations and section anchors, and compare the rendered profile in both themes at desktop and phone widths. Check the same public profile after publication. [GitHub’s guide to theme-aware README images](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github#adding-an-image-to-suit-your-visitors)
