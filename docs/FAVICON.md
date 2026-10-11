# Hardwired NWA favicon

The favicon adapts the newer supplied wordmark reference: a blue hexagon with a white barbell. It is drawn directly as native SVG geometry, simplified for small browser tabs. The mark uses the site's blue `#2C5D75` and white `#FFFFFF`; the surrounding square is transparent. The existing full badge logo and 22-icon illustration collection are unchanged.

## Source and exports

- Editable source: `assets/images/hardwired-nwa-favicon.svg` (64-unit viewBox).
- `static/favicon.svg`: identical standalone SVG copy.
- `static/favicon-16x16.png` and `static/favicon-32x32.png`: transparent RGBA PNGs.
- `static/favicon.ico`: contains 16, 32 and 48px images.
- `static/apple-touch-icon.png`: transparent 180px PNG.
- `static/site-icon-512.png`: transparent 512px PNG for reuse, including the planned WordPress handoff.
- `static/downloads/hardwired-nwa-favicon-kit.zip`: all six exported files.
- `/favicon-preview/`: actual-size 16, 32 and 64px samples on light and dark backgrounds, plus downloads.

Rebuild after editing the source:

```sh
python3 scripts/build_favicons.py
```

Exporting requires ImageMagick's `magick` command. The script renders the SVG at high resolution, downsamples the PNGs, builds a multi-size ICO, and writes a deterministic ZIP. Normal Hugo builds use the saved exports and do not require ImageMagick or Python image packages.

## Site integration

`layouts/partials/favicon.html` declares the SVG, PNG, ICO and touch-icon links in the Hugo base layout. All paths use `relURL` to preserve the GitHub Pages project subpath. The standalone icon, commitment, motif and favicon preview pages have equivalent relative links. `scripts/build_svg_sprite.py` preserves these links when regenerating the icon gallery.

## Targeted checks

The exported PNG sizes and RGBA transparency, the ICO's three resolutions, native SVG structure, matching ZIP entries and deterministic regeneration were checked locally. All 13 generated HTML pages declare the favicon set, and the GitHub Pages subpath build and link/asset checks passed. Browser checks confirmed all favicon resources return their expected image types and the preview images render on light/dark backgrounds without overflow at 1440 and 320 CSS pixels. The existing badge, 22 vectors, icon ZIP and staged Git index are preserved. These are local asset/build/render checks.
