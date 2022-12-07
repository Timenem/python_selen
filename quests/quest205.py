"""
If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

If n is not an integer, return the string "None".

Ex:
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""

def dashatize(n:int):
    if type(n)!=int :
        return str(None)
    m= [int(i) for i in str(abs(n))]
    a = []
    for i in m :
        if i %2 !=0:
            a.append('-'+str(i)+'-')
        else:
            a.append(str(i))
    answer = "".join(a).replace('--','-')
    if answer.startswith('-'):
        answer = answer[1:]
    if answer.endswith('-'):
        answer = answer[:-1]
    return (answer)
