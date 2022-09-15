"""
You are given a list/array which contains only integers (positive and negative). Your job is to sum only the numbers that are the same and consecutive. The result should be one list.

Extra credit if you solve it in one line. You can assume there is never an empty list/array and there will always be an integer.

Same meaning: 1 == 1

1 != -1
"""



from itertools import  groupby
def sum_consecutives(s:list)->list:
    return ([sum(i) for c ,i in groupby(s)])
