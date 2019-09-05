import pytest
from unittest.mock import MagicMock
from unittest.mock import patch

from solution import Call, calc_call_cost, get_charged_calls, calc_total_cost
from solution import timestr_to_timeobj, main


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


class TestTimestrToTimeobj:

    time_obj = timestr_to_timeobj('01:02:03')

    def test_seconds(self):
        assert self.time_obj.second == 3

    def test_minuts(self):
        assert self.time_obj.minute == 2

    def test_hour(self):
        assert self.time_obj.hour == 1


class TestMain:

    def test_no_system_arg(self):
        with pytest.raises(IndexError):
            main()

    def test_invalid_path(self):
        import sys
        sys_argv = ['solution.py', 'dassadadsdasdsa']
        with patch.object(sys, 'argv', sys_argv):
            with pytest.raises(FileNotFoundError):
                main()
