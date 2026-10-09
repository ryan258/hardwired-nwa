# Organization color reference

The user supplied two screenshots on October 9, 2026 and confirmed that these are the organization's desired colors. The screenshots list slate blue/deep teal `#2C5D75` and peach/apricot `#F9B689`. Their surrounding design suggestions are reference material, not separate requirements.

The user initially reported no clear design preferences, then supplied a gym mural and asked for the site to be modeled after it. The palette remains fixed; the current design adds handwritten accents, sketched lines, and a mural-inspired training diagram. See `MURAL-DIRECTION.md`.

## Application

- Slate blue: brand mark, headings, links, dark section backgrounds, and browser theme color.
- Peach: primary buttons, the community statement strip, and accent artwork.
- Dark navy `#193442`: text on peach buttons and light surfaces.
- Warm white `#F7F4EF` and pale blue `#DCE9EF`: supporting surfaces.

Computed contrast for the supplied blue and peach pair is approximately 4.12:1, below the 4.5:1 threshold for ordinary small text. The implementation uses dark navy text on peach buttons and warm white text on blue sections. White on the supplied blue is approximately 7.17:1. Color-pair calculations alone do not establish site accessibility conformance.

The hero illustration was edited with the built-in image generation tool to use blue and peach clothing while preserving the concept composition. The new asset is `static/images/adaptive-training-concept-blue-peach.png`. The original illustration is retained as an unused earlier concept.
