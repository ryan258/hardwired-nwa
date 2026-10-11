#!/usr/bin/env python3
"""Build the single web SVG sprite from editable vector sources (stdlib only)."""
from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET
from html import escape
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent.parent
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
SUPPORT_ICONS = {
    "support-move-your-way": "Move Your Way",
    "support-scholarships-available": "Scholarships Available",
    "support-coach-who-cares": "A Coach Who Cares",
}
VALUES_ICONS = {
    "commitment-strength": "Strength",
    "commitment-community": "Community",
    "commitment-opportunity": "Opportunity",
}
DONATION_ICONS = {
    "donation-online": "Donate Online",
    "donation-check": "Donate by Check",
}


def tag(name):
    return f"{{{NS}}}{name}"


def compact(element):
    """Remove formatting and metadata, and hoist identical inherited attributes."""
    element.text = None
    element.tail = None
    for child in list(element):
        if child.tag in (tag("title"), tag("desc"), tag("metadata")):
            element.remove(child)
        else:
            compact(child)
    children = list(element)
    for attribute in ("fill", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin"):
        values = [child.get(attribute) for child in children]
        if values and values[0] is not None and all(value == values[0] for value in values):
            element.set(attribute, values[0])
            for child in children:
                del child.attrib[attribute]


sprite = ET.Element(tag("svg"))
source = ET.parse(ROOT / "assets/images/physical-skills-icons.svg").getroot()
for symbol in source.findall(tag("symbol")):
    sprite.append(deepcopy(symbol))

for name in ("access-scholarships", "access-coach-cares", "commitment-safety", "commitment-efficacy", "commitment-efficiency", "adaptive-equipment", *SUPPORT_ICONS, *VALUES_ICONS, *DONATION_ICONS):
    original = ET.parse(ROOT / f"assets/images/motifs/{name}.svg").getroot()
    symbol = ET.SubElement(sprite, tag("symbol"), {
        "id": name, "viewBox": original.attrib["viewBox"], "fill": "none",
    })
    for child in original:
        symbol.append(deepcopy(child))

# Optimize within each symbol so inherited styles cannot leak between icons.
for symbol in sprite:
    compact(symbol)
ids = [symbol.attrib["id"] for symbol in sprite]
assert len(ids) == len(set(ids)) == 24, "Expected 24 unique symbols"
assert not sprite.findall(f".//{tag('image')}"), "Only native vector artwork belongs here"
output = ROOT / "static/images/hardwired-icons.svg"
output.parent.mkdir(parents=True, exist_ok=True)
encoded = ET.tostring(sprite, encoding="unicode").replace(" />", "/>") + "\n"
output.write_text(encoded)
print(f"Built {len(ids)} symbols in {output.relative_to(ROOT)} ({len(encoded.encode())} bytes).")

# A visible two-row sheet for reviewing/sharing the skill artwork as one SVG.
sheet = ET.Element(tag("svg"), {
    "width": "800", "height": "360", "viewBox": "0 0 800 360",
    "role": "img", "aria-labelledby": "skills-sheet-title",
})
ET.SubElement(sheet, tag("title"), {"id": "skills-sheet-title"}).text = "Ten physical skill illustrations"
definitions = ET.SubElement(sheet, tag("defs"))
skills = [symbol for symbol in sprite if symbol.get("id", "").startswith("skill-")]
for i, symbol in enumerate(skills):
    definitions.append(deepcopy(symbol))
    x = (i % 5) * 160
    y = (i // 5) * 180
    ET.SubElement(sheet, tag("use"), {
        "href": f"#{symbol.get('id')}", "x": str(x + 16), "y": str(y + 4),
        "width": "128", "height": "128",
    })
    ET.SubElement(sheet, tag("text"), {
        "x": str(x + 80), "y": str(y + 154), "text-anchor": "middle",
        "font-family": "Arial, sans-serif", "font-size": "16", "font-weight": "600",
        "fill": "#2C5D75",
    }).text = symbol.get("id").removeprefix("skill-").title()
sheet_path = ROOT / "static/downloads/hardwired-nwa-skills-sheet.svg"
sheet_path.parent.mkdir(parents=True, exist_ok=True)
sheet_path.write_text(ET.tostring(sheet, encoding="unicode").replace(" />", "/>") + "\n")

# Visible sheets make each related icon group easy to review together.
def write_icon_sheet(icon_labels, title, title_id, filename):
    width = 240 * len(icon_labels)
    sheet = ET.Element(tag("svg"), {
        "width": str(width), "height": "240", "viewBox": f"0 0 {width} 240",
        "role": "img", "aria-labelledby": title_id,
    })
    ET.SubElement(sheet, tag("title"), {"id": title_id}).text = title
    definitions = ET.SubElement(sheet, tag("defs"))
    for i, symbol in enumerate(symbol for symbol in sprite if symbol.get("id") in icon_labels):
        definitions.append(deepcopy(symbol))
        ET.SubElement(sheet, tag("use"), {
            "href": f"#{symbol.get('id')}", "x": str(i * 240 + 40), "y": "24",
            "width": "160", "height": "160",
        })
        ET.SubElement(sheet, tag("text"), {
            "x": str(i * 240 + 120), "y": "212", "text-anchor": "middle",
            "font-family": "Arial, sans-serif", "font-size": "17", "font-weight": "600",
            "fill": "#2C5D75",
        }).text = icon_labels[symbol.get("id")]
    (ROOT / f"static/downloads/{filename}").write_text(ET.tostring(sheet, encoding="unicode").replace(" />", "/>") + "\n")


write_icon_sheet(SUPPORT_ICONS, "Access to Support: three additional illustrations",
                 "support-sheet-title", "hardwired-nwa-support-sheet.svg")
write_icon_sheet(VALUES_ICONS, "Our Commitments: Strength, Community and Opportunity",
                 "commitments-sheet-title", "hardwired-nwa-commitments-sheet.svg")
write_icon_sheet(DONATION_ICONS, "Donation options: Donate Online and Donate by Check",
                 "donations-sheet-title", "hardwired-nwa-donations-sheet.svg")

# Export real standalone SVGs: expand each symbol into a visible SVG root.
# Set currentColor explicitly so the skill icons keep their blue outside the site.
downloads = ROOT / "static/downloads/icons"
downloads.mkdir(parents=True, exist_ok=True)
cards = []
support_cards = []
values_cards = []
donation_cards = []
archive = ROOT / "static/downloads/hardwired-nwa-icons.zip"
with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
    for symbol in sprite:
        name = symbol.attrib["id"]
        label = name.removeprefix("skill-").removeprefix("commitment-").replace("-", " ").title()
        if name == "access-scholarships":
            label = "Supporters / Scholarships"
        elif name == "access-coach-cares":
            label = "A Coach Who Cares"
        elif name in SUPPORT_ICONS:
            label = SUPPORT_ICONS[name]
        elif name in DONATION_ICONS:
            label = DONATION_ICONS[name]
        attributes = {key: value for key, value in symbol.attrib.items() if key != "id"}
        attributes.update({"width": "128", "height": "128", "color": "#2C5D75",
                           "role": "img", "aria-labelledby": f"{name}-title"})
        standalone = ET.Element(tag("svg"), attributes)
        ET.SubElement(standalone, tag("title"), {"id": f"{name}-title"}).text = label
        for child in symbol:
            standalone.append(deepcopy(child))
        data = (ET.tostring(standalone, encoding="unicode").replace(" />", "/>") + "\n").encode()
        downloads.joinpath(f"{name}.svg").write_bytes(data)
        entry = ZipInfo(f"hardwired-nwa-icons/{name}.svg", date_time=(1980, 1, 1, 0, 0, 0))
        entry.compress_type = ZIP_DEFLATED
        entry.external_attr = 0o644 << 16
        bundle.writestr(entry, data)
        target = donation_cards if name in DONATION_ICONS else values_cards if name in VALUES_ICONS else support_cards if name in SUPPORT_ICONS else cards
        target.append(f'<li><img src="../downloads/icons/{name}.svg" width="128" height="128" alt="" aria-hidden="true">'
                      f'<h3>{escape(label)}</h3><a href="../downloads/icons/{name}.svg" download>Download SVG</a></li>')

preview = ROOT / "static/icons-preview/index.html"
preview.parent.mkdir(parents=True, exist_ok=True)
preview.write_text('''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>SVG icon downloads · Hardwired NWA</title>
<link rel="icon" href="../favicon.ico" type="image/x-icon" sizes="16x16 32x32 48x48">
<link rel="icon" href="../favicon-16x16.png" type="image/png" sizes="16x16">
<link rel="icon" href="../favicon-32x32.png" type="image/png" sizes="32x32">
<link rel="icon" href="../favicon.svg" type="image/svg+xml" sizes="any">
<link rel="apple-touch-icon" href="../apple-touch-icon.png" sizes="180x180">
<style>
*{box-sizing:border-box}body{margin:0;padding:clamp(20px,5vw,64px);background:#f7f4ef;color:#193442;font:16px/1.6 system-ui,sans-serif}
main{max-width:1120px;margin:auto}h1{color:#2c5d75;font-size:clamp(32px,5vw,56px);line-height:1.2}a{color:#2c5d75;text-underline-offset:4px}
a:focus-visible{outline:3px solid #2c5d75;outline-offset:4px}.actions{display:flex;gap:24px;flex-wrap:wrap;margin:24px 0 36px}
ul{list-style:none;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:20px}
li{text-align:center;border:1px solid #738b99;border-radius:8px;background:#fdfbf8;padding:24px}img{display:block;margin:0 auto 20px;max-width:100%;height:auto}h2{color:#2c5d75;font-size:28px;line-height:1.3;margin-top:48px}h3{font-size:20px;line-height:1.3}.trio-icons{grid-template-columns:repeat(3,minmax(0,1fr))}.pair-icons{grid-template-columns:repeat(2,minmax(0,1fr))}.trio-icons img,.pair-icons img{width:160px}
@media(max-width:1000px){ul{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media(max-width:650px){ul{grid-template-columns:repeat(2,minmax(0,1fr))}li{padding:20px 12px}}
@media(max-width:650px){.trio-icons,.pair-icons{grid-template-columns:1fr}}
@media(max-width:420px){ul{grid-template-columns:1fr}}
</style></head><body><main><h1>SVG icon downloads</h1>
<p>__ICON_COUNT__ hand-drawn vector icons with transparent backgrounds. Download one icon or the complete ZIP.</p>
<div class="actions"><a href="../downloads/hardwired-nwa-icons.zip" download>Download all __ICON_COUNT__ icons (ZIP)</a>
<a href="../downloads/hardwired-nwa-donations-sheet.svg">View new donation sheet</a>
<a href="../downloads/hardwired-nwa-commitments-sheet.svg">View commitments sheet</a>
<a href="../downloads/hardwired-nwa-support-sheet.svg">View support sheet</a>
<a href="../downloads/hardwired-nwa-skills-sheet.svg">View skills sheet</a>
<a href="../images/hardwired-icons.svg" download>Download shared sprite</a><a href="../">Back to site</a></div>
<section aria-labelledby="donation-heading"><h2 id="donation-heading">Ways to Give — two new icons</h2>
<p>Donate Online and Donate by Check in the same blue-and-peach marker style.</p><ul class="pair-icons">
'''.replace("__ICON_COUNT__", str(len(ids))) + "\n".join(donation_cards) +
"\n</ul></section><section aria-labelledby=\"values-heading\"><h2 id=\"values-heading\">Our Commitments</h2><ul class=\"trio-icons\">\n" + "\n".join(values_cards) +
"\n</ul></section><section aria-labelledby=\"support-heading\"><h2 id=\"support-heading\">Access to Support</h2><ul class=\"trio-icons\">\n" + "\n".join(support_cards) +
"\n</ul></section><section aria-labelledby=\"existing-heading\"><h2 id=\"existing-heading\">Existing collection — 16 unchanged vectors</h2><ul>\n" +
"\n".join(cards) + "\n</ul></section></main></body></html>\n")
print(f"Exported {len(ids)} standalone SVGs, ZIP archive and /icons-preview/.")
