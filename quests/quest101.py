"""
Very simple, given an integer or a floating-point number, find its opposite.
1: -1
14: -14
-34: 34
"""

def opposite(number):
    if number<0:
        return  abs(number)
    else:
        return -number

print(opposite(-2.2345))
