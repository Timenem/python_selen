"""
 You are given some text potentially including sensible words. You should count how many words are included in the given text. A word should be whole and may be a part of other word. Text letter case does not matter. Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once.
For example, text - " How are sjfhdskfhskd you ?", words - ("how", "are", "you", "hello"). The result will be 3.
Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).
Output: The number of words in the text as an integer. 
"""


from string import  punctuation
import re 
def count_words(text: str, words: set) -> int:
    s = "".join([i for i in text.lower() if i not in punctuation])
    counter  = 0
    for i in words:
        if re.findall(i,s):
            counter+=1
    return counter
