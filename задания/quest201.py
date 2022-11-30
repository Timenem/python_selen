"""

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:
"""

def solve(s: str) -> str:
    lower = 0
    upper = 0
    for i in s:
        if i.islower():
            lower += 1
        else:
            upper += 1
    if lower >= upper:
        return s.lower()
    return s.upper()
