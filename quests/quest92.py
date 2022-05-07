"""
codewars 
Complete the function that

    accepts two integer arrays of equal length
    compares the value each member in one array to the corresponding member in the other
    squares the absolute value difference between those two values
    and returns the average of those squared absolute value difference between each member pair.

Examples

[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2
"""


def solution(array_a:[int], array_b:[int]):
    ar1 = np.array(array_a)
    ar2 = np.array(array_b)
    res = np.subtract(ar2 , ar1)
    # print(list(res))
    r = [abs(i) ** 2 for i in list(res) ]
    
    return (sum(r) / len(r))


def solution_2(array_a, array_b):
    answer = ((x-y)**2 for x ,y in zip(array_a,array_b))
    return sum(answer) / len(array_a)
