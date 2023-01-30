"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array 
with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. I
f the number is prime return the string '(integer) is prime' 
(null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
