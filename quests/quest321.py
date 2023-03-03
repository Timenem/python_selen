"""
 You are given a list of integers, which are elements of arithmetic progression - the difference between the consecutive elements is constant. But this list is unsorted and one element is missing...good luck!

Input: List of integers.

Output: Integer.

Examples:
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

"""

def reverse_ascending(items):
    if len(items) < 2:
        return items
    res = []
    tmp = []
    for i in range(len(items)-1):
        if items[i] >= items[i+1]:
            if i > 0 and items[i] > items[i-1]:
                tmp.append(items[i])
                tmp.reverse()
                res.extend(tmp)
                tmp = []
            else:
                res.append(items[i])
        else:
            tmp.append(items[i])
        if i == len(items)-2:
            if items[i] < items[i + 1]:
                tmp.append(items[i+1])
                tmp.reverse()
                res.extend(tmp)
                tmp = []
            else:
                res.append(items[i+1])
    if tmp:
        tmp.reverse()
        res.extend(tmp)
    return res
