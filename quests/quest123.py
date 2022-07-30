"""

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed

Return nil (or your language's equivalent) for invalid inputs.
Examples

For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

"""


def up_array(arr):
    if len(arr) < 1 :
        return None

    for i in arr:
        if len(str(i)) > 1 or i < 0:
            return None
    else:
        return [int(i) for i in str(int("".join([str(n) for n in arr]))+1)]
