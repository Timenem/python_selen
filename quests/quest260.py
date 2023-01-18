"""
For a given string s find the character c (or C) with longest consecutive repetition and return:
(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.
For empty string return:
('', 0)
In JavaScript: If you use Array.sort in your solution, you might experience issues with the random tests as Array.sort is not stable in the Node.js version used by CodeWars. This is not a kata issue.
"""
from itertools import groupby
from collections import OrderedDict


def longest_repetition(chars):
    if chars == '':
        return '', 0
    else:
        chars_list = ["".join(grp) for ch, grp in groupby(chars)]
        d = OrderedDict(zip(chars_list, [len(i) for i in chars_list]))
        sort_dict_list = (sorted(d.items(), key=lambda kv: kv[1], reverse=True))
        ch, val = sort_dict_list[0]
        a = (*set(ch), val)
        return a

