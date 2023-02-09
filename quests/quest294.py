"""
Given a string, return the minimal number of parenthesis reversals needed to make balanced parenthesis.

For example:

solve(")(") = 2 Because we need to reverse ")" to "(" and "(" to ")". These are 2 reversals. 
solve("(((())") = 1 We need to reverse just one "(" parenthesis to make it balanced.
solve("(((") = -1 Not possible to form balanced parenthesis. Return -1.

Parenthesis will be either "(" or ")".

More examples in the test cases.

Good luck.

"""

def solve(s):
    if len(s) % 2:
        return -1
    while True:
        s2 = s.replace('()', '')
        if s2 == s:
            break
        s = s2
    return len(s) // 2 + s.count('(') % 2
