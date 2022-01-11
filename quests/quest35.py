"""
Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
"""

d = {"I": 1, "V": 5, "X": 10, "L": 50,
     "C": 100, "D": 500, "M": 1000}

roman_numerals = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9, "V":5,"IV":4,"I":1}

def roman_int(x):
    if x == "1":
        result = 0
        for k,v in roman_numerals.items():
            result += v * x.count(k)
            if len(k) == 2:
                result -= roman_numerals[k[0]] * x.count(k)
                result -= roman_numerals[k[1]] * x.count(k)
        print(result)

roman_int(1989)