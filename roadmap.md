# Hardwired NWA project roadmap

## Current milestone: Favicon suite, expanded 24-symbol vector sprite & donation card motifs

Implemented on 2026-10-11; see `docs/FAVICON.md`, `docs/DONATION-ICONS.md`, `docs/SVG-SPRITE.md`, and `docs/VERIFICATION.md` for local and subpath checks performed.

- **Hexagon Barbell Favicon Suite:** Authored a dedicated browser icon based on the blue hexagon and white barbell wordmark (`assets/images/hardwired-nwa-favicon.svg`). Automated full export via `scripts/build_favicons.py` producing `static/favicon.svg`, multi-resolution `static/favicon.ico` (16, 32, 48px), transparent PNGs (16x16, 32x32), 180px `apple-touch-icon.png`, 512px `site-icon-512.png`, downloadable ZIP kit, and standalone test gallery at `/favicon-preview/`. Injected across all layouts via `layouts/partials/favicon.html`.
- **24-Symbol Consolidated Vector Sprite:** Expanded `static/images/hardwired-icons.svg` via `scripts/build_svg_sprite.py` to house 24 distinct symbols across five semantic groups: 10 physical skills, 3 access cards, 3 support pathways, 6 commitments, and 2 donation card motifs (`donation-online`, `donation-check`).
- **Automated Vector Downloads & Gallery Previews:** Automated generation of 24 standalone SVG downloads in `static/downloads/icons/`, four group review sheets (skills, support, commitments, donations), full icon ZIP archive (`static/downloads/hardwired-nwa-icons.zip`), and an interactive multi-size gallery at `/icons-preview/`.
- **Artwork Tracing & Maintenance Scripts:** Added deterministic tracing pipelines (`scripts/trace_skill_artwork.py`, `scripts/trace_support_artwork.py`) preserving authentic gym whiteboard marker contours in pure vector form.

## Preceding milestone: Shared SVG symbol sprite, access icons & commitments review

Implemented on 2026-10-10; see `docs/SVG-SPRITE.md` and `docs/VERIFICATION.md` for local and subpath checks performed.

- **Consolidated SVG Symbol Sprite:** Generated a unified 14-symbol SVG sprite (`static/images/hardwired-icons.svg`, 5,492 bytes) via `scripts/build_svg_sprite.py`, eliminating per-page duplicate inline symbols. Referenced universally with subpath-safe external `<use href="{{ "images/hardwired-icons.svg" | relURL }}#...">`.
- **Ten Physical Skill Motifs:** Integrated the 10 general physical skills from the gym whiteboard mural (Cardio through Accuracy) in `layouts/partials/training-wall.html` on Home and Adaptive CrossFit pages, with standalone preview at `/motifs-preview/`.
- **Supporter Access Icon:** Redesigned the 02 / For Supporters card icon as a native vector SVG (`assets/images/motifs/access-scholarships.svg`, symbol `access-scholarships`), rendered via `layouts/partials/access-icon.html`.
- **Our Commitments Review Set:** Authored three vector commitment motifs (`commitment-safety`, `commitment-efficacy`, `commitment-efficiency`), with circular arc geometry for efficacy. Provided a standalone preview page at `/commitments-preview/`.
- **Transparent Vector Badge SVG:** Traced and integrated the updated Hardwired NWA badge logo (`assets/images/hardwired-nwa-badge.svg`) with full background transparency across header, footer, SVG favicon, and resized touch icons (`assets/images/hardwired-nwa-badge-icon.png`). Provided downloadable master vector at `static/downloads/hardwired-nwa-logo.svg`.

## Preceding milestone: GitHub Pages live deployment, CI/CD pipeline & mural-led training wall

Implemented on 2026-10-09; see `docs/VERIFICATION.md` for live and local checks performed.

- **GitHub Pages Live Hosting:** Published the responsive Hugo prototype to GitHub Pages at <https://ryan258.github.io/hardwired-nwa/> under repository `ryan258/hardwired-nwa`.
- **Subpath-Compatible Routing:** Configured menu URLs, templates, and markdown render hooks (`layouts/_default/_markup/render-link.html`) to dynamically support subpath base URLs (`/hardwired-nwa/`) without breaking standard root previews (`localhost:1313`).
- **Automated CI/CD Deployment:** Added GitHub Actions workflow (`.github/workflows/deploy.yml`) for Hugo extended 0.166.0 builds, automated link and asset verification, and deployment to GitHub Pages on pushes to `main`.
- **Automated Link & Asset Gate:** Created `scripts/check_links.py` to recursively validate internal routes, static assets, and section fragment IDs across all generated HTML files.
- **Mural-Inspired Training Wall:** Added a handwritten gym sketch layer inspired by the user-supplied whiteboard mural (`docs/references/mural-reference.png`, `docs/MURAL-DIRECTION.md`). Introduces a training-wall component (`layouts/partials/training-wall.html`), Patrick Hand typography accents, hand-drawn barbell illustration, and an accessible 5-tier training pyramid (Nutrition, Conditioning, Gymnastics, Lifting, Sport).
- **Adaptive CrossFit Integration:** Embedded the training wall on both the Home landing page and the Adaptive CrossFit interior page (`content/adaptive-crossfit.md`), connecting to the `#what-scaling-means` anchor.

## Preceding milestone: Brand identity, charter copy & interactive prototype

Implemented on 2026-10-09; see `docs/VERIFICATION.md` for local checks.

- **Charter Information Architecture:** Implemented eight core charter routes in Hugo with zero runtime dependencies: Home, About, Our Coach, Our Gym, Adaptive CrossFit, Support & Scholarships, FAQ, and Contact.
- **Organization Palette Alignment:** Applied confirmed organization colors: slate blue (`#2C5D75`) and peach (`#F9B689`), supported by navy (`#193442`), warm white (`#F7F4EF`), and pale blue (`#DCE9EF`).
- **Editorial Concept Illustration:** Generated and integrated a textured editorial cut-paper hero illustration (`static/images/adaptive-training-concept-blue-peach.png`) matching brand colors and tone.
- **Client-Side Prototype Interactions:** Implemented a non-transmitting inquiry preview form with validation, interactive scholarship cost calculator ($75 punch cards vs. $135 monthly memberships), accessible donation modal dialog, expandable FAQ accordion, and mobile drawer navigation.

## Future roadmap: Organization review & production handoff

Pending stakeholder confirmation; see `docs/HANDOFF.md` for detailed review requirements.

- **Organization Confirmations:**
  - Official mission text and scope approval.
  - Head coach biography, verified credentials, and consent for portrait photography.
  - Facility address, arrival route, parking, restrooms, and verified accessibility audit.
  - Confirmed class schedule and introductory athlete onboarding procedures.
  - Final pricing, punch card rules, and scholarship governance policies.
  - Approved Arkansas Community Foundation (ARCF) donation portal URL.
  - Production inquiry inbox, privacy policy, and delivery verification.
- **Asset Replacement:**
  - Supplied logo is selected and integrated in the prototype. Obtain an original vector master for production if available.
  - Replace AI concept illustration with real, rights-cleared photography of Hardwired athletes and coaches.
- **Production Architecture Decision:**
  - Evaluate WordPress theme conversion versus static hosting (GitHub Pages / Netlify / Cloudflare Pages).
  - If WordPress is chosen: port CSS design tokens, custom components, and templates to WordPress blocks/theme.
  - If static hosting is chosen: configure custom apex/subdomain DNS, TLS certificates, and static form backend (e.g. Formspree/Netlify Forms).
