
from itertools import  groupby
def sum_consecutives(s:list)->list:
    return ([sum(i) for c ,i in groupby(s)])
