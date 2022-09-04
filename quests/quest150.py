""""
 Your task in this mission is to truncate a sentence to a length that does not exceed a given number of characters.

If the given sentence already is short enough, you don't have to do anything to it. But if it needs to be truncated, the omission must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.

Input: Two arguments:

    one-line sentence as a string;
    max length of the truncated sentence as an int.

Output: The shortened sentence plus the ellipsis (if required) as a one-line string. 
""""


import textwrap


def cut_sentence(line: str, length: int) -> str:
    if len(line) <= length:
        return line
    else:
        return textwrap.shorten(line, width=length,placeholder="", break_long_words=False) + "..."
