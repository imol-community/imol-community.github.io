# IMOL Community Website

This is the source for the IMOL community website. It is a static site built with [Astro](https://astro.build/).

## Quick Start

Install dependencies:

```bash
npm install --ignore-scripts
```

Run the local development server:

```bash
npm run dev
```

Open the URL printed by Astro, usually:

```text
http://localhost:4321/
```

Build the static site:

```bash
npm run build
```

The production build is written to `dist/`.

## Deployment

Pushing to `main` runs `.github/workflows/deploy.yml`. The workflow installs dependencies with `npm ci --ignore-scripts`, builds the Astro site, uploads `dist/`, and deploys it with GitHub Pages Actions.

In the repository settings, GitHub Pages should use **GitHub Actions** as its source.

## Project Map

```text
src/
  components/
    Nav.astro          Main navigation.
    Footer.astro       Footer contact/community links.
  layouts/
    PageLayout.astro   Shared page shell, metadata, header, footer, CTA block.
  pages/
    index.md           Homepage.
    manifesto.md       Manifesto page.
    community.md       Board and member information.
    participate.md     Mailing list, Discord, membership, and activities.
    resources.md       Literature/resources.
    archive.md         Past events page.
    jobs.md            Hidden from navigation while empty, but still available at /jobs/.
    404.md             Not-found page.
  styles/
    global.css         Site-wide visual design and responsive rules.

public/
  CNAME                Custom domain for GitHub Pages builds.
  assets/img/          Static images used by the site.
```

## Editing Content

Most page content lives in Markdown files under `src/pages/`. These files can contain Markdown and inline HTML.

The main navigation is configured in `src/components/Nav.astro`.

The footer links are configured in `src/components/Footer.astro`.

The shared page structure and call-to-action buttons are in `src/layouts/PageLayout.astro`.

The visual design is in `src/styles/global.css`.

## Current Navigation

Visible navigation:

- Home
- Manifesto
- Community
- Seminars
- Participate
- Resources
- Past events

Hidden but kept:

- Jobs: available at `/jobs/`, hidden from navigation while empty.

Removed from navigation:

- Contact: contact links are in the footer.

## Dependency Hygiene

The direct dependency is Astro. The current install also pins `esbuild` through `package.json` overrides.

Useful checks:

```bash
npm audit --omit=dev --audit-level=moderate
npm audit signatures
```
