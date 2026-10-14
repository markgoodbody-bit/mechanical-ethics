"""Deterministic path-preserving original reader ZIP; no browser or publication."""
import hashlib
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import zipfile
from . import build_reader as reader

ENTRY = "research/full_review/author_review.html"
OUTPUT = reader.ROOT / "output" / "me-original-reader.zip"

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        for key in ("href", "src"):
            if key in props:
                self.targets.append(props[key])

def archive_bytes():
    page, mapping = reader.produce()
    files = {ENTRY: page, "research/full_review/CHAPTER_MAP.json": mapping}
    pending = [ENTRY]
    seen = set()
    while pending:
        name = pending.pop()
        if name in seen:
            continue
        seen.add(name)
        raw = files[name]
        if name.endswith(".html"):
            parser = References(); parser.feed(raw.decode("utf-8")); targets = parser.targets
        elif name.endswith(".md"):
            targets = re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", raw.decode("utf-8"))
        else:
            targets = []
        for href in targets:
            url = urlsplit(href)
            if url.scheme in ("https", "http") or not url.path:
                continue
            if url.scheme or url.netloc:
                raise ValueError("Unexpected archive reference: " + href)
            target = (reader.ROOT / name).parent / unquote(url.path)
            target = target.resolve()
            if not target.is_relative_to(reader.ROOT.resolve()) or not target.is_file():
                raise ValueError("Missing/outside archive dependency: " + href + " from " + name)
            relative = target.relative_to(reader.ROOT.resolve()).as_posix()
            if relative not in files:
                files[relative] = target.read_bytes()
                pending.append(relative)
    manifest = {"status": "ORIGINAL_BOOK_REVIEW_ONLY_NOT_RELEASED",
                "entry": ENTRY, "book_sha256": reader.owner.BOOK_SHA256,
                "browser_layout_verification": "NOT_RUN",
                "files": {name: hashlib.sha256(raw).hexdigest() for name, raw in sorted(files.items())}}
    files["READ_FIRST.txt"] = ("Extract the whole ZIP, keeping folders. Open " + ENTRY +
        " in a separately permitted reader. Full released v0.8 text and four figures; optional core is AI-proposed. "
        "No new released v0.9. No browser/keyboard/layout verdict is implied.\n").encode("utf-8")
    files["MANIFEST.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, raw in sorted(files.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, raw)
    return output.getvalue(), manifest

def main():
    raw, manifest = archive_bytes()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(raw)
    print(json.dumps({"output": str(OUTPUT), "entry": ENTRY,
                      "sha256": hashlib.sha256(raw).hexdigest(), "files": len(manifest["files"]),
                      "browser": "NOT_RUN", "publication": "NONE"}, sort_keys=True))

if __name__ == "__main__":
    main()
