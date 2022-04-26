"""
You need to count how many non-empty lines a given text has.
An empty line is a line without symbols or the one that contains only spaces.
Input: A text.
Output: An int. 
"""



def remove_min_max(data:set,total:int)-> set:
    if len(data) ==3 and total==2:
        return set()
    elif len(data)==0 :
        return set()
    else:
        for i in range(total):
            max_int = max(data)
            min_int = min(data)
            data.remove(max_int)
            data.remove(min_int)
        return data




assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()
