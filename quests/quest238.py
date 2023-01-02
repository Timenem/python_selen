"""
You are given a string. Your function should return True if the string is a valid number (contains only digits and "+-." at proper places), otherwise - False. Look at the mask:
[+- ][zero or more digits][.][zero or more digits]
Of course, not all parts are necessary (but at least one digit part is!). For example, "+10." or "-.55" are valid numbers, where part equal 0 is omitted.
Input: A string.
Output: A boolean.
"""

def is_number(s:str):
    if 'e' in s :
        return False
    try:
        if float(s) or int(s):
            return True
        if not s.isdigit():
            return False
    except ValueError:
        return False
