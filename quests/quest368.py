from  math import factorial
def zeros(n:int):
    # s = (str(factorial(n)))
    s = str(factorial(n))
    counter = 0
    for i in s[::-1]:
        if i =='0':
            counter +=1
        else:
            break
    return counter
