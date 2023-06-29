def min_remove(A):
    A = sorted(A)
    sort_set = sorted(set(A))
    len_list = len(A)
    for i, x in enumerate(sort_set):
        for j in range(i + 1):
            if x <= sort_set[j] ** 2:
                len_list = min(len_list, A[::-1].index(x) + A.index(sort_set[j]))
    return len_list
