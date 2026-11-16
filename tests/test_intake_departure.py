"""Route checks in tools/intake.py use the next Saturday 10:00 Spanish time, summer and winter."""
import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import intake  # noqa: E402


class NextSaturday(unittest.TestCase):
    def test_winter_is_0900_utc(self):
        self.assertEqual(intake._next_saturday(dt.date(2026, 11, 16)), "2026-11-21T09:00:00Z")

    def test_summer_is_0800_utc(self):
        self.assertEqual(intake._next_saturday(dt.date(2027, 7, 5)), "2027-07-10T08:00:00Z")

    def test_saturday_gives_the_following_saturday(self):
        self.assertEqual(intake._next_saturday(dt.date(2026, 11, 21)), "2026-11-28T09:00:00Z")


if __name__ == "__main__":
    unittest.main()
