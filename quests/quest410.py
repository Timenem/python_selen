
from itertools import zip_longest

def checkio(text, word):

    lines = text.replace(" ", "").lower().split('\n')
    for row, line in enumerate(lines, start=1):
        index = line.find(word)
        if index != -1:
            row_start, row_end = row, row
            column_start, column_end = index + 1, index + len(word)
    transposed_array = [list(elem) for elem in zip_longest(*lines, fillvalue='')]
    transposed_lines = ["".join(elem) for elem in transposed_array]
    for row, line in enumerate(transposed_lines, start=1):
        index = line.find(word)
        if index != -1:
            column_start, column_end = row, row
            row_start, row_end = index + 1, index + len(word)

    return [row_start, column_start, row_end, column_end]
