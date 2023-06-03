
def arrange(s:list[int])->list[int]:
    t = []
    for i in range(len(s) // 2):
        if i % 2:
            t += [s[-i - 1], s[i]]
        else:
            t += [s[i], s[-i - 1]]
    if len(s) % 2:
        t += [s[len(s) // 2]]
    return t
