import unittest
from solution import calc_call_cost, calc_total_cost, get_charged_calls
from datetime import timedelta
import random
import string


class SolutionTestCase(unittest.TestCase):
    def test_calc_call_cost_less_and_equals_to_5min(self):
        self.assertEqual(
            calc_call_cost(timedelta(seconds=0)),
            0
        )
        self.assertEqual(
            calc_call_cost(timedelta(seconds=59)),
            0.05
        )
        self.assertEqual(
            calc_call_cost(timedelta(seconds=60)),
            0.05
        )
        self.assertEqual(
            calc_call_cost(timedelta(seconds=61)),
            0.10
        )
        self.assertEqual(
            calc_call_cost(timedelta(seconds=5*60)),
            0.25
        )

    def test_calc_call_cost_more_than_5min(self):
        self.assertEqual(
            calc_call_cost(timedelta(seconds=(5*60+1))),
            0.27
        )
        self.assertEqual(
            calc_call_cost(timedelta(seconds=(6*60-1))),
            0.27
        )
        self.assertEqual(
            calc_call_cost(timedelta(seconds=(6*60))),
            0.29
        )

    def test_get_charged_calls(self):
        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            }
        ]
        self.assertEqual(len(list(get_charged_calls(calls))), 0)

        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            },{
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(len(list(get_charged_calls(calls))), 0)

        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "2",
                "to": "1"
            },{
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(list(get_charged_calls(calls))[0]["from"], "1")

        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "2",
                "to": "1"
            },{
                "time_delta": timedelta(seconds=2),
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(list(get_charged_calls(calls))[0]["from"], "2")

    def test_calc_total_cost(self):
        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            }
        ]
        self.assertEqual(calc_total_cost(calls), 0)

        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            },{
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(calc_total_cost(calls), 0.05)

        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "2",
                "to": "1"
            },{
                "time_delta": timedelta(seconds=1),
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(calc_total_cost(calls), 0.05)

        calls = [
            {
                "time_delta": timedelta(seconds=1),
                "from": "2",
                "to": "1"
            },{
                "time_delta": timedelta(seconds=2),
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(calc_total_cost(calls)["from"], 0.05)


if __name__ == '__main__':
    unittest.main()
