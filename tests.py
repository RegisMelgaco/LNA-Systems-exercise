import unittest
from solution import calc_call_cost, calc_total_cost, get_charged_calls


class SolutionTestCase(unittest.TestCase):

    def test_calc_call_cost_less_and_equals_to_5min(self):
        call = {
            "time_delta": 0,
            "from": "1",
            "to": "2"
        }
        self.assertEqual(
            calc_call_cost(call),
            0
        )
        call['time_delta'] = 59
        self.assertEqual(
            calc_call_cost(call),
            0.05
        )
        call['time_delta'] = 60
        self.assertEqual(
            calc_call_cost(60),
            0.05
        )
        call['time_delta'] = 61
        self.assertEqual(
            calc_call_cost(call),
            0.10
        )
        call['time_delta'] = 5*60
        self.assertEqual(
            calc_call_cost(call),
            0.25
        )

    def test_calc_call_cost_more_than_5min(self):
        self.assertEqual(
            calc_call_cost(5*60+1),
            0.27
        )
        self.assertEqual(
            calc_call_cost(6*60-1),
            0.27
        )
        self.assertEqual(
            calc_call_cost(6*60),
            0.27
        )
        self.assertEqual(
            calc_call_cost(6*60+1),
            0.29
        )

    def test_get_charged_calls(self):
        calls = [
            {
                "time_delta": 1,
                "from": "1",
                "to": "2"
            }
        ]
        self.assertEqual(len(list(get_charged_calls(calls))), 0)

        calls = [
            {
                "time_delta": 1,
                "from": "1",
                "to": "2"
            },{
                "time_delta": 1,
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(len(list(get_charged_calls(calls))), 0)

        calls = [
            {
                "time_delta": 1,
                "from": "2",
                "to": "1"
            },{
                "time_delta": 1,
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(list(get_charged_calls(calls))[0]["from"], "1")

        calls = [
            {
                "time_delta": 1,
                "from": "2",
                "to": "1"
            },{
                "time_delta": 2,
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(list(get_charged_calls(calls))[0]["from"], "2")

    def test_calc_total_cost(self):
        calls = [
            {
                "time_delta": 1,
                "from": "1",
                "to": "2"
            }
        ]
        self.assertEqual(calc_total_cost(calls), 0)

        calls = [
            {
                "time_delta": 1,
                "from": "1",
                "to": "2"
            },{
                "time_delta": 1,
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(calc_total_cost(calls), 0)

        calls = [
            {
                "time_delta": 1,
                "from": "2",
                "to": "1"
            },{
                "time_delta": 1,
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(calc_total_cost(calls), 0.05)

        calls = [
            {
                "time_delta": 1,
                "from": "2",
                "to": "1"
            },{
                "time_delta": 2,
                "from": "1",
                "to": "2"
            },
        ]
        self.assertEqual(calc_total_cost(calls), 0.05)


if __name__ == '__main__':
    unittest.main()
