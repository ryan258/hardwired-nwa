# Transparent logo version

The user initially requested removal of the circular logo's white background. The original supplied file is retained at `assets/images/hardwired-nwa-logo.png`. The separate background-removed asset is `assets/images/hardwired-nwa-logo-transparent.png`, created with the built-in image generation tool. These earlier assets are retained; the updated badge below is now used on the site. The CSS white tile behind the image has also been removed.

## Final edit prompt

Background extraction edit of the supplied Hardwired NWA logo. Remove all white and near-white background, including white areas inside the circular design, wheelchair gaps, and holes inside letters, replacing those areas with genuine alpha transparency. Preserve the logo artwork exactly: curved HARDWIRED text, bottom NWA text, central HW letters, both high-fiving figures, wheelchair, barbell, circular blue arc segments and peach rays. Preserve their colors, proportions, positions, lettering, contours, and existing shading; do not redraw, recolor, simplify or redesign. Keep the complete square framing and clean smooth antialiased edges without a white halo. Transparent background PNG output.

## Updated badge — October 10, 2026

The user supplied a replacement badge and requested its use without white, following the request for an SVG. Its original PNG is retained byte-for-byte at `assets/images/hardwired-nwa-badge-original.png`.

- Site vector: `assets/images/hardwired-nwa-badge.svg`.
- Downloadable vector: `static/downloads/hardwired-nwa-logo.svg` (identical copy).
- Transparent PNG rendered from the vector: `assets/images/hardwired-nwa-badge-vector.png` (1002 × 1074).
- Square transparent PNG for browser/touch icons: `assets/images/hardwired-nwa-badge-icon.png` (180 × 180).
- Separate built-in image generation cutout: `assets/images/hardwired-nwa-badge-transparent.png`. Retained as an alternate raster asset; the website uses the vector traced directly from the original.

The SVG is a 53-path trace of the original PNG, made with VTracer 0.6.15. It contains no embedded image, background rectangle, or white fills. All white areas are transparent, including letter counters and the badge interior. Artwork colors are the original dominant blue `#2D5473` and peach `#EEAD7E`; the site's CSS palette remains unchanged. The viewBox is cropped to the artwork plus a 5-unit margin (`49 99 501 537`). Raster antialiasing was classified against the two artwork colors using a 0.45 coverage threshold. Tracing used color/cutout/spline mode, speckle filter 1, color precision 8, layer difference 1, corner threshold 60, length threshold 1, max iterations 10, splice threshold 45, and path precision 3. This is a derived trace, not an original designer-authored vector master. The supplied “501c3” artwork is retained without independently verifying nonprofit status.

The header/footer use the SVG with an accessible image name. The SVG favicon and transparent PNG icons use the same badge. PNG copies were rasterized from the SVG with ImageMagick.

### Final badge cutout prompt — built-in tool mode

Remove the white background from this exact supplied Hardwired NWA badge logo. Make all white areas truly transparent, including the white rectangular sign interior, white lower shield interior, gaps around/between the figures and wheelchair, and counters inside letters. Preserve every blue and peach shape exactly and every word: Hardwired, N·W·A, FITNESS FOR ALL, and 501c3. Do not redraw, change typography, recolor, reposition, add/remove logo elements, or invent new details. Preserve clean smooth edges. Keep original rectangular framing. Output transparent PNG.
