import unittest
from solution import calc_call_cost, calc_total_cost, get_charged_calls, Call


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.calls = [
            Call(0, "1", "2"),
            Call(1, "1", "2"),
            Call(1, "2", "1"),
            Call(59, "1", "2"),
            Call(60, "1", "2"),
            Call(61, "1", "2"),
            Call(5*60, "1", "2"),
            Call(6*60 - 1, "1", "2"),
            Call(6*60, "3", "1"),
            Call(6*60 + 1, "1", "2"),
        ]

    def test_calc_call_cost_less_and_equals_to_5min(self):
        self.assertEqual(
            calc_call_cost(self.calls[0]),
            0
        )
        self.assertEqual(
            calc_call_cost(self.calls[3]),
            0.05
        )
        self.assertEqual(
            calc_call_cost(self.calls[4]),
            0.05
        )
        self.assertEqual(
            calc_call_cost(self.calls[5]),
            0.10
        )
        self.assertEqual(
            calc_call_cost(self.calls[6]),
            0.25
        )

    def test_calc_call_cost_more_than_5min(self):
        self.assertEqual(
            calc_call_cost(self.calls[7]),
            0.27
        )
        self.assertEqual(
            calc_call_cost(self.calls[8]),
            0.27
        )
        self.assertEqual(
            calc_call_cost(self.calls[9]),
            0.29
        )

    def test_get_charged_calls(self):
        self.assertEqual(len(list(get_charged_calls(self.calls[0:1]))), 0)

        self.assertEqual(len(list(get_charged_calls(self.calls[0:2]))), 0)

        self.assertEqual(
            list(get_charged_calls(self.calls[1:3]))[0].caller,
            "2"
            )

        self.assertEqual(
            list(get_charged_calls([self.calls[2], self.calls[1]]))[0].caller,
            "1"
            )

    def test_calc_total_cost(self):
        self.assertEqual(calc_total_cost([]), 0)
        self.assertEqual(calc_total_cost(self.calls[0:1]), 0)

        self.assertEqual(calc_total_cost(self.calls), 0.32)


if __name__ == '__main__':
    unittest.main()
