def chmod_calculator(perm):
    READ = 'r'
    WRITE = 'w'
    EXECUTE = 'x'
    EMPTY = '-'
    d = dict.fromkeys(['user', 'group', 'other'], 0)
    for unit, p in perm.items():
        transform = (p.replace(READ, '4').replace(WRITE, '2').replace(EXECUTE, '1').replace(EMPTY, '0'))
        d[unit] = sum(map(int, transform))
    return "".join(list(str(i) for i in d.values()))
