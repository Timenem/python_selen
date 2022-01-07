"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. 
Ignore numbers and punctuation
"""
def is_pangram(s):
    s.lower()
    l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letterCounter = {}
    for i in l  :
        letterCounter[i] =s.count(i)
    l = []
    x = [ l.append(i) for i in letterCounter.values() if i > 0 ]
    return (True if len(x) ==26 else False)
