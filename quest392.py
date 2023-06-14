def changing_direction(elements: list[int]) -> int:

    dirs = []
    for i, j in zip(elements, elements[1:]):
        if j > i and (not dirs or dirs[-1] == '-'):
            dirs.append('+')
        elif j < i and (not dirs or dirs[-1] == '+'):
            dirs.append('-')
    return len(dirs) - bool(dirs)

  
def delete_duble(elements:list[int]):
    indx = 0
    while indx < len(elements):
        if elements[indx] == elements[indx-1]:
            elements.pop(indx)
            indx -= 1
        else:
            indx += 1
    return elements
