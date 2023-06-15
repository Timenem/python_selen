
from textwrap import wrap

def text_formatting(text, width, style):
    lines = wrap(text, width=width)
    if style == 'l':
        return '\n'.join(lines)
    if style == 'c':
        return '\n'.join(' '*((width-len(line))//2) + line for line in lines)
    if style == 'r':
        return '\n'.join(line.rjust(width) for line in lines)
    for i in range(len(lines) - 1):
        gap, big_blocks = divmod(width - len(lines[i]), lines[i].count(' '))
        lines[i] = lines[i].replace(' ', ' '*(gap+1)) \
                           .replace(' '*(gap+1), ' '*(gap+2), big_blocks)
    return '\n'.join(lines)
