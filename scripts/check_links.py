#!/usr/bin/env python3
"""Verify a generated build's local links and assets under a given base path."""
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.links.append(attrs[attr])

root = Path(sys.argv[1]).resolve()
prefix = sys.argv[2] if len(sys.argv) > 2 else "/hardwired-nwa/"
if not prefix.startswith("/"):
    prefix = "/" + prefix
if not prefix.endswith("/"):
    prefix = prefix + "/"

files = list(root.rglob("*.html"))
assert files, "No generated pages to check"
pages = {path: Page(path) for path in files}
errors = []

for path, page in pages.items():
    relative = path.relative_to(root).as_posix()
    route = relative.removesuffix("index.html")
    origin = "https://ryan258.github.io"
    current = origin + prefix + route
    for link in page.links:
        if link.startswith(("mailto:", "tel:", "javascript:")):
            continue
        url = urlsplit(urljoin(current, link))
        if url.netloc != "ryan258.github.io" or url.scheme not in ("http", "https"):
            continue
        if prefix != "/" and not url.path.startswith(prefix):
            errors.append(f"{relative}: escaped base path: {link}")
            continue
        rel_path = url.path.removeprefix(prefix)
        target = root / unquote(rel_path)
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"{relative}: missing {link}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"{relative}: missing anchor {link}")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Checked internal links and assets across {len(pages)} HTML pages.")
