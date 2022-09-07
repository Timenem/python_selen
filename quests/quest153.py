"""
You will get two integers n (width) and m (height) and your task is to draw the following pattern.
Each line is seperated with a newline (\n)
Both integers are equal or greater than 1; no need to check for invalid parameters.

"""



def dot(width, height):
    sep = '+---' * width + '+'
    dot = '| o ' * width + '|'
    return '\n'.join([sep, dot] * height + [sep])
