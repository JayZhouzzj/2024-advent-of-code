import sys


def relaxed_is_safe(report):
    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
            return is_safe(report[:i] + report[i + 1 :]) or is_safe(
                report[: i + 1] + report[i + 2 :]
            )
        if i > 0 and (report[i] - report[i + 1]) * (report[i - 1] - report[i]) < 0:
            return (
                is_safe(report[:i] + report[i + 1 :])
                or is_safe(report[: i + 1] + report[i + 2 :])
                or is_safe(report[: i - 1] + report[i:])
            )
    return True


def is_safe(report):
    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
            return False
        if i > 0 and (report[i] - report[i + 1]) * (report[i - 1] - report[i]) < 0:
            return False
    return True


def solve(reports):
    return sum(1 if relaxed_is_safe(report) else 0 for report in reports)


if __name__ == "__main__":
    reports = []
    for line in sys.stdin.read().strip().split("\n"):
        levels = list(map(int, line.split()))
        reports.append(levels)
    print(solve(reports))
