"""
 The function input is an array of datetime objects - this is the date and time of pressing the button. Your task is to determine how long the light bulb has been turned on.
Input: A list of datetime objects

Output: A number of seconds as an integer. 
"""

from datetime import datetime
def sum_light(d):
    seconds = []
    for x in range(0,len(d),2):
        splitedList = (d[x:x+2])
        duration = (splitedList[1] - splitedList[0])
        seconds.append(duration.total_seconds())
    return (int(sum(seconds)))
