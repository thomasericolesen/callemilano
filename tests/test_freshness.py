import datetime as dt
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import freshness  # noqa: E402
from common import load_front_matter  # noqa: E402


class FreshnessTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copy(ROOT / "docs" / "places" / "granada.md", self.tmp / "granada.md")
        self.orig = freshness.PLACES
        freshness.PLACES = self.tmp

    def tearDown(self):
        freshness.PLACES = self.orig
        shutil.rmtree(self.tmp)

    def test_not_overdue_before_date(self):
        r = freshness.scan(dt.date(2026, 11, 14))
        self.assertEqual(r["overdue"], [])

    def test_overdue_set_back(self):
        nr = freshness.as_date(load_front_matter(self.tmp / "granada.md")["next_review_at"])
        day = nr + dt.timedelta(days=1)
        r = freshness.scan(day)
        self.assertEqual([x["slug"] for x in r["overdue"]], ["granada"])
        self.assertTrue(freshness.set_back("granada", day))
        d = load_front_matter(self.tmp / "granada.md")
        self.assertEqual(d["status"], "needs_fact_check")
        self.assertIn("review_overdue", [i["code"] for i in d["review_issues"]])
        self.assertFalse(freshness.set_back("granada", day))  # already set back

    def test_token_warning(self):
        self.assertTrue(freshness.scan(dt.date(2027, 1, 20))["import_token"]["renew_now"])
        self.assertFalse(freshness.scan(dt.date(2026, 11, 14))["import_token"]["renew_now"])


if __name__ == "__main__":
    unittest.main()
