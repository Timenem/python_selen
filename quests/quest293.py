"""
The hamming distance between a pair of numbers is the number of binary bits that differ in their binary notation.
Example

For a = 25, b = 87, the result should be 4

25: 00011001
87: 01010111

The hamming distance between these two would be 4 ( the 2nd, 5th, 6th, 7th bit ).
"""

def hamming_distance(a, b):
    str_a = "{0:b}".format(a)
    str_b = "{0:b}".format(b)
    dif_len = abs(len(str_b) - len(str_a))
    if len(str_a) <len(str_b) :
        str_a = str_a.zfill(len(str_b))
    if len(str_b) <len(str_a):
        str_b = str_b.zfill(len(str_a))
    counter = 0
    for ch_a, ch_b in zip(str_a,str_b):
        if ch_a != ch_b:
            counter +=1
    return counter
