# Targeted prototype checks — October 9, 2026

## Passed

- Hugo 0.166.0 extended builds the complete prototype.
- All eight charter routes return HTTP 200.
- Generated HTML has one main heading per page, English document language, and noindex metadata.
- Internal page links, local assets, and fragment anchors resolve. The Hugo development server’s virtual live-reload script is excluded from disk-only asset checks.
- Browser JavaScript passes the Node syntax check.
- Home renders its illustration and intended fonts at desktop width. Google Fonts loaded during this check.
- Desktop Home and Support fit a 1440px viewport.
- Home and FAQ fit a 390px mobile viewport.
- Home and Support fit a 320px mobile viewport. A small-screen headline adjustment fixed a four-pixel overflow observed on Home during review.
- The menu opens, exposes navigation, and closes with Escape.
- Six punch cards produce $450 and 60 visits; six membership months produce $810.
- Donation explanation opens and closes; keyboard Escape closes it and returns focus to the trigger.
- Native FAQ opens using Enter while its summary has keyboard focus.
- A sample inquiry produces a visible local preview. Markup-like input is displayed as text. The preview handler has no delivery endpoint, storage calls, or persistence.
- No browser console errors or warnings were reported on the checked Support page.

## Limits

These are targeted implementation and browser checks. They do not establish WCAG conformance, screen-reader acceptance, physical facility access, payment configuration, contact delivery, approved program information, or production readiness. Real athlete, coach, facility, and partner representations require organization approval.

The illustration is AI-generated concept art and labeled accordingly. The typography uses Google Fonts; fallback fonts are provided for unavailable network fonts.

## Supplied palette update

The user supplied slate blue `#2C5D75` and peach `#F9B689`. The shared stylesheet, browser theme, favicon, buttons, accent surfaces, and hero illustration now use that palette. The Hugo build passed; browser computed styles confirmed the exact blue/peach values and navy text on peach buttons. The revised home page fits 1440px desktop and 390px mobile viewports, and its revised illustration loads. The earlier desktop screenshot records the initial palette, not the current design. See `PALETTE.md` for color roles and contrast calculations.

## Mural direction update

The shared design now uses handwritten accents, sketched edges, and a training-wall section on Home and Adaptive CrossFit. Hugo build and targeted internal link/asset/fragment checks passed, including the scaling anchor. Patrick Hand loaded in the browser. The revised Home has no horizontal overflow at 1440px desktop, 390px mobile, or 320px mobile. The Adaptive CrossFit page also fits 320px, with one main heading and a working scaling anchor. The five pyramid labels are accessible HTML text, with the decorative SVG excluded from the accessibility tree.

## GitHub Pages & subpath verification

On October 9, 2026, the prototype was deployed live to GitHub Pages at <https://ryan258.github.io/hardwired-nwa/>.

- **Automated CI/CD:** GitHub Actions workflow `.github/workflows/deploy.yml` executed successfully (Hugo 0.166.0 extended build, link verification, artifact packaging, and Pages deployment).
- **Subpath Link & Asset Check:** `scripts/check_links.py` executed quietly across all 9 generated HTML pages under baseURL `/hardwired-nwa/` and passed with 0 errors (0 escaped base paths, 0 missing assets, 0 broken fragment anchors).
- **Live Endpoint Verification:** Verified HTTP/2 200 responses on live endpoints:
  - Home: `https://ryan258.github.io/hardwired-nwa/`
  - Support: `https://ryan258.github.io/hardwired-nwa/support/`
  - About: `https://ryan258.github.io/hardwired-nwa/about/`
  - Adaptive CrossFit: `https://ryan258.github.io/hardwired-nwa/adaptive-crossfit/`

## Supplied logo integration

The user-selected PNG logo replaces the temporary header/footer mark and browser icon. The original source in `assets/images/hardwired-nwa-logo.png` is byte-identical to the supplied attachment. Hugo generates 160px/320px web versions, a 64px favicon, and a 180px Apple touch icon. All nine generated HTML pages contain both logo placements with the accessible home-link name and resolving icon/image assets. The build passed. Browser checks confirmed loaded header/footer logos, square proportions, and no Home overflow at 1440px desktop or 320px mobile. The original colors, composition, and white background are preserved.

## Logo background removal

A separate RGBA transparent logo now replaces the white-background version on the website. The original supplied source remains unchanged. The Hugo build passed; the transparent source and derived web copies retain alpha at their corners. Browser inspection confirmed the header uses the new asset and has no CSS background tile. The rendered Home was visually checked against its warm-white page background. See `LOGO-EDIT.md` for the image editing prompt and asset paths.

## Replacement badge SVG — October 10, 2026

The latest supplied badge now replaces the earlier circular logo. The retained original is byte-identical to the latest attachment. Both SVG copies match and contain 53 vector paths, two artwork fills, no white fill, no background rectangle, and no embedded raster image. The SVG was rendered and visually inspected for the supplied lettering, figures, and wheelchair; transparent PNG render/icon copies have alpha from 0 to 255 and transparent corners. The Hugo build passed, and all internal links/assets resolved across nine generated HTML pages. Desktop Home browser inspection at 1440px confirmed loaded header/footer SVGs, transparent CSS backgrounds, and no horizontal overflow. A 320px mobile emulation also confirmed loaded logos and no horizontal overflow. The existing local preview needed a restart after it cached a missing icon during asset creation; the restarted preview serves the complete site successfully. These are targeted logo/build/render checks, not a new full accessibility audit.

## Physical skill motifs & SVG icons integration — October 10, 2026

The ten general physical skills pictured on the gym whiteboard mural (Cardio, Stamina, Strength, Flexibility, Power, Speed, Coordination, Agility, Balance, Accuracy) are now integrated as scalable SVG vector symbols and responsive cards on the website.

- **Vector Sprite Pipeline:** Created `layouts/partials/svg-skills-sprite.html` containing clean `<symbol>` elements for each skill using `stroke="currentColor"` and `fill="none"` with a 24×24 viewBox. Embedded into `layouts/_default/baseof.html` for zero-request, universal `<use href="#skill-...">` rendering across all pages.
- **Static & Downloadable Assets:** Exported vector assets to `assets/images/physical-skills-icons.svg`, `static/images/physical-skills-icons.svg`, and `static/downloads/physical-skills-icons.svg`.
- **UI Integration:** Extended `layouts/partials/training-wall.html` with an accessible `<ol class="skills-grid">` featuring Patrick Hand numbering, displayed subtitles, and aria-hidden SVG icons. Rendered on both Home and Adaptive CrossFit pages.
- **Styling:** Added responsive grid styles to `assets/css/site.css` (5 columns on desktop, 3 columns on tablet, 2 columns on mobile) with tactile card border radius variations and hover micro-interactions (badge background transition to `--peach` `#F9B689`, card elevation).
- **Preview & Verification:**
  - `hugo --minify` builds all 10 HTML pages cleanly in ~25-50ms.
  - `scripts/check_links.py ./public /` passed quietly with 0 broken links or missing assets across all 10 generated pages.
  - Subpath build `hugo --baseURL "https://ryan258.github.io/hardwired-nwa/" --minify` and `scripts/check_links.py ./public /hardwired-nwa/` passed with 0 errors.
  - Dedicated standalone preview at `/motifs-preview/` (`static/motifs-preview/index.html`) serves both raster sprite sheet downloads and vector SVG download options.


## SVG consolidation and target correction — October 10, 2026

The earlier inline sprite and separate static/download copies described above have been superseded by `static/images/hardwired-icons.svg`. The shared file contains all 14 icon symbols; the efficacy target now has concentric circular arcs with matching arrow gaps. The base-path build and eleven-page link check passed, all 30 external symbol references resolved, regeneration was deterministic, and Home/commitments previews rendered at desktop and 320px without horizontal overflow. See `docs/SVG-SPRITE.md` for the current pipeline and evidence.
