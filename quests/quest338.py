"""
Given a list of items, some of which may be duplicated, create and return a new Iterable that is otherwise the same as items, but only up to k occurrences of each element are kept, and all occurrences of that element after those first k are discarded. Note also the counterintuitive but still completely legitimate edge case of k == 0 that has a well defined answer of an empty list!
Input: A list and an integer.
Output: List or another Iterable (tuple, iterator, generator). "
"""
def remove_after_kth(items: list, k: int) -> list:
    result = []
    for item in items:
        if result.count(item) < k:
            result.append(item)
    return result
