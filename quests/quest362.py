"""
Your job is to implement a function which returns the last D digits of an integer N as a list.
Special cases:

    If D > (the number of digits of N), return all the digits.
    If D <= 0, return an empty list.

"""

def solution(n,d):
    if d <= 0:
        return []
    else:
        return ([int(i) for i in str(n)][-d:])
