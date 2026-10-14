import hashlib
import io
import json
import unittest
from unittest.mock import patch
import zipfile
from . import portable as p

class PortableReader(unittest.TestCase):
    def test_archive_custody_and_all_local_dependencies_are_packaged(self):
        raw, manifest = p.archive_bytes()
        self.assertEqual(raw, p.archive_bytes()[0])
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            for name, digest in manifest["files"].items():
                self.assertEqual(hashlib.sha256(z.read(name)).hexdigest(), digest)
                self.assertFalse(name.startswith("../"))
            self.assertEqual(z.read("MECHANICAL_ETHICS.md"), p.reader.BOOK.read_bytes())
            for name in p.reader.owner.FIGURES:
                self.assertEqual(z.read("figures/" + name), (p.reader.ROOT / "figures" / name).read_bytes())
            self.assertIn("research/compact_core/CASES.md", z.namelist())
            self.assertIn("research/full_review/EDITORIAL_DECISION.md", z.namelist())
            self.assertIn(b"footer{overflow-wrap:anywhere}", z.read(p.ENTRY))
            self.assertEqual(json.loads(z.read("MANIFEST.json")), manifest)

    def test_missing_dependency_stops_instead_of_shipping_html_alone(self):
        original = p.reader.produce
        def missing():
            page, mapping = original()
            return page.replace(b"</footer>", b'<a href="missing-review-file.md">missing</a></footer>'), mapping
        with patch.object(p.reader, "produce", missing):
            with self.assertRaisesRegex(ValueError, "Missing/outside"):
                p.archive_bytes()

if __name__ == "__main__":
    unittest.main()
