"""
In this kata, you should calculate type of triangle with three given sides a, b and c (given in any order).

If all angles are less than 90°, this triangle is acute and function should return 1.

If one angle is strictly 90°, this triangle is right and function should return 2.

If one angle more than 90°, this triangle is obtuse and function should return 3.

If three sides cannot form triangle, or one angle is 180° (which turns triangle into segment) - function should return 0.

Input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both).
"""

def triangle_type(a, b, c):
    a, b, c = sorted((a, b, c))
    if a + b <= c:
        return 0  #triangle cannot be made with given sides 
    answer = a ** 2 + b ** 2 - c ** 2
    if answer > 0:
        return 1 #acute triangle
    if answer == 0:
        return 2 #right triangle
    else:
        return 3 #obtuse triangle
