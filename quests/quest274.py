"""

ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10

This is a valid ISBN, because:

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

"""

def valid_ISBN10(isbn):
    if len(isbn) == 10 and isbn[0:9].isdigit() and (isbn[9].isdigit() or isbn[9] == 'X'):
        return sum([pos * (int(x) if x.isdigit() else 10) for pos, x in enumerate(str(isbn), 1)]) % 11 == 0
    return False
