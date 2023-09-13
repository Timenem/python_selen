from collections import Counter

def loneliest(strng):
    spaces = Counter()
    s = 0
    for c in strng.strip():
        if c.isspace():
            spaces[p] += 1
            s += 1
        else:
            spaces[c] += s
            p = c
            s = 0
    x = max(spaces.values())
    return [c for c in spaces if spaces[c] == x]
