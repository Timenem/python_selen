def adjacent_letters(line: str) -> str:
    stack = []
    for s in line:
        if stack and stack[~0] == s:
            stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)
