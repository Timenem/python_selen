
"""
 Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.
But how does the Excel column numbering actually work? Well, the column number is like decimal number, but with base (radix) 26 and "digits" A-Z. Read more about number bases. Let's look at the exact numbers:
Excel   Decimal
    A   1
    Z   26
The 1-"digit" numbers have ended. 2-"digits" numbers start from double first "digit" and go to double last one:
Excel   Decimal
    A   1
    Z   26
   AA   27
   AZ   52
   BA   53
   BZ   78
   CA   79
   ZZ   702
Now it's turn for 3-"digit" numbers...
Input: String.
Output: Integer.
Examples:
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701
"""
from string import ascii_uppercase


def column_number(name: str) -> int:
    l = list(' ' + ascii_uppercase)
    for first in ascii_uppercase:
        for last in ascii_uppercase:
            ch = first + last
            l.append(ch)

    return l.index(name)
