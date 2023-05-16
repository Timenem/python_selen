def evaporator(content:int, evap_per_day:int, threshold:int):
    days = 0
    percent = 100
    while percent > threshold:
        percent = percent - percent* (evap_per_day/100)
        days +=1
    return days
