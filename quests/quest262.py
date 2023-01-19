"""
Return true when any odd bit of x equals 1; false otherwise.

Assume that:

    x is an unsigned, 32-bit integer;
    the bits are zero-indexed (the least significant bit is position 0)

"""

def any_odd(x):
    return int("1" in f"{x:032b}"[::2])
