"""
In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
-- We sort by highest frequency to lowest frequency.
-- If two elements have same frequency, we sort by increasing value.


"""

def solve(arr):
    nums = set(arr)
    frequencies = {}
    for num in nums:
        if arr.count(num) in frequencies:
            frequencies[arr.count(num)].append(num)
        else:
            frequencies[arr.count(num)] = [num]
    output = []
    for count in sorted(frequencies.keys(), reverse=True):
        for num in sorted(frequencies[count]):
            output.extend([num for y in range(count)])
    return output
  
  
  
from collections import Counter

def solve(a):
    c = Counter(a)
    return sorted(a, key=lambda k: (-c[k], k))
