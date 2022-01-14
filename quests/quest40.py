"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!
Here's the deal:
    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
"""


s = "codewars is nice"
def generate_hashtag(s):
    if len(s) ==0:
        return False

    elif len(s) != 0 : 
        m = [i.capitalize() for i in s.split()]
        m.insert(0,"#")
        m = "".join(m).replace(" ","")
        return m if len(m) <140 else False 

generate_hashtag(s)
