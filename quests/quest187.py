"""
Your task, is to create NxN multiplication table, of size provided in parameter.
for example, when given size is 3:
1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size: int) -> list[list[int]]:
    outer_list = []
    for i in range(1, size + 1):
        inner_list = []
        for j in range(1, size + 1):
            inner_list.append(i * j)
        outer_list.append(inner_list)
    return outer_list
