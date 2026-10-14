"""One A/B whole-reader acceptance, not a human or browser validation."""
from __future__ import annotations
import hashlib
from html.parser import HTMLParser
import re
import unittest

from research.full_review.horizon_successor import build, concise
from research.full_review import build_reader as original


def words(s):
    return len(s.split())


class WholeBookOptions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full, cls.full_receipt = build.produce()
        cls.short, cls.receipt = concise.produce()
        cls.f = cls.full.decode("utf-8")
        cls.s = cls.short.decode("utf-8")

    def test_previous_full_option_is_byte_for_byte_preserved(self):
        self.assertEqual(self.full, build.OUTPUT.read_bytes())
        self.assertEqual(hashlib.sha256(self.full).hexdigest(), self.receipt["full_candidate_sha256"])
        self.assertEqual(self.receipt["full_source_sha256"], hashlib.sha256(build.SOURCE.read_bytes()).hexdigest())

    def test_alternative_only_replaces_one_ai_aside(self):
        af = concise.ASIDE.findall(self.f)
        ab = concise.ASIDE.findall(self.s)
        self.assertEqual((len(af), len(ab)), (1, 1))
        self.assertEqual(self.s.replace(ab[0], af[0], 1), self.f)
        self.assertEqual(self.s.count('<h1 id="conclusion">Conclusion</h1>'), 1)
        self.assertLess(self.s.index('id="what-this-can-build"'), self.s.index('id="horizon-successor"'))
        self.assertLess(self.s.index('id="horizon-successor"'), self.s.index('id="conclusion"'))

    def test_three_substantive_scenes_verbatim(self):
        kept = concise.assert_kept_scenes_verbatim()
        self.assertEqual(len(kept), 3)
        self.assertIn("independently held, trustworthy earlier digest", self.s)
        for key in ("Elena, Luca and Samir", "without being punished for declining",
                    "The camera that could settle everything"):
            self.assertIn(key, self.s)
        self.assertNotIn("AI-assisted proposal — The future remains answerable", self.s)
        self.assertNotIn("AI-assisted proposal — From a saved route to a newly built world", self.s)

    def test_four_attributed_sections_and_visible_end(self):
        aside = concise.ASIDE.findall(self.s)[0]
        headings = re.findall(r'<h2 id="horizon-[^"]+">AI-assisted proposal — ([^<]+)</h2>', aside)
        self.assertEqual(tuple(headings), concise.EXPECTED_HEADINGS)
        self.assertEqual(len(headings), 4)
        self.assertIn('aria-label="Four AI-assisted proposed sections"', aside)
        self.assertIn("NOT MARK-AUTHORED · NOT RELEASED · CONCISE OPTION", aside)
        self.assertEqual(aside.count('class="status"'), 1)
        self.assertIn("END OF AI-ASSISTED PROPOSAL — MARK’S ORIGINAL CONCLUSION FOLLOWS", aside)
        self.assertIn('href="horizon_successor/BRIDGE_CONCISE.md"', aside)
        self.assertIn('href="horizon_successor/A_B_DECISION.md"', aside)

    def test_original_release_source_and_artwork_are_unchanged(self):
        self.assertEqual(self.receipt["original_reader_unmodified"], True)
        self.assertEqual(self.receipt["released_source_changed"], False)
        self.assertEqual(len(re.findall(r"<img\b", self.s)), 4)
        self.assertEqual(self.receipt["human_acceptance"], "UNRUN")
        self.assertEqual(self.receipt["browser_visual_qa"], "UNRUN")
        self.assertEqual(hashlib.sha256(original.ROOT.joinpath("MECHANICAL_ETHICS.md").read_bytes()).hexdigest(),
                         build.owner.BOOK_SHA256)

    def test_side_by_side_word_counts_and_determinism(self):
        a = words(build.SOURCE.read_text(encoding="utf-8"))
        b = words(concise.SOURCE.read_text(encoding="utf-8"))
        self.assertGreater(a, b)
        self.assertLess(b / a, .7)
        self.assertGreater(b / a, .45)
        self.assertEqual(self.short, concise.OUTPUT.read_bytes())
        self.assertEqual(hashlib.sha256(concise.SOURCE.read_bytes()).hexdigest(), self.receipt["concise_source_sha256"])

    def test_negative_controls_reject_dropped_scene_or_active_markup(self):
        source = concise.SOURCE.read_bytes()
        with self.assertRaisesRegex(ValueError, "headings or order changed"):
            concise.chapters(source.replace(b"## The camera that could settle everything", b"## The missing camera"))
        with self.assertRaisesRegex(ValueError, "Unsupported concise proposal block"):
            concise.chapters(source.replace(b"## A stepping stone at the workshop", b"<script>alert(1)</script>\n\n## A stepping stone at the workshop"))


if __name__ == "__main__":
    unittest.main()
