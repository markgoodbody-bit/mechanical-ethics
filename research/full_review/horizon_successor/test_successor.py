"""Human v0.9 editorial successor: source/custody QA only, not reader usability."""
from html.parser import HTMLParser
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

from research.full_review import build_reader as original
from research.full_review.horizon_successor import build as successor


class Reader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.images = []
        self.ids = []
        self.links = []
        self.tags = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append(tag)
        if "id" in data:
            self.ids.append(data["id"])
        if tag == "img":
            self.images.append(data)
        if tag == "a":
            self.links.append(data.get("href", ""))


class PositiveHumanSuccessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw, cls.receipt = successor.produce()
        cls.text = cls.raw.decode("utf-8")
        cls.base = original.produce()[0].decode("utf-8")
        cls.page = Reader()
        cls.page.feed(cls.text)

    def test_original_html_recovers_exactly_after_subtracting_only_labelled_proposal(self):
        # No claim that the proposed bridge is part of the original authorial text.
        restored, count = re.subn(r'<aside id="horizon-successor".*?</aside>\n',
                                  "", self.text, count=1, flags=re.S)
        self.assertEqual(count, 1)
        restored = restored.replace(successor.NEW_LABEL, successor.PR67_LABEL)
        restored = restored.replace(successor.NEW_ROUTE, successor.OLD_ROUTE)
        restored = restored.replace(
            "Full ME v0.8 text retained; a clearly marked AI-assisted Part VI bridge is proposed "
            "before the original Conclusion, and the separate compact-core appendix remains optional.",
            "Full ME v0.8 text retained, plus one separately attributed optional compact-core appendix.")
        restored = restored.replace(
            "Mark’s original words and four figures are preserved, with the unapproved bridge "
            "clearly bounded and attributed; the optional appendix remains a Codex proposal.",
            "The original book below is Mark’s released work; the appendix is a Codex proposal for his editorial decision.")
        self.assertEqual(restored, self.base)

    def test_original_55_headings_and_figures_still_present(self):
        self.assertEqual(self.receipt["original_chapter_count"], 55)
        original_map = original.produce()[1].decode("utf-8")
        self.assertIn('"original_sections"', original_map)
        self.assertEqual(len(self.page.images), 4)
        for image in self.page.images:
            self.assertTrue(image.get("alt"))
            self.assertTrue((successor.OUTPUT.parent / image["src"]).resolve().is_file())
        self.assertEqual(len(self.page.ids), len(set(self.page.ids)))
        self.assertIn("conclusion", self.page.ids)
        self.assertIn("original-book", self.page.ids)

    def test_proposed_horizon_placed_after_build_before_original_conclusion(self):
        page = self.text
        self.assertLess(page.index('id="what-this-can-build"'), page.index('id="horizon-successor"'))
        self.assertLess(page.index('id="horizon-successor"'), page.index('id="conclusion"'))
        self.assertLess(page.index('id="conclusion"'), page.index('id="optional-core"'))
        self.assertIn('href="#horizon-successor"', page)
        self.assertEqual(page.count('id="horizon-successor"'), 1)

    def test_authorial_and_release_distinctions_are_explicit(self):
        self.assertIn("NOT MARK-AUTHORED · NOT RELEASED", self.text)
        self.assertIn('href="horizon_successor/BRIDGE.md"', self.text)
        self.assertIn('aria-label="Unapproved AI-assisted Part VI editorial candidate"',self.text)
        self.assertEqual(self.receipt["human_acceptance"], "UNRUN")
        self.assertEqual(self.receipt["browser_visual_qa"], "UNRUN")
        self.assertFalse(self.receipt["released_source_changed"])
        self.assertTrue(self.receipt["original_reader_unmodified"])

    def test_power_privacy_and_positive_construction_both_visible(self):
        for required in ("The camera that could settle everything", "Powerful helpers, unfinished relationships",
                         "A stepping stone at the workshop", "The future remains answerable",
                         "refusal", "permission", "maintenance"):
            self.assertIn(required.casefold(),self.text.casefold())
        bridge = successor.SOURCE.read_text(encoding="utf-8")
        self.assertNotIn("## Mandatory",bridge)
        self.assertIn("This scene is invented",bridge)
        self.assertIn("not blueprints",bridge)

    def test_all_relative_links_and_anchor_routes_resolve(self):
        root = original.ROOT.resolve()
        for link in self.page.links:
            if link.startswith("#"):
                self.assertIn(link[1:], self.page.ids)
            elif not link.startswith("https://"):
                target = (successor.OUTPUT.parent / link).resolve()
                self.assertTrue(target.is_relative_to(root), link)
                self.assertTrue(target.is_file(), link)

    def test_no_active_scripts_forms_or_remote_resources(self):
        for tag in ("script","iframe","form","video","audio","link"):
            self.assertNotIn(tag,self.page.tags)
        self.assertIn("@media print", self.text)
        self.assertIn("@media(max-width:680px)", self.text)

    def test_rejects_unsupported_source_markup_and_missing_section(self):
        good = successor.SOURCE.read_bytes()
        with self.assertRaisesRegex(ValueError, "Unsupported proposal block"):
            successor.proposal_html(good.replace(b"A life is not just",b"<script>A life is not just",1))
        with self.assertRaisesRegex(ValueError, "Essential ethical tension"):
            successor.proposal_html(good.replace(b"## The camera that could settle everything",b"## The edited camera section"))

    def test_deterministic_source_generated_artifact(self):
        self.assertEqual(self.raw, successor.OUTPUT.read_bytes())
        self.assertRegex(self.receipt["proposed_bridge_sha256"],r"^[a-f0-9]{64}$")
        self.assertEqual(self.receipt["proposed_section_count"], 6)


if __name__ == "__main__":
    unittest.main()
