import math
"""
Round any given number to the closest 0.5 step

I.E.

solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5

Round up if number is as close to previous and next 0.5 steps.

solution(4.75) == 5


"""

def solution(n):
    floor_num = math.floor(n)
    ceil_num = math.ceil(n)
    if n - floor_num < 0.25:
        return floor_num
    elif n - (floor_num + 0.5) >= 0.25:
        return ceil_num
    return floor_num + 0.5
