"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""



import  re
def to_camel_case(text:str):
    splitedText = ''
    if len(text) ==0 :
        return ''
    elif "-" and "_"  or "-" or "_" in text:
        splitedText = re.split("-|_",text)
    a = []
    for i in splitedText[1::]:
        if i[0].islower():
            a.append(i[0].upper()+i[1::])
        else:
            a.append(i)
    return (splitedText[0]+"".join(a))

def to_camel_case_second(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
