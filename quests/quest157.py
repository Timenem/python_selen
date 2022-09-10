"""
Given an integer n and two other values, build an array of size n filled with these two values alternating.
Examples

5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []

"""


def alternate(n,first,second):
    a = []
    while len(a) != n:
        a.append(first)
        if len(a) !=n:
            a.append(second)
        else:
            break
    return (a)
from itertools import cycle, islice

def alternate(n, *values):
    return [*islice(cycle(values), n)]
