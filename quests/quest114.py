"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
"""




def get_middle(s):
    if len(s)%2 ==0:
        middle =int(len(s)/2)
        return(s[middle-1:middle+1])
    else:
        len(s) %2 !=0
        middle =int(len(s)/2)
        return(s[middle])
