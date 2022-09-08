"""
 Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.

Output: a boolean.

Example: 
"""



import re
def is_all_upper(text:str)->bool:
    if len(text) == 0:
        return False
    if all([i.isupper() for i in re.split(r"\s+",text)]):
        return True
    else:
        return False

