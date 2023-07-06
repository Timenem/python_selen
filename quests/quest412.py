from itertools import cycle
def make_looper(string:str):
    c = cycle(string)
    return lambda next(c)
