"""The row statuses documented in docs/trip-planner-agents.md are accepted by check-restaurants."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import trip_restaurants  # noqa: E402


class RowStatusTest(unittest.TestCase):
    def test_documented_statuses_are_allowed(self):
        doc = (ROOT / "docs" / "trip-planner-agents.md").read_text(encoding="utf-8")
        line = next(l for l in doc.splitlines() if l.startswith("| `status` |"))
        values = re.sub(r"\([^)]*\)", "", line.split("|")[2])  # drop explanations in parentheses
        documented = set(re.findall(r"`([^`]+)`", values))
        self.assertEqual(documented, trip_restaurants.R_STATUS)


if __name__ == "__main__":
    unittest.main()
