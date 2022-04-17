"""
 Sort the numbers in an array. But the position of zeros should not be changed. 
"""

from typing import Iterable


def except_zero(items: list) -> Iterable:
    a= [i for i in range(len(items)) if items[i]==0]
    b= sorted([x for x in items if x!=0])
    [b.insert(i,0) for i in a ]
    return b

if __name__ == '__main__':
    except_zero(list([[5, 3, 0, 0, 4, 1, 4, 0, 7]]))
#  These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
