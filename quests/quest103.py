
"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

def duplicate_count(text):
    d = dict.fromkeys(text)
    for i in text.lower():
        d[i.lower()] = text.count(i)
    aboweOne = [i for i in d.values() if i >1]
    return len(aboweOne)

