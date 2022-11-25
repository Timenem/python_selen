"""
Complete the function to find the count of the most frequent item of an array. 
You can assume that input is an array of integers.
For an empty array return 0
"""

from collections import Counter

def most_frequent_item_count(collection):
    if len(collection) ==0:
        return 0
    return Counter(collection).most_common(1)[0][1]
