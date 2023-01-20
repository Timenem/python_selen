"""
A car is zooming through the streets! Maybe a bit too fast... Here come some more cars! Oh-No!!!
Instructions:

You need to find, if given a multi-line string road, whether the speeding car will crash or not.

A road will always contain the following:

    The speeding car, O='`o, who's driver is too scared to turn.
    The other cars, signified by X's. They will always be heading in the same direction as the car.

The function returns true/ True if there are X's ahead of the speeding car in the same lane, but returns false/False if the speeding car has already passed all of the car's in the lane, or if its lane is empty.
Examples:

These three will all return true (crash):
"""

def car_crash(road):
    return "O='`oX" in road.replace(' ', '')
