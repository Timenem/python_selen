"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
"""

def to_underscore(string:str):
    a = ''
    if type(string) == int :
        return str(string)
    for i in string:
        if i.islower():
            a +=i
        elif i.isdigit():
            a +=i
        elif i.isupper():
            a +='_'+i.lower()
    return (a[1:])
