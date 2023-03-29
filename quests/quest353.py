"""
Extend the Math object (JS) or module (Ruby and Python) to convert degrees to radians and viceversa. The result should be rounded to two decimal points. Note that all methods of Math object are static.

Example:

math.degrees(math.pi) //180deg
math.radians(180) //3.14rad


"""
def degrees(rad):
    return '%gdeg' % round(180 * rad / math.pi, 2)

def radians(deg):
    return '%grad' % round(math.pi * deg / 180, 2)
