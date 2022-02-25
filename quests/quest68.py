"""
Our robots are always working to improve their linguistic skills.
For this mission, they research the Latin alphabet and its applications.
The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words.
These words are separated by whitespaces and punctuation marks.
Numbers are not considered as words in this mission (a mix of letters and digits is not a word either).
You should count the number of words (striped words) where the vowels with consonants are alternating; words that you count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- don't count those. Casing is not significant for this mission.
Input: A text as a string (unicode)
Output: A quantity of striped words as an integer.
Example:
checkio('My name is ...') == 3
checkio('Hello world') == 0
checkio('A quantity of striped words.') == 1
checkio('Dog,cat,mouse,bird.Human.') == 3
"""



def checkio(line: str) -> str:
    vowels = 'AEIOUY'
    consonants = 'BCDFGHJKLMNPQRSTVWXZ'
    cont = 0
    newline = ''
    for c in line:
        if c.upper() in vowels:
            newline += 'a'
        elif c.upper() in consonants:
            newline += 'b'
        elif not c.isalnum():
            newline += ' '
        else:
            newline += c
    for word in newline.split():
        if 'aa' not in word and 'bb' not in word and word.isalpha() and len(word)>1:
            cont += 1
    return cont


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
