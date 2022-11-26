"""
 The task in this mission is as follows:

You are given an integer. If it consists of one digit, simply return its value. If it consists of two or more digits - add them until the number contains only one digit and return it.

Input: A int.

Output: A int.

Example:
assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6


"""


def sum_digits(num: int):
    a = sum([int(i) for i in list(str(num))])
    if len(str(a)) == 1:
        return a
    elif len(str(a)) > 1:
        return sum_digits(a)
    else:
        return 0
