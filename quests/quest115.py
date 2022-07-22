"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

"""


from string import ascii_lowercase

def alphabet_position(text):
    answer = ""
    a = "`"+ascii_lowercase
    for i in text.lower():
        if i in a :
            answer += " "+str(a.index(i))
    return (answer.strip())

