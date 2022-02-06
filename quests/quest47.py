"""
You are given two dates as an array with three numbers - a year, month and day.
For example: 19 April 1982 will be (1982, 4, 19).
You should find the difference in days between the given dates.
For example between today and tomorrow = 1 day.
The difference will always be either a positive number or zero, so don't forget about the absolute value.
Input: Two dates as tuples of integers.
Output: The difference between the dates in days as an integer.
"""

from datetime import datetime

def days_diff(a:tuple, b:tuple):
    a = f"{a[0]}-{a[1]}-{a[2]}"
    b = f"{b[0]}-{b[1]}-{b[2]}"
    d1 = datetime.strptime(a,"%Y-%m-%d")
    d2 = datetime.strptime(b,"%Y-%m-%d")
    return abs((d2 - d1).days)


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    assert days_diff((1, 1, 1), (9999, 12, 31)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
