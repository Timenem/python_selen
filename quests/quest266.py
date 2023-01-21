"""
It's 9 time!

I want to count from 1 to n. How many times will I use a '9'?

9, 19, 91.. will contribute one '9' each, 99, 199, 919.. wil contribute two '9's each...etc

Note: n will always be a positive integer.
Examples (input -> output)

8  -> 0
9  -> 1
10 -> 1
98 -> 18
100 -> 20


"""
def count_nines(n:int):
    counter = 0
    for i in range(0,n+1):
        if '9' in str(i):
            counter += str(i).count('9')
    return counter
