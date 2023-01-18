"""
The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

    A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
    The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

"""

import re

def abbreviate(s: str):
    words_list = [word for word in re.findall(r'[A-Za-z]+|.', s) if len(word) > 1]
    words_and_len = dict(zip(words_list, [len(word) for word in words_list]))
    ans = []
    for word, word_len in words_and_len.items():
        first_char = word[0]
        last_char = word[-1]
        if word_len == 3:
            ans.append(word)
        else:
            ans.append(f"{first_char}{word_len - 2}{last_char}")
    return "".join(ans)
