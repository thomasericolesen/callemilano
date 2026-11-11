"""Shared helpers in tools/common.py."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import common  # noqa: E402


class MinutesTest(unittest.TestCase):
    def test_formats_in_records(self):
        cases = {
            "22 min": 22,
            "75 min": 75,
            "1 h 15 min": 75,
            "1 t 5 min": 65,
            "9 hours 21 min": 561,
            "2 hours 35 mins": 155,  # Google's own format; 'mins' used to be dropped
            "3 hours": 180,
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(common.minutes(text), expected)

    def test_unparsable(self):
        for text in (None, "", "ukendt", "about an hour"):
            with self.subTest(text=text):
                self.assertIsNone(common.minutes(text))


class FrontMatterTest(unittest.TestCase):
    def test_every_record_reads(self):
        for path in sorted(common.PLACES.glob("*.md")):
            with self.subTest(record=path.name):
                self.assertIn("slug", common.load_front_matter(path))


if __name__ == "__main__":
    unittest.main()
