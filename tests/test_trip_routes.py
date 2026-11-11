import datetime as dt
import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import trip_core as trip  # noqa: E402


class TripRouteTests(unittest.TestCase):
    def test_current_route_departure_converts_to_utc(self):
        now = dt.datetime(
            2026, 11, 5, 12, 30, 45, 987654, tzinfo=dt.timezone(dt.timedelta(hours=1))
        )

        self.assertEqual(trip.current_route_departure(now), "2026-11-05T11:30:45Z")

    def test_route_request_uses_the_supplied_departure_time(self):
        response = SimpleNamespace(returncode=0, stdout='{"routes":[{"duration":"312s"}]}')
        origin = {"lat": 36.5, "lon": -4.6}
        destination = {"lat": 36.6, "lon": -4.7}
        departure = "2026-11-05T11:30:45Z"

        with patch.object(trip.subprocess, "run", return_value=response) as run:
            result = trip.route_minutes_between(origin, destination, departure)

        self.assertEqual(result, 5)
        command = run.call_args.args[0]
        payload = json.loads(command[command.index("-d") + 1])
        self.assertEqual(payload["departureTime"], departure)
        self.assertIn("X-Goog-Api-Key: dummy", command)


if __name__ == "__main__":
    unittest.main()
