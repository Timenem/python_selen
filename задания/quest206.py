import time
def time_checker(func:callable):
    def wrap(arg):
        a = time.perf_counter()
        res = func(arg)
        end = time.perf_counter()
        print(f"{'function time'}:{end-a}")
        return res
    return wrap
@time_checker
def capitalization(s:str):
    even = ''.join([i.upper() if s.index(i)%2==0 else i.lower()  for i in s])
    odd = ''.join([i.lower() if s.index(i)%2==0 else i.upper()  for i in s])
    print( [even,odd])
