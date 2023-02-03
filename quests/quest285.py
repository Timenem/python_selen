"""
Implement zip_with

zip_with takes a function and two arrays and zips the arrays together, applying the function to every pair of values.
The function value is one new array.

If the arrays are of unequal length, the output will only be as long as the shorter one.
(Values of the longer array are simply not used.)

Inputs should not be modified.
"""

def zip_with(fn,a1,a2):
    return [fn(i, x) for i, x in zip(a1, a2)]
