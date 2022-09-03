"""

 In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case;
    should contain at least 3 different letters (or digits) even if it is longer than 10

Input: A string.

Output: A bool. 
"""

def is_acceptable_password(s:str)->bool:
    one = len(s) > 6
    two = any(map(str.isdigit,s)) and not s.isdigit()
    three = len(s) > 9
    four = 'password' not in s.lower()
    five = len(set(s)) >=3
    return  one and (two or three) and four and five
