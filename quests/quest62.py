"""
You are given a text, which contains different English letters and punctuation symbols.
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency , then return the letter which comes first in the Latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
Input: A text for analysis as a string.
Output: The most frequent letter in lower case as a string.
Example:
checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"
How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text.
For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear.
This is interesting stuff for language experts!
Precondition :
A text contains only ASCII symbols.
0 < len(text) ≤ 10 5
"""
# from  collections import  Counter
def checkio(text: str) -> str:
    global most
    total = 0
    lower = text.lower()
    for i in lower:
        if i.isalpha():
            if lower.count(i) > total:
                most = i
                total = lower.count(i)
            elif lower.count(i) == total:
                if i < most:
                    most = i
                    total = lower.count(i)

    return most
if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
