import unittest
from solution import calc_call_cost, calc_total_cost, get_charged_calls
from datetime import timedelta


class SolutionTestCase(unittest.TestCase):
    def test_calc_call_cost_less_and_equals_to_5min(self):
        self.assertEquals(
            calc_call_cost(timedelta(seconds=0)),
            0
        )
        self.assertEquals(
            calc_call_cost(timedelta(seconds=59)),
            0.05
        )
        self.assertEquals(
            calc_call_cost(timedelta(seconds=60)),
            0.05
        )
        self.assertEquals(
            calc_call_cost(timedelta(seconds=61)),
            0.10
        )
        self.assertEquals(
            calc_call_cost(timedelta(seconds=5*60)),
            0.25
        )

    def test_calc_call_cost_more_than_5min(self):
        self.assertEquals(
            calc_call_cost(timedelta(seconds=(5*60+1))),
            0.27
        )
        self.assertEquals(
            calc_call_cost(timedelta(seconds=(6*60-1))),
            0.27
        )
        self.assertEquals(
            calc_call_cost(timedelta(seconds=(6*60))),
            0.29
        )

    def test_get_charged_calls(self):
        