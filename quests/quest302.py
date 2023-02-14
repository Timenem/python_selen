"""
You are given two sorted lists, with distinct elements. Find the maximum path sum while traversing through the lists.

Points to consider for a valid path:

    A path can start from either list, and can finish in either list.
    If there is an element which is present in both lists (regardless of its index in the lists), you can choose to change your path to the other list.

Return only the maximum path sum.
"""

def max_sum_path(l1, l2):
    path = 0
    joins = sorted(list(set(set(l1).intersection(l2))))
    for j in joins:
        l1_path = l1[:l1.index(j)+1]
        l2_path = l2[:l2.index(j)+1]
        path += max(sum(l1_path), sum(l2_path))
        del l1[:l1.index(j)+1]
        del l2[:l2.index(j)+1]
    path += max(sum(l1), sum(l2))
    return path
