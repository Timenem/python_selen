"""
 "Sometimes, zeros resemble very tasty donuts. And every time we finish a donut, we want another, and then another, and then another..."

You are given a list of integers. Your task in this mission is to double all the zeros in the given list (think about donuts ;-P).

Input: List.

Output: List. 
"""


def duplicate_zeros(a :list[int]):
    b =[]    
    for i in a :
        if i != 0:
            b.append(i)
        elif i ==0:
            b.extend([0,0])
    return b

