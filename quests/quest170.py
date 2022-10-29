"""
The idea of the mission is very easy. You need to determine whether the given integer is a palindrome or not in base B. A number is a palindrome if it reads the same in both directions, for example 121 is a palindrome, and 122 is not. If the integer is a palindrome in base B, return True, if not, return False.
Input: Given Int and base B(Int).
Output: Bool.
"""


def int_palindrome(a, b):
    # Stores the reverse of a
    rev = 0
    # Stores the value of a
    a1 = a
    # Extract all the digits of a
    while (a1 > 0):
        # Generate its reverse
        rev = rev * b + a1 % b
        a1 = a1 // b
    return a == rev
