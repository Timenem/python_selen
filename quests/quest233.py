"""
SBN stands for International Standard Book Number.

For more than thirty years, ISBNs were 10 digits long. On January 1, 2007 the ISBN system switched to a 13-digit format. Now all ISBNs are 13-digits long. Actually, there is not a huge difference between them. You can convert a 10-digit ISBN to a 13-digit ISBN by adding the prefix number (978) to the beginning and then recalculating the last, check digit using a fairly simple method.

Method
Take the ISBN ("1-85326-158-0").
Remove the last character, which can be a number or "X".
Add the prefix number (978) and a hyphen (-) to the beginning.
Take the 12 digits, then alternately multiply each digit from left to right by 1 or 3.
Add up all 12 numbers you got.
Take the number and perform a modulo 10 division.
If the result is 0, the check digit is 0. If it isn't 0, then subtract the result from 10. In this case, that is the check digit.
Add the check digit to the end of the result from step 3.
Return the 13-digit ISBN in the appropriate format:
"prefix number - original ISBN except the last character - check digit"
"978 - 1 - 85326 - 158 - 9"
"""
from itertools import cycle

def isbn_converter(isbn):
    prefix = "978"
    original = isbn[:-2].replace('-', '')
    temp = prefix + original
    c = cycle([1, 3])
    a = []
    for num in temp:
        a.append(int(num)* next(c))
    digit = 0 if sum(a) % 10 == 0 else 10 - sum(a) % 10
    return prefix + "-" + isbn[:-2] + "-" + str(digit)


def isbn_converter(isbn: str):
    isbn = '978-' + isbn[:-2]
    a = []
    for indx, num in enumerate([int(i) for i in isbn if i.isdigit()], start=1):
        if indx % 2 != 0:
            a.append(num * 1)
        elif indx % 2 == 0:
            a.append(num * 3)
    modulus_ten = sum(a) % 10
    if modulus_ten == 0:
        isbn += '-' + str(modulus_ten)
    elif modulus_ten != 0:
        modulus_ten = 10 - (modulus_ten % 10)
        isbn += '-' + str(modulus_ten)
    return (isbn)


