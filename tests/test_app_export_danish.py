"""Danish text layer in tools/app_export.py: current translations apply, stale ones fall back to English."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import app_export  # noqa: E402


def place(price: str) -> dict:
    return {"id": "X-1", "name": "X", "category": "restaurant",
            "guide": {"summary": "Fish restaurant.", "practical": [{"label": "Pris", "text": price}],
                      "text_language": "en"}}


class DanishLayerTest(unittest.TestCase):
    def test_current_translation_is_applied(self):
        p = place("Mains 10-20 €.")
        sha = app_export.source_sha(p["guide"])
        da = {"X-1": {"source_sha": sha, "summary": "Fiskerestaurant.",
                      "practical": [{"label": "Pris", "text": "Hovedretter 10-20 €."}]}}
        applied, stale, todo = app_export.apply_danish([p], da)
        self.assertEqual((applied, stale, todo), (1, [], []))
        self.assertEqual(p["guide"]["text_language"], "da")
        self.assertEqual(p["guide"]["summary"], "Fiskerestaurant.")

    def test_changed_english_text_falls_back_to_english(self):
        old = place("Mains 10-20 €.")
        da = {"X-1": {"source_sha": app_export.source_sha(old["guide"]), "summary": "Fiskerestaurant.",
                      "practical": [{"label": "Pris", "text": "Hovedretter 10-20 €."}]}}
        new = place("Mains 12-24 €.")
        before = copy.deepcopy(new)
        applied, stale, todo = app_export.apply_danish([new], da)
        self.assertEqual((applied, stale), (0, ["X-1"]))
        self.assertEqual(new, before)
        self.assertEqual(todo[0]["previous_da"]["summary"], "Fiskerestaurant.")


if __name__ == "__main__":
    unittest.main()
