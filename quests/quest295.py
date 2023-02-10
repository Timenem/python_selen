"""
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
Examples

    "foefet" is an anagram of "toffee"

    "Buckethead" is an anagram of "DeathCubeK"


"""
def is_anagram(test:str, original:str):
    sort_test = sorted(test.lower())
    sort_original = sorted(original.lower())
    return sort_test == sort_original
