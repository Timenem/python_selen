"""
 Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. Be careful with spaces - it's hard to see if you place two spaces instead one.

Input: An integer.

Output: String.

Examples:
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
1
2
3
4

How it is used: This concept may be useful for the speech synthesis software or automatic reports systems. This system can also be used when writing a chatbot by assigning words or phrases numerical values and having a system retrieve responses based on those values. 
"""

def first_tens(num: int) -> str:
    FIRST_TEN: dict[str, int] = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    k = list(FIRST_TEN.keys())
    v = list(FIRST_TEN.values())
    ind = v.index(num)
    return f"{k[ind]}"


def twenties(num: int) -> str:
    SECOND_TEN: dict[str, int] = {"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
                  "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
                  "eighteen": 18, "nineteen": 19, }
    k = list(SECOND_TEN.keys())
    v = list(SECOND_TEN.values())
    ind = v.index(num)
    return f"{k[ind]}"


def between_twenty_and_hundred(num: int) -> str:
    OTHER_TENS: dict[str, int] = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90, }
    first = int(str(num)[0])
    second = int(str(num)[1])
    if second == 0:
        k = list(OTHER_TENS.keys())
        v = list(OTHER_TENS.values())
        ind = v.index(first * 10)
        return k[ind]
    else:
        sec = first_tens(int(str(second)))
        k = list(OTHER_TENS.keys())
        v = list(OTHER_TENS.values())
        ind = v.index(first * 10)
        return f"{k[ind]} {sec}"


def hundreds(num: int) -> str:
    HUNDRED = 'hundred'
    first = f"{first_tens(int(str(num)[0]))} {HUNDRED}"
    second = int(str(num)[1])
    third = int(str(num)[2])
    if second == 0 and third == 0:
        return f"{first}"
    elif second == 0:
        return f"{first} {first_tens(third)}"
    elif int(str(num)[1::]) < 20:
        n = int(str(num)[1::])
        return f"{first} {twenties(n)}"
    elif int(str(num)[1::]) >= 20:
        n = int(str(num)[1::])
        return f"{first} {between_twenty_and_hundred(n)}"


def chekio(num: int) -> str:
    if num < 10:
        return first_tens(num)
    elif 10 <= num < 20:
        return twenties(num)
    elif 20 <= num < 100:
        return between_twenty_and_hundred(num)
    elif 100 <= num < 1000:
        return hundreds(num)
