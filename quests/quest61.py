"""
 Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). 
The words contains only letters. You should check if the string contains three words in succession .
For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string with words.
Output: The answer as a boolean.
Example:
checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False
"""


def checkio(words: str) -> bool:
    count = 0
    for  i in words.split():
        if i.isalpha():
            count +=1
        else:
            count = 0
        if count >= 3:
            return True
    return False

if __name__ == '__main__':
    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12") == False   
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
