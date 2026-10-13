"""Whole-reader source conservation and presentation contract, not usability."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch

from . import build_reader as b


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.book = False
        self.book_text, self.images, self.ids, self.links, self.tags = [], [], [], [], []

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        self.tags.append(tag)
        if tag == "article" and props.get("id") == "original-book":
            self.book = True
        if "id" in props:
            if props["id"] in self.ids:
                raise AssertionError("duplicate anchor")
            self.ids.append(props["id"])
        if tag == "a":
            self.links.append(props.get("href", ""))
        if tag == "img":
            self.images.append(props)
            if self.book:
                self.book_text.append(props.get("alt", ""))

    def handle_data(self, value):
        if self.book:
            self.book_text.append(value)

    def handle_endtag(self, tag):
        if tag == "article":
            self.book = False


def source_words(text):
    kept = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped == r"\newpage" or stripped == "$$" or stripped.startswith(("<!--", "```")):
            continue
        image = re.fullmatch(r"!\[(.+)]\(figures/[^)]+\)", stripped)
        if image:
            kept.append(image[1])
        else:
            kept.append(re.sub(r"^(?:#{1,3} |>-? ?|\s*- )", "", line))
    return re.findall(r"\w+", " ".join(kept), re.UNICODE)


def rendered_words(page):
    p = Page()
    p.feed(page)
    return re.findall(r"\w+", " ".join(p.book_text), re.UNICODE)


class WholeReader(unittest.TestCase):
    def setUp(self):
        self.raw, self.mapping = b.produce()
        self.html = self.raw.decode("utf-8")
        self.page = Page()
        self.page.feed(self.html)

    def test_every_original_word_is_retained_in_original_order(self):
        self.assertEqual(rendered_words(self.html), source_words(b.BOOK.read_text(encoding="utf-8")))

    def test_text_loss_negative_control_is_detectable(self):
        altered = self.html.replace("Let us begin with as little as possible.", "", 1)
        self.assertNotEqual(rendered_words(altered), source_words(b.BOOK.read_text(encoding="utf-8")))

    def test_all_55_sections_and_spans_are_mapped(self):
        mapping = json.loads(self.mapping)
        sections = mapping["original_sections"]
        self.assertEqual(len(sections), 55)
        self.assertEqual(sections[0]["start_line"], 1)
        self.assertEqual(sections[-1]["end_line"], len(b.BOOK.read_text(encoding="utf-8").splitlines()))
        for previous, following in zip(sections, sections[1:]):
            self.assertEqual(previous["end_line"] + 1, following["start_line"])
        self.assertTrue(all(x["rewrite"] == "NONE" and x["anchor"] in self.page.ids for x in sections))

    def test_four_original_figures_resolve_locally(self):
        self.assertEqual(len(self.page.images), 4)
        for image in self.page.images:
            self.assertTrue(image.get("alt"))
            self.assertTrue((b.HERE / image["src"]).resolve().is_file())
            self.assertTrue(image["src"].startswith("../../figures/"))

    def test_authorship_and_optional_appendix_are_separate(self):
        self.assertIn("not a released v0.9 edition", self.html)
        self.assertIn("not Mark-authored or released", self.html)
        self.assertLess(self.html.index('id="original-book"'), self.html.index('id="optional-core"'))
        self.assertIn('<details id="optional-core">', self.html)
        self.assertNotIn('<details id="optional-core" open', self.html)
        self.assertIn("Author's Note", b.BOOK.read_text(encoding="utf-8"))

    def test_local_links_and_fragment_targets_resolve(self):
        for link in self.page.links:
            if link.startswith("#"):
                self.assertIn(link[1:], self.page.ids)
            elif not link.startswith("https://"):
                target = (b.HERE / link).resolve()
                self.assertTrue(target.is_file(), str(target))
                self.assertTrue(target.is_relative_to(b.ROOT))

    def test_no_active_or_remote_assets(self):
        for tag in ("script", "iframe", "form", "video", "audio", "link"):
            self.assertNotIn(tag, self.page.tags)
        self.assertIn("@media print", self.html)
        self.assertIn("@media(max-width:680px)", self.html)
        self.assertIn('href="#book"', self.html)

    def test_original_source_drift_stops_build(self):
        original = Path.read_bytes
        def changed(path):
            raw = original(path)
            return raw + b"extra source" if path == b.BOOK else raw
        with patch.object(Path, "read_bytes", changed):
            with self.assertRaisesRegex(ValueError, "Original book changed"):
                b.produce()

    def test_figure_drift_stops_build(self):
        original = Path.read_bytes
        target = b.ROOT / "figures" / b.owner.FIGURES[0]
        def changed(path):
            return b"altered figure" if path == target else original(path)
        with patch.object(Path, "read_bytes", changed):
            with self.assertRaisesRegex(ValueError, "Original figure changed"):
                b.produce()

    def test_deterministic_output_and_manifest(self):
        self.assertEqual(self.raw, b.OUTPUT.read_bytes())
        self.assertEqual(self.mapping, b.MAP.read_bytes())

    def test_creation_and_protection_both_have_direct_routes(self):
        self.assertIn('href="#interlude-the-saturday-workshop"', self.html)
        self.assertIn('href="#a-timing-condition"', self.html)


if __name__ == "__main__":
    unittest.main()
