def what_is_the_time(time_in_mirror):
    hour = int(time_in_mirror[:2])
    minute = int(time_in_mirror[3:])

    if hour == 11:
        hour = 12
    elif hour == 12:
        hour = 11
    else:
        hour = 11 - hour
    if minute == 0:
        minute = 0
        hour += 1
    else:
        minute = 60 - minute
    return "{:02}:{:02}".format(hour, minute)


