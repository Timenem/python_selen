def sum_diagonals(matrix:list[int]):
    forward = [m[indx] for indx,m in enumerate(matrix)]
    back = [m[indx] for indx,m in enumerate(matrix[::-1])]
    return sum(back + forward)
