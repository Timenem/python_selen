"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered
"""


from collections import Counter

def scramble(s1,s2):
    cnt = Counter(s1)
    cnt.subtract(Counter(s2))
    return (all(e >= 0 for e in cnt.values()))
