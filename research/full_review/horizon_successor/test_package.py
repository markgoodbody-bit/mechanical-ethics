"""Integrated offline author-review acceptance: real archive bytes, not HTML only."""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
from io import BytesIO
import json
from pathlib import PurePosixPath
import unittest
from unittest.mock import patch
from zipfile import ZipFile

from research.full_review.horizon_successor import package as p


class ReadingPackage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data, cls.receipt = p.archive_bytes()
        cls.z = ZipFile(BytesIO(cls.data))
        cls.files = {name: cls.z.read(name) for name in cls.z.namelist()}
        cls.manifest = json.loads(cls.files[p.MANIFEST])

    @classmethod
    def tearDownClass(cls):
        cls.z.close()

    def test_open_one_reading_route_and_all_four_images_are_actually_in_zip(self):
        self.assertIn(p.ENTRY, self.files)
        self.assertIn(p.INSTRUCTIONS, self.files)
        opening = self.files[p.ENTRY].decode("utf-8")
        self.assertIn("research/full_review/positive_successor.html", opening)
        self.assertIn("unzip the entire archive", opening.lower())
        self.assertIn("NOT A RELEASED v0.9 EDITION", opening)
        for name in p.owner.FIGURES:
            self.assertIn("figures/" + name, self.files)
            self.assertTrue(self.files["figures/" + name].startswith(bytes([0x89, 0x50, 0x4E, 0x47])))
        self.assertEqual(self.manifest["reader_open_path"], p.ENTRY)
        self.assertEqual(self.manifest["whole_book_path"], "research/full_review/positive_successor.html")
        self.assertIn("MECHANICAL_ETHICS.pdf", self.files)

    def test_all_manifest_members_and_bytes_checked(self):
        listed = self.manifest["files"]
        self.assertEqual(set(self.files), {x["path"] for x in listed} | {p.MANIFEST})
        self.assertEqual(len(listed), len({x["path"] for x in listed}))
        for entry in listed:
            raw = self.files[entry["path"]]
            self.assertEqual(len(raw),entry["size"],entry["path"])
            self.assertEqual(p.digest(raw),entry["sha256"],entry["path"])
        self.assertEqual(self.manifest["released_markdown_sha256"],p.owner.BOOK_SHA256)
        self.assertEqual(p.digest(self.files["MECHANICAL_ETHICS.md"]),p.owner.BOOK_SHA256)
        self.assertTrue(self.files["MECHANICAL_ETHICS.pdf"].startswith(b"%PDF"))

    def test_all_local_html_targets_resolve_inside_zip(self):
        files={k:v for k,v in self.files.items() if k != p.MANIFEST}
        self.assertGreaterEqual(p.check_html_references(files),30)
        self.assertEqual(self.manifest["html_local_links_checked"],p.check_html_references(files))
        self.assertNotIn(b"<script",self.files[p.ENTRY])

    def test_negative_missing_figure_is_rejected_not_silent(self):
        files={k:v for k,v in self.files.items() if k != p.MANIFEST}
        files.pop("figures/" + p.owner.FIGURES[0])
        with self.assertRaisesRegex(ValueError,"Offline link not included"):
            p.check_html_references(files)

    def test_cannot_sneak_absent_content_as_a_resolved_page(self):
        files={k:v for k,v in self.files.items() if k != p.MANIFEST}
        files[p.ENTRY] = files[p.ENTRY].replace(
            b"research/full_review/positive_successor.html",b"missing.html")
        with self.assertRaisesRegex(ValueError,"Offline link not included"):
            p.check_html_references(files)

    def test_nontraversing_fixed_zip_paths(self):
        for name in self.files:
            path=PurePosixPath(name)
            self.assertFalse(path.is_absolute(), name)
            self.assertNotIn("..",path.parts)
            self.assertEqual(path.as_posix(),name)
        self.assertEqual(self.z.testzip(),None)

    def test_both_complete_editorial_books_and_choice_routes(self):
        self.assertIn("research/full_review/positive_successor.html", self.files)
        self.assertIn("research/full_review/positive_successor_concise.html", self.files)
        self.assertIn("research/full_review/horizon_successor/A_B_DECISION.md", self.files)
        self.assertIn("research/full_review/horizon_successor/BRIDGE_CONCISE.md", self.files)
        opening=self.files[p.ENTRY].decode("utf-8")
        self.assertIn("A, full proposal",opening)
        self.assertIn("B, concise proposal",opening)
        full=self.files["research/full_review/positive_successor.html"].decode("utf-8")
        short=self.files["research/full_review/positive_successor_concise.html"].decode("utf-8")
        import re
        a=re.findall(r'<aside id="horizon-successor".*?</aside>\\n',full,re.S)
        b=re.findall(r'<aside id="horizon-successor".*?</aside>\\n',short,re.S)
        self.assertEqual((len(a),len(b)),(1,1))
        self.assertEqual(short.replace(b[0],a[0],1),full)
        self.assertEqual(self.manifest["full_book_path"],"research/full_review/positive_successor.html")
        self.assertEqual(self.manifest["concise_book_path"],"research/full_review/positive_successor_concise.html")
        self.assertEqual(self.manifest["concise_bridge_sha256"],
                         p.digest(self.files["research/full_review/horizon_successor/BRIDGE_CONCISE.md"]))

    def test_actual_upload_folder_matches_verified_archive_bytes(self):
        # The GitHub artifact zips this folder once. Test its actual staged
        # bytes, not just a separate locally generated ZIP.
        self.assertTrue(p.STAGING.is_dir(), "run package --stage first")
        staged = {
            file.relative_to(p.STAGING).as_posix(): file.read_bytes()
            for file in p.STAGING.rglob("*") if file.is_file()
        }
        self.assertEqual(set(staged), set(self.files))
        for name, raw in self.files.items():
            self.assertEqual(staged[name], raw, name)

    def test_source_package_deterministic_and_current(self):
        self.assertEqual(p.archive_bytes()[0],self.data)
        self.assertEqual(self.data,p.OUTPUT.read_bytes())
        self.assertEqual(self.receipt["status"],"SOURCE_ONLY_OFFLINE_DRAFT")
        self.assertEqual(self.receipt["zip_sha256"],hashlib.sha256(self.data).hexdigest())

    def test_source_and_ai_attribution_both_remain_in_complete_reader(self):
        book = self.files["research/full_review/positive_successor.html"].decode("utf-8")
        original = self.files["research/full_review/author_review.html"].decode("utf-8")
        self.assertIn("END OF AI-ASSISTED PROPOSAL",book)
        self.assertIn("AI-assisted proposal",book)
        self.assertIn("Mark’s original words",book)
        self.assertNotIn("id=\"horizon-successor\"",original)
        self.assertIn("Original book source:",original)
        self.assertIn("research/full_review/horizon_successor/BRIDGE.md",self.files[p.MANIFEST].decode())
        self.assertIn("research/full_review/horizon_successor/READER_DECISION.md",self.files[p.MANIFEST].decode())
        self.assertEqual(self.manifest["evidence_limit"],"SOURCE_INTEGRITY_ONLY_NOT_BROWSER_OR_HUMAN_VALIDATION")


if __name__ == "__main__":
    unittest.main()
