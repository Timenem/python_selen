"""
Write a function that takes two dates and two times as input and returns the total number of working hours between the two dates (incl. both).
Times representing the start and end of a workday. Working hours are defined as the time between the end and start times, Monday through Friday,excluding holidays. 
So the function also takes an argument that specifies a list of holidays to exclude (could be empty).
Time may have minutes. Convert them into float as minutes/60 with two-digits precision.
Input: Five arguments: two dates as strings, two times as strings, holidays as list of strings.
Output: Number of total working hours as integer or float. 
"""
import datetime

def working_hours(date1: str, date2: str, start_time: str, end_time: str, holy: list[str]) -> int | float:
    start_date = datetime.datetime.strptime(date1, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(date2, "%Y-%m-%d")
    day_delta = end_date.day - start_date.day
    start = datetime.date(year=start_date.year, month=start_date.month, day=start_date.day)
    start_work = datetime.datetime.strptime(start_time, "%H:%M")
    end_work = datetime.datetime.strptime(end_time, "%H:%M")
    hours_delta = end_work - start_work
    daterange = {}
    for day in range(day_delta + 1):
        date = (start + datetime.timedelta(days=day)).isoformat()
        weekday = (start + datetime.timedelta(days=day)).isoweekday()
        if date not in holy and weekday < 6:
            daterange[date] = hours_delta.seconds
    full_hours = sum(daterange.values()) / 3600
    if full_hours %1 ==0:
        return int(full_hours)
    else:
        return round(full_hours, 2)
