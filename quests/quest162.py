"""
Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. 
Each piece of land will be marked with 'X' 
while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land.
"""


def land_perimeter(arr):
    p = 0
    for row in arr + zip(*arr):
        current = list(row)
        p += sum(a != b for a, b in zip(['O'] + current, current + ['O']))
    return f"{'Total land perimeter: '}{p}"

