# Donation-card SVG icons

Two native SVG illustrations supply the Donate Online and Donate by Check cards in the user's reference. They extend the existing blue-and-peach marker style, preserving all 22 previous vectors and the favicon assets.

| Card | Symbol ID | Editable source | Artwork |
| --- | --- | --- | --- |
| Donate Online | `donation-online` | `assets/images/motifs/donation-online.svg` | Browser window, peach heart and blue cursor |
| Donate by Check | `donation-check` | `assets/images/motifs/donation-check.svg` | Paper check, peach signature, small heart and pen |

Each drawing uses the exact colors `#2C5D75` and `#F9B689`, rounded strokes, a transparent 128-unit canvas, and a longest geometry extent of 100 units before stroke thickness. Online giving has an open frame corner around the cursor to avoid intersecting outlines. Neither SVG contains embedded raster images or external dependencies.

## Downloads and review

- `/icons-preview/#donation-heading`: the new pair, individual download links and the complete 24-icon ZIP.
- `/downloads/icons/donation-online.svg` and `/downloads/icons/donation-check.svg`: self-contained standalone files.
- `/downloads/hardwired-nwa-donations-sheet.svg`: visible two-icon sheet with internal symbols and system-font labels.
- `/images/hardwired-icons.svg`: shared web sprite containing both new IDs.

Regenerate using `python3 scripts/build_svg_sprite.py`. The generator supports review sheets of different group lengths and keeps existing definitions and exports intact. With equivalent card text nearby, render icons as decorative; standalone downloads have descriptive titles.

The original 22 sources, symbol definitions, individual files and review sheets passed preservation comparisons. New SVG structure/palette checks, 24-entry ZIP integrity, deterministic regeneration, the base-path Hugo build, thirteen-page link checks and 1440/320px gallery checks passed. The screenshot's donation copy and mailing-address placeholder are context for the icons; site payment and contact configuration are unchanged.
