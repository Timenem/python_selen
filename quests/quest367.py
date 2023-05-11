
from math import acos, asin, pi, sin


def tankvol(h, d, vt):
    # Radius of the vertical walls
    r = d / 2
    # Lenght of the tank
    l = vt / (pi * (r) ** 2)
    # Related angle with the height of the liquid
    ang = 2 * (acos(1 - (h / r)))
    # Area of the circular segment (required to calculate the liquid volume)
    a_seg = (r ** 2 / 2) * (ang - sin(ang))
    v = a_seg * l

    return int(v)
