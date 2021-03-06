"""
Your mission is to sort the list by the frequency of numbers included in it. 
If a few numbers have an equal frequency - they should be sorted according to their natural order.
For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]
"""

from typing import List
import collections


def frequency_sorting(numbers: List[int]) -> List[int]:
    return sorted(sorted(numbers), key=numbers.count, reverse=True)



if __name__ == "__main__":
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [
        4,
        4,
        4,
        3,
        3,
        11,
        11,
        7,
        13,
    ], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [
        10,
        10,
        21,
        21,
        55,
        55,
        99,
        99,
    ], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
