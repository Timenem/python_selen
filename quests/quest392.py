def checkio(data:list[int]):
    f = lambda l: l[0] if len(l) == 1 else l[0] + f(l[1:])
    s  = f(data)
    return s
