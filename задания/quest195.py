"""
Nicola believes that Sophia calls Home too much and her phone bill is much too expensive. He took the bills for Sophia's calls from the last few days and wants to calculate how much did it cost.

The bill is represented as an array with information about the calls. Help Nicola to calculate the cost for each of Sophia’s calls. Each call is represented as a string with date, time and duration of the call in seconds in the following format:
"YYYY-MM-DD hh:mm:ss duration"
The date and time here are the start of the call.
Space-Time Communications Co. has several rules on how to calculate the cost of calls:

First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Calls count to the day when they began. For example, if a call was started 2014-01-01 23:59:59, then it should be counted to 2014-01-01;
For example:

"""
def total_cost(calls):
    db = Counter()
    for call in calls:
        day, time, duration = call.split()
        db[day] += (int(duration) + 59) // 60
    return sum(m if m < 100 else 2 * m - 100 for m in db.values())
