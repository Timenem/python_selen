from  collections import Counter
def number_of_pairs(l:list[str]):
    answer = {}
    if len(l) ==0:
        return 0
    else:
        d = dict(Counter(l))
        for name,key in d.items():
            if key %2 ==0:
                answer[name] = key
            else:
                answer[name] = key-1
    return int(sum(answer.values()) / 2)
