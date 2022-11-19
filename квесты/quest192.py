from string import ascii_lowercase
"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

def high(s: str):
    n = list(' ' + ascii_lowercase)
    d = {}
    for i in s.split(sep=' '):
        d[i] = sum([n.index(ch) for ch in i])
    return max(d,key=d.get)
