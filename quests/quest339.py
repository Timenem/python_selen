"""
In another Kata I came across a weird sort function to implement. We had to sort characters as usual ( 'A' before 'Z' and 'Z' before 'a' ) except that the numbers had to be sorted after the letters ( '0' after 'z') !!!

(After a couple of hours trying to solve this unusual-sorting-kata I discovered final tests used **usual** sort (digits **before** letters :-)

So, the unusualSort/unusual_sort function you'll have to code will sort letters as usual, but will put digits (or one-digit-long numbers ) after letters.
"""
def unusual_sort(array):
    text = []
    tver = []
    xar = []
    for i in array:
        if isinstance(i,str) and i.isalpha():text.append(i)
        elif isinstance(i,str) and i.isdigit():xar.append(i)
        else: tver.append(i)
    text.sort()
    for i in range(0,10):
        if i in tver:
            f = tver.count(i)
            for j in range(0,f):
                text.append(i)
            f1 = xar.count(str(i))
            for j in range(0,f1):
                text.append(str(i))
        elif str(i) in xar:
            f = xar.count(str(i))
            for j in range(0,f):
                text.append(str(i))
    return  text
