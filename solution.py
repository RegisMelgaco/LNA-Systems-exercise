import sys
import csv
from datetime import datetime, time
from functools import reduce
from typing import NamedTuple
from math import ceil
from enum import Enum


class Call(NamedTuple):
    duration: int
    caller: str
    callee: str


class CallCosts(Enum):
    BEFORE_THAN_FIVE_MINS = 0.05
    AFTER_THAN_FIVE_MINS = 0.02


class ConsoleMensages(Enum):
    MISSING_FILE_PATH = ('''
            Missing file path. Please execute the script as in the README file.
    ''')

    FILE_NOT_FOUND = "File not found."


# Returns the cost of a call of a given time in seconds. Appling rules 1 and 2.
def calc_call_cost(call: Call) -> float:
    time = call.duration
    charged_mins = ceil(time / 60)

    before_five_mins = 5 if charged_mins >= 5 else charged_mins
    after_five_mins = charged_mins - 5 if charged_mins > 5 else 0

    return (
        (before_five_mins * CallCosts.BEFORE_THAN_FIVE_MINS) +
        (after_five_mins * CallCosts.AFTER_THAN_FIVE_MINS)
        )


# Returns all given call, except thoes from the caller
# with highest call duration. Appling rule 3.
def get_charged_calls(calls: [Call]) -> [Call]:
    if len(calls) > 0:
        def keep_first_longest_call(last_longest_call, call):
            if call.duration > last_longest_call.duration:
                return call
            return last_longest_call

        longest_call = reduce(keep_first_longest_call, calls)

        def step_filter_charged_calls(call):
            return call.caller != longest_call.caller

        return filter(step_filter_charged_calls, calls)
    else:
        return []


# Returns the sum of the cost of the calls that should be charged.
# Appling rules 1, 2 and 3.
def calc_total_cost(calls: [Call]) -> float:
    charged_calls = get_charged_calls(list(calls))
    calls_cost = map(calc_call_cost, charged_calls)
    return sum(calls_cost)


# Converts a time(format HH:MM:SS) to a datetime object(datetime module).
def parse_timestr(time_str: str) -> datetime:
    splitted_str = map(int, time_str.split(":"))
    return datetime.combine(datetime.today(), time(*splitted_str))


def main():
    try:
        input_filepath = sys.argv[1]

        with open(input_filepath, newline='\n') as input_file:
            csv_reader = csv.reader(input_file, delimiter=";")

            def input_row_to_call(row: [str]) -> Call:
                call_duration = parse_timestr(row[1]) - parse_timestr(row[0])
                return Call(
                    call_duration.seconds,
                    row[2],
                    row[3]
                )

            calls = map(input_row_to_call, csv_reader)
            total_cost = calc_total_cost(calls)
            print("%.2f" % total_cost)
            return total_cost

    except IndexError as error:
        raise IndexError(ConsoleMensages.MISSING_FILE_PATH) from error

    except FileNotFoundError as error:
        raise FileNotFoundError(ConsoleMensages.FILE_NOT_FOUND) from error


if __name__ == '__main__':
    main()
