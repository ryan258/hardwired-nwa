#!/usr/bin/env python3
"""Export the editable favicon SVG to PNG, ICO and a shareable ZIP.

Authoring requires ImageMagick's `magick` command. Normal Hugo builds use the
saved static files and do not need ImageMagick or any Python image packages.
"""
from pathlib import Path
from shutil import copyfile, which
from subprocess import run
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"
SOURCE = ROOT / "assets/images/hardwired-nwa-favicon.svg"
magick = which("magick")
if not magick:
    raise SystemExit("Favicon export requires ImageMagick's magick command; the saved favicon files remain usable by Hugo.")


def convert(*arguments):
    run([magick, *map(str, arguments)], check=True)


copyfile(SOURCE, STATIC / "favicon.svg")
with TemporaryDirectory(prefix="hardwired-favicon-") as directory:
    master = Path(directory) / "master.png"
    convert("-background", "none", "-density", "768", SOURCE,
            "-resize", "512x512", "-strip", f"PNG32:{master}")
    copyfile(master, STATIC / "site-icon-512.png")
    for size, filename in ((16, "favicon-16x16.png"), (32, "favicon-32x32.png"),
                           (180, "apple-touch-icon.png")):
        convert(master, "-resize", f"{size}x{size}", "-strip", f"PNG32:{STATIC / filename}")
    convert(master, "-define", "icon:auto-resize=48,32,16", STATIC / "favicon.ico")

files = ("favicon.svg", "favicon.ico", "favicon-16x16.png", "favicon-32x32.png",
         "apple-touch-icon.png", "site-icon-512.png")
archive = STATIC / "downloads/hardwired-nwa-favicon-kit.zip"
archive.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
    for filename in files:
        entry = ZipInfo(f"hardwired-nwa-favicon/{filename}", date_time=(1980, 1, 1, 0, 0, 0))
        entry.compress_type = ZIP_DEFLATED
        entry.external_attr = 0o644 << 16
        bundle.writestr(entry, (STATIC / filename).read_bytes())
print("Built SVG, 16/32px PNGs, 16/32/48px ICO, 180px touch icon, 512px site icon and favicon ZIP.")
