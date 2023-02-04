"""
Closure Counter

    Define the function counter that returns a function that returns an increasing value.
    The first value should be 1.
    You're going to have to use closures.

Example:

        const newCounter = counter();
        newCounter() // 1
        newCounter() // 2


"""


def counter():
    num = 0
    def d():
        nonlocal num
        num += 1
        return num
    return d
    
