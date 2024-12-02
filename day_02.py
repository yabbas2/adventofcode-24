from utils import read_file_lines
import builtins

input_file_path = "./day_02_input.txt"

INCREASING = 1
DECREASING = 2

LOWER_LIMIT = 1
UPPER_LIMIT = 3


def convert_report_str_to_list(reports: list) -> None:
    for idx in range(len(reports)):
        reports[idx] = list(map(int, reports[idx].split(" ")))


def is_safe_report(report: list, use_problem_dampener: bool) -> bool:
    assert len(report) >= 2, "report contains less than 2 elements"

    sub = report[0] - report[1]
    dir = INCREASING if sub < 0 else DECREASING

    for idx in range(0, len(report) - 1):
        sub = report[idx] - report[idx + 1]
        if (sub < 0 and dir == DECREASING) or (sub > 0 and dir == INCREASING) or abs(sub) > UPPER_LIMIT or abs(sub) < LOWER_LIMIT:
            if not use_problem_dampener:
                return False
            # use problem dampener
            for pos in range(idx - 1, idx + 2):  # idx-1, idx, idx+1
                if pos >= 0 and pos < len(report):
                    to_dampener_report = report.copy()
                    del to_dampener_report[pos]
                    dampener_result = is_safe_report(to_dampener_report, False)
                    if dampener_result:
                        return True
            return False

    return True


def parse_reports(reports: list, use_problem_dampener: bool = False) -> int:
    safe_count = 0
    unsafe_reports = list()
    for report in reports:
        if is_safe_report(report, use_problem_dampener):
            safe_count += 1
        else:
            unsafe_reports.append(report)
    return safe_count, unsafe_reports


if __name__ == "__main__":
    # read file lines
    reports = read_file_lines(input_file_path)
    # convert each line to list of numbers
    convert_report_str_to_list(reports)
    # parse each list (report) -> safe or unsafe
    safe_count1, unsafe_reports1 = parse_reports(reports)
    # print number of safe reports
    print(f"INFO: safe report count (without problem dampener) = {safe_count1}")
    # using problem dampener
    safe_count2, _ = parse_reports(unsafe_reports1, True)
    # print number of safe reports after problem dampener
    print(f"INFO: safe report count (with problem dampener) = {safe_count1 + safe_count2}")
