from  collections import *
from string import  punctuation
def most_wanted(text: str) -> list:
    stringChar = "".join(i for i in text if i not in punctuation and i.isalpha())    
    s = Counter(stringChar.lower()).most_common()
    maxChar = s[0][1]
    answer = []
    for i in s:
        if i[1] == maxChar:
            answer.append(i[0])
    return answer


most_wanted("Helloo World")
if __name__ == '__main__':
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
    assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
    assert sorted(most_wanted("One")) == ["e", "n", "o"]
    # # , "All letter only once."
    assert sorted(most_wanted("Oops!")) == ["o"], "Don't forget about lower case."
    assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
    assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
    # print("Start the long test")
    assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."
    print("The local tests are done.")
