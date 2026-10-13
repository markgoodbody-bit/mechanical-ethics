"""Source custody, HTML semantics and deliberate drift detection. Standard library."""
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch
import build_review as r


class ReaderHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.tags = []
        self.headings = []
        self._headlevel = None
        self._text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                raise AssertionError("duplicate id: " + attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href"))
        if tag in ("h1", "h2", "h3"):
            self._headlevel = tag

    def handle_data(self, data):
        if self._headlevel:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == self._headlevel:
            self.headings.append((tag, "".join(self._text).strip()))
            self._headlevel = None
            self._text.clear()


class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.source = r.SOURCE.read_text(encoding="utf-8")
        self.page = r.OUTPUT.read_text(encoding="utf-8")
        self.parsed = ReaderHTML()
        self.parsed.feed(self.page)

    def test_exact_source_identity_and_same_bytes_on_rebuild(self):
        self.assertEqual(r.blob_id(r.SOURCE.read_bytes()), r.EXPECTED_SOURCE_BLOB)
        self.assertEqual(r.produce(), r.OUTPUT.read_bytes())

    def test_frozen_source_edit_is_rejected_even_if_html_still_exists(self):
        with tempfile.TemporaryDirectory() as d:
            changed = Path(d) / "changed.md"
            changed.write_text(self.source + "\nUnauthorized extra sentence.\n", encoding="utf-8")
            with patch.object(r, "SOURCE", changed):
                with self.assertRaisesRegex(ValueError, "source text changed"):
                    r.produce()

    def test_no_source_section_or_paragraph_is_omitted(self):
        expected_article, expected_nav = r.article_and_toc(self.source)
        self.assertIn(expected_article, self.page)
        self.assertIn("<ol>" + expected_nav + "</ol>", self.page)
        self.assertEqual(expected_article.count("<h3"), 10)
        self.assertEqual(expected_article.count("<p>"), 52)
        self.assertEqual(expected_article.count("<li>"), 7)

    def test_heading_order_and_functional_keyboard_skip(self):
        self.assertIn("main", self.parsed.ids)
        h3 = [(tag, title) for tag, title in self.parsed.headings if tag == "h3"]
        self.assertEqual(len(h3), 10)
        self.assertIn(("h3", "1. More than a repaired bicycle"), h3)
        self.assertIn(("h3", "Source and status note for this optional review"), h3)
        self.assertIn("#main", self.parsed.links)
        for href in self.parsed.links:
            if href and href.startswith("#"):
                self.assertIn(href[1:], self.parsed.ids, href)

    def test_no_active_resources_and_status_is_evident(self):
        for forbidden in ("script", "form", "iframe", "video", "audio", "img"):
            self.assertNotIn(forbidden, self.parsed.tags)
        self.assertIn("RESEARCH ONLY · NOT RELEASED · NOT A REPLACEMENT", self.page)
        self.assertIn("HUMAN EDITORIAL GATE: MARK", self.page)
        self.assertIn("e2ef746e931161cb70ac46a4eaa122442134e86b", self.page)
        self.assertIn("four figures", self.page)
        self.assertNotIn("https://fonts.", self.page)
        self.assertNotIn("analytics", self.page.lower())
        self.assertIn("@media print", self.page)
        self.assertIn("@media(max-width:720px)", self.page)

    def test_protective_clock_and_constructive_outcome_readable(self):
        for phrase in (
            "The repaired bicycle matters",
            "Learning takes time.",
            "A correct entry in a database does not make the room safe",
            "That is private",
        ):
            self.assertIn(phrase, self.page)

    def test_navigation_target_ids_and_source_blob(self):
        self.assertEqual(self.page.count("source-git-blob"), 1)
        self.assertIn(f'content="{r.EXPECTED_SOURCE_BLOB}"', self.page)
        for anchor in ("1-more-than-a-repaired-bicycle",
                       "2-the-future-does-not-wait-for-our-account-of-it",
                       "an-unfinished-ending"):
            self.assertIn(anchor, self.parsed.ids)


if __name__ == "__main__":
    unittest.main()
