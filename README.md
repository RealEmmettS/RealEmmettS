<div align="center">

# Emmett Shaughnessy

**Full-Stack Developer | Technical Consultant | Builder**

[![Website](https://img.shields.io/badge/emmettshaughnessy.com-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://emmettshaughnessy.com)
[![QubeTX](https://img.shields.io/badge/Qube_TX-FF6B6B?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K&logoColor=white)](https://qubetx.com)

---

</div>

## 🚀 Current Projects

<table>
<tr>
<td width="50%">

### [Qube TX](https://qubetx.com)
**Diagnostics Tooling & Web Studio**

A growing ecosystem of Rust CLI diagnostics tools — `qube-machine-report` (TR-300, now at v3.13.x with Windows polish, VPN-aware Windows IP, Fast Startup uptime annotation, and a `uzers` migration to clear RUSTSEC advisories), `qube-network-diagnostics` (nd300 v3.0.x — subcommand syntax, a diagnostic-driven triage loop with bounded iterations, and a probe-and-retry self-update chain that prefers cargo when invokable and falls back to the installer with per-attempt diagnostics), and `qube-system-diagnostics`. Around them sit the web surfaces (`QubeTX_Landing`, `qube-machine-report-homepage`), the multi-provider SpeedQX web app (bootstrap CIs, inverse-variance weighted aggregation, RFC 3550 jitter, network-metadata pre-test), and offline installer bundles (`qube-reports-executables`). Also where most freelance/client work lives.

`Rust` `TypeScript` `Next.js` `CLI Tooling`

</td>
<td width="50%">

### [QorkMe](https://qork.me)
**URL Shortener**

Custom aliases, click analytics, and a clean redirect layer, now running on a Next.js + Supabase stack with hardened RLS, an admin dashboard, and a Makira-typeset UI.

`Next.js` `TypeScript` `Supabase` `Tailwind`

</td>
</tr>
<tr>
<td width="50%">

### [shaughvOS](https://github.com/RealEmmettS/shaughvOS)
**Custom Diagnostics OS**

Lightweight Debian-based diagnostics OS with Shaughv branding. Just shipped v1.20.0 (install + startup validation, focus-smoke shellcheck gate, release-newline check) on top of the v1.19.x CLI-first boot, working desktop shortcuts, and apt-mark fixes.

`Shell` `Linux` `Build Pipelines`

</td>
<td width="50%">

### Dorsey 2026
**Music Artist Site**

A full rebuild of a touring artist's site on Next.js 16 / React 19 / Tailwind v4, with shadcn/ui components and Framer Motion choreography. Recently pivoted from a custom Jazz-Bauhaus reinterpretation to a faithful recreation of the live leonleedorsey.com visual language — header/footer reworked, home / about / music / store / videos / contact and several press / gear pages rebuilt, mobile nav swapped to a full-screen white sheet, and Squarespace media imported locally to avoid hotlinking. Currently finishing secondary route parity and final QA.

`Next.js 16` `React 19` `Tailwind v4` `Framer Motion`

</td>
</tr>
<tr>
<td width="50%">

### [Time](https://github.com/RealEmmettS/time)
**Atomic Clock Web App**

A nicer-looking alternative to time.gov — accurate, fast, and visually pleasant.

`JavaScript` `Web` `UX`

</td>
<td width="50%">

### [Personal Site](https://emmettshaughnessy.com)
**Portfolio & Writing**

Professional showcase, project index, and technical writing. Mid-rebuild on a fresh TypeScript stack.

`TypeScript` `Next.js` `Vercel`

</td>
</tr>
</table>

### Also in the workshop
Web surfaces around the Qube TX ecosystem (`QubeTX_Landing`, `qube-machine-report-homepage`, `qube-reports-executables` for offline installers), the SpeedQX web speed-test app and a parallel Expo/React Native port (porting the v2.0/v2.1 measurement engine, statistics module, and metric-info UX onto mobile), Remotion-based programmatic video experiments, MDX docs sites, and a rotating cast of small utilities (timer, qrgen, csv tools, countdown apps).

## 💻 Tech Stack

```mermaid
graph LR
    A[Web] -->|TypeScript / Next.js| B[Frontend & SSR]
    A -->|React Native / Expo| C[Mobile]
    D[Systems] -->|Rust| E[CLI Diagnostics & Reports]
    D -->|Shell| F[Lightweight OS Tooling]
    G[Backend] -->|Node.js| H[APIs]
    G -->|Python| I[Scripting & Data]
    J[Cloud] -->|Vercel| K[Edge Deployment]
    J -->|Cloudflare| L[DNS / CDN]
    J -->|AWS| M[S3, EC2, SES]
    J -->|Supabase| N[Postgres / Auth / RLS]
    J -->|Firebase| O[Realtime / Auth]
```

### Languages
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-FA7343?style=flat-square&logo=swift&logoColor=white)

### Frameworks & Libraries
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Tailwind](https://img.shields.io/badge/Tailwind_v4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-000000?style=flat-square&logo=shadcnui&logoColor=white)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white)
![Expo](https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Remotion](https://img.shields.io/badge/Remotion-3178C6?style=flat-square&logo=remotion&logoColor=white)

### Cloud & Infrastructure
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)

### Where my focus is right now
- 🦀 **Rust diagnostics tooling** – shipping the v3.x lines of `qube-machine-report` (v3.13.x) and `qube-network-diagnostics` (nd300 v3.0.x): subcommand syntax, diagnostic-driven triage loops, Windows polish, VPN-aware reporting, and a probe-and-retry self-update chain that survives missing toolchains
- 🐧 **shaughvOS** – Debian-based diagnostics OS, just shipped v1.20.0 with install/startup validation and a focus-smoke shellcheck gate
- 🎵 **Dorsey 2026** – touring artist's site rebuild on Next.js 16 / React 19 / Tailwind v4; mid-port of the live leonleedorsey.com layout with imported Squarespace media
- 🌐 **Modern web stacks** – Next.js 16 / React 19 / Tailwind v4 / shadcn/ui builds for client sites and Qube TX surfaces, deployed on Vercel
- 🔗 **Full-stack product work** – QorkMe on Next.js + Supabase with hardened RLS, click analytics, and an admin dashboard
- 📱 **Cross-platform mobile** – Expo / React Native speedtest porting the SpeedQX accuracy pipeline (bootstrap CIs, inverse-variance weighting, AIM scores, byte-weighted progress) onto iPhone/iPad
- 🤖 **AI-assisted workflows** – pairing Claude / Codex agents into real product development; release pipelines moved from foreground `gh run watch` to non-blocking Monitor poll-loops, with `gh --jq` keeping the diff portable across machines without local jq
- 🔧 **Technical consulting** – pragmatic, end-to-end solutions for client work through Qube TX

---

<div align="center">

**Building reliable, maintainable solutions that solve real problems.**

</div>
