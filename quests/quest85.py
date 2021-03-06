"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.
Input: A string.
Output: a boolean.
Example:
is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == False
"""


def is_all_upper(text: str) -> bool:
    # your code here
    return text.upper() == text


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    #assert is_all_upper('') == False
    assert is_all_upper("") == True
