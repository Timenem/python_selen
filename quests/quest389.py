
def del_none_and_zeros(d:dict):
    for k,v  in list(d.items()):
        if v ==0 or k =='':
            del d[k]
    return d
def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    d = dict.fromkeys([i[0] for i in data],0)
    for i in data:
        k = i[0]
        v = i[1]
        d[k] +=v
    return del_none_and_zeros(d)
