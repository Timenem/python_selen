"""
You are given some string where you need to find its middle characters.
The string may contain one word, a few symbols or a whole sentence. 
If the length of the string is even, then you should return two middle characters,
but if the length is odd, return just one. For more details look at the Example. 
"""

from math import floor 
def middle(text):
    if len(text) <=2:
        return text
    elif len(text) <=4:
        return text[1:3]
    elif len(text) %2 ==0:
        indx = floor(len(text)/2)
        return text[indx-1:indx+1]
    else:
        indx = floor(len(text)/2)
        return  text[indx]

if __name__ == '__main__':
    # assert middle('example') == 'm'
    # assert middle('test') == 'es'
    assert middle("    few whitespaces   ") == "it"    
    # assert middle('very-very long sentence') == 'o'
    # assert middle('I') == 'I'
    # assert middle('no') == 'no'