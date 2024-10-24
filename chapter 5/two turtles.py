def race(v1, v2, range):
    if v1 >= v2:
        return [-1, -1, -1]
    hour = range / (v2 - v1)
    hours = int(hour)
    minute = (hour - hours) * 60
    minutes = int(minute)
    second = (minute - minutes) * 60
    seconds = round(second)
    return [hours, minutes, seconds]
print(race(720, 850, 70))