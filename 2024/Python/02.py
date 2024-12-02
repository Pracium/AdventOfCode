import math


def check(dif, direction):
    if 1 <= abs(dif) <= 3 and direction == math.copysign(1, dif):
        return True
    return False


def check_report(report):
    direction = None
    for i in range(1, len(report)):
        dif = int(report[i - 1]) - int(report[i])

        if direction is None:
            direction = math.copysign(1, dif)

        if not check(dif, direction):
            return False

        direction = math.copysign(1, dif)
    else:
        return True


data = open('02.txt', 'r').read().split('\n')

safe_reports = 0
safe_pd_reports = 0

for report in data:
    report = report.split(" ")

    if check_report(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            if check_report(report[:i] + report[i + 1:]):
                safe_pd_reports += 1
                break

print(safe_reports)
print(safe_reports + safe_pd_reports)
