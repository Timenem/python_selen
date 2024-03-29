"""
Complete the function to create backronyms. Transform the given string (without spaces) to a backronym, using the preloaded dictionary and return a string of words, separated with a single space (but no trailing spaces).

The keys of the preloaded dictionary are uppercase letters A-Z and the values are predetermined words, for example:

dictionary["P"] == "perfect"

Examples

"dgm" ==> "disturbing gregarious mustache"

"lkj" ==> "literal klingon joke"

"""

#preloaded variable: "dictionary"



def make_backronym(acronym):
    dictionary = {'A': 'awesome', 'B': 'beautiful', 'C': 'confident', 'D': 'disturbing', 'E': 'eager',
                  'F': 'fantastic', 'G': 'gregarious', 'H': 'hippy', 'I': 'ingestable', 'J': 'joke', 'K': 'klingon',
                  'L': 'literal', 'M': 'mustache', 'N': 'newtonian', 'O': 'oscillating', 'P': 'perfect',
                  'Q': 'queen', 'R': 'rant', 'S': 'stylish', 'T': 'turn', 'U': 'underlying', 'V': 'volcano',
                  'W': 'weird', 'X': 'xylophone', 'Y': 'yogic', 'Z': 'zero'}
    a = ''
    for i in acronym.upper():
        a += ' '+dictionary[i]
    return (a.lstrip())
