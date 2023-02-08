"""
The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of positions where the input strings do not match.
Examples:

a = "I like turtles"
b = "I like turkeys"
Result: 3

a = "Hello World"
b = "Hello World"
Result: 0

a = "espresso"
b = "Expresso"
Result: 2

"""

def hamming(a, b):
    len_a = len(a)
    len_b = len(b)
    dif_len = abs(len_a-len_b)
    if len_a < len_b :
        a = str(a).zfill(dif_len+len_a)
    elif len_b < len_a:
        b=str(b).zfill(dif_len+len_b)
    counter = 0
    for char_a , char_b in zip(a,b):
        if char_a != char_b:
            counter +=1
        elif char_a == char_b :
            counter +=0
    return (counter)
