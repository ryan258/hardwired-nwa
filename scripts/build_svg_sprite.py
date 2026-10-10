#!/usr/bin/env python3
"""Build the single web SVG sprite from editable vector sources (stdlib only)."""
from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


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

for name in ("access-scholarships", "commitment-safety", "commitment-efficacy", "commitment-efficiency"):
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
assert len(ids) == len(set(ids)) == 14, "Expected 14 unique symbols"
assert not sprite.findall(f".//{tag('image')}"), "Only native vector artwork belongs here"
output = ROOT / "static/images/hardwired-icons.svg"
output.parent.mkdir(parents=True, exist_ok=True)
encoded = ET.tostring(sprite, encoding="unicode").replace(" />", "/>") + "\n"
output.write_text(encoded)
print(f"Built {len(ids)} symbols in {output.relative_to(ROOT)} ({len(encoded.encode())} bytes).")
