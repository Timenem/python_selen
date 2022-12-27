"""
Description:

We want to generate a function that computes the series starting from 0 and ending until the given number.

Example:
Input:

> 6
Output:

0+1+2+3+4+5+6 = 21

Input:

> -15
Output:

-15<0

Input:

> 0
Output:

0=0
"""
def show_sequence(n):
    if n <0 :
        return f"{n}<0"
    elif n == 0:
        return f"{n}=0"
    answ  =sum([num for num in range(0,n+1)])
    str_ans = " ".join([str(i) for i in range(0,n+1)]).replace(' ','+')+' = '+str(answ)
    return (str_ans)
