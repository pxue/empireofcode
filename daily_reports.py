# https://github.com/Checkio-Game-Missions/checkio-empire-dailies-reports.git

import string
from datetime import datetime, timedelta as td
def count_reports(full_report, from_date, to_date):

    # generate the map of values
    # from A1-Z9
    ingots = []
    for ch in string.ascii_uppercase:
        for i in range(1, 10):
            ingots.append("%s%d" % (ch, i))

    parsed = {}

    ingot_sum = 0
    for line in full_report.split("\n"):
        # each day
        date, values = line.split(" ")

        parsed[date] = 0
        for v in values.split(","):
            parsed[date] += (ingots.index(v) + 1)

        if from_date <= date <= to_date:
            ingot_sum += parsed[date]

    return ingot_sum
