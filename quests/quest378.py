
from  collections import Counter
def long_repeat(s:str):
    ans = []
    for num, ch in enumerate(s) :
        try:
            if ch == s[num+1]:
                ans.append(ch)
            else:
                ans.append(ch+'*')
        except IndexError:
            ans.append(ch)
    a = max([len(sub) for sub in "".join(ans).split('*')])
    return (a)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
