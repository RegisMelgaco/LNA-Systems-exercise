from solution import Call, calc_call_cost, get_charged_calls, calc_total_cost


calls = [
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


class TestCalcCallCost:

    def test_0sec_duration(self):
        assert calc_call_cost(calls[0]) == 0

    def test_59sec_duration(self):
        assert calc_call_cost(calls[3]) == 0.05

    def test_60sec_duration(self):
        assert calc_call_cost(calls[4]) == 0.05

    def test_61sec_duration(self):
        assert calc_call_cost(calls[5]) == 0.10

    def test_5min_duration(self):
        assert calc_call_cost(calls[6]) == 0.25

    def test_5min_and_59sec_duration(self):
        assert calc_call_cost(calls[7]) == 0.27

    def test_6min_duration(self):
        assert calc_call_cost(calls[8]) == 0.27

    def test_6min_and_1sec_duration(self):
        assert calc_call_cost(calls[9]) == 0.29


class TestGetChargedCalls:

    def test_no_calls(self):
        assert list(get_charged_calls([])) == []

    def test_only_not_charged_calls(self):
        assert list(get_charged_calls(calls[0:2])) == []

    def test_dont_charge_first_biggest_caller(self):
        assert list(get_charged_calls(calls[1:3])) == [calls[2]]
        assert list(get_charged_calls([calls[2], calls[1]])) == [calls[1]]


class TestCalcTotalCost:

    def test_no_calls(self):
        assert calc_total_cost([]) == 0

    def test_with_no_charged_calls(self):
        assert calc_total_cost(calls[0:2]) == 0

    def test_multiple_callers(self):
        assert calc_total_cost(calls) == 0.32
