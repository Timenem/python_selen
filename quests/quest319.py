"""
In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in the string. If there is no such letter in the string, then the function should return -1. If the letter occurs only once in the string, then -1 should also be returned.

Examples:

second_symbol('Hello world!!!','l') --> 3
second_symbol('Hello world!!!', 'A') --> -1

"""
def second_symbol(s:str, symbol:str):
    if s.count(symbol) ==0 or s.count(symbol) ==1:
        return -1
    else:
        return [num for num ,ch in enumerate(s) if ch == symbol ][1]
