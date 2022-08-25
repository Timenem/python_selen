"""

According to ISO 8601, the first calendar week (1) starts with the week containing the first thursday in january. Every year contains of 52 (53 for leap years) calendar weeks.

Your task is to calculate the calendar week (1-53) from a given date. For example, the calendar week for the date 2019-01-01 (string) should be 1 (int).

Good luck 👍

See also ISO week date and Week Number on Wikipedia for further information about calendar weeks.

On whatweekisit.org you may click through the calender and study calendar weeks in more depth.

heads-up: require(xxx) has been disabled
"""



from datetime import  datetime
import  datetime
def get_calendar_week(date_string):
    date_split = datetime.datetime.strptime(date_string,"%Y-%m-%d")
    a = datetime.date(date_split.year,date_split.month,date_split.day).isocalendar()[1]
    print(a)
    return a
