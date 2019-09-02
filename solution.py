import sys, csv
from datetime import datetime, time
from functools import reduce


def calc_call_cost(call_delta):
    if (call_delta.seconds > 5 * 60):
        return ((call_delta.seconds - 300) // 60 + 1) * 0.02 + 0.25
    else:
        return (call_delta.seconds // 60 + 1) * 0.05

def calc_total_cost(calls):
    longest_call = reduce(lambda longest_call, call:
            call if call['time_delta'] > longest_call['time_delta'] else longest_call,
            calls
        )
    not_charged_num = longest_call['from']
    charged_calls = filter(lambda call: call['from'] != not_charged_num, calls)
    return reduce(lambda acc, call: acc + calc_call_cost(call['time_delta']), charged_calls, 0)

def timestr_to_timeobj(str):
    splitted_str = map(int, str.split(":"))
    return datetime.combine(datetime.today(), time(*splitted_str))

def treat_input(row):
    return {
        "time_delta": timestr_to_timeobj(row[1]) - timestr_to_timeobj(row[0]),
        "from": row[2],
        "to": row[3]
    }

def main():
    try:
        input_filepath = sys.argv[1]

    except IndexError as error:
        raise IndexError(
            "Missing file path. Please execute the script as in the README file."
        ) from error

    try:
        with open(input_filepath, newline='\n') as input_file:
            csv_reader = csv.reader(input_file, delimiter = ";")
            total_cost = calc_total_cost(list(map(treat_input, csv_reader)))
            print("%.2f" % total_cost)

    except FileNotFoundError as error:
        raise FileNotFoundError(
            "File not found."
        ) from error


if __name__ == '__main__':
    main()
