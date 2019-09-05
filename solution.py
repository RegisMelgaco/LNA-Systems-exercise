import sys
import csv
from datetime import datetime, time
from functools import reduce
from typing import NamedTuple


class Call(NamedTuple):
    duration: int
    caller: str
    callee: str


# Returns the cost of a call of a given time in seconds. Appling rules 1 and 2.
def calc_call_cost(call: Call) -> float:
    call_delta = call.duration
    charged_mins = (call_delta // 60) + (1 if call_delta % 60 > 0 else 0)
    first_five_mins = 5 if charged_mins >= 5 else charged_mins
    last_five_mins = charged_mins - 5 if charged_mins > 5 else 0
    return (first_five_mins * 0.05) + (last_five_mins * 0.02)


# Returns all given call, except thoes from the caller
# with highest call duration. Appling rule 3.
def get_charged_calls(calls: [Call]) -> [Call]:
    def step(longest_call, call):
        if call.duration > longest_call.duration:
            return call
        return longest_call

    if len(calls) > 0:
        longest_call = reduce(step, calls)
        return filter(lambda call: call.caller != longest_call.caller, calls)
    else:
        return []


# Returns the sum of the cost of the calls that should be charged.
# Appling rules 1, 2 and 3.
def calc_total_cost(calls: [Call]) -> float:
    charged_calls = get_charged_calls(list(calls))
    return sum(map(calc_call_cost, charged_calls))


# Converts a time(format HH:MM:SS) to a datetime object(datetime module).
def timestr_to_timeobj(time_str: str) -> datetime:
    splitted_str = map(int, time_str.split(":"))
    return datetime.combine(datetime.today(), time(*splitted_str))


def main():
    try:
        print(sys.argv)
        input_filepath = sys.argv[1]

        with open(input_filepath, newline='\n') as input_file:
            csv_reader = csv.reader(input_file, delimiter=";")

            def input_row_to_call(row: [str]) -> Call:
                return Call(
                    (timestr_to_timeobj(row[1]) - timestr_to_timeobj(row[0])).seconds,
                    row[2],
                    row[3]
                )

            total_cost = calc_total_cost(map(input_row_to_call, csv_reader))
            print("%.2f" % total_cost)

    except IndexError as error:
        raise IndexError(
            '''
            Missing file path. Please execute the script as in the README file.
            '''
        ) from error

    except FileNotFoundError as error:
        raise FileNotFoundError(
            "File not found."
        ) from error


if __name__ == '__main__':
    main()
