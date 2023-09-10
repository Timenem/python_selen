from collections import Counter
def added_char(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    if len(set_s2) == len(set_s1):
        s1 =Counter(s1)
        s2 =Counter(s2)
        return list(s2 - s1)[0]
    else:
        a = set_s2 - set_s1
        return str(*a)
