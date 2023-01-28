"""
 Lets cow say!

Our cow is young and can only say some of the words we teach it. Not only does it talk, but this cow can turn into the famous Tux ( wiki/Cowsay ) if we ask it nicely.
You are given some text and your function should format it in the "cows" speech. Let's examine the rules for this problem:

    The cow is always the same, only quote changes.
    Multiple spaces in a row are replaced by one space.
    The top border consists of underscore characters. It starts from a single space and ends before the border column.
    Each line of the quote consists of these parts: quote border(1), space(1), line(1-39), space(1), quote border(1).
    If line is less than 40 characters, it will fit into one string. The string is quoted in <> .
    If the line is greater than or equal to 40 characters, it should be split by these rules:
        Max line size is 39 chars. If any spaces are in the line, split it by the rightmost space (this space is removed from text) otherwise take the first 39 characters.
        After the split align all lines to same length by adding spaces at the end of each line.
        First line borders: /\
        Middle line borders: ||
        Last line borders: \/
    The bottom border consists of the minus sign. Has same length as top.
    cowsay console program has strange behavior in certain cases, this cases will not be tested here.

     _________________________________
    / Dog goes woof                   \
    | Cat goes meow                   |
    | Bird goes tweet                 |
    | And mouse goes squeek           |
    | Cow goes moo                    |
    | Duck goes quack                 |
    \ And the solution will go to you /
     ---------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    

What does the cow say?

Input: Text as a string.

Output: The result for the console as a string.

Hint: Read python docs ( 2.7 , 3.3 ) about formatting styles (str.format and %). Notice for r before the string. It is a raw string and they use different rules for interpreting backslash escape sequences. 
"""


COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

MAXCHAR = 39

def cowsay(text):
    while '  ' in text: text = text.replace('  ', ' ')
    lines = []
    line = ''
    for word in text.split(' '):
        if len(word) > MAXCHAR:
            if line:
                lines.append(line[:-1])
                line = ''
            while len(word) > MAXCHAR:
                lines.append(word[:MAXCHAR])
                word = word[MAXCHAR:]
            if word:
                line += word + ' '
        else:
            if len(line) + len(word) > MAXCHAR:
                lines.append(line[:-1])
                line = ''
            line += word + ' '
    if line:
        lines.append(line[:-1])
    n = len(lines)
    maxlen = max(len(line) for line in lines)
    s = '\n {}\n'.format('_' * (maxlen + 2))
    for i in range(n):
        border = ['||', '\\/', '/\\', '<>'][(2*(i == 0) + (i == n - 1))]
        s += '{} {:{}} {}\n'.format(border[0], lines[i], maxlen, border[1])
    return s + ' {}{}'.format('-' * (maxlen + 2), COW)
