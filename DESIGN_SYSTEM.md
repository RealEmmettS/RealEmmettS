# Design System

Comprehensive reference for the Next.js portfolio. Use this as the contract for visual language, motion, and interaction patterns across projects.

## Brand Principles
- Minimal, functional layouts with Bauhaus-inspired geometry and decisive typography.
- Clarity first: interaction cues (hover, focus, scroll) must guide hierarchy, not add noise.
- Motion supports meaning: staggered reveals, subtle parallax/hover depth, smooth global scroll.
- Consistent orange accent on actionable elements; cream/forest neutrals for structure; dark mode stays high-contrast.

## Tech & Global Behavior
- Stack: Next.js 16 App Router, React 19, TypeScript, Tailwind CSS v4 utilities via `@theme inline`, framer-motion, Lenis smooth scrolling, lucide-react icons.
- Global layout: `src/app/layout.tsx` wraps pages with `Navbar`, `DotMatrix`, `CustomCursor`, `SmoothScroll`, and `Footer`.
- Base body classes: `antialiased bg-background text-foreground overflow-x-hidden`. Max content width per section: `max-w-[1920px]` centered with horizontal padding `px-6` (mobile) / `md:px-12` (desktop).
- Data attributes: `data-magnetic` marks interactive targets for the custom cursor hover state.

## Foundations

### Color System (CSS variables via `src/app/globals.css`)
- Light theme (`color-scheme: light`):
  - `--background` / `--color-cream`: `#F5E0C5`
  - `--foreground` / `--color-forest`: `#204F20`
  - `--muted-gold` / `--color-gold`: `#C2A83E`
  - `--orange` / `--color-orange`: `#FF5E1A`
  - `--dot-color`: `var(--foreground)`
- Dark theme (`prefers-color-scheme: dark`):
  - `--background`: `#090909`
  - `--foreground`: `#E6E6E6`
  - `--muted-gold`: `#2F2F2F`
  - `--orange`: `#FF5E1A`
  - `--dot-color`: `#3a3a3a`
- Mobile dark override (`@media (prefers-color-scheme: dark) and (max-width: 768px)`): background `#0B0B0B`, foreground `#F2F2F2`, muted gold `#141414`, dot-color `#3e3e3e`, plus helper classes:
  - `.mobile-dark-surface`: force near-black surfaces
  - `.mobile-dark-border`: lighten borders for contrast
  - `.mobile-dark-text`: lighten copy
  - `.mobile-dark-panel`: translucent panels with stronger shadow
  - `.mobile-dark-gradient`: orange-accented radial gradient overlay
- Usage: cream for primary surfaces, forest for text/borders, gold for muted strokes, orange for CTAs/accents. Avoid introducing new hex values unless first added as tokens.

### Typography
- Fonts (via `next/font/google`):
  - Headings: `Unbounded` (`--font-heading`)
  - Body/UI: `Manrope` (`--font-sans`)
- Defaults: headings use `font-heading`, body and UI text use `font-sans`. Body color `var(--foreground)`; headings often uppercase with tight leading.
- Scale observed in current UI (Tailwind sizes):
  - Hero title: `text-5xl` → `lg:text-[11rem]`, leading `0.95`
  - Section titles: `text-6xl` → `md:text-8xl`
  - Subhead/eyebrow: `text-xl` → `md:text-2xl`, uppercase, `tracking-widest`
  - Body copy: `text-lg` → `md:text-xl`, `leading-relaxed`
  - Metadata/labels: `text-sm` uppercase, `tracking-widest`; pills use `text-xs` mono uppercase
- Casing: buttons and nav uppercase; body paragraphs sentence case. Tracking is generous on labels/eyebrows for industrial feel.

### Layout, Spacing & Shape
- Section vertical rhythm: hero `min-h-screen` with `pt-20`; other sections `py-20` to `py-32`.
- Container padding: `px-6` mobile, `md:px-12` desktop; keep consistent across sections.
- Grid patterns:
  - Two-column cards (About/Philosophy, Contact hero/form) with slightly uneven fractions (`1.05fr/0.95fr` or `0.95fr/1.05fr`).
  - Projects list: `md:grid-cols-12` with spans `1 / 4 / 6 / 1` for index/info/media/CTA.
  - Skills: `md:grid-cols-2`, `lg:grid-cols-4`.
- Borders: prefer subtle strokes `border-forest/20`–`/30`; accent strokes `border-orange` for emphasis lines; project rows use solid `border-forest`.
- Radius: mostly square; pills `rounded-full`; contact iframe wrapper `rounded-[32px]` with inner `rounded-[28px]`.
- Shadows/blur: rare; contact form uses `shadow-[0_30px_80px_rgba(32,79,32,0.12)]` and soft gradient overlays; cards use blurred radial glows for depth.

### Iconography & Imagery
- Icons from `lucide-react` (`ArrowUpRight`, `Menu`, `X`).
- Project imagery via `next/image` with grayscale → color on hover; images live in `public/*.webp`.
- Use simple line icons and keep hover states subtle (opacity fades, color transitions).

## Motion & Interaction
- Smooth scrolling: Lenis initialized globally; call `lenis.raf` in `requestAnimationFrame`. Keep section anchors compatible (`href="#section"`).
- Framer Motion patterns:
  - Hero: container stagger (`staggerChildren: 0.1`, `delayChildren: 0.2`), items animate `y: 100 → 0`, `opacity: 0 → 1`, duration `0.8`, ease `[0.16, 1, 0.3, 1]`.
  - Projects: while-in-view fade/slide (`opacity 0→1`, `y 50→0`, duration `0.6`, stagger by `0.1`).
  - Skills: while-in-view fade/slide with `delay index*0.1`, duration `0.5`.
  - About text: per-word opacity interpolation on scroll via `useScroll` + `useTransform`.
- Custom cursor: visible only on fine pointers. Orange dot (`w-4 h-4`, `mix-blend-difference`) springs toward pointer (`damping 25`, `stiffness 700`) and scales to `2.5x` over links/buttons/`data-magnetic` targets.
- Dot matrix background: canvas of 30px spaced dots, radius `1.5`; reacts to cursor within 150px influence radius; adapts dot color to theme ensuring ≥2.5 contrast ratio. Rebuilds on resize, theme, or viewport breakpoints.
- Hover states:
  - Links/nav: color shift to orange; underline for contact links.
  - CTA buttons: orange bg → forest on hover; rounded minimal radius.
  - Project rows: on hover background flips to forest, text to cream; images scale/lose grayscale; arrow chip fills orange on hover.
  - Footer social links: arrow fades in (`opacity-0 → 100`) on hover.

## Surfaces & Backgrounds
- Global canvas `DotMatrix` sits behind everything (`z-[-1]`, `opacity-40`), giving the dotted field.
- Radial overlays: About and Contact sections use layered radial gradients (orange + forest) for atmospheric glow; mobile dark gradient helper reinforces contrast.
- Lines/dividers: fine hairlines (`h-px`) with gradients or muted forest strokes to segment sections.

## Components & Section Patterns
- **Navigation** (fixed top, mix-blend-difference):
  - Desktop: brand mark left (`EMMETT`), right-aligned links with uppercase labels.
  - Mobile: hamburger toggles full-screen overlay (`bg-forest`, center-aligned 3xl links); closes on link tap.
- **Hero**: centered vertical stack; eyebrow “Digital Craftsman”; oversized uppercase first/last name split into two lines; CTA button anchors to projects.
- **About/Philosophy**:
  - Two cream cards with thin borders and blurred corner glows.
  - About card: animated paragraph, highlight chips (mono, rounded-full, bordered).
  - Philosophy card: mirrored layout with bullet dots (`bg-orange`), text at `text-lg`.
- **Projects**:
  - Header row with section title and index meta; list entries separated by borders.
  - Each row: index (mono), title/category/year, description, tech pill, media preview, external link arrow (if URL defined). Hover inverts colors and activates image reveal.
- **Skills**:
  - Four columns of categories; left border in orange; items in mono uppercase list.
- **Contact**:
  - Two-column: headline + copy + quick links, and YouForm embed (`iframe` `h-[720px]` inside rounded translucent panel with gradient overlay and blur).
  - Surface uses cream base with gradient background; mobile dark helpers applied.
- **Footer**:
  - Forest background, cream text; headline, availability blurb, CTA mail link with arrow; socials stacked right; copyright uses `new Date().getFullYear()`.

## Responsive Behavior
- Tailwind defaults (sm 640, md 768, lg 1024, etc.).
- Patterns:
  - Nav collapses to hamburger below `md`; padding increases on desktop.
  - Hero type scales: `text-5xl` mobile → `lg:text-[11rem]`; spacing increases (`gap-2 → gap-4`).
  - Layout grids collapse to single column on mobile; Contact iframe stays full-width with preserved height.
  - Images hidden on mobile? Projects keep preview visible but rely on grid stacking (media after copy).
- Mobile dark overrides keep dark mode legible on small screens; apply helper classes to new dark surfaces when adding sections.

## Accessibility & Content Guidelines
- Maintain high contrast using provided tokens; rely on `--dot-color` auto-contrast logic for add-on canvases.
- Keep buttons/links keyboard accessible; avoid `cursor: none` on coarse pointers (handled automatically by `CustomCursor`).
- Use semantic headings per section (h1 in hero, h2 elsewhere) and preserve uppercase labels via CSS, not raw text when possible.
- External links use `rel="noopener noreferrer"` and `target="_blank"` when leaving site.

## Implementation Checklist (for new sections/components)
- Use root padding/grid conventions: `max-w-[1920px] mx-auto px-6 md:px-12` and `py-20/32` depending on prominence.
- Choose surfaces from token set (cream/forest/orange/gold); add new colors only through `globals.css` variables.
- Set typography with `font-heading` for headlines and `font-sans`/`font-mono` for body/meta; keep CTA/nav uppercase with generous tracking.
- Provide hover/focus styles consistent with existing patterns (color shifts, opacity fades, subtle scale not required).
- Respect smooth scrolling and anchor targets; avoid position schemes that break Lenis scroll.
- For interactive canvases/backgrounds, ensure theme-aware colors and cleanup listeners on unmount (follow `DotMatrix` pattern).
