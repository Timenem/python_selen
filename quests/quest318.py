"""
In your class, you have started lessons about arithmetic progression. Since you are also a programmer, you have decided to write a function that will return the first n elements of the sequence with the given common difference d and first element a. Note that the difference may be zero!

The result should be a string of numbers, separated by comma and space.
"""

def arithmetic_sequence_elements(a, d, n):
    l = []
    if d > 0:
        while len(l) != n:
            l.append(a)
            a += d
    if d == 0:
        while len(l) != n:
            l.append(a)
    elif d < 0:
        while len(l) != n:
            l.append(a)
            a =a - abs(d)
    return str(l).replace('[', '').replace(']', '')
