
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text

    def get_longest_word(self) -> str:
        """:return longest word """
        d = {}
        for i in self.text.split(sep=' '):
            d[i] = len(i)
        return max(d, key=d.get)

    def most_common_word(self) -> list[str]:
        """:return most common word"""
        word_list = Counter(self.text.split(sep=' '))
        return word_list.most_common(1)[0][0]

    def count_spec_symbols(self) -> int:
        """:return count symbols"""
        symbols = ['!', '?', ',', '.', '-']
        counter = 0
        for i in self.text:
            if i in symbols:
                counter += 1
        return counter

    def palindroms(self) -> str:
        """:return all palindroms"""
        palindroms = []
        for word in self.text.split(sep=' '):
            if word == word[::-1] and len(word) > 1:
                palindroms.append(word)
        return ", ".join(palindroms)
