"""
Determine whether the sequence of elements items is
ascending such that each of its elements is strictly larger than (and not merely equal to) the preceding element.
Input: Iterable with ints.
Output: Bool.
# """

from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    k = 0
    prev_v = None
    for v in items:
        if v - 1 == prev_v:
            k += 1
            if k == 5:
                return True
        else:
            k = 1
        prev_v = v
    return False

if __name__ == '__main__':
    print("Example:")
    # print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_ascending([-5, 10, 99, 123456]) == True
    # assert is_ascending([99]) == True
    # assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    # assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

l = [1,-2,3,4,5,6,7]
flag = True
for i in l :
    if i  < l[i-1]:
        print('False')
        break
    else:
        print('True')