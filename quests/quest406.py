
import math

def checkio(a, b, c):
    if max(a, b, c) >= a + b + c - max(a, b, c):
        return [0, 0, 0]
    elif max(a, b, c) == min(a, b, c):
        return [60, 60, 60]
    else:
        arc_cosinesX = math.acos((pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b))
        arc_cosinesX1 = math.acos((pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c))
        x = round(math.degrees(arc_cosinesX))
        x1 = round(math.degrees(arc_cosinesX1))
        x2 = 180 - (x + x1)
        return sorted([x, x1, x2])
