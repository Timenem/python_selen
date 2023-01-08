"""
Complete the function that accepts a valid string and returns an integer.

Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, then the result should be the sum of the numbers in the hex strings (ignore letters).
Examples

"Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
"Hello, World!"  ==> 91
"Forty4Three"    ==> 113



"""
from time import time
from functools import wraps
def check_time(func:callable):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time()
        r = func(*args,**kwargs)
        end = time() - start
        print(f"{'spent time :'} {end}")
        return r
    return wrapper

def hex_hash(code:str):
    m = list(code.encode('utf-8').hex())
    return sum([int(i) for i in m if i.isdigit()])
