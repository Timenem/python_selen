"""
Determine whether the sequence of elements items is ascending such that each of its elements is strictly larger than (and not merely equal to) the preceding element.
Input: Iterable with ints.
Output: Bool.
Example:
is_ascending([-5, 10, 99, 123456]) == True
is_ascending([99]) == True
is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
"""


from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    if len(items) ==1 or len(items)==0:
        return True
    if sorted(items) == items and items[0] < items[-1]:
        return True

    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")