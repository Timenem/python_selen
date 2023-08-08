def string_parse(string):
    res = []
    result = []
    if type(string) != str:
        return 'Please enter a valid string'
    for i in range(len(string)):
        if len(result)>1 and string[i] == result[-1] and string[i] == result[-2]:
            res.append(string[i])
        elif len(res)>0:
            result.append(f'[{"".join(res.copy())}]'); res.clear()
            result.append(string[i])
        else:
            result.append(string[i])
    if len(res)>0:
        result.append(f'[{"".join(res.copy())}]')
    return ''.join(result)
