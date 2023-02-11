"""
A new task for you!

    You have to create a method, that corrects a given time string.
    There was a problem in addition, so many of the time strings are broken.
    Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.

Examples

"09:10:01" -> "09:10:01"  
"11:70:10" -> "12:10:10"  
"19:99:99" -> "20:40:39"  
"24:01:01" -> "00:01:01"  

"""


from datetime import datetime as dt
from time import strftime
from time import gmtime
def time_correct(s:str)->str:
    if s == '':
        return ''
    elif isinstance(s,dt):
        return None
    elif s == None:
        return None
    else :
        try:
            a = s.split(':')
            hours = int(a[0])
            minutes = int(a[1])
            seconds = int(a[2])
            total_hours = hours*3600
            total_minutes = minutes * 60
            total_seconds = total_hours + total_minutes + seconds
            st = strftime("%H:%M:%S",gmtime(total_seconds))
            return st
        except Exception:
            return None
