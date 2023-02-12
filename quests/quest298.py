"""
Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).

Heron's formula:
s∗(s−a)∗(s−b)∗(s−c)\sqrt{s * (s - a) * (s - b) * (s - c)}s∗(s−a)∗(s−b)∗(s−c)

where
s=a+b+c2s = \frac{a + b + c} 2s=2a+b+c​

Output should have 2 digits precision.
"""

from math import sqrt


def heron(a, b, c):
    s = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)
