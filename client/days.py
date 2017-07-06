monthSize = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
yearSize = 365

def dateToDays(now, next):
    days = 0

    yearOverflow = next['y'] - now['y']
    monthOverflow = next['m'] - now['m']

    days += yearSize * yearOverflow

    if monthOverflow > 0:
        for i in range(now['m'], now['m'] + monthOverflow):
            days += monthSize[i-1]

    days += next['d'] - now['d']

    return days


def addMonth(now, add):
    ret = now
    monthSizeCur = monthSize[ now["m"] - 1 ]

    ret["d"] += int(monthSizeCur / add)
    while ret["d"] > monthSizeCur:
        ret["d"] -= monthSizeCur
        ret["m"] += 1
        if ret["m"] > 12:
            ret["m"] = 1
            ret["y"] += 1

        monthSizeCur = monthSize[ now["m"] - 1 ]

    return ret
